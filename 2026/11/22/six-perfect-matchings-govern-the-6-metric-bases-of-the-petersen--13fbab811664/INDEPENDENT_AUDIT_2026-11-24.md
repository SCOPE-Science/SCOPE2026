# Independent mathematical audit

## correctness

PASS

Reconstructed the line graph on the stated GP(5,2) edges, not the vertex metric on the Petersen graph. An independent exhaustive calculation of distances and all 105 unordered pairs reproduced 105 distinct five-element bisectors. A set S guarantees |S| minus its maximum bisector intersection, so evaluating all 32768 masks certifies all ten dimension and count rows, with no k above ten feasible. Separately enumerating the perfect matchings on the ten original vertices gives exactly the six complements of optimal six-metric bases. Every 11-subset contains a bisector, so cannot be a 7-generator; every (k+5)-subset has at most five nondistinguishing landmarks. Deletion lowers the guaranteed multiplicity by at most one, so the lower bound at seven propagates to k=8,9,10 and all these claimed minimizers are exact. As a structural check on bisector cardinality, represent a Petersen edge by two disjoint pairs in [5]. The missing symbol groups its line-graph vertex into one of five triples; distance three is exactly the two other vertices of that triple. Within a triple the two disjoint four-neighbor sets leave four equidistant vertices outside plus the third member. Across triples each vertex has one neighbor in the other's triple, and there is exactly one common neighbor (the third edge at a shared endpoint for distance one; the unique bridging edge for distance two). Among the nine vertices outside both triples the two three-neighbor sets then have symmetric difference four, again leaving five equidistant vertices. This reasoning supports sizes; distinctness and the bases census were checked exhaustively.

## originality

PASS

The supported contribution is the full labeled robustness census and the perfect-matching classification at k=6. Possible earlier knowledge of the ordinary metric dimension or its fault-tolerant variant is not credited as novel. The strongest identified statements on the same graph concern different landmark tests, or just the standard metric-dimension parameter.

## value

PASS

The Petersen line graph is a canonical test for robustness under landmark loss. At the boundary k=6 the least-size sets are governed by a different invariant of the underlying graph (perfect matchings), while at k=7 the optimum size jumps by two and every set of that size works. The exact counts and uniform bisectors separate these regimes and give useful benchmark data beyond the ordinary dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
