# Mixed-dimensional sphere wedges for ordinary four-cut complexes of three-row rook graphs

## Finding

For every integer \(n\ge4\), let \(G_n=K_3\square K_n\) be the rook graph on \(V=[3]\times[n]\), with adjacency when exactly one coordinate agrees. The ordinary four-cut complex \(\Delta_4(G_n)\) has facets the complements of disconnected induced four-vertex sets. Let \(X_n=\Delta_4(G_n)^\vee\) be its combinatorial Alexander dual on the full \(3n\)-element ground set. Then
\[
X_n\simeq\bigvee^{n(n-1)(n-2)} S^2\ \vee\ \bigvee^{(n-1)(n-2)^2/2} S^3.
\]
The complete reduced integral homology of the original four-cut complex is
\[
\widetilde H_i(\Delta_4(G_n);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{(n-1)(n-2)^2/2},&i=3n-6,\\
\mathbb Z^{n(n-1)(n-2)},&i=3n-5,\\
0,&\text{otherwise}.
\end{cases}
\]
The original complex is pure of dimension \(3n-5\) and is not shellable. The wedge describes the dual, not the original cut complex. The known \(n=3\) case is not claimed as new.

## Proof

**1. Rectangular core.** By the dual definition, \(A\subseteq V\) is a face of \(X_n\) if and only if every four-element subset of \(A\) induces a connected graph. Identify a selected cell with its edge in the bipartite graph on row and column labels. A set of these cells is connected in the rook graph exactly when its row–column edges have only one edge-bearing component.

A set of at least four cells meeting at least two rows and at least four columns contains four cells in different columns meeting at least two rows: choose two cells in distinct rows and columns and complete to four distinct columns. These four edges cannot connect the at least six vertices they meet. Likewise, if the set meets three rows and at least three columns, choose two cells in distinct rows and columns, then a third cell in the remaining row, then (if necessary) a fourth in a third column. If the first three already meet three columns, any fourth cell does. Again four edges cannot connect the at least six vertices they meet. The initial distinct-row, distinct-column pair exists in each case: otherwise, upon choosing two cells in different rows, they would have to share a column, and any cell in another column would differ in row from at least one of them. It follows that a face with four or more cells is contained in a single row, a two-row/three-column rectangle, or a three-row/two-column rectangle.

Conversely, any four cells in a single row are adjacent to one another. In a two-row/three-column rectangle, distinct components of a disconnected induced graph would have disjoint rows and columns. There would have to be two components on separate single rows, so the four selected cells would use four distinct columns, impossible. The transpose argument handles the three-row/two-column rectangle. Let \(Y_n\) be the union of the simplices on the indicated rows and rectangles. Precisely the \(6\binom n3=n(n-1)(n-2)\) triples with three distinct rows and three distinct columns are in \(X_n\) but not in \(Y_n\); all smaller faces belong to \(Y_n\). These additional triangles are maximal and have their boundaries in \(Y_n\).

**2. Product-of-simplices model for the core.** For a nonempty face \(F\) of \(Y_n\), let \(R(F)\) and \(C(F)\) be its row and column projections. The map \(F\mapsto R(F)\times C(F)\) takes values in the nonempty face poset of \(Y_n\), is order-preserving, and is an idempotent satisfying \(F\subseteq R(F)\times C(F)\). Its image poset of full admissible rectangles has homotopy-equivalent order complex: the composition of the retraction with inclusion is homotopic to the identity, since pointwise comparable poset maps induce homotopic maps on order complexes (triangulate the prism over each chain). The image order, given by independent inclusions of the two projections, is the face order of the product cells \(\Delta(R)\times\Delta(C)\) with the allowed row/column sizes. Consequently the barycentric subdivisions identify \(|Y_n|\) up to homotopy with the following polyhedral subcomplex \(P\) of the product \(\Delta^2\times Q\), where \(Q=\Delta^{n-1}\) is the column simplex:
\[
P=(\Delta^2\times Q^{(1)})\ \cup\ ((\Delta^2)^{(1)}\times Q^{(2)})\ \cup\ ((\Delta^2)^{(0)}\times Q).
\]
Here superscripts in parentheses denote skeleta. Indeed, a row vertex allows all columns, a row edge allows at most three columns, and the row triangle allows at most two columns.

**3. The core is a wedge of three-spheres.** Take a spanning two-edge tree \(T\) of \((\Delta^2)^{(1)}\). Form the subcomplex
\[
W=(\Delta^2\times Q^{(1)})\ \cup\ (T\times Q^{(2)})\ \cup\ ((\Delta^2)^{(0)}\times Q).
\]
Collapse the row triangle along the third edge onto \(T\), fixing \(T\). Taking the product with \(Q^{(1)}\) and leaving the other pieces fixed deforms \(W\) onto \((T\times Q^{(2)})\cup ((\Delta^2)^{(0)}\times Q)\). Collapse each disjoint simplex \(\{r\}\times Q\) to its own point. Each quotient is a homotopy equivalence, since the collapsed subcomplex is contractible and its inclusion is a cofibration. The resulting space consists of two unreduced suspensions of \(Q^{(2)}\), one for each tree edge, joined at their common endpoint. Now \(Q^{(2)}\simeq\bigvee^{\binom{n-1}{3}}S^2\): the cone from a fixed column vertex over the complete graph on the other vertices is a contractible subcomplex, and every remaining triangle has its boundary in that subcomplex. Quotienting by the cone leaves one two-sphere per remaining triangle. Because \(Q^{(2)}\) is connected, its unreduced suspension is homotopy equivalent to the reduced suspension (collapse the basepoint interval), and hence \(W\simeq\bigvee^{2\binom{n-1}{3}}S^3\).

The cells of \(P\) not in \(W\) are precisely the products of the remaining row edge with a column triangle. All their boundaries lie in \(W\): the end vertices of the row edge support the full column simplex, and the boundary of a column triangle lies in \(Q^{(1)}\). Each product cell is a three-ball with attaching sphere \(S^2\); its attaching map is nullhomotopic since \(W\) is 2-connected. Attach the \(\binom n3\) cells to obtain
\[
Y_n\simeq P\simeq\bigvee^{2\binom{n-1}{3}+\binom n3}S^3
=\bigvee^{(n-1)(n-2)^2/2} S^3.
\]

**4. Additional triangles and duality.** Each additional triangle attaches along a loop in the simply connected core, so it adds a wedge summand \(S^2\). This establishes the asserted homotopy type of \(X_n\), including integral torsion-freeness. Combinatorial Alexander duality on \(N=3n\) vertices gives \(\widetilde H_i(\Delta_4(G_n);\mathbb Z)\cong\widetilde H^{N-i-3}(X_n;\mathbb Z)\); the wedge gives exactly the required groups. Disconnected quadruples exist, for example three distinct columns in one row and an isolated cell in a different row and fourth column. Each cut facet has exactly \(N-4\) vertices. Nonzero reduced homology in degree \(N-6\) over every field contradicts homology concentration for a pure shellable complex (and the Cohen–Macaulay condition over each field).

## Reproducibility and scope

The proof requires no computation. Optional corroboration is provided by `evidence/verify.py`, which checks the four-subset predicate and the core/transversal decomposition on finite boards and tests homology and a finite Morse model. These checks neither substitute for the proof nor assert any particular critical-set formula for all lengths. The result is neither a homotopy classification of the original cut complex nor an equivariant statement.

## Relationship to prior work

The ordinary cut-complex literature distinguishes clique prisms \(K_2\square K_n\) from path grids \(P_m\square P_n\). Earlier rook-board results at cut threshold three, or specific four-cut results on the \(3\times3\) and \(4\times4\) boards, do not give the classification for all three-row boards with \(n\ge4\). The rectangular core and extra transversals explain the two distinct dimensions of integral homology. Priority beyond inspected sources is not asserted.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, https://arxiv.org/abs/2304.13675, especially Sections 1 and 7.3.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, https://arxiv.org/abs/2407.08158, especially the grid section.
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, Resultary `bd50464fc17f`.
4. *Integral four-cut homology separates the Shrikhande and rook graphs*, Resultary `de2f98e55b1f`.
5. *A mixed sphere wedge in the four-cut Alexander dual of the 3-by-3 rook graph*, Resultary `dc4e90566a37`.
