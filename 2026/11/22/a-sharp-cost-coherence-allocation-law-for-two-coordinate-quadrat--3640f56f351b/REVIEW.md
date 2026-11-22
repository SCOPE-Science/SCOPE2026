# Mathematical review

## Correctness — PASS

The exact coordinate step is an orthogonal projection in the transformed energy coordinates. Dividing by expected work transforms the objective into the smallest eigenvalue of a two-atom information matrix with a linear price budget. The constructed unit witness has a constant Rayleigh quotient at every feasible design, providing a global upper bound. The explicit positive allocation attains it, and the independent projection directions force uniqueness. The arithmetic–geometric mean inequality supplies the sharp gain bound and its limiting extremizers. The supplementary verifier passed 35,662 rational/numerical assertions; universality and uniqueness follow from the written proof rather than finite sampling.

## Originality — PASS, with publication-priority risk

Rodomanov and Kropotov (arXiv:1904.04587v1) develop volume sampling for randomized coordinate descent, not the present exact price-normalized spectral optimum. Csiba and Richtárik (2018) incorporate work in complexity bounds but optimize a different separable upper bound, not the exact worst-direction quotient. A published planar Kaczmarz result obtains uniform two-row sampling with no prices; a published two-row work-budget result allows batched/no-op masks but gives singleton rows equal prices. Neither stated claim implies the nonuniform rule derived here. The 1952 Elfving and 2000 Martinez–Wegman design sources are relevant equivalent formulations, but their complete primary texts were not accessible; a specialized E-optimality corollary remains a substantial precedence risk. Source comparisons distinguish actual coverage from lack of search results.

## Value — PASS

Heterogeneous coordinate evaluation costs arise naturally in randomized first-order methods. Existing curvature-based probabilities do not optimize a price-dependent exact worst-direction one-step objective. The complete two-coordinate solution identifies a structural, continuous transition from equal selection to inverse-square-root cost as coupling approaches singularity, with a sharp improvement limit of two. The result is a meaningful finite-dimensional design law, not a claim about long-run rates or actual wall-clock gains.

## Closest literature and limitations

Primary comparisons: Rodomanov–Kropotov (2019), Csiba–Richtárik (2018), *Planar coincidence theorem for optimal randomized Kaczmarz sampling* (2026), and *Sharp work-budget phase transition between one-step and asymptotic randomized two-row Kaczmarz* (2026). The result is restricted to fixed nonadaptive single-coordinate exact minimization on real two-dimensional positive-definite quadratics, with exogenous positive work prices and worst-direction expected one-update progress per mean work. An independently established priority claim is not made.

Self-review: passed. Independent audit: not yet performed.
