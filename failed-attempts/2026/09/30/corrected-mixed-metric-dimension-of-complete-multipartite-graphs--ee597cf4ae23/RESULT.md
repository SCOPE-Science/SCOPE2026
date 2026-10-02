# Corrected mixed metric dimension of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\), \(N=\sum_{i=1}^r n_i\), and
\[
s=|\{i:n_i=1\}|.
\]
Then its mixed metric dimension is
\[
\operatorname{mdim}(G)=
\begin{cases}
N, & s\ge 2,\\
N-2, & r=2\text{ and }n_1,n_2\ge 3,\\
N-1, & \text{otherwise}.
\end{cases}
\]

This corrects the complete-multipartite formula stated as Theorem 5 by Hayat, Khan, and Zhong (2022). For example, their formula gives \(8\) for \(K_{3,3,5}\), while the value above is \(10\).

There is also a separate literature inconsistency in their Theorem 4: for \(r\ge3\), the edge metric dimension is \(N-1\), not \(N-r\). That edge-dimension value was already established by Peterin and Yero, so it is prior work rather than a new theorem here.
## Assumptions and scope
Graphs are finite, simple, and connected. A mixed resolving set is a vertex set \(S\) such that every two distinct objects in \(V(G)\cup E(G)\) have different distance vectors to \(S\), where the distance from a vertex \(z\) to an edge \(uv\) is \(\min\{d(z,u),d(z,v)\}\). The mixed metric dimension is the minimum size of such a set.

The statement covers all connected complete multipartite graphs, including stars and complete graphs. Singleton parts are exactly the universal vertices of a complete multipartite graph.
## Proof
First record an elementary edge-resolution fact. If \(r\ge3\), every edge-resolving set has size at least \(N-1\). Indeed, suppose two vertices \(x,y\) are omitted. If they lie in the same part, choose a landmark \(z\) outside that part; the edges \(xz\) and \(yz\) have identical distances to every landmark. If they lie in distinct parts, choose \(z\) in a third part; then \(xz\) and \(yz\) again have identical distances to every landmark. Conversely, omitting only one vertex leaves every edge with at least one landmark endpoint, and distinct edges have different zero-coordinate patterns. Hence \(\operatorname{edim}(G)=N-1\) for \(r\ge3\). This also gives a direct obstruction to the set used in the 2022 proof of Theorem 4.

We now prove the mixed formula by cases.

If \(s\ge2\), let \(u\) be a universal vertex. Any proper landmark set omits some vertex \(x\). Choose a universal landmark \(u\) distinct from \(x\) if necessary; when the omitted vertex itself is universal, another universal vertex is available. The vertex \(u\) and the edge \(ux\) have the same distance to every landmark: distance \(0\) at \(u\), and distance \(1\) at every other landmark. Thus no proper subset of \(V(G)\) is mixed resolving, and \(\operatorname{mdim}(G)=N\).

Suppose \(s=1\), and let \(u\) be the unique universal vertex. A set omitting at least two vertices cannot be mixed resolving. If \(u\) is omitted together with \(x\), then the vertex \(u\) and the edge \(ux\) both have distance \(1\) to every landmark. If \(u\) is a landmark and two non-universal vertices \(x,y\) are omitted, then the edges \(ux\) and \(uy\) both have distance \(0\) at \(u\) and distance \(1\) at every other landmark. Hence \(\operatorname{mdim}(G)\ge N-1\). On the other hand, \(V(G)\setminus\{u\}\) is mixed resolving: every edge has one or two landmark endpoints, and a vertex and an incident edge are separated by another vertex in the same non-singleton part. Therefore \(\operatorname{mdim}(G)=N-1\).

Suppose \(s=0\) and \(r\ge3\). The edge-resolution argument above gives \(\operatorname{mdim}(G)\ge N-1\). For the reverse inequality, omit one vertex \(x\). Every part has size at least two. Distinct edges are separated by their landmark endpoints. The omitted vertex has no zero coordinate, whereas every edge has at least one. Finally, if a landmark vertex \(v\) is compared with an incident edge whose other endpoint is \(x\), another landmark in the part of \(v\) has distance \(2\) from \(v\) and distance \(1\) from that edge. All remaining vertex-edge pairs are even more directly separated by an endpoint coordinate. Thus \(V(G)\setminus\{x\}\) is mixed resolving, so \(\operatorname{mdim}(G)=N-1\).

