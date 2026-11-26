# Independent mathematical audit

## correctness

PASS

Every three-edge simple path is shortest, since a shorter path between its ends would yield a cycle of length at most five. Hence selected-edge components are stars (there are no triangles), and including isolated vertices gives at least four components on 16 vertices. Equality at 12 edges consists of four disjoint full cubic stars, whose centres partition the vertices by closed neighbourhoods. For an independent finite check, reconstruct the labelled GP(8,3), BFS from each vertex, and for every endpoint pair follow all edges that increase distance from the source and decrease distance to the target. This exhausts the 216 shortest paths up to reversal and gives 192 distinct triples, including nonconsecutive triples on length-four paths. Increasing-edge-index recursion counts each triple-free set exactly once, and testing all single additions detects every facet by heredity. The resulting face vector is (1,24,276,1832,7362,17712,24468,18240,7017,1576,300,48,4), with 78860 total; the nonzero facet coefficients are 792,1329,336,36,4 at sizes 7,8,9,10,12. The independently checked closed-neighbourhood codes give exactly the four maximum star sets. Their six pairwise intersections have size four, so the simultaneous replacement distance is exactly eight. The four maxima each have twelve distinct size-eleven subsets and no two maxima share one; these account for all 48 such admissible sets and establish unique extension.

## originality

PASS

The efficient dominating codes themselves are covered by prior perfect two-colouring work and must receive prior credit. What distinguishes this finding is the exact edge-geodesic complex, including its face and facet profiles, the characterization of its optimum sets by those codes, and its near-optimum extension result. The checked stronger-looking graph-family and parameter results do not give this complex or those profiles.

## value

PASS

The classical symmetric cubic girth-six graph is a natural test of how edge general position interacts with efficient domination beyond the tree and cube settings. The distinction between vertices of the facet size spectrum matters: non-largest maximal sets exist at sizes seven through ten, yet an admissible eleven-edge set has exactly one largest extension. This is precise information about local maximality and stability, not a recomputation of known perfect codes or a bare maximum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
