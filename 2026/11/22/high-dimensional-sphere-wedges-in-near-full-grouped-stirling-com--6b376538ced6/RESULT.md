# High-dimensional sphere wedges in near-full grouped Stirling complexes of stars

## Finding
For every integer \(m\ge3\) and \(r\ge4\), let \(T_m=K_{1,m}\) have one central vertex and \(m\) leaves. Put \(r\) distinguishable color groups, each with \(m\) indistinguishable robots, on \(T_m\), with the grouped Stirling noncollision and vertex-covering rules. Then
\[
\mathcal S_{(m,\ldots,m)}(T_m)\simeq
\bigvee^{(m-1)^r-m} S^{r-1}.
\]
Thus the complex is \((r-2)\)-connected, its reduced integral homology is concentrated in degree \(r-1\), and the free rank there is \((m-1)^r-m\). For four groups, the ranks for three, four and five arms are \(13,77,251\), respectively. This is a homotopy classification, not a field-homology conjecture.

## Assumptions and scope
The graph \(T_m\) has \(m+1\) vertices and \(m\) simple edges; no metric edge lengths are used. The grouped complex uses the original finite closed cubical cell model with color vector \((m,\ldots,m)\), \(r\) entries. A cell for one color is either a missing vertex \(v\), with robots at all other vertices, or an edge \(e=\{u,w\}\), with one robot in the open edge and one at every vertex other than \(u,w\). Consequently, choosing one such option \(\sigma_i\) per color gives a cell precisely when \(\bigcap_{i=1}^r\sigma_i=\varnothing\), interpreting vertices and edges as their closed supports. All homotopy equivalences are ordinary nonequivariant homotopy equivalences and use integral coefficients.

## Proof
**1. Cubical identification.** The preceding robot-location correspondence identifies the grouped Stirling complex with the product cubical subcomplex
\[
K_r(G)=\bigcup_{\substack{\sigma_i\in V(G)\cup E(G)\\
\bigcap_i\sigma_i=\varnothing}}\sigma_1\times\cdots\times\sigma_r\subseteq |G|^r.
\]
Every excluded product cube \(Q\) meets the thin diagonal \(\Delta=\{(x,\ldots,x)\}\) either in a single corner or, when all factors are the same edge, in its internal main diagonal; excluded zero-cubes lie entirely on \(\Delta\). If \(Q\cap\Delta\) is a corner, radial projection away from that corner strongly retracts \(Q\setminus\Delta\) onto \(\partial Q\setminus\Delta\). If it is a main diagonal, use radial projection from the center of the cube: every ray from the center through a nondiagonal point remains nondiagonal, and the boundary is fixed. Apply these retractions in descending cubical dimension. The maps agree on shared boundaries, giving a strong deformation retraction \(|G|^r\setminus\Delta\to K_r(G)\). In particular this holds for the star.

**2. Cone and join.** Regard \(|T_m|\) as the cone on a discrete \(m\)-point space \(A_m\). Radial normalization of the product of cones identifies the complement of its cone point, up to a contractible radial factor, with the simplicial join \(L=A_m^{*r}\). The thin diagonal consists of the central cone point and \(m\) radial rays, one for each arm, so its intersection with the radial link is one interior point of each *diagonal facet* \(F_j=\{(1,j),\ldots,(r,j)\}\) of \(L\). Removing these points and radially retracting within their facets gives the subcomplex
\[
L'=A_m^{*r}\setminus\{\text{interiors of }F_1,\ldots,F_m\}.
\]
Therefore the grouped complex is homotopy equivalent to \(L'\).

**3. Top homology.** The join \(L\) is \((r-2)\)-connected and has \(\widetilde H_{r-1}(L;\mathbb Z)=\mathbb Z^{(m-1)^r}\); all other reduced homology vanishes. Since \((L,L')\) has precisely \(m\) relative cells of dimension \(r-1\), its relative homology is \(\mathbb Z^m\) in that dimension only. The map \(\widetilde H_{r-1}(L)\to H_{r-1}(L,L')\) is surjective: for each \(j\), choose alternative labels \(k_1,\ldots,k_r\ne j\) with \(k_1\ne k_2\) (possible as \(m\ge3\)). The cross-polytope boundary
\[
\bigstar_{i=1}^r\bigl([(i,j)]-[(i,k_i)]\bigr)
\]
is an integral \((r-1)\)-cycle in \(L\). Among the deleted diagonal facets, its sole nonzero coefficient is \(\pm1\) on \(F_j\). The relative map is thus onto each standard basis vector. The long exact sequence of \((L,L')\) yields \(\widetilde H_{r-1}(L';\mathbb Z)\cong\mathbb Z^{(m-1)^r-m}\), with all lower reduced integral homology zero.

**4. Homotopy, not merely homology.** For \(r\ge4\), the deleted facets have dimension at least three, so \(L'\) and \(L\) have the same two-skeleton. The join \(L\) is simply connected; hence \(L'\) is simply connected. Inductively applying the Hurewicz theorem, the vanishing of lower integral homology makes \(L'\) \((r-2)\)-connected. Since \(L'\) has dimension \(r-1\), a basis of its free top homology is represented by maps of \((r-1)\)-spheres. Their wedge induces homology isomorphisms and, by the simply connected Whitehead theorem, is a homotopy equivalence. This completes the classification.

## Verification
The standalone `verify_grouped.py` enumerates exactly the allowed cubical cells, checks the integral chain identity \(\partial^2=0\), computes exact mod-two boundary ranks, and separately enumerates the *join-with-diagonal-facets-deleted* simplicial model. For every arm count from three through seven and two through four colors it found the predicted ranks in 15 matched cubical and join cases; specifically all five tested four-color cases agree with the theorem. Finite checks corroborate the proof but do not establish its infinite quantifiers or integral homotopy type by themselves. Run with `python3 verify_grouped.py` using Python's standard library.

## Relationship to prior work
Revelli and Scheirer introduced grouped Stirling complexes and determined the cell counts for the relevant near-full color vectors, explicitly leaving higher-dimensional homotopy and star-graph calculations open (arXiv:2602.09884, Section 4). Alvarado-Garduño and González proved general stabilization of discretized no-\(k\)-equal graph configurations (arXiv:2407.07854, Theorem 1.2); that supplies conceptual background for the diagonal-complement model but not this complete star-family wedge rank and integral homotopy type. Chettih's 2016 dissertation considered no-three-equal configurations of a three-armed star, outside the present restriction to \(r\ge4\) color groups. The contribution here is the uniform high-dimensional sphere-wedge theorem, proved by an explicit deleted-diagonal-facet join argument rather than merely recasting those general models.

## Limitations
The homotopy classification is for unsplit stars with at least three arms and at least four near-full color groups. It does not assert a matching formula for general trees, graphs with cycles, fewer color groups, or equivariant homotopy. The source literature uses related models and conventions; the cell correspondence above is essential to the claim. An independent mathematical audit has not yet been performed.

## References
1. A. Revelli and S. Scheirer, *Grouped Stirling complexes*, arXiv:2602.09884 (first posted 2026-02-10), https://arxiv.org/abs/2602.09884.
2. O. Alvarado-Garduño and J. González, *Abrams' stabilization theorem for no-k-equal configuration spaces on graphs*, arXiv:2407.07854 (first posted 2024-07-10), https://arxiv.org/abs/2407.07854.
3. S. Chettih, *Dancing in the Stars: Topology of Non-k-Equal Configuration Spaces of Graphs*, University of Oregon dissertation (2016), https://scholarsbank.uoregon.edu/server/api/core/bitstreams/3028c141-3515-4fd2-98fa-18de56a8271c/content.
