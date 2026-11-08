# Minimal connected vertex covers of full subdivisions: a spanning-tree transform and cardinality gaps

## Finding

For a finite connected simple graph \(G\) of order \(n\ge3\) and minimum degree at least two, form its *full subdivision* \(S(G)\) by replacing every edge \(uv\) with the path \(u,s_{uv},v\). A connected vertex cover is a set meeting every graph edge and inducing a connected subgraph; inclusion-minimal refers to containment, not merely minimum size.

**Classification.** Every inclusion-minimal connected vertex cover of \(S(G)\) has the unique form
\[
C(I,T)=\bigl(V(G)\setminus I\bigr)\ \cup\ \{s_e:e\in\delta_G(I)\cup E(T)\},
\]
where \(I\subseteq V(G)\) is independent, \(G-I\) is connected, and \(T\) is any spanning tree of \(G-I\). Here \(\delta_G(I)\) is the cut consisting of edges with exactly one endpoint in \(I\).

Writing \(\tau(H)\) for the number of spanning trees of a connected graph \(H\), the **complete inclusion-minimal connected-vertex-cover polynomial** is
\[
\boxed{P_{S(G)}(z)=z^{2n-1}\!\sum_{\substack{I\subseteq V(G)\text{ independent}\\G-I\text{ connected}}}\!\tau(G-I)z^{\sum_{v\in I}(\deg_G(v)-2)}.}
\]
In particular, every minimal cover has size at least \(2n-1\), and all minimum covers are exactly the pairs \((I,T)\) with every vertex of \(I\) of degree two. The scalar minimum \(2n-1\) is already known; the new content is the full classification and polynomial.

For the complete bipartite graph \(G=K_{2,q}\), for every integer \(q\ge2\), the polynomial specializes to
\[
\boxed{P_{S(K_{2,q})}(z)=q3^{q-1}z^{2q+3}+2z^{3q+1}.}
\]
At \(q=2\) the exponents agree, yielding eight covers of size seven. At every \(q\ge4\) there are exactly \(q-3\) missing intermediate cardinalities. Thus inclusion-minimal connected vertex covers can have arbitrarily large gaps between attainable sizes, already on full subdivisions of complete bipartite graphs with a fixed two-vertex side.

## Assumptions and scope

All graphs are finite, simple, and undirected. The input \(G\) is connected, has \(n\ge3\) vertices, and has minimum degree \(\delta(G)\ge2\). Vertices \(s_e\) for distinct edges are distinct, and each has exactly the endpoints of \(e\) as neighbors. \(G-I\) means the induced graph on \(V(G)\setminus I\). A spanning tree is counted on the labeled vertex set of \(G-I\); different trees give different cover sets. Every term has nonnegative integral exponent, since the degree condition applies to every omitted vertex.

## Proof

**Step 1: the omitted original vertices form an independent set.** Let \(C\) be any connected vertex cover of \(S(G)\), and put \(U=C\cap V(G)\), \(I=V(G)\setminus U\). The set \(C\) has more than one vertex: a single vertex cannot meet the edges of the subdivision of a graph of minimum degree two and order at least three. If \(uv\in E(G)\) with \(u,v\in I\), both edges \(us_{uv}\) and \(s_{uv}v\) force \(s_{uv}\in C\), but that subdivision vertex is isolated in \(S(G)[C]\), contradicting connectedness. Hence \(I\) is independent.

**Step 2: forced edges and connectivity.** If \(uv\) crosses the cut \((I,U)\), the edge incident with its omitted endpoint forces \(s_{uv}\in C\). Every such selected cut subdivision vertex is pendant in \(S(G)[C]\). Subdivision vertices on edges wholly inside \(U\) are optional from the standpoint of coverage, but must join the original vertices in a connected induced graph. Write \(F\) for the set of these internal original edges whose subdivision vertices are selected. The graph \((U,F)\) is connected and therefore \(G[U]\) is connected.

**Step 3: necessity of a spanning tree.** If \((U,F)\) contained a cycle, removing the subdivision vertex corresponding to any edge of this cycle would leave all subdivided edges covered and would preserve connectedness, contradicting inclusion-minimality. Thus \(F\) is a spanning tree \(T\) on \(U\). There are no selected subdivision vertices with both endpoints in \(I\), by Step 1; therefore \(C=C(I,T)\) uniquely.

**Step 4: sufficiency and strong minimality.** Fix any admissible \((I,T)\). The set \(C(I,T)\) is connected (it is a subdivision of the tree \(T\), with all cut subdivisions attached as leaves) and it covers every edge of \(S(G)\): an internal edge is covered by an endpoint in \(U\), while an edge incident with an omitted original vertex is covered by its selected subdivision vertex. Each selected subdivision vertex is indispensable: removing a cut vertex uncovers an edge, and removing a tree subdivision vertex disconnects the selected original vertices.

For an original vertex \(u\in U\), distinguish three cases. If \(u\) has an omitted neighbor \(v\in I\), then \(s_{uv}\) is retained but becomes isolated when \(u\) is deleted. If \(u\) has no omitted neighbors and some incident edge outside \(T\), then the corresponding subdivision vertex is unselected, and deleting \(u\) uncovers the edge from \(u\) to that vertex. Otherwise every original edge incident to \(u\) lies in \(T\), so \(\deg_T(u)=\deg_G(u)\ge2\); deleting \(u\) splits the subdivided tree into at least two nonempty components. Thus no selected vertex can be removed while maintaining a connected vertex cover.

