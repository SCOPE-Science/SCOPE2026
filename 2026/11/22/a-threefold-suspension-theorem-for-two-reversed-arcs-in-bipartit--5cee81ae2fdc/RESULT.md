# A threefold-suspension theorem for two reversed arcs in bipartite multipath complexes

## Finding
Let \(G=(A\sqcup B,E)\) be a finite simple bipartite graph, and choose two edges \(a_1b_1\) and \(a_2b_2\) with four distinct endpoints. Define \(D=D(G;a_1b_1,a_2b_2)\) by orienting all edges from \(A\) to \(B\), except that the two chosen edges are oriented \(b_1\to a_1\) and \(b_2\to a_2\). Let \(X(D)\) be the simplicial complex of subsets of directed edges that form a disjoint union of directed paths, and let \(\mathcal M(H)\) be the ordinary matching complex of \(H\).

**Theorem.** If both cross edges \(a_1b_2\) and \(a_2b_1\) exist in \(G\), there is a homotopy equivalence
\[
X(D)\simeq \Sigma^3\mathcal M\bigl(G-\{a_1,a_2,b_1,b_2\}\bigr).
\]
Here \(\Sigma\) denotes *unreduced* suspension. If at least one cross edge is absent, \(X(D)\) is simplicially a cone and is contractible. Consequently, for all integers \(j\),
\[
\widetilde H_{j+3}(X(D);\mathbb Z)\cong\widetilde H_j\bigl(\mathcal M(G-\{a_1,a_2,b_1,b_2\});\mathbb Z\bigr),
\]
with the usual reduced/augmented degree convention at the empty complex.

**Torsion consequence.** For \(G=K_{7,7}\), the residual graph is \(K_{5,5}\). Its chessboard matching complex has \(\widetilde H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\mathbb Z\) by Jonsson [3]. Hence \(\widetilde H_5(X(D);\mathbb Z)\cong\mathbb Z/3\mathbb Z\). This gives two-arc-reversed, otherwise one-way, bipartite digraphs retaining arbitrary integral homotopy information from residual matching complexes, including nontrivial torsion.

## Assumptions and scope
Graphs are finite, simple and bipartite. The two reversed original edges are disjoint, and no other edge is reversed. A directed multipath is a collection of vertex-disjoint directed paths; isolated vertices are irrelevant to the edge-set complex. Equivalently, its edges give each vertex indegree and outdegree at most one, with no directed cycle. The ordinary matching complex of a graph has a vertex for each graph edge and faces indexed by matchings. For an edgeless residual graph its augmented matching complex is \(\{\varnothing\}\), formally \(S^{-1}\); then its threefold augmented suspension is \(S^2\). No balanced-partition, connectivity, minimum-degree or completeness assumption is required.

## Proof
Write the four special directed arcs
\[
r_1:b_1\to a_1,\quad r_2:b_2\to a_2,\quad x:a_1\to b_2,\quad y:a_2\to b_1.
\]
The arcs \(x,y\) exist precisely when the two cross edges are present. They form a unique directed four-cycle \(r_1xy r_2\) when all four exist. Every directed cycle in \(D\) must use both \(r_1\) and \(r_2\): a directed edge from \(B\) to \(A\) is required to return from \(B\), and a simple cycle uses at least two such edges, because there is no opposite pair on any one graph edge. As all other arcs point \(A\to B\), a directed cycle using both reversed arcs must be exactly this four-cycle. A subset of arcs satisfying the indegree/outdegree bounds is therefore a directed multipath if and only if it does not contain all four arcs.

Let \(Q=X(D)\setminus r_1\) be the deletion subcomplex. **First**, \(Q\) is a simplicial cone on \(r_2\). In any face not containing \(r_2\), adjoin \(r_2\). This cannot violate degree conditions, since every remaining arc has source in \(A\) and target in \(B\), whereas \(r_2\) has source in \(B\) and target in \(A\). One reversed arc cannot create a directed cycle. Thus \(Q\) is contractible.

**Second**, let \(L=\operatorname{lk}_{X(D)}(r_1)\subseteq Q\). If the cross edges are absent, adding \(r_1\) to any face of \(Q\) cannot create a cycle, and \(X(D)\) is the cone \(r_1*Q\), proving the second case.

