# Self-review

## Correctness

**PASS.** The incidence derivatives \(c,d\), the unit center eigenvector \((\alpha,1,\omega)\), and the exact identity \(Q=v^2D(p)/(p^2u^2)\) follow from a direct Taylor expansion at the adoption-free state. The inequalities \(A<0\), \(B_0<0\), \(D(0)>0\), \(D(1/2)<0\) prove uniqueness and strict position of the nonlinear boundary. A parameter-dependent center manifold and the implicit-function theorem yield local branch direction and multipliers. The invariance of \(a=0\) identifies the strong-stable exceptional set; scalar parabolic dynamics gives the \(1/n\) limit for every sufficiently close physical state with \(a_0>0\). The standalone checker verifies exact symbolic identities and representative finite trajectories; the latter are corroboration only.

## Originality

**PASS within the inspected record, with residual priority risk.** Muñoz–Nuño–Meacci [1] supply the same round map and the **linear invasion threshold**, and investigate nonlinear endemic points and distant Neimark–Sacker/chaotic dynamics. The full source's Definition 1, Propositions 3–5, sections 5–8 and Appendix were inspected; it does not give the quadratic center coefficient, unique \(p_*\), or its critical parabolic relaxation law. Katriel's full 2018 continuous-time work [2] already determines the \(p=1/2\) forward/backward split for the limiting ODE; the present coefficient genuinely depends on finite \(\tau\). Heidecke–Barbarossa [3] prove transcritical direction changes for a different continuous-time replenishment model. Generic center-manifold theory implies conditional conclusions once \(Q\) is supplied, but does not specify this exact competing-risks map's sign boundary. The closest semantic research records concern different SIRS/epidemic maps, not this exact incidence-and-turnover map. No claim of definitive historical priority is made.

## Mathematical value

**PASS.** The motivating paper identifies the invasion multiplier but does not resolve whether a near-threshold nonzero branch is physical and attracting, or quantify critical relaxation. Finite updating shifts the natural continuous-time forward/backward dividing line by an explicit finite-round amount; this matters for predicting hysteresis versus continuous onset in such round-based contact systems. The universal \(1/n\) coefficient supplies a model-specific finite-round clearing-time diagnostic. This is a structural parameter-boundary theorem, not a routine restatement of linear stability.

## Limits and closest literature

The result is local in the deterministic large-population map. It does not decide global basins, a degenerate cubic normal form at \(p=p_*\), or finite-population stochastic persistence. Related prior works: [1] arXiv:2611.08353v1 (same map and linear threshold), [2] arXiv:1812.08867 (continuous-time counterpart), [3] arXiv:2011.08792 (different continuous-time model). No independent validation has taken place.

Self-review: passed. Independent audit: not yet performed.
