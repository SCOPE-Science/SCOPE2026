# Scientific review: four-child Hadamard Haar endpoint theorem

## Correctness
PASS. The four local Walsh signs produce exactly eight signed \((3,-1,-1,-1)\) patterns. Conditioning on the continuing child yields an exact two-action Bellman recurrence with the correct level factor \(4\), and the invariant window \(|u|\le1\) closes under its successors. The comparison of its affine branches is an explicit nonnegative product; the coefficient recurrence determines the all-depth norm. The optimizer count follows from strictness at intermediate states and ties at initial and final states. The complete proof, normalization and equality arguments appear in `RESULT.md`, with finite independent diagnostics in `verify.py`.

## Originality
PASS, with bibliographic limitation. The closest compared work on ordinary Haar transforms addresses restricted weak-type bounds, not the four-child signed endpoint constant. The 2014 higher-rank Haar work addresses weighted \(L^p\) basis unconditionality; its available abstract does not decide the precise finite endpoint question, and full-text comparison was unavailable. The fair binary finite-depth result yields the same expression but on a genuinely different local signed-kernel family, so it cannot directly settle the four-child theorem. Searches for four-adic Walsh–Haar signed endpoint constants and aliases did not locate a dominating statement. Failed searches alone do not establish novelty, and the older higher-rank literature remains a residual risk.

## Value
PASS. Four-child Hadamard contrasts are a canonical vector-valued multiresolution basis. The exact equality of the sharp endpoint constant to two stages of the classical dyadic Haar basis is not forced by equality of spans, because the allowed signed kernels differ. The exact all-depth law and optimizer multiplicity measure the effect of orthogonal packetization on extreme coefficient-sign sensitivity. They provide a reproducible benchmark for comparison with other contrast choices, beyond a small-depth table.

## Closest literature and limitations
Osękowski, DOI 10.1155/2013/646012, publicly available December 5, 2013. Kazarian–Kazaryan–San-Antolín, arXiv:1410.4888, first publicly available October 17, 2014. Full-text access to the latter was unsuccessful and equivalent older calculations cannot be excluded. The result is restricted to the specified real uniform four-child Walsh/Haar basis and complete finite generations.

Self-review: passed. Independent audit: not yet performed.
