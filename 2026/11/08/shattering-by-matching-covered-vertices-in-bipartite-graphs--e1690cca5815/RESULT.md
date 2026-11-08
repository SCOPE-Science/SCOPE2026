# Shattering by matching-covered vertices in bipartite graphs

## Finding

Let \(G=(L\sqcup R,E)\) be any finite simple bipartite graph, including one with isolated vertices or no edges. For a matching \(M\) (including the empty matching), write \(V(M)\) for the vertices incident to its edges, and set \(\mathcal C(G)=\{V(M):M\text{ is a matching of }G\}\). Concepts are subsets of \(V(G)\), and a query at \(v\) reports whether \(v\in V(M)\).

**Exact shattering criterion.** A support \(S\subseteq V(G)\) is shattered by \(\mathcal C(G)\) if and only if the edge cut \(E(S,V(G)\setminus S)\) contains a matching saturating all of \(S\). Equivalently, both bipartite neighborhood inequalities hold:
\[
|N_G(A)\setminus (S\cap R)|\ge |A|\quad\text{for every }A\subseteq S\cap L,
\]
\[
|N_G(B)\setminus (S\cap L)|\ge |B|\quad\text{for every }B\subseteq S\cap R.
\]
Here \(N_G\) is open neighborhood. The two Hall systems are independent because the corresponding matching edge sets have disjoint endpoints. In particular, membership in the *entire shattering complex* is decidable by a single bipartite matching computation on the cut (or two Hall tests), without enumerating \(\mathcal C(G)\).

Writing \(\nu(G)\) for maximum matching cardinality, one obtains
\[
\operatorname{VCdim}(\mathcal C(G))=\nu(G).
\]
For \(G=K_{a,b}\), with \(a,b\ge0\), the complete shattered-support polynomial is
\[
\Phi_{K_{a,b}}(z)=\sum_{j=0}^{\min(a,b)}\binom{a+b}{j}z^j.
\]

**Nonpurity on connected paths.** For every integer \(t\ge1\), label the vertices of the path \(P_{5t+1}\) by \(0,1,\dots,5t\) in order. Then
\[
S_t=\{5j+2,5j+3:0\le j<t\}
\]
is an inclusion-maximal shattered support of size \(2t\), whereas the VC dimension of the same concept family is \(\lfloor(5t+1)/2\rfloor\). Thus the maximum and minimum cardinalities of maximal shattered supports differ by **at least** \(\lfloor(t+1)/2\rfloor\) on this family of connected trees. This is not a claim that \(2t\) is the smallest maximal-support size.

Bipartiteness is essential: for the triangle \(K_3\), the same matching-saturation concept family shatters two vertices, although \(\nu(K_3)=1\).

## Assumptions and scope

Graphs are finite, undirected and simple. Both matching and shattering use ordinary (not maximum-only or maximal-only) matchings, and the empty matching is allowed. The query domain is **vertices** of \(G\), rather than its edges. An isolated vertex cannot lie in a nonempty shattered support. Assertions about the VC dimension hold also for edgeless graphs, in which the dimension is zero. No statement about Littlestone dimension or a polynomial-size description of all maximal faces is made.

## Proof

**Criterion, necessity.** Suppose \(S\) is shattered. The prescribed labeling which is positive exactly on \(S\cap L\) has a matching witness \(M_L\); each vertex in \(S\cap L\) is covered and each vertex in \(S\cap R\) is uncovered. Therefore the edges of \(M_L\) incident to \(S\cap L\) match \(S\cap L\) injectively into \(R\setminus S\). Similarly the labeling positive exactly on \(S\cap R\) has a witness \(M_R\), giving a matching from \(S\cap R\) into \(L\setminus S\). The two selected submatchings are vertex-disjoint: one lies between \(S\cap L\) and \(R\setminus S\), the other between \(S\cap R\) and \(L\setminus S\). Their union is a matching whose every edge crosses the cut and which saturates \(S\). Hall's marriage theorem yields the equivalent pair of neighbor inequalities.

**Criterion, sufficiency.** Let \(Q\) be a crossing matching saturating \(S\). Each edge of \(Q\) has exactly one endpoint in \(S\), and no two share endpoints. For any labeling whose positive set is \(T\subseteq S\), retain exactly the edges of \(Q\) incident to \(T\). This submatching covers precisely \(T\) among the queried vertices, so all \(2^{|S|}\) labelings are realized, including the empty labeling.

**VC dimension.** Any shattered \(S\) is saturated by a matching with \(|S|\) edges, so \(|S|\le\nu(G)\). Conversely take any maximum matching \(Q\), and choose exactly one endpoint from each edge, forming a set \(S\) of size \(\nu(G)\). The matching \(Q\) crosses the cut \((S,V\setminus S)\), so \(S\) is shattered by the criterion. The empty graph case follows with \(Q=\varnothing\).

