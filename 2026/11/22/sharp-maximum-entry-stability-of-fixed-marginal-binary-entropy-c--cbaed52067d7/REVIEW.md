# Self-review

## Correctness — PASS

The feasible coupling is a one-dimensional open interval with a strictly increasing log-odds parameter, hence the unique exact optimum is interior for every real log-kernel. Implicit differentiation yields a checkerboard rank-one Jacobian with exact induced maximum-entry norm \(4/H_{r,c}(z)\). Strict convexity of the positive reciprocal curvature yields a unique minimizer, segment integration gives the global bound, and explicit admissible infinitesimal checkerboard inputs establish sharpness. Both marginal harmonic inequalities and their equality conditions have been proved, as has the sign identity for the worst-conditioned coupling. Standard-library checker replay: 9,675 supplementary assertions passed. Risk: these numeric checks are finite; the universal claim rests on the written analytic proof, which independently needs external review.

## Originality — PASS (provisional priority)

Eisenberger et al., arXiv:2205.06688, Sec. 4.2, derive general Sinkhorn gradients and therefore establish the *pointwise derivative concept*, but not the global maximum-entry optimization over all fixed-marginal binary kernels or its balanced-variance rigidity. Ghosal et al., arXiv:2106.03670, Theorem 1.4, concern convergence under changes of costs/marginals rather than a sharp modulus. Eckstein–Nutz arXiv:2110.06798 concerns general quantitative stability, especially varying marginals. Published binary Sinkhorn sweep contraction concerns iterated scaling coordinates, not this map from a changing log-kernel to an optimal plan. The known analytic background is acknowledged rather than claimed as new. Residual risks: an exact equivalent may have appeared in classical binary contingency tables or sensitivity-analysis literature not uncovered by the targeted comparisons; the full Eckstein–Nutz paper was not materially read, so its precise boundary is assessed from abstract/introduction only.

## Mathematical value — PASS

The four-cell setting is the first nontrivial entropy transport problem with both sets of marginal constraints. The result gives the exact, attained-in-the-derivative worst robustness coefficient for *all* input kernel contrasts, clarifies exactly when a natural marginal-variance bound is sharp, and shows the worst susceptibility generally occurs at associated rather than independent tables. These are natural invariants for perturbations of differentiable transport layers, not arbitrary finite-table computations. It is limited to two rows and two columns and does not assert a broader large-table result.

Self-review: passed. Independent audit: not yet performed.
