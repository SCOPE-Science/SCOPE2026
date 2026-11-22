# Cycle-root attachments control the fragmentation variance of unicyclic habitats

## Finding

Let \(G\) be any finite connected simple undirected unicyclic graph with \(n\geq3\) habitat patches, unique cycle \(C\) of length \(\ell\), and degrees \(d_v\). Retain vertices independently with probability \(0<p<1\); let \(K\) be the number of components of the surviving induced graph, including \(K=0\) if all vertices are lost. Define
\[
W=\sum_{v\in V(G)}\binom{d_v}{2},\qquad h=\sum_{v\in C}(d_v-2).
\]
Thus \(h\) is exactly the number of edges by which off-cycle branches attach to the unique cycle (counted at cycle endpoints). Then
\[
\mathbb E K=n(p-p^2)+p^\ell,
\]
\[
\operatorname{Var}K=n(p-4p^2+4p^3-p^4)+2W p^3(1-p)
+p^\ell(1-p^\ell)-2(\ell+h)p^{\ell+1}(1-p).
\]
In particular, for any two such graphs \(G,H\) having equal vertex number, degree multiset and cycle length, their means agree for all \(p\), whereas
\[
\operatorname{Var}K_G-\operatorname{Var}K_H
=-2(h_G-h_H)p^{\ell+1}(1-p).
\]
Therefore the graph with fewer off-cycle edges incident to the unique cycle has strictly larger fragmentation-count variance at **every** intermediate survival probability, regardless of the arrangements farther out on branches.

Six patches are the minimum graph order at which the cycle-root attachment count can differ between unicyclic graphs with the same degree multiset and cycle length. An explicit sharp pair consists of the edge sets
\[
E(G)=\{01,02,03,34,35,45\},\qquad
E(H)=\{02,12,13,14,24,35\},
\]
where \(ij\) denotes the edge between vertices \(i\) and \(j\). Both have degree multiset \((1,1,2,2,3,3)\) and a triangle; their attachment counts are \(h_G=1\), \(h_H=2\). Consequently
\[
\operatorname{Var}K_G-\operatorname{Var}K_H=2p^4(1-p)>0,
\]
which equals \(1/16\) when \(p=1/2\).

## Assumptions and scope

The host network is a fixed connected unicyclic simple graph, not a stochastic random-graph ensemble. All patches survive independently with the **same** probability \(p\). Connectivity is measured by the number of components of the retained induced graph; isolated surviving vertices count as components, and the empty graph contributes zero. The formulas hold exactly for all \(n\ge3\), all cycle lengths \(3\le\ell\le n\), and all real \(0\le p\le1\), with strict inequalities only for \(0<p<1\). The pairwise comparison requires matched degree multisets **and** matched cycle lengths.

The ecological interpretation is a snapshot fragmentation statistic, not colonization–extinction dynamics, metapopulation persistence, or a prescription for selecting conservation corridors.

## Proof

Write \(X_v\in\{0,1\}\) for independent vertex-survival indicators, \(S=\sum_vX_v\), \(E=\sum_{uv\in E(G)}X_uX_v\), and \(Z=\prod_{v\in C}X_v\). Every induced subgraph of a unicyclic graph has a cycle exactly when all vertices of its unique cycle survive. The graph-theoretic identity components = vertices − edges + cycle rank therefore gives the **outcome-wise identity**
\[
K=S-E+Z.
\]
There are exactly \(n\) edges. Hence \(\mathbb ES=np\), \(\mathbb EE=np^2\), and \(\mathbb EZ=p^\ell\), proving the mean formula.

For the forest-like part \(T=S-E\), independence gives
\[
\operatorname{Var}S=np(1-p),\quad
\operatorname{Var}E=n(p^2-p^4)+2W(p^3-p^4),
\quad\operatorname{Cov}(S,E)=2np^2(1-p).
\]
Two distinct edge indicators covary only when their edges share a vertex, and the number of such unordered edge pairs is \(W\). Consequently
\[
\operatorname{Var}T=n(p-4p^2+4p^3-p^4)+2W p^3(1-p).
\]
To calculate the cycle correction, a vertex indicator has nonzero covariance with \(Z\) precisely if its vertex lies in \(C\), giving
\[
\operatorname{Cov}(S,Z)=\ell p^\ell(1-p).
\]
An edge has nonzero covariance with \(Z\) precisely if it lies on the cycle or joins a cycle vertex to an off-cycle vertex. There are \(\ell\) such cycle edges and \(h\) such branch-attachment edges. Their respective covariances are \(p^\ell(1-p^2)\) and \(p^{\ell+1}(1-p)\). Therefore
\[
\operatorname{Cov}(E,Z)=\ell p^\ell(1-p^2)+h p^{\ell+1}(1-p),
\]
\[
\operatorname{Cov}(T,Z)=-(\ell+h)p^{\ell+1}(1-p).
\]
Also \(\operatorname{Var}Z=p^\ell(1-p^\ell)\). The variance identity for \(K=T+Z\) gives the asserted closed form. Matching \(n\), degree multiset and \(\ell\) matches \(W\) and every term except the one involving \(h\), proving the signed difference exactly, with no approximation.

