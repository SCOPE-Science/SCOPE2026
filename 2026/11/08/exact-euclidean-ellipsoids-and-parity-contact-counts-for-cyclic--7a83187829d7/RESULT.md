# Exact John ellipsoids and inward-contact transitions for cyclic edge-diamond sums

## Finding

For each integer \(n\ge3\), let \(C_n\) be the cycle on \([n]\), with indices modulo \(n\), and let
\[
D_{ij}=\operatorname{conv}\{\pm e_i,\pm e_j\},\qquad
K_n=\sum_{\{i,j\}\in E(C_n)}D_{ij}\subset\mathbb R^n.
\]
The **unique John ellipsoid** (maximum-volume inscribed ellipsoid) of \(K_n\) is the origin-centered Euclidean ball \(r_nB_2^n\), where
\[
\boxed{r_n^2=\min\{n,4\}.}
\]
Exactly \(T_n\) supporting facets touch this ball, where
\[
\boxed{T_n=\begin{cases}2^n,&n=3,\\2^n+2n,&n=4,\\2n,&n\ge5.\end{cases}}
\]
For \(n=3\), their outward unit normals are the \(2^n\) sign vectors \((\pm1,\ldots,\pm1)/\sqrt n\). For \(n=4\), the preceding sign vectors and the \(2n\) signed coordinate vectors both occur. For \(n\ge5\), precisely the signed coordinate vectors occur. All these contacts are with geometrically distinct genuine facets. This is the complete classification, not only the radius.

The squared radius and the farthest-vertex multiplicity of the **Löwner** (minimum-volume containing) ball, and the associated diameter, were already established in *The complete Euclidean vertex-shell spectrum of cyclic cross-polytope sums* (published mathematical record, 8 November 2026, \(n\ge5\)). They are **not claimed as new here**. The general subset formula for the inradius of a sum of coordinate cross-polytopes follows from the inequality description of Wang–Hou–Thawinrak–Liu–Dai (2026) and is likewise credited. The new claim is the complete cyclic **inward** metric and facet-contact classification above.

## Domain and normalization

The cycle is simple and unweighted, \(n\ge3\), with every diamond in the canonical ambient Euclidean coordinates. The body is full-dimensional and centrally symmetric. Radii are standard-Euclidean, not invariant under arbitrary affine or lattice transformations. A touching facet is a distinct supporting facet whose hyperplane intersects the boundary of the centered John ball; opposite facets count separately. No claim about arbitrary weighted graphs, outer-shell novelty, or all incenter points is made.

## Proof

**Support minimization.** For any unit normal \(u\), Minkowski support additivity gives
\[
h_{K_n}(u)=\sum_{\{i,j\}\in E(C_n)}\max\{|u_i|,|u_j|\}.
\]
More generally, for a family of nonempty coordinate hyperedges \(I_\alpha\) and positive weights \(w_\alpha\), set \(W(S)=\sum_{\alpha:I_\alpha\cap S\ne\varnothing}w_\alpha\). Write the nonnegative vector \(a=(|u_i|)_i\) as a positive linear combination \(a=\sum_{j}\delta_j\mathbf1_{S_j}\) of its nested nonempty superlevel sets. The identity \(\max_{i\in I_\alpha}a_i=\sum_{j}\delta_j\mathbf1_{I_\alpha\cap S_j\ne\varnothing}\) implies
\[
h_K(u)=\sum_j\delta_jW(S_j)
\ge r_*\sum_j\delta_j\sqrt{|S_j|}
\ge r_*\|a\|_2,
\qquad r_*:=\min_{\varnothing\ne S\subset[n]}\frac{W(S)}{\sqrt{|S|}}.
\]
The last inequality is the Euclidean triangle inequality. Every minimizing indicator \(u=\mathbf1_S/\sqrt{|S|}\), with arbitrary signs, gives equality. Because equality in the Euclidean triangle inequality forces the nonzero vectors \(\mathbf1_{S_j}\) to be positive multiples of one another, and different nested indicator supports are not parallel, equality occurs only when \(a\) has one strictly positive magnitude. Thus all support-minimizing unit normals have equal magnitude on one minimizing subset \(S\) and vanish elsewhere, with independent signs. This calculation is reproduced for clarity; the underlying general subset inradius formula is previously implied by the published cross-polytope inequalities and is not the novelty basis.

