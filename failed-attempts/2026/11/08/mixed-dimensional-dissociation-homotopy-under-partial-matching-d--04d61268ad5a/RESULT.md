# Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)

## Finding

Let \(a,b\ge3\) and \(0\le t\le\min\{a,b\}\) be integers. Form \(G_{a,b,t}=K_{a,b}\setminus\{a_i b_i:1\le i\le t\}\), where the two labeled shores are \(\{a_1,\ldots,a_a\}\) and \(\{b_1,\ldots,b_b\}\), and only those \(t\) matching edges are deleted. Let \(\mathcal D(G)\) denote the simplicial complex of vertex sets whose induced graph has maximum degree at most one. There is an **integral homotopy equivalence**

\[
\mathcal D(G_{a,b,t})\simeq
\begin{cases}
\bigvee^{ab-1}S^1,&t=0,\\
\bigvee^{(a-t)(b-t)}S^1\;\vee\;\bigvee^{\binom{t-1}{2}}S^2,&1\le t\le\min\{a,b\}.
\end{cases}
\]

A wedge with zero summands is omitted. In particular, deleting exactly three matching edges from \(K_{4,4}\) produces \(\mathcal D(G_{4,4,3})\simeq S^1\vee S^2\), a first mixed-dimensional case. For \(3\le t<\min\{a,b\}\), both reduced integral homology groups are nonzero, with ranks \((a-t)(b-t)\) in degree one and \(\binom{t-1}{2}\) in degree two; these groups are torsion-free.

The complete face polynomial \(D_{a,b,t}(z)=\sum_{F\in\mathcal D(G_{a,b,t})}z^{|F|}\) and the inclusion-maximal face polynomial \(M_{a,b,t}(z)\) are

\[
D_{a,b,t}(z)=(1+z)^a+(1+z)^b-1+abz^2+t(a+b-2)z^3+\binom t2z^4,
\]
\[
M_{a,b,t}(z)=z^a+z^b+(a-t)(b-t)z^2+t(a+b-2t)z^3+\binom t2z^4.
\]

Thus the intermediate deletion regime simultaneously has full-shore facets, smaller local facets, and a topological transition not visible from the maximum dissociation number alone.

## Assumptions and scope

All graphs are finite, simple, and labeled. A dissociation set is a vertex set inducing maximum degree at most one. Its family includes the empty set and forms a simplicial complex. The homotopy statements are for geometric realizations, with integral (not merely field-coefficient) meaning. The formulas include \(t=0\) and \(t=\min\{a,b\}\) as limiting comparisons; the primary new regime is strictly between them. The explicit facet polynomial requires \(a,b\ge3\), as assumed. All binomial coefficients use their ordinary combinatorial meanings.

## Proof

**1. Classification of faces.** Let \(X\) and \(Y\) be the selected indices on the two shores, with sizes \(r\) and \(s\). For each selected \(a_i\), its selected degree is \(s-\mathbf1_{\{i\in Y,\ i\le t\}}\); symmetrically, for each selected \(b_j\), the selected degree is \(r-\mathbf1_{\{j\in X,\ j\le t\}}\). Therefore, if both shores are nonempty, \(r,s\le2\). All \(ab\) cross-shore pairs are allowed; mixed triples have form \(\{a_i,a_j,b_k\}\) with \(k\in\{i,j\}\cap[t]\), or its mirror. There are exactly \(t(a-1)+t(b-1)\) such triples. Mixed four-sets must have exactly two on each shore, and both selected index pairs must coincide inside \([t]\); there are \(\binom t2\). No larger mixed set is feasible. Adding the two full-shore simplices, subtracting the duplicated empty set, and adding these disjoint mixed size classes proves the face polynomial.

**2. Classification of facets.** Every nonempty one-shore proper set extends within its shore, so the only one-shore facets are the two whole shores. A mixed cross edge \(a_i b_j\) can be extended to a feasible mixed triple exactly if \(i\le t\) or \(j\le t\), except that matched-pair edges themselves also extend (using a second vertex on either shore, possible since \(a,b\ge3\)). Thus the maximal mixed edges have both endpoints among unmatched indices, in number \((a-t)(b-t)\). A mixed triple extends to a four-set exactly when its second index is also matched; all other mixed triples are facets, in number \(t(a-t)+t(b-t)\). Every allowed mixed four-set is a facet. This proves the maximal-face polynomial.

**3. Quotient and square-complex model.** Regard the two full-shore simplices \(\Delta_A\) and \(\Delta_B\) as disjoint nonempty contractible subcomplexes. Contracting each to a point is a homotopy equivalence for CW complexes: inclusion of a contractible subcomplex is a cofibration, and the quotient is homotopy equivalent to the original complex. The quotient \(\mathcal D(G_{a,b,t})/(\Delta_A,\Delta_B)\) has two poles, one edge \(e_{ij}\) between the poles for every \((i,j)\in[a]\times[b]\), one triangular two-cell for every mixed triple, and one three-cell for every allowed mixed four-set.

