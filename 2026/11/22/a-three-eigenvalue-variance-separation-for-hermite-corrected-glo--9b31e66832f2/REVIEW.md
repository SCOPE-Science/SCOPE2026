# Review of the three-eigenvalue Hermite-correction variance separation

## Correctness

**PASS.** For the stated sparse positive-definite family the last two coordinates form an explicit block with eigenvalues \(N\) and \(2N\), alongside \(N^3\) unit eigenvalues. The one-node full-size global-Lanczos Rayleigh quotient and Hermite tangent are therefore exact. A single offdiagonal coordinate pair determines the entire Rademacher quadratic-form noise. Its scalar multiplier is \(1-2N^2/\mu_N^2\), giving a pathwise identity for every finite probe sequence. The variance is consequently amplified by a factor asymptotic to \(4N^4\). Spectral formulas for the inverse and the Hermite remainder prove that the Gaussian corrected-to-baseline variance ratio tends to zero like \(5/N\). The exact trace formula proves the deterministic relative-bias limit. The two-eigenvalue bound follows by spectral-projector decomposition. The included exact-rational script passed 2,501 assertions, complementing but not replacing the algebraic proof.

## Originality

**PASS, subject to historical-priority risk.** The full motivating preprint by Rinelli, Simunec and Vermeiren (arXiv:2611.18864v1) contains the algorithm, the Hermite remainder, and Gaussian/Rademacher variance expressions; those are used rather than re-proposed. Published spectral-deflation literature, including Gambhir, Stathopoulos and Orginos (arXiv:1603.05988), already recognizes that reducing some spectral errors need not reduce stochastic sign-probe variance. The present three-point-spectrum quantitative separation, its exact all-probe law, the contrasting Gaussian asymptotics, and the two-versus-three-eigenvalue conditioning gap were not established by the closest inspected statements. The previously established two-level inverse-trace scalar formula cannot supply quartic growth at condition \(2N\). No claim is made that a failed literature search proves worldwide novelty.

## Value

**PASS.** In matrix-function trace estimation, the same Hermite approximation can look excellent in relative Frobenius error and in deterministic trace while being unreliable with sign probes. A sparse three-eigenvalue construction makes this mismatch exact and arbitrarily large, identifying a concrete spectral-and-coordinate mechanism rather than an unexplained numerical failure. The two-eigenvalue bound gives a meaningful minimum spectral-complexity contrast. This can inform the choice of residual estimator and variance assessment but does not establish performance or cost advantages.

## Closest literature and limits

Rinelli, Simunec and Vermeiren, arXiv:2611.18864v1 (2026); Gambhir, Stathopoulos and Orginos, arXiv:1603.05988 (2016); Hallman and Troester, arXiv:2103.10516 (2021). The conclusion applies only to exact inverse actions, a one-step full-size Hermite correction, and the specified family. The finite tests do not certify all dimensions, while the proof does. Historical priority is open to independent checking. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
