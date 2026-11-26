# Independent mathematical audit

## correctness

PASS

In the bipartite Kneser representation independence places each selected right edge in F(A), while domination excludes every unselected right edge from F(A); swapping the roles gives the second closure equality. With one side of size 0, 1 or 2, the opposite side under F has respective size 10, 7, or 4/5 according as a pair is disjoint/intersecting. This proves the lower bound six and identifies the (2,4) and (4,2) minima as matching-versus-complement on four labels. A (3,3) state comes precisely from a triangle or P4: a triangle closes to itself; for path ab,bc,cd the opposite side is ac,bc,bd and closes back. The other triple types on five labels, star and P3 plus isolated edge, give sizes four and two under F. There are ten triangles, plus six matching/complement states and twelve path states on each four-set. Any jump of independent dominating sets is a slide because the entering vertex must have a selected neighbor in the old state and no such neighbor can survive. Triangles cannot slide since reducing one side yields an intersecting pair, which would require five on the other side. For each path state, deleting the middle edge in either part and adding its disjoint partner in the other part leads to the two matching-index states; removing a terminal edge would leave an intersecting pair. The two induced matchings are distinct; for every ordered pair of distinct matching indices on a four-set there are two choices of the common middle edge, giving two subdividing vertices per link of K3,3 minus its matching. No slide moves between support sets. Each doubled-and-subdivided hexagon is a 12-cycle with twins added at its six subdividing positions; every vertex has an antipodal position at distance six and all distances are at most six. This gives 120 edges and degrees 0,2,4 with counts 10,60,30. A fresh direct GP(10,3) program reproduced every minimum and transition invariant and the exact 30-edge isomorphism, and a separate 1024-mask closure evaluation reproduced all 187 entries counted by the frozen profile table.

## originality

PASS

The supported distinct result is the full minimum-layer reconfiguration graph on this host, including its exact structural decomposition. Host aliases and jump-versus-slide equivalence are background. The scalar value six is reproduced but not assigned standalone originality. The strongest available same-predicate catalogue comparison concerns prisms, and the strongest same-host mobility comparison concerns zero forcing. Neither determines the audited feasible layer or its edges. The exact same-predicate i-graph literature and cited cubic and generalized-Petersen papers leave an explicit access risk; no exclusion is asserted for their unread contents.

## value

PASS

The canonical cubic Desargues incidence graph has a natural minimum coverage-with-independence layer. Its decomposition shows a specific obstruction to mobility: two kinds of exact structure coexist, ten frozen optima and five internally navigable components with a sharp common eccentricity. The matching/triangle/path description explains the components rather than merely reporting a scalar optimum or an arbitrary finite slice, and provides a fully specified test case for independent-domination reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
