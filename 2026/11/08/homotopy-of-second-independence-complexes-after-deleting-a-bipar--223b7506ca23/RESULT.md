# Homotopy of second independence complexes after deleting a bipartite matching

## Finding

For integers \(a,b\geq1\) and \(0\leq t\leq\min(a,b)\), take the complete bipartite graph on \(A=\{u_1,\ldots,u_a\}\) and \(B=\{v_1,\ldots,v_b\}\) and delete the \(t\) independent edges \(u_iv_i\), \(1\leq i\leq t\). Denote the resulting graph by \(G_{a,b,t}\). Let \(\operatorname{Ind}_2(G)\) be the simplicial complex of vertex sets whose induced connected components have order at most two. Then the **integral homotopy type for the entire partial-matching-deletion family** is

\[
\operatorname{Ind}_2(G_{a,b,t})\simeq
\begin{cases}
\displaystyle\bigvee^{ab-1}S^1,&t=0,\\[3pt]
\displaystyle\left(\bigvee^{(a-t)(b-t)}S^1\right)\vee
\left(\bigvee^{\binom{t-1}{2}}S^2\right),&1\leq t\leq\min(a,b).
\end{cases}
\]

A wedge with zero summands means a point. In particular the balanced crown graph \(G_{n,n,n}\), for every \(n\geq1\), has second independence complex homotopy equivalent to \(\bigvee^{\binom{n-1}{2}}S^2\) (the values at \(n=1,2\) are contractible). Thus the complete bipartite starting graph has \(ab-1\) circles, whereas deletion of a full matching in the balanced case produces only two-spheres.

## Assumptions and scope

Graphs are finite, simple, undirected. The bipartite classes \(A\) and \(B\) are disjoint, labeled as above, with exactly the specified edges omitted; in particular \(t=0\) is permitted. As the graphs are bipartite, an induced subgraph has components of order at most two exactly when all its induced degrees are at most one. Equivalently the complex is the \(P_3\)-devoid (dissociation) complex, where forbidden three-vertex paths need not be induced. The conclusion is an ordinary (nonequivariant) integral homotopy equivalence; no induced-subcomplex persistence or equivariant claim is made.

## Proof

**1. List every mixed face.** Every subset contained entirely in one bipartition class is a face, so both full simplices \(\Delta_A\) and \(\Delta_B\) occur. Every mixed two-element set \(\{u_i,v_j\}\) is a face. For a mixed face with at least three vertices, the induced-degree condition implies there can be at most two vertices from either side. A face of the form \(\{u_i,u_j,v_k\}\) is permitted precisely when \(k\leq t\) and \(k\in\{i,j\}\): the only way for \(v_k\) to meet at most one selected \(A\)-vertex is to select its missing-edge partner \(u_k\). Symmetrically the permitted faces of form \(\{u_k,v_i,v_j\}\) have \(k\leq t\) and \(k\in\{i,j\}\). A mixed four-element face is permitted precisely when it is the tetrahedron on \(\{u_i,v_i,u_j,v_j\}\) for some \(1\leq i<j\leq t\); its induced edges are the disjoint pair \(u_iv_j,u_jv_i\). There are no larger mixed faces. These statements also follow by testing degrees directly, so they cover all boundary cases \(a=1\), \(b=1\), and \(t=0,1\).

**2. Remove unmatched/matched mixed triangles.** Fix \(k\leq t\) and \(j>t\) on the \(A\)-side. The edge \(\{u_j,v_k\}\) lies in exactly one larger face, namely the triangle \(\{u_j,u_k,v_k\}\), and in no four-face. Thus this triangle and edge form a free elementary simplicial collapse. Likewise, if \(j>t\) on the \(B\)-side, the pair \(\{u_k,v_j\}\subset\{u_k,v_k,v_j\}\) is a free collapse. The free edges are distinct, and collapsing all of these pairs removes every mixed face meeting exactly one unmatched vertex and one matched opposite-side vertex, without removing any other face.

For \(t\geq1\), the resulting complex has two kinds of pieces: a connected core \(Y=\Delta_A\cup\Delta_B\cup T_t\), where \(T_1\) is the single edge \(\{u_1,v_1\}\) and for \(t\geq2\), \(T_t\) is the union of tetrahedra \(\Delta_{\{u_i,v_i,u_j,v_j\}}\) for \(1\leq i<j\leq t\); and exactly \((a-t)(b-t)\) additional edges \(u_iv_j\) with \(i>t,j>t\). Each such additional edge is maximal and has endpoints already in the connected core \(Y\). Attaching a one-cell with both endpoints in a connected CW complex adds one circle up to homotopy (choose an existing path between the endpoints). Hence

\[
\operatorname{Ind}_2(G_{a,b,t})\simeq |Y|\vee\bigvee^{(a-t)(b-t)}S^1.
\]

