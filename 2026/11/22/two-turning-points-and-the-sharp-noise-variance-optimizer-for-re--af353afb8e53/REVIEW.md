# Scientific review: reflection-symmetric three-bin variance

## Correctness — PASS

The proof starts from the exact categorical covariance of the two adjacent differences under multinomial sampling. The multivariate central limit theorem and uniform fourth-moment bounds justify convergence of variances, not just convergence in law. The bivariate Gaussian folded-absolute-moment identity gives an exact limiting coefficient. Under the monotone correlation coordinate \(r\), differentiation gives an explicit numerator \(H(r)\) whose second derivative is strictly positive on the complete admissible interval. One-sided signs at both endpoints and at \(r=0\) then prove the existence of precisely two simple turning points and determine their order. An explicit interior comparison beats both boundary limits. The code reproduces the finite-support covariances, numerical roots and values, and finite multinomial moments; these checks support, but do not replace, the analytic theorem.

The checker does not establish an independent mathematical audit or a finite-sample optimizer. The theorem is for the leading variance coefficient under fixed positive trinomial probabilities and a matched reference.

## Originality — PASS against inspected literature

The closest known source is Banić–Elezović, *Discrete total variation under the multinomial, Part 4: variance under a general distribution* (arXiv:2611.09592v1, 2026-11-06). Its general folded-Gaussian variance formula applies to the present profile and implies the *formula* for the coefficient after substitution, but the inspected sections give neither its complete two-turning-point classification nor a sharp optimizer of the matched-null coefficient on the reflection-symmetric three-bin line. Its explicit alternating combs in §4.2 have even bin counts. The authors' Part 5 (arXiv:2611.14735v1, 2026-11-10) instead studies cyclic variation, with an additional edge. The earlier Hoel–Kamat uniform-case calculations do not optimize nonuniform probability profiles.

The closest published results encountered in semantic claim searches concern large deviations of uniform histograms, sample-size conditioning of uniform-histogram roughness, and multinomial local statistical power. These neither imply the new optimizer theorem nor present the same exact classification. A relevant full-text search for this exact parameter optimization was negative, but a search is not proof of historical novelty. The greatest residual priority risk is an obscure general optimization of folded bivariate Gaussian absolute sums, or an unindexed related histogram result.

## Value — PASS

The reflected three-bin family is the minimal two-edge null model with a tunable dependence parameter; it is motivated independently of the numeric answer. The theorem gives an exact globally worst noise profile for Gaussian-scale calibration, and reveals a second non-monotone regime near the center-bin depletion boundary. The strict-convexity reduction gives a global classification rather than an isolated computational extremum. No finite-sample, nonsymmetric, or statistical-power optimality is claimed.

Self-review: passed. Independent audit: not yet performed.
