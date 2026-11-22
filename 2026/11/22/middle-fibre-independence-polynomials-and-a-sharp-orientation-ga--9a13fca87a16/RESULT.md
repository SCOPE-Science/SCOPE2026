# Middle-fibre independence polynomials and a sharp orientation gap for three-level targets

## Finding
Let \(D=(V,A)\) be any finite loopless digraph obtained by orienting each edge of a simple graph \(G\), with no pairs of oppositely directed arcs. For positive integers \(p,q,r\), let \(T_{p,q,r}\) have three independent vertex levels of respective sizes \(p,q,r\), with every arc directed from a lower to a higher level. The middle-level homomorphism polynomial and all unweighted homomorphism counts admit an exact reduction to a single independence polynomial on a canonically determined induced subgraph.

Define \(M\) to be the vertices of \(D\) having both an in-neighbour and an out-neighbour; let \(I_0\) be its isolated vertices. When \(M\) is independent in \(G\), set \(R=G[V\setminus(I_0\cup N_G[M])]\), where \(N_G[M]\) denotes the closed neighbourhood. Let \(P\) and \(Q\) be, respectively, the nonisolated vertices having only outgoing or only incoming arcs. Then
\[
\#\operatorname{Hom}(D,T_{p,q,r})=(p+q+r)^{|I_0|}q^{|M|}
\sum_{\substack{S\subseteq V(R)\\ S\,\mathrm{independent}}}
q^{|S|}p^{|P\setminus S|}r^{|Q\setminus S|}.
\]
If \(M\) is not independent, this count is zero. In particular, for the strict three-vertex transitive tournament \(T_3=T_{1,1,1}\), weighting each occurrence of the middle vertex by \(z\) gives
\[
Z_D(z)=\sum_{h:D\to T_3}z^{|h^{-1}(2)|}
=(2+z)^{|I_0|}z^{|M|}I_R(z),
\]
with \(I_R(z)=\sum_{S\subseteq V(R),\ S\text{ independent}}z^{|S|}\). The formula is zero if \(M\) is not independent.

This identity yields a sharp stability result: for any connected bipartite graph \(G\) with at least one edge, exactly the two orientations from one bipartition class to the other maximize the number of maps to \(T_3\). The maximum is \(I_G(1)\). Every other orientation admits at most \(I_G(1)/2\) such maps; this bound is strict for each fixed finite connected graph and the factor \(1/2\) is best possible uniformly, even among trees.

For orientations of the \(n\)-vertex path (\(n\ge2\)), exactly \(2F_n\) of the \(2^{n-1}\) orientations admit a homomorphism to \(T_3\), where \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\); the sum of homomorphism counts over every orientation is \(3\cdot2^{n-1}\).

## Assumptions and scope
All vertex and arc sets are finite. A graph orientation assigns exactly one direction to each edge, without loops or parallel/opposite arcs. Homomorphisms preserve each directed arc but not non-arcs. Levels of \(T_{p,q,r}\) have no internal arcs. Isolated vertices of \(D\) are allowed and each may map anywhere. The set \(M\) comprises mixed vertices; \(P\), \(Q\), and \(I_0\) are pairwise disjoint and partition \(V\) together with \(M\). The notation \(N_G[M]\) refers to all vertices of \(M\) and all their neighbours in \(G\). The induced graph \(R\) contains only nonisolated pure vertices outside this closed neighbourhood. An empty induced graph has independence polynomial \(1\).

## Proof
First, consider a directed arc \(u\to v\). A homomorphism to \(T_{p,q,r}\) places the source in a strictly lower level than its target. Therefore any vertex with both an incoming and an outgoing arc must occupy the middle level. Two such mixed vertices cannot be adjacent: an arc between them would require two different levels. Thus if \(G[M]\) has an edge no homomorphism exists.

Suppose \(M\) is independent. A vertex outside \(M\) that is nonisolated is either a pure source or a pure sink. If adjacent to a mixed vertex, it is necessarily a source entering that mixed vertex or a sink receiving an arc from it, so its level is forced to be, respectively, bottom or top. All remaining nonisolated vertices form \(R\). Their neighbours within \(R\) are necessarily source–sink pairs with arcs directed from the source to the sink. The set of vertices of \(R\) mapped to the middle level must be independent: adjacent middle-level vertices would violate strict increase. Conversely, any independent set \(S\subseteq V(R)\) can be mapped to the middle level, with all other pure sources mapped to the bottom level, all other pure sinks to the top level, and all mixed vertices to the middle level. Every arc then strictly increases its level. These are precisely all possible assignments of levels; the choices of individual vertices in levels contribute \(q^{|M|+|S|}p^{|P\setminus S|}r^{|Q\setminus S|}\), and isolates contribute \((p+q+r)^{|I_0|}\). Summing over independent sets proves the first identity and, on substituting \(p=q=r=1\) with a middle-level weight \(z\), the polynomial identity.

