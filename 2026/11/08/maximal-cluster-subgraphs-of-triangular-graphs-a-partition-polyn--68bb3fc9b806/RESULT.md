# Maximal cluster subgraphs of triangular graphs: a partition polynomial and the exceptional pure case

## Finding

For each integer \(n\ge3\), let \(T_n=L(K_n)=J(n,2)\) have a vertex for each edge of the labeled complete graph \(K_n\), with two vertices adjacent exactly when their corresponding edges meet. A **cluster graph** is a disjoint union of cliques, equivalently a graph with no induced three-vertex path. Write \(M_n(z)=\sum_s m_{n,s}z^s\) for the polynomial counting vertex subsets of \(T_n\) that induce inclusion-maximal cluster graphs, by number \(s\) of selected vertices.

**Classification.** A selected edge set \(F\subseteq E(K_n)\) produces an inclusion-maximal cluster subgraph of \(T_n\) if and only if exactly one of the following holds:

1. Every one of the \(n\) base vertices is incident to an edge of \(F\), and the connected components of \(([n],F)\) are disjoint single edges, triangles, or stars with at least three leaves.
2. Exactly one base vertex is isolated in \(([n],F)\), and every nontrivial component is a triangle.

These possibilities are disjoint and uniquely identify each maximal set. In particular, with \([t^n]\) denoting coefficient extraction,
\[
M_n(z)=n![t^n]\left\{\exp\!\left(\frac{zt^2}{2}+\frac{z^3t^3}{6}+\sum_{k\ge4}\frac{z^{k-1}t^k}{(k-1)!}\right)+t\exp\!\left(\frac{z^3t^3}{6}\right)\right\}.
\]
For \(n\ge4\), the attainable cardinalities are exactly
\[
\mathcal S_n=\begin{cases}
([n/2,n-1]\cap\mathbb Z)\cup (\{n\}\text{ if }3\mid n),& n\text{ even},\\
([(n+3)/2,n-1]\cap\mathbb Z)\cup (\{n\}\text{ if }3\mid n),& n\text{ odd}.
\end{cases}
\]
Here intervals denote all integers between their endpoints, inclusive, and the conditional singleton is absent when \(3\nmid n\). The sole case \(n=3\) has \(M_3(z)=z^3\). Consequently, among \(n\ge3\), all inclusion-maximal induced cluster subgraphs have equal order **if and only if** \(n=3\) or \(n=5\). Equivalently, the simplicial complex of cluster-inducing vertex subsets of \(T_n\) is pure exactly for these two orders.

## Assumptions and scope

Graphs are finite, undirected, and simple; all \(n\) vertices of \(K_n\) are distinctly labeled. A vertex subset is inclusion-maximal if no omitted vertex can be added while keeping the cluster property, irrespective of its cardinality. The result counts labeled subsets, not isomorphism classes, and concerns vertex deletion from \(T_n\), not edge deletion from that graph. The sum in the generating function is a formal power series, so coefficient extraction is finite at each fixed \(n\).

## Proof

**Step 1: transfer to edge components.** For any \(F\subseteq E(K_n)\), the induced graph \(T_n[F]\) is precisely \(L(([n],F))\). A line graph is a cluster graph if and only if each nontrivial connected component of its root is a star or a triangle: every nontrivial root component must have pairwise intersecting edges, since its line graph must be a clique, and a pairwise intersecting family of edges in a simple graph is either a star or exactly the three edges of a triangle. Conversely, stars and triangles have clique line graphs; disconnected root components have no adjacency between their edges.

**Step 2: necessary maximality restrictions.** A root graph with two isolated base vertices is not maximal: inserting the edge between them produces another isolated clique vertex in the line graph. If exactly one base vertex is isolated and a nontrivial component is a star, adding an edge from the isolated vertex to its center extends that star (this also holds for a one-edge star), so maximality fails. Thus, with one isolated vertex, all components must be triangles. If no base vertex is isolated, any two-edge star (a path on three base vertices) can be completed to a triangle by adding its missing leaf-to-leaf edge, and the cluster property persists. Hence two-edge stars are excluded; the remaining star sizes are one edge or at least three edges. These yield the two listed types.

**Step 3: sufficiency.** For either listed type, take any omitted root edge \(e\). If its endpoints belong to two distinct nontrivial components, an old edge at each endpoint and the new edge \(e\) induce a three-vertex path in the line graph; hence it is no longer a cluster graph. If the endpoints lie in one star with at least three leaves, then \(e\) connects two leaves. The new edge meets the old spoke to one of those leaves and misses a spoke to a third leaf, so again an induced three-vertex path appears. A single edge or a triangle has no missing internal edge. In the exceptional type, an omitted edge from the one isolated vertex to a vertex in a triangle meets two triangle edges but misses the third, again forming an induced three-vertex path. There is no pair of isolated vertices. Thus, no omitted vertex of \(T_n\) can be added in either type. Necessity and sufficiency are proved.

