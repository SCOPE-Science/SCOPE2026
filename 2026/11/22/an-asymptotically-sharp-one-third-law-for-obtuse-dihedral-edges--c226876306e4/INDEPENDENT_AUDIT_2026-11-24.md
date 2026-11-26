# Independent mathematical audit

## correctness

PASS

For a full-dimensional simple convex 3-polytope the normal cones of vertices give 2F-4 nondegenerate spherical triangles of total area 4π; E=3F-6. Complementary normal and interior angles make an obtuse edge precisely a short fan side. A triangle with all sides at least π/2 has the same lower bound on its angles by the spherical cosine law and hence area at least π/2. For F>=7 there are at least ten triangles, so eight good ones plus the others cannot fit. At most 2m triangles meet a short side, yielding 2F-4-2m<=7 and m>=F-5 by integrality. The finite-facet witness checks: the horizontal normals of the base tetrahedron positively surround zero and the three side planes meet above its nondegenerate base. The recurrence follows from (X-R)(X²+2X/R+1); its positive coefficients uniquely expose the last triple intersection. A support level between the signed value at the apex and the maximum signed value at the other vertices truncates only that vertex. Successive new facets meet precisely their three predecessors; the initial bottom adjacencies remain. At side gaps 1 and 2 the negative cosine dominates corrections bounded by R^-3 and R^-4; gap 3 is positive and the bottom products are negative. Hence exactly F-4 edges are obtuse. The unit-normal estimate gives the strict angle ceiling once arcsin(4/R)<δ. The two proportions squeeze to 1/3, without settling either of the two possible finite counts for F>=7. The bundled CHECKER.py and VERIFICATION.md were inspected but not executed; the finite halfspace tests are supplementary.

## originality

PASS

Pass for the universal lower count and the resulting asymptotically exact density. Credit both the truncation family and the essentially immediate F-4 sign count from its published normals and adjacencies to the prior construction; they are not independent novelty claims. No equivalent universal count was established in the inspected sources.

## value

PASS

A known family already shows that the maximum dihedral angle may be arbitrarily close to right with arbitrarily many facets. Counting how many of those edges must cross the right-angle threshold is a distinct natural extremal question. The universal bound gives density one third up to an additive-one gap in absolute edge count uniformly in the angle cap, rather than merely detecting one obtuse edge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
