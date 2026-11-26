# Independent mathematical audit

## correctness

PASS

An inclusion-maximal matching leaves independent uncovered shores. Four points have 12 incidences, with at most six repeated incidences because a point pair shares at most one chosen line; at most three lines avoid those four points, ruling out size <=5. For three points, at least six lines are met, and equality (required for size six) needs one distinct available line for each pair. They form a noncollinear triangle with precisely the three allowed directions. Its horizontal/vertical corner and nonzero horizontal displacement give a unique displayed T_{x,y,a}; the three avoided lines are forced. For the reference triangle, three point-to-line edges are forced, and the remaining six vertices form a 6-cycle with two perfect matchings. Translation and simultaneous negation cover the other triangles. An independent increasing-edge-index enumeration visits each matching once and tests maximality by inspecting every edge for an uncovered pair, yielding {6:36,7:567,8:648,9:42}. It reproduces the published 36 masks and 126 exchange edges exactly. Among the 630 unordered pairs the needed exchanges are 3,4,5,6 with counts 126,54,270,180; thus one- and two-edge moves are impossible. Independent graph traversal gives degree seven, 108 triangles, and the common shell profile (1,7,12,12,4), establishing connectedness and radius and diameter four. The 108 direction-preserving affine collineations give one orbit on the 36 states. An extra independent check groups the two completions for each uncovered triangle as adjacent true twins; their 18-vertex quotient is isomorphic to Pappus, so the computed exchange graph is also Pappus[K_2].

## originality

PASS

The standard Pappus graph, edge-domination correspondence and use of incidence-free sets are prior. The same-day Pappus forcing record explicitly uses the 42 perfect matchings, so that top coefficient is not a distinct new fact here. The supported contribution is the affine classification and full census of the minimum maximal matchings, the lower-size maximal matching coefficients, and the exact three-edge exchange threshold and graph on the minima. The strongest other Pappus exchange statements act on different configurations; similar incidence-free exchange results on other graphs do not imply this exact census or mobility graph.

## value

PASS

The Pappus incidence graph is canonical, and minimum maximal matchings model minimum edge domination on it. Describing all optima by complementary affine triangles explains their geometry rather than just outputting 36. The exact jump from every optimum isolated at budget two to a single connected transitive graph at budget three is a meaningful finite reconfiguration cutoff with a useful complete distance profile. It cannot be read off from the optimum cardinality or from the previously known perfect matchings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
