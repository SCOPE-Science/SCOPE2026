# Scientific review: exact all-iteration two-spectrum covariance probing law

## Correctness — PASS

The statement is an exact consequence of a two-eigenvalue spectral reduction followed by a nontrivial all-iteration extremization: with common Rademacher probes, covariance-diagonal error is one fixed projector diagonal-estimation error multiplied by a scalar spectral-ratio function. The high-to-low covariance ratio decreases strictly from the condition number to its reciprocal under the stated step restriction. The relative-error multiplier is maximized at an endpoint, and comparing endpoints yields the sharp leverage threshold of one half. The projector identity gives the exact rowwise Rademacher variance proxy. In the flat rank-one case the independent sign products give an exact binomial sum, not an approximation. The checker returned `VERIFY_OK` for 1,200 dense-operator comparisons, six complete short finite-sign enumerations, and 20 endpoint comparisons. Those computations confirm the implementation but do not replace the analytic proof.

## Originality — PASS, qualified

The closest direct source, Abhishek and Holman (2026, arXiv:2610.00882, Sections 3.3, 3.5, 3.6 and Appendix 5.1), already provides the propagated Gaussian covariance and fixed-index Rademacher diagonal-estimation construction. Hallman, Ipsen and Saibaba (2023, DOI:10.1137/22M1476277, Sections 3 and 5) already prove fixed-matrix diagonal-concentration inequalities and discuss projector diagonals as an application. Matti, He, Kressner and Lam (2025 preprint, arXiv:2502.18626, Section 2) already analyze parameter-dependent *trace* estimation with shared Gaussian random matrices and integrated-error guarantees. None of their materially inspected statements supplies the exact two-spectrum coordinatewise supremum, the leverage-one-half endpoint rule or the flat-spike all-horizon binomial distribution. Searches across mathematical findings, related published literature, aliases and parameter-dependent methods revealed no governing stronger claim; these searches are evidence of comparison, not proof of historical uniqueness. Historical-priority risk persists, especially if older projector-diagonal sampling or parameterized stochastic estimates contain an implicit equivalent.

## Value — PASS

A randomized stopping criterion may evaluate covariance diagonals at many iterations with the *same* probes. Applying one fixed-index concentration bound and union-bounding over a long or unbounded horizon is inefficient or impossible without additional control. The sharp half-leverage dichotomy identifies which part of the full trajectory controls calibration and yields a horizon-free event for each coordinate. The exact flat-spike binomial law is a canonical finite-sample benchmark for selecting the number of probes. The statement has a natural object and invariant, not an arbitrary finite slice; it provides no automatic full confidence-coverage guarantee for arbitrary data-dependent stopping rules.

## Scope and residual risks

The two-spectrum assumption and nonnegative Landweber factors must be retained. The all-time probability bound is not asserted sharp for an arbitrary orthogonal projector. The flat-spike exact distribution is coordinatewise; dependencies across different coordinates are not claimed away. A finding on a special spectral class does not imply a general inverse-problem bound. Novelty remains contingent on historical literature not contained in inspected sources.

Self-review: passed. Independent audit: not yet performed.
