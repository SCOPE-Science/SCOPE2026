# Review

## Correctness

**PASS.** Each update is an exact scalar-plus-rotation matrix; squaring its action yields the exact expected multiplier. Independence across iterations proves the all-horizons formula, and the scalar quadratic sign supplies an if-and-only-if stable step interval including the neutral boundary. The distribution-free half-reuse sufficiency follows from \(a_\rho=\mu^2+(2\rho-1)(m_2-\mu^2)\); necessity uses rare positive two-point laws and strict continuity. The bundled checker gives exact-rational independent examples, not a replacement for the proof.

## Originality

**PASS, with publication-precedence risk.** Chavdarova et al. establish possible divergence for independent oracle calls, Mishchenko et al. motivate shared samples, and the 2022 bilinear/extragradient studies address rates for endpoint choices. The inspected source sections do not imply the sharp half-reuse guarantee over *all* finite-fourth-moment coefficient distributions. A related uniform positive two-point coupling classification is narrower: in that family \(m_2<2\mu^2\), so there is no rare-event obstruction and no distribution-free half-reuse cutoff. More obscure joint-oracle coupling literature may overlap and warrants specialist review.

## Value

**PASS.** This is a sharp uniform coordination requirement for a natural family interpolating between two standard stochastic extragradient implementations. It shows that the amount of sample sharing needed to assure *some* mean-square-stable stepsize has a universal one-half threshold, even though the admissible stepsize itself depends on oracle moments. The sharpness persists with strictly positive, bounded two-point oracles. The mean-versus-mean-square separation illustrates why looking only at the expected iterate is insufficient.

## Scope and limitations

The theorem concerns equal-step, two-dimensional scalar bilinear games, iid iteration pairs, arbitrary marginal laws of finite fourth moment and nonzero mean. It does not assert a universal numerical step size, almost-sure instability, general matrix-valued extensions, or full publication-precedence certification.

Self-review: passed. Independent audit: not yet performed.
