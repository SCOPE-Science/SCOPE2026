# Review of the exact binary four-by-four decomposition-fiber census

## Correctness

PASS. The claim concerns a finite 65,536-element matrix ring, not an infinite extrapolation. The direct count of 1,680,172 admissible ordered pairs, a separate integer Walsh convolution, and the primary rational canonical 34-class census agree. The structural identities \(|\mathcal N|=316\) and \(|\mathcal T|=5317\) independently check cardinalities. The critical centralizer formula, matrix multiplication, row-major encoding, tripotency, and noncommuting summands are specified in RESULT.md and implemented in the packaged `verify.py`; its output and generated `class_table.csv` were tested.

## Originality

PASS, with historical-priority qualification. The April 2026 Danchev–García–Gómez Lozano work establishes broad potent decomposition existence; the November 18, 2026 Phuc–Danchev paper explicitly establishes existence in order four but does not give individual fiber sizes. The 2021 potent-plus-square-zero paper also addresses existence. The closest indexed three-by-three binary diagonalizable-plus-square-zero census concerns a stricter first-summand identity and different order, and does not imply the 25-level spectrum. Published and indexed searches did not find a covering multiplicity table. Older or unindexed specialist computations remain a residual risk.

## Mathematical value

PASS. Order four is the first matrix dimension after the cubic obstruction where universal tripotent-plus-square-zero decomposability holds. Distinguishing how many presentations occur at that boundary gives a natural sharp rigidity invariant: precisely one similarity class of 1,120 nonzero matrices has three presentations, and the rank-three idempotent class of 120 matrices uniquely attains the largest nonidentity fiber of 162. The 25-level spectrum and complete 34-class refinement are exact classification data rather than a selected example or a routine restatement of existence.

## Limitations

No claim is made for larger matrices or other fields; the finite certificate is exhaustive only in the explicitly stated domain. Historical priority remains provisional and independent audit is unperformed.

Self-review: passed. Independent audit: not yet performed.
