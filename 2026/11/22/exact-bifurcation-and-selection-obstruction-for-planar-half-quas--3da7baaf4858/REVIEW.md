# Independent mathematical audit

## correctness

PASS

For t>0 reflection to the positive quadrant strictly improves any negative coordinate; when the input is feasible t≤1/4 its unique nearest point is itself. Outside, compactness ensures a minimizer, which must lie on the boundary since any interior point can move toward the target. On the positive boundary set s=x−y; then x+y=(1+s²)/2 and −1≤s≤1, with x=(1+s)²/4, y=(1−s)²/4. Squared error is (1+s²−4t)²/8+s²/2. As a strictly convex quadratic in s² its minimizer is 4t−3 clipped to [0,1]. This establishes all fibers, including the singleton at t=3/4 and the two endpoints at t=1. Substitution gives the four stated distances. The first derivatives match at the joins (0, 2, 2 respectively); the second derivatives jump 0→4, 4→0, and 0→4. At t=3/4+δ the two branches differ by norm 2√(2δ) and each lies at distance √(2δ+2δ²) from the singleton, verifying sharp local exponent 1/2. Independently of the swap argument, if w is any nearest point to z, then along z_s=(1−s)z+s w, 0<s<1, w is the unique nearest point: the squared-distance gap to any y≠w is (1−s)(||z−y||²−||z−w||²)+s||y−w||²>0. Two distinct w at each t>3/4 therefore force incompatible limits for any planar local selection.

## originality

PASS

The supported distinct content is the complete explicit diagonal classification, including where nonuniqueness begins and the sharp geometry of its onset. The general ℓ_p projection problem, coordinate-ordering lemma, and obstruction once a fiber is known to contain two points do not, by themselves, constitute a separate novelty claim. The inspected general methods do not state or supply without additional global minimization the specific diagonal phase diagram.

## value

PASS

The dimension, exponent and equal-coordinate line are intrinsic to the smallest symmetric nonconvex projection example in this family. The complete classification gives a usable exact benchmark for positive-coordinate, diagonal and axis solutions, proves when symmetry breaks while the distance stays differentiable, and distinguishes the onset of nonunique projection from the mere fact of nonconvexity. These exact transition locations and branch sizes matter for checking projection or branch-selection algorithms; value does not rest on the elementary conditional obstruction to selecting two nearest points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
