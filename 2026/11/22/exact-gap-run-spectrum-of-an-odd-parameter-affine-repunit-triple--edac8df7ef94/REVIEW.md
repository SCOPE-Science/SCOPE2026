# Self-review

## Correctness — PASS
For odd \(a\), the residue-to-coin map \(2t\bmod a\) is a bijection. Minimizing \(2y+4z\) at fixed \(t=y+3z\) gives \(2(t-\lfloor t/3\rfloor)\); its monotonicity proves the Apéry minimum for each residue, including possible representations with larger \(t\). Exact even/odd residue heights then force a single terminal even-length gap run per row and singleton internal gaps. Each terminal length occurs as many times as one explicit cost increment; the genus minus their total lengths gives the isolated-gap quasipolynomial. No unproved infinite step relies on computation. The provided verifier corroborates all odd \(a\le251\), across 1,785,903 gaps.

## Originality — PASS within inspected evidence
The principal preprints by Liu, Xin, Ye and Yin (arXiv:2306.03459, arXiv:2306.10738) already cover Apéry sets and Frobenius/genus for the same affine-repunit family. These known membership results are not claimed as new. Explicit formulae for all maximal missing-integer run lengths with a period-three two-or-zero frequency and the corresponding quadratic isolated-gap census were not asserted in the inspected texts. The closest same-generator minimal-presentation result determines toric binomials, not gap runs; the closest full run-spectrum result treats two generators. The unit-shift repunit isolated-gap box treats another increment. A potentially implicit evaluation in earlier Apéry literature remains the main priority risk; non-discovery does not prove uniqueness.

## Mathematical value — PASS
This is a complete, sharp, natural invariant of a two-parameter-derived semigroup family at the fixed increment-two slice. It distinguishes isolated holes from long missing intervals, identifies all impossible gap lengths, and gives exact counts without enumerating each parameter individually. The period-three missing-length mechanism is explained by the coin-cost plateau, not by a superficial arithmetic fit.

## Boundaries and verification
All statements concern odd parameters and the three specified generators; even parameters and other increments remain outside scope. The proof is mathematical and the finite checker is corroborative. The evidence has not undergone independent external validation.

Self-review: passed. Independent audit: not yet performed.
