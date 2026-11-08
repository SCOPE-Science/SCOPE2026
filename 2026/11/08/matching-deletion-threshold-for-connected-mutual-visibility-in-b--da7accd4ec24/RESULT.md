# Matching-deletion threshold for connected mutual visibility in balanced bicliques

## Finding
Let \(n\ge4\) and \(0\le t\le n\) be integers. Form \(G_{n,t}\) by deleting \(t\) pairwise disjoint edges from the complete bipartite graph \(K_{n,n}\). Write its labelled shores as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with exactly the edges \(a_i b_i\) for \(1\le i\le t\) deleted. A *connected mutual-visibility set* is a nonempty vertex subset whose induced graph is connected and for which each selected vertex pair has an ambient shortest path with no other selected vertex internally. Let \(\mu_c(G_{n,t})\) be its maximum size, and \(M_{n,t}\) the number of labelled maximizing subsets.

**Theorem (matching-deletion phase and extremal rigidity).** For all \(n\ge4\),
\[
\boxed{\mu_c(G_{n,t})=\begin{cases}2n-2,&0\le t<n,\\2n-3,&t=n,\end{cases}}
\]
and
\[
\boxed{M_{n,t}=\begin{cases}
n^2,&t=0,\\
(n-1)^2+1,&t=1,\\
(n-t)^2,&2\le t<n,\\
2n(n-1),&t=n.
\end{cases}}
\]

More precisely, for \(t<n\) all maximum sets are exactly the complements of \(\{a_i,b_j\}\) with \(i,j>t\), together with **one additional set when \(t=1\)**, namely the complement of \(\{a_1,b_1\}\). For \(t=n\), all maximum sets are exactly the complements of \(\{a_i,b_i,b_j\}\) and of \(\{b_i,a_i,a_j\}\), over ordered choices \(i\ne j\). There are no other maximum sets.

In particular, deleting any proper submatching preserves the maximum cardinality \(2n-2\), but the number of maximizers decreases from \(n^2\) to a **unique** one at \(t=n-1\); deleting the last surviving matching edge then drops the maximum cardinality by one and creates \(2n(n-1)\) new maximizers. The exceptional extra maximizer at \(t=1\) is not part of the generic quadratic progression.

## Assumptions and scope
All graphs are finite, simple, undirected, and the endpoints of the deleted edges are labelled as above. The parameter \(t\) is the cardinality of a matching, not the number of arbitrary deleted edges. A singleton is connected and mutually visible; the empty set is excluded. Geodesics are measured in the full graph, not merely in the induced selected graph. Maximizer counts distinguish labelled vertex subsets and do not identify sets under graph automorphisms. The restriction \(n\ge4\) is essential for the uniform formulas: the six-cycle at \(n=3,t=3\), for example, is exceptional.

## Proof
Write \(S\) for a connected mutual-visibility set and let \(P=\{i:a_i\notin S\}\), \(Q=\{j:b_j\notin S\}\). We use two elementary geodesic facts.

First, if at least two \(a\)-vertices are selected, then some \(b\)-vertex must be unselected, since distinct \(a\)-vertices have distance two and every geodesic between them has an internal \(b\)-vertex; the symmetric fact holds on the other shore. Second, suppose exactly one vertex is omitted from each shore, say \(P=\{i\}\), \(Q=\{j\}\). At least \(n-1\ge3\) vertices remain on each shore. The only possible external internal vertex for an ambient geodesic between two selected \(a\)-vertices is \(b_j\). It works for *all* selected \(a\)-pairs exactly when \(b_j\) is adjacent to *every* selected \(a\)-vertex. In \(G_{n,t}\), that happens precisely when \(j>t\) or \(i=j\). Symmetrically, all selected \(b\)-pairs have an external two-edge geodesic exactly when \(i>t\) or \(i=j\). These two necessary conditions therefore restrict all feasible two-omission sets to either \(i,j>t\) or \(i=j\le t\).

**Proper submatchings.** Suppose \(0\le t<n\). If fewer than two vertices are omitted, one shore is fully selected and at least \(n-1\) vertices are selected on the other, contradicting the first geodesic fact. Hence \(|S|\le2n-2\). Choose omitted vertices \(a_i,b_j\) with \(i,j>t\), which is possible because \(t<n\). Each omitted vertex is adjacent to every selected vertex on the opposite shore, and so supplies the required length-two geodesics for same-shore pairs. Any selected deleted-matching nonedge \(a_k,b_k\), necessarily with \(k\le t\), has distance three and the external geodesic \(a_k,b_j,a_i,b_k\): all three edges are present because \(i,j>t\). Adjacent pairs need no internal vertices. The induced selected graph \(K_{n-1,n-1}\) with at most \(t\) disjoint edges deleted is connected for \(n-1\ge3\). Thus all \((n-t)^2\) such sets attain \(2n-2\).

