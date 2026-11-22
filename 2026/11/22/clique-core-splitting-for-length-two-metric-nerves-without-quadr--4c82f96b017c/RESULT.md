# Clique-core splitting for length-two metric nerves without quadrilaterals

## Finding

For every finite connected simple graph \(G\) with the unweighted shortest-path metric and **no cycle of length four** (not even a noninduced one), write \(v=|V(G)|\), \(e=|E(G)|\), and let \(t\) be its number of unoriented three-cycles. For the inclusive length-two ordered enriched nerve \(N_2(G)\), the noncanonical integral homotopy equivalence is

\[
|N_2(G)|\simeq |\operatorname{Cl}(G)|\vee\bigvee^{e+5t}S^2
\simeq\bigvee^{e-v+1-t}S^1\vee\bigvee^{e+5t}S^2.
\]

Here \(\operatorname{Cl}(G)\) is the ordinary graph clique complex, including the filled triangles. Both multiplicities are nonnegative. Consequently \(\widetilde H_1(|N_2(G)|;\mathbb Z)\cong\mathbb Z^{e-v+1-t}\), \(\widetilde H_2(|N_2(G)|;\mathbb Z)\cong\mathbb Z^{e+5t}\), and all other reduced integral homology vanishes. This is a statement of homotopy type, not only a rank or Euler-characteristic formula.

As a noncactus example, attach a triangle to a pentagon along an entire edge; then \((v,e,t)=(6,7,1)\), and the result is \(S^1\vee\bigvee^{12}S^2\). The example does not decompose as a one-point wedge of its triangle and pentagon.

## Assumptions and scope

The graph has at least one vertex, no loops or parallel edges, is finite and connected, and contains no simple four-cycle. Its graph distance satisfies \(d(a,b)=1\) on each edge. For \(n\geq0\), the \(n\)-simplices of \(N_2(G)\) are ordered tuples \((x_0,\ldots,x_n)\) with \(\sum_{i=0}^{n-1}d(x_i,x_{i+1})\leq2\). Faces delete entries; degeneracies repeat an adjacent entry. Consecutively equal entries are degenerate, but a nonconsecutive repetition such as \((a,b,a)\) is **not** degenerate. The geometric realization is that of this simplicial **set**, not an unordered flag/Rips complex or the realization of a simplicial abelian group.

The sole nondegenerate cells are vertices, oriented ordered pairs at graph distance one or two, and ordered length-two walks \((a,b,c)\) along two edges, including backtracks with \(a=c\). There are no nondegenerate cells in dimension at least three, since each nondegenerate consecutive step has distance at least one.

## Proof

**Combinatorial consequences.** If two distinct vertices had two distinct common neighbors, they would lie on a simple four-cycle. Thus a nonedge at distance two has a unique intermediate neighbor. Likewise, distinct triangles have disjoint edge sets, since two triangles sharing an edge would create a simple four-cycle. We will use both consequences for independent cell cancellations.

**Cell structure and backtracks.** Put a directed one-cell \(u_{ab}\) for every ordered pair of distinct vertices of distance at most two. For every length-two walk \((a,b,c)\), attach a two-cell with signed cellular boundary \(u_{bc}-u_{ac}+u_{ab}\) when \(a\ne c\), and \(u_{ba}+u_{ab}\) when \(a=c\). The second expression follows because the middle face \((a,a)\) is degenerate. Thus for each undirected edge \(\{a,b\}\) the two backtrack disks both have attaching word \(u_{ab}u_{ba}\), up to orientation and cyclic permutation. Using one disk, cancel the reverse one-cell \(u_{ba}\) against it; the other disk becomes trivially attached and gives one free \(S^2\). These are elementary CW one-cell/two-cell cancellations: the chosen attaching word traverses the eliminated edge once with exponent \(\pm1\), allowing the other occurrences to be substituted, rather than merely abelianized. Repeating over all \(e\) undirected edges identifies each reversed graph edge with its inverse and leaves exactly \(e\) freely attached two-spheres.

**Length-two shortcuts.** Consider an unordered pair \(\{a,c\}\) of nonadjacent vertices at distance two. Its unique intermediate neighbor is \(b\). The two ordered disks \((a,b,c)\) and \((c,b,a)\) have boundary words \(u_{ab}u_{bc}u_{ac}^{-1}\) and \(u_{cb}u_{ba}u_{ca}^{-1}\), respectively. The two directed shortcut one-cells \(u_{ac}\) and \(u_{ca}\) each occur once in a respective disk. Cancel each one-cell against its disk, substituting the two-edge original-graph path and its reverse. Since the middle vertex is unique, there are no competing length-two disks for this nonedge; all such cancellations leave no additional cells. The remaining one-skeleton is the ordinary unoriented graph, modeled by one one-cell per graph edge.

**Triangles.** For each unoriented triangle \(\{a,b,c\}\), there are exactly six ordered nondegenerate two-cells with distinct entries. All their attaching words are the same triangle-boundary loop up to inversion or cyclic permutation. Select one of the triangle's three edges. Cancel that edge one-cell against one of the six disks; substituting the remaining two-edge path into every other attaching word makes the other five triangle disks nullhomotopic as loops. Hence those five disks contribute five free two-spheres. Triangles have edge-disjoint supports, so selecting and removing one edge from each triangle is simultaneous and does not interfere with any other triangle relation. No other two-cells remain after the preceding cancellations.

