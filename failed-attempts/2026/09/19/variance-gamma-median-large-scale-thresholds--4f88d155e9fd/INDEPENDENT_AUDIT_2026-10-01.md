# Independent mathematical audit — 2026-10-01

## Final claim assessed

The variance-gamma median has five sharp large-scale regimes separated by critical shapes r=1 and r=3, with the displayed power/logarithmic constants; substituting the correlated-normal-product/Wishart parametrization gives the stated small-correlation median expansions.

## Correctness — PASS

The formulas agree with the earlier independently stated five-regime theorem and survive direct algebraic reconstruction. With kappa=(sigma/theta) to the power 2, the r=1 denominator reduces exactly to log(sigma/theta)+log(2 log(sigma/theta))+1-gamma_E, and the r=3 term becomes (4/3)theta to the power 3 sigma to the power -2 log(sigma/theta). The r=2 expansion matches the exact asymmetric-Laplace check. The bundled numerical code was inspected; independently redoing the parameter conversions reproduces the Wishart corollaries.

## Originality — FAIL

The complete five-regime theorem, including both critical logarithmic transitions and the same constants, was already published in SCOPE on 2026-09-18. The Wishart statements are obtained by direct substitution theta=rho S and sigma=S sqrt(1-rho to the power 2) into that prior theorem. An alternate Bessel derivation and routine specialization do not evade implication-based coverage.

## Value — FAIL

The five-regime classification is valuable mathematics, but this later record does not supply an unknown answer: the theorem was already published and the Wishart formulas are mechanical substitutions. Under the value bar, an alternate derivation plus direct corollary is not a separate motivated mathematical gap.

## Source inspections and risks

- **Sharp large-noise asymptotics for variance-gamma medians** (SCOPE 2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e): Complete RESULT.md from audited Git snapshot. Assessment: COVERING.
- **Bounds for the median of the generalized hyperbolic and related distributions** (arXiv:2609.20212): Primary arXiv abstract; full-text retrieval through the web endpoint failed, so no claim of whole-document noncoverage is made. Assessment: BACKGROUND.

Residual risks: The 2001 generalized-Laplace monograph was not needed to decide this record because exact earlier SCOPE coverage is already decisive.
