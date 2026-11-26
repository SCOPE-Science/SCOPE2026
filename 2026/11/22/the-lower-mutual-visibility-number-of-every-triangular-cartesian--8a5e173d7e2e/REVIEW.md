# Independent mathematical audit

## correctness

PASS

In the strip a shortest path is a horizontal segment if rows agree, and otherwise switches once at a column between the endpoints, inclusive. A boundary closed neighborhood of size four is visible (for the two nonadjacent pairs switch rows in column 1), and is maximal because all paths out of its center start with a selected vertex. Every pair extends by completing its column when co-columnar, or by adding a vertex at one endpoint's column in a row not used by the pair and putting any necessary switches at the other endpoint's column. For triples there is also a direct all-length argument independent of computation. A 2+1 distribution extends by filling the double column: from the singleton switch at its column, then travel in the target row. A full column extends into any existing neighbor. For one vertex in each of three occupied columns, add a fourth vertex in the middle column. For any outer-to-middle pair, switch if needed at the outer column; the other selected middle vertex cannot block the path. If outer rows are equal, visibility forces the existing middle vertex to be in a different row, and the added vertex uses the remaining row. If outer rows differ, choose a middle double that omits an outer row (pick an outer row different from the current middle row to omit); the outer-to-outer geodesic uses that omitted row between the outer columns and switches at the opposite outer endpoint. This proves the strengthened assertion and lower bound even for consecutive occupied columns. The original normalized certificate is valid as well: each empty gap of positive interior length supplies one equivalent switch option, while every occupied switch location stays distinct; same-row paths only test the order of selected columns. The independently replayed seven types yield 133 visible triples, 132 in-column extensions, and one full-column exception with all three neighboring-row additions working.

## originality

PASS

The supported distinction is the all-n lower bound and extension property for triangular path cylinders. The upper bound is an application of the prior Neighborhood Lemma. The same-graph maximum results, four-row lower results and triangular tori give different mathematical statements.

## value

PASS

The triangular strip is the first nondegenerate cycle fiber in the published cylinder problem. An exact invariant at every length, and a local extension for all visible triples, are useful boundary results for that problem. The extension shows why extreme gap size between occupied columns cannot generate a small maximal obstruction in this family; it is not a maximum-value table entry or merely the prior neighborhood bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
