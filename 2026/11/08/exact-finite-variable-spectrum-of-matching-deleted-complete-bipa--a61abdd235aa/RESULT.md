# Exact finite-variable spectrum of matching-deleted complete bipartite graphs

## Finding
For integers \(a,b\ge3\) and \(0\le t\le\min(a,b)\), let \(G(a,b,t)\) be the simple undirected graph obtained from \(K_{a,b}\) by deleting \(t\) pairwise vertex-disjoint edges. Write \(u=a-t\), \(v=b-t\), and let \(\equiv_{\mathrm{FO}^{k}}\) mean agreement on all counting-free first-order sentences in the adjacency language using at most \(k\) reusable variable names, with no bound on quantifier depth.

For \(k=1,2\), all graphs in this family have the same theory. For every \(k\ge3\), define the following invariant (unordered pairs permit exchange of the two bipartition sides):

\[
\mathcal I_k(G(a,b,t))=
\begin{cases}
(0,\{\min(a,k),\min(b,k)\}) & t=0,\\
(1,\min(t,k),\{\min(u,k),\min(v,k)\})& t>0.
\end{cases}
\]

Then \(G(a,b,t)\equiv_{\mathrm{FO}^{k}}G(a',b',t')\) if and only if their invariants \(\mathcal I_k\) agree. The precise number of theories in this infinite family at width \(k\ge3\) is

\[
T_k=\frac{k^3+4k^2-7k-2}{2}.
\]

In particular \(T_3=20\). Every theory has a unique minimum-order representative within the stated family, up to graph isomorphism. The hierarchy is strict from width two onward: for each \(k\ge3\), two graphs in this family are \(\mathrm{FO}^{k}\)-equivalent but not \(\mathrm{FO}^{k+1}\)-equivalent.

## Assumptions and scope
Graphs are finite, undirected, loopless, and have no named bipartition classes or vertices. The restriction \(a,b\ge3\) is essential for the definability argument: distinct vertices on the same bipartition side retain a common neighbor despite the deleted matching. Equality is permitted. Counting quantifiers and order predicates are not permitted. The notation \(t=0\) includes complete bipartite graphs; \(t=\min(a,b)\) includes balanced crown graphs when \(a=b\).

The two side sizes are not ordered invariants. When \(t>0\), the unmatched-side counts \(u,v\) may be zero, and they count vertices *not incident to the removed matching*, not the sizes of the two complete bipartition sides themselves.

## Proof
**1. Three-variable intrinsic reconstruction.** Let \(E\) denote adjacency. The formula

\[
S(x,y):=(x=y)\lor\exists z\,(E(x,z)\land E(y,z))
\]

uses three variable names and holds precisely when \(x,y\) lie on the same bipartition side. For distinct vertices on one side, each vertex lacks at most one neighbor on the opposite side, which has at least three vertices; hence they have a common neighbor. Vertices in opposite sides cannot have a common neighbor in a bipartite graph. Next define

\[
D(x,y):=x\ne y\land\neg E(x,y)\land\neg S(x,y),\qquad
P(x):=\exists y\,D(x,y),\qquad U(x):=\neg P(x).
\]

Here \(D\) is exactly the removed matching and \(P\) selects its endpoints. Both formulas need at most three variable names after expanding the abbreviations. The existential sentence \(\exists x\exists y\,D(x,y)\) distinguishes \(t=0\) from \(t>0\).

**2. Exact sharp thresholds.** For \(1\le j\le k\), a formula using at most \(\max(3,j)\) variable names says that there are \(j\) pairwise distinct \(P\)-vertices on one side: select \(j\) distinct vertices, assert \(P\) on each and \(S\) between each and the first. Because each bipartition side contains exactly \(t\) matched vertices, this is equivalent to \(t\ge j\). Thus \(\min(t,k)\) is recoverable whenever \(t>0\).

For the unmatched vertices, define \(Q_j(x)\) to say that \(x\) and \(j-1\) other pairwise distinct vertices lie on its side and satisfy \(U\). It uses at most \(\max(3,j)\) names. Consequently \(\exists x\,Q_j(x)\) says \(\max(u,v)\ge j\), while

\[
\exists x\exists y\,(\neg S(x,y)\land Q_j(x)\land Q_j(y))
\]

says \(\min(u,v)\ge j\). The two occurrences of \(Q_j\) are separately scoped: names used locally in one occurrence can shadow names introduced elsewhere, so the displayed sentence still needs at most \(\max(3,j)\) names. Likewise, in the counting formulas, the third bound name needed to expand \(S\) may shadow an otherwise selected name *inside that subformula* without losing any outside inequality. This is ordinary variable reuse rather than counting quantification. These formulas recover the unordered clipped unmatched counts.

When \(t=0\), every vertex satisfies \(U\), and the same two unmatched-size threshold schemes recover the unordered clipped original side sizes. Hence unequal invariants always yield a distinguishing \(\mathrm{FO}^{k}\) sentence.

**3. Unlimited-round converse.** Suppose the invariants agree. Fix a choice of matching of the two bipartition sides, including their unmatched-side counts, possibly after swapping sides. Duplicator maintains a partial correspondence of occupied vertices with the following properties: side membership is preserved; each occupied unmatched vertex corresponds injectively to an unmatched vertex on its matched side; and occupied matching endpoints correspond through an injective partial map of deleted-matching indices, with mates always mapped to mates. This preserves equality and adjacency because the only cross-side nonedges are corresponding endpoints of removed edges.

On a new move, an already occupied vertex is answered with its existing image. For a new unmatched vertex, choose an unoccupied unmatched vertex on the corresponding side. For a new matched vertex, use the already assigned matching index if its mate is occupied; otherwise choose an unused matching index. If the relevant population is smaller than \(k\), clipping equality makes the populations exactly equal. If it is at least \(k\) in both graphs, at most \(k-1\) occupied pebbles precede a move, so a fresh choice exists. This strategy is symmetric and continues indefinitely, proving \(\mathrm{FO}^{k}\)-equivalence at every quantifier depth.

For \(k=2\), every vertex in every graph of the family has both a neighbor and a *distinct nonneighbor*: its opposite side has at least three vertices and at most one deleted incident edge, while its own side has at least three vertices. In the ordinary two-pebble game, the response to any move is therefore chosen to preserve equality, edge, or distinct nonedge relative to the one other pebble. This works forever. With one variable, the structures are all nonempty and loopless, so their one-variable sentences also agree.

**4. Counting theories and minimum representatives.** For \(k\ge3\), distinct invariant values occur in the following disjoint cases. When \(t=0\), the two clipped side sizes range over \(3,\ldots,k\), giving \(\binom{k-1}{2}\) unordered pairs. When \(t=1\), each clipped unmatched-side count ranges over \(2,\ldots,k\), giving \(\binom{k}{2}\). When \(t=2\), those counts range over \(1,\ldots,k\), giving \(\binom{k+1}{2}\). Finally, for each clipped \(t\) in \(3,\ldots,k\), both counts range over \(0,\ldots,k\), giving \((k-2)\binom{k+2}{2}\). Their sum is \(T_k\) above.

For \(t=0\), the minimum representative has side sizes \(\min(a,k),\min(b,k)\). For \(t>0\), set \(\tau=\min(t,k)\), \(\alpha=\min(a-t,k)\), and \(\beta=\min(b-t,k)\); the minimum representative is \(G(\tau+\alpha,\tau+\beta,\tau)\). It lies in the family because each side retains size at least three, and no graph with the same invariant can have fewer vertices. Uniqueness follows from the parameters up to side exchange.

For strictness, compare \(G(3,k+1,1)\) and \(G(3,k+2,1)\) for any \(k\ge3\). Their unmatched counts are \(\{2,k\}\) and \(\{2,k+1\}\), so they are equivalent at width \(k\) but not at width \(k+1\). The transition from two to three variables is strict as \(G(3,3,0)\) and \(G(3,3,1)\) illustrate.

## Verification
The independent structural checker tested the definability of \(S\) and \(D\) for all \(168\) parameter triples with \(3\le a\le b\le9\), checking \(28{,}854\) ordered vertex pairs and finding no mismatch. It also enumerated the canonical clipped parameter profiles for widths \(3\) through \(8\), reproducing the stated polynomial counts.

The finite logical-refinement checker computed fixed points of the non-counting \(k\)-tuple color-refinement operator over a simultaneous family of graph structures. For \(3\le a\le b\le6\) and every \(0\le t\le a\), it checked \(50\) graphs: at width two there was one theory, and at width three there were exactly \(20\) theories, with zero pair-classification disagreements. An additional width-four sample contained \(13\) graphs and yielded no disagreements. Source programs and exact recorded output are supplied with the result. These finite checks do not prove the arbitrary-size theorem, which follows from the definability and permanent pebble strategy above.

## Relationship to prior work
Grohe and Otto (2012) develop general counting-free finite-variable pebble equivalences, including Boolean-semiring formulations, but their relevant results do not present this three-parameter closed classification. The matching-deleted family has been studied in graph topology: Lv (2023), following earlier work of Mohar and others, investigates its nonorientable genus, not its finite-variable logical theories. Unnithan, Kannan and Jathavedan (2014) compute betweenness for the balanced perfect-matching-deletion crown subfamily. The full arbitrary-matching, unbalanced classification is not implied by those scalar invariants. Earlier logical classifications of crown graphs concern the proper subfamily \(a=b=t\), and do not imply the two independent unmatched-side parameters or the piecewise exact theory count established here.

The research comparison found no exact previously stated theorem, but this does not establish historical uniqueness: an unlocated general finite-model-theoretic composition or graph-decomposition result could imply it.

## Limitations
The statement does not cover side sizes below three, arbitrary deleted edge sets, vertex-coloured or side-named signatures, or logic with counting quantifiers. The computational verification checks only finite ranges. The mathematical argument is a self-review rather than independent validation. Historical originality has not been independently established.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first posted 2012-04-09); *Computer Science Logic* (2012), DOI: 10.4230/LIPIcs.CSL.2012.289. https://arxiv.org/abs/1204.1990
2. S. Lv, *Constructing nonorientable genus embedding of complete bipartite graph minus a matching*, arXiv:2305.10008 (2023). https://arxiv.org/abs/2305.10008
3. S. K. R. Unnithan, B. Kannan, and M. Jathavedan, *Betweenness Centrality in Some Classes of Graphs*, *International Journal of Combinatorics* (2014), DOI: 10.1155/2014/241723. https://doi.org/10.1155/2014/241723
