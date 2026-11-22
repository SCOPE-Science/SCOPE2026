# Sharp odd girth of optimum decycling-set slides on Möbius ladders

## Finding
For every integer \(n\ge3\), let \(M_{2n}\) be the cubic Möbius ladder on \(2n\) vertices: a cycle of length \(2n\) with antipodal matching edges. A *minimum feedback vertex set* (minimum decycling set) is a vertex set of smallest cardinality whose deletion leaves a forest. Let \(R_n\) be the graph of all minimum feedback vertex sets, where two configurations are adjacent precisely when one selected vertex is slid across an edge of \(M_{2n}\) to an unselected vertex and the resulting set remains minimum.

**Theorem.** The shortest odd cycle in \(R_n\) has length
\[
\operatorname{og}(R_n)=
\begin{cases}
\infty,&n\text{ odd},\\
n+1,&n\text{ even and }n\ge4.
\end{cases}
\]
Here \(\operatorname{og}=\infty\) means that the graph is bipartite, including the possibility of isolated vertices. In particular, every even-width Möbius ladder admits a shortest *odd* closed relocation cycle of minimum-size feedback vertex sets, and the number of necessary slides is exactly one more than its rung count. The theorem does not assert that the entire reconfiguration graph is a single cycle or classify all its components.

## Assumptions and scope
All graphs are simple undirected labelled graphs; a legal move changes exactly one selected vertex to a distinct adjacent unselected vertex. The vertex count of \(M_{2n}\) is \(2n\), whereas its rung count is \(n\). An odd cycle is a simple odd cycle in the configuration graph, not a closed walk with repeated configurations. Odd girth is infinite for bipartite graphs. For even \(n=2m\ge4\), write the vertices as \(a_0,\ldots,a_{n-1}\) and \(b_0,\ldots,b_{n-1}\), with rungs \(a_ib_i\), ordinary rail edges \(a_ia_{i+1}\) and \(b_ib_{i+1}\) for \(0\le i<n-1\), and twisted seam edges \(a_{n-1}b_0\) and \(b_{n-1}a_0\).

## Proof
**1. Lower bound on deletion size.** The cubic graph \(M_{2n}\) has \(2n\) vertices and \(3n\) edges. If \(S\) is a feedback vertex set of size \(k\) and \(q\) is the number of edges induced by \(S\), then the surviving forest has \(2n-k\) vertices and \(3n-3k+q\) edges. A nonempty forest has at most one fewer edge than vertices. Consequently
\[
3n-3k+q\le 2n-k-1,\qquad 2k\ge n+1+q.
\]
For \(n=2m\), every feedback vertex set has at least \(m+1\) vertices.

**2. Exact minimum-set recognition lemma for even \(n\).** Let \(S\) have size \(m+1\) in the two-rail model. Call column \(i\) *empty* if neither of its two vertices belongs to \(S\), and *double* if both do. Then \(S\) is a feedback vertex set **if and only if** (i) no two cyclically adjacent columns are empty and (ii) at most one edge has both endpoints in \(S\).

Necessity: adjacent empty columns leave a four-cycle in the complement; the inequality in step 1 gives at most one induced edge in \(S\). For sufficiency, put \(r,s,d\) for the numbers of empty, single, and double selected columns. Since \(s+2d=m+1\) and \(r+s+d=2m\), one has \(r=m-1+d\). From (i) the empty columns form an independent set of the cyclic column adjacency, so \(r\le m\), hence \(d\le1\). If \(d=1\), a fully deleted column cuts the surviving graph to an open two-row ladder; in such a strip every cycle contains two adjacent full (no selected vertex) columns, forbidden by (i). If \(d=0\), there are \(m-1\) empty columns and \(m+1\) singleton columns, so the cyclic singleton runs separated by the empties contain exactly \((m+1)-(m-1)=2\) singleton-to-singleton adjacencies. Any surviving cycle contained in a proper column interval would again require adjacent empty columns. Therefore any surviving cycle would have to wind through every cyclic column boundary; at each of those two singleton-to-singleton boundaries, its unique surviving rail edge forces the **selected** vertices across that same boundary also to be adjacent (this holds at the twisted seam too). That would give at least two edges inside \(S\), contradicting (ii). Thus the survivor is a forest. This lemma also covers \(m=2\), where the one singleton run has three columns.

**3. Explicit optimal odd cycle for even \(n\).** Start with
\[
S_0=\{a_0,a_2,\ldots,a_{n-4},a_{n-1},b_{n-2}\}.
\]
Perform the following ordered moves, omitting an empty range:

1. Slide \(b_{n-2}\to b_{n-3}\).
2. For even indices \(j=n-4,n-6,\ldots,2\), in that order, slide \(a_j\to a_{j-1}\).
3. Slide \(b_{n-3}\to a_{n-3}\).
4. Slide \(a_0\to b_{n-1}\) across the twisted seam.
5. Slide \(b_{n-1}\to b_{n-2}\).
6. For odd indices \(j=n-3,n-5,\ldots,3\), in that order, slide \(a_j\to a_{j-1}\).
7. Slide \(a_1\to a_0\).

