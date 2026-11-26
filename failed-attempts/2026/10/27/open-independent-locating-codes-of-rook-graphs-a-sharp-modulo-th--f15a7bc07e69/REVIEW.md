# Independent mathematical audit

## correctness

PASS

The degree-one condition forces selected components to be dominoes, and line sharing would connect two components. In the line-graph model R_{a,b}=L(K_{a,b}), selected cells correspond to edges forming vertex-disjoint two-edge paths in K_{a,b}; selected sets in a row or column are the selected edges incident to its endpoint. Two unused rows give identical signatures in a used column, two unused columns likewise, and intersecting unused lines cause non-domination. With an unused row, any horizontal domino causes a singleton signature collision with its selected mate; hence only vertical dominoes are possible. With full coverage, each unselected signature is the disjoint union of two nonempty endpoint sets and cannot equal a selected singleton. A same-line collision is impossible by disjointness of the other endpoint sets. A collision in different rows and columns would force crossed row/column sets to agree, hence each must be the singleton at the intersection, contradicting that every selected edge has an endpoint of selected degree two. With one unused row and all vertical dominoes, singleton, doubleton and triple signatures separate selected cells, unused-row cells and other cells; a triple's unique full selected column pair and its third cell recover the two coordinates. Transposition handles one unused column. The full-coverage constraints are h+2v=a and 2h+v=b. Partitioning and matching the labeled rows and columns yields a!b!/(2^(h+v)h!v!). The unused-line counts follow by reserving that line and assigning unordered pairs to the other side. The component weights XY^2/2 and X^2Y/2 give the EGF, dropping empty components as required for positive side sizes. For a=1 the rook graph is K_b: selected degree one forces two cells, and locating permits at most one unselected cell, so b=2 or 3 with counts 1 and 3. The transposed case and R_{1,1} agree, as does the square specialization.

## originality

FAIL

A distinct indexed rook-code result explicitly matches the complete rectangular-family classification and counts for both sides at least two. The one-dimensional cases are immediate complete-graph cases, and the EGF, square specialization and examples follow from the same factorial census. The older induced-matching and dissociation results alone do not cover the locating criterion. This is exact indexed coverage, not a claim of publication priority.

## value

FAIL

The sharp signature criterion is meaningful for the natural rook family and would be of interest apart from overlap. Here the identical classification and census are covered. The added generating-function form, examples and complete-graph boundary do not establish an independent worthwhile unknown exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
