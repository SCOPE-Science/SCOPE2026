# Exact orientation and minimum-set spectra of total domination on cycle bouquets

## Finding

Let \(r\ge2\) and \(\ell_1,\ldots,\ell_r\ge3\). Let \(B=B(\ell_1,\ldots,\ell_r)\) be the simple graph obtained from otherwise vertex-disjoint cycles of lengths \(\ell_1,\ldots,\ell_r\) by identifying exactly one vertex of every cycle to a common hub. Its order is \(N=1+\sum_{i=1}^r(\ell_i-1)\). An orientation \(D\) is **valid** if every vertex has positive indegree. For a valid orientation, let \(\gamma_t(D)\) be the minimum cardinality of \(S\subseteq V(B)\) such that every vertex has an incoming arc from some vertex of \(S\).

Put \(b=2+\sum_{i=1}^r(\ell_i-3)=N+1-2r\). The complete orientation-score polynomial and the orientation–optimal-set-pair polynomial are, respectively,

\[
A_B(z)=\sum_{D\,\mathrm{valid}}z^{\gamma_t(D)}=z^b\left(\prod_{i=1}^r(\ell_i-1+2z)-\prod_{i=1}^r(\ell_i-1)\right)
\]

and

\[
T_B(z)=\sum_{D\,\mathrm{valid}}\ \sum_{\substack{S\text{ is a minimum directed total}\\\text{dominating set of }D}} z^{|S|}
=z^b\,z\frac{d}{dz}\left(\prod_{i=1}^r(2(\ell_i-2)+2z)\right).
\]

Thus every integer in \([b+1,b+r]\) occurs as \(\gamma_t(D)\), and \(\mathrm{dom}_t(B)=N+2-2r\), \(\mathrm{DOM}_t(B)=N+1-r\). The number of valid orientations is \(\prod_i(\ell_i+1)-\prod_i(\ell_i-1)\). On the friendship graph with \(r\) triangular petals, the two polynomials reduce to

\[
A_B(z)=2^rz^2\big((1+z)^r-1\big),\qquad
T_B(z)=r2^rz^3(1+z)^{r-1}.
\]

## Assumptions and scope

The cycles are labelled by their edges and share exactly one vertex; no other pair of vertices or edges is identified. Each orientation of each labelled edge is counted separately. The variable \(z\) records the directed total-domination number, not the number of edges reversed. A valid orientation is exactly one admitting a directed total dominating set, because every vertex must have a positive indegree. Only minimum-cardinality sets contribute to \(T_B(z)\), and the same set is counted separately for distinct orientations. No assumption that the petals have equal lengths is made.

## Proof

Number the vertices in petal \(i\) as \(v=x_0,x_1,\ldots,x_{\ell_i-1},x_{\ell_i}=v\) around the cycle. Mark each edge by \(+\) if it points forward in this order and by \(-\) otherwise. A nonhub vertex \(x_j\) has indegree zero precisely when its two adjacent edge signs are \((-,+)\). Therefore all nonhub vertices have positive indegree if and only if the sequence of signs, treated as a linear sequence cut at the hub, is

\[
+^a-^{\ell_i-a},\qquad 0\le a\le\ell_i.
\]

The two extreme cases \(a=0\) and \(a=\ell_i\) are directed cycles. Each of the other \(\ell_i-1\) cases consists of two directed paths leaving the hub and meeting at an internal sink. Only a directed-cycle petal sends an arc into the hub. Thus a global orientation is valid if and only if every petal has one of these \(\ell_i+1\) forms and at least one petal is a directed cycle. Let \(c\) be the number of directed-cycle petals; necessarily \(1\le c\le r\).

The hub must lie in every directed total dominating set: an internal vertex immediately after the hub on an outward path has the hub as its unique in-neighbor, in every permitted petal type. Consider a cyclic petal oriented \(v\to x_1\to\cdots\to x_{\ell_i-1}\to v\) (the reverse case is symmetric). To dominate all of its internal vertices, the set must contain \(v,x_1,\ldots,x_{\ell_i-2}\). Hence it requires exactly \(\ell_i-2\) internal chosen vertices, apart from an optional final vertex \(x_{\ell_i-1}\) that can dominate the hub. No other internal vertex in this cyclic petal can dominate the hub.

For a noncyclic petal, the two outward paths from the hub have edge lengths \(a\) and \(\ell_i-a\), where \(1\le a\le\ell_i-1\). Every internal non-sink vertex has a unique in-neighbor. These force all necessary internal predecessors. The sink has the two path predecessors as in-neighbors, except that if a branch has length one its predecessor is the already selected hub. Thus exactly \(\ell_i-3\) internal vertices suffice and are necessary. When \(a=1\) or \(a=\ell_i-1\), the local minimum choice is unique; when \(2\le a\le\ell_i-2\), it has exactly two choices (select one of the two sink predecessors). The conclusion also holds at the boundary \(\ell_i=3\): only the two one-edge-branch arrangements occur.