**Step 4: enumeration.** For a block of \(k\) labeled root vertices, a two-vertex edge contributes \(z\) (one choice), a three-vertex triangle contributes \(z^3\) (one choice), and for each \(k\ge4\) a star has \(k\) possible centers and contributes \(z^{k-1}\). The labeled exponential formula for set partitions into these blocks gives the first exponential. The exceptional type has one singled-out isolated vertex and unordered triangle blocks on all remaining vertices; this gives \(t\exp(z^3t^3/6)\). These types do not overlap, proving the displayed generating function.

**Step 5: cardinality spectrum.** A block on \(k\) root vertices contributes at most \(k\) selected edges, with equality precisely for a triangle. Consequently no maximal set has more than \(n\) edges, and \(n\) is attained exactly when \(3\mid n\), using a triangle partition. Otherwise a single star on all \(n\) vertices gives \(n-1\) selected edges for \(n\ge4\). Every full-cover partition into \(b\) admissible blocks has \(n-b\) edges plus one extra edge per triangle block; at most \(\lfloor n/2\rfloor\) blocks occur. For even \(n=2k\ge4\), \(k\) disjoint edge blocks give size \(k\). Replacing any \(r\) edge blocks (\(2\le r\le k\)) by a star on their \(2r\) vertices raises the size by \(r-1\), furnishing each size from \(k\) through \(2k-1\). For odd \(n=2k+1\ge5\), parity forces at least one block of odd order (or the exceptional isolated-vertex type); every maximal set therefore has at least \(k+2\) selected edges. One triangle and \(k-1\) edge blocks attain \(k+2\); replacing any \(r\) of the edge blocks by a star on their \(2r\) vertices raises the size by \(r-1\), giving every size through \(2k=n-1\). The exceptional isolated-vertex family has \(n-1\) edges. The stated spectra follow. For \(n=3\), only the full triangle is maximal. For \(n=4\) the spectrum has two sizes; for \(n=5\) it has only size four; for every \(n\ge6\) the interval has at least two sizes. This proves the purity criterion.

## Verification

A direct C++ implementation constructs \(T_n\) from the edge-intersection rule and tests each of its vertex subsets for having clique connected components; it then tests maximality by attempting to insert each omitted vertex. This uses no component classification to recognize a valid subset. Exhaustive comparison with a separately coded labeled-block recurrence succeeded for each \(3\le n\le7\), examining \(2,131,016\) subsets, of which \(5,012\) were cluster-inducing and \(545\) were inclusion-maximal. The coefficients through \(n=7\) are \(M_3=z^3\), \(M_4=3z^2+8z^3\), \(M_5=15z^4\), \(M_6=15z^3+60z^4+6z^5+10z^6\), and \(M_7=210z^5+217z^6\). The independent Python recurrence agrees on these examples and checks the claimed support and exceptional pure cases through \(n=25\). To reproduce, compile `verify.cpp` with a C++17 compiler and run it, then run `python3 verify.py`. Finite checks do not replace the proof for unbounded \(n\).

## Relationship to prior work

Yixin Cao, *Enumerating Maximal Induced Subgraphs* (first submitted April 21, 2020, arXiv:2004.09885), proves general enumeration algorithms for several hereditary graph classes, including cluster graphs; it does not give a triangular-graph-specific cardinality polynomial or the purity classification here. Dekel Tsur, *Faster parameterized algorithm for Cluster Vertex Deletion* (January 22, 2019, arXiv:1901.07609), addresses the general optimization problem and the induced-three-vertex-path characterization, not an all-cardinality classification for \(T_n\). Caroline Brosse et al., *Efficient enumeration of maximal split subgraphs and induced sub-cographs and related classes* (first submitted July 2, 2020, arXiv:2007.01031), supplies related algorithms for different hereditary classes, not this closed enumerator. These works motivate the structural counting problem without implying this exact result from their stated theorems.

## Limitations

Publication priority is provisional; a differently indexed prior result or database entry may contain an equivalent partition enumerator. No assertion is made about arbitrary line graphs or all minimal cluster-deletion sets beyond the triangular family. The algorithms exhaust only the indicated finite orders. An independent mathematical audit has not been performed.

## References

1. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885 (2020); published in ESA 2023. https://arxiv.org/abs/2004.09885
2. D. Tsur, *Faster parameterized algorithm for Cluster Vertex Deletion*, arXiv:1901.07609 (2019). https://arxiv.org/abs/1901.07609
3. C. Brosse, A. Lagoutte, V. Limouzy, A. Mary, and L. Pastor, *Efficient enumeration of maximal split subgraphs and induced sub-cographs and related classes*, arXiv:2007.01031 (2020). https://arxiv.org/abs/2007.01031