**Complete bipartite graph.** Let \(S_L=S\cap L\) and \(S_R=S\cap R\). A crossing matching exists precisely when \(|S_L|\le b-|S_R|\) and \(|S_R|\le a-|S_L|\); these inequalities are equivalent to \(|S|\le\min(a,b)\). All supports of each permissible size therefore occur, yielding the displayed polynomial by choosing \(j\) of the \(a+b\) vertices.

**An inclusion-maximal face on a path.** For each \(j\), match the selected vertex \(5j+2\) to \(5j+1\) and the selected vertex \(5j+3\) to \(5j+4\). These \(2t\) edges are disjoint, have one end in \(S_t\), and prove shattering. The crossing partners \(5j+1\) and \(5j+4\) are **forced**: \(5j+2\) has no other neighbor outside \(S_t\), nor does \(5j+3\). Hence adding either \(5j+1\) or \(5j+4\) removes the only available crossing partner of an existing selected vertex. Every remaining unselected vertex is a \(5j\), with \(0\le j\le t\). Its existing neighbors (one at each endpoint, two otherwise) are forced partners already used by the original selected vertices. Thus it cannot acquire a new distinct crossing partner without breaking saturation of an original selected vertex. No unselected vertex can be added. The maximum matching of a path on \(5t+1\) vertices has size \(\lfloor(5t+1)/2\rfloor\). Subtracting \(2t\) gives \(\lfloor(t+1)/2\rfloor\), which grows unboundedly.

**Triangle boundary.** For any two vertices \(u,v\) of \(K_3\), the empty matching, the edge from \(u\) to the third vertex, the edge from \(v\) to the third vertex, and the edge \(uv\) realize the patterns \(00,10,01,11\), respectively. The maximum matching size is only one.

## Verification

The accompanying standalone program `check_matching_saturation.py` uses two independent finite algorithms: exhaustive enumeration of graph matchings and their covered-vertex traces, and a separate backtracking test for a matching saturating a query support into its complement. It compared the methods on all labeled bipartite subgraphs of \(K_{1,1}\), \(K_{1,2}\), \(K_{2,2}\), \(K_{2,3}\), and \(K_{3,3}\), including edgeless cases. It also tested path dimensions through 17 vertices, the displayed path facets, complete-bipartite full skeletons, and the nonbipartite triangle boundary. Its recorded output was:

`MATCHING_SATURATION_SHATTERING_PASS 598 35112 16 3`

The numbers denote tested bipartite graphs, graph/support pairs, path lengths, and exhibited path facets. These exhaustive finite checks corroborate but do not replace the unrestricted proofs above. Reproduce with `python check_matching_saturation.py`.

## Relationship to prior work

Bucić, Devlin, Hendon, Horne, and Lund (2019, arXiv:1906.05908) study intersection frequencies and derangement ratios for **perfect matchings**; their main theorem concerns how many perfect matchings intersect a given perfect matching, not binary vertex-incidence traces of **all** matchings. Adler, Benediktsson, and Macpherson (2020, arXiv:2007.16042) develop VC dimensions for graph-neighborhood relations on Johnson and Hamming graphs; their theorem's concept class differs from the present matched-vertex family. Simon (2024, arXiv:2402.06729) studies ordered greedy matchings and teaching-related consistency graphs; his sample-assignment matching differs from the vertex set of a matching in the original graph. The present conclusion therefore is not inferred from matching-paper titles or from generic VC terminology. Hall's theorem itself is classical and is used, not claimed as new.

Koana and Wahlström (arXiv:2402.11596, §1.1) explicitly define the **matching delta-matroid**, whose feasible sets are precisely the vertex sets of matchings; this identification is established prior literature, not claimed new. Their paper analyzes linear delta-matroid representations and optimization, without stating the Hall-cut characterization of shattered supports or the path facet construction. The 2013 paper of Kozma and Moran on graph orientations and shattering establishes other links between graph properties and VC theory, but its orientation-concept setting is different. The possible existence of an equivalent older theorem in matching-system or transversal-matroid language is a genuine remaining priority risk.

## Limitations

The equivalence fails for nonbipartite graphs; the triangle already shows that the VC dimension can exceed the matching number. Matching *edge*-membership, maximum-only matchings, and online Littlestone dimension are different questions. The path construction provides a lower bound on the gap among facet cardinalities, not an exact classification of all facets. Full historical priority is not established by a negative bibliographic search. No independent mathematical audit has been performed.

## References

1. M. Bucić, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908, initially public 2019-06-13, https://arxiv.org/abs/1906.05908.
2. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, initially public 2020-07-31, https://arxiv.org/abs/2007.16042.
3. H. U. Simon, *Greedy Matchings in Bipartite Graphs with Ordered Vertex Sets*, arXiv:2402.06729, initially public 2024-02-09, https://arxiv.org/abs/2402.06729.
4. T. Koana, M. Wahlström, *Faster algorithms on linear delta-matroids*, arXiv:2402.11596, initially public 2024-02-18, https://arxiv.org/abs/2402.11596.
5. L. Kozma, S. Moran, *Shattering, Graph Orientations, and Connectivity*, Electron. J. Comb. 20(3), P44 (2013), https://doi.org/10.37236/3326.
