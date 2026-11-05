#!/usr/bin/env python3
"""Address-level examples, not traced historical glyph reproductions."""
import json

DIGRAPH_ALPHABET = 'ABCDEFGHILMNOPQRSTVZ'
SLOT_ALPHABET = 'abcdefghilmnopqrstuxyz'
SLOT_ORDER = ('top_left', 'top_right', 'bottom_left', 'bottom_right')


def digraph_addresses(text):
    if len(text) % 2 or any(c not in DIGRAPH_ALPHABET for c in text):
        raise ValueError('Unsupported letter or odd length; no implicit padding')
    return [dict(pair=text[i:i+2], column_letter=text[i], row_letter=text[i+1],
                 column_index_1based=DIGRAPH_ALPHABET.index(text[i])+1,
                 row_index_1based=DIGRAPH_ALPHABET.index(text[i+1])+1)
            for i in range(0, len(text), 2)]


def four_slot_addresses(text):
    letters = text.lower().replace('v','u')
    if len(letters) % 4 or any(c not in SLOT_ALPHABET for c in letters):
        raise ValueError('Unsupported letter or incomplete block; no implicit padding')
    return [dict(zip(SLOT_ORDER, letters[i:i+4])) for i in range(0,len(letters),4)]


def run_example():
    assert len(DIGRAPH_ALPHABET) == 20
    assert len(SLOT_ALPHABET) == 22
    text = 'MVLTISCL'
    pair = digraph_addresses(text)
    slots = four_slot_addresses(text)
    assert [(x['column_index_1based'],x['row_index_1based']) for x in pair] == [(11,19),(10,18),(9,17),(3,10)]
    assert slots[0] == dict(top_left='m',top_right='u',bottom_left='l',bottom_right='t')
    assert ''.join(x['column_letter']+x['row_letter'] for x in pair) == text
    assert ''.join(block[s] for block in slots for s in SLOT_ORDER).upper().replace('U','V') == text
    refused=0
    for function, bad in [(digraph_addresses,'ABC'),(digraph_addresses,'AX'),
                          (four_slot_addresses,'ABC'),(four_slot_addresses,'ABCK')]:
        try: function(bad)
        except ValueError: refused += 1
    assert refused == 4
    return dict(schema='public-domain-period-address-demo-v1',
        source='Giambattista della Porta, De furtivis literarum notis, 1563, Book II, chapters XIII-XIV',
        source_pages=dict(grid='https://archive.org/details/defvrtivislitera00port/page/n118/mode/1up',
            worked_text='https://archive.org/details/defvrtivislitera00port/page/n119/mode/1up',
            four_slots='https://archive.org/details/defvrtivislitera00port/page/n121/mode/1up'),
        printed_pages=[90,91,93],public_example_prefix=text,
        digraph=dict(alphabet=DIGRAPH_ALPHABET,addresses=pair),
        four_slots=dict(alphabet=SLOT_ALPHABET,normalization='V to u for printed mark labels',addresses=slots),
        invalid_input_refusals=refused,
        verification_scope='Address selection and inverse address replay only. Original cell glyphs and complete printed composite examples have not been independently traced or compared pixel by pixel.',
        historical_glyph_reproduction_verified=False)


if __name__ == '__main__':
    print(json.dumps(run_example(),indent=2))
