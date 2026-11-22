# Scientific review

## Correctness — PASS

Equation (9) of the originating article gives the displayed ordinary difference map at order one. The piecewise-quadratic potential \(H(y)=\eta y|y|/2-y\) creates an exact, signed quadratic coboundary on any one-sided phase segment. Telescoping it bounds the sum of squared inputs; the nonzero sigmoid input and its global derivative bound rule out segments longer than the displayed explicit \(M_R\). Invariance then gives \(\mu(y>0),\mu(y<0)\ge1/M_R\). Removing cubic feedback decouples the input, makes its sign fixed and bounded away from zero after the initial steps, and forces linear phase escape. The analytical proof handles endpoint values, all real parameters in scope, non-ergodic invariant measures and arbitrary bounded initial states. The standalone rational diagnostic passed 93 exact identity tests and the standard-library numerical diagnostics passed; they are not substituted for the proof.

## Originality — PASS within inspected evidence

The exact model, its numerical bifurcations and entropy studies, and its controlled variants were inspected in Al-Taani et al. (2024). The published absence of equilibria is strictly weaker than either a no-bounded-orbits result on the feedback-zero face or a finite-visit property for all compactly supported invariant measures. The later same-author 2025 memristive article describes a different two-dimensional map. Indexed sign-crossing and sigmoid-spiking statements concern different equations and do not imply this theorem; related continuous-time obstruction techniques are acknowledged, not claimed as new. Searches and exact comparisons are recorded in AUDIT.json. Unindexed equivalent priority, and inaccessible full text of relevant indexed summaries, remain explicit risks.

## Value — PASS

The source investigates hidden dynamics principally numerically. This theorem supplies a parameter-uniform, testable necessary geometry of compact recurrent dynamics: any invariant probability must charge both signs of the memory phase by a quantitative amount, and no bounded orbit survives removal of cubic feedback. The finite-block estimate is not sharp but is mathematical information about every bounded orbit, independent of whether a chaotic attractor exists. It helps interpret reported bifurcation diagrams and the feedback parameter without making security or physical-measure claims.

## Closest literature and limits

Sources: Al-Taani et al., *Symmetry* 16 (2024), 1447, DOI 10.3390/sym16111447, and Al-Taani et al., *Symmetry* 17 (2025), 143, DOI 10.3390/sym17010143. Indexed analogies for the Sprott E flow and a two-cell sigmoid-spiking map concern different dynamics. The result is integer-order only; arbitrary noninteger fractional-order histories are not treated. The constant may be conservative, and unpublished or unindexed equivalents are not excluded.

Self-review: passed. Independent audit: not yet performed.
