# Spanning-tree exchange geometry of minimum skew forcing on full graph subdivisions

## Finding

**Theorem.** Let \(H\) be any finite connected simple graph with \(n\ge 2\) vertices and \(m\) edges. Form \(S(H)\) by subdividing each edge exactly once; denote the subdivision vertex corresponding to \(e\in E(H)\) by \(x_e\). Skew zero forcing allows **any** vertex, blue or white, to turn its unique white neighbor blue. A subset \(B\subseteq V(S(H))\) is a successful initial blue set if and only if it contains at least one original vertex and the edge set
\[
F(B)=\{e\in E(H): x_e\notin B\}
\]
is a forest in \(H\). Consequently, with \(T_H\) the Tutte polynomial,
\[
\mathcal Z^-(S(H);z)=\big((1+z)^n-1\big)z^{m-n+1}T_H(1+z,1),\qquad Z^-(S(H))=m-n+2.
\]
All minimum skew-zero-forcing sets are exactly
\[
B(r,T)=\{r\}\cup\{x_e:e\in E(H)\setminus T\},
\]
where \(r\in V(H)\) and \(T\) is a spanning tree of \(H\). Thus there are \(n\tau(H)\) minimum sets, where \(\tau(H)\) counts spanning trees. Let \(\mathcal B(H)\) be the graph whose vertices are spanning trees of \(H\), adjacent when a single edge is exchanged while retaining a spanning tree. Under optimum-preserving one-token exchange and edge-adjacent token sliding, respectively,
\[
R_{\rm exchange}(S(H))\cong K_n\mathbin\square\mathcal B(H),\qquad
R_{\rm slide}(S(H))\cong n\tau(H)K_1.
\]
The first graph is connected, with the exact distance
\[
d\big(B(r,T),B(s,U)\big)={\bf1}_{r\ne s}+(n-1-|T\cap U|).
\]

For \(H=K_n\), the optimum count is \(n^{n-1}\), and the degree in the exchange graph of a configuration \(B(r,T)\) equals the Wiener index \(W(T)=\sum_{\{u,v\}\subseteq V(K_n)}d_T(u,v)\). Its exact edge count is
\[
\left|E(R_{\rm exchange}(S(K_n)))\right|=\frac n4\sum_{a=1}^{n-1}{n\choose a}a^a(n-a)^{n-a}.
\]
Its diameter is \(1\) when \(n=2\), \(2\) when \(n=3\), and \(n\) for all \(n\ge4\). The sliding graph is edgeless at every order.

The new contribution is the full optimum-reconfiguration structure and metric, including the Wiener degree law and complete-clique edge census. The feasibility characterization and Tutte specialization are stated for completeness and to provide a constructive bridge from existing general forcing theory to this geometry.

## Assumptions and scope

All graphs in the theorem are finite, undirected, connected and simple. The graph \(H\) has at least two vertices, so \(m\ge n-1\). A forest is an acyclic spanning edge subset of \(H\), allowing isolated vertices. Edges and vertices in the host \(S(H)\) are distinct objects: its original vertices correspond to \(V(H)\), and its subdivision vertices are indexed by \(E(H)\). Initially blue vertices are an unordered set, not labeled tokens. All intermediate configurations of a relocation must remain *minimum* skew forcing sets; addition/removal of intermediate tokens is not allowed. The Tutte polynomial uses the normalization
\[
T_H(x,y)=\sum_{A\subseteq E(H)}(x-1)^{c(A)-1}(y-1)^{|A|-n+c(A)},
\]
where \(c(A)\) counts components of \((V(H),A)\). Expressions involving \((y-1)^0\) take value one at \(y=1\).

## Proof

**1. Characterization.** Suppose no original vertex is initially blue. Every original vertex stays white: to force one of them, some subdivision vertex \(x_{uv}\) would have to have exactly one white neighbor, yet both of its original neighbors are white until the first original vertex is forced. Hence no first original vertex can be forced. If \(F(B)\) contains a cycle, its cycle subdivision vertices are all initially white. Before the first one is forced, each original endpoint on the cycle has at least two white subdivision neighbors, so cannot force a cycle subdivision vertex. A subdivision vertex cannot force a subdivision vertex (the host is bipartite). Hence none of these white subdivision vertices can ever be forced.

