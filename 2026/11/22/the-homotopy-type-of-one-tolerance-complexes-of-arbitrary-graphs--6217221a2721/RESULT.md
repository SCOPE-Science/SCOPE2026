# The homotopy type of one-tolerance complexes of arbitrary graphs

## Finding
Let \(G\) be any finite simple graph on \(n\ge2\) vertices, regarded **strictly as a one-dimensional simplicial complex** \(K(G)\): graph three-cycles are not filled in the input. Let \(c\) be the number of connected components, \(m\) the number of graph edges, \(d(v)\) the vertex degrees, and \(\tau\) the number of unordered three-cycles. Define
\[
s=(n-2)m-\sum_{v\in V(G)}\binom{d(v)}2+\tau,\quad
b_1=\binom{c-1}{2},\quad
b_2=s-\binom{n-1}{2}+\binom{c-1}{2}.
\]
Then \(b_2\) is a nonnegative integer, and the **integral homotopy type** of the one-tolerance complex is
\[
\boxed{\mathcal T_1(K(G))\simeq\left(\bigvee^{b_1}S^1\right)\vee\left(\bigvee^{b_2}S^2\right).}
\]
An empty wedge is a point. In particular, the fundamental group is free of rank \(b_1\), all integral homology groups are torsion-free, and there is no reduced homology above degree two.

This is an all-graph statement: it does not assume that \(G\) is connected, triangle-free, chordal, a tree, or a clique graph. It concerns the specified one-dimensional input, not the flag clique complex of \(G\) if \(G\) has triangles.

## Assumptions and scope
For a simplicial complex \(K\) on a fixed vertex set \(V\), the one-tolerance complex \(\mathcal T_1(K)\) consists of those subsets \(\sigma\subseteq V\) for which deleting at most one element leaves a face of \(K\). Every pair of distinct vertices is a face of \(X=\mathcal T_1(K(G))\), and a triple is a face precisely when it contains an edge of \(G\). No set of size four is a face because \(K(G)\) is one-dimensional. Thus \(X\) has the full complete-graph one-skeleton, with exactly \(s\) triangular faces.

For comparison, if \(n\ge4\), then
\[
\mathcal T_1(K(C_n))\simeq\bigvee^{\,n(n-3)/2-1}S^2.
\]
For the path \(P_n\) with \(n\ge3\), the answer is \(\bigvee^{(n-2)(n-3)/2}S^2\), while for the star \(K_{1,n-1}\), the answer is contractible. Hence even among contractible one-dimensional input complexes on the same number of vertices, tolerance can distinguish path and star topology by an unbounded number of two-spheres.

## Proof
**1. Count triangles.** Summing \(n-2\) choices of a third vertex over each original graph edge counts each triple according to the number of edges it spans in \(G\). Subtracting \(\sum_v\binom{d(v)}2\) removes its unordered pairs of edges. A triple with one or two graph edges is then counted once; a triple with three graph edges is counted zero and must be restored once. Thus the number of triangles of \(X\) is exactly \(s\).

**2. An explicit acyclic matching.** Fix a spanning forest of \(G\), one rooted tree in each connected component, with roots \(r_0,\ldots,r_{c-1}\). Choose a total vertex order with all roots first, then the other vertices in a parent-before-child order. Denote the parent of a nonroot vertex \(v\) by \(p(v)\). The following pairs of *nonempty* faces of \(X\) define a discrete-Morse matching.

First match every nonroot vertex \(\{v\}\) to the edge \(\{v,p(v)\}\), and every root \(\{r_i\}\), \(i>0\), to \(\{r_0,r_i\}\). Then, for each edge \(\{u,v\}\) of the complete one-skeleton, write \(u<v\) in the chosen total order. If \(v\) is a nonroot and \(u\neq p(v)\), match this edge to the triangle \(\{u,v,p(v)\}\). This triangle belongs to \(X\) because \(vp(v)\) is an edge of the forest.

No simplex participates twice: the edge-to-triangle pairing uses the greatest vertex \(v\) of the triangle, with \(p(v)\) one of the other two vertices, and so cannot produce the same triangle from a second edge. The two classes of pairs use disjoint edges; vertex pairs also are disjoint. A dimension-zero gradient path strictly decreases the total vertex order, since it follows either a parent edge or a root-to-\(r_0\) edge. A dimension-one gradient path from \(\{u,v\}\) through its matched triangle can continue, if at all, only through \(\{u,p(v)\}\), whose greatest vertex is strictly smaller than \(v\); the other alternative is a forest edge paired with a vertex, not with a triangle. Hence no closed gradient path exists.

