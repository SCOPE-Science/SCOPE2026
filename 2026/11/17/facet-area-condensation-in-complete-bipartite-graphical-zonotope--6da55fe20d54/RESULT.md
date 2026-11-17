# Facet-area condensation in complete-bipartite graphical zonotopes

## Finding

Let \(q\ge2\) be an integer, let \(G=K_{2,q}\) have hubs \(h_1,h_2\) and leaves \(\ell_1,\ldots,\ell_q\), and equip \(\mathbb R^{q+2}\) with its standard Euclidean metric. Define the graphical zonotope
\[
 Z_q=\sum_{i=1}^{2}\sum_{j=1}^{q}[e_{h_i},e_{\ell_j}],
\]
with all volumes measured intrinsically in its \((q+1)\)-dimensional affine hull. Write \(A_q\) for its \(q\)-dimensional Euclidean boundary area and \(W_q\) for its \((q+1)\)-dimensional volume.

**Complete facet-area spectrum.** There are exactly \(2q+2^{q+1}\) facets, partitioned into the following *combinatorially labeled* types (coincident numerical areas are counted separately):

* Exactly \(2q\) leaf-singleton cut facets, each having \(q\)-dimensional area
  \[
  L_q=(q-1)2^{q-2}\sqrt{q+1}.
  \]
* For each \(b\in\{0,\ldots,q\}\), exactly \(2\binom qb\) further facets, each having area
  \[
  a_{q,b}=\sqrt{(b+1)(q-b+1)}.
  \]
  At \(b=0,q\) these are the four hub-singleton cut facets; all other cases split the two hubs between the two sides of the cut.

Consequently,
\[
 \boxed{A_q=2qL_q+2\sum_{b=0}^q\binom qb\sqrt{(b+1)(q-b+1)},\qquad
 W_q=\sqrt{q+2}\,q2^{q-1}.}
\]

