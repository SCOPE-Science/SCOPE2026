# The wheel general-position complex is a projective plane at five rim vertices and a periodic sphere wedge thereafter

## Finding

Let \(W_n=K_1\vee C_n\) be the wheel with \(n\ge3\) rim vertices, and let \(\operatorname{GP}(W_n)\) consist of all vertex subsets having **no three distinct vertices on any common graph-geodesic**. The following is a complete *integral homotopy* classification:

\[
\operatorname{GP}(W_n)\simeq
\begin{cases}
\{\mathrm{point}\}, & n=3,\\
\bigvee^2 S^1, & n=4,\\
\mathbb{RP}^{2}, & n=5,\\
S^2\vee \operatorname{Ind}_2(C_n), & n\ge6.
\end{cases}
\]

Here \(\operatorname{Ind}_2(C_n)\) denotes the simplicial complex of subsets of the rim whose induced connected components have at most two vertices. The last term has the following previously determined integral homotopy types (Deshpande–Singh, Theorem 4.6):

\[
\operatorname{Ind}_2(C_n)\simeq
\begin{cases}
\bigvee^3 S^{2k-1},&n=4k,\\
S^{2k-1},&n=4k+1,\\
S^{2k},&n=4k+2,\\
S^{2k+1},&n=4k+3.
\end{cases}
\qquad (n\ge6).
\]

Thus the only integral torsion among this entire wheel family occurs at \(n=5\):
\(H_1(\operatorname{GP}(W_5);\mathbb Z)\cong\mathbb Z/2\mathbb Z\). In particular \(\operatorname{GP}(W_5)\) is not a wedge of spheres. For each \(n\ge6\) the homotopy type is a wedge of spheres, with one new two-sphere in addition to the known rim summands.

## Assumptions and scope

Graphs are finite, undirected, unweighted and simple. \(C_n\) is the simple cycle with \(n\) vertices, \(K_1\) denotes a single universal hub vertex, and the wheel is their graph join. The number \(n\) always counts rim vertices, so \(W_n\) has \(n+1\) vertices. A geodesic is a shortest graph path between its endpoints. A subset is in ordinary general position if it contains no three distinct vertices all lying on one geodesic; the empty set is a simplex. The geometric realization of a simplicial complex is implicit in homotopy and homeomorphism statements. This is **not** the ordinary independence complex or the graph's general-position polynomial.

## Proof

**1. Exact face decomposition.** For \(n\ge4\) the graph \(W_n\) has diameter two. Denote its hub by \(h\), and index rim vertices cyclically as \(v_0,\dots,v_{n-1}\). A triple of selected rim vertices lies on a geodesic exactly when it consists of three cyclically consecutive rim vertices: the middle rim vertex can lie on a two-edge geodesic only when it is adjacent to both endpoints along the rim. Therefore a hub-free vertex subset is in general position if and only if its rim indicator has no cyclic occurrence of \(111\). Equivalently, every connected component induced by the chosen rim vertices has at most two vertices. Such subsets form precisely \(K_n=\operatorname{Ind}_2(C_n)\).

A hub-containing subset is in general position if and only if all its selected rim vertices are pairwise adjacent. Indeed, nonadjacent selected rim vertices lie at distance two via the hub, contradicting general position; if all selected rim vertices are pairwise adjacent, the selected vertices form a clique in \(W_n\), so no triple lies on a geodesic. Since the rim is \(C_n\), its clique complex is exactly its 1-dimensional cycle \(L_n=C_n\) when \(n\ge4\). Thus the full simplicial complex is the union
\[
\operatorname{GP}(W_n)=K_n\cup_{L_n}(h*L_n),
\]
where \(h*L_n\) is the simplicial cone and \(L_n\subseteq K_n\) is the rim cycle as a subcomplex. (Every rim edge is indeed a face of \(K_n\).) On realization this is the homotopy cofiber of the inclusion \(L_n\hookrightarrow K_n\).

**2. Every \(n\ge6\).** Deshpande and Singh's Theorem 4.6, specialized to their parameters \(d=4\) and hence \(r=2\), gives the above four-periodic *homotopy equivalences* for \(K_n\), not merely a homology rank table. For every \(n\ge6\) every sphere occurring there has dimension at least two: \(K_n\) is simply connected and path-connected. Any map from the circle \(L_n\cong S^1\) into such a space is therefore nullhomotopic. The homotopy cofiber of a nullhomotopic map \(S^1\to K_n\) is homotopy equivalent to \(K_n\vee\Sigma S^1\cong K_n\vee S^2\). This proves the formula with its integral, unstable homotopy content, and immediately establishes the torsion-free assertion for these \(n\).

