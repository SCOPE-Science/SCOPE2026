# A path-or-cycle dichotomy for matching-defected multipartite clique-free complexes

## Finding
Let \(r\ge3\). Start with a complete \(r\)-partite graph on nonempty shores \(V_1,\ldots,V_r\). Remove the edges of a matching \(F\) (no two deleted edges share a graph vertex). Assume that each pair of shores supports at most one deleted edge and that the **color-incidence graph** \(H\) on \(\{1,\ldots,r\}\), with edges recording which shore pairs support deletions, has maximum degree two.

Let \(\mathsf{CF}_r(G)\) consist of all vertex subsets that contain no graph clique of size \(r\). If \(H\) has any path component with at least one edge, then
\[
|\mathsf{CF}_r(G)|\simeq *.
\]
If instead all non-isolated components of \(H\) are cycles, let \(c\) be their number and let \(k\) be the total number of shores in those cycles. Then
\[
\boxed{|\mathsf{CF}_r(G)|\simeq S^{r+k-c-2}.}
\]
The empty deletion matching gives \(c=k=0\) and the familiar sphere \(S^{r-2}\). In particular, deleting a matching supported around a single \(k\)-cycle of shores produces \(S^{r+k-3}\), whereas deleting edges on any nontrivial path of shores makes the complex contractible. The result holds for all allowable shore sizes, without a regularity or balance assumption.

## Assumptions and scope
The graph is simple, \(r\ge3\), all shores are finite and nonempty, deleted graph edges form a matching, the color-incidence graph is simple and has maximum degree two, and a shore with two incident defect edges has at least two vertices. The latter follows from the matching assumption. A path component means one with at least one edge, not an isolated vertex. The assertions concern the geometric realization, ordinary nonequivariant homotopy and integral homology; no shellability or naturality of a chosen sphere equivalence is asserted.

## Proof
**1. A strong simplicial compression.** Fix a shore \(V_i\) incident to a deleted edge. Let \(v\in V_i\) be an endpoint of such an edge. Every other vertex \(u\in V_i\) that is not incident to a deleted edge has \(N_G(v)\subseteq N_G(u)\). In the clique-free complex, every simplex containing \(u\) but not \(v\) can be enlarged by \(v\): an alleged new \(r\)-clique containing \(v\) would become an existing \(r\)-clique upon replacing \(v\) by \(u\); a clique cannot contain both vertices from the same shore. Thus \(u\) is dominated by \(v\) and can be deleted by a strong simplicial collapse. Repeat for all non-endpoint vertices in shores incident to a defect. In an untouched shore all vertices have the same external neighbors, so all but one can similarly be removed. These operations preserve the homotopy type. The reduced graph has exactly one vertex for each incident deleted edge at a non-isolated color and one vertex at each isolated color; its missing edges remain the original matching.

**2. Paths suppress every full transversal.** Every graph \(r\)-clique selects exactly one vertex from each shore. In a path component \(i_1-\cdots-i_s\), \(s\ge2\), the initial shore has just one remaining vertex, which is paired by a missing edge to one of the choices at the next shore. The next shore is forced to use its other choice (if interior), and this requirement propagates to the terminal shore, where it contradicts its sole available choice. When \(s=2\) the first missing edge itself gives the contradiction. There is consequently no graph \(r\)-clique in the compressed graph. Its clique-free complex is the entire simplex on its vertices and is contractible.

**3. A cycle has exactly two full-transversal choices.** Orient a cyclic color component and call each vertex corresponding to an outgoing missing edge \(a_i\), and the other vertex (corresponding to the incoming edge) \(b_i\). The missing edge from color \(i\) to the next color joins \(a_i\) to \(b_{i+1}\). A choice of one vertex per shore is allowed if and only if no consecutive binary selections have the pattern (outgoing, incoming). Around a directed cycle this forces all choices to be outgoing or all to be incoming. Thus each cycle component of length \(k_j\) contributes two disjoint vertex blocks \(A_j\) and \(B_j\), each of size \(k_j\), and a full \(r\)-clique chooses exactly one block for each cycle, together with the singleton vertex of every isolated color.

