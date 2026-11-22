# Self-review

## Correctness — PASS

The exact statement is the all-degree \(BV(-1,1)\)-to-\(L^2(-1,1)\) residual norm of the unweighted Legendre projector, with the full extremizer classification. The proof independently checks BV jump decomposition, Legendre Parseval identity, telescoping derivative, interlacing, strict monotonicity of a Sturm energy at distinct Gauss nodes, strict equality conditions and even/odd asymptotics. `CHECK.py` passed 892 symbolic and numerical assertions. The finite computations are corroborative, not a substitute for the analytic argument.

## Originality — PASS (qualified)

Material comparisons were made with the 2015 fixed-jump Legendre \(L^2\)-error table, a 1993 Legendre spectral-viscosity paper, classical Christoffel–Darboux identities, accessible indexed research claims, and other archival convergence-rate literature. The 2015 paper's fixed jump at \(2/3\) and the earlier degree-three projector variation-output norm do not imply the all-degree worst-jump \(L^2\) error or its parity/equality classification. The 1981 Bojanić–Vuilleumier BV convergence paper was not available in full text, leaving priority uncertainty. Classic Sturm and orthogonal-polynomial identities are credited as background.

## Value — PASS

The natural full BV class and a standard spectral approximation operator have a newly determined sharp energy-error constant at every degree, together with all equality cases and a sharp large-degree constant. This is more informative than a convergence order or a fixed-step table; the off-center worst case at every odd degree matters to polynomial approximation of discontinuous inputs.

## Scientific limitations

The conclusion is for real BV, unweighted Legendre projection and unweighted Lebesgue L2. It does not claim novelty for standard Legendre identities, covers no weighted/multivariate projections, and is not independently certified. An inaccessible older primary source and possible unindexed equivalent formulas are the main originality risks.

Self-review: passed. Independent audit: not yet performed.
