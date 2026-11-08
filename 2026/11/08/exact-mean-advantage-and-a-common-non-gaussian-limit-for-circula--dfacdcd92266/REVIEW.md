# Scientific review

## Correctness
PASS. The central finite-population gain is derived by cyclic exchangeable Dirichlet gaps, a beta-density tilt, an order-statistic/binomial identity and a telescoping central absolute-deviation identity. For even sizes the random-deletion coupling supplies the same gain as the preceding odd size. The limiting law follows from a tight circle-valued empirical-cost process, the explicit triangular-distance covariance, asymptotic Haar uniformity of RD/PCD/EPCD selection measures, and a joint denominator expansion. The standalone checker reproduces finite identities and mechanism simulations, not the infinite-sample proof.

## Originality
PASS under available literature. Meir (2019), Rogowski and Dziubiński (2025), and Chan, Lin and Wang (2026) establish the mechanism definitions and adversarial worst-case performance; their inspected relevant sections and appendices do not give a closed Haar-sample mean advantage or a joint Gaussian-supremum approximation-ratio limit. Published research-record comparisons and targeted searches did not find the equivalent statement. Earlier circular-median asymptotics and general empirical-process limit theory are plausible components, but do not by themselves assert the exact PCD/EPCD mean or mechanism-specific joint law. Publication priority remains provisional in the presence of possibly unindexed literature.

## Mathematical value
PASS. The exact finite-\(n\) mean gain and its \(1/4\) limiting value distinguish the two familiar lotteries under a natural homogeneous population. The joint non-Gaussian limit specifies the first stochastic correction to the typical approximation ratio, explaining how all three mechanisms may have different worst-case guarantees or finite unconditional costs yet share the same leading random typical inefficiency. It is a meaningful performance benchmark, not only an algebraic restatement of known bounds.

## Scope and residual risk
Only independent uniform locations on a continuous unit circle, and conditional expected cost ratios, are covered. The limit distribution is an explicit Gaussian supremum rather than an elementary cdf. Closest sources mainly study worst-case guarantees; specialized or unindexed average-case work could predate this result.

Self-review: passed. Independent audit: not yet performed.