**Surface-area condensation.** Let \(\mathcal L_q\) denote the union of the \(2q\) leaf-singleton facets. Although these are an exponentially vanishing fraction of the total number of facets, their share of surface area tends to one. More precisely,
\[
\boxed{\frac{\#\{\text{leaf-singleton facets}\}}{\#\{\text{all facets}\}}=\frac{q}{q+2^q}\longrightarrow0,\qquad
\frac{\operatorname{Area}_q(\mathcal L_q)}{A_q}
=1-\frac2{q^{3/2}}+O(q^{-5/2}).}
\]
The exact surface-to-volume ratio also satisfies
\[
\boxed{\frac{A_q}{W_q}=q-\frac32+\frac2{\sqrt q}+O(q^{-1}).}
\]
The implied constants in the big-\(O\) statements are absolute as \(q\to\infty\) through integers.

## Assumptions and scope

All edges have unit segment weight, the embedding is the inherited ordinary Euclidean metric, and \([e_u,e_v]\) is the segment between the two standard coordinate vectors. Translating each segment to \([0,e_u-e_v]\) preserves all asserted Euclidean measures. Replacing these by \([- (e_u-e_v),e_u-e_v]\) *without scaling by one half* would instead dilate the body by two and change both areas and volume; that different convention is excluded. The term area means intrinsic \(q\)-dimensional Hausdorff measure of a facet (or sum of those measures for the boundary), not a normalized lattice volume. At \(q=2\), distinct facet types can have equal area without merging facets.

## Proof

**1. Connected-cut criterion and orthogonal decomposition.** For any connected graph \(H=(V,E)\) on \(n\) vertices, consider the zonotope \(\sum_{uv\in E}[e_u,e_v]\). A linear form that is constant on a nonempty subset \(S\subsetneq V\) and takes a distinct constant value on its complement fixes one endpoint of each crossing-edge segment, while retaining each segment with both endpoints in \(S\) or in \(V\setminus S\). The exposed face is therefore, up to translation, the sum of the two graphical zonotopes of the induced subgraphs \(H[S]\) and \(H[V\setminus S]\). Their direction subspaces have disjoint coordinate supports and are orthogonal. Its dimension is
\[
 (|S|-c(H[S]))+(|V\setminus S|-c(H[V\setminus S])),
\]
where \(c\) counts connected components (including isolated vertices). This dimension is \(n-2\) if and only if both induced graphs are connected, giving precisely the facet-defining cuts. Conversely every zonotope facet normal is perpendicular to its retained edge directions, hence has exactly two connected constant-coordinate blocks: for a connected graph, a facet is an oriented connected cut. The sets \(S\) and its complement label opposite, distinct facets.

**2. A Euclidean forest-volume rule.** For every connected graph \(H\) on \(s\ge2\) labeled vertices, its intrinsic graphical-zonotope volume equals \(\sqrt{s}\,\tau(H)\), where \(\tau(H)\) is its spanning-tree count; for \(s=1\), interpret this as \(1\). Indeed the zonotope volume is the sum of Euclidean parallelotope volumes of all independent \(s-1\)-element subsets of its edge-root generators. The independent subsets are spanning trees; every tree's rooted incidence matrix has determinant \(\pm1\), and the Euclidean Gram determinant of its \(s-1\) root columns is \(s\), by Cauchy–Binet or the matrix-tree identity. Thus every spanning tree contributes \(\sqrt{s}\). For a facet cut \(S\), orthogonality yields
\[
 \operatorname{Area}_{n-2}(F_S)
 =\sqrt{|S|}\,\tau(H[S])\cdot
   \sqrt{|V\setminus S|}\,\tau(H[V\setminus S]),
\]
with the singleton convention.

**3. Exhaust the cuts of \(K_{2,q}\).** Since leaves are mutually nonadjacent, each connected induced subgraph of size at least two must contain a hub. Thus the connected cuts are exclusively:

(a) \(S\) is one leaf, or its complement is one leaf. There are \(2q\) such oriented cuts. Their nonsingleton induced graph is \(K_{2,q-1}\) on \(q+1\) vertices. Its spanning-tree count is \(2^{q-2}(q-1)\) by the complete-bipartite matrix-tree formula. The facet area is \(L_q\).

(b) \(S\) contains exactly one hub and exactly \(b\) leaves; its complement contains the other hub and \(q-b\) leaves, with \(0\le b\le q\). There are \(2\binom qb\) such cuts. The two induced graphs are stars \(K_{1,b}\) and \(K_{1,q-b}\), counting a single vertex as the zero-dimensional case. Both have spanning-tree count one, and orthogonality gives \(a_{q,b}\). This exhausts all cuts without duplication.

The stated facet spectrum and boundary-area sum follow. The entire volume is \(W_q=\sqrt{q+2}\,\tau(K_{2,q})=\sqrt{q+2}\,q2^{q-1}\), using the same forest-volume rule.

**4. Quantitative condensation.** If \(B\sim\operatorname{Binomial}(q,1/2)\), define
\[
 M_q=\mathbb E\sqrt{(B+1)(q-B+1)}.
\]
The area of the nonleaf facets is exactly \(2^{q+1}M_q\), while that of the leaf facets is \(2qL_q\). Hence the exact nonleaf-to-leaf ratio is
\[
 R_q=\frac{2^{q+1}M_q}{2qL_q}
 =\frac{4M_q}{q(q-1)\sqrt{q+1}}.
\]
Set \(a=(q+2)/2\) and \(Y=B-q/2\). Then the random variable under the square root is \(\sqrt{a^2-Y^2}\). Put \(u=Y^2/a^2\in[0,1)\). The elementary identity
\[
 0\le a\left(1-\frac u2-\sqrt{1-u}\right)
 =\frac{Y^4}{2a^3(1+\sqrt{1-u})^2}\le\frac{Y^4}{2a^3}
\]
and the exact binomial central moments
\[
 \mathbb E Y^2=\frac q4,\qquad
 \mathbb E Y^4=\frac{3q^2}{16}-\frac q8
\]
show uniformly that
\[
 M_q=a-\frac{q}{8a}+O(q^{-1})
 =\frac q2+\frac34+O(q^{-1}).
\]
It follows that \(R_q=2q^{-3/2}+O(q^{-5/2})\), and the leaf surface-area share is \((1+R_q)^{-1}=1-2q^{-3/2}+O(q^{-5/2})\). Dividing the two exact terms in \(A_q\) by \(W_q\) gives
\[
 \frac{A_q}{W_q}
 =(q-1)\sqrt{\frac{q+1}{q+2}}
 +\frac{4M_q}{q\sqrt{q+2}}
 =q-\frac32+\frac2{\sqrt q}+O(q^{-1}).
\]
This proves every part.

## Verification

A reproducible Python program, `verify_k2q.py`, constructs the actual vertices in the inherited Euclidean coordinates and uses convex hulls in orthonormal affine coordinates to compare every predicted facet measure with direct Euclidean measurements. For \(q=2,3,4\), it verifies all \(12+22+40=74\) facets individually, along with total area and volume. Its separately evaluated stable binomial expectations corroborate the large-\(q\) constants at \(q=100,1000,3000\). Run `python verify_k2q.py` with the versions declared in `requirements.txt`. These numerical tests are finite consistency checks; the all-\(q\) and asymptotic statements are established by the proof above.

## Relationship to prior work

Chapoton and Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra* (first preprint January 18, 2022), use complete-bipartite graphical zonotopes as the shuffle of two points, establish their facet combinatorics, and tabulate facet counts (especially Proposition 36, Proposition 101, and Appendix A). The \(2q+2^{q+1}\) facet **count is therefore not claimed to be new**. Dall and Pfeifle's *A Polyhedral Proof of the Matrix Tree Theorem* (2014) provides the known spanning-tree/zonotope-volume framework; that framework is used rather than reasserted as a new theorem. Padrol, Pilaud, and Poullot's *Deformed Graphical Zonotopes* (online 2023) addresses deformation cones and normal-fan geometry, not the Euclidean facet-area probability law. The specific facet-area spectrum, exact surface-area series, and vanishing-facet-fraction/near-total-area phenomenon are the proposed contributions.

## Limitations

The statement is restricted to the two-hub complete-bipartite family \(K_{2,q}\), its unweighted unit-segment realization, and the inherited Euclidean metric. The formula does not assert analogous condensation for arbitrary bipartite graphs or weighted generators. The literature comparison supports best-knowledge novelty, not a proof that no equivalent unindexed publication exists. No external independent mathematical audit is represented by the numerical checks.

## References

1. F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first submitted 2022-01-18. https://arxiv.org/abs/2201.06896
2. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, arXiv:1404.3876, 2014. https://arxiv.org/abs/1404.3876
3. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry, online 2023-10-13, DOI:10.1007/s00454-023-00586-x. https://doi.org/10.1007/s00454-023-00586-x
