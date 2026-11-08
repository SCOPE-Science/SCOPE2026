# A seven-column transition and connected edge-metric basis mobility in complete prisms

## Finding
For each integer \(n\ge2\), let \(G_n=K_n\square K_2\), with vertices \((a,i)\), \(a\in\{0,1\}\), \(i\in[n]\). Vertices are adjacent when they occupy the same clique layer with different column labels, or occupy opposite layers in the same column. Under the vertex-to-edge distance \(d(v,xy)=\min\{d(v,x),d(v,y)\}\), the edge metric dimension is
\[
\operatorname{edim}(G_n)=\begin{cases}n,&2\le n\le6,\\n-1,&n\ge7.\end{cases}
\]
For every \(n\ge7\), an edge-metric basis is **exactly** a set containing one vertex from each of \(n-1\) columns, none from the remaining column, and at least three selected vertices in each clique layer. Hence the number of bases equals
\[
B_n=n\sum_{k=3}^{n-4}\binom{n-1}{k}
=n\left(2^{n-1}-2-2(n-1)-2\binom{n-1}{2}\right).
\]
The graph of these bases under token sliding (replace one selected vertex by an adjacent unselected vertex while retaining a basis) is connected, and therefore so is its token-jump supergraph. At \(n=7\), the slide and jump graphs coincide and are connected, six-regular graphs on \(140\) vertices (and hence have \(420\) edges).

## Assumptions and scope
The graph is finite, simple, undirected, and has all two-layer clique and matching edges stated above. A set \(S\subseteq V(G_n)\) is an edge-metric resolving set when the vectors of distances from all edges to \(S\) are pairwise distinct. An edge-metric basis has minimum cardinality. Token jumping permits any one-vertex exchange between bases; token sliding permits such an exchange only across an edge of \(G_n\). Vertices within each layer and columns are labeled for counting, and every basis is counted as an unordered vertex subset.

## Proof
Write \(R_j\) for the matching edge in column \(j\), and \(H_{a,\{i,j\}}\) for the edge between columns \(i\) and \(j\) in layer \(a\). For every landmark \((b,k)\), direct distances in the Cartesian product give
\[
 d((b,k),R_j)=1-\mathbf1_{k=j},\qquad
 d((b,k),H_{a,X})=1-\mathbf1_{k\in X}+\mathbf1_{b\ne a},\quad |X|=2.
\]
These equations also hold for \(n=2\). They are the starting point for all comparisons; no appeal to finite data is needed for the infinite statement.

**Lower bound.** Two different matching edges \(R_i,R_j\) have equal distances to every vertex outside columns \(i,j\). Thus an edge-resolving set must meet at least \(n-1\) columns, and must contain at least \(n-1\) vertices.

**All size-\(n-1\) candidates.** If a set has exactly \(n-1\) vertices and resolves, it has one vertex in each column except for a unique missing column \(c\). Let \(A\) and \(B\) be its occupied column labels in layers zero and one respectively. Then \(A\sqcup B=[n]\setminus\{c\}\). We show it resolves exactly when \(|A|,|B|\ge3\).

For necessity, suppose \(|A|\le2\). If \(|A|=2\), then the rung \(R_c\) and the layer-one edge \(H_{1,A}\) have equal distances to every selected vertex: both distances equal one. If \(|A|=1\), with \(A=\{p\}\), replace the horizontal edge by \(H_{1,\{p,c\}}\); again both edges have distance one to every selected vertex. If \(A=\varnothing\), choose any occupied column \(p\) and compare \(R_p\) and \(H_{1,\{p,c\}}\): their distances agree at the selected vertex of column \(p\) (zero) and at all others (one). The case \(|B|\le2\) follows by exchanging layers. Therefore both layer counts must be at least three.

For sufficiency assume \(|A|,|B|\ge3\). Any two rungs are distinguished because the chosen columns omit only \(c\). Any two different clique edges in the *same* layer, say \(H_{a,X},H_{a,Y}\), are distinguished since their distance difference at any selected column \(k\) is \(\mathbf1_{k\in Y}-\mathbf1_{k\in X}\); distinct two-element subsets cannot have identical membership on \([n]\setminus\{c\}\). If a rung \(R_j\) and a clique edge \(H_{a,X}\) had the same selected distances, then at every landmark in the opposite layer, equality of \(1-\mathbf1_{k=j}\) and \(2-\mathbf1_{k\in X}\) would force \(k\in X\) and \(k\ne j\). But the opposite layer has at least three selected columns and \(|X|=2\). Finally, if \(H_{0,X}\) and \(H_{1,Y}\) were indistinguishable, comparing at layer-zero landmarks would force every \(k\in A\) to lie in \(Y\setminus X\), impossible because \(|A|\ge3\) while \(|Y|=2\). These exhaust all edge-pair types. The size-\(n-1\) characterization is proved.

