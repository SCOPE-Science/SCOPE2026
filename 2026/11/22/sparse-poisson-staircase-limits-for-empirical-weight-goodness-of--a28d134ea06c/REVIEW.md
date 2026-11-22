# Scientific review

## Correctness — PASS

The proof establishes the fitted-to-true mean ratio by exact Poisson variance, finite common-cell weight ratios by binomial Chebyshev bounds, the unique critical rare-cell count by a binomial-to-Poisson probability-generating-function limit, and the simultaneous absence of higher cells by an exact union bound. An exact decomposition of the *entire infinite weighted tail*, not a truncated approximation, produces the fixed-weight limits. Small fitted/empirical weights at the critical cell and on the unseen tail prove the adaptive-weight limits. The same argument proves all plateau regimes. The complete standalone checker passed 367 supplementary assertions. All requirements are finite fixed count indices, positive summable deterministic weights, and explicitly stated triangular-array hypotheses.

## Originality — PASS, qualified

The closest paper is Kirui et al., arXiv:2402.12866v1 (2024-02-20), especially §2, formulas (2.2)–(2.7), §3 and Appendices A–B. Kirui's 2023 dissertation, Chapters 3–5 and numerical appendix, presents the underlying statistics and fixed-mean computational study. Neither inspected work derives the rare-cell critical distribution, nonvanishing full-tail floor, simultaneous limit across the three fixed-weight distances, deterministic plateaus, or the six-adaptive-versus-three-fixed asymptotic separation. Published Stein–Chen Poisson tests use different statistics. Standard rare-event Poisson convergence is acknowledged, not presented as novel. Searches for aliases (sparse intensity, triangular array, empirical histogram ratios, weighted \(L_p\) distances and occupancy thresholds) found no direct coverage; absence in search is not proof of absolute priority.

## Value — PASS

The result identifies a concrete calibration boundary for all nine members of a published test family under a *correct* but increasingly sparse null. It distinguishes nonvanishing discrete sampling residuals caused by weights assigned to unobserved count cells from vanishing adaptive-weight residuals, and supplies an exact null distribution for every rare-cell transition. For example, at \(n\lambda_n^2\to2\) the fixed exponential \(L_1\) score has a positive, discontinuously distributed limit even though the fitted and empirical counterparts go to zero. This structural distinction is useful when analyzing the validity and calibration of sparse-count diagnostics, though it does not by itself prove bootstrap miscalibration.

## Residual risks and scope

The MSc thesis was inspected in its relevant construction and conclusion chapters, not subjected to a complete line-by-line historical review. General sparse-multinomial literature might contain equivalent asymptotic formulations without naming these particular tests; no such implication was identified. This work does not establish a bootstrap rejection-probability theorem, local power, or uniformity in growing count indices. Independent external assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
