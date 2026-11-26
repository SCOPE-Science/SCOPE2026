# Independent mathematical audit

## correctness

PASS

The complement of a three-path cover has induced maximum degree at most one. A size-eight such set can be assumed to have at least four points by Fano duality. With four points there are at most three lines meeting them at most once (and only one if the four points complement a line); with five points there is only one such line and with six or seven none. Size seven is attained by each shore. The one-point and two-point cases cannot supply enough allowable lines, nor can their duals. In a three-point/four-line optimum the points cannot be collinear (each remaining line meets their line, so four incidences would repeat a point). For a noncollinear triple each point has exactly one nonside line through it, so all four nonside lines together form a valid state. Its complement is also valid: the three side lines each meet the outside points once and their outside neighbors are distinct, as every pair of side lines meets within the triple. Duality gives exactly 28 states with four points, so these complements exhaust that case. A same-type swap is impossible since either the triangle or its side-line set determines the other (the triangle is the set of pairwise intersections of its sides). The pure shores are isolated. Cross-type jumping requires disjoint triangles; then the unique line in neither side set meets both triples at most once and must contain the one omitted point. Thus each cross-type jump slides along that incident flag, giving precisely the categorical Coxeter double. Independent direct enumeration of covers over all 42 simple three-vertex paths, construction of both move graphs and BFS from every mobile root confirm cardinality seven, 58 states, two isolates, 84 mobile edges, and shells (1,3,6,12,18,12,3,1), hence mobile radius and diameter seven.

## originality

PASS

Pass the exact optimum-cover realization and slide/jump equality, not the classical Coxeter graph, the double-cover operation, or their abstract graph metrics considered alone. The strongest related same-day record has an especially close Coxeter connection but a different optimizer family, state graph, and slide behavior. The checked statements support this distinction; neither catalogue dating nor inaccessible literature fixes priority.

## value

PASS

This is an exact solution of a natural mobility question for a standard cubic geometry, not just an enumeration of the frozen states. The Fano incidence proof explains why an apparently stronger jump operation never adds a move and identifies the classical cubic lift governing all remaining configurations. The isolated-versus-mobile split and exact shell profile make a useful comparison instance for optimum-cover reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