**3. The four-rim boundary.** For \(n=4\), no three distinct rim vertices are allowed, so \(K_4\) is the complete graph \(K_4\), viewed as a one-dimensional simplicial complex. It has cycle rank three. The subcomplex \(L_4=C_4\) is a simple embedded cycle; choosing a maximal spanning tree containing three consecutive rim edges identifies its attaching loop with a primitive free generator of the free group \(\pi_1(K_4)\). Attaching the hub cone fills this one loop. Collapsing its disk and this generator leaves a graph with two independent circles, giving \(\operatorname{GP}(W_4)\simeq\bigvee^2 S^1\).

**4. The five-rim torsion exception.** For \(n=5\), the rim-only complex \(K_5\) contains all five rim vertices, every rim edge, and exactly five triangles \(\{v_i,v_{i+1},v_{i+3}\}\) (indices modulo five; equivalently all five three-vertex rim subsets with no three consecutive vertices). Adding the cone on the rim cycle creates one more vertex, five hub edges and five hub triangles. Consequently the whole complex has exactly \(6\) vertices, \(15\) edges and \(10\) triangles, with no higher-dimensional faces. Each edge belongs to exactly two triangles, and each of the six vertex links is a connected five-edge, five-vertex cycle (these facts also follow by inspecting the cyclic face rule). Therefore the realization is a closed connected triangulated surface. Its Euler characteristic is \(6-15+10=1\). The classification of closed connected surfaces implies that this surface is homeomorphic to \(\mathbb{RP}^{2}\). Its first integral homology is \(\mathbb Z/2\mathbb Z\), its second integral homology vanishes, and its fundamental group is \(\mathbb Z/2\mathbb Z\).

**5. The three-rim boundary.** For \(n=3\), the wheel is the complete graph \(K_4\). Every subset is in general position; the complex is a full three-simplex, hence contractible.

These cases exhaust all integers \(n\ge3\).

## Verification

The standalone standard-library Python file `verify.py` constructs \(W_n\) directly, computes all-pairs shortest-path distances via breadth-first search, and enumerates all forbidden geodesic triples. For every integer \(3\le n\le12\), it independently compares **every** vertex subset with the cone–cycle face criterion used in the proof and recomputes the reduced simplicial mod-two homology by exact bit-matrix elimination. At \(n=5\), it also exhaustively checks the six vertex links and fifteen edge incidences of the claimed closed surface. The resulting output is in `expected_output.txt`. Direct enumeration confirms the predicted Betti numbers at these ten sample sizes and the precise surface structure at \(n=5\); the infinite-family classification rests on the symbolic homotopy-cofiber argument and the cited all-length cycle theorem, not on these finite samples.

## Relationship to prior work

The exact rim-complex homotopy formula is **due to Deshpande and Singh**, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, Theorem 4.6, and is not presented as a new cycle calculation. The graph-geodesic characterization of wheel general-position sets and their maximal-set cardinalities appears in Yao–He–Ji–Li (2020) and in the previously published 2026 wheel-facet classifications listed below. Iršič–Klavžar–Rus–Tuite (2024), Proposition 3.3, counts all general-position vertex subsets under graph joins but does not determine the homotopy type, the cofiber attaching map, or the torsion in the exceptional six-vertex complex. The two 2026 wheel studies enumerate inclusion-maximal general-position sets, not the integral homotopy type of the full simplicial complex.

The contribution here is the explicit cone–cycle homotopy cofiber description, the exact nullhomotopy threshold, the full unstable homotopy classification of the wheel family, and, especially, the identification of the five-rim complex as a six-vertex triangulation of the real projective plane. The stable part is an application of the cited cycle theorem after a new identification of the attachment; this dependence is essential to the priority claim and should not be overlooked.

## Limitations

No homotopy classifications for arbitrary cones, weighted-geodesic variants or metric spaces beyond the stated graph wheels are claimed. The four-periodic rim term is prior literature and is explicitly credited. The surface recognition is a finite combinatorial argument, while the infinite-family cofiber splitting requires the known all-length cycle theorem. An unindexed equivalent wheel homotopy result remains a genuine publication-priority risk. Independent mathematical review has not been performed.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020-01-15), Theorem 4.6. https://arxiv.org/abs/2001.05448
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11), Proposition 3.3. https://arxiv.org/abs/2401.05696
3. Y. Yao, M. He, S. Ji and G. Li, *On the general position set of two classes of graphs*, arXiv:2002.03108 (first posted 2020-02-08), Section 4, Theorem 4.1. https://arxiv.org/abs/2002.03108
4. *Exact facet spectrum and cyclic transfer polynomial for wheel general-position sets* (archive-dated 2026-11-08; publicly committed 2026-11-09), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-facet-spectrum-and-cyclic-transfer-polynomial-for-wheel-ge--6fdafe068eeb
5. *The maximal general-position polynomial of wheel graphs* (archive-dated 2026-11-02; publicly committed 2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-maximal-general-position-polynomial-of-wheel-graphs--273b6a86bbe7
