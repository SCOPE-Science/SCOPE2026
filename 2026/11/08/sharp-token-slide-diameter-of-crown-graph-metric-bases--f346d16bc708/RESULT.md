# Sharp token-slide diameter of crown-graph metric bases

## Finding
For every integer \(n\ge3\), let \(H_n=K_{n,n}-M\) be the crown graph with vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and edges \(a_i b_j\) precisely when \(i\ne j\). Let \(\mathcal R_n\) have as vertices **minimum ordinary vertex-metric resolving sets** (metric bases) of \(H_n\); two sets are adjacent when one selected vertex is replaced by an adjacent, formerly unselected vertex of \(H_n\) and the result is again a minimum resolving set. Then
\[
\boxed{\operatorname{diam}(\mathcal R_n)=n+3\qquad(n\ge3).}
\]
Moreover, \(\mathcal R_n\) is connected, is \((n-1)\)-regular, has \(n2^{n-1}\) vertices and \(n(n-1)2^{n-2}\) edges, and has the following natural representation: a state has a single vacant matched index and one of the two sides selected at every other index. A slide moves the vacancy to an occupied index and reverses that index's side when it fills the old vacancy. The diameter is realized by the two states with the same vacancy and all remaining tokens on opposite sides.

The all-basis enumeration and state description are structural inputs, **not claimed as new**: they coincide with those established previously for edge-metric bases of the same crown graphs. The asserted new result is the sharp token-slide diameter together with explicit all-parameter routes proving it.

## Assumptions and scope
Graphs are finite, simple, undirected and unweighted. Distances are ordinary graph distances between **vertices**, not distances from a vertex to an edge. A resolving set distinguishes all pairs of vertices by their distance vectors. A basis is a minimum-cardinality resolving set. Moves are token **slides** along edges, with no temporary increase in cardinality and no two tokens occupying the same vertex. Indices are distinguishable; the graph \(H_2\) is disconnected and is excluded. The statement is for each integer \(n\ge3\) without an upper limit.

## Proof
**1. Classification of all metric bases.** In \(H_n\), vertices in the same bipartition side at different indices are at distance \(2\); vertices of opposite sides at different indices are at distance \(1\); the two vertices \(a_i,b_i\) at the same matched index are at distance \(3\). If a resolving set misses both indices \(i\) and \(j\), then its landmarks see \(a_i\) and \(a_j\) at identical distances, so it is not resolving. Thus every resolving set meets at least \(n-1\) matched indices and has at least \(n-1\) elements.

Conversely, choose exactly one endpoint of every matched pair except one pair \(h\), which is left empty. This set resolves all vertices. Indeed, two vertices at different indices \(i\ne j\) are distinguished by a landmark at any selected one of these indices: its distance to a vertex of its own index is \(0\) or \(3\), whereas its distance to a vertex of another index is \(1\) or \(2\). If two vertices have the same index, a selected landmark at that index sees them at distances \(0\) and \(3\); if their index is empty, any landmark sees them at distances \(1\) and \(2\). Therefore the metric dimension is \(n-1\), and exactly these \(n2^{n-1}\) transversals are metric bases.

**2. Exact move model.** Encode a basis by \((h,\sigma)\), where \(h\) is its empty index and \(\sigma_i\in\{0,1\}\) specifies which of \(a_i,b_i\) is chosen for each \(i\ne h\). An edge slide preserving the basis must move the sole token of some index \(j\ne h\) into the opposite-side vertex of the empty pair \(h\). After this move the vacancy is \(j\), and the token newly at \(h\) has side \(1-\sigma_j\). Conversely all \(n-1\) such choices are legal slides because \(j\ne h\), and the resulting set is still a transversal. Every state has degree \(n-1\); hence the claimed numbers of vertices and edges follow.

**3. Universal upper bound by induction.** For \(n=3\), the 12 encoded states form a connected 2-regular graph: starting with a vacancy at index 1 and both tokens on the \(a\)-side, repeat the vacancy itinerary \(1,2,3\) four times. The 12 states encountered before return are distinct, so this graph is \(C_{12}\), with diameter \(6=3+3\).

Now take \(n\ge4\) and two bases \(X,Y\). If they contain the same selected vertex at an index \(r\), leave that token fixed. On the remaining \(n-1\) index pairs, both restricted configurations are exactly bases of \(H_{n-1}\), and all their legal slides stay legal in \(H_n\). The induction hypothesis therefore gives a route of at most \(n+2\) slides.

Suppose henceforth that \(X,Y\) have **no common selected vertex**. Write \(h\) for the empty index of \(X\) and \(t\) for that of \(Y\).

*If \(h=t\):* every selected side must be reversed. Since \(n-1\ge3\), choose two occupied indices \(p,q\) with equal initial side \(c\). Let \(O\) list, in any order, all other indices whose initial side is \(1-c\), and let \(C\) list all other indices with initial side \(c\). Make the vacancy visit, in order,
\[
h,\ p,\ q,\ h,\ O,\ p,\ q,\ C,\ h.
\]
Here a list means visiting each of its indices successively, and empty lists are omitted. Every successive pair is distinct. Applying the rule from step 2 shows that the final vacancy is again \(h\), each index in \(O\) changes from \(1-c\) to \(c\), and each index in \(\{p,q\}\cup C\) changes from \(c\) to \(1-c\). Thus the final state is \(Y\). The number of slides is \(6+|O|+|C|=n+3\), since \(|O|+|C|=n-3\).