**Cycle coverage and equality sets.** For a proper nonempty \(S\subset[n]\) of size \(k\), having \(c(S)\ge1\) cyclic components, precisely \(k+c(S)\) cycle edges meet \(S\). Therefore
\[
\frac{W(S)}{\sqrt{|S|}}=\frac{k+c(S)}{\sqrt k}\ge \frac{k+1}{\sqrt k}\ge2.
\]
The second inequality follows from \((k-1)^2\ge0\) and has equality only at \(k=1\). For the full support \(S=[n]\), \(W(S)=n\), yielding value \(\sqrt n\). Consequently the support-minimizing subsets are the full support alone for \(n=3\), the full support and all singletons for \(n=4\), and exactly the singletons for \(n\ge5\). Their squared support minima are \(\min\{n,4\}\), and independent sign choices give exactly the stated normal counts.

**Every contact hyperplane defines a facet.** For the full-support normals, fix any sign vector \(\sigma\in\{\pm1\}^n\). Every edge diamond exposes the segment joining \(\sigma_i e_i\) and \(\sigma_j e_j\). These edge differences span the \((n-1)\)-dimensional hyperplane orthogonal to \(\sigma\), because the cycle is connected. Their Minkowski sum is therefore a genuine facet of \(K_n\). For a singleton normal \(\pm e_i\), the two adjacent diamond summands have unique maximizing points \(\pm e_i\); the remaining \(n-2\) diamonds are the edges of a path on the \(n-1\) other coordinates, and their Minkowski sum has dimension \(n-1\): the union of the coordinate-plane diamonds contains independent difference directions across all those coordinates. Hence its support face is also a facet. No other facet can touch the ball, since its unit supporting normal would have to be support-minimizing. Each listed sign pattern or singleton gives a distinct supporting hyperplane, proving the exact contact counts.

**John uniqueness and optimality.** Independent sign changes and cyclic permutation of coordinates act by Euclidean isometries preserving \(K_n\). The maximum-volume inscribed ellipsoid of a full-dimensional convex body is unique. Its center and positive-definite shape matrix are fixed by the whole symmetry group: coordinate reflections make the matrix diagonal and force the center to be zero, while cyclic permutation makes all diagonal entries equal. The John ellipsoid must therefore be a centered ball. A centered Euclidean ball of radius \(r\) lies in \(K_n\) exactly when \(r\le\min_{\|u\|=1}h_{K_n}(u)\), already computed as \(\sqrt{\min\{n,4\}}\). This completes the proof. \(\square\)

## Verification and limits

The unchanged accompanying finite checker `verify.py` covers additional outer geometry established elsewhere. For the inward claim, an independent integer/rational calculation enumerated **every nonempty coordinate subset** for \(3\le n\le7\), computed its cycle-edge coverage and exact squared support ratio, and recovered every minimizing support and signed normal count. These checks corroborate but do not prove the all-dimensional result. The all-dimensional proof is the support-level decomposition, cycle component count, facet dimension argument, and John uniqueness above. Priority is a best-of-knowledge scientific comparison, not a certification: closely related signed-permutohedron geometry might contain an unindexed equivalent inward classification. A complete primary full-text reading of Wang et al. was unavailable in this audit due to an access block; its implications are credited conservatively rather than claimed absent.

## Prior work and scope separation

- H. Wang, Q. Hou, W. Thawinrak, Z. Liu, and Z. Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037v1 (17 August 2026), especially the general subset-inequality formulation. https://arxiv.org/abs/2608.16037
- *The complete Euclidean vertex-shell spectrum of cyclic cross-polytope sums*, published mathematical record, 8 November 2026; exact same \(K_n\) for \(n\ge5\), with complete outer vertex radii, Löwner ball, and outer contacts. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-the-complete-euclidean-vertex-shell-spectrum-of-cyclic-cross-pol--8120a5ffa59c
- C. Eur, A. Fink, M. Larson, H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752, 2024; broader type-B combinatorial framework, no full-document priority determination made here. https://arxiv.org/abs/2209.06752