**4. The core with no isolated colors.** Suppose there are \(c\ge1\) cycles of lengths \(k_1,\ldots,k_c\), and let \(k=\sum k_j\). The core clique-free complex \(K\) is on \(2k\) vertices; its minimal nonfaces are the \(2^c\) unions \(\bigcup_j X_j\) with \(X_j\in\{A_j,B_j\}\). Its combinatorial Alexander dual \(K^*\) is the union of the \(2^c\) simplices whose vertex sets are the complements of these minimal nonfaces. Their intersections are simplices. The nerve has vertices the binary words of length \(c\); a set of words spans a simplex precisely when some coordinate is constant on the set. Covering this nerve by the \(2c\) coordinate-value simplices gives a second nerve: a face chooses at most one of two opposite values in each coordinate. That nerve is the join of \(c\) copies of \(S^0\), hence is \(S^{c-1}\). Both applications of the simplicial nerve lemma are valid because every nonempty finite intersection is a simplex. Therefore \(K^*\simeq S^{c-1}\).

Combinatorial Alexander duality over \(\mathbb Z\) now gives exactly \(\widetilde H_{2k-c-2}(K;\mathbb Z)\cong\mathbb Z\), with all other reduced integral homology zero. If \(k\ge4\), every triangle is a face because each minimal nonface has size \(k\). Consequently \(K\) contains the entire two-skeleton of a simplex and is simply connected. For the only case \(k=3\), there is one triangle of colors and \(c=1\); then \(K=\partial\Delta^{2}_{A_1}*\partial\Delta^{2}_{B_1}\cong S^3\). Thus in every case \(K\) is simply connected. Hurewicz supplies a sphere map generating its sole integral homology group, and the simply-connected homological Whitehead theorem proves \(K\simeq S^{2k-c-2}\).

**5. Restore isolated colors.** For an untouched shore reduced to one vertex \(z\), every full \(r\)-clique contains \(z\). Deleting \(z\) from the clique-free complex gives the full simplex on remaining vertices, and its link is the lower-threshold clique-free complex for the remaining color graph. The decomposition into that simplex and the cone on the link identifies the homotopy type with the suspension of the link. Applying this \(r-k\) times changes the core sphere dimension from \(2k-c-2\) to \(r+k-c-2\).

Finally, if no defect exists at all, compression leaves exactly one vertex per shore and the only forbidden \(r\)-set is the full vertex set. The complex is the boundary of an \((r-1)\)-simplex, namely \(S^{r-2}\). This completes all cases.

## Verification
The accompanying standard-library script `check_color_defects.py` independently constructs the graph from incidence edges, directly enumerates surviving graph \(r\)-cliques, builds every allowed simplicial face, computes reduced mod-two homology from full boundary matrices, and compares with the theorem. It exhaustively checks all simple color-incidence graphs of maximum degree two on three and four colors (49 graphs), plus eight larger and enlarged-shore tests, including two disjoint triangles of colors. The script verifies finite instances; it does not replace the all-size integral homotopy proof above.

Run `python3 check_color_defects.py` from a directory containing that script. Compare with `verification_output.txt`.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623, first public version February 10, 2026), define these graph complexes and prove shellability criteria for chordal families and clique-attachment constructions. Their theorems do not classify matching-deleted complete multipartite graphs by the component structure of a color-incidence graph. Carnero Bravo, *Total cut complexes and their duals* (arXiv:2602.21427, initial version February 24, 2026), Proposition 37, treats the intact complete multipartite case in an equivalent bounded-independence formulation, not the deleted matching incidence cycles. A forest-deletion restriction in which all missing edges join one specified pair of shores cannot exhibit a simple color cycle; the present theorem detects such cycles across at least three shore pairs. The nerve lemma, Alexander duality and homological Whitehead theorem themselves are standard tools and are not claimed as new.

## Limitations
The classification is not asserted if two missing edges join the same shore pair, if missing edges meet as graph edges, or if the shore-incidence graph has degree at least three. It does not classify the attaching maps in a deletion filtration, symmetry representations, or shellability. Failure to identify a matching published classification is not proof that no such formulation exists.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (2026-02-10), https://arxiv.org/pdf/2602.09623.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v1 (2026-02-24), https://arxiv.org/pdf/2602.21427; see Proposition 37 in subsequent versions.
3. Standard simplicial nerve lemma, combinatorial Alexander duality, Hurewicz theorem and simply-connected homological Whitehead theorem (classical results used explicitly above).
