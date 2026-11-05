# Synthetic composition demo

A standard-library Python demonstration by Chen-Yu Chu, under the MIT license.
The main experiment is entirely synthetic. A separate address replay uses a
cited public-domain example. No private transcription, image, recovered
plaintext, or private research data is included. These examples have not undergone external scholarly review.

Run `python3 composition_demo.py --out results.json`.

The pair experiment compares an independently encoded pair with an arbitrary
whole-cell key. Both use exactly the same visible component pairs. Five
combinations are held out while every component is observed during training.
Known-plaintext component fitting succeeds on the factorized example and
refuses the conflicting whole-cell example. This supervised synthetic check
does not turn geometry alone into a decipherment method.

The slot experiment exhaustively checks all 1,296 four-letter messages over
a six-letter synthetic alphabet, with fixed order top-left, top-right,
bottom-left, bottom-right. The symbols are abstract IDs, not reproductions
of any historical marks. Invalid lengths and unsupported letters are refused.

The graph functions report pair coverage and four-cycle counts. A dense
Cartesian graph is compatible with both kinds of key, so these statistics
cannot by themselves establish which cipher generated an inscription.

Historical scope: a whole-cell digraph substitution and a four-position
compositional alphabet are different mechanisms. This synthetic program does
not claim to reproduce a historical printed glyph. Such a claim would require
an independently transcribed alphabet and comparison with the original example.

`python3 period_address_demo.py` separately replays the addresses for the
public-domain opening `MVLTISCL` in Porta's 1563 example. For the 20-by-20
table, the first letter selects the column and the second selects the row.
The expected one-based addresses are `(11,19), (10,18), (9,17), (3,10)`.
For the four-slot method, the first block uses `m,u,l,t` in top-left,
top-right, bottom-left, bottom-right order; the printed `u` corresponds to
the plaintext `V`. The next block uses `i,s,c,l`.

Sources: Porta, *De furtivis literarum notis* (1563), Book II, chapters
XIII-XIV: [printed p. 90](https://archive.org/details/defvrtivislitera00port/page/n118/mode/1up),
[p. 91](https://archive.org/details/defvrtivislitera00port/page/n119/mode/1up),
[p. 93](https://archive.org/details/defvrtivislitera00port/page/n121/mode/1up).
This is an **address-level control**. It does not validate the shapes of the
400 table glyphs or reproduce the complete original composite-glyph example.
