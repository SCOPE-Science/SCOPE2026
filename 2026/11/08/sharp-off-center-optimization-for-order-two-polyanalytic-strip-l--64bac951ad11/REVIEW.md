# Scientific review

## Correctness — PASS
The strip symbol is reduced exactly, not approximately, through the published two-Hermite matrix-function formula [1, Proposition 10.4]. Exact Gaussian integrations give the finite-width Gram entries, the positive curvature at the origin, and the complement tail matrices. The thin-width limit follows from localized rank-one Gram convergence with a global trace bound. The large-width limit follows from explicit, positive determinant identities, a uniform two-term saddle profile, and a global exclusion argument showing every optimizing fiber enters the bounded rescaled phase region. The standard-library checker passed 404 finite consistency assertions. The direct-integral nature of the operator rules out inferring an actual global norm-attaining eigenvector from a maximizing fiber.

## Originality — PASS (historical priority provisional)
The exact Hermite matrix reduction [1,2,3] is prior art and explicitly excluded from the novelty claim. Material from the full [1] and [2] papers, including the main propositions and operator-algebra results, was compared with the precise moving-interval norm and optimizing-displacement claims. Neither inspected source states the strictly off-center all-width conclusion or the sharp wide-strip \(\log(2a)/a\) displacement and inverse-cubic leakage constant. Relevant cross-topic research records concerning half-line Hermite spectral gaps, radial Fock symbol smoothing, and a different double-Hilbert strip were compared by mathematical implication, not title. The residual risk is an equivalent earlier asymptotic theorem under another Toeplitz or Gaussian-tail formulation; a negative search does not certify uniqueness.

## Mathematical value — PASS
The full polyanalytic space has two coupled Hermite channels, and simply using the centered Gaussian loses a full factor of the squared strip width in the leading leakage. The theorem quantifies the optimizing off-center fiber at both thin and wide widths and gives a sharp scale and coefficient for the natural operator norm, identifying nontrivial coupling effects invisible in one-channel analytic Fock localization. This concerns an unbounded strip and a physically natural order-two concentration operator, rather than an arbitrary numerical slice. The detailed number and uniqueness of finite-width maximizing fibers remain open here.

## Closest literature and limits
[1] E. Lee-Guzmán et al., arXiv:2309.03410v1, especially Proposition 10.4 / equation (51): matrix symbol, not norm optimization. [2] Arroyo Neri et al., DOI:10.1155/2021/9919243, especially Theorem 9: horizontal matrix Toeplitz representation, not moving-window asymptotics. [3] Sánchez-Nungaray et al., DOI:10.1155/2018/8031259: earlier horizontal symbols. Independent historical and mathematical validation remains necessary.

Self-review: passed. Independent audit: not yet performed.
