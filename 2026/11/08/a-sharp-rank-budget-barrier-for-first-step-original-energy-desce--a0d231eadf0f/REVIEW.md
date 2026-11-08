# Scientific review

## Correctness

**PASS (same-model).** Equations (1)–(2) are derived by eliminating the scalar auxiliary variable in the first SAV/RSAV step at consistent initialization. The proof reduces the all-input objective inequality to \(B\preceq2I\), proves necessity by arbitrarily small inputs, and uses Loewner inversion to give the exact criterion \(h(H-2L)\preceq2I\). Courant–Fischer gives the rank lower bound, attained by spectral truncation. The \(C>0\) boundary and every rank \(0\le r<d\) are included. An independently executable diagnostic script passed 17,663 numerical assertions, which do not replace the proof.

## Originality

**PASS (literature-qualified).** The most directly related paper [1] proves conditional original-objective descent for all iterations using a general smoothness restriction, not a necessary-and-sufficient coherent-first-step criterion nor an optimal rank-budget ceiling. The separate original-energy R-SAV formulation [2] and the higher-rank *pullback correction* of [3] are different operators and do not supply the same theorem. Earlier SAV optimization literature [4] discusses auxiliary-energy discrepancies without identifying the rank-\(r\) spectral-tail frontier. Searches for quadratic SAV original-energy thresholds, low-rank curvature and spectral eigenvalue tails, together with comparisons against indexed mathematical records, found no direct covering result. The main residual priority risk is a classical spectral preconditioning or SAV calculation that gives an equivalent statement without the present terminology.

## Value

**PASS.** The source's unconditional *modified*-energy dissipation makes its original-objective behavior an important but distinct issue. The theorem supplies a sharp design constraint for curvature-rank budgets, proves rank-deficient methods have finite universal original-energy step limits, and identifies precisely which neglected Hessian eigenvalue controls the best possible limit. These are nontrivial, universally quantified structural and worst-case statements, not merely a numerical example or a small constant improvement. The theorem is restricted to the first coherently initialized step and makes no unsupported all-iteration claims.

## Sources, scope and risk

Closest: [1] arXiv:2606.10562v1, especially equations (5)–(6) and Theorem 4.6; [2] DOI 10.1016/j.aml.2026.109905; [3] arXiv:2606.18551v1; [4] arXiv:2301.02942. A differently reformulated SAV positive-root method and general matrix spectral-step results do not subsume the fixed-curvature rank theorem. The principal limitations are first-step coherent initialization, SPD quadratics, exact arithmetic and absence of a Nyström-sample-quality guarantee. Unindexed equivalence remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
