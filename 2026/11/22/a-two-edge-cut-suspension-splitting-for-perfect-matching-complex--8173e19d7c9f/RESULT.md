# A two-edge-cut suspension splitting for perfect-matching complexes

## Finding
Let \(G_1,G_2\) be finite simple graphs on disjoint even vertex sets. Choose distinct vertices \(a,b\in V(G_1)\) and \(c,d\in V(G_2)\), with \(ab\in E(G_1)\) and \(cd\in E(G_2)\). Suppose that each of the four graphs \(G_1,G_2,G_1-\{a,b\},G_2-\{c,d\}\) admits a perfect matching. Construct \(H\) from the disjoint union of \(G_1\) and \(G_2\) by adjoining only the edges \(ac\) and \(bd\) between the two vertex sets. Write \(\mathcal P(G)\) for the simplicial complex of all edge sets extendible to perfect matchings of \(G\), and \(*\) for simplicial join.

Then there is a nonequivariant homotopy equivalence
\[
\mathcal P(H)\simeq
\big(\mathcal P(G_1)*\mathcal P(G_2)\big)
\vee\Sigma\big(\mathcal P(G_1-\{a,b\})*\mathcal P(G_2-\{c,d\})\big).
\]
Moreover, the canonical inclusion \(\mathcal P(G_1)*\mathcal P(G_2)\hookrightarrow\mathcal P(H)\) is split injective on reduced integral homology in every degree, with the suspension summand as its complementary group.

In particular, let \(H_{6,6}\) be the twelve-vertex graph consisting of two copies of \(K_6\) on \(\{0,\ldots,5\}\) and \(\{6,\ldots,11\}\), joined only by \(\{0,6\}\) and \(\{1,7\}\). Then
\[
\boxed{\mathcal P(H_{6,6})\simeq
\bigvee^{4}S^2\ \vee\ \bigvee^{256}S^3.}
\]
This is an integral homotopy decomposition, not merely a Betti-number or Euler-characteristic calculation.

## Assumptions and scope
All graphs are finite, simple and undirected; the distinguished vertices within each graph are different. Both sides have even, positive order; both bridge edges are distinct and have disjoint endpoints. Deletion \(G-\{u,v\}\) means induced vertex deletion. All four perfect-matching complexes in the theorem are nonvoid. Graph edges are vertices of the perfect-matching complex, so an edge not belonging to any perfect matching is excluded from that complex. A perfect matching is a set of pairwise vertex-disjoint edges covering every graph vertex. The empty face is included combinatorially, but the topology concerns ordinary geometric realizations of nonvoid complexes. The joins in the theorem are nonempty and path-connected, so the stated wedge decomposition has the usual unambiguous based homotopy meaning.

## Proof
Set
\[
K_0=\mathcal P(G_1)*\mathcal P(G_2),\qquad
A=\mathcal P(G_1-\{a,b\})*\mathcal P(G_2-\{c,d\}).
\]
Let \(e=ac\) and \(f=bd\) be the two new graph edges, and let \(K_2=\Delta(\{e,f\})*A\), where \(\Delta(\{e,f\})\) is the full one-simplex on these edge-vertices.

**Parity classification.** Every perfect matching of \(H\) has either zero or two cross edges: the number of cross edges in a perfect matching has the parity of the even number of vertices on the first side. As there are only two cross edges, exactly these alternatives occur. Zero-cross perfect matchings are precisely the unions of a perfect matching of each \(G_i\), giving \(K_0\). Two-cross perfect matchings contain both \(e,f\) and restrict to perfect matchings of the vertex-deleted graphs, giving \(K_2\). Thus \(\mathcal P(H)=K_0\cup K_2\), and \(K_2\) is contractible.

**Exact intersection.** Any face in \(K_0\cap K_2\) avoids \(e,f\), hence belongs to \(A\). Conversely any face of \(A\) is contained in a union of perfect matchings of the punctured sides. Appending the internal edges \(ab\) and \(cd\) yields perfect matchings of the two original sides, respectively. Therefore \(A\subseteq K_0\), and \(K_0\cap K_2=A\), with its original simplicial structure.

