# Sharp Euclidean inradius among symmetric homology polytopes of polygon triangulations

## Finding

For every integer \(n\ge2\) and every triangulation \(\Delta\) of a convex \((n+2)\)-gon, let \(B_\Delta\) be its oriented triangle-to-edge boundary matrix, and let \(Q_\Delta=\operatorname{conv}\{\pm B_\Delta e_i:1\le i\le n\}\), with its intrinsic Euclidean metric inherited from the edge-coordinate space. Write \(T_\Delta\) for the dual tree on the triangles, and \(A_T\) for its adjacency matrix. Then

\[
 r(Q_\Delta)=\left[\mathbf 1^{\mathsf T}(3I_n-A_T)^{-1}\mathbf 1\right]^{-1/2}.
\]

The largest inscribed ball centered at the origin is tangent to **exactly two opposite facets**. The set of centers of all largest inscribed Euclidean balls has affine dimension precisely \(n-1\). Every \(Q_\Delta\) has the same smallest-enclosing-ball radius \(\sqrt3\), although its inradius depends on the dual tree.

Among **all** triangulations of the convex \((n+2)\)-gon, the largest possible inradius is obtained **if and only if the dual tree is a path**. Let \(\lambda=(3+\sqrt5)/2\). The sharp value is

\[
 r_{\max}(n)=\left[n-\frac{2\lambda(\lambda^n-1)}{(\lambda-1)(1+\lambda^{n+1})}\right]^{-1/2},
 \qquad
 r_{\max}(n)\sim n^{-1/2}.
\]

An exact six-gon witness distinguishes the two possible dual-tree types with four triangles: a path gives squared reciprocal inradius \(14/5\), while the three-arm star gives \(3\). Thus their inradii are \(\sqrt{5/14}\) and \(1/\sqrt3\), respectively.

## Assumptions and scope

A polygon triangulation is a finite two-dimensional simplicial complex whose geometric realization is a convex polygon, with all its original vertices retained and no interior vertices. There are exactly \(n\) triangles and \(n-1\) interior diagonals; its triangle-adjacency graph \(T_\Delta\) is a tree. Each triangle carries counterclockwise orientation; the edge-coordinate space has its **standard orthonormal basis indexed by every boundary or interior edge**. The matrix \(B_\Delta=\partial_2\) has a column for each triangle, with entries \(0,\pm1\) according to the induced oriented boundary. The polytope is studied in its \(n\)-dimensional linear span, not in the full edge-coordinate space. The Euclidean inradius optimizes over arbitrary centers in that span, not only the origin. Triangles need not be congruent: their geometric side lengths do not enter the canonical coordinate metric.

The statement applies to every integer \(n\ge2\) and every such triangulation, with no restriction to fan triangulations. A dual path is attained, for example, by every fan triangulation; the equality condition is on the dual graph, rather than on a unique triangulation.

## Proof

**1. Gram identification and invertibility.** An oriented triangle has three boundary edges, so the diagonal entries of \(G=B_\Delta^{\mathsf T}B_\Delta\) are \(3\). Two distinct triangles of a polygon triangulation share either one interior edge or none. If they share one, their induced boundary orientations along that edge are opposite. Hence the corresponding Gram entry is \(-1\), and

\[
 G=3I_n-A_{T_\Delta}.
\]

The dual graph is a finite tree of maximum degree \(3\) and has vertices of degree below \(3\). For \(x\in\mathbb R^n\),

\[
 x^{\mathsf T}Gx
 =\sum_{\{i,j\}\in E(T)}(x_i-x_j)^2
 +\sum_i(3-\deg_T(i))x_i^2.
\]

Connectedness and a strictly positive term in the second sum make this positive for every \(x\ne0\). Thus the columns of \(B_\Delta\) are linearly independent. The strict Perron bound \(\rho(A_T)<3\) gives the convergent entrywise nonnegative expansion

\[
 G^{-1}=\frac13\sum_{\ell=0}^{\infty}\left(\frac{A_T}{3}\right)^\ell.
\]

For every pair of vertices of the connected tree, some power of \(A_T\) has a strictly positive corresponding entry. Therefore **all entries** of \(G^{-1}\) are strictly positive.

**2. Every supporting facet and the exact inradius.** Because \(B_\Delta\) is injective, \(Q_\Delta\) is a linear image of the standard \(n\)-crosspolytope. Its \(2^n\) facets are indexed by \(\varepsilon\in\{\pm1\}^n\). The intrinsic outward normal to facet \(\varepsilon\), normalized to support value \(1\), is

\[
 w_\varepsilon=B_\Delta G^{-1}\varepsilon,
 \quad
 w_\varepsilon^{\mathsf T}B_\Delta e_i=\varepsilon_i,
 \quad
 \|w_\varepsilon\|^2=\varepsilon^{\mathsf T}G^{-1}\varepsilon.
\]

The centered inscribed ball consequently has radius \(\left(\max_\varepsilon\|w_\varepsilon\|\right)^{-1}\). Strict positivity of every entry of \(G^{-1}\) implies

\[
 \varepsilon^{\mathsf T}G^{-1}\varepsilon
 \le\mathbf1^{\mathsf T}G^{-1}\mathbf1,
\]

with equality exactly when all entries of \(\varepsilon\) have the same sign. Hence precisely the two antipodal facets indexed by \(\mathbf1\) and \(-\mathbf1\) touch the centered ball. No translated ball can improve on it: its two opposing facet constraints imply \(r\le 1/\|w_{\mathbf1}\|\), regardless of center. Conversely, if \(r=r(Q_\Delta)\), those two constraints force \(w_{\mathbf1}^{\mathsf T}c=0\). All other facet constraints have strict slack at \(c=0\), hence continue to hold for sufficiently small \(c\) in that hyperplane. The complete optimal-center locus therefore has affine dimension exactly \(n-1\).

