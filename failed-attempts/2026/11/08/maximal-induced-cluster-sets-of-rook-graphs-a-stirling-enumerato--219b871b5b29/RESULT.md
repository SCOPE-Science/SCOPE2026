# Maximal induced cluster sets of rook graphs: a Stirling enumerator and a gap theorem

## Finding

For all integers \(m,n\ge1\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), with one vertex for each cell of an \(m\)-by-\(n\) board, and adjacency in a common row or column. A *cluster set* \(S\subseteq V(R_{m,n})\) is one whose induced subgraph is a disjoint union of cliques; it is *maximal* if no additional vertex can be selected while retaining this property. Let \(M_{m,n}(z)=\sum_{S\text{ maximal cluster}}z^{|S|}\).

Write \(T(u,k)\) for the number of partitions of a labeled \(u\)-element set into exactly \(k\) unlabeled blocks, each of size at least two. Thus \(T(0,0)=1\), \(T(u,0)=0\) when \(u>0\), and \(T(u,k)=0\) when \(u<2k\) or \(k<0\). With \(p=m-a-c\) and \(q=n-b-c\), define

\[
\begin{aligned}
P_{m,n}(z)=\sum_{\substack{a,b,c\ge0\\p,q\ge0}}
\frac{m!n!\,T(q,a)T(p,b)}{c!p!q!}
 z^{m+n-a-b-c}.
\end{aligned}
\]

The complete inclusion-maximal cluster polynomial is

\[
\boxed{M_{m,n}(z)=P_{m,n}(z)
+z^n\sum_{a=1}^{m-1}\frac{m!}{(m-a)!}T(n,a)
+z^m\sum_{b=1}^{n-1}\frac{n!}{(n-b)!}T(m,b).}
\]

In the asymmetric rectangular regime \(2\le m\le n\) and \(n\ge 2m\), the set of exponents with nonzero coefficients is **exactly**

\[
\boxed{\{m\}\ \cup\ \{n,n+1,\ldots,n+m-2\}.}
\]

Therefore there are precisely \(n-m-1\) consecutive missing cardinalities \(m+1,\ldots,n-1\), unbounded as \(n\) grows with \(m\) fixed. The minimum inclusion-maximal size is \(m\), the maximum is \(n+m-2\). If \(m\ge3\), exactly \(mn\) maximal sets attain the maximum size. These statements concern inclusion-maximal sets, not necessarily maximum-cardinality sets.

## Assumptions and scope

Graphs are finite, labeled, simple, and undirected; the complete bipartite graph \(K_{m,n}\) has distinct labeled shores \(A,B\) of sizes \(m,n\). An induced cluster graph has no induced three-vertex path, equivalently is a disjoint union of complete graphs. An edge set \(F\subseteq E(K_{m,n})\) corresponds to \(S\subseteq V(R_{m,n})\). For an edge set, a *star component* has one center and one or more leaves; a one-edge component is treated separately, with no designated center. A vertex of \(K_{m,n}\) is *covered* if incident with a selected edge. Empty sums are zero. Coefficients of coincident monomials are added. The formula includes the boundaries \(m=1\) or \(n=1\).

## Proof

**1. Cluster-to-star correspondence.** The line graph of the selected edge set \(F\) is a disjoint union of cliques precisely when each connected component of \((A\cup B,F)\) with at least one edge is a star. Indeed, if a connected component of the line graph is a clique, its edges are pairwise intersecting; a pairwise-intersecting set of edges of a simple bipartite graph must have a common endpoint (three edges without a common endpoint would form a triangle). Conversely, a star gives a clique in the line graph. Thus cluster sets correspond exactly to star forests, ignoring isolated vertices of the original bipartite host. Equivalently, a set of cells is a cluster set if and only if it does not contain three corners of any \(2\)-by-\(2\) subboard.

**2. Maximal star forests.** Let \(F\) be a star forest. If each vertex on both shores is covered, then any missing edge links two different star components; its addition joins two previously disjoint edges into one connected component, which cannot be a star. Thus every vertex-covering star forest is maximal. If there are uncovered vertices on both shores, an edge between them can be inserted, so maximality fails. Suppose some \(A\)-vertex is uncovered, but every \(B\)-vertex is covered. Any star centered in \(B\) can be enlarged through an uncovered \(A\)-vertex. Any single-edge component can also be enlarged in that way. Therefore a maximal forest in this case must comprise only stars of at least two edges centered in \(A\), and these must cover all of \(B\). Conversely, every such forest is maximal: adding an edge from an uncovered \(A\)-vertex to a leaf of a selected star produces a nonstar component, while an edge between covered vertices either already belongs to its star or connects two distinct components. The case with uncovered \(B\)-vertices is symmetric. Hence exactly three disjoint maximality types exist: (i) spanning star forests without isolated vertices; (ii) nonspanning \(A\)-centered stars of size at least two covering \(B\); (iii) the symmetric \(B\)-centered type.

**3. Count spanning configurations.** Consider a vertex-covering star forest with \(a\) stars of at least two edges centered in \(A\), \(b\) such stars centered in \(B\), and \(c\) isolated-edge components. Its \(p=m-a-c\) remaining \(A\)-vertices are leaves of the \(b\) \(B\)-centered stars, and its \(q=n-b-c\) remaining \(B\)-vertices are leaves of the \(a\) \(A\)-centered stars. Assigning labeled vertices to these five roles, pairing the two shores of the isolated-edge components, and distributing the leaves into star components yields

