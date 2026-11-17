# Independent mathematical audit

## correctness

PASS

For G_n=K_(n+1,n+1)-M_n and n>=4, distances are 1 for present cross-edges, 2 for same-shore pairs, 3 for missing matched pairs. Checking allowed internal vertices gives the three explicit conditions L,R,P in occupancy classes (c,d,e,h) plus unmatched omission flags u,v. Every omitted vertex maps to one of six occupancy updates; all comparisons have thresholds <=3, so capping counts at 4 preserves both current visibility and all single-addition maximality decisions. The 2360 capped states exhaust the parametrized classification into seven disjoint cases, giving the six-term polynomial and all boundary coefficients. Fresh independent BFS direct visibility through n=6 agreed, as did independent 2360-state check.

## originality

PASS

This is ordinary mutual visibility requiring a geodesic avoiding other selected vertices, not total/dual visibility; near-crown K_(n+1,n+1)-M_n has two unmatched vertices and is not the perfect crown K_(n,n)-M_n. Bujtas, Klavzar, Tian visibility-polynomial theory includes complete bipartite classes and general definitions. A Resultary theorem on matching-deficient TOTAL mutual visibility concerns a different predicate, so its polynomial does not imply the maximal ordinary mutual-visible sets here. An all-subset polynomial of the perfect crown or a total-visibility enumerator cannot be specialized to the new graph and maximality criterion without additional geodesic and extension analysis; the explicit capping classification establishes the missing implication. Best-of-knowledge originality with disclosed residual risks; no search failure alone is treated as novelty proof.

## value

PASS

The first exact complete maximal mutual-visibility cardinality polynomial for a natural matching-deficient near-crown family resolves both extreme sizes and the unbounded holes in its support. The explicit finite-state reduction is mathematically motivated by geodesic obstructions, not an arbitrary tiny graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