Conversely, suppose an original vertex is blue initially and \(F(B)\) is acyclic. Repeatedly choose a leaf original vertex \(v\) of the nonempty remaining edge forest, with unique incident remaining edge \(e\). Every subdivision neighbor of \(v\), except \(x_e\), is already blue. Thus \(v\), regardless of its own color, can force \(x_e\). Delete \(e\) from the remaining forest and repeat until every subdivision vertex is blue. Now traverse any spanning tree of \(H\) outward from an initially blue original vertex. For an original edge \(uv\) with \(u\) blue and \(v\) white, the blue subdivision vertex \(x_{uv}\) has the unique white neighbor \(v\), so forces \(v\). Connectivity colors every original vertex blue. This proves both directions without assuming every forcing vertex is blue.

**2. Polynomial and minima.** Write \(s=|B\cap V(H)|\), and \(f=|F(B)|\). Successful sets are precisely those with \(1\le s\le n\) and an arbitrary spanning forest \(F(B)\). Their sizes are \(s+m-f\). Since \(f\le n-1\), every successful set has at least \(m-n+2\) vertices; equality requires \(s=1\) and \(f=n-1\). A forest of \(n-1\) edges in a connected \(n\)-vertex graph is a spanning tree. All pairs \((r,T)\) occur independently, yielding \(n\tau(H)\) minima.

The original-vertex choice enumerator is \((1+z)^n-1\), and the subdivision-vertex choice contributes \(\sum_{F\text{ forest}}z^{m-|F|}\). The defining subset expansion of the Tutte polynomial implies \(T_H(1+z,1)=\sum_{F\text{ forest}}z^{n-1-|F|}\); multiplying gives the asserted polynomial, including its leading coefficient \(n\tau(H)\) at degree \(m-n+2\).

**3. Relocation product and distances.** Two sets \(B(r,T)\) and \(B(s,U)\) differ by a one-token exchange precisely when they have the same spanning-tree data and different roots, or the same root and spanning trees with a one-edge symmetric difference. In particular there is no mixed exchange of an original vertex and a subdivision vertex, because every minimum set contains exactly one original. Thus the exchange graph is the stated Cartesian product. In any connected graph, for spanning trees \(T,U\), repeatedly choose \(e\in U\setminus T\); the fundamental cycle of \(T+e\) contains some \(f\in T\setminus U\), since \(U\) cannot contain a cycle. Replacing \(f\) by \(e\) increases \(|T\cap U|\) by one, reaching \(U\) in exactly \(n-1-|T\cap U|\) exchanges. No shorter sequence can insert more than one missing edge per step. The shortest Cartesian-product distance is the sum of this distance and \({\bf1}_{r\ne s}\). Any edge of \(S(H)\) joins an original vertex to a subdivision vertex; sliding a selected token along it would change the count of selected original vertices away from one. It therefore cannot lead from one minimum configuration to another. This proves complete sliding rigidity.

**4. Complete-graph degree and edge count.** In a spanning tree \(T\subseteq K_n\), exchanging a non-tree edge \(uv\) for an edge on its unique \(T\)-path offers exactly \(d_T(u,v)\) choices. Therefore the degree inside \(\mathcal B(K_n)\) equals
\[
\sum_{uv\notin T}d_T(u,v)=W(T)-(n-1),
\]
because each of the \(n-1\) tree edges has distance one. There are another \(n-1\) root changes, so the degree in the Cartesian product equals \(W(T)\). Each tree edge \(e\) separates its tree into components of sizes \(a_e\) and \(n-a_e\), and \(W(T)=\sum_{e\in T}a_e(n-a_e)\). Sum this identity over all labeled spanning trees. A specified unordered split with shore sizes \(a,n-a\) arises from \(a^{a-2}(n-a)^{n-a-2}a(n-a)\) trees after choosing the two shore trees and the joining edge; multiplying by the distance contribution \(a(n-a)\) gives \(a^a(n-a)^{n-a}\). Summing over ordered shore choices and dividing by two gives
\[
\sum_T W(T)=\frac12\sum_{a=1}^{n-1}{n\choose a}a^a(n-a)^{n-a}.
\]
For singleton shores use the standard one-vertex tree convention, which agrees with this expression. There are \(n\) choices of root per tree, so the handshake lemma gives the asserted formula for exchange edges.

**5. Diameter.** The distance formula gives the upper bound \(n\). For \(n\ge4\), take one spanning tree to be the path with edges \(\{i,i+1\}\) for \(0\le i\le n-2\), and the other to have edges \(\{0,j\}\) for \(2\le j\le n-1\), together with \(\{1,3\}\). These are edge-disjoint spanning trees. Choose distinct roots to attain distance \(1+(n-1)=n\). For \(n=3\), any two spanning trees share one edge, and distinct roots give distance two. At \(n=2\), a single tree and two roots give diameter one.

