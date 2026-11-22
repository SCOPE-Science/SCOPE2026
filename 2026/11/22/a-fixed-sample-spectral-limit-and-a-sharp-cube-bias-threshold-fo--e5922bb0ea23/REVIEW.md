# Scientific assessment: fixed-sample quadratic maximal-projection test

## Correctness — PASS

The source formula [1, (1.3)] is checked against its exact quadratic spectral representation. For dimensions \(d\ge2n\), the derivation reduces the original test exactly to the largest eigenvalue of its observation Gram matrix, with the negative scatter eigenvalue shown not to dominate. The Haar Gram central limit follows from a multivariate classical central limit theorem for Gaussian coordinate products and Slutsky normalization. The independent biased-sign model has the explicitly computed pair-product covariance with diagonal \(1-\mu_d^4\), shared-vertex covariance \(\mu_d^2-\mu_d^4\), and zero covariance for disjoint edges. A bounded triangular-array central limit theorem gives the deformed Gaussian eigenvalue. The spectral mapping, null quantile continuity, and diverging-shift Rayleigh quotient establish both sides of the threshold. For two observations, the Beta null and binomial alternative laws give an independent exact finite-dimensional confirmation. The included checker passed 751 assertions; simulations do not establish the infinite-dimensional limit.

## Originality — PASS, with historical-priority limitation

The 2023 full primary preprint [1] defines the source statistic, proves fixed-dimension large-sample limits and discusses rates of consistency as a direction for further work. The full accessible author preprint of Cutting, Paindaveine and Verdebout [2] studies a different Frobenius Bingham test in a different (jointly diverging) sample/dimension regime with rotationally symmetric alternatives. The Rayleigh study [3] concerns a first-order statistic. Direct searches for fixed-sample Gaussian Gram spectral limits of the specific quadratic maximal-projection test, for biased-cube alternative critical power, and for the \(d^{-1/4}\) transition identified no statement implying the combined theorem. Routine multivariate central limit methods are explicitly credited rather than represented as new. Historical priority is not independently certified, and generic high-dimensional random-Gram results may be stronger in other settings.

## Value — PASS

The source test is explicitly designed for detecting departures from uniform spherical directions, and its quadratic member is sensitive to second-moment structure. The dimension-only asymptotic regime exposes a quantitatively sharp detection boundary for a natural independent-coordinate alternative and, at zero bias, an exact information-loss example: a singular non-Haar law retains nominal asymptotic rejection probability. The exact two-observation binomial/Beta law provides a practical finite-dimensional calibration benchmark. These are specific, mathematically motivated statistical consequences, not a generic restatement of the central limit theorem.

## Limitations and closest literature

The claimed rate is specific to the tested family; it is not a minimax rate. The two-observation formula is the only finite-dimensional exact distribution provided; the general fixed-\(n\) limit is an asymptotic eigenvalue law. The closest primary sources are [1] Borodavka–Ebner and [2] Cutting–Paindaveine–Verdebout. The original 2023 preprint's methods/results/conclusion and the author's Bingham preprint's methods/introduction have been read; the separate 2026 journal printing of [1] was accessible in abstract/bibliographic form, so its article body was not independently compared line by line. A qualified historical-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
