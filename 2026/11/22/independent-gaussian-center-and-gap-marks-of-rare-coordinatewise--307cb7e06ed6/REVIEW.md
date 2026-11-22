# Self-review

## Correctness (PASS)

For an oriented comparable pair, the conditioned one-coordinate density is exactly the uniform-triangle density, with sum/gap mean zero, variances 1/6 and 1/18, and zero covariance. Independent coordinates give the joint Gaussian limit; a dependency neighborhood of size \(4n-6\) and the one-coordinate two-edge probabilities \(1/3\) and \(1/6\) give the claimed finite-partition Poisson approximation using Arratia–Goldstein–Gordon (1990, Theorem 2 and Section 3.1). The critical error exponents are strictly negative, and standard Poisson void probabilities yield the extremes. The exact-rational checker passed 3007 assertions; the proof of weak convergence is analytic, not computational.

## Originality (PASS against accessible evidence)

The closest literature establishes the non-Pareto count phase diagram (Bhattacharjee et al., 2026), fixed-coordinate Poisson projections of non-Pareto vertices (Ilienko–Jin, 2026, as described explicitly in the accessible follow-up), random partial-order chain/degree thresholds (Bollobás–Brightwell, 1995), and general marked locally dependent Poisson approximation (Arratia–Goldstein–Gordon, 1990). The new claim is not any of those inputs; it is the full-coordinate, two-endpoint, bivariate Gaussian **mark process of all sparse domination edges**, with independent local center/gap marks and dependent global extremes. Fixed-coordinate limits do not imply a growing-number-of-coordinates central limit theorem. The related 2026 source's entire full text and the 1995 source's entire full text were unavailable; the risk that a broader theorem subsumes this specialization remains and independent priority review is needed.

## Value (PASS)

The result gives an explicit second-order geometry of an intrinsic event at the sharp Pareto-sparsity threshold: it identifies the typical center and separation fluctuations of an entire rare directed relation, not merely the count of affected vertices. The independent-Gaussian mark structure together with shared-count dependence of extreme center/gap statistics is a natural, directly usable probabilistic description. The threshold and unmarked Poisson count are credited, not presented as gains.

## Limitations

Exact scope: independent uniform cube samples with dimension satisfying \(n(n-1)2^{-d}\to\lambda\in(0,\infty)\), finite Borel partitions, and weak point-process convergence. The matching statement may already follow from older maximum-degree work. No uniform-in-growing-number-of-bins error, no high factorial moment convergence, no away-from-threshold result, and no independent assessment are claimed.

Self-review: passed. Independent audit: not yet performed.