**Nullhomotopy.** Every face \(\sigma\in A\) may be augmented by \(ab\) in the left factor without losing extendibility, because its left part avoids \(a,b\) and extends to a perfect matching of \(G_1-\{a,b\}\). Therefore the inclusion \(A\hookrightarrow K_0\) factors through the simplicial star of the vertex \(ab\) in \(K_0\). That star is a cone, so the inclusion is nullhomotopic. The two-piece simplicial union is a homotopy pushout of the cofibrations \(A\hookrightarrow K_0\) and \(A\hookrightarrow K_2\). Because \(K_2\) is contractible, it has the homotopy type of the mapping cone of \(A\to K_0\). The map is nullhomotopic, so the cone splits as \(K_0\vee\Sigma A\). The splitting identifies the original inclusion of \(K_0\) as the first wedge summand and proves the integral homology statement.

**The two-clique example.** Every matching of \(K_6\) extends to a perfect matching, so \(\mathcal P(K_6)\) is its ordinary matching complex. It has fifteen vertices (edges of \(K_6\)), forty-five one-faces (unordered pairs of disjoint graph edges), and fifteen two-faces (perfect matchings). Every one-face is in exactly one two-face, as the two remaining vertices have a unique pairing. Collapse each two-simplex over any of its free one-faces. These fifteen elementary collapses leave a connected graph with fifteen vertices and thirty edges, hence a wedge of sixteen circles:
\[\mathcal P(K_6)\simeq\bigvee^{16}S^1.\]
Likewise \(\mathcal P(K_4)\) is the disjoint union of three one-simplices, one per perfect matching of \(K_4\), hence it is homotopy equivalent to three discrete points. Homotopy invariance of joins therefore gives
\[
\mathcal P(K_6)*\mathcal P(K_6)\simeq\bigvee^{256}S^3,
\quad
\mathcal P(K_4)*\mathcal P(K_4)\simeq K_{3,3}\simeq\bigvee^{4}S^1.
\]
Applying the splitting and suspending the latter join yields the asserted \(4\) two-spheres and \(256\) three-spheres.

## Verification
The standalone file `checker.py` independently enumerates all perfect matchings and all faces of \(\mathcal P(H_{6,6})\) using only standard Python. Running `python checker.py` checks 234 perfect matchings, partitioned into 225 that avoid the cross edges and nine that use both. The complete simplicial face vector in dimensions zero through five is
\[(32,340,1476,2589,1404,234),\]
with Euler characteristic \(-251\). Exact binary boundary reductions give reduced Betti ranks \((0,0,4,256,0,0)\) in dimensions zero through five. The exhaustive face intersection contains exactly 100 faces including the empty face, agreeing with the join of the three-segment complexes on the punctured \(K_4\) sides. These finite checks corroborate the explicit example but do not establish the unrestricted graph theorem; the parity/intersection/cone proof does that.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduced perfect-matching complexes and computed honeycomb families; their 2023 paper records the equivalence with ordinary matching complexes for complete even graphs. Chandrakar and Singh (2025) obtained wedge classifications for polygonal line tilings. Chandrakar, Chau, Goyal, Karki and Subhash (first public November 13, 2026) proved a Fibonacci sphere-wedge classification for the \(3\times2n\) rectangular grid by a star-cover recursion. These papers motivate compositional tools for perfect-matching topology. The claim here is specifically a general two-edge-cut splitting for two even graph sides containing the internal endpoint edges, and its exact mixed-dimensional twelve-vertex example; it neither claims the previous grid classifications nor restates the familiar single-vertex link/deletion lemma.

## Limitations
The formula does not assert a similar splitting for odd vertex sides, one cross edge, more than two cross edges, or when the internal edges \(ab,cd\) are missing. No natural equivariant splitting or canonical wedge equivalence is claimed. The calculation of the two-clique example is valid integrally because an actual homotopy equivalence was proved; the mod-two checker alone does not prove integral torsion-freeness. Literature comparisons are not a proof of publication priority, and an unindexed equivalent cut decomposition remains a residual risk.

## References
- H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of \(3\times 2n\) Grid Graph*, arXiv:2611.18058v1, first public November 13, 2026, https://arxiv.org/abs/2611.18058.
- M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30 (2023), P2.45, https://doi.org/10.37236/11525; preprint arXiv:2209.02803.
- H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, Annals of Combinatorics 29 (2025), 1211–1233, https://doi.org/10.1007/s00026-025-00755-0; preprint arXiv:2407.05809.
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, https://arxiv.org/abs/2608.30601.
