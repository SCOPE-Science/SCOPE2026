# Dual, outer, and total mutual-visibility chromatic numbers of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\) and \(n_i\ge1\). For the dual, outer, and total mutual-visibility chromatic numbers introduced in arXiv:2609.31427v1,
\[
\chi_{\mu_{\mathrm{o}}}(G)=
\begin{cases}
1,&n_1=\cdots=n_r=1,\\
2,&\text{otherwise,}
\end{cases}
\]
\[
\chi_{\mu_{\mathrm{d}}}(G)=
\begin{cases}
1,&n_1=\cdots=n_r=1,\\
\infty,&r=2,\ \min_i n_i=1,\ \max_i n_i\ge3,\\
2,&\text{otherwise,}
\end{cases}
\]
and
\[
\chi_{\mu_{\mathrm{t}}}(G)=
\begin{cases}
1,&n_1=\cdots=n_r=1,\\
\infty,&r=2,\ \min_i n_i=1,\ \max_i n_i\ge2,\\
2,&\text{otherwise.}
\end{cases}
\]
Thus the only infinite complete-multipartite cases are stars: for total mutual visibility every \(K_{1,n}\) with \(n\ge2\), and for dual mutual visibility exactly \(K_{1,n}\) with \(n\ge3\).

## Assumptions and scope
Graphs are finite, simple, connected, and nontrivial. For \(M\subseteq V(G)\), vertices \(x,y\) are \(M\)-visible when some shortest \(x,y\)-path has no internal vertex in \(M\). A dual mutual-visibility set requires this for pairs both in \(M\) and pairs both outside \(M\); an outer mutual-visibility set requires it for pairs both in \(M\) and pairs with exactly one endpoint in \(M\); a total mutual-visibility set requires it for every pair. A corresponding coloring partitions \(V(G)\) into sets of the indicated type, and its chromatic number is the least number of parts, with value \(\infty\) if no such partition exists.

## Proof
Write the parts as \(V_1,\ldots,V_r\). If \(x,y\) lie in different parts, then they are adjacent and hence \(M\)-visible for every \(M\). If distinct \(x,y\in V_i\), then their distance is two and every shortest path has form \(xzy\) with \(z\in V(G)\setminus V_i\). Consequently
\[
x,y\text{ are \(M\)-visible}\quad\Longleftrightarrow\quad V(G)\setminus(M\cup V_i)\ne\varnothing.
\]
This is the only geodesic fact needed.

For outer mutual visibility, if every part is a singleton then \(G\) is complete and one color suffices. Otherwise one color fails because two vertices in a non-singleton part have every shortest path internally blocked when \(M=V(G)\). For two colors, take \(V_1\) and \(V(G)\setminus V_1\). Same-part pairs in either class use a vertex of the other class as the unblocked internal vertex, and every mixed-class pair relevant to the outer condition is adjacent. Thus the outer formula holds.

For total mutual visibility, suppose \(r\ge3\). Again use the classes \(V_1\) and \(V(G)\setminus V_1\). For \(M=V_1\), a pair in \(V_1\) uses a vertex outside \(V_1\), while a pair in \(V_j\), \(j\ne1\), uses a vertex in a third part \(V_k\), \(k\notin\{1,j\}\), outside \(M\). For \(M=V(G)\setminus V_1\), any same-part pair outside \(V_1\) uses a vertex of \(V_1\), and a pair in \(V_1\) uses any vertex outside it. Hence both classes are total mutual-visibility sets.

If \(r=2\) and both parts have size at least two, split each part into two nonempty pieces and let each color meet both parts. The complement of either color also meets both parts, so every same-part pair has an unblocked internal vertex in the other part. Thus two colors suffice.

It remains to consider \(K_{1,n}\) with \(n\ge2\). Let \(c\) be its center. Any color class \(M\) containing \(c\) fails to be total: two leaves have the unique shortest path through \(c\in M\). Therefore no total coloring exists, proving the total formula.

Every total mutual-visibility set is dual, so the preceding finite constructions also give dual two-colorings. The additional case \(K_{1,2}\) has a dual two-coloring: if its center is \(c\) and its leaves are \(u,v\), then \(\{c,u\}\) and \(\{v\}\) are dual mutual-visibility sets. Finally, if \(G=K_{1,n}\) with \(n\ge3\) and a dual mutual-visibility set \(M\) contains \(c\), then at least two leaves lie on the same side of the partition \(M,V(G)\setminus M\). Two leaves in \(M\) violate visibility inside \(M\), while two leaves outside \(M\) violate the outside-pair requirement; in either case their unique shortest path is blocked by \(c\in M\). Hence no dual set contains \(c\), so no dual coloring exists. The dual formula follows.

## Verification
A standalone verifier reconstructs every complete-multipartite isomorphism type with at least two parts through order \(9\). For every nonempty vertex subset \(M\), it checks visibility directly by breadth-first search, comparing unrestricted shortest-path distance with the shortest distance when vertices of \(M\) are forbidden as internal vertices. It then computes the minimum partition into valid dual, outer, or total sets by exact bitmask dynamic programming.

Across all \(87\) complete-multipartite types through order \(9\), it checks \(261\) graph/invariant cases and agrees with the formulas. Its deterministic output is `ALL CHECKS PASSED; multipartite_types=87; invariant_cases=261; max_order=9`. This is a finite stress test only; the universal theorem is established by the proof above.

## Relationship to prior work
Babu, Jakovac, Kuziak, Lakshmanan S., and Yero introduce the dual, outer, and total mutual-visibility chromatic numbers in arXiv:2609.31427v1, first submitted September 25, 2026. Their exact-family results concern block graphs, Hamming graphs, and strong grids. Their Theorem 3 characterizes infinite total coloring via centers of convex \(P_3\), and their Theorem 4 gives sufficient convex-\(P_5\)/convex-\(K_{1,3}\) obstructions for infinite dual coloring while noting that the full general dual characterization remains open. The inspected full text contains no occurrence of “multipartite”.

The present theorem is not just an infinitude specialization: it determines every finite value, supplies the two-color constructions, distinguishes \(K_{1,2}\) sharply between the dual and total variants, and determines the outer invariant on the whole family. Targeted semantic-index and web searches using the exact invariant names together with complete-multipartite and complete-bipartite aliases found no prior statement implying these three formulas. The closest complete-multipartite records concern different invariants, including dual general-position sets and outer multiset dimension.

## Limitations
The proof is specific to complete multipartite graphs and uses their diameter-two geodesic structure. It does not settle the general characterization of graphs with infinite dual mutual-visibility chromatic number. An older equivalent family statement under substantially different terminology remains a residual literature risk, although these three chromatic variants themselves were introduced in the 2026 source paper.

## References
1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., and I. G. Yero, “A variety of the mutual-visibility coloring problem for graphs,” arXiv:2609.31427v1, first submitted September 25, 2026.