To establish sharpness, for \(n\le5\), if the cycle has length at least four, there is at most one off-cycle vertex and thus \(h\) is fixed by \(n\) and \(\ell\). If \(\ell=3\), at most two off-cycle vertices exist. With two off-cycle vertices, \(h=1\) forces a single length-two pendant chain from the triangle, with degree multiset \((1,2,2,2,3)\). If \(h=2\), both off-cycle vertices attach directly to the triangle: attachment to the same cycle vertex gives \((1,1,2,2,4)\), while attachment to distinct cycle vertices gives \((1,1,2,3,3)\). These are disjoint multisets. With fewer off-cycle vertices \(h\) is automatically fixed. Hence no pair on five or fewer vertices with matched degree multiset and cycle length can disagree in \(h\). The stated six-vertex edge sets are each connected, have six vertices and six edges with exactly one triangle, and direct degree calculation yields the same degree multiset and \(h_G=1,h_H=2\). Their variance difference is the claimed positive polynomial. This completes the proof.

## Verification

Run `python3 verify.py` from the directory containing this document and the included checker. The checker uses only the Python standard library. For each of the 3,898 labeled connected unicyclic graphs with three through six vertices, it enumerates every surviving vertex set and constructs the first- and second-moment polynomials exactly over the integers. Both agree coefficientwise with the theorem, giving 7,796 exact polynomial equalities. It independently confirms that degree-matched/cycle-length-matched graphs on at most five vertices have the same \(h\), and checks the explicit six-vertex variance difference. Its finite census supplements but does not establish the unrestricted theorem: the proof above covers all graph orders.

## Relationship to prior work

Hanski and Ovaskainen (2000) motivate the ecological importance of habitat connectivity but use a spectral metapopulation-capacity measure, not the variance of connected fragments under independent patch loss. Tittmann, Averbouch and Makowsky (2008) introduce the general induced-subgraph component polynomial \(Q(G;x,y)\), which indeed *implicitly determines* the entire component-count distribution and therefore its variance for any finite graph. The elementary subset enumeration of the present example is already available in principle from that general machinery. The contribution here is instead the closed structural law for **every unicyclic graph**, its all-parameter order comparison using the cycle-root attachment count, and the sharp six-patch distinction between degree-matched and cycle-length-matched habitats. Liao and Hou (2013) investigate reconstructible graph invariants and explicit special families using \(Q\), but do not state this unicyclic variance identity or its sharp matching boundary. Related published work on degree-matched **trees** shows equality of the first two fragment-count moments, whereas the cycle term \(Z\) creates the new variance distinction here.

## Limitations

No conclusion is claimed for multicyclic graphs, heterogeneous or correlated patch survival, bond percolation, component-size statistics, or conditional moments given at least one survivor. The six-patch pair is a minimal structural example, not an empirical prediction or an assertion that the entire component-count distribution is uniquely recoverable. The general induced-subgraph polynomial already determines these statistics computationally; the novelty claim is confined to the structural closed form and sharp six-patch comparison. Literature searches cannot certify absolute historical priority; a separate independent audit remains unperformed.

## References

- I. Hanski and O. Ovaskainen, *The metapopulation capacity of a fragmented landscape*, Nature **404** (2000), 755–758, DOI: 10.1038/35008063. First publicly verified journal issue date: 2000-04-13. https://www.nature.com/articles/35008063
- P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147 (2008). https://arxiv.org/abs/0812.4147
- S. Liao and Y. Hou, *Note on the subgraph component polynomial*, arXiv:1311.6856 (2013). https://arxiv.org/abs/1311.6856
- *Degree-matched habitat trees conceal fragmentation in the first two moments, but not the third* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-degree-matched-habitat-trees-conceal-fragmentation-in-the-first--54bd12285874
