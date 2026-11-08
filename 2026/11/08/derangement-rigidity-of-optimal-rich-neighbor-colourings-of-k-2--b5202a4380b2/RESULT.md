# Derangement rigidity of optimal rich-neighbor colourings of \(K_{2,n}\)

## Finding
For every integer \(n\ge3\), let \(G=K_{2,n}\), with its vertices and edges labelled, and fix a palette of \(n+1\) named colours. An edge is *rich* in a proper edge-colouring if all edges adjacent to it have pairwise distinct colours. A proper colouring is *rich-neighbor* if every edge has a **different**, adjacent rich edge. Let \(!r\) be the number of derangements of \(r\) labelled objects, and let \(p_{\ge2}(r)\) be the number of integer partitions of \(r\) whose parts are at least two.

**Structural classification.** Every rich-neighbor colouring with this palette has exactly two rich edges. They are the two edges in one uniquely determined column (one vertex on the \(n\)-side). Their two colours are distinct. The other \(n-1\) columns carry precisely the same set of \(n-1\) colours in the two rows, each used once per row, and the relative row permutation is a derangement. Conversely, every such arrangement is rich-neighbor.

**Exact enumeration.** The number of these labelled, named-colour assignments is
\[
F_n=n(n+1)n\,(n-1)!\,!(n-1).
\]
Up to graph automorphisms and arbitrary permutations of colour names, the number of optimal colourings is exactly
\[
p_{\ge2}(n-1).
\]
These equivalence classes are uniquely distinguished by the cycle type of their relative derangement.

Among all proper edge-colourings from the same \(n+1\)-colour palette (with unused colours allowed), the exact fraction that are rich-neighbor is
\[
P_n=\frac{n\,!(n-1)}{!(n+1)+!n},
\qquad \lim_{n\to\infty}nP_n=1.
\]
For \(n=3,4,5\), the named optimum counts are respectively \(72,960,32400\). For the boundary \(n=2\), no three-colour rich-neighbor colouring exists; the four-colour optimum has \(24\) named colourings.

## Assumptions and scope
Graphs are finite, simple and labelled. Write the two vertices on the small side of \(K_{2,n}\) as \(u,v\), and the vertices on the other side as \(b_1,\ldots,b_n\). The palette consists of exactly \(n+1\) available named colours; a proper edge-colouring need not use every available colour, but every rich-neighbor colouring in the theorem does. Two edges are adjacent if they share a vertex. Richness concerns pairwise inequality among the colours on edges adjacent to a specified edge, not the edge's own colour (properness already excludes equality with its own adjacent edges).

The known optimum rich-neighbor chromatic index of \(K_{2,n}\) is \(n+1\) for \(n\ge3\), by Kong (2026). The enumeration and equivalence classification concern **all** colourings at that known optimum, not a new determination of the chromatic index.

## Proof
Fix \(n\ge3\), write \(k=n+1\), and consider any proper colouring with colours in a fixed set \(C\) of size \(k\). Each row \(\{ub_j\}\) and \(\{vb_j\}\) uses \(n\) different colours, so each omits exactly one colour of \(C\), say \(\alpha\) in the \(u\)-row and \(\beta\) in the \(v\)-row.

The edges adjacent to \(ub_j\) are the \(n-1\) other \(u\)-row edges and the single edge \(vb_j\). Therefore \(ub_j\) is rich if and only if the colour on \(vb_j\) equals \(\alpha\): it must be absent from the \(u\)-row, as it already differs from the colour of \(ub_j\). As the \(v\)-row has no repetitions, at most one edge in the \(u\)-row is rich. Similarly \(vb_j\) is rich if and only if the colour on \(ub_j\) equals \(\beta\), and at most one edge in the \(v\)-row is rich.

If a colouring is rich-neighbor, at least one rich edge exists. Every rich edge itself requires a distinct adjacent rich edge, so the two rows must each contribute exactly one rich edge and these two must be adjacent. Since they lie in different rows, adjacency forces both rich edges to be in the same column \(b_j\). Conversely, if both edges in one column are rich, every other edge meets the corresponding rich edge in its row, and each of the two rich edges meets the other; the colouring is rich-neighbor. The column is unique because each row has at most one rich edge.

Let the colours at the unique rich column be \(x\) on \(ub_j\) and \(y\) on \(vb_j\). Properness gives \(x\ne y\). The two richness equivalences imply \(\alpha=y\) and \(\beta=x\). The remaining \(n-1\) columns therefore contain, in each row, each colour from \(C\setminus\{x,y\}\) exactly once. The two row permutations of this shared \(n-1\)-set must disagree at every column to preserve properness. Equivalently, once one row is ordered, the relative permutation \(\sigma\) of the other row is a derangement. This proves the structural classification and its converse.

