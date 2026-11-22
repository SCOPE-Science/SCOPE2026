# Review: A sphere-to-capsule crossover in extreme surface-chord distributions

## Correctness — PASS
For each positive axial half-length the antipodal poles are the only diameter endpoints. The cap parametrization produces a positive-definite quadratic distance deficit, whose four-dimensional ellipsoid volume and exact product surface density yield the \(arepsilon^2/[4a(a+r)]\) coefficient. Even Taylor remainders give the stated fixed-parameter \(O(arepsilon^3)\). At the spherical endpoint the exact dot-product law gives a linear tail. In the double scale \(a=\lambdaarepsilon\), localization near antipodal sphere directions produces the integrated positive-part profile. The negligible seam and cylindrical-band masses are accounted for. `verify_capsule.py` independently integrates the exact Cartesian cap distances and passed 35 checks; finite computations corroborate rather than replace the proof.

## Originality — PASS (provisional historical comparison)
The primary full text of Mayer–Molchanov (2006) includes the spherical case but not shrinking capsules; Schrempp (2017) concerns volume-supported distributions. Three closely relevant published full-theorem/proof texts were read: capsule central-section areas, near-sphere volume-sampled ellipsoids, and invariant-line chords of finite cylinders. The four sampling/observable differences prevent their statements from implying the present coupled theorem. published-finding corpus search covered alternate names and nearby formulations. A hidden older stereological surface-distance calculation remains possible; an unsuccessful search is not uniqueness proof.

## Value — PASS
A natural geometric probability statistic changes its tail power discontinuously as a capsule becomes a sphere. The exact, nontrivial transition profile has a sharp \(C^1\)-to-\(C^2\) regularity failure at \(\lambda=1/2\), and the coefficient reconstructs the capsule radius and axial half-length from diameter and one probability tail.

## Scientific limitations
The fixed-shape remainder is not uniform as the axial segment vanishes; the moving-parameter formula is only for fixed \(\lambda\). The law is restricted to three-dimensional round capsules and independent complete-boundary surface-area sampling. No absolute historical priority or independent proof certification is asserted.

Self-review: passed. Independent audit: not yet performed.