**3. Reduce to the matched core.** Define \(X_t\) as the subcomplex of \(Y\) on the \(2t\) matched vertices, namely \(X_t=\Delta_{\{u_1,\ldots,u_t\}}\cup\Delta_{\{v_1,\ldots,v_t\}}\cup T_t\). Define a simplicial retraction \(r:Y\to X_t\) fixing all matched vertices and sending every unmatched \(A\)-vertex to \(u_1\) and every unmatched \(B\)-vertex to \(v_1\). The map is simplicial because a face of \(Y\) belongs to \(\Delta_A\), \(\Delta_B\), or \(T_t\). For each such face \(\sigma\), the union \(\sigma\cup r(\sigma)\) remains a face of the same member of this cover. Thus the identity and \(r\) are contiguous, fixing \(X_t\); their induced maps furnish a homotopy equivalence \(|Y|\simeq|X_t|\).

**4. Determine \(X_t\).** If \(t=1\), \(X_t\) is a single edge, and is contractible. For \(t\geq2\), let \(U=T_t\cup\Delta_{\{u_1,\ldots,u_t\}}\). The simplicial map on \(U\) fixing each \(u_i\) and sending \(v_i\) to \(u_i\) retracts onto the full \(A\)-simplex. For every face of a tetrahedron in \(T_t\), the union of that face and its image is in the same tetrahedron; all other faces lie in the full \(A\)-simplex. This makes the map contiguous to the identity and proves that \(U\) is contractible. The full \(B\)-simplex is contractible too, and

\[
U\cap\Delta_{\{v_1,\ldots,v_t\}}=\operatorname{Skel}_1\Delta_{\{v_1,\ldots,v_t\}}.
\]

Indeed a tetrahedron in \(T_t\) meets the \(B\)-class in at most two vertices and every pair of distinct \(B\)-vertices occurs. The homotopy-pushout theorem for two contractible simplicial subcomplexes therefore yields

\[
X_t\simeq\Sigma\big(\operatorname{Skel}_1\Delta^{t-1}\big)
\simeq\bigvee^{\binom{t}{2}-t+1}S^2
=\bigvee^{\binom{t-1}{2}}S^2.
\]

For \(t=2\), the one-skeleton is an interval, giving a contractible suspension; the formula also agrees with the separately treated \(t=1\) case under the zero-summand convention. Combining steps 2–4 proves the second line of the displayed theorem.

**5. No missing edges.** When \(t=0\), every mixed face is a single cross-edge. The complex is two disjoint full simplices joined by all \(ab\) cross-edges. The first cross-edge joins its two contractible components; each of the remaining \(ab-1\) cross-edges adds one loop. This establishes the first line.

All reductions are homotopy equivalences of finite CW complexes, so the conclusion is integral, not just rational or mod-two homology. In particular the only nonzero reduced integral homology is free and occurs in degrees one and two, with the multiplicities in the theorem.

## Verification

The accompanying self-contained program `verify_matching_deleted_bipartite.py` enumerates every vertex subset, checks the induced degree condition, independently constructs the proposed face list, explicitly verifies the unique-free-edge collapses and simplicial-contiguity reductions, and computes unreduced mod-two Betti numbers by exact bit-vector boundary reduction. For all \(127\) parameter triples \(1\leq a,b\leq6\), \(0\leq t\leq\min(a,b)\), the direct and constructive face sets match and the resulting Betti vectors match the formulas, including zero higher Betti numbers. Its reproduced output is in `verification_output.txt`. This finite testing corroborates but does not replace the all-parameter topological proof above.

## Relationship to prior work

Taylan (2015, arXiv:1501.06754, first public 2015-01-27) defined \(P_3\)-devoid complexes and calculated instances including paths, cycles, and forests. The crown graph at \(t=a=b=3\) is the six-cycle and so that boundary example is covered, but the present result computes all bipartite partial matching deletions and both sphere degrees. Nilakantan–Shukla (2017, arXiv:1709.04789) and Goyal–Shukla–Singh (2019, arXiv:1905.06926) treat ordinary (one-)independence of regular bipartite graphs and categorical products; the crown graph is such a product, but ordinary independence is a different complex. Deshpande–Singh (2020, arXiv:2001.05448, Theorem 3.5) computes the higher-independence complex of complete multipartite graphs, covering the \(t=0\) boundary but not graphs with a nonempty matching deleted. The latter paper's other named families do not supply the partial-matching formula. A MathWorld crown-graph entry gives aliases and graph data but no second-independence homotopy classification. Searches of an indexed mathematical findings collection under all these aliases found nearby statements on crown graph invariants, ordinary independence, and two-matching edge complexes, with different face conditions and no implication of the stated homotopy formula. This does not establish definitive publication priority.

## Limitations

Only second independence complexes, for one omitted matching in complete bipartite graphs, are classified. The proof does not determine the maps induced by increasing \(t\), equivariant homotopy representations, higher \(r\)-independence, or analogous deletions of non-matching edge sets. The general result is not a claim that all special values are new: the complete-bipartite baseline and the six-cycle instance have published coverage. Unindexed equivalent research remains a novelty risk, and no independent mathematical audit has been performed.

## References

- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first public January 27, 2015. https://arxiv.org/abs/1501.06754
- N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789 (2017). https://arxiv.org/abs/1709.04789
- S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019), Section 3. https://arxiv.org/abs/1905.06926
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (2020), Theorem 3.5. https://arxiv.org/abs/2001.05448
- E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (graph identity only).
