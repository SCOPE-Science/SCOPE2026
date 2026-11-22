# Review of the weighted-cycle circumsphere finding

## Correctness — PASS
The maximum-norm certificate is valid for the whole zonotope because Euclidean norm is convex and the zonotope is the linear image of a cube. The sign-product identity, the cycle parity constraint and positive products yield the claimed radius and every contact sign pattern. Central symmetry gives the unique minimum-ball center. For even cycles, the equality constraints are exactly alternating neighbor-sum solutions. For odd cycles, the average over all single-defect quadratic forms yields a positive cyclic Fourier spectral lower bound, which proves uniqueness and quantitative stability. A standalone standard-library exhaustive-enumeration checker validates 3,360 finite examples; this is a test of computations rather than a replacement for the proof.

## Originality — PASS, with priority risk
The 2021-11-24 Padrol--Pilaud--Poullot preprint proves the natural all-positive-edge deformation parameterization for triangle-free graphs; its metric assertions do not include a fixed-total-weight circumradius minimization. Pešović--Stojadinović primarily study generalized-permutahedron interpolations and weighted integer-point enumerators; Winter classifies homogeneous/vertex-transitive zonotopes under different hypotheses. Existing unit-weight cycle distance/circumsphere facts already imply the unweighted special cases and are not new parts of the priority claim. The new joint assertion is the exact weighted contact classification and the odd/even fixed-budget minimizer set and stability bound. Searches did not identify an equivalent general weighted-cycle theorem; an unindexed equivalent remains possible.

## Mathematical value — PASS
The positive rescalings parameterize a full natural deformation family, and fixing total generator length is intrinsic to comparing deformations at a common geometric budget. The all-weight contact classification explains how the limiting farthest-vertex orbit changes with adjacent edge-weight products. More importantly, the precise fixed-budget minimizers exhibit a qualitative rigidity dichotomy: odd cycles force a unique equal-weight realization while even cycles have a one-dimensional continuum; the quantitative odd-cycle estimate measures departure from optimality. This is a complete natural special-family optimization, not a parameter renaming or mere numerical evaluation.

## Residual limitations
Historical priority has not been independently verified. Only cycles with at least four vertices and strictly positive generator weights are included, in the standard Euclidean incidence realization. The odd-cycle stability coefficient is sufficient but not claimed optimal. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
