# Tree-resolvent inballs and a shape gap for triangular homology polytopes

## Finding

Let \(\Delta\) be a triangulation of a convex polygon into \(m\ge1\) triangles. Regard each oriented edge of \(\Delta\) as an orthonormal coordinate vector, and let \(b_i\) be the simplicial boundary vector of its \(i\)-th triangle. Write
\[
P_\Delta=\operatorname{conv}\{\pm b_1,\ldots,\pm b_m\}\subset\mathbb R^{2m+1}.
\]
Use the Euclidean metric in the intrinsic span \(E=\operatorname{span}\{b_i\}\), not the planar metric of a drawing of the original triangulation. Let \(T\) be the dual tree of triangles and let \(A_T\) denote its ordinary adjacency matrix. Put
\[
G_T=3I_m-A_T,\qquad S_T=\mathbf 1^\top G_T^{-1}\mathbf1.
\]
Then the exact largest-ball radius is
\[
\boxed{\rho(P_\Delta)=S_T^{-1/2}.}
\]
The origin-centered optimal ball touches precisely **two opposite facets** of \(P_\Delta\). The affine dimension of the complete set of optimal ball centers is exactly \(m-1\), including dimension zero when \(m=1\). Its full set of centers is described explicitly below.

For a path dual tree, let \(\tau=(3-\sqrt5)/2\). For every \(m\ge1\),
\[
\boxed{S_m^{\mathrm{path}}=m-\frac{2\tau(1-\tau^m)}{(1-\tau)(1+\tau^{m+1})}.}
\]
For a complete rooted binary dual tree of height \(h\ge0\), let \(m=2^{h+1}-1\) and \(N=2^{h+1}\). Then
\[
\boxed{S_h^{\mathrm{binary}}=2m-h-1-\frac{(h+2)(h+N^{-1})}{2-N^{-1}}.}
\]
Both dual-tree types are realized by triangulations of convex polygons. For these two triangulations with equal \(m=2^{h+1}-1\),
\[
\boxed{\lim_{h\to\infty}\frac{\rho_{\mathrm{binary}}}{\rho_{\mathrm{path}}}=\frac1{\sqrt2}.}
\]
All these polytopes are combinatorial \(m\)-crosspolytopes; the limiting radius difference is invisible to their face vectors.

## Assumptions and scope

The \(m+2\) polygon vertices are all on the boundary and the triangulation has no interior vertices. The triangle-dual graph has one vertex for each triangle and an edge for each shared diagonal; it is a tree with maximum degree at most three. The ambient edge-chain space has dimension \(2m+1\) with its standard orthonormal basis. Orient all triangles consistently so that shared edges have opposite induced orientations; changing individual triangle signs leaves \(P_\Delta\) unchanged. No additional normalization of the boundary vectors is imposed: each \(b_i\) has squared Euclidean norm \(3\).

## Proof

**Boundary Gram matrix.** Two distinct triangles share either one diagonal edge or no edge. Consistent orientation makes the shared coordinate have opposite coefficients. Thus, for the matrix \(B\) whose columns are the \(b_i\),
\[
B^\top B=3I_m-A_T=G_T.
\]
For every real \(z\in\mathbb R^m\),
\[
z^\top G_Tz=\sum_{ij\in E(T)}(z_i-z_j)^2+\sum_i(3-\deg_T(i))z_i^2.
\]
This is strictly positive unless \(z=0\): equality would force \(z\) constant along the connected tree, while the leaf terms force the constant to vanish. Thus \(G_T\) is positive definite and the columns of \(B\) are linearly independent. The polytope is therefore an \(m\)-crosspolytope.

**Every facet and its norm.** For \(\varepsilon\in\{-1,1\}^m\), define
\[
y_\varepsilon=B G_T^{-1}\varepsilon\in E.
\]
It satisfies \(B^\top y_\varepsilon=\varepsilon\), and \(\langle y_\varepsilon,x\rangle\le1\) defines a facet of \(P_\Delta\). These are all \(2^m\) facets, with
\[
\|y_\varepsilon\|^2=\varepsilon^\top G_T^{-1}\varepsilon.
\]
Since \(T\) is connected and has maximum degree three, \(\lambda_{\max}(A_T)<3\); this follows, for example, from the positive-definite expression above. Consequently
\[
G_T^{-1}=\frac13\sum_{k=0}^\infty(A_T/3)^k
\]
has **strictly positive entries**: every pair of vertices is joined by a walk. Therefore
\[
\varepsilon^\top G_T^{-1}\varepsilon\le\mathbf1^\top G_T^{-1}\mathbf1=S_T,
\]
with equality **only** for \(\varepsilon=\mathbf1\) or \(\varepsilon=-\mathbf1\). Indeed, a nonconstant sign vector makes at least one positive off-diagonal contribution strictly smaller. The distance from the origin to facet \(\varepsilon\) is \(1/\|y_\varepsilon\|\). Since \(P_\Delta\) is centrally symmetric, a largest inscribed ball can always be centered at zero: reflect any inscribed ball and average the two ball inclusions. This proves \(\rho=S_T^{-1/2}\) and classifies exactly the two facets tangent at the origin-centered optimum.

