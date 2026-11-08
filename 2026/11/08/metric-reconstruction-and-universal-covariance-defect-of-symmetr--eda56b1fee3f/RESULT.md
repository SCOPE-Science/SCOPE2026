# Metric reconstruction and universal covariance defect of symmetric homology polytopes

## Finding
Let \(\Delta\) be a finite, connected, closed, orientable simplicial \(d\)-pseudomanifold, \(d\geq 1\), with \(F\) top-dimensional facets. Set \(k=d+1\), let \(B=\partial_d\) be its ridge-by-facet signed boundary matrix, and equip the ridge-coordinate space with its standard Euclidean metric. Its **symmetric homology polytope** is
\[
P_\Delta=\operatorname{conv}\{\pm B_{\cdot j}:1\leq j\leq F\}.
\]
Let \(G_\Delta\) denote the facet–ridge dual graph. Then:

**Exact metric reconstruction.** Two such polytopes, considered with their intrinsic Euclidean metrics, are congruent if and only if their dual graphs are isomorphic. Their vertices are precisely the \(2F\) signed boundary columns, and the dual graph can be reconstructed without choosing signs: each antipodal pair is one graph vertex, and distinct antipodal pairs \(\{\pm b_i\}\), \(\{\pm b_j\}\) are adjacent exactly when
\[
\min_{\epsilon\in\{-1,1\}}\|b_i-\epsilon b_j\|_2^2=2k-2;
\]
otherwise that minimum is \(2k\). The antipodal distance \(2\sqrt{k}\) recovers \(k\), while the number of antipodal pairs recovers \(F\).

**Universal covariance defect.** If \(S=\operatorname{span} P_\Delta\), \(\Pi_S\) is the orthogonal projection onto \(S\), and \(\Sigma\) is the covariance matrix of the uniform distribution on the \(2F\) vertices, then \(\dim S=F-1\) and
\[
\Sigma=\frac1F BB^{\mathsf T},\qquad
\left\|\Sigma-\frac{k}{F-1}\Pi_S\right\|_{\mathrm F}^{2}
=\frac{k(F-k-1)}{F(F-1)}.
\]
The dimensionless normalized mean-square spectral defect is exactly
\[
\frac{\|\Sigma-\frac{k}{F-1}\Pi_S\|_{\mathrm F}^{2}}
{(F-1)(\frac{k}{F-1})^2}
=\frac{F-k-1}{Fk}.
\]
This defect depends **only** on \(d\) and \(F\), not on the isomorphism type or the topology of \(\Delta\). The vertices form a tight frame in their intrinsic Euclidean span precisely when \(F=d+2\), equivalently when \(\Delta\) is the boundary of a \((d+1)\)-simplex.

## Assumptions and scope
“Closed pseudomanifold” here means a pure finite simplicial complex in which every ridge belongs to exactly two facets and whose facet–ridge graph is connected. “Orientable” means the facets admit coherent integral orientations; this includes triangulated orientable closed manifolds but does not require manifold links. The dimension \(d\) is at least one, and the complexes have no repeated facets. Since simplicial facets share at most one ridge, \(G_\Delta\) is a simple \(k\)-regular connected graph. Changing reference orientations changes column signs, and changing ridge orientations changes row signs, neither of which changes \(P_\Delta\) up to an ambient orthogonal map.

Intrinsic congruence means an affine Euclidean isometry between the affine spans; those spans both contain the origin and the isometry is necessarily linear. If ambient ridge-coordinate dimensions differ, “congruent” does not assert an orthogonal automorphism of a single preset ambient coordinate space. The covariance uses uniform weights on **distinct vertices**, not normalized volume measure on the polytope. The Frobenius norm is the ambient one, equal to the intrinsic norm because the operator vanishes on the orthogonal complement of \(S\).

## Proof
**1. The boundary Gram matrix.** Coherently orient all facets. Every ridge is in exactly two facets, and its signed boundary row has one \(+1\) and one \(-1\). Consequently each column has \(k=d+1\) nonzero entries, two different columns share precisely one ridge coordinate if their facets meet in a ridge, and none otherwise. Thus
\[
B^{\mathsf T}B=kI_F-A(G_\Delta)=L(G_\Delta),
\]
where \(A\) is the adjacency matrix and \(L\) the graph Laplacian. A connected graph has one-dimensional Laplacian kernel, hence \(\operatorname{rank} B=F-1\) and \(\sum_j b_j=0\).

**2. Vertices and distance reconstruction.** All \(b_j\) and their negatives have squared norm \(k\). The signed columns are pairwise distinct: for different facets, their scalar product is either \(-1\) or \(0\), whereas equal or opposite vectors would have scalar product of absolute value \(k\ge2\). A finite set of distinct points on a common Euclidean sphere is in strictly convex position: for each point \(v\), the functional \(x\mapsto v\cdot x\) has its unique maximum at \(v\). Therefore these \(2F\) points are exactly the vertices.

The polytope is centrally symmetric around zero and full-dimensional in \(S\). A bounded centrally symmetric convex body has a unique center of symmetry; any congruence must send the origin to the origin, send vertices to vertices, and preserve antipodal pairs. For distinct facet labels \(i,j\), the Gram identity gives \(|b_i\cdot b_j|=1\) if adjacent and \(0\) if not. Hence
\[
\min_{\epsilon=\pm1}\|b_i-\epsilon b_j\|^2
=2k-2|b_i\cdot b_j|,
\]
which reconstructs precisely the adjacency relation on antipodal vertex pairs. Thus congruence forces graph isomorphism.

