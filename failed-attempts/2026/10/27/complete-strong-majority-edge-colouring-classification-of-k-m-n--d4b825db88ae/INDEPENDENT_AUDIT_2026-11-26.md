# Independent mathematical audit

## correctness

PASS

For two named colours both neighbourhood counts must equal half the degree. In the red indicator matrix this gives r_i+s_j−2x_ij=(m+n−2)/2. The sums over rows and columns force constant rows' and columns' red totals if both sides exceed two, hence a monochromatic contradiction. With two rows and n>2, the equal row totals force each column to be monochromatic; the red columns must be exactly half. In K₂,₂ an edge's two neighbours must have opposite colours, giving four assignments. For three colours the cyclic matrix has at most the sum of the two ceilings for each other colour; for its own colour subtract two. The ceiling inequalities hold on all stated ranges (including 4,6 and 4,n≥8); monochromatic balanced columns work in the remaining degree-two cases. Direct neighbour counting checked the small upper bounds. For K₃,₄ a single colour has at most four cells: a row of size two forces other columns empty and the selected columns to have size at most two; if all rows have size at most one the class has size at most three, and no row can have size three or four. Size four forces a 2×2 rectangle; three such classes could not fill any column of odd height three. For K₄,₅ a degree-three row restricts its colour to three columns of degree at most two. Otherwise any class of size at least seven has at least three degree-two rows and a column of degree at least two, which must hit all those rows and the remaining row to satisfy the outside bound of three. Its degree four then violates the inside bound of five. Both obstructions and all boundary cases are covered.

## originality

FAIL

Two distinct earlier-dated Resultary findings state the same minimum-colour classification on the entire frozen domain, one as part of a larger domain. The exact named census is not singled out as a separate finding there, but for n>2 the published characterization by balanced monochromatic columns already gives it by choosing the red columns, and for n=2 there are just the two orientations of the two monochromatic lines with either colour first. This is equivalent coverage of the principal classification plus an immediate count, not just a matching title or matching exceptions.

## value

FAIL

The family and threshold are mathematically natural, but the full classification is already available. The added named census simply counts the choices of half the columns after the existing rigidity theorem, plus a four-edge check. It supplies no substantive new invariant or lower-bound mechanism beyond those comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
