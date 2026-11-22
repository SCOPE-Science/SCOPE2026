# Complete edge-geodesic transversal polynomials and unmixedness of multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a simple labelled complete multipartite graph with \(r\ge2\), \(n_i\ge1\). Write its parts as \(V_i\), let \(m=\sum_{i<j}n_i n_j\), and let \(s\) count singleton parts. An **edge-geodesic transversal** is a set of edges meeting every maximal shortest path, where maximal means not a proper subpath of any longer shortest path. Write \(\mathcal{T}_e(G;z)=\sum_{S}z^{|S|}\), summing over *all* such transversals.

**Classification.** A subset \(S\subseteq E(G)\) is an edge-geodesic transversal if and only if, for its omitted-edge set \(F=E(G)\setminus S\): (i) no edge joining two singleton parts is omitted; (ii) for every other unordered pair \(i<j\), the omitted edges between \(V_i\) and \(V_j\) form a matching of \(K_{n_i,n_j}\). The matching choices are independent between different part pairs.

In particular,
\[
\boxed{\mathcal{T}_e(G;z)=z^{\binom{s}{2}}\prod_{\substack{i<j\\(n_i,n_j)\ne(1,1)}}\left(\sum_{k=0}^{\min(n_i,n_j)}\binom{n_i}{k}\binom{n_j}{k}k!\,z^{n_i n_j-k}\right).}
\]
Here an empty product equals one. Let \(\mathcal B\) be the pairs \(i<j\) other than singleton–singleton pairs. Then
\[
\boxed{\operatorname{gt}_e(G)=m-\sum_{(i,j)\in\mathcal B}\min(n_i,n_j),\qquad\#\{S:|S|=\operatorname{gt}_e(G)\}=\prod_{(i,j)\in\mathcal B}\frac{\max(n_i,n_j)!}{(\max(n_i,n_j)-\min(n_i,n_j))!}.}
\]
**Unmixedness:** every inclusion-minimal edge-geodesic transversal is minimum. Moreover \(\mathcal{T}_e(G;z)\) has only nonpositive real zeros; its nonzero coefficients are log-concave and occupy every integer degree from \(\operatorname{gt}_e(G)\) through \(m\).

For example, \(K_{2,2,2}\) has \(m=12\), minimum transversal size six, and exactly eight labelled minimum transversals. In \(K_{1,1,2}\), the edge between the singleton parts is compulsory, while each of the two two-edge bipartite blocks independently permits one omitted edge.

## Assumptions and scope
All graphs are finite, simple, undirected; partite vertex labels and colours are fixed. Distances and maximal geodesics are in the entire graph, not individual bipartite blocks. The case in which all parts are singletons is a complete graph; the theorem applies, with every edge compulsory. For \(r\ge2\), the graph is connected. A matching means pairwise vertex-disjoint edges *within one unordered bipartite block*; selected edges from distinct blocks may share vertices.

## Proof
**Maximal-geodesic classification.** Distinct vertices in different parts are adjacent. Distinct vertices in the same non-singleton part are at distance two, via every vertex outside that part. Consequently, all two-edge geodesics are precisely the paths \(x-y-z\) with \(x,z\in V_i\), distinct, and \(y\in V_j\), \(i\ne j\). These are maximal because no geodesic can have more than two edges. An edge \(xy\), with \(x\in V_i\) and \(y\in V_j\), extends to a two-edge geodesic whenever \(n_i\ge2\) (choose a second vertex of \(V_i\)) or \(n_j\ge2\). If both parts are singletons, neither extension exists, and the edge itself is a maximal geodesic. This exhausts all maximal geodesics, including the complete-graph boundary case.

**Block characterization.** The two edges of a maximal length-two geodesic lie in a unique bipartite block \(E(V_i,V_j)\) and have a common endpoint. Conversely, any two incident edges of that block form a two-edge geodesic (their non-common endpoints belong to the same part). Thus an omitted-edge set avoids all maximal length-two geodesics exactly when it induces a matching in each block. The singleton–singleton edges must additionally be selected because they are maximal one-edge geodesics. The constraints involve one block at a time; hence they are independent. This proves the if-and-only-if classification.

**Counting, minimum cardinality and inclusion minimality.** In \(K_{a,b}\), the number of matchings with \(k\) edges is \(\binom ak\binom bk k!\). Each such matching omits \(k\) edges from the selected transversal of that block. Multiplication over the independent blocks and compulsory singleton-pair edges gives the stated polynomial. A matching in \(K_{a,b}\) is inclusion-maximal if and only if it is maximum: when it has fewer than \(\min(a,b)\) edges, some vertex on *each* side is unmatched and an edge joining these vertices can be added. Therefore \(S\) is inclusion-minimal among transversals if and only if every permitted omitted block is a maximum matching. Every such \(S\) has the displayed common cardinality. A maximum matching in \(K_{a,b}\) injects the smaller side into the larger, yielding \(\max(a,b)!/(\max(a,b)-\min(a,b))!\) choices. Multiplying counts yields the minimum-transversal census. Taking any matching size from zero to its maximum in each independent block gives the contiguous degree interval.

**Real-rootedness and log-concavity.** The ordinary matching generating polynomial of \(K_{a,b}\) is \(M_{a,b}(t)=\sum_{k=0}^{\min(a,b)}\binom ak\binom bk k!t^k\). The classical Heilmann–Lieb theorem that the matching polynomial of a graph has only real roots implies that the roots of \(M_{a,b}(t)\) are strictly negative (its coefficients are positive and its constant term is one). Each non-compulsory block factor above is the reciprocal polynomial \(z^{ab}M_{a,b}(1/z)\), hence has only nonpositive real roots; the compulsory factor is a power of \(z\). Products preserve real-rootedness. Newton's inequalities for polynomials with nonnegative coefficients and only real roots prove log-concavity of their nonzero coefficient sequence.

## Verification
The standalone `verify.py` independently forms maximal geodesics for several boundary and nontrivial profiles, exhaustively enumerates every edge subset, and directly tests the literal hitting condition against (i) the omitted-block matching rule, (ii) every coefficient of the product formula, and (iii) inclusion-minimality versus minimum cardinality. The test set includes all-singleton, mixed-singleton, bipartite and three-partite graphs; all pass. Finite enumeration corroborates, but is not a proof of, the arbitrary-size result. The mathematical proof above needs no enumeration assumption.

## Relationship to prior work
Prabha, Sandhiya and Manuel introduced the edge-geodesic transversal invariant in the public preprint arXiv:2610.36821v1 (27 October 2026). Its complete eight-page text gives basic bounds, an edge-cut method and results for paths, cycles, complete graphs, hypercubes, stacked prisms and ladders; it does **not** state an all-size complete-multipartite edge-transversal polynomial or inclusion-minimal rigidity theorem.

The published published-finding corpus result on complete-multipartite **edge-geodesic covers and partitions** (4 October 2026) observes the same confinement of length-two geodesics to bipartite blocks, but minimizes numbers of geodesic *paths covering edges*, not edge *subsets hitting paths*. This elementary block observation is used here without any claim of novelty. A distinct published-finding corpus work on **vertex-disjoint geodesic packings** (8 November 2026) counts disjoint paths and gives a separate purity boundary. Another work (12 October 2026) counts **vertex** geodesic transversals of multipartite graphs, not edge transversals. Neither known result implies the matching-block complement classification, exact edge-transversal enumerator or unmixedness for the edge-hitting problem. The Heilmann–Lieb matching-root theorem is previously known and is used, not rediscovered.

## Limitations
The underlying classification follows from the diameter-two path structure specific to complete multipartite graphs; no comparable statement is asserted for arbitrary diameter-two graphs. The root conclusion is a consequence of the classical matching-polynomial theorem after the new complement characterization, not a new real-rootedness theorem for matching polynomials. Literature searches cannot rule out differently phrased, unindexed or unpublished earlier derivations. This is a self-review, not an independent mathematical audit.

## References
1. R. Prabha, B. Sandhiya and P. Manuel, *The Edge Geodesic Transversal Problem*, arXiv:2610.36821v1, 27 October 2026, https://arxiv.org/abs/2610.36821.
2. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232, DOI 10.1007/BF01877590.
3. *Edge-geodesic cover and partition numbers of complete multipartite graphs*, published-finding corpus mathematical record, 4 October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-edge-geodesic-cover-and-partition-numbers-of-complete-multiparti--ed7c74654578/RESULT.md.
4. *Geodesic-packing polynomials of complete multipartite graphs and reentrant purity for doubleton parts*, published-finding corpus mathematical record, 8 November 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-geodesic-packing-polynomials-of-complete-multipartite-graphs-and--e3ceab8f39fe/RESULT.md.
5. *All geodesic transversals of complete multipartite graphs*, published-finding corpus mathematical record, 12 October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-all-geodesic-transversals-of-complete-multipartite-graphs--e5c4e05a4d10/RESULT.md.