Define the two-dimensional CW complex \(Q_{a,b,t}\) as follows. Its vertices are the \(ab\) symbols \(e_{ij}\). For every \(k\le t\), put edges from \(e_{kk}\) to each \(e_{kj}\) with \(j\ne k\), and from \(e_{kk}\) to each \(e_{ik}\) with \(i\ne k\). For every \(i<j\le t\), attach a square along
\[
e_{ii}\longrightarrow e_{ij}\longrightarrow e_{jj}\longrightarrow e_{ji}\longrightarrow e_{ii}.
\]
The mixed triangles correspond to suspensions of edges of \(Q_{a,b,t}\), while the mixed tetrahedra correspond to suspensions of these squares. Hence the quotient CW structure is exactly the **unreduced suspension** \(\Sigma Q_{a,b,t}\); the construction uses all cells and all attaching maps, not just an Euler-characteristic count.

**4. Homotopy type of the square complex.** Suppose first that \(t\ge1\). Exactly \((a-t)(b-t)\) vertices \(e_{ij}\), with \(i>t\) and \(j>t\), are isolated in \(Q_{a,b,t}\). Every other vertex belongs to one connected component \(Q_0\). Its unmatched-index vertices are leaves attached to the diagonal vertices \(e_{kk}\) with \(k\le t\). Each off-diagonal vertex \(e_{ij}\) with distinct \(i,j\le t\) lies on a length-two path from \(e_{ii}\) to \(e_{jj}\). For every unordered pair \(\{i,j\}\subset[t]\), there are two such length-two paths, and the square two-cell fills the loop between them. Collapse the square across one of its two paths; this is a homotopy equivalence, leaving one path between \(e_{ii}\) and \(e_{jj}\). Doing this independently for all pairs, then contracting the remaining subdivision vertices and pendant leaves, gives \(Q_0\simeq K_t\) (as a one-dimensional CW graph). It follows that \(Q_0\simeq\bigvee^{\binom{t-1}{2}}S^1\), including the contractible cases \(t=1,2\). Suspending its \(1+(a-t)(b-t)\) components yields
\[
\Sigma Q_{a,b,t}\simeq\bigvee^{\binom{t-1}{2}}S^2\vee\bigvee^{(a-t)(b-t)}S^1.
\]
If \(t=0\), \(Q_{a,b,0}\) is a discrete set of \(ab\) vertices, and its unreduced suspension is a wedge of \(ab-1\) circles. This completes the integral homotopy proof.

## Verification

A standalone Python 3 script, `verify.py`, independently enumerates all vertex subsets using the original degree constraint, compares the face polynomial and maximal-face polynomial, and computes reduced homology ranks over \(\mathbb F_2\) from simplicial boundary matrices. It checks all \(28\) parameter profiles with \(3\le a\le b\le5\), \(0\le t\le a\): \(11{,}776\) candidate vertex subsets and \(425\) maximal faces. This is finite corroboration only. The integer homotopy statement follows from the explicit CW reductions above, not from mod-two ranks.

## Relationship to prior work

Tu, Li, and Du (arXiv:2103.01402; first posted March 2, 2021) established sharp *global extremal bounds* for numbers of maximal dissociation sets in general and triangle-free graphs. Their Theorems 1.1–1.5 do not classify the dissociation complex of these partial matching deletions. Carnero Bravo (arXiv:2307.13271; first posted July 25, 2023) introduced the forest filtration \(\mathcal F_d\), whose \(d=1\) case is the same dissociation complex, and computed \(\mathcal F_1(K_{a,b})\simeq\bigvee^{ab-1}S^1\) in the complete-bipartite case, as well as a result for categorical products \(K_n\times K_m\). Neither its join-graph result nor its categorical-product result gives the intermediate \(0<t<\min\{a,b\}\) parameter family directly. The complete deletion case \(K_{n,n}-M_n\) has an existing standalone homotopy description; the present contribution lies in the **partial-deletion mixed-dimensional transition**, including its exact ranks and face/facet enumerators. No claim is made of first proof of either endpoint.

## Limitations

The result concerns deleted matchings, not arbitrary deleted bipartite subgraphs. Independent audit and external priority verification have not been performed. Equivalent statements in less discoverable language or specialized graph-complex literature may exist. Computational checks are finite and mod-two; they are not substitutes for the topological proof.

## References

1. J. Tu, Y. Li and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402 (first public version 2021-03-02), https://arxiv.org/abs/2103.01402.
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first public version 2023-07-25), https://arxiv.org/abs/2307.13271.
