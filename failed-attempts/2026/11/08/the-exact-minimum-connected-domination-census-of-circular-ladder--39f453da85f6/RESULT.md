# The exact minimum connected-domination census of circular ladders

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the ordinary prism graph (circular ladder) on the labeled vertices \((i,\ell)\), with \(i\in\mathbb Z/n\mathbb Z\), \(\ell\in\{0,1\}\). A *connected dominating set* is a nonempty set \(S\) such that every outside vertex has a neighbor in \(S\) and \(G_n[S]\) is connected. Let \(\gamma_c(G_n)\) be its minimum cardinality. Define the refined minimum-set polynomial
\[
Q_n(u)=\sum_{\substack{S\subseteq V(G_n)\\S\text{ connected dominating},\ |S|=\gamma_c(G_n)}}u^{d(S)},
\qquad d(S)=|\{i:(i,0),(i,1)\in S\}|.
\]
Then, for every permitted integer \(n\),
\[
\gamma_c(G_n)=\begin{cases}2,&n=3,\\ n,&n\ge4,\end{cases}
\qquad
Q_n(u)=\begin{cases}
3u,&n=3,\\
2+24u+4u^2,&n=4,\\
2+2n(n-1)u+2nu^2,&n\ge5.
\end{cases}
\]
In particular, for \(n\ge5\), there are exactly \(2n^2+2\) minimum connected dominating sets: exactly two induce cycles and exactly \(2n^2\) induce trees. When \(n=4\), 24 of the 30 minimum sets induce trees and six induce cycles; when \(n=3\), all three minimum sets are edges.

## Assumptions and scope
All graphs are finite, simple, and undirected. The cycle has its usual edges between consecutive indices modulo \(n\), and each pair \((i,0),(i,1)\) is joined by a rung. Vertices and columns are labeled; a vertex subset is counted once, not modulo automorphisms. This theorem enumerates *minimum-cardinality connected dominating sets*, not all inclusion-minimal connected dominating sets and not all ordinary dominating sets. A column is called *empty*, *single*, or *double* according as it contains zero, one, or two selected vertices. Let \(z\) and \(d\) denote the numbers of empty and double columns, respectively. Since there are \(n\) columns,
\[
|S|=n+d-z.
\]

## Proof
**1. Projection, empty-column bound, and minimum size.** For a nonempty connected induced subgraph, its set of occupied column indices is connected in the base cycle. When at least one column is empty, its occupied columns form one interval of the cycle; therefore the empty columns form one complementary consecutive interval. Since an empty column has no selected vertical neighbor, an interior column in a block of three empty columns could not be dominated. Hence \(z\le2\). If \(z=1\) and \(d=0\), there is precisely one selected vertex per occupied column and no rung in the selected induced graph. Connectivity makes all selected vertices lie in the same row; the omitted-row vertex of the single empty column has no selected neighbor. Thus \(z=1\) requires \(d\ge1\). If \(z=2\), the empty columns are consecutive. Each of their two layers must be dominated from the occupied column immediately outside the empty block on its side, forcing both boundary occupied columns to be double; thus \(d\ge2\). When \(n=4\) the two boundary columns are distinct, as are they for all \(n\ge4\). With \(z=0\) we have \(d\ge0\). It follows that every connected dominating set for \(n\ge4\) has \(|S|=n+d-z\ge n\). Either complete row forms a connected dominating set of cardinality \(n\), proving \(\gamma_c(G_n)=n\) for \(n\ge4\).

**2. Classification of equality.** For minimum sets with \(n\ge4\), equality forces \(d=z\). There are just three disjoint cases.

* **No empty column, no double column:** Every column contains exactly one selected vertex. Because no selected rung can join rows, connectivity requires the chosen vertex to remain in one fixed layer all around the cycle. The two complete rows yield the coefficient \(2\).
* **One empty and one double column:** Choose the empty column in \(n\) ways. The remaining \(n-1\) columns form an ordered path, and its unique double column can occupy any of \(n-1\) positions. On each side of the double column, selected singleton vertices must remain in one fixed row for connectivity. If the double column lies strictly inside the path, the two singleton-row choices must be opposite: otherwise the empty column has an undominated vertex in the other row. This leaves exactly two choices. When the double column is at a path endpoint, its adjacency to the empty column dominates both vertices there, while the singleton chain on the other side can use either row; again exactly two choices. Conversely all these assignments are connected, dominate the empty column, and dominate the omitted vertex in every single column via its rung. Hence there are exactly \(2n(n-1)\) distinct sets with one double column.
* **Two consecutive empty columns and two double columns:** The double columns are forced to be the two boundary occupied columns. The \(n-2\) occupied columns form a path with double endpoints and \(n-4\) singleton interior columns. To keep the selected induced graph connected, all interior singletons (when any exist) must have the same row. For \(n\ge5\) there are two choices per location of the empty block, yielding \(2n\) distinct sets. For \(n=4\) there is no interior singleton, and just one set per empty block, yielding four sets. Every described set is connected and dominating: the double endpoints dominate both neighboring empty columns, and singletons have selected rung neighbors. No other cases can occur because \(z\le2\) and \(d=z\).

