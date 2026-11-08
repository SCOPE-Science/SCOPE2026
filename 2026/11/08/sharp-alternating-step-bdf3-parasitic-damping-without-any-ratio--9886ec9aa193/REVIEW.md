# Scientific assessment

## Correctness — PASS

The claim concerns a fixed two-periodic sequence of step sizes and the BDF3 homogeneous recurrence. Independent cubic-interpolation weights reproduce the stated difference transfer; the two-matrix product gives exact rational trace and determinant in the reciprocal invariant \(q=r+r^{-1}\). Strict degree-two Jury inequalities prove all Floquet multipliers lie inside the radius-\(1/5\) disk for all positive ratios, with the limiting boundary attained only as a supremum. The discriminant quartic has one positive root by Descartes' rule; monotonicity of determinant on its complex-root side and monotonicity of the negative-root modulus on its real-root side establish the **global**, not local, optimum. Exact rational Vandermonde checks and bisection reproduced the displayed formulas. No finite experiment is used as a universal proof.

## Originality — PASS, with residual historical risk

The closest inspected primary source, Li and Liao (2022), proves ratio-bounded general-grid perturbed stability and notes its ratio restriction is nonnecessary. It does not state a reciprocal two-periodic monodromy spectrum or its optimal damping ratio. Chen et al. (2021/2022 preprint) prove a ratio-bounded Allen–Cahn energy theorem, which is not an unrestricted zero-equation periodic classification. Söderlind et al. (2018) impose smooth deformation, forcing adjacent ratios towards one. Searches for exact BDF3 alternating/Floquet/ratio-optimal results found no matching theorem. Grigorieff–Paes-Leme (1984) and Guglielmi–Zennaro (2001) remain meaningful historical-overlap risks because full original texts were unavailable; absence of a search hit is not proof of novelty.

## Value — PASS

A third-order multistep method typically comes with restrictive universal sufficient adjacent-step-ratio bounds. Fixed alternating schedules are an important, natural exceptional test class because their ratio product is one. Proving that **every** positive fixed ratio works and determining the sharp worst and best two-step parasitic damping factors completely resolves a natural mesh-design question; the unexpectedly extreme optimal ratio is analytically characterized. This is more than a local approximation or a cosmetic reformulation of classical root tests.

## Scientific limitations

The contraction is a Floquet-eigenvalue statement for homogeneous BDF3 at a fixed ratio, not a uniform-in-r transient norm estimate, full nonlinear convergence theorem, or unconditional stability of arbitrary variable grids. Historical primary full-text overlap remains possible.

Self-review: passed. Independent audit: not yet performed.