The resulting set equals \(S_0\), with exactly \(1+(m-2)+1+1+1+(m-2)+1=2m+1=n+1\) legal slides. Direct inspection of the moving boundaries shows that each intermediate set has \(m+1\) vertices, the empty columns remain pairwise nonadjacent, and the number of selected-to-selected edges is at most one: during either descending-index wave the sole such edge, when present, is between the two consecutive selected vertices at the wave front; the transition through the double column creates only its selected rung edge. By the recognition lemma every intermediate set is a minimum feedback vertex set. Also, the moving wave front and the two distinctive seam/rung transitions give distinct intermediate vertex subsets (equivalently, compare the unique empty-column pattern and the selected layer labels); hence this closed walk is a *simple* cycle of length \(n+1\). The standalone parametric program verifies these exact invariants for even \(n=4,6,\ldots,100\) as a finite cross-check; the proof itself is uniform in \(n\).

**4. No shorter odd cycle.** For any graph \(G\), a closed token-slide walk in its fixed-cardinality subset graph yields a directed multiset of original-edge moves with equal in-degree and out-degree at every original vertex, because initial and final vertex occupancies coincide. This balanced directed multigraph decomposes into closed directed walks. If the total number of moves is odd, at least one of these walks is odd and contains an odd simple cycle in \(G\) no longer than the token-slide walk. Restricting configurations to feasible subsets cannot invalidate this lower bound. Thus
\[
\operatorname{og}(R_n)\ge\operatorname{og}(M_{2n}).
\]
When \(n\) is even, model \(M_{2n}\) on residues modulo \(2n\) with steps \(+1,-1,n\). A closed walk with an odd number of antipodal edges must contain at least \(n\) unit steps, because its unit-step displacement must be congruent to \(n\) modulo \(2n\). A closed walk with an even number of antipodal edges necessarily has an even number of unit steps and hence even total length. Therefore any odd closed walk has length at least \(n+1\), attained by the path of \(n\) consecutive cycle edges closed by one antipodal edge. Combined with step 3, this proves the exact odd girth \(n+1\).

**5. Odd \(n\).** When \(n\) is odd, both \(\pm1\) and \(n\) flip parity in the residue representation of \(M_{2n}\). Hence the original graph is bipartite. Every slide changes the number of selected vertices in either bipartition class by exactly one, so it reverses that number's parity. The minimum-set slide graph is therefore bipartite, proving infinite odd girth.

## Verification
Run `python3 check_construct.py` to reconstruct the explicit cycle, verify its vertex sets and edges independently in the twisted two-rail model, and check the forest and minimum-size invariants for all even \(n\) from 4 through 100. Run `python3 check_finite.py` to enumerate every subset up to the minimum feedback size in the independent cycle-plus-antipodes graph and compute the actual shortest odd cycles for \(n=3,4,5,6,7,8\). Both scripts use only the Python standard library. Exact finite checks support, but are not substituted for, the all-parameter proof.

## Relationship to prior work
Bousquet, Hommelsheim, Kobayashi, Mühlenthaler and Suzuki study feedback vertex set reconfiguration using unrestricted one-vertex replacement rather than edge-local token sliding; their general connectivity and complexity statements do not imply the present odd-girth formula. Avis and Hoang study token sliding for **independent sets**, including girth phenomena, but the feasibility condition is different from minimum feedback vertex sets. The odd-girth obstruction for a token graph itself is elementary and is **not** claimed as independently new; the contribution is constructing an optimal-feasible relocation cycle that exactly attains this obstruction for every even Möbius ladder. Previously investigated cyclic-prism feedback-set configurations are a different base graph: a twisted seam changes the optimal-slide odd-cycle behavior. Searching the indexed mathematical literature and relevant published result titles did not reveal an equivalent theorem, but this is not proof of priority.

## Limitations
The theorem determines odd girth, not ordinary girth, full reconfiguration connectivity, diameter, all odd-cycle counts or a complete minimum-set census. The 2023 feedback-set reconfiguration article was available in a detailed indexed HTML excerpt but its full publisher PDF could not be accessed during comparison; a lawful institutional request also could not proceed because access connectivity was unavailable. This leaves an explicit historical-priority uncertainty. No independent human audit or formal proof assistant validation has been performed.

## References
1. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, first posted 2022-03-31. https://arxiv.org/abs/2203.16861
2. N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), 114188. https://doi.org/10.1016/j.tcs.2023.114188
3. A. Hertz, *Decycling bipartite graphs*, Journal of Graph Algorithms and Applications 25 (2021), 461–480. https://doi.org/10.7155/jgaa.00567
