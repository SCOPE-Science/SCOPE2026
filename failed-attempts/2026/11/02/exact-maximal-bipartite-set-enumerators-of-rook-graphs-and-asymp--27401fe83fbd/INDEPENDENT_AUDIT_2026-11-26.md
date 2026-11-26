# Independent mathematical audit

## correctness

PASS

Selected cells are edges in a complete bipartite incidence graph. Occupancy >=3 gives a rook triangle; if every incidence degree is at most two the components are paths/even cycles, whose line graphs are bipartite. For maximality, any row and column both of degree <=1 must already meet in a selected cell. If both deficient classes are nonempty this forces exactly one of each, both of degree one at the common cell, and 2m-1=2n-1. Otherwise a whole shore is of degree two, necessarily the smaller shore on a rectangle. The independent labeled-column monomials thus count exactly the rectangular class. On a square the two classes consist of a spanning simple bipartite two-factor, or an isolated selected incidence at one of r^2 pairs plus a two-factor on the remaining board. Alternating cycles on j specified labels on each shore number (j!)^2/(2j) for j>=2, giving the claimed exponential function, the r=2 exception (A_1=0) and both sizes for r>=3. For a_r=A_r/(r!)^2, the singular expansion gives a_r=e^(-1/2)(pi r)^(-1/2)(1-3/(8r)+O(r^-2)); the next coefficient transfer is valid for the analytic remainder multiplying (1-t)^(3/2). Dividing consecutive terms and using a_{r-1}/(a_r+a_{r-1}) yields 1/2+1/(8r)+O(r^-2) for uniform sampling of labeled sets. An independent six-board replay of graph maximality, two-colorability and the coefficient counts matched both boundary and nontrivial cases, including B_3,4=114z^6 and B_4,4=96z^7+90z^8.

## originality

FAIL

The complete labeled rectangular and square enumerators are already covered as exact claims by distinct Resultary record 5aee7013f56e. Its equivalent path-and-cycle enumeration changes the form, not the coefficients. The first probability correction was not located verbatim there, but follows mechanically from the exact square coefficients and their classical generating function. The index establishes overlap and implication, not historical priority.

## value

FAIL

Maximal-set multiplicities are a natural refinement of the lower bipartite number, but the exact multiplicities here have equivalent coverage. The ostensible residual new item is only the first term of an immediate adjacent-coefficient ratio of the same classical series. The correction is not an independent asymptotic phenomenon or a substantive repair to the covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