Conversely, an isomorphism of the dual graphs allows the columns to be relabeled, and coherent facet orientations chosen, so their Gram matrices agree: both are the same graph Laplacian. The linear map sending each column of \(B\) to its corresponding column of \(B'\) is well-defined and inner-product-preserving because equality of Gram matrices gives identical linear relations and norms of all linear combinations. It extends to a linear isometry \(S\to S'\), taking \(P_\Delta\) to \(P_{\Delta'}\). This proves the converse without assuming any combinatorial equivalence of the complexes themselves.

**3. Covariance and isotropy defect.** The uniform antipodal vertex set has mean zero and covariance \(\Sigma=BB^{\mathsf T}/F\). Its nonzero eigenvalues are \(\lambda_i(L(G_\Delta))/F\), for \(1\le i\le F-1\). Since \(G_\Delta\) is simple and \(k\)-regular,
\[
\operatorname{tr}(L)=Fk,\qquad
\operatorname{tr}(L^2)=Fk(k+1).
\]
The latter holds by expanding \(L=kI-A\), using \(\operatorname{tr} A=0\) and \(\operatorname{tr} A^2=Fk\). Hence \(\operatorname{tr}\Sigma=k\), \(\operatorname{tr}\Sigma^2=k(k+1)/F\). The mean eigenvalue on \(S\) is \(m=k/(F-1)\). Therefore
\[
\|\Sigma-m\Pi_S\|_{\mathrm F}^2
=\operatorname{tr}\Sigma^2-\frac{(\operatorname{tr}\Sigma)^2}{F-1}
=\frac{k(F-k-1)}{F(F-1)},
\]
and division by \((F-1)m^2\) yields the stated dimensionless expression.

By nonnegativity of squared Frobenius norm, tightness occurs exactly at \(F=k+1=d+2\). For completeness, that condition forces \(G_\Delta\) to be the complete graph on \(d+2\) facets. Fix a facet \(\tau\). Its \(d+1\) neighboring facets each replace exactly one vertex of \(\tau\) by a new vertex; any two of these neighboring facets share a ridge only if the replacement vertex is the same. Since all neighbors are pairwise adjacent, all replacements are the same vertex outside \(\tau\). Thus \(\Delta\) consists of the \(d+2\) facets of the boundary of a \((d+1)\)-simplex. The converse is immediate.

## Verification
The standalone `verify.py` uses only Python's standard library and exact integers/rational numbers. Running `python verify.py` reconstructs ridge boundary matrices from explicit facets, solves the coherent-orientation sign constraints, verifies the Gram identity and every antipodal class distance, and checks the trace and normalized defect identities with `fractions.Fraction`. It passed on 19 oriented simplicial complexes: simplex boundaries in dimensions one through five, cross-polytope boundaries in dimensions one through four, eight stacked two-spheres, and two published 14-facet two-spheres.

For the latter two spheres, the dual graphs have respectively zero and one triangles but share \(d=2\), \(F=14\), squared defect \(15/91\), and normalized defect \(5/21\). They are thus noncongruent although the single scalar defect agrees. The pairwise-distance reconstruction detects the distinction. The finite tests corroborate the unrestricted argument; they do not replace its proof.

## Relationship to prior work
Donzelmann, Holleben, and Juhnke introduce symmetric homology polytopes and prove, among other results, that the polytopes of closed connected orientable pseudomanifolds are unimodularly equivalent to symmetric edge polytopes of cycles. That lattice equivalence is **not an isometry** and does not provide their Euclidean congruence classification or intrinsic vertex covariance. Their Example 8.7 gives the two explicit 14-facet spheres used here, originally to distinguish **cohomology** polytopes by a lattice invariant; the graph distinction is earlier evidence, not a new observation.

Cuchilla, Hound, Plepel, Vindas-Meléndez, and Ye prove a closely related metric reconstruction for symmetric **edge** polytopes of graphs. Those are convex hulls of signed edge-incidence **columns**. The present homology polytopes are signed columns of the top boundary, which for an orientable pseudomanifold form the **transpose** of the incidence matrix of its facet–ridge graph. Transposition does not preserve the relevant Gram matrices or Euclidean polytopes, so the published edge-polytope theorem is not a direct statement of this result. The argument here explicitly adapts metric reconstruction to the transpose-incidence configuration and adds the universal covariance-defect identity. The separate matroidal equivalence theorem of D'Alì, Juhnke-Kubitzke, and Koch concerns unimodular, rather than orthogonal, equivalence.

## Limitations
No uniqueness of discovery or independent priority certification is asserted. Equivalent transverse-incidence, graph-star, or frame-theoretic formulations may exist under different names. The statement concerns the canonical ridge-coordinate Euclidean realization, not a generic lattice realization or the Euclidean symmetric cohomology polytope. It does not determine the complete Laplacian eigenvalue multiset, inradius, volume, or optimal ellipsoids; a fixed defect value does not imply congruence. The published unitary-equivalence theorem for ordinary symmetric edge polytopes is an important adjacent result that limits how much of the distance-reconstruction argument can be regarded as conceptually new.

## References
1. Torben Donzelmann, Thiago Holleben, Martina Juhnke, *Symmetric (co)homology polytopes*, arXiv:2602.17253v1 (first posted 2026-02-19), especially Sections 3 and 8 and Example 8.7. https://arxiv.org/html/2602.17253v1
2. Tito Augusto Cuchilla, Joseph Hound, Cole Plepel, Andrés R. Vindas-Meléndez, Louis Ye, *Unitary Actions and Equivariant Volumes of Symmetric Edge Polytopes*, arXiv:2507.18846v2, Theorem 3.8. https://arxiv.org/html/2507.18846v2
3. Alessio D'Alì, Martina Juhnke-Kubitzke, Melissa Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933. https://arxiv.org/abs/2307.04933
