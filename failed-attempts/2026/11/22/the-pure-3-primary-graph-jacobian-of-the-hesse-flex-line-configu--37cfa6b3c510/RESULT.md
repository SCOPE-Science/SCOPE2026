# The pure 3-primary graph Jacobian of the Hesse flex–line configuration

## Finding
Let \(k\) be an algebraically closed field of characteristic zero. For any smooth plane cubic, let \(\mathcal H\) denote its classical Hesse configuration: the nine inflection points and the twelve lines containing triples of these points. Let \(\Gamma\) be its simple bipartite *Levi graph*, with one vertex for every inflection point, one for every such line, and an edge for every point–line incidence. Then
\[
K(\Gamma)\cong \mathbb Z/3\mathbb Z\oplus (\mathbb Z/9\mathbb Z)^4\oplus (\mathbb Z/27\mathbb Z)^3.
\]
The graph has 21 vertices, 36 edges, first Betti number 16, and precisely \(3^{18}=387420489\) spanning trees. Thus its critical group has exponent 27, eight nontrivial cyclic invariant factors, and is entirely 3-primary.

There exists a stable nodal curve \(C_0/k\) consisting of 21 rational components with this dual graph and with 36 ordinary nodes; its arithmetic genus is 16. For a one-parameter **regular, split, semistable smoothing with all node thicknesses one**, the geometric component group of the Néron model of the smooth generic fibre's Jacobian is the displayed group. This construction does not assert that a member of the original cubic pencil degenerates to \(C_0\).

## Assumptions and scope
The incidence is over characteristic zero, so the flex configuration is reduced with nine distinct points. By the classical Hesse geometry, its abstract point–line incidence is the affine plane \(\mathbb F_3^2\): a point is a pair \((x,y)\in\mathbb F_3^2\), and the twelve lines are the level sets \(y-mx=a\) for \(m\in\{0,1,2\}\), \(a\in\mathbb F_3\), together with \(x=a\). Every point lies on four lines, every line contains three points, and every pair of distinct points determines exactly one line. No line-to-line intersections outside these nine flexes are used as vertices. The graph has no loops or parallel edges.

The critical group \(K(\Gamma)\) means the finite abelian cokernel of any reduced integral graph Laplacian, not the Smith cokernel of the rectangular incidence matrix. Rational components in the auxiliary stable curve are abstract components glued at distinct marked points, not the original Hesse projective lines.

## Proof
Index the nine points and twelve lines by the affine coordinates above and form the \(9\times12\) incidence matrix \(B\), with entries zero or one. Counting common lines through points yields the integral identity
\[
BB^{\mathsf T}=3I_9+J_9,
\]
where \(J_9\) is the all-ones matrix: the diagonal entries are four and off-diagonal entries are one. The 21-vertex graph Laplacian is
\[
L=\begin{pmatrix}4I_9&-B\\-B^{\mathsf T}&3I_{12}\end{pmatrix}.
\]
The spectrum of \(BB^{\mathsf T}\) is 12 once and 3 eight times. Since \(B\) has rational rank nine, \(\ker(B)\) has dimension three. Applying the Schur complement to \(tI-L\), or diagonalizing the singular-value blocks, gives
\[
\det(tI_{21}-L)=t(t-7)(t-3)^3(t^2-7t+9)^8.
\]
Thus \(\Gamma\) is connected, and the matrix–tree theorem gives
\[
\tau(\Gamma)=\frac{7\cdot3^3\cdot9^8}{21}=3^{18}.
\]
This proves the claimed order, but does **not** determine the integral invariant factors.

