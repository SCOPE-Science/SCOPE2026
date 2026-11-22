# Scientific assessment

## Correctness — PASS

The weighted Laplacian and single diagonal pin have a strictly positive quadratic form. The exact-rational verifier establishes four disjoint characteristic-root intervals for each of twelve pinned matrices, exhausting the degree-four spectra. Its interval-ratio comparisons prove all nine strict global winner inequalities; continuity proves at least two switches and robust winner identities. A separate grounded-principal-minor argument proves vertex 2 uniquely minimizes the condition number for all sufficiently large gains. This is a finite exact theorem, not an inference from approximate eigenvalues.

## Originality — PASS, subject to literature coverage

Jalili, Askari Sichani and Yu (2015) use the same extremal eigenratio and optimize driver placement, and Orouskhani, Jalili and Yu (2016) separately optimize driver sets and gains. The latter already recognize dependence of optimal driver sets on gain, so that general observation is prior knowledge. The inspected works do not state or imply the exact return of a unique optimum on a fixed four-vertex weighted path. Jafarizadeh (2024) derives a more general weighted-network optimization program including singly pinned paths, but optimizes edge weights and feedback gains jointly; that does not provide these fixed-parameter comparisons. Indexed public mathematical research comparisons and the available historical claim corpus did not reveal this same finite example. Incomplete and unindexed coverage leaves a publication-priority risk.

## Value — PASS

One-time centrality rankings and simple monotonic-in-gain rules for pin-location selection are appealing shortcuts for a computationally intensive eigenratio objective. The strict, exact and perturbation-stable return on the smallest practical example explored here shows such monotone rules are unsound in general, and supplies a tiny reproducible regression test for gain-aware pinning optimization. Its significance is the robust qualitative counterexample, not its graph size or a quantitative gain-factor improvement.

## Scope and residual risks

Three specified positive gain values and the eventual large-gain winner are classified, with no minimum-order assertion, full switching diagram, independent audit, or dynamical stability theorem beyond the chosen proxy. The closest primary texts are listed in RESULT.md; related results absent from indexes may exist.

Self-review: passed. Independent audit: not yet performed.
