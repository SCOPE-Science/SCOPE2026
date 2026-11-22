# Scientific review

## Correctness — PASS
The exact intrinsic-coordinate first-passage equation gives the normalization unambiguously; strictly convex Jensen inequalities reduce *every* admissible profile to the unique two-plateau minimizer. The derivative of the scalar objective is a cubic with one positive root, and an exact strictly signed polynomial derivative proves monotonic improvement. The two endpoint constants and half-budget allocation follow from explicit rational parameterization. Reproducible symbolic identities, numerical minimizers, and heterogeneous-profile checks passed. Piecewise-constant interface transmission is explicitly defined; the smooth-only case is characterized as a sharp infimum, not a smooth minimizer.

## Originality — PASS (qualified)
The 2026 primary source already states the interior plateau and depicts the two-layer Stratonovich design numerically; those are not new. The 2023 article gives the general first-passage transform. Neither inspected source reports the *exact global all-launch algebraic parameterization, strict gain monotonicity, two sharp endpoint gain laws, and the singular half-budget allocation law* together, nor does its stated result imply their exact formulas without solving the additional budget-optimization problem. Indexed related results concern reset-location design, partially absorbing traps and heterogeneous search without this fixed-budget law. The main residual risk is an unindexed prior derivation or an overlooked specialization of broader convex optimization. Priority is not certified independently.

## Value — PASS
The precise result replaces a numerical interior-launch design landscape with a complete sharp analytic family and identifies a physically instructive singular allocation: a vanishing terminal layer receives one half of the diffusivity resource, and the optimal relative completion time falls with a square-root law. The strict monotone launch-position gain and cubic weak-interiority onset quantify when mobility heterogeneity first helps. This is a natural global design invariant under the constraint studied in the motivating paper; correctness and new notation alone are not the value argument.

## Closest literature and limits
Menon (2026), arXiv:2611.17470, Sec. III.C and Figs. 4–5, is the closest prior and owns qualitative two-level optimality. Menon–dos Santos–Anteneodo (2023), arXiv:2311.00818, owns the coordinate transform and arbitrary-profile mean first-passage formula. Tung–Lawley (2026), arXiv:2512.19646, treats three-dimensional target escape rather than the present one-dimensional budget design. The result is restricted to Stratonovich transport, an interior start, prescribed mean diffusivity and the explicit interface convention.

Self-review: passed. Independent audit: not yet performed.
