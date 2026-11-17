# Self-review

## Correctness — PASS
The result is an exact optimization over two independent permutahedron coordinates and two possible diagonal-simplex indices. Strict rearrangement uniquely maximizes each base permutation difference, the additional coordinate perturbation has the independently sharp bound \(4(n-1)+2\) per block, and a single explicit family simultaneously achieves both bounds. When the two indices agree, the sharp bound is strictly smaller. A direct strict-convexity argument removes all nonvertex endpoints; the equality conditions determine a unique partner and yield the factorial exact count. The outer-shell proportion follows from direct squared-radius expansion and endpoint counting. The packaged finite checker checks all true vertices and all pairs for ranks 2 through 4 and explicit witnesses through rank 100. These tests corroborate, rather than establish, the all-rank proof.

## Originality — PASS (historical priority provisional)
Ardila and Escobar's harmonic-polytope paper fixes the exact Minkowski-sum coordinates and classifies vertices and facets, but its relevant mathematical statements do not give an ambient Euclidean diameter or its maximizers. Ardila's bipermutahedron work treats a different polytope. The closest published same-object result classifies radial shells and outer-sphere contacts; it specifically does **not** determine a full pairwise-distance distribution. The present metric optimization is not implied by that one-point radial information: distinct antipodal geometry requires the simultaneous rearrangement and perturbation equality arguments. Other same-object reports treat inradius and one-skeleton degrees. Source and implication comparisons are recorded in the accompanying structured review. An independently rediscovered formula under alternate terminology remains the main priority risk.

## Mathematical value — PASS
This is a complete natural Euclidean geometric invariant of an infinite, well-studied Minkowski-sum family, with a rigid classification of **every** farthest pair rather than only a diameter value. The diameter graph unexpectedly has degree at most one despite the polytope's large vertex count. Its sparse endpoint proportion, \(1/(n-1)\), gives a concrete asymptotic separation between support on a minimum-enclosing sphere and participation in diameter pairs. No general downstream theorem is asserted or required.

## Limits
The claim is realization-specific, relies on the classical permutation rearrangement inequality and the established harmonic-polytope model, and does not solve arbitrary pairwise-distance distributions. Full historical priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