Combining the cases proves all coefficients of \(Q_n(u)\) for \(n\ge4\). For \(n\ge5\) the one-double and two-double cases have no induced cycle (their occupied columns form paths, with respectively one selected rung or two nonadjacent selected rungs), so they induce trees. The two full rows induce cycles. For \(n=4\), the two-double case comprises four squares and the two full rows also induce cycles; the other 24 sets induce trees.

**3. Triangular-prism boundary.** When \(n=3\), no singleton dominates \(G_3\). Each rung-edge pair dominates all six vertices and is connected. A pair within one cycle fails to dominate the vertex in the opposite layer over the remaining column. Since all edges of the prism are rungs or same-row cycle edges, its only connected dominating pairs are its three rungs. Thus \(\gamma_c(G_3)=2\) and \(Q_3(u)=3u\), completing the proof.

## Verification
The standalone Python 3 program `verify_prism_cds.py` constructs adjacency lists directly from the graph definition. It exhaustively checks all nonempty vertex subsets for \(3\le n\le10\), compares the complete minimum-set family against separately constructed representatives of the three structural types, and checks the number of double columns. It also checks every constructed minimum set for \(11\le n\le40\). Execution result:

```
VERIFY_OK exhaustive_orders=3..10 nonempty_subsets=1398072 connected_dominating_subsets=81456 explicit_sets_orders=11..40 43570 minimum_set_profiles=PASS disjoint_construction=PASS
```

To reproduce, run `python3 verify_prism_cds.py` with Python 3.10 or later; no external packages are required. Finite checks are corroboration, not an infinite certificate. The unrestricted statement follows from the preceding projection and case analysis.

## Relationship to prior work
Abu-Khzam, Fernau, Gras, Liedloff, and Mann's 2022 work introduces general algorithms and bounds for enumerating inclusion-minimal connected dominating sets. It does not give this exact labeled minimum-set classification on circular ladders. The connected domination number of prisms is a known scalar invariant; the present enumeration is not a claim of discovering that scalar value. The 2023/2024 prism domination literature and Allagan and collaborators' 2026 *Exact Dominion of the Prism Graph* treat *ordinary* (not connected) minimum domination on the same graph, which imposes different constraints, gives a different optimum, and does not imply the counts above. The number \(2n^2+2\) occurs as a familiar quadratic integer sequence in other contexts; the claim is its graph-theoretic classification here, not the numerical sequence's first appearance. Related public work on circular-ladder cut-complex topology concerns other invariants.

## Limitations
Only minimum connected dominating sets are classified; there is no assertion about the full inclusion-minimal connected-dominating-set polynomial, weighted domination variants, larger cylinders, or uniqueness of published priority. No independent mathematical audit has been performed. General graph enumeration packages can compute finitely many instances; a finite database does not by itself establish or refute the uniform formula. An unindexed prior exact enumeration may exist.

## References
1. F. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Connected Dominating Sets*, arXiv:2205.00086, first posted 2022-04-29, https://arxiv.org/abs/2205.00086; conference version *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI 10.4230/LIPIcs.ESA.2022.1.
2. *Minimum Dominating Set for the Prism Graph Family*, 2023, DOI 10.5206/mase/15775.
3. *Dominance Parameters in Prism Graphs: A Comparative Study of Minimum Dominating Sets*, 2024, DOI 10.18280/mmep.110112.
4. J. Allagan and collaborators, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488, first posted 2026-01-07; DOI 10.1155/ijmm/1411005.
5. Wolfram MathWorld, *Connected Domination Number*, https://mathworld.wolfram.com/ConnectedDominationNumber.html.