**All centers.** Put \(\rho=S_T^{-1/2}\) and \(q=BG_T^{-1}\mathbf1\). A ball of radius \(\rho\) centered at \(c\in E\) lies in \(P_\Delta\) precisely when
\[
\langle y_\varepsilon,c\rangle\le1-\rho\|y_\varepsilon\|\quad\text{for all }\varepsilon\in\{-1,1\}^m.
\]
For \(\varepsilon=\pm\mathbf1\), the right side vanishes and the two constraints give \(\langle q,c\rangle=0\). For every other sign vector the right side is *strictly positive*, and all these inequalities hold strictly at \(c=0\). Hence the complete center locus is exactly
\[
\boxed{\left\{c\in E:\ \langle q,c\rangle=0,\quad
\langle y_\varepsilon,c\rangle\le1-\rho\|y_\varepsilon\|\ \text{for every }\varepsilon\notin\{\pm\mathbf1\}\right\},}
\]
a convex body with nonempty relative interior in the \((m-1)\)-dimensional hyperplane \(q^\perp\cap E\).

**Path solution.** Number path vertices \(1,\ldots,m\), and solve \(G_Tu=\mathbf1\) using boundary conditions \(u_0=u_{m+1}=0\). The recurrence is \(3u_i-u_{i-1}-u_{i+1}=1\). Direct substitution gives
\[
u_i=1-\frac{\tau^i+\tau^{m+1-i}}{1+\tau^{m+1}},\qquad \tau=(3-\sqrt5)/2.
\]
Summing \(u_i\) proves the displayed path formula. In particular \(S_m^{\mathrm{path}}=m-(\sqrt5-1)+O(\tau^m)\).

**Complete binary solution.** Root the complete binary tree at depth zero, with two children per nonleaf vertex and leaves at depth \(h\). Symmetry makes \(u=G_T^{-1}\mathbf1\) constant on each depth, say \(u_k\). The equations are
\[
3u_0-2u_1=1,\quad 3u_k-u_{k-1}-2u_{k+1}=1\ (1\le k<h),\quad 3u_h-u_{h-1}=1,
\]
with the obvious one-vertex equation at \(h=0\). For \(h\ge1\) the solution is
\[
u_k=B_0-k+C_0 2^{-k},\quad C_0=-\frac{h+2}{2-1/N},\quad B_0=h+1-C_0/N.
\]
The same expression also satisfies the single-vertex equation at \(h=0\). Since there are \(2^k\) vertices at depth \(k\), summation gives
\[
\sum_{k=0}^h2^ku_k=2m-h-1-\frac{(h+2)(h+1/N)}{2-1/N}.
\]
Now \(S_h^{\mathrm{binary}}=2m-O(h^2)\), whereas \(S_m^{\mathrm{path}}=m-O(1)\). Since \(m=2^{h+1}-1\), the radius ratio tends to \(1/\sqrt2\).

**Realizability.** Any finite tree of maximum degree at most three can be rooted and realized as the dual tree of a polygon triangulation. Start from a triangle for the root and recursively attach a fresh triangle with one new boundary vertex along a currently unused edge of the parent triangle. Each parent has enough available edges because its total degree is at most three. Every attachment is an ear addition, producing a triangulated topological disk with all vertices on its boundary; its boundary cyclic order yields a triangulation of a convex polygon. In particular, path and complete binary trees occur.

## Verification

The standalone file `verify_homology_tree.py` independently constructs boundary matrices by gluing triangles, checks the Gram identity, computes exact rational inverses, and exhaustively evaluates signed facet norms for small path cases. It also checks the explicit path and complete-binary formulas against direct solutions. Executing the embedded file using Python 3 and NumPy returned `PASS 2258 checks`. These finite tests corroborate the formulas; the proof above establishes every integer size.

## Relationship to prior work

Donzelmann, Holleben, and Juhnke introduced symmetric homology polytopes \(\operatorname{conv}[\partial_d|-\partial_d]\) and proved their crosspolytope characterization when top homology vanishes. That establishes the relevant *combinatorial type*, not this intrinsic Euclidean inradius, all-center locus, or binary-versus-path metric comparison. Previously studied symmetric edge polytopes of graph paths have a different Gram normalization (diagonal two rather than the triangle-boundary diagonal three), so their radii do not imply the present formulas. The result uses only elementary finite-dimensional Euclidean geometry after the recent construction and does not assert a new combinatorial classification.

## Limitations

The metric is the intrinsic metric induced by orthonormal edge-chain coordinates; arbitrary linear or unimodular changes of coordinates need not preserve these radii. No optimality of either path or complete binary shape among all triangulations is claimed. Results do not extend automatically to complexes with interior vertices or cyclic triangle-dual graphs. The originality assessment is provisional because obscure equivalent metric classifications may exist; no independent audit has been carried out.

## References

1. T. Donzelmann, T. Holleben, and M. Juhnke, *Symmetric (co)homology polytopes*, arXiv:2602.17253v1 (first public version February 19, 2026), especially Definition (1) and Corollary 5.2. https://arxiv.org/abs/2602.17253
2. A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, Mathematika 65 (2019), 763–784, DOI:10.1112/S0025579319000147 (background on graph symmetric edge polytopes).
