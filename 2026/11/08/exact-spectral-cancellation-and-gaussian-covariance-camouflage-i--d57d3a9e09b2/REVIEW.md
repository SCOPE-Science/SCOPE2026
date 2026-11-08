# Scientific review

## Correctness

**PASS (self-review).** The stationary process is a Gaussian stochastic convolution conditional on the environment. The two-state generator yields the closed second-moment and lag-covariance systems, with the exact spectral-sign factorization and global curvature classification. Exact fourth-moment equations establish a positive fourth cumulant even at the unique OU-covariance matching surface. A standalone standard-library checker passed 1,050 rational-grid cases, with separately implemented matrix-exponential comparisons. This is not an exhaustive or independent validation.

## Originality

**PASS, with substantial prior-framework qualification.** Frydel's on/off trap has symmetric switching and treats the stationary density, potential energy, and entropy production, not this unequal-rate spectral-cancellation and curvature phase diagram. Huang et al. give a general matrix recipe for covariance of Markov-modulated OU processes (a potentially broad antecedent), not the explicit necessary-and-sufficient complete-monotonicity, single-exponential cancellation, and positive fourth-cumulant classification at that cancellation. Earlier results for symmetric switching cover the negative fast-weight regime, not the asymmetric positive-weight transition. Thus the contribution is a nontrivial sharp property classification, not a new covariance solution method. The general 2014 framework could make priority sensitive to whether its implicit consequences are considered already covered; follow-up scholarly comparison is prudent.

## Mathematical value

**PASS.** The result resolves a natural two-time-observation ambiguity in a physical on/off trapping model: equilibrium covariance can occur at a unique finite rate surface while one-point non-Gaussianity remains sharp and measurable. It also identifies when a passive switching trap violates complete monotonicity, and an exact inflection criterion. These are structural, global-in-parameter observations rather than isolated numerical cases.

## Limitations

The theorem assumes an independent two-state Markov environment, purely on/off harmonic stiffness, and no position kicks. It proves neither exact full-law equivalence nor finite-data identifiability, and it does not generalize the classification to arbitrary switching distributions. All external claims of novelty remain qualified by broad older moment/covariance frameworks.

Self-review: passed. Independent audit: not yet performed.
