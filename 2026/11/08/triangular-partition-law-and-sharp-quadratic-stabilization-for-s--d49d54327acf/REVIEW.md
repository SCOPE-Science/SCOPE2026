# Scientific review

## Correctness — PASS
The proof gives a bijection between length-\(n\) words with exactly \(k>0\) scattered \(001\) occurrences and a triangular-number partition profile together with three nonnegative length fillers. The profile's largest index is unique; its gap count is exactly \(\sum_j\binom j2 r_j\). Exactly one profile reaches degree \(k+2\), with all remaining degrees at most \(k+1\); this yields the all-length generating function, the polynomial for \(n\ge k\), and the one-unit discrepancy at \(k-1\). Reconstructed calculations and independent enumeration/streaming tests support all boundary cases. Infinite validity is established symbolically, not inferred from computation.

## Originality — PASS (best-knowledge, residual risk)
Bruda's 2026 Theorem 1.4 implies eventual degree two but gives no all-\(k\) triangular numerator or sharp length threshold for this symmetry class. Menon–Singh provide formulas only for occurrence counts through four; Tian gives general constructive algorithms. The existing fixed-frequency result for scattered \(010\) has a different three-run pattern and linear, not quadratic, degree. published-finding corpus searches, web literature queries, and accessible prior-claim comparisons returned no equivalent or stronger exact sharp onset. These observations support originality, but unknown unindexed literature or implicit specializations in general algorithms remain genuine priority risks; a search absence does not prove novelty.

## Value — PASS
The result identifies the exact length distribution for every positive frequency in the remaining nonalternating nonconstant length-three pattern class. The full generating numerator gives a natural triangular-partition interpretation of the leading coefficient, while a uniform optimal onset improves substantially on an unspecified eventual-polynomial statement. This is a motivated infinite family of exact enumerations, not a computational table or merely a degree restatement.

## Closest literature and limitations
Bruda (2026), arXiv:2607.02578; Menon–Singh (2023), arXiv:2306.07870; Tian (2025), arXiv:2507.03205. Applicability is restricted to scattered positive-frequency binary patterns equivalent to \(001\) under reversal/complementation. External validation and priority certification are not asserted.

Self-review: passed. Independent audit: not yet performed.
