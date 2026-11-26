# Independent mathematical audit

## correctness

PASS

Independent global check: for five sphere points in general affine position, the affine dependence partitions the labels into two and three vertices (a singleton would be a convex combination, impossible on the strictly convex sphere). Thus the segment of the two meets the interior triangle of the other three, and the hull is the union of the two pyramids over that triangle. Its volume is the triangle area times the difference of the apex normal projections divided by three. The area is <=3*sqrt(3)/4 because the base plane cuts the sphere in a circle of radius <=1 and an equilateral triangle maximizes area in its circle; the apex projection difference is <=2. Equality requires a great-circle equilateral base and antipodal apices normal to it. The bound and equality analysis also apply to degenerate limits by approximation by generic tuples, selecting a subsequence with the same apex labels, and using continuity of the two factors. This independently establishes V*=sqrt(3)/2 and the equality configurations. Compactness therefore localizes the small deficits to those maximizing orbits. Order the two apex labels by a fixed convention; there are ten pairs and two base orientations, giving twenty distinct labelled rotation orbits. Exchangeability and reflection yield equal weights in symmetric neighborhoods. Near a maximum the apex segment continues to cross the base plane inside the triangle, so the signed determinant volume formula is indeed exact. Fixing one apex by isotropy and removing the common equatorial azimuth give the stated seven coordinates and a local density 2*pi/(4*pi)^4 / sqrt(1-u²-v²). Independently ran `python audit_checks/independent_replays.py 5`, constructing the second-order equatorial point jets and expanding the oriented volume; the quadratic matches every term of H/2, including the u/z and v/z sign pattern. The spectrum is 1/6 twice, 1/3, 2/3 and 1 three times; determinant 1/162. Integration over the small ellipsoids gives 20 times (1/(128*pi³)) times (16*pi³/105) times 2^(7/2)/sqrt(1/162) = 24/7. Positive definiteness bounds x by O(sqrt(epsilon)); in H^(1/2)x/sqrt(2*epsilon) coordinates the sublevel indicators converge a.e. to the unit-ball indicator with a common bounded support and the rescaled density factor tends uniformly to a constant. Normalizing and using dominated convergence gives L1 and thus total variation, not merely weak convergence. The normalized deficit differs from squared rescaled radius by O(sqrt(epsilon)) on the event, yielding the Beta(7/2,1) limit. The submitted symbolic code was inspected; the independent replay checks local algebra, not localization or convergence.

## originality

PASS

The deterministic inscribed maximum is credited as prior, and quadratic sublevel localization is a general method. The supported distinct contribution is the evaluated sharp fixed-five surface-sampling tail coefficient and the seven-coordinate conditional total-variation law. The retrieved nearest statements do not cover this combination; inaccessible passages and unknown prior endpoint calculations remain risks, not evidence of absence.

## value

PASS

The five-vertex triangular bipyramid is the first nonsimplex inscribed volume maximizer in three dimensions, making this a natural fixed-sample stochastic benchmark beyond the tetrahedron. The exact constant combines branch multiplicity, a coupled pose/shape Hessian and the surface probability measure; it does not follow by substituting the maximal volume into a general law. The total-variation conclusion describes the geometry of successful configurations, not just their frequency. No higher-order expansion or result for other sampling laws is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