**Threshold and count.** Both layer counts can be at least three with \(|A|+|B|=n-1\) exactly when \(n\ge7\). Thus for \(2\le n\le6\), the lower bound \(n-1\) is unattainable. The entire layer \(S_0=\{(0,j):j\in[n]\}\) resolves all edges: on this set the distance signatures are \(R_j\) with a unique zero at \(j\), \(H_{0,X}\) with zeros precisely on \(X\), and \(H_{1,X}\) with ones precisely on \(X\) and twos elsewhere. These are distinct for \(n\ge2\). Therefore \(\operatorname{edim}=n\) for \(2\le n\le6\) and equals \(n-1\) for \(n\ge7\). To count minimum sets for \(n\ge7\), choose the missing column in \(n\) ways and which \(k\) of the other \(n-1\) labels use layer zero, with \(3\le k\le n-4\). This yields the displayed formula.

**Token-slide connectivity.** Fix a basis, its missing column \(c\), and its layer-zero population \(k\). A token in occupied column \(i\) can slide within its own clique layer into the empty column \(c\), making \(i\) the new empty column without changing layer populations. Thus the empty column can be placed at any desired label. To interchange the layer assignments of two occupied columns \(i,j\) of opposite layers while keeping \(c\) missing, perform three legal slides: move the token in \(i\) to \(c\) in its layer; move the token in \(j\) to the now-vacant \(i\) in its layer; move the token at \(c\) into the now-vacant \(j\). These exchanges generate all assignments with the same missing column and population \(k\), always preserving the minimum of three in each layer. Hence all bases with fixed population are slide-connected.

If \(k<n-4\), the opposite layer has at least four tokens; switching any such token along its matching (vertical) edge increases \(k\) by one and leaves both populations at least three. Reversing this operation decreases \(k\) whenever \(k>3\). Thus every allowable population is connected to every other by slides. The entire slide graph is connected. At \(n=7\) every basis has exactly three selected vertices in each layer. The only legal one-vertex exchanges move an occupied token in its own layer to the unique empty column, giving exactly six moves; no exchange can change its layer because that would create a two-versus-four split. Every jump is therefore a slide, giving the claimed six-regular graph.

## Verification
The independent program `verify_direct.py` enumerates all vertex subsets of cardinalities \(n-1\) and \(n\) as appropriate for \(2\le n\le9\). It computes vertex-to-edge distances from the adjacency geometry and tests actual edge signatures, confirming all minimum sizes and every predicted minimum configuration for \(n=7,8,9\). It gives counts \(140,560,1638\) in these three cases. It also finds exactly \(4,14,50,182,532\) minimum sets for \(n=2,3,4,5,6\), respectively; these last values are checks, not a separate all-parameter counting claim.

A second program, `verify_structural.py`, independently generates the classified bases and constructs their token-jump and token-slide graphs for \(7\le n\le10\). All the graphs are connected. For \(n=7\) both move models produce \(140\) states, \(420\) undirected transitions, and degree six at every state. The programs are standalone, require only standard Python, and have outputs embedded alongside them. Their finite checks corroborate, rather than substitute for, the all-parameter proofs.

## Relationship to prior work
Kelenc, Tratnik and Yero introduced vertex-to-edge metric dimension in arXiv:1602.00291v1 (first public date 2016-01-31), and studied among other families complete graphs, complete bipartite graphs and Cartesian grids; their inspected sections do not give a complete-clique-prism basis classification. Zubrilina, *On Edge Dimension of a Graph*, arXiv:1611.01904 (first public 2016-11-07), Theorem 4.2 gives a general one-unit interval for the edge dimension of Cartesian products with paths in terms of a union of vertex and edge bases. Its interval does not classify the complete-prism bases, count them or determine their reconfiguration, and the manuscript contains no complete-prism specialization.

A published mathematical research record, *Mixed metric bases of complete prisms* (October 2026), proves that for \(n\ge5\) the **mixed** metric bases have size \(n\), are matching transversals with at least two vertices in either layer, and number \(2^n-2n-2\). Mixed resolving sets distinguish vertices as well as edges; they are a strictly stronger requirement. In particular, this known mixed metric formula neither implies nor contradicts the present edge-only minimum of \(n-1\) for \(n\ge7\). It supplies a nearby contrast, not a novelty claim for mixed metric dimension. No equivalent exact edge-only basis enumeration or minimum-basis sliding theorem was identified in the searches described in the review, but incomplete indexing prevents an absolute priority guarantee.

## Limitations
The theorem concerns exactly two complete clique layers with a perfect matching, not arbitrary Cartesian products or the ordinary cycle prisms. The integer range \(n\ge2\) is exact, and the basis enumeration and mobility characterization are asserted for \(n\ge7\). No statement about exact reconfiguration diameters for general \(n\) is established. Search coverage is finite; an unindexed earlier result could duplicate part of the theorem. Independent scholarly validation is not claimed here.

## References
1. A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1, first posted 2016-01-31, DOI:10.1016/j.dam.2018.05.052.
2. N. Zubrilina, *On Edge Dimension of a Graph*, arXiv:1611.01904v1, first posted 2016-11-07, particularly Theorem 4.2.
3. *Mixed metric bases of complete prisms*, published mathematical research record dated 2026-10-04, record suffix `2c5387cbdbd0` (mixed, not edge-only, metric dimension).