The unique critical vertex is \(r_0\). The critical edges are precisely edges \(\{r_i,r_j\}\) with \(1\le i<j<c\), giving \(\binom{c-1}2\) critical one-cells. All other edges are used in one of the two matching classes. Therefore the number of critical two-cells is
\[
s-\left[\binom n2-(n-c)-\binom c2\right]
=s-\binom{n-1}2+\binom{c-1}2=b_2.
\]
In particular \(b_2\ge0\). Discrete Morse theory produces a CW complex with exactly one zero-cell, \(b_1\) one-cells and \(b_2\) two-cells, homotopy equivalent to \(X\).

**3. The two-cell attaching maps vanish.** Let \(R\) be the complete one-dimensional graph on the component roots. Mapping each vertex of \(G\) to its component root defines a simplicial retraction \(f:X\to R\), with the inclusion \(R\hookrightarrow X\) as a section: every two-simplex of \(X\) contains two vertices joined by an original graph edge, so its image contains at most two distinct roots.

The retraction induces an isomorphism on fundamental groups. Indeed, whenever \(ab\) is an original graph edge and \(w\) is a third vertex, the triangle \(abw\) permits an edge path with endpoint \(a\) to slide to one with endpoint \(b\), while inserting the original edge \(ab\). Sliding endpoints along the fixed forest paths moves every edge of every loop to an edge of the root graph, up to conjugating endpoint paths; the original forest loops themselves collapse by the same triangle relations. Thus the section is surjective on fundamental groups; since it is a section of the retraction, it is also injective. Consequently
\[
\pi_1(X)\cong\pi_1(R)\cong F_{\binom{c-1}{2}}.
\]
Under the stated matching, all tree edges and the root-star edges are contracted, while the surviving critical one-cells correspond exactly to the non-star edges of \(R\). The induced map of the Morse CW one-skeleton to \(R\) therefore identifies its loop generators with a free basis of \(\pi_1(R)\). Each critical two-cell attaches by a loop which is null-homotopic in \(X\); because the one-skeleton already induces an isomorphism on \(\pi_1\), that attaching loop is null-homotopic in the one-skeleton itself. Replacing all such attaching maps by constant maps yields the asserted wedge of \(b_1\) circles and \(b_2\) two-spheres. All conclusions hold integrally. \(\square\)

## Verification
The included `verify.py` directly constructs the complete one- and two-skeleta, builds the stated face matching, checks uniqueness and face incidence, counts critical cells, and checks mod-two boundary ranks. All 33,866 labeled simple graphs on two through six vertices passed exact counts and boundary-rank comparisons. The *entire directed Hasse graph* was additionally tested for acyclicity for every graph on at most five vertices, and for paths, stars and cycles of lengths seven through twelve. The `verify_output.txt` records the actual results. These finite checks verify the implementation and sample cases; the arbitrary-size and integral homotopy claims follow from the preceding explicit acyclic matching and attaching-map proof, not from enumeration.

## Relationship to prior work
The tolerance construction originates in Kim and Lew's work on Leray numbers; their 2023 paper establishes general Leray estimates and includes the familiar example of two disjoint edges, whose one-tolerance complex is a two-sphere. Selvaraja's November 2026 work gives broad collapsibility, Leray, and symbolic-power results, notably bounds for chordal clique complexes and top-dimensional nonvanishing under hypotheses. Those results are not claimed as new here, and neither gives the present two-degree integral homotopy classification for every one-dimensional input graph or the connected-component formula for its fundamental group. The proof here is topological, through an explicit global Morse matching and root-graph retraction rather than a Leray bound.

## Limitations
This theorem addresses tolerance parameter exactly one and a simplicial complex of dimension at most one with all original graph vertices retained. It does not classify higher tolerance, the tolerance of a *flag clique complex* when a graph has filled triangles, induced-subcomplex persistent maps, or equivariant homotopy representations. The literature comparison does not prove global uniqueness; unindexed or unpublished independent statements may exist. No independent mathematical audit has been performed.

## References
1. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384v1, first publicly submitted 10 November 2026. https://arxiv.org/abs/2611.14384
2. M. Kim and A. Lew, *Leray Numbers of Tolerance Complexes*, Combinatorica 43 (2023), 985–1006. https://doi.org/10.1007/s00493-023-00044-5
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