For stability, take a connected bipartite \(G\) with at least one edge. When no mixed vertex exists, each vertex is a pure source or a pure sink; adjacency then forces opposite roles. Connectivity leaves exactly the two consistently oriented bipartitions. For either, \(R=G\), and the number of maps to \(T_3\) is \(I_G(1)\). For any other orientation, \(M\ne\varnothing\). If \(M\) is not independent the count is zero. Otherwise, \(R=G-N_G[M]\), since the graph has no isolates. Every independent set of \(R\), together with any subset of \(M\), is an independent set of \(G\): these \(2^{|M|}I_R(1)\) sets are distinct. Hence \(I_R(1)\le2^{-|M|}I_G(1)\le I_G(1)/2\). The first inequality is strict in a connected nontrivial graph because a neighbour of a mixed vertex gives a singleton independent set not counted by the displayed injection. Consequently only the two source–sink orientations maximize, and every other orientation lies strictly below half.

To show that the constant cannot be lowered, consider a tree with vertices \(a,m,b\), edges \(a-m\) and \(m-b\), and \(N\) pendant leaves attached independently to each of \(a\) and \(b\). Direct the edges \(a\to m\to b\), direct edges from \(a\) to its leaves, and direct edges from the leaves attached to \(b\) into \(b\). Then \(M=\{m\}\), and \(R\) consists of \(2N\) isolated leaves, so \(\#\operatorname{Hom}(D,T_3)=2^{2N}\). Separating independent sets by whether they contain \(m\) gives \(I_G(1)=2^{2N}+(2^N+1)^2\). Their ratio tends to \(1/2\) as \(N\to\infty\), proving sharpness.

For the path \(P_n\), encode its successive edge orientations by a binary word of length \(n-1\). A non-endpoint vertex is mixed exactly when the two adjacent signs agree. Two adjacent mixed vertices therefore occur exactly at a run of three equal signs. The first identity shows existence of a map to \(T_3\) exactly when such a run is absent. Let \(a_m\) count binary words of length \(m\) with no three consecutive equal symbols. For \(m\ge3\), sorting by the last run length one or two gives \(a_m=a_{m-1}+a_{m-2}\), with \(a_1=2,a_2=4\). Hence \(a_{n-1}=2F_n\). Finally, every proper three-colouring of the undirected path determines exactly one orientation by directing each edge from its lower to its higher colour, and each map into \(T_3\) comes from such a colouring. There are \(3\cdot2^{n-1}\) proper three-colourings, proving the last formula.

## Verification
The accompanying self-contained \(\texttt{verify.py}\) enumerates all orientations or missing-edge configurations on up to four vertices with three distinct target level-size choices and compares the exact homomorphism count against the independence-set formula. It also tests deterministic random configurations up to eight vertices, compares coefficients of the middle-fibre polynomial on smaller configurations, and verifies the Fibonacci path count through fourteen vertices. Running \(\texttt{python3 verify.py}\) prints \(\texttt{VERIFY_OK 3473}\). The numerical tests support but do not replace the proof for arbitrarily large graphs.

## Relationship to prior work
Meyer–Starke study existential constraint satisfaction and Datalog definability for transitive tournaments, whereas the new invariant counts all solutions and separates middle-fibre sizes. Das–Ghosh–Prabhu–Sen construct a homomorphic polynomial for oriented graphs with tournament targets and give small oriented-path examples; no exact canonical closed-neighbourhood independence reduction or sharp half-gap for these targets was identified in the inspected sections. The classical Gallai–Hasse–Roy–Vitaver theorem already characterizes the existence of maps to transitive tournaments via directed path obstructions; no novelty is claimed for mere existence or for the general notion of an independence polynomial. Previous work on orientations and linear extensions counts a different statistic. The novelty claim is limited to the exact weighted reduction and its sharp orientation-stability consequence.

## Limitations
This theorem does not address general digraphs with directed two-cycles, arbitrary target tournaments, or templates containing within-level arcs. The path count is a corollary of the exact polynomial, not an independent new logical classification. Historical priority is provisional: exact #CSP reductions for the three-vertex transitive tournament may occur in earlier literature under different terminology. Neither an independent proof audit nor a comprehensive historical-priority certification has been performed.

## References
1. Sebastian Meyer and Florian Starke, *Almost Symmetric Linear Arc Monadic Datalog and Transitive Tournaments*, arXiv:2606.24711, first submitted 23 June 2026. https://arxiv.org/abs/2606.24711
2. Sandip Das, Sumitava Ghosh, Swathy Prabhu, and Sagnik Sen, *A homomorphic polynomial for oriented graphs*, 2023. https://arxiv.org/search/?query=A+homomorphic+polynomial+for+oriented+graphs&searchtype=title
3. *Gallai–Hasse–Roy–Vitaver theorem*, classical homomorphism/longest-directed-path characterization. https://en.wikipedia.org/wiki/Gallai%E2%80%93Hasse%E2%80%93Roy%E2%80%93Vitaver_theorem
4. J. Iriarte, *Graph Orientations and Linear Extensions*, 2013/2017. https://dmtcs.episciences.org/en/articles/2455