*If \(h\ne t\):* the required final selected side at \(h\), call it \(d\), exists. If any token of \(X\) has side \(1-d\), slide that token into the vacant index \(h\). This creates the correct, now shared vertex at \(h\), and then the induction case of a shared vertex reaches \(Y\) in at most \(1+(n+2)=n+3\) slides. Otherwise all occupied tokens of \(X\) have the same side \(d\). Since there are no common selected vertices, \(Y\) has side \(1-d\) at every index outside \(\{h,t\}\) and side \(d\) at \(h\). Choose any index \(p\notin\{h,t\}\), and let \(U\) list all the other indices outside \(\{h,t,p\}\). The vacancy itinerary
\[
h,\ p,\ t,\ h,\ p,\ U,\ t
\]
reaches \(Y\) by the move rule: \(h\) ends with side \(d\), every index outside \(\{h,t\}\) ends with side \(1-d\), and \(t\) is empty. It uses \(n+2\) slides. In all cases, \(d_{\mathcal R_n}(X,Y)\le n+3\).

**4. Matching sharp lower bound.** Let \(X\) be the basis with empty index \(h\) and every other token on side \(a\); let \(Y\) have the same empty index and all other tokens on side \(b\). Every slide flips the moving token's side. If a route uses \(u\) slides from \(a\) to \(b\) and \(v\) from \(b\) to \(a\), then \(u-v=n-1\) and the total length is \(n-1+2v\). The first token arriving at the initially empty pair \(h\) is on side \(b\). To make \(h\) empty again requires moving this token out, a \(b\)-to-\(a\) slide. But on the **last** slide out of \(h\), the outgoing token must be on side \(a\), because it must deposit a \(b\)-token at its destination in the final all-\(b\) configuration. Therefore, after the first \(b\)-to-\(a\) slide out of \(h\), at least one other \(b\)-to-\(a\) slide must deposit an \(a\)-token back at \(h\). These are distinct slides, so \(v\ge2\). Every route has at least \(n+3\) slides. Combined with step 3 this proves the diameter formula for all \(n\ge3\). \(\square\)

## Verification
The included independent `artifacts/verify_direct.py` constructs the original crown graphs, independently computes all vertex distances, and exhaustively checks all subsets of cardinality at most \(n-1\) for \(3\le n\le7\). It independently rebuilds legal token-slide edges from the original graph and verifies all configurations and degrees. Its replayed output is in `artifacts/direct_output.txt`.

The independent `artifacts/verify_state.py` implements only the vacancy-and-side transition. It computes **all-pairs** shortest paths and the exact diameter for \(3\le n\le8\), samples starting states for \(9\le n\le11\), and exhaustively tests the explicit same-hole complement route for all binary side assignments for \(4\le n\le11\). It also tests the exceptional all-constant-side different-hole route. Its output is in `artifacts/state_output.txt`. These finite tests corroborate but do not replace the inductive proof.

## Relationship to prior work
Kelenc, Tratnik and Yero introduced edge metric dimension and compared it with ordinary vertex metric dimension in their January 2016 preprint [1]. That paper does not give crown-graph token-slide distances. A later mathematical record, “Edge metric bases of crown graphs” [2], gives the exact \(n-1\)-vertex **edge-metric** basis classification and the count \(n2^{n-1}\); its full mathematical statement and proof were inspected. The coincident ordinary vertex-metric basis classification and enumeration are treated here as known underlying structure rather than a new contribution. Neither inspected source derives the token-slide graph's exact diameter.

A 2018 paper on the metric dimension of crown-graph subdivisions [3] concerns a scalar metric parameter; its full text was not obtainable, and its possible contents remain a priority uncertainty. Published student research descriptions on **metric-basis reconfiguration** [4] confirm that the token-slide diameter is a natural invariant and name studies of several graph families, but do not explicitly establish a crown-graph diameter. A 2026 thesis entitled “Reconfigurations of Metric Bases” was identified [5] without an accessible full text and remains a more serious unresolved historical-priority risk; its existence is not evidence of this specific statement. Search under “crown,” “deleted perfect matching,” “bipartite double cover,” “edge/vertex resolving basis,” and “vacancy-side flip” found no exact covering theorem, but search failure is not proof of priority.

## Limitations
The theorem is about minimum **vertex** resolving sets on the connected crown graphs only, using adjacency-constrained token slides. It does not describe all shortest routes or the complete distance distribution, nor does it establish any analogous bound for other graph families. The all-parameter mathematical proof is self-contained; finite enumeration alone would not establish it. Publication priority is provisional pending inspection of inaccessible relevant research and an independent mathematical review.

## References
1. A. Kelenc, N. Tratnik and I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291v1, first public 2016-01-31, https://arxiv.org/html/1602.00291v1.
2. “Edge metric bases of crown graphs,” published mathematical research record (2026), opaque record identifier b5b3c45f23e8.
3. “Invariance of metric dimension of subdivision of the crown graph,” 2018, abstract indexed at https://psa.pastic.gov.pk/SearchArticleView.aspx?S_id=8594&articledetailId=186118; complete text not inspected.
4. “Metric Basis Reconfiguration,” mathematical research project description, https://www.cpp.edu/camp-reu/research_projects.shtml.
5. B. Foster-Greenwood, student research listing identifying J. Morentin, “Reconfigurations of Metric Bases,” thesis (2026), https://www.cpp.edu/faculty/brianaf/student-research.shtml; text not inspected.
