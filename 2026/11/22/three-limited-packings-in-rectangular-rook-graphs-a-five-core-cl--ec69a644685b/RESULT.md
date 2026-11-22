# Three-limited packings in rectangular rook graphs: a five-core classification

## Finding

Let \(m,n\geq 3\), and let \(G_{m,n}=K_m\square K_n\) be the labelled rook graph with cells indexed by a row and a column. A *three-limited packing* is a vertex subset \(S\) such that \(|S\cap N[v]|\leq 3\) at every vertex \(v\), with closed neighborhoods. Write \(P_{m,n}(z)=\sum_S z^{|S|}\), summing over all such labelled subsets.

Every admissible \(S\), viewed as an edge set in \(K_{m,n}\), belongs to **exactly one** of the following families:

1. A bipartite star forest with each component a single edge or a two-edge star, all nonsingleton stars centered on the same shore. A matching belongs to this family in both orientations but is counted only once.
2. A single three-edge star and no other edges.
3. A single three-edge path on four vertices together with any matching on the unused vertices.
4. A single four-edge path on five vertices together with any matching on the unused vertices.
5. A single four-cycle together with any matching on the unused vertices.

Here a path or cycle is a component of the selected-edge graph, not necessarily an induced component of the ambient complete bipartite graph. The five families are disjoint as *sets*, and their union is all three-limited packings.

For nonnegative integers \(a,b\) define the rook matching polynomial
\[
M_{a,b}(z)=\sum_{j=0}^{\min(a,b)}\binom aj\binom bj j!\,z^j,
\]
and the oriented two-star-forest polynomial
\[
R_{a,b}(z)=\sum_{\substack{p,q\geq0\\p+q\leq a\\2p+q\leq b}}
\frac{a!b!}{p!q!(a-p-q)!\,2^p(b-2p-q)!}\,z^{2p+q}.
\]
Then the entire labelled counting polynomial is
\[
\begin{aligned}
P_{m,n}(z)={}&R_{m,n}(z)+R_{n,m}(z)-M_{m,n}(z)\\
&+\left[m\binom n3+n\binom m3\right]z^3\\
&+4\binom m2\binom n2 z^3 M_{m-2,n-2}(z)\\
&+m\binom n2(m-1)(m-2)z^4M_{m-3,n-2}(z)\\
&+n\binom m2(n-1)(n-2)z^4M_{m-2,n-3}(z)\\
&+\binom m2\binom n2z^4M_{m-2,n-2}(z).
\end{aligned}
\]
In particular, writing \(s=\min(m,n)\) and \(\ell=\max(m,n)\), the maximum packing number is
\[
\boxed{L_3(K_m\square K_n)=\max\{s+2,\min(2s,\ell)\}.}
\]
Equivalently this equals \(s+2\) for \(s\leq\ell\leq s+2\), equals \(\ell\) for \(s+2\leq\ell\leq2s\), and equals \(2s\) for \(\ell\geq2s\); the formulas agree at their boundaries. When \(\ell\geq2s\) and \(s\geq3\), all maximum packings consist of two edges on each of the \(s\) rows with distinct column endpoints; the number of maxima is \(\ell!/[2^s(\ell-2s)!]\).

## Assumptions and scope

All graphs are finite, simple and labelled; each cell is distinguished by its row and column index. Only *closed*-neighborhood three-limited packings are considered. No maximum- or maximality-condition is imposed when defining the all-set polynomial. The theorem is for all integers \(m,n\geq3\), without a balance restriction. A polynomial coefficient counts distinct subsets of cells, not isomorphism classes.

## Proof

Identify each selected cell \((i,j)\) with the corresponding edge \(ij\) of the complete bipartite graph, and let \(H\) be the selected-edge subgraph. Let \(d_i\) and \(e_j\) be the selected row and column degrees. The closed rook neighborhood of cell \((i,j)\) contains precisely
\[
d_i+e_j-\mathbf1_{\{ij\in E(H)\}}
\]
selected cells. Thus admissibility is equivalent to this expression being at most three for every row-column pair, including *unselected* cells.

If \(H\) is nonempty, put \(r=\max_i d_i\) and \(c=\max_j e_j\). Taking a row of degree \(r\) and column of degree \(c\) shows that \(r+c\leq4\). If \(r+c\leq3\), either \((r,c)=(1,1),(2,1),(1,2)\), which are respectively matchings or oriented unions of two-stars and single edges. Conversely each such graph is admissible by the neighborhood formula.

If \(r+c=4\), **every intersection of a maximum-degree row with a maximum-degree column must be selected**; otherwise its rook neighborhood contains four selected cells. Conversely, that complete rectangle of intersections makes all maximum-degree-pair cells safe; all other degree sums are at most three. Thus the full condition is necessary and sufficient.

There are three possibilities, up to interchanging shores. For \((r,c)=(3,1)\), every column of positive degree is maximum-degree; all must meet each degree-three row. Since the columns have degree one, all three edges lie in that row and no other edges exist. This is the isolated three-star family.