## Verification

Two independently structured, standard-library-only Python programs accompany this result. Run `python3 check_skew_small.py` and `python3 check_skew_trees.py` in the same directory as this document. The first exhaustively computes skew forcing closure for every candidate starting set on all \(43\) connected labelled simple graphs of orders two through four and four more connected graphs of order five, and compares every result against the forest criterion and optimum counts. It also directly compares all pairs of optimal sets for token jumps and original-edge slides. The second generates spanning trees of labeled complete graphs from Prüfer sequences for orders three through seven, independently checks the Wiener degree law, counts exchange edges by the shore-cut formula, and exhaustively tests the tree-basis distance formula for orders three through five. Both succeeded in a fresh execution on the delivered source files.

For reproducibility, selected outcomes are: \(K_3\) has \(9\) minimum configurations and \(18\) token-jump edges; \(K_4\) has \(64\) and \(312\); \(K_5\) has \(625\) and \(5900\); \(K_6\) has \(7776\) and \(124200\); \(K_7\) has \(117649\) and \(2908542\). Finite checks are corroboration of the all-order proof, not a substitute for it.

## Relationship to prior work

Jacob introduced the skew-zero-forcing polynomial terminology in *The zero forcing span of a graph* (arXiv:2309.06234, first public 12 September 2023). Curtis, Flagg and Hogben studied token addition/removal for skew forcing and other vertex-set parameters (arXiv:2406.05509, first public 8 June 2024). DeAlba's 2014 paper gave matching and matroid results for certain bipartite graphs, under hypotheses distinct from a general full subdivision. Bong and collaborators' 2025 study investigated minimum skew-forcing token exchanges and slides, especially on trees, and proves their tree sliding rigidity, but does not assert the arbitrary-source-graph subdivision product.

Most directly, Bonato and collaborators (arXiv:2412.04389, first public 5 December 2024), Theorem 33, showed that skew forcing of a hypergraph incidence graph is equivalent to simultaneous lazy burning of the hypergraph and its dual. Specializing this general theorem to a two-uniform connected hypergraph yields a route to the forest feasibility criterion, so that criterion is **not** asserted here to be unrelated to prior work. The additional exact optimum exchange-graph identification, its all-pairs distance formula, complete sliding obstruction, and the Wiener-index and edge-count identities for the subdivided clique require further graph-specific structure. A published indexed result on ordinary (blue-only) zero forcing of full clique subdivisions uses a different rule and hence gives different optimum sets; it does not imply these skew-reconfiguration conclusions. Generic graphic-matroid basis exchanges explain connectivity after the rooted-spanning-tree correspondence, but do not by themselves identify which forcing configurations have that correspondence.

## Limitations

The theorem addresses one subdivision per edge of a *simple connected* graph. Disconnected hosts, higher subdivisions, variants requiring a blue forcing vertex, and relocation using intermediate nonminimum sets are outside scope. The edge-count and diameter identities specialize to complete graphs; an arbitrary host graph's basis-graph diameter is given only through the exact pairwise tree-intersection distance. The originality comparison relies on the named accessible full texts and indexed queries; no negative search result can establish universal historical priority. Independent formal proof review has not been performed.

## References

1. B. Jacob, *The zero forcing span of a graph*, arXiv:2309.06234, 2023. https://arxiv.org/abs/2309.06234
2. B. A. Curtis, M. Flagg and L. Hogben, *TAR reconfiguration for vertex set parameters*, arXiv:2406.05509, 2024. https://arxiv.org/abs/2406.05509
3. L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618, 2014. https://arxiv.org/abs/1404.1618
4. A. Bonato, C. Jones, T. G. Marbach, T. Mishura and Z. Zhang, *Hypergraph burning, matchings, and zero forcing*, arXiv:2412.04389, first public 2024-12-05, Theorem 33. https://arxiv.org/abs/2412.04389
5. N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642, first public 2025-01-07. https://arxiv.org/abs/2501.03642
6. D. Hall, S. Pfeil and J. Taylor, *Skew Zero Forcing Matroids*, arXiv:2611.15741, 2026. https://arxiv.org/abs/2611.15741
7. T. Hanaka et al., *Basis sequence reconfiguration in the union of matroids*, arXiv:2409.07848, 2024. https://arxiv.org/abs/2409.07848