It remains to consider \(r=2\) with no singleton part; write \(G=K_{a,b}\) with \(a,b\ge2\). An edge-resolving set must omit at most one vertex from each part, so every mixed resolving set has size at least \(N-2\).

If \(a,b\ge3\), omit one vertex from each part. The resulting \(N-2\) landmarks mixed-resolve the graph: edges are determined by their zero-coordinate pattern, the unique edge joining the two omitted vertices has the all-one edge vector, and each landmark vertex is separated from an incident edge by another landmark in its own part. Hence \(\operatorname{mdim}(G)=N-2\).

If one part has size \(2\), an \(N-2\)-vertex mixed resolving set would have to omit one vertex from each part. Let \(a\) be the unique landmark left in the two-vertex part and let \(y\) be the omitted vertex in the other part. Then the vertex \(a\) and the edge \(ay\) have identical distances to all landmarks, a contradiction. Thus \(\operatorname{mdim}(G)\ge N-1\). Omitting one vertex from the other part gives an \(N-1\)-vertex mixed resolving set, because both vertices in the two-vertex part remain as landmarks and separate each vertex from its incident edge. Therefore \(\operatorname{mdim}(G)=N-1\).

These cases exhaust all complete multipartite graphs.
## Verification
An exact exhaustive checker independently constructs every complete multipartite type of orders \(2\) through \(8\), enumerates all landmark subsets, computes all vertex and edge distance vectors, and compares the brute-force minimum with the formula above. It verifies all \(58\) types. The same checker also verifies \(\operatorname{edim}(G)=N-1\) for every tested type with \(r\ge3\). The checker and its exact output are included with this result.

This computational check is finite corroboration of the proof, not an independent audit.
## Relationship to prior work
Kelenc, Kuziak, Taranenko, and Yero introduced mixed metric dimension and determined the complete bipartite cases. Peterin and Yero later determined the edge metric dimension of complete multipartite graphs, including the value \(N-1\) for at least three parts. Hayat, Khan, and Zhong subsequently stated different complete-multipartite edge and mixed formulas in Theorems 4 and 5 of their 2022 paper. The edge formula there conflicts with the earlier Peterin-Yero theorem for every \(r\ge3\); a direct two-omitted-vertex obstruction is given above. The mixed formula is also false outside several special subfamilies, and the piecewise formula proved here supplies the corrected all-parameter statement.

Ghalavand, Klavžar, and Tavakoli later characterized graphs of maximum mixed metric dimension and treated universal vertices. Those results are consistent with the singleton-part cases above. The contribution here is the explicit correction and complete synthesis for all complete multipartite parameters, not a claim that each constituent ingredient is new.
## Limitations
The literature comparison is best-of-knowledge rather than a proof that no earlier correction exists. The theorem has received same-model review and exact finite corroboration, but no independent audit, formal proof assistant verification, or expert attestation has been performed. The edge-dimension formula is prior work and is included only to expose the contradiction and support the mixed-dimension correction.
## References
1. M. Kelenc, D. Kuziak, A. Taranenko, and I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292 (first public version 2016-11-14); Applied Mathematics and Computation 314 (2017), 429–438, DOI: 10.1016/j.amc.2017.07.027.
2. I. Peterin and I. G. Yero, “Edge metric dimension of some graph operations,” arXiv:1809.08900 (first public version 2018-09-24); Bulletin of the Malaysian Mathematical Sciences Society 43 (2020), 2465–2477, DOI: 10.1007/s40840-019-00816-7.
3. S. Hayat, A. Khan, and Y. Zhong, “On Resolvability- and Domination-Related Parameters of Complete Multipartite Graphs,” Mathematics 10 (2022), 1815, published 2022-05-25, DOI: 10.3390/math10111815.
4. A. Ghalavand, S. Klavžar, and M. Tavakoli, “Graphs whose mixed metric dimension is equal to their order,” arXiv:2305.19620 (first public version 2023-05-31); Computational and Applied Mathematics 42 (2023), 296, DOI: 10.1007/s40314-023-02351-5.