For \((r,c)=(2,2)\), let \(a\) be the number of degree-two rows and \(b\) the number of degree-two columns. Both are at least one. The complete intersection forces \(a\leq2\) and \(b\leq2\). If \((a,b)=(1,1)\), the distinguished selected degree-two vertices are adjacent and their remaining endpoints have degree one, forming a three-edge path. If \((a,b)=(1,2)\) or \((2,1)\), the distinguished component is a four-edge path; the two exterior endpoints must be different, otherwise an additional degree-two vertex would arise. If \((a,b)=(2,2)\), the distinguished component is a four-cycle. In each case every other positive-degree vertex has degree one, and its edge joins two vertices outside the distinguished component: hence those remaining edges are a disjoint matching. The component decomposition is unique and exhaustive. Conversely each listed configuration passes the degree-sum condition, so the classification is an equivalence.

To count, choose \(p\) labelled centers of two-stars on a designated shore, \(q\) labelled centers of single edges, and \(2p+q\) distinct opposite-shore vertices, with unordered pairs for the stars. This gives the summand of \(R_{a,b}\). Adding the two orientations counts the matching family twice, corrected by subtracting \(M_{m,n}\). Three-stars have \(m\binom n3+n\binom m3\) placements.

A three-edge path occupies two rows and two columns and is one of the four ways to delete an edge from the corresponding complete \(2\)-by-\(2\) block; its untouched rows and columns support \(M_{m-2,n-2}\). A four-edge path with central vertex on the row shore occupies three distinct rows and two columns: choose its central row, its pair of columns, and an ordered pair of distinct other rows, giving \(m\binom n2(m-1)(m-2)\), followed by \(M_{m-3,n-2}\). Interchanging shores gives the other term. A four-cycle chooses two rows and two columns and supports \(M_{m-2,n-2}\) outside. These disjoint counts prove the displayed polynomial.

Assume \(m=s\leq n=\ell\). Oriented two-star forests attain at most \(\min(2s,\ell)\), realized by assigning distinct columns to rows with row occupancy at most two; the reverse orientation attains at most \(s\). The isolated three-star attains three. A three-edge path plus matching and either four-edge path orientation attain at most \(s+2\), while a four-cycle plus matching attains \(s+2\) exactly, by matching all remaining \(s-2\) rows into remaining columns. Consequently the maximum is \(\max\{s+2,\min(2s,\ell)\}\). For \(\ell\geq2s\) the maximum \(2s\) is strictly greater than \(s+2\) when \(s\geq3\), except \(s=2\), which is excluded. Therefore only row-centered two-star forests can maximize, with every row incident to exactly two edges and no column repeated. Assigning two of \(\ell\) distinct columns to every row, unordered within each row, gives the stated factorial count.

## Verification

The accompanying `verify_formula.py` calculates the stated expression using exact integer arithmetic and independently enumerates all cell subsets on boards through \(4\)-by-\(5\), testing every closed neighborhood directly. The separate C++ `verify_direct.cpp` checks all subsets through \(4\)-by-\(6\), including boundary cases of the aspect-ratio phase transition. The `verify_shapes.py` program reconstructs the selected-edge connected components independently and checks that no valid small-board subset violates the classification. The text files `formula_output.txt`, `direct_output.txt`, and `shapes_output.txt` record actual outputs. These checks confirm finite instances only; the unrestricted result is established by the degree-sum argument above.

For example, the polynomial for \(K_4\square K_4\) is \(1+16z+120z^2+560z^3+1284z^4+1008z^5+72z^6\), and the corresponding one for \(K_3\square K_3\) is \(1+9z+36z^2+84z^3+81z^4+9z^5\).

## Relationship to prior work

The notion of limited packing predates this work. Ahmadi, Soltankhah and Samadi's 2023 paper develops two-limited-packing partitions and duality; Ahmadi and Soltankhah's 2024 preprint proves general product bounds for two-limited and two-total-limited packings. Neither provides this three-limited, labelled rook-board classification or generating polynomial. The full-text comparison was directed at the definitions, product sections and theorem statements. Related rook-graph results concerning three-independent sets count a different property: bounding degrees of the *selected induced subgraph* does not impose the closed-neighborhood condition here. No priority claim is made beyond the distinctions supported by the checked sources; other unpublished or unindexed calculations may exist.

## Limitations

This exact result concerns only two-factor Cartesian products of complete graphs at capacity three. It does not solve the general capacity-\(k\) problem, identify optimal exchange-graph structure, or determine arbitrary graph-product packing polynomials. Computational results cannot independently certify the infinite family. Historical priority has not been independently audited.

## References

1. A. S. Ahmadi, N. Soltankhah and B. Samadi, *Limited packings: related vertex partitions and duality issues*, arXiv:2308.16837v1, made public 2023-08-31. https://arxiv.org/abs/2308.16837
2. A. S. Ahmadi and N. Soltankhah, *On k-(total) limited packing in graphs*, arXiv:2405.03237v1, made public 2024-05-06. https://arxiv.org/abs/2405.03237
3. P. N. Balister, B. Bollobás and K. Gunderson, *Limited packings of closed neighbourhoods in graphs*, arXiv:1501.01833v1, made public 2015-01-08. https://arxiv.org/abs/1501.01833