**Resulting wedge.** Removing one edge from each triangle leaves a connected graph with exactly \(e-t\) edges and \(v\) vertices; connectedness holds because every removed edge has the alternate two-edge path inside its own triangle, whose edges are never removed. This graph is homotopy equivalent to \(\bigvee^{e-v+1-t}S^1\). The remaining \(e\) backtrack and \(5t\) triangle two-cells have constant attaching maps, giving the asserted wedge. Filling each original triangle also produces the same core graph, so \(|\operatorname{Cl}(G)|\simeq\bigvee^{e-v+1-t}S^1\). All steps are integral homotopy-preserving CW cancellations and substitutions, rather than conclusions inferred from field homology.

**A boundary example.** The four-cycle is excluded. Direct signed cellular computation for \(C_4\) gives \((\beta_1,\beta_2)=(0,7)\), whereas the displayed formula with \(t=0\) would incorrectly give \((1,4)\). The hypothesis is therefore substantive: distinct two-edge paths to the same nonedge create extra relations.

## Verification

The standalone file `checkers/verify_quadfree.py` exhausts every labeled connected graph on two through six vertices with no four-cycle (a total of \(5111\) graphs), builds its normalized oriented simplicial-set chains through degree two and verifies the proposed first and second Betti numbers over \(\mathbb F_2\). Exact results are in `evidence/quadfree_mod2.txt`.

The independent file `checkers/verify_small_integral.py` constructs signed integer boundary matrices for five explicit profiles including an edge-glued triangle and pentagon. It verifies \(\partial_1\partial_2=0\) and computes Smith forms of the full integer second boundary, finding only unit nonzero invariants and exactly the claimed free homology ranks; see `evidence/smith_examples.txt`. The two finite scripts are corroboration, not the proof for unbounded graph size. That proof is the preceding complete CW cancellation argument.

As a separate symbolic consistency test, the number of length-two ordered faces is \(\sum_{w\in V}\deg(w)^2\); and the number of one-cells is twice \(e+\sum_w\binom{\deg(w)}2-3t\). Thus \(\chi(|N_2(G)|)=v+6t\), agreeing with the wedge formula \(1-(e-v+1-t)+(e+5t)\).

## Relationship to prior work

The construction is Otter's total-length enriched nerve, also the \(\ell_1\) Vietoris–Rips **simplicial set** of Ivanov–Xu. The earlier published results construct this filtration, relate it to blurred magnitude homology, or prove stability and general comparisons, without the graph-specific quadrilateral-free homotopy decomposition here. Asao's November 2026 work studies length-filtered tuple homology, coarse and uniformly finite extensions, not this exact topological wedge theorem. Kuribayashi's subsequent preprint develops interleaving and product structures rather than a homotopy classification of graphs of this kind.

The special case \(t=0\), a wedge of \(e-v+1\) circles and \(e\) two-spheres, has already been established separately and is not asserted to be novel. The new part includes triangles in arbitrary noncactus graphs, establishes the sharp correction of one killed circle and five additional two-spheres per triangle, and identifies the filled clique complex as the residual homotopy core. General one-point-wedge decomposition results cover certain cactus special cases but do not cover edge-sharing cycle configurations like the example above. In contrast, unordered graph-metric Rips or Čech complexes have different cells and their formulas do not imply this one.

## Limitations

The equivalence is noncanonical and does not identify the integral automorphism representation. It applies only to finite connected graphs without four-cycles and to inclusive length exactly two; longer filtrations, disconnected formulations, integral persistent maps beyond the immediate stages, and graphs admitting quadrilaterals are not classified. Previous high-girth and graph-wedge special cases remain prior work, not new contributions. Complete publication-priority assurance requires independent literature review; the body of one related recent length-filtration preprint was unavailable during this comparison.

## References

1. N. Otter, *Magnitude meets persistence: Homology theories for filtered simplicial sets*, Homology Homotopy Appl. 24 (2022). Accepted open text: https://qmro.qmul.ac.uk/xmlui/bitstream/123456789/79678/2/Otter%20Magnitude%20meets%20persistence%202022%20Accepted.pdf . Original public preprint: https://arxiv.org/abs/1807.01540 . Definitions 9–10 and Theorem 32.
2. S. O. Ivanov and X. Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, Journal of Applied and Computational Topology 10 (2026), article 15. Open full text: https://link.springer.com/article/10.1007/s41468-026-00247-x . In particular §§1–2.
3. Y. Asao, *Magnitude, path and coarse homology*, arXiv:2611.05972v1, first public 4 November 2026. https://arxiv.org/html/2611.05972v1 . Introduction and §3.
4. K. Kuribayashi, *Enriched nerves, interleaving distances and the multiplicative magnitude-path spectral sequence*, arXiv:2611.22433v1, first public 17 November 2026. https://arxiv.org/html/2611.22433v1 . §§1–3. This later paper is comparison literature, not the date anchor for the present direction.
5. L. Melodia, *Magnitude Homology Is the Associated Graded of the Length Filtration*, arXiv:2608.21479v1. https://arxiv.org/abs/2608.21479 . Abstract was accessible; full manuscript not available to inspect during this comparison.
