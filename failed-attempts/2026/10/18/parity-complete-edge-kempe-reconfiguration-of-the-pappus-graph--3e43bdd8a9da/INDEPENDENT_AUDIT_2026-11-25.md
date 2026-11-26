# Independent mathematical audit

## correctness

PASS

The incidence model and its supplied map to the Pappus LCF graph agree. An independent replay exhausts point-to-line bijections with the incidence restriction and constructs triples from disjoint perfect matchings and their complements. Direct enumeration of named edge assignments independently checks the state count. For each pair of colors every connected component of their union is an alternating cycle, so enumerating all such switches and discarding global renaming loops exhausts the moves on the quotient. Replay confirms 42 perfect matchings, 20 unordered states (120 named), 36 edges, two opposite-product-sign components each with one universal hub and three disjoint peripheral triangles, and the claimed cycle profiles. Switching a 2k-cycle multiplies the sign of each of the two matching bijections by the same (−1)^(k−1), proving invariance; the computed components prove sufficiency and diameter two. Relabeling either ordered bipartition may flip the overall sign convention, not the sign partition.

## originality

FAIL

The central claim is demonstrably covered in the distinct published Resultary record 81d0af0022f9, which gives the same graph, quotient, single-cycle moves, entire windmill structure, counts and cycle profiles. That text is catalogued later; this is a finding about mathematical coverage of the submission against the published corpus, not a claim of earlier discovery, copying, or established priority by that entry. The parity statement not made there follows directly from the two components and a sign-reversing automorphism: (x,y)↦(x,−y), (m,b)↦(−m,−b) preserves incidence and acts with opposite permutation signs (three versus four transpositions) on the two parts. It flips every coloring's product sign; the elementary switch invariant then identifies the two components. The named count and switch diameter follow immediately from the quotient, and the perfect matching count follows from the published cycle profiles. No distinct substantive remainder is established by these additions.

## value

FAIL

For the natural Pappus graph a genuinely unknown full switch graph would be useful beyond knowing a class count: it resolves class sizes, cliques and worst-case distance. In this submission the precise finite object is already available in the distinct published match. The marginal sign label follows from the two known components, the standard matching sign invariant and one explicit reflection; the other marginal counts follow from known profiles. The package does not furnish a scientifically valuable distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