Finally, the family of connected vertex covers of a *connected* graph is upward closed: any vertex added to a connected vertex cover has a neighbor inside it (as the cover meets every edge and the graph is connected), preserving both coverage and connectivity. Consequently a connected vertex cover without any deletable single vertex has no proper connected vertex cover subset. This establishes inclusion-minimality without mistaking local minimality for global minimality.

**Step 5: exact polynomial and minimum.** Every admissible \((I,T)\) contributes one cover, and the indexing is injective because \(I\) and \(T\) are recoverable from the selected original and subdivision vertices. Since \(I\) is independent, the number of cut edges equals \(\sum_{v\in I}\deg_G(v)\). Therefore
\[
\begin{aligned}
|C(I,T)|&=|U|+(|U|-1)+|\delta_G(I)|\\
&=2n-1+\sum_{v\in I}(\deg_G(v)-2).
\end{aligned}
\]
Summing over the \(\tau(G-I)\) spanning trees proves the polynomial. All exponents beyond \(2n-1\) are nonnegative. Since \(I=\varnothing\) is allowed, minimum size is exactly \(2n-1\). Equality holds exactly when every omitted vertex has degree two.

**Step 6: the two-by-\(q\) bipartite specialization.** In \(K_{2,q}\), any independent \(I\) whose complement is connected consists either of a proper subset of the \(q\)-vertex side or of exactly one vertex from the two-vertex side. For an omitted set of size \(k\) from the large side, \(G-I=K_{2,q-k}\), \(0\le k\le q-1\), and its tree count is \(2^{q-k-1}(q-k)\). All such omitted vertices have original degree two and contribute weight zero. Summing gives
\[
\sum_{b=1}^{q}\binom qb 2^{b-1}b=q3^{q-1}.
\]
Omitting one of the two high-degree vertices gives two stars \(K_{1,q}\), each with a unique spanning tree and weight increment \(q-2\). This yields the two-term formula. Its exponents differ by \(q-2\), so for \(q\ge4\) precisely \(q-3\) intermediate integers are not attainable.

## Verification

The accompanying `verify.py` independently reconstructs each full subdivision and checks the original cover, connectedness and single-deletion definitions. It enumerates every labeled connected graph of minimum degree at least two on three, four, and five vertices: respectively \(1,10,253\) graphs. Their complete minimal-cover families agree with the spanning-tree construction, with \(1,165,880\) original-family subset masks examined and \(12,695\) minimal covers identified. The additional bipartite exhaustive tests examine \(149,756\) masks, making \(1,315,636\) masks in total. It additionally verifies the bipartite specialization by exhaustive subset checks at \(q=2,3,4,5\) and by generated-family checks at \(q=6\). The verifier uses only the Python standard library.

This finite testing supplements, but does not replace, the all-graph proof.

## Relationship to prior work

Kobayashi, Kurita, Mann, Matsui and Ono (first public preprint August 31, 2023) study enumeration of inclusion-minimal connected vertex covers; their paper proves the upward-closure property and general enumeration algorithms but not this full-subdivision spanning-tree distribution. Golovach, Heggernes and Kratsch (2016) prove bounds and enumeration algorithms for minimal connected vertex covers without this transformation. Adak and Nanoti (September 2026) prove the **already known** minimum connected-cover size \(2n-1\) for full subdivisions of connected graphs of minimum degree at least two, using covers constructed from spanning trees of the whole original graph; they explicitly state that their constructed covers need not exhaust the minimum covers when degree-two original vertices occur. The present theorem instead classifies **all inclusion-minimal** covers and all minimum covers, including ones omitting degree-two originals, and gives their cardinality polynomial. The independent-set/spanning-tree transform is not a consequence of the cited scalar minimum result or the general enumeration algorithms.

## Limitations

The input minimum-degree hypothesis matters: for a path on three vertices, the spanning-tree construction using all original vertices gives a connected cover that is not minimal. The theorem does not extend unmodified to graphs with leaves or to arbitrary edge-subdivision lengths. No claim of absolute publication priority or independent mathematical certification is made. Searches cannot exclude differently indexed earlier literature. Computing the polynomial still involves a weighted sum over connected induced subgraphs and spanning-tree counts.

## References

1. Y. Kobayashi, K. Kurita, K. Mann, Y. Matsui and H. Ono, *Enumerating minimal vertex covers and dominating sets with capacity and/or connectivity constraints*, arXiv:2308.16426, first submitted August 31, 2023, https://arxiv.org/abs/2308.16426 .
2. P. A. Golovach, P. Heggernes and D. Kratsch, *Enumeration and Maximum Number of Minimal Connected Vertex Covers in Graphs*, arXiv:1602.07504, February 24, 2016, https://arxiv.org/abs/1602.07504 .
3. R. Adak and S. G. Nanoti, *On Eternal Connected Vertex Cover*, arXiv:2609.39103, September 2026, especially Section 5.1, https://arxiv.org/abs/2609.39103 .