\[
\frac{m!}{a!c!p!}\frac{n!}{b!c!q!}\,c!\,a!T(q,a)\,b!T(p,b)
=\frac{m!n!T(q,a)T(p,b)}{c!p!q!}.
\]

Every configuration is counted exactly once because all components of size at least two have uniquely determined centers, while single-edge components have no arbitrary orientation. A star forest with \(a+b+c\) nontrivial components and all \(m+n\) vertices covered has \(m+n-a-b-c\) edges. This gives \(P_{m,n}(z)\).

**4. Count nonspanning configurations.** In type (ii), choose \(a\) labeled centers from \(A\), with \(1\le a<m\), and partition all \(n\) vertices of \(B\) among these centers in blocks of at least two. The count is

\[
\binom ma a!T(n,a)=\frac{m!}{(m-a)!}T(n,a)
\]

and the number of selected edges is \(n\). Type (iii) contributes the symmetric term of size \(m\). Disjointness of the three classes proves the polynomial.

**5. Rectangular gap.** Assume \(2\le m\le n\) and \(n\ge2m\). In a spanning configuration, the number of star components is at most \(m\), because each component contains an \(A\)-vertex. Thus its selected-edge count is at least \(n\). Since \(n>m\), at least one component has its center in \(A\); if there were only one component it could not cover all \(m\ge2\) vertices of \(A\). Hence there are at least two components, so the selected-edge count is at most \(m+n-2\). The two nonspanning classes have sizes exactly \(n\) and \(m\).

All claimed sizes occur: size \(m\) comes from one \(B\)-centered star covering \(A\), leaving unused \(B\)-vertices; size \(n\) comes from \(m\) \(A\)-centered stars with at least two leaves each (possible because \(n\ge2m\)). For \(1\le t\le m-2\), take \(a=m-t-1\), \(b=1\), \(c=0\). Then \(p=t+1\ge2\), \(q=n-1\ge2a\), so this is a spanning star forest of size \(n+t\). If \(m\ge3\), size \(m+n-2\) forces exactly two components; all spanning configurations with this size have \(a=b=1,c=0\) since \(m\ge3,n\ge2m\). There are \(m\) choices for the \(A\)-center and \(n\) choices for the \(B\)-center; all remaining vertices attach uniquely, giving \(mn\) such sets. This completes the proof.

## Verification

The accompanying standalone Python script `verify_cluster_rook.py` constructs a forbidden-triple list directly from \(2\)-by-\(2\) rectangles, independently checks all cell subsets for the absence of induced three-vertex paths, and checks all possible single-cell additions for maximality. It independently computes the Stirling-based coefficient formula using a recurrence on set partitions. Its exhaustive check covers \(14\) labeled rectangular graph instances with \(mn\le20\), examining \(1{,}152{,}910\) subsets. It found \(9{,}545\) cluster sets and \(1{,}539\) inclusion-maximal cluster sets; all coefficients agreed. It also checks the exact rectangular size spectrum for \(2\le m\le8\) and \(2m\le n\le4m\). The algorithm is finite evidence; Steps 1–5 provide the general proof.

Reproduce using `python3 verify_cluster_rook.py` with Python 3.9 or later and no external packages. No computational result is needed for the infinite argument.

## Relationship to prior work

Le and Le (2022) study the cluster vertex deletion problem, equivalently deletion to an induced \(P_3\)-free graph, with a complexity dichotomy on forbidden-induced-subgraph classes. Their results establish the ambient problem but do not give this labeled rook-graph cardinality distribution. Conte et al. (2019/2021) develop algorithms for listing several kinds of maximal induced subgraphs, but do not give this specific closed distribution. Liu and Huang (2010) enumerate general spanning forests of complete bipartite graphs, not the restricted inclusion-maximal star-forest families counted here. OEIS A352211 concerns the *largest* number of maximal induced cluster sets among graphs of a given order, while OEIS A291104 counts maximal *irredundant* rook-graph sets, a different predicate (for instance the latter gives \(48\) at the \(3\)-by-\(3\) rook graph, versus \(21\) maximal cluster sets here).

## Limitations

Only finite simple complete rook graphs \(K_m\square K_n\) are covered; arbitrary Cartesian products, weighted counts, and other vertex-deletion target classes are not claimed. The formula counts labeled subsets, not symmetry orbits. The publication-priority claim is provisional: an unpublished or unindexed equivalent formula cannot be ruled out. The independent mathematical audit has not been performed.

## References

1. Hoang-Oanh Le and Van Bang Le, *Complexity of the Cluster Vertex Deletion Problem on H-Free Graphs*, MFCS 2022, DOI 10.4230/LIPIcs.MFCS.2022.68 (first verified public date 2022-08-22).
2. Alessio Conte, Roberto Grossi, Andrea Marino, Takeaki Uno and Luca Versari, *Proximity Search For Maximal Subgraph Enumeration*, arXiv:1912.13446, initial preprint 2019, version examined 2021.
3. Bolian Liu and Fengying Huang, *Enumeration For No-Trivial Spanning Forests of Complete Bipartite Graphs*, Ars Combinatoria 97 (2010), 289–300.
4. OEIS A352211, *Largest number of maximal node-induced cluster subgraphs of an n-node graph*, and OEIS A291104, *Number of maximal irredundant sets in the n X n rook graph*.
