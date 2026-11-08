# Scientific review

## Correctness

**PASS.** Conditioning on the first feasible edge establishes the rational recurrence for every induced forest state. A complete isomorphism-class enumeration of 987 trees through order twelve and 1301 trees at order thirteen, with support degree at most three and exact quadratic/cubic discriminants, gives the sharp threshold and exactly six exceptions. The explicitly described symmetric tree has an exact polynomial and negative integer discriminant. An independently formulated integer dynamic program aggregates all 12! edge orders and reproduces the same probabilities. The executable verifier and its dependency specification are included.

## Originality

**PASS, qualified.** The key distinction is the terminal law under greedy maximal matching, not the classical matching enumerator. Heilmann–Lieb real-rootedness covers the unweighted sum of all matchings and cannot imply this distributional result. The accessible full text of Krivelevich–Mészáros–Michaeli–Shikhelman studies greedy independent-set densities and trees, and the accessible Bal–Bennett paper studies asymptotic matching processes on random graph models; their statements do not cover the exact finite-tree zeros. Related database and literature searches returned no dominating theorem or the six-type table. The full texts of Dyer–Frieze (1991) and Pippenger (1989) were unavailable; this remains a historical-priority risk, not a proven absence of coverage.

## Value

**PASS.** Real-rootedness is a meaningful distributional shape constraint, strictly stronger than log-concavity and associated with Poisson-binomial factorization. The exact first-failure threshold and complete boundary classification show precisely when a classical matching-polynomial intuition fails under a natural sequential sampling law. The symmetric witness remains strictly log-concave, isolating the stronger obstruction rather than a superficial coefficient irregularity.

## Limits

This is a finite exact classification, not a theorem about every larger tree, weighted variants, or a failure of log-concavity. Reproducibility depends on the standard complete unlabeled-tree generator and exact arithmetic; independent external mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