To enumerate, choose the exceptional column in \(n\) ways, the ordered pair \((x,y)\) of colours in \(k(k-1)=(n+1)n\) ways, the first off-column row in \((n-1)!\) ways, and the second off-column row in \(!(n-1)\) ways. There is no overcount, since the exceptional column is unique. This proves the formula for \(F_n\).

For equivalence classes, first normalize the exceptional column, the two ordered colours there, and the first off-column row by relabelling graph vertices and colours. The only remaining datum is a derangement \(\sigma\in S_{n-1}\). An arbitrary relabelling of off-column colours, coupled with the corresponding column permutation, transforms \(\sigma\) to a conjugate; swapping \(u,v\) transforms it to \(\sigma^{-1}\). Conversely, the exceptional column is intrinsic, and all allowed relabellings induce only conjugation or conjugation after inversion on the relative permutation. Since a permutation and its inverse have the same cycle type, two colourings are equivalent exactly when their derangements have the same cycle type. Derangements have no one-cycles, so their conjugacy classes correspond to partitions of \(n-1\) with all parts at least two.

For the probability, first choose an arbitrary injective first row in \((n+1)!\) ways. Given this row, an injective second row must avoid its colour in each matching column. It is equivalent to a permutation of \(n+1\) colours in which the first \(n\) positions are not fixed. If the last position is also nonfixed, it is a derangement of \(n+1\) positions; if the last position is fixed, the first \(n\) positions form a derangement of \(n\). Thus the total proper count is \((n+1)!\big(!(n+1)+!n\big)\), and the ratio with \(F_n\) simplifies to \(P_n\). The classical estimate \(!r\sim r!/e\) gives \(P_n\sim 1/(n+2)\), hence \(nP_n\to1\).

At \(n=2\), a derangement of one object does not exist, so no three-colour solution is possible. Four distinct edge colours make all four edges of \(C_4\) rich, and the optimum colourings are the \(4!=24\) bijections from edges to four named colours.

## Verification
The standalone `verify.py` reconstructs the edge adjacency definition directly. By colour-name symmetry it fixes the first row to \(0,\ldots,n-1\) and iterates all injective second rows from an \(n+1\)-colour palette, checking properness, richness, and the requirement of a distinct adjacent rich edge. It compares the resulting totals, exceptional-column positions, and cycle types against the formulas for every \(2\le n\le8\). The multiplier \((n+1)!\) restores all possible first rows. Run `python3 verify.py` from a directory containing the file; only Python's standard library is required. Exhaustive finite tests are corroboration, not a proof for unbounded \(n\).

## Relationship to prior work
Kong's 2026 article establishes the exact optimal index \(\chi'_{\mathrm{rn}}(K_{m,n})=m+n-1\) except at \(K_{2,2}\), and constructs optimum bipartite colourings (Section 3.1). That index theorem and construction are inputs, **not** new results claimed here. The present theorem classifies *every* optimum \(K_{2,n}\) colouring, counts its named solutions, and classifies them modulo automorphism and palette relabelling, with a random-proper-colouring asymptotic. These assertions do not follow from an index value alone and are not stated in the inspected source. Kashima et al. (2026) provide general linear bounds and the rich-edge lower bound, not an optimum-count classification. Earlier papers establish the notion and subcubic cases, but the accessible summaries do not resolve the unrestricted enumerative statement.

## Limitations
The nontrivial classification assumes one bipartition class has size two and \(n\ge3\). It does not count optimum colourings of general \(K_{m,n}\) when \(m\ge3\), nor colourings using more than the minimum palette. The orbit count treats vertex and palette relabellings as equivalences; the labelled count does not. Some earlier primary full texts were not accessible, so historical priority requires independent literature confirmation. No independent mathematical audit has been performed.

## References
1. Jiangxu Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:2610.21036v1, first public 2026-10-15, https://arxiv.org/abs/2610.21036 (especially Theorem 1.2 and Section 3.1).
2. Masaki Kashima, Mirko Petruševski, Jelena Sedlar, Riste Škrekovski, *The rich-neighbor chromatic index is linear in the maximum degree*, arXiv:2610.16446v1, 2026-10-12, https://arxiv.org/abs/2610.16446 (definitions, lower bounds, general upper bounds).
3. Mirko Petruševski and Riste Škrekovski, *Proper edge-colorings with a rich neighbor requirement*, Discrete Mathematics 347 (2024), 113803, https://doi.org/10.1016/j.disc.2023.113803 (foundational definition; full text not inspected).
4. Lily Chen, Yi Tan, Xiangqian Zhou, *On the Rich-Neighbor Edge-Colorings of Subcubic Graphs*, Graphs and Combinatorics 41 (2025), 89, https://doi.org/10.1007/s00373-025-02949-y (subcubic context; abstract and bibliographic material inspected).
