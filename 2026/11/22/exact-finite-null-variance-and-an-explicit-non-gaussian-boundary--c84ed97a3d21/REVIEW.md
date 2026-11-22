# Scientific assessment: a cyclic rank-sum boundary law

## Correctness — PASS

The specified score gives a uniform random value and therefore has no cross-score ties almost surely. The exact signed-quadratic identity reduces the statistic to a cyclic-ascent count and orthogonal products of independent symmetric signs. Cyclic-ascent covariance and the conditional sum of squared coefficients prove the finite-sample moments. The second-order limit is obtained from finite-rank spectral truncations: one-dependent, sign-weighted eigenfunction sums obey a Gaussian central limit theorem with identity covariance, and an exact sign-product orthogonality controls the Hilbert–Schmidt truncation error. The compact kernel's complete spectrum follows from an explicit one-dimensional boundary-value problem; the entire-function product and chi-square cumulants yield the stated characteristic function, variance and excess kurtosis. A standard-library checker enumerates every binary-pattern/rank-order combination through six observations, and separately checks root and product identities. Those computations are supporting evidence, not an infinite proof.

## Originality — PASS, subject to independent priority review

The primary study [1] states the precise cyclic rank-sum statistic and a first-order normal approximation conditional on non-additivity. Its Remark 3 expressly identifies additive probability-integral-transformed scores as an excluded case. This theorem is confined to that excluded boundary and supplies new exact moments, non-Gaussian order and full eigenvalue/characteristic-function description. General work on canonical U-statistic chaos for independent or weakly dependent data [3–5] gives reusable proof tools, but the complete score-specific spectrum, moments and hyperbolic formula are not conclusions stated in the inspected material. No directly equivalent formula was found among the inspected sources; absence from those sources is not proof of global priority. Broader uninspected specializations remain a residual risk.

## Value — PASS

The motivation is the explicit non-additivity boundary of the published independence statistic, not an arbitrary choice of a toy distribution. The score demonstrably depends on both margins while attaining exact first-order degeneracy. The result supplies a complete finite-sample variance and a usable limiting null distribution, with a closed form characteristic function and a large non-Gaussian kurtosis, enabling calibration research in this excluded regime. A mere statement that the Gaussian hypothesis fails would not provide those facts.

## Closest literature and limits

The original authors already identified the non-additivity condition, so that condition is not presented as new. Standard quadratic-chaos theory supplies the general expectation of a second-order limit, and is credited. This analysis does not address learned classifiers or the finite-sample properties of the source's estimated variance/studentizer, and it offers no alternative-distribution power theorem. Historical-priority risk remains for uninspected specialized work.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Cai, Lei and Roeder, arXiv:2110.07652 (2021), https://arxiv.org/abs/2110.07652.
[2] Cai, Lei and Roeder, Journal of the American Statistical Association, DOI:10.1080/01621459.2023.2218030.
[3] Borisov and Volodko, arXiv:0906.5465 (2009), https://arxiv.org/abs/0906.5465.
[4] Carlstein, DOI:10.1177/0008068319880106 (1988).
[5] Shao, DOI:10.1080/24754269.2025.2579414 (2025).