Each column \(B_\Delta e_i\) has squared norm \(3\). The origin-centered radius-\(\sqrt3\) ball encloses all vertices. Any nonzero center \(c\) gives, for each opposite vertex pair, maximum squared distance \(3+\|c\|^2+2|c^{\mathsf T}B_\Delta e_i|>3\). Thus the minimum enclosing sphere is unique, centered at the origin, with radius \(\sqrt3\).

**3. Sharp global optimization among triangulations.** For any \(n\)-vertex tree \(T\), define the number of unrestricted vertex-to-vertex walks of length \(\ell\) by \(W_\ell(T)=\mathbf1^{\mathsf T}A_T^\ell\mathbf1\). The resolvent expansion yields

\[
 \mathbf1^{\mathsf T}(3I_n-A_T)^{-1}\mathbf1
 =\frac13\sum_{\ell=0}^{\infty}3^{-\ell}W_\ell(T).
\]

Bollobás and Tyomkyn, *Walks and Paths in Trees*, prove that among trees with \(n\) vertices, the path \(P_n\) minimizes the total number of **all** walks of each fixed length (not merely closed walks); see their Section 5 construction of the unrestricted-walk injection. Applying their inequality term by term gives the desired lower bound on the reciprocal squared inradius. It is **strict** unless \(T\) is a path, already at \(\ell=2\):

\[
 W_2(T)=\sum_i\deg_T(i)^2
 =4n-6+\sum_i(\deg_T(i)-1)(\deg_T(i)-2).
\]

Every summand in the final sum is nonnegative for a tree; all vanish exactly when every degree is \(1\) or \(2\), equivalent to \(T\) being a path. Thus the path is the unique maximizing dual-tree type, and fan triangulations supply equality in every dimension.

**4. Closed form and asymptotic.** Let \(x=(3I_n-A_{P_n})^{-1}\mathbf1\) and adjoin boundary values \(x_0=x_{n+1}=0\). Then \(3x_i-x_{i-1}-x_{i+1}=1\) for \(1\le i\le n\). Its unique solution is

\[
 x_i=1-\frac{\lambda^i+\lambda^{n+1-i}}{1+\lambda^{n+1}},
 \qquad \lambda=\frac{3+\sqrt5}{2}.
\]

Summing gives

\[
 F_n:=\mathbf1^{\mathsf T}(3I_n-A_{P_n})^{-1}\mathbf1
 =n-\frac{2\lambda(\lambda^n-1)}{(\lambda-1)(1+\lambda^{n+1})}.
\]

Because \(\lambda>1\), this equals \(n-(\sqrt5-1)+O(\lambda^{-n})\), proving the claimed asymptotic. For the six-gon example, choosing fan triangles \((0,1,2),(0,2,3),(0,3,4),(0,4,5)\) gives dual path; choosing \((0,2,4),(0,1,2),(2,3,4),(0,4,5)\) gives the three-arm star. Direct inversion yields the two displayed rational values.

## Verification

The standalone `verify.py` independently enumerates **all 196 labeled triangulations** of convex polygons with \(1\) through \(6\) triangles using the Catalan recurrence. For each, it constructs the actual oriented boundary matrix, recomputes \(B^{\mathsf T}B\), checks invertibility and the sharp path inequality, and tests the exact supporting-normal comparison for **10,064 sign facets**. Among those triangulations, **84** have nonpath dual trees and are checked for strictness. It separately checks the radical Green-sum expression for \(1\le n\le11\) and both exact four-triangle examples. Computation is finite corroboration; the unrestricted theorem is proved above using the full tree-walk inequality.

Run in Python with SymPy installed: `python verify.py`. No data files or external network are needed.

## Relationship to prior work

Donzelmann, Holleben and Juhnke introduced symmetric homology polytopes of boundary matrices and investigated their faces, lattice properties, and combinatorial crosspolytope cases. The present work specializes their **canonical Euclidean realization** to disk triangulations, obtains the exact Gram-matrix inradius, and optimizes it across all triangulations. General combinatorial or unimodular equivalence does **not** preserve intrinsic Euclidean radii.

The unrestricted-walk extremal inequality on trees is **not new**: it is explicitly taken from the work of Bollobás and Tyomkyn. The new assessed geometric conclusion requires identifying the boundary-matrix Gram inverse as a weighted walk generating function, proving that it controls the true translated-ball inradius and exact contact sets, and transferring the extremal inequality with a strict equality classification. Known path symmetric-edge-polytope radius formulas concern a different Gram matrix, with diagonal \(2\) rather than \(3\), and do not imply the formula here by an isometry or common scaling.

## Limitations

The Euclidean norm is the canonical **edge-coordinate** norm; replacing it by a metric using geometric edge lengths, or studying polygons with interior vertices, changes the problem. The theorem gives the **maximum**, not a sharp minimum, over triangulations. The inradius depends on the dual-tree structure, not on the precise placement of polygon vertices. Earlier equivalent results under alternative names or in nonindexed sources cannot be ruled out; priority has not been independently certified. No independent mathematical audit has been performed.

## References

1. Torben Donzelmann, Thiago Holleben, Martina Juhnke, *Symmetric (co)homology polytopes*, arXiv:2602.17253v1 (first public release 2026-02-19), https://arxiv.org/html/2602.17253 . In particular, definition of the homology polytope and the crosspolytope and facet results in Sections 3 and 5.
2. Béla Bollobás, Mykhaylo Tyomkyn, *Walks and paths in trees*, arXiv:1002.2768v1 (2010-02-14), https://arxiv.org/abs/1002.2768 . Section 5 establishes the unrestricted-walk comparison used in Step 3.
