# Scientific review: diagonal degree-seven Padé reciprocal positivity

## Correctness — PASS

The claimed polynomial agrees term by term with the normalized exponential Padé denominator formula. The exact rational verifier certifies seven disjoint complex root disks using Rouché inequalities, all relevant derivative and modulus bounds, strict positivity of indices 0 through 31, and a rational residue majorant that is strictly below the positive-real-root contribution for index 32 and every later index. The analytic partial-fraction argument extends the certificate to every nonnegative index. Assumptions and simple-root counting are explicit.

## Originality — PASS, with priority caveat

Fasi–Higham (2019) state the odd-degree positivity assertion as a conjecture. Scardino (2026) gives a conditional eventual-positivity criterion and exact off-diagonal counterexamples but explicitly leaves diagonal positivity open. The nearby degree-three and degree-five cases concern different denominator orders and do not imply the order-seven result. Search comparisons included diagonal degree seven, reverse Bessel synonyms, reciprocal coefficients, the source paper, and numerical-analysis records. Dunster et al. (2021) treat polynomial and zero computation rather than coefficientwise positivity of the inverse. An unindexed older theorem about inverse reverse-Bessel series is a residual historical-priority risk; novelty is not inferred merely from missing search hits.

## Value — PASS

The exact seventh-order diagonal case is the smallest odd diagonal denominator order beyond the separately treated degree-three and degree-five cases. It is a commonly relevant matrix-exponential Padé order and a natural unsolved instance of the diagonal question singled out by the source literature. Proving all indices, not an arbitrary finite table, and independently certifying the needed dominant-pole property provide a substantive finite-order mathematical boundary for a conjecture tied to matrix exponential error bounds. The result deliberately does not claim a general theorem for every odd order or an implementation guarantee.

## Limits and closest literature

The method of partial-fraction positivity and the recurrence themselves precede this result; the new work consists of exact seven-disc certification and complete coverage of the diagonal \([7/7]\) instance. Published historical coverage may be broader than indexed searches reveal. The independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