Across all petals, the internal lower bound without dominating the hub is

\[
\sum_i(\ell_i-3)+c.
\]

Exactly one extra internal vertex must be chosen among the \(c\) cyclic-petal predecessors of the hub. It cannot be replaced by a vertex from a noncyclic petal, since those petals have no inward arc to the hub. Consequently

\[
\gamma_t(D)=1+\sum_i(\ell_i-3)+c+1=b+c.
\]

This lower bound is attained by making the specified forced local choices and choosing one of the \(c\) incoming predecessors of the hub. The minimum sets are therefore counted by \(c\) multiplied by the independent local choices for noncyclic petals.

For \(A_B\), the weight of a noncyclic petal is \(\ell_i-1\) and that of a cyclic petal is \(2z\). Multiply the factors \(\ell_i-1+2z\), delete the term with \(c=0\), and multiply by \(z^b\). For \(T_B\), noncyclic orientations weighted by their number of local minimum choices contribute

\[
2\cdot1+(\ell_i-3)\cdot2=2(\ell_i-2),
\]

while cyclic orientations contribute \(2z\). The operation \(z\frac{d}{dz}\) multiplies each term containing \(c\) cyclic petals by exactly the required factor \(c\) and automatically deletes the \(c=0\) term. Multiplication by \(z^b\) completes the second identity.

Each factor has a strictly positive coefficient for a cyclic petal and for a noncyclic petal, so all \(c=1,\ldots,r\) are attained, proving the interval spectrum and extremal formulas. Evaluation of \(A_B\) at \(z=1\) gives the count of valid orientations. Substitution \(\ell_i=3\) for all \(i\) gives the friendship-graph formulas. \(\square\)

## Verification

The accompanying `verify_bouquet.py` uses only the Python standard library. It constructs each labelled graph independently, enumerates all orientations of its edges, checks indegree positivity, and independently minimizes directed total domination by enumerating all vertex subsets. It records both the distribution of minima and the number of minimum sets per orientation and checks both against the two formulas. Executing `python3 verify_bouquet.py` gives `VERIFY_OK profiles 14 valid_orientations 424 all_signed_edge_orientations_and_directed_total_domination=PASS minimum_set_enumerator=PASS`. The checked cycle-length tuples include one-petal controls, unequal two-petal cases, and three-petal cases. These are finite checks, not a substitute for the proof for arbitrary \(r\) and \(\ell_i\).

## Relationship to prior work

Hansen, Lai, and Yue (1999) introduced open orientable domination and gave foundational extremal and orientation-spectrum observations. Anderson, Dravec, Johnston, and Kuenzel (arXiv:2311.16307v1, first public 27 November 2023) study orientable total domination and include an exact unicyclic result and results for complete bipartite graphs and grids, but no orientation-score or minimum-set enumerator for multi-cycle bouquets. Blázsik and Nagy (arXiv:2411.04560, first public 7 November 2024) address the global extremal case of upper orientable total domination equal to graph order minus one, which can include the two-petal upper-bound specialization here; that scalar case is not asserted to be new. The distinctive claim here is the complete two-polynomial orientation/minimum-set distribution for every bouquet with at least two petals, including unequal lengths.

## Limitations

This theorem applies only to cycles intersecting in exactly one common vertex and counts labelled-edge orientations. It does not assert the same formulas for arbitrary cactus graphs, other intersection patterns, or ordinary undirected total domination. The independently enumerated cases do not constitute an infinite proof. Despite targeted literature and research-record comparisons, equivalent results under older open-orientable-domination terminology or a general block-gluing principle may remain unindexed; publication priority needs external scrutiny. No independent mathematical audit was performed.

## References

1. L. Hansen, Y.-L. Lai, and B. Q. Yue, "Orientable Open Domination of Graphs," *Journal of Combinatorial Mathematics and Combinatorial Computing* 29 (1999), 159–181. https://combinatorialpress.com/article/jcmcc/Volume%20029/vol-029-paper%2013.pdf
2. S. E. Anderson, T. Dravec, D. Johnston, and K. Kuenzel, "Orientable total domination in graphs," arXiv:2311.16307v1 (first public 2023-11-27). https://arxiv.org/html/2311.16307v1
3. Z. L. Blázsik and L. V. Nagy, "Characterization of graphs with orientable total domination number equal to \(|V|-1\)," arXiv:2411.04560 (first public 2024-11-07). https://arxiv.org/abs/2411.04560
