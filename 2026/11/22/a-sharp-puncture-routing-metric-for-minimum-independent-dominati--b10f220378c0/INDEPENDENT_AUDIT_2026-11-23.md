# Independent mathematical audit

## correctness

PASS

A leaf requires selection from its spoke pair, and selecting a single rim vertex with all other leaves meets the lower bound n. Every optimum thus has no hub, chooses exactly one from each pair, and its selected rim set is independent and nonempty; slides preserving those pair counts are exactly spoke toggles. For n=3 the only states are isolated singletons, and for n=4 each opposite pair and its two singletons form a P3. For n≥5 Hamming is a lower bound; a shared vertex, or insertion of a compatible target vertex before the last source deletion, provides a Hamming geodesic. Otherwise the supports are disjoint and completely cross-adjacent, so a Hamming-length route must pass through empty; toggle parity gives the lower bound of two extra. A cycle of length at least five has no K2,2 subgraph, so the only obstructed types are adjacent singletons and a singleton versus its two neighbors. A singleton buffer outside the two neighborhoods gives a four-step route for the first type; for the second, buffer a+2 survives until transfer to a−1 (nonadjacent to the buffer even at n=5), and then insertion of a+1 finishes in five steps. These are 2n distinct unordered pairs. The Fibonacci vertex count follows by conditioning on a vertex; an edge toggling a given coordinate corresponds to a nonempty allowed subset of the residual n−3 path, giving the stated edge count. For a state of size k with gaps g_i, subtracting its intersection from any target cannot reduce their Hamming distance; the maximal distance is thus B=k+Σ floor(g_i/2), attained by an independent choice in the complementary paths. Exactly singletons and two-neighbor sets must take max(B,5). Writing 2B=n+2k−o with o the odd-gap count gives the stated radius bound and singleton attainment at n≥8; at n=5 all types are exceptional, n=6 has an opposite pair of eccentricity four, and n=7 the 2-set gaps are (2,5) or (3,4) with B=5 while three vertices give B=6. For n≥6 the puncture distances are at most five and do not attain or exceed the diameter: the alternating pair is the only complementary independent pair in even length, and omitting one vertex leaves a path with a unique unordered bipartition in odd length. At n=5 exactly the five singleton/two-neighbor pairs have distance five.

## originality

PASS

The established move model and ordinary Lucas-cube metrics are prior. The supported distinct claim is the helm representation and exact puncture-induced routing penalty, its complete 2n-pair classification, and the resulting extremal geometry. The closest prior punctured-cube i-graph examined has no detours.

## value

PASS

Removing the empty state is forced by hub domination, not an arbitrary fault choice. The distance and exact exceptional-pair list tell which natural optimum-to-optimum transformations require a detour, give an optimal route, and distinguish this family from known punctured Boolean networks where no detour is needed. The radii and antipodal counts follow as useful exact features of this routing benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