For the integral structure, delete any one row and the same column of \(L\), producing an explicit \(20\times20\) integral matrix \(L_*\). The accompanying dependency-free `verify_hesse.py` constructs \(B\) directly from the twelve affine equations, independently checks the twelve lines against all \(\binom{9}{3}\) point triples, and performs exact 3-adic elementary row and column operations on \(L_*\) in \(\mathbb Z/3^6\mathbb Z\). A pivot of minimum 3-adic valuation is a unit times a power of 3, so multiplying its row by a unit and clearing its column and row are invertible operations over this local principal ideal ring. Inductively, no diagonal valuations remain ambiguous at precision six. At each of six independently selected sink vertices (including point and line vertices), the verified ordered valuations are
\[
(\underbrace{0,\ldots,0}_{12},1,2,2,2,2,3,3,3).
\]
Each of these six integral reduced Laplacians also has determinant \(3^{18}\), independently obtained with fraction-free Bareiss elimination. Since the product of the 3-power diagonal entries already equals the whole determinant, no other prime-primary factors can occur. Hence the full integral Smith diagonal has twelve unit entries, one 3, four 9s, and three 27s, proving the group decomposition. This is an exhaustive exact finite computation for a fixed 20-dimensional matrix, not an extrapolation from numerical experiments.

Finally, choose 21 copies of \(\mathbb P^1_k\) and put three or four distinct labeled smooth points on each according to the graph degree. Pair the marked points for the 36 edges to form 36 ordinary nodes. All components have at least three special points, so the curve is stable; its arithmetic genus is \(36-21+1=16\). Standard unobstructed smoothing of stable nodal curves permits a regular one-parameter smoothing with local equations \(uv=t\) at every node; in the specified unit-thickness split situation the component-group/graph-Jacobian comparison identifies its geometric Néron component group with \(K(\Gamma)\).

## Verification
Run `python3 verify_hesse.py` using Python 3.8+ with no third-party packages. The program checks the abstract geometry, the complete incidence matrix, the Gram identity, row sums and edge count, 3-adic Smith valuations, six independent reduced determinants, order reconciliation, and genus. Expected final line: `SNF 1^12 3^1 9^4 27^3; tree_count=3^18; stable_genus=16`. The source file and its SHA-256 digest are in this package. All code inputs are embedded; no internet or external matrix file is used.

## Relationship to prior work
Artebani–Dolgachev describe the nine flexes, twelve lines and affine-plane labeling of the Hesse configuration. Chandler–Sin–Xiang determine Smith forms for **rectangular point–subspace incidence matrices** across affine and projective spaces; their general results concern \(B\), rather than the mixed-degree reduced graph Laplacian \(L_*\). Indeed \(B\) in this case has Smith diagonal \((1^6,3^3)\), different from \(L_*\). Busonero–Melo–Stoppino establish the general link between complexity groups of dual graphs and stable-curve Jacobians; the geometric interpretation here is an application, not a new general comparison theorem. The asserted new specific result is the integral group of this precise 21-vertex Hesse Levi graph and its application to the indicated genus-16 stable curve, not the affine-plane geometry, general chip-firing theory or the matrix–tree theorem.

## Limitations
This is a self-contained calculation for one natural small incidence graph, not a uniform theorem for all affine planes. The integral decomposition does not follow solely from rational eigenvalues; the finite local Smith computation is a substantive part of the proof. Historical priority remains subject to unindexed computations or general affine-design critical-group results not located during the comparison. The stable-curve construction is auxiliary and does not describe a degeneration of the original genus-one cubic or its elliptic Jacobian. No independent external mathematical audit has been performed.

## References
- D. B. Chandler, P. Sin, Q. Xiang, *The invariant factors of the incidence matrices of points and subspaces in PG(n,q) and AG(n,q)*, arXiv:math/0312506 (first public 2003-12-30), https://arxiv.org/abs/math/0312506.
- M. Artebani, I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (first public 2006-11-19), https://arxiv.org/abs/math/0611590.
- S. Busonero, M. Melo, L. Stoppino, *On the complexity group of stable curves*, arXiv:0808.1529 (first public 2008-08-11), https://arxiv.org/abs/0808.1529.
