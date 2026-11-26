# Independent mathematical audit

## correctness

PASS

In KG(5,2), distinct intersecting root pairs have distance two because their union leaves a common disjoint pair. For a Petersen edge ab its distance-two set is exactly the four cross-pairs between a and b. These are 15 distinct root four-cycles with one isolated ground label; the two missing diagonals recover ab. Domination fails precisely on subsets of these blocks, so is automatic from size five. Independently reproduced the full finite census in a bounded JavaScript calculation: construct GP(5,2) in outer/inner coordinates, take all-pairs Floyd–Warshall distances, and take minima to endpoints for each edge column. For each of the 105 pairs of edge columns mark every submask of their agreement mask as nonresolving; likewise mark all submasks of the 15 far masks as nondominating. There are 40 distinct agreement masks, with maximum size six. Tallying all 1024 masks gives resolving counts (0,0,0,0,15,162,195,120,45,10,1), dominating (0,0,0,60,195,252,210,120,45,10,1), and joint (0,0,0,0,0,162,195,120,45,10,1). The two failed-predicate flags at size four are complementary for every mask, not merely in aggregate. To reconstruct the orbits, assign Kneser labels 01,23,04,12,34 to the outer cycle, and 24,14,13,03,02 to the respective spokes' other endpoints. Permuting the five labels on each supplied representative gives pairwise disjoint complete orbits of sizes 5,10,15,60,60,60 and 60,60,60,30,30,12 in table order, and exactly the stated yes rows and root types. S5 is also the full automorphism group: the five maximum independent sets are the root stars (an intersecting family without a common label has size at most three), and their pairwise intersections determine every vertex. Both provided scripts and both saved outputs were inspected but not executed; the agreement-mask reconstruction independently tests the exact claim.

## originality

PASS

Current evidence supports the structural four-set incompatibility and complete joint census as distinct from the known scalar edge-metric dimension and the prior definition of the joint invariant.

## value

PASS

Petersen is a natural small symmetry-rich test for a pre-existing joint edge identification and coverage invariant. Its entire set of ordinary optimal sensors is precisely the set failing coverage, a stronger structural result than a one-unit numerical gap between optima. The four types at the true joint minimum describe the possible optimal layouts and the polynomials quantify redundancy over all sizes. This is useful as an exact benchmark without implying a general theorem for all generalized Petersen graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