Now suppose the cross edges exist. Write \(\sigma=\{r_2,x,y\}\), a two-simplex of \(Q\). Every face of \(Q\) is extendable by \(r_1\) unless it contains \(\sigma\). Therefore
\[
L=\{\tau\in Q:\sigma\not\subseteq\tau\},\qquad X(D)=Q\cup(r_1*L).
\]
The star of \(\sigma\) inside \(Q\) is \(\Delta(\sigma)*K\), where \(K=\operatorname{lk}_Q(\sigma)\). Since the path \(a_1\to b_2\to a_2\to b_1\) already uses all four distinguished vertices, a further arc can be added precisely when it is a forward edge between vertices outside this four-element set, and distinct added arcs must form a matching. Accordingly
\[
K\cong\mathcal M(G-\{a_1,a_2,b_1,b_2\}).
\]
The subcomplex \(L\) contains all faces of \(Q\) not containing \(\sigma\), so \(Q=L\cup(\Delta(\sigma)*K)\) and their intersection is \(\partial\Delta(\sigma)*K\).

**Third**, the geometric realization of \(X(D)\) is the homotopy cofiber of the subcomplex inclusion \(L\hookrightarrow Q\). The complex \(Q\) is contractible, hence \(X(D)\simeq Q/L\). The preceding decomposition and the subcomplex-cofibration property give
\[
Q/L\cong (\Delta(\sigma)*K)/(\partial\Delta(\sigma)*K).
\]
Since \(\Delta(\sigma)*K\) is contractible, its quotient by the subcomplex \(\partial\Delta(\sigma)*K\) has the homotopy type of the unreduced suspension of that subcomplex. Since \(\partial\Delta(\sigma)\cong S^1\), the join identity gives
\[
\Sigma(\partial\Delta(\sigma)*K)\simeq\Sigma(S^1*K)\simeq\Sigma^3 K.
\]
For \(K=\{\varnothing\}\), interpret the join and suspension in the augmented sense, giving \(S^2\) directly from the quotient of a two-simplex by its boundary. These are genuine homotopy equivalences, not computations over a chosen field. The homology statement follows by integral suspension, and the torsion consequence follows from [3]. \(\square\)

## Verification
The executable `verify_two_reversals.py` independently enumerates faces from directed indegree, outdegree and cycle constraints, then checks that the deletion is a cone, the deletion-link is precisely the complement of the upper star of \(\sigma\), and the residual link is the ordinary matching complex. It also compares reduced homology over \(\mathbb F_2\), with the predicted degree shift, on smaller cases. The complete recorded run checked 457 graphs containing the four-cycle, including 435 homology tests, totalling 70,002 enumerated faces, and separately checked 100 graphs where at least one cross edge was absent. All checks passed. This finite test is supporting evidence; the proof above covers all finite graphs and integral coefficients.

## Relationship to prior work
Caputi–Collari–Di Trani–Smith [1] introduce and analyze the multipath complexes used here, including the one-way complete-bipartite case, but do not give a two-disjoint-arc-reversal suspension formula. Caputi–Collari–Ramos [2] compare multipath and matching complexes for directed graphs **without directed cycles**; the noncontractible instances here have a directed four-cycle, hence do not fall under that comparison theorem. Jonsson [3] proves the \(K_{5,5}\) degree-two chessboard homology used only for the torsion consequence. The threefold suspension reduction and the two-reversal cone/cycle dichotomy are the proposed new results.

## Limitations
The classification requires exactly two reversed, vertex-disjoint bipartite edges. It does not address three reversals, reversals sharing endpoints, directed multigraphs or nonbipartite underlying graphs. The homotopy equivalence need not commute with arbitrary deletion maps between distinct underlying graphs. No independent external audit has been performed. A full bibliographic search cannot rule out unindexed equivalent statements, especially general cofiber formulas which might subsume this special case.

## References
[1] L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09, https://arxiv.org/abs/2208.04656.

[2] L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (2024), https://arxiv.org/abs/2401.01248.

[3] J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644, https://arxiv.org/abs/1203.5644. In particular, \(\widetilde H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\mathbb Z\).
