# Scientific review: Pascal-row nondivisibility correlations

## Correctness — PASS

The proof starts from the Lucas/Fine base-\(p\) product for nondivisible binomial coefficients, establishes the exact finite cyclic mixed-moment carry recursion, and uses the exact mean and variance to identify its centered limiting Pearson kernel. Its recursion is terminating and rational for every fixed shift. Symbolic identities show that the one-digit shift \(1\) is strictly largest, the one-digit shift \(2\) strictly second-largest, and every displacement having two nonzero base-\(p\) digits lies strictly below the second level. The row-sum contraction for repeatedly occurring digit \(1\) proves a zero infimum without a zero correlation. Exact-rational symbolic factorization independently verified the critical polynomial inequalities. The included checker compares direct Pascal-triangle rows and exact cyclic mixed moments against digit and carry predictions for several odd primes. These finite checks do not establish the universal theorem by themselves.

## Originality — PASS within the material inspected

Lane (2023, arXiv:2309.12942) studies the same row-count statistic and one-point residue distributions, without stating the fixed-shift Pearson correlation kernel or both sharp extremal levels. Rowland (2017, arXiv:1704.05872) supplies a known generalization of the underlying one-row digit product, not shifted two-row correlations. Mathonet–Rigo–Stipulanti–Zénaïdi (2022, arXiv:2201.06636) encode entire Pascal rows as integers rather than studying the row-count correlation. The closest indexed mathematical result addresses the binary case \(p=2\) and does not imply the odd-prime hierarchy. Search and implication checks found no identified stronger theorem. The possibility of an unindexed equivalent digital-sequence result is a residual originality risk, not evidence of uniqueness.

## Mathematical value — PASS

At a natural number-theoretic object—the count of entries in Pascal's triangle nonzero modulo an odd prime—the finding supplies a complete rational two-point carry computation, a strict ranking of every displacement into two maximizer tiers and the rest, and an unattained zero infimum. The equality families \(p^k\) and \(2p^k\) are structural rather than arbitrary finite examples. It extends the study from marginal row frequencies to precise dependence between rows.

## Limits and comparison

The limit is taken at a **fixed** displacement while complete prime-power cutoffs grow. No finite-cutoff maximizer theorem, growing-shift uniform limit, independent external audit or exhaustive literature priority is claimed.

Self-review: passed. Independent audit: not yet performed.
