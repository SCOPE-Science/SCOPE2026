# Independent mathematical audit

## correctness

PASS

I checked the Fano-nonline and three-layer graph descriptions by finding an isometry of their distance matrices, without using the supplied isomorphism. A resolving set must meet the separator set for each unordered vertex pair; independent bitset enumeration found zero resolving triples and 7,728 resolving quadruples, and monotonicity excludes smaller sets. Grouping bases by their three-subsets constructs each exchange edge exactly once; the independent count is 155,904 with the entire stated degree histogram. Full distance-preserving backtracking found all 336 graph automorphisms: every surviving branch respects pairwise equality of distances and injectivity, and all choices are exhausted. The 29 resulting base orbits have multiplicities 18×336, 9×168, 2×84. One exact BFS per orbit, weighted by the orbit size and halved for off-diagonal unordered pairs, reproduces the five distance counts, radius, diameter, eccentricity frequencies and all 449,820 detours, including the breakdown by distance. Each exchange can increase intersection with a target by at most one, so the Johnson term is a true lower bound. The explicit bases sharing two landmarks violate the matroid basis-exchange axiom: none of the four target-directed intermediate candidates resolves, and independent BFS gives distance three. The independent group search removes reliance on the cited group order for this census.

## originality

PASS

The supported addition is the full minimum-basis and exchange-geometry classification of the 28-vertex Coxeter graph, rather than its known metric dimension or the symmetry-reduced search method. The most similar identified catalog statements differ in the underlying graph or basis predicate, and the inspected prior same-graph metric-dimension tables do not provide the census or exchange distances. This is a best-of-knowledge decision, with a specifically identified thesis access risk.

## value

PASS

The exchange graph describes how optimal resolving sets on a canonical cubic graph can be reconfigured without using extra landmarks. Among more than 29 million pairs it gives a uniform sharp one-step detour bound, classifies exactly where lengthening occurs by distance, and certifies a non-matroid obstruction. This distinguishes structural behavior not implied by the known dimension or abstract Johnson adjacency, and supplies an exact reference for comparing other graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
