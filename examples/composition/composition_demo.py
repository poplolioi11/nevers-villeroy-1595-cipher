#!/usr/bin/env python3
"""Synthetic encoders and a geometry-only identifiability counterexample."""
import argparse
import itertools
import json
from collections import defaultdict


def graph_statistics(pairs):
    pairs = list(pairs)
    edges = set(map(tuple, pairs))
    left = {a for a, _ in edges}
    right = {b for _, b in edges}
    neighbors = {a: {b for x, b in edges if x == a} for a in left}
    rectangles = 0
    for a, b in itertools.combinations(left, 2):
        common = len(neighbors[a] & neighbors[b])
        rectangles += common * (common - 1) // 2
    return dict(observations=len(pairs), left_types=len(left), right_types=len(right),
                edges=len(edges), possible_edges=len(left) * len(right),
                density=len(edges)/(len(left)*len(right)) if left and right else None,
                four_cycles=rectangles)


def structural_holdout(train, holdout):
    edges = set(map(tuple, train))
    left = {a for a, _ in edges}
    right = {b for _, b in edges}
    out = dict(observations=0, seen_pair=0, new_pair_known_components=0,
               unknown_component=0)
    for a, b in holdout:
        out['observations'] += 1
        if (a, b) in edges:
            out['seen_pair'] += 1
        elif a in left and b in right:
            out['new_pair_known_components'] += 1
        else:
            out['unknown_component'] += 1
    return out


def fit_known_component_map(examples):
    """Known-plaintext test only. Refuse any inconsistent component map."""
    candidates = [defaultdict(set), defaultdict(set)]
    for glyph, plaintext in examples:
        for axis in (0, 1):
            candidates[axis][glyph[axis]].add(plaintext[axis])
    conflicts = sum(len(values) != 1 for axis in candidates for values in axis.values())
    if conflicts:
        return dict(status='INCONSISTENT', conflicting_components=conflicts), None
    maps = [{component: next(iter(values)) for component, values in axis.items()}
            for axis in candidates]
    return dict(status='SUPPORTED', conflicting_components=0), maps


def decode_component_pair(glyph, maps):
    if maps is None or any(glyph[i] not in maps[i] for i in (0, 1)):
        return None
    return tuple(maps[i][glyph[i]] for i in (0, 1))


SLOTS = ('top_left', 'top_right', 'bottom_left', 'bottom_right')


def encode_slots(letters, alphabet_to_mark):
    if len(letters) != 4 or any(c not in alphabet_to_mark for c in letters):
        raise ValueError('Exactly four supported letters are required')
    return dict(zip(SLOTS, (alphabet_to_mark[c] for c in letters)))


def decode_slots(glyph, alphabet_to_mark):
    inverse = {v: k for k, v in alphabet_to_mark.items()}
    if len(inverse) != len(alphabet_to_mark) or set(glyph) != set(SLOTS):
        raise ValueError('Ambiguous key or missing slot')
    return ''.join(inverse[glyph[slot]] for slot in SLOTS)


def run_demo():
    n = 5
    pairs = [(f'row{r}', f'column{c}') for r in range(n) for c in range(n)]
    positive = []
    negative = []
    for r in range(n):
        for c in range(n):
            glyph = (f'row{r}', f'column{c}')
            positive.append((glyph, (chr(65+(2*r+1)%n), chr(65+(3*c+2)%n))))
            # An invertible cell permutation: each output depends on both parts.
            negative.append((glyph, (chr(65+(r+c)%n), chr(65+(r+2*c)%n))))
    assert len({p for _, p in negative}) == n*n
    train_indices = [r*n+c for r in range(n) for c in range(n) if (r+c)%n != 0]
    hold_indices = [i for i in range(n*n) if i not in train_indices]
    results = {}
    for name, data in [('factorized', positive), ('whole_cell_nonfactorized', negative)]:
        train = [data[i] for i in train_indices]
        hold = [data[i] for i in hold_indices]
        status, maps = fit_known_component_map(train)
        predictions = [decode_component_pair(g, maps) for g, _ in hold]
        results[name] = dict(fit=status, train_count=len(train), holdout_count=len(hold),
            holdout_covered=sum(p is not None for p in predictions),
            holdout_exact=sum(p == truth for p, (_, truth) in zip(predictions, hold)),
            geometry=graph_statistics(g for g, _ in data))
    assert results['factorized']['holdout_exact'] == 5
    assert results['whole_cell_nonfactorized']['fit']['status'] == 'INCONSISTENT'
    assert results['factorized']['geometry'] == results['whole_cell_nonfactorized']['geometry']
    _, maps = fit_known_component_map([positive[i] for i in train_indices])
    assert decode_component_pair(('new_row', 'column0'), maps) is None
    symbols = dict(zip('ABCDEF', ('mark2', 'mark5', 'mark1', 'mark4', 'mark0', 'mark3')))
    slot_cases = [''.join(x) for x in itertools.product('ABCDEF', repeat=4)]
    for letters in slot_cases:
        assert decode_slots(encode_slots(letters, symbols), symbols) == letters
    refused = 0
    for letters in ['ABC', 'ABCDE', 'ABCG']:
        try:
            encode_slots(letters, symbols)
        except ValueError:
            refused += 1
    assert refused == 3
    return dict(schema='synthetic-composition-demo-v1', seed=None,
        design='deterministic exhaustive fixtures; no fit to observed ciphertext',
        pair_experiments=results,
        heldout_geometry=structural_holdout([pairs[i] for i in train_indices],
                                            [pairs[i] for i in hold_indices]),
        unseen_component_abstention=True,
        slot_roundtrips=len(slot_cases), slot_invalid_refusals=refused,
        conclusion='Identical geometry is compatible with both factorized and arbitrary whole-cell keys. Geometry alone cannot identify plaintext factorization.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out')
    args = parser.parse_args()
    result = json.dumps(run_demo(), indent=2, ensure_ascii=False) + '\n'
    if args.out:
        with open(args.out, 'w') as f:
            f.write(result)
    else:
        print(result, end='')
