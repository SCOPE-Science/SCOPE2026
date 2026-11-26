# Independent mathematical audit

## correctness

PASS

Cells correspond to simple bipartite edges. A base degree at least three makes a triangle in the induced line graph; with maximum base degree two the base components are paths, even cycles and isolates, so the induced line graph is bipartite. The product of the two unsaturated sets must consist wholly of selected edges for maximality. When both are nonempty, each vertex there has degree at most one, so they are singletons joined by an isolated edge. Both degree sums are then one less than twice their shore sizes, forcing a square. Otherwise a shore is saturated; edge capacity makes it the smaller shore on rectangles and both shores on squares. These criteria are sufficient too. In the saturated classes only isolated larger-shore vertices, alternating paths with one extra larger-shore vertex and even cycles occur. Dividing alternating list counts by orientation and, for cycles, label starting position gives k!(k+1)!/2 and (k!)²/(2k). The resulting labeled EGF is g(xy)exp(y h(xy)); exactly n−m factors carrying an extra y gives the stated coefficient. The other square class amounts to choosing the two isolated-edge endpoints and a two-factor on the remaining labels. A two-factor on one row and one column is impossible, while spanning even cycles realize both sizes for n≥3; a single alternating path on all rows and m+1 columns realizes the rectangular size. Independent direct two-coloring and single-cell extension tests agree with all five checked polynomials.

## originality

PASS

The supported distinct finding is the complete inclusion-maximal facet classification and enumerator, in particular the rectangular purity versus square nonpurity transition and exact contribution of smaller square facets. The larger square coefficient B_n and finite-board entries are demonstrably prior, not separate new results. The prior path-and-cycle generating functions also supply ingredients for the rectangular top coefficient. Neither those ingredients nor the strongest inspected homology and enumeration results give the inclusion-maximal classification at all parameters.

## value

PASS

The classification locates exactly when all inclusion-maximal bipartite choices on the natural rook graph are optimal and when a second facet dimension occurs. The nonmaximum square class gives genuinely useful facet data that an ordinary face enumerator or top-coefficient census does not isolate. Having the combined size distribution and its sharp shape criterion for the degree-two chessboard complex is a meaningful exact result; the individual already-known top counts are not its contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