For completeness, consider the remaining two-omission possibility \(i=j\le t\). If \(t=1\), omitting \(a_1,b_1\) removes the only missing edge's endpoints: the selected graph is \(K_{n-1,n-1}\); the omitted vertices supply all same-shore geodesics, so this is one additional maximum set. If \(t\ge2\), choose any \(k\le t\) with \(k\ne i\). Both \(a_k\) and \(b_k\) are selected, but their connecting edge has been deleted. Their ambient distance is three. The only two omitted vertices are \(b_i,a_i\), and these cannot be successive internal vertices of a geodesic because the edge \(a_i b_i\) has itself been deleted. Thus this configuration is not mutually visible. The preceding necessary condition now proves completeness and the first three multiplicity formulas.

**Full matching deletion.** Now let \(t=n\), so \(G_{n,n}\) is the crown graph. Again, fewer than two omissions are impossible. With exactly two omissions, one must be on each shore, say \(a_i,b_j\). The same-shore necessity forces \(i=j\). But as \(n\ge4\), there remains a selected matched nonedge \(a_k,b_k\) with \(k\ne i\). Its ambient distance is three, and the only possible omitted internal vertices are \(a_i,b_i\), which are not adjacent. Hence \(|S|\le2n-3\).

If three vertices are omitted, the two-shore geodesic fact forces at least one omission on each shore. Up to interchanging shores, omissions are \(P=\{i\}\) and \(Q=\{j,k\}\). The selected \(a\)-shore has size \(n-1\ge3\), so each pair must share an omitted \(b\)-neighbor: this happens precisely when \(i\in Q\). Thus the only candidates are \(P=\{i\}\), \(Q=\{i,j\}\), with \(j\ne i\), or the reversed pattern. Conversely, every such set is feasible: same-shore selected pairs use an omitted opposite-shore vertex adjacent to both endpoints; any selected matched nonedge \(a_k,b_k\), where \(k\notin\{i,j\}\), has the external length-three geodesic \(a_k,b_j,a_i,b_k\). The induced graph has shores of sizes \(n-1\) and \(n-2\), and deletes only matching edges, hence it is connected for \(n\ge4\) (the smaller shore still has at least two vertices, and the larger shore at least three). This exhausts all maximizing sets. The two complement types are disjoint, and each has \(n(n-1)\) members, proving the final formula.

## Verification
The accompanying `verify.py` uses the unmodified graph adjacency relation to enumerate connected mutual-visibility sets and test the theorem without using its proof conditions: it computes distances by breadth-first search, checks connectivity of the induced selected graph, and separately checks for an ambient geodesic that avoids other selected vertices. For every \(4\le n\le7\) and every \(0\le t\le n\), it exhaustively checks all nonempty subsets and compares the *entire set* of maximum configurations to the formula. For \(n=8\), it checks all candidate sizes at or above the asserted optimum against the exact predicted family. All tests finish with `VERIFY_OK`. The unbounded conclusions follow from the proof, not the finite census.

## Relationship to prior work
Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs* (arXiv:2609.18877, 2026), introduce the connectivity requirement and determine general bounds and complete bipartite cases, but not the matching-deletion phase. Bujtás, Klavžar and Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets* (arXiv:2412.03066), study ordinary mutual visibility and its counting polynomial. Fresán-Figueroa, Goldfeder and Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets* (arXiv:2610.24324), give exact ordinary visibility configurations for undeleted complete bipartite graphs. Moreover, OEIS A004280 records the **ordinary** crown-graph maximum, and OEIS A390404 (with Andrew Howroyd's 2026 derivation) already gives the **entire ordinary visibility polynomial and set classification for full crowns**. Neither the undeleted endpoint nor that full-crown ordinary result is claimed independently as new here. The result's focus is the exact **connected** extremal phase for every intermediate proper matching deletion, especially its unique-maximizer boundary and the exceptional one-edge pattern. The full-matching endpoint is included only to make that phase transition precise.

The prior ordinary full-crown classification can imply part of the full-deletion boundary after a separate connectivity test; it does not determine the proper-deletion regime. Likewise, previously published results on geodesic-subpath counts of matching-deleted bicliques concern a different invariant and do not determine connected mutual visibility. The claimed priority of the intermediate-deletion phase remains provisional.

## Limitations
The theorem is restricted to balanced complete bipartite graphs of shore size at least four and deletion of a matching. It makes no claim about arbitrary edge deletions, unequal shores, the complete all-size visibility polynomial, or smallest exceptional shores. The ordinary full-crown maximum and polynomial are prior results. Independent historical and mathematical assessment has not been performed.

## References
- Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877, first public 2026-09-16. https://arxiv.org/abs/2609.18877
- Csilla Bujtás, Sandi Klavžar and Jing Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, first public 2024-12-04. https://arxiv.org/abs/2412.03066
- Julián A. Fresán-Figueroa, Ilán A. Goldfeder and Aldo Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets*, arXiv:2610.24324, first public 2026-10-16. https://arxiv.org/abs/2610.24324
- OEIS A004280, ordinary mutual-visibility maximum of crown graphs. https://oeis.org/A004280
- OEIS A390404 and Andrew Howroyd, *Visibility polynomial of the n-crown graph* (January 2026), full ordinary polynomial and seven-case classification. https://oeis.org/A390404/a390404.txt
