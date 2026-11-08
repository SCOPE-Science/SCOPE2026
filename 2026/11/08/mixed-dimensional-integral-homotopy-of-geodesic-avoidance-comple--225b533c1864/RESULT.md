# Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets

## Finding
For arbitrary integers \(r\ge 2\) and \(m_1,\ldots,m_r\ge 1\), form the generalized windmill (clique bouquet)
\[
W=K_1\vee\bigl(K_{m_1}\sqcup\cdots\sqcup K_{m_r}\bigr),\qquad N=\sum_{i=1}^{r}m_i.
\]
Let \(\Delta(W)\) be the simplicial complex of vertex subsets containing no complete inclusion-maximal geodesic. The exact **integral homotopy type** is
\[
\Delta(W)\simeq\bigvee^{N-1}S^1\;\vee\;\bigvee^{\prod_{i=1}^r(m_i-1)}S^{r-1}.
\]
Zero summands are omitted; the two types of circles are combined when \(r=2\). The full face polynomial, including the empty face, is
\[
F_W(z)=\prod_{i=1}^{r}(1+m_i z)+z+Nz^2.
\]
The complete polynomial enumerating **inclusion-minimal** geodesic-transversal sets by cardinality is
\[
M_W(z)=\left(\prod_{i=1}^r m_i\right)z^{N+1-r}+N z^{N-1}.
\]
The complex is pure exactly when \(r=2\). For \(r\ge3\) with every \(m_i\ge2\), its nontrivial reduced integral homology occurs simultaneously in dimensions \(1\) and \(r-1\), with respective ranks \(N-1\) and \(\prod_i(m_i-1)\).

## Assumptions and scope
All graphs are finite, undirected, loopless, and simple. Their shortest paths are ordinary vertex sequences. A geodesic is **inclusion-maximal** when it is not a proper contiguous subpath of any longer geodesic. A geodesic-transversal set meets the vertex set of every maximal geodesic; its complement is a face of \(\Delta(W)\). This statement concerns every \(r\ge2\) and every positive petal size, including singleton petals and the coincident-degree case \(r=2\). No assumptions of equal petal size or asymptotic scale are made.

## Proof
Write \(c\) for the hub; its \(r\) peripheral cliques have vertex sets \(P_1,\ldots,P_r\). Distances between distinct peripheral vertices are one within one petal and two between petals. A shortest path inside a petal is the two-vertex edge; it cannot be extended to a longer geodesic because the endpoints are adjacent true twins. Between different petals, the unique shortest path is \(u,c,v\); it is maximal because the whole graph has diameter two. Any hub–peripheral edge is contained in such a three-vertex geodesic because \(r\ge2\). It follows that the maximal geodesics are precisely the in-petal edges and the cross-petal triples through the hub.

Let \(D(P)\) denote the zero-dimensional simplicial complex consisting of the empty face and singleton vertices in \(P\). A face omitting \(c\) contains at most one vertex from each \(P_i\), because it cannot contain an entire in-petal edge. A face containing \(c\) contains at most one peripheral vertex: otherwise an in-petal edge or cross-petal triple is contained in the face. Conversely, each face satisfying these conditions avoids every maximal geodesic. Thus the **full labelled complex** is exactly
\[
\Delta(W)=K\cup(c*D(X)),\quad K=D(P_1)*\cdots*D(P_r),\quad X=\bigsqcup_{i=1}^r P_i,
\]
where \(K\cap(c*D(X))=D(X)\). The cone \(c*D(X)\) is contractible.

The join of nonempty discrete spaces is connected for \(r\ge2\). A discrete space with \(m_i\) vertices has the reduced homotopy type of a wedge of \(m_i-1\) zero-spheres, in the pointed-join sense. Repeated joins (equivalently, suspensions of smash products) give
\[
K\simeq\bigvee^{\prod_i(m_i-1)}S^{r-1},
\]
where a factor with one vertex makes the join contractible. To account for the cone, regard \(c*D(X)\) as \(N\) edges from \(c\) to distinct peripheral vertices. Choose a spanning tree within the connected one-skeleton of \(K\) connecting the \(N\) attachment vertices. The added star plus that tree has cycle rank \(N-1\); equivalently, the homotopy pushout of \(D(X)\hookrightarrow K\) and \(D(X)\to\{c\}\) is homotopy equivalent to \(K\vee\bigvee^{N-1}S^1\). This is a homotopy equivalence over the integers, not merely a Betti-number computation. The claimed wedge follows.

All faces omitting \(c\) are obtained independently by taking either no vertex or one of the \(m_i\) vertices of each petal, giving \(\prod_i(1+m_i z)\). The remaining faces are \(\{c\}\) and \(\{c,u\}\) for \(u\in X\), contributing \(z+Nz^2\). The facets are precisely the \(\prod_i m_i\) choices of one vertex from every petal (size \(r\)) and the \(N\) hub–peripheral pairs (size \(2\)). Their complements are precisely the inclusion-minimal geodesic transversals, of respective sizes \(N+1-r\) and \(N-1\), proving the formula for \(M_W\). Since both facet families are nonempty and have dimensions \(r-1\) and \(1\), purity holds if and only if \(r=2\).

## Verification
A standalone Python 3 verifier, `verify.py`, constructs each clique bouquet without using the asserted geodesic classification; independently enumerates all shortest paths with breadth-first search; discards extendable paths; exhaustively checks every face against the original maximal-geodesic avoidance definition; checks the facet count and minimal-transversal polynomial; and computes reduced mod-two simplicial homology via boundary-matrix rank. It passes for 102 parameter profiles with \(2\le r\le4\), all \(1\le m_i\le3\), and \(N\le9\), examining 37,656 vertex subsets. Mod-two homology is only a computational cross-check; the unrestricted **integral** homotopy claim follows from the explicit topological proof above. Run `python3 verify.py` with the standard library.

## Relationship to prior work
Manuel, Brešar, and Klavžar initiated the geodesic-transversal problem and examined minimum transversals (arXiv:2101.08042v1, January 20, 2021). Peterin and Semanišin independently studied maximal-shortest-path covering (Mathematics 9(14), 1592, 2021). In a separate join/lexicographic-product paper (Computational and Applied Mathematics 41, 128, 2022), Peterin and Semanišin already characterize relevant maximal geodesics and establish an exact **scalar minimum** for graph joins; their Lemma 3.1 and join theorem are important prior structural coverage. The scalar minimum and the ease of obtaining basic facet information from the join description are **not claimed as new**. The assessed contribution is the complete **integral homotopy calculation**, especially the mixed-dimensional circle/sphere wedge when \(r\ge3\), accompanied by exact full-face and inclusion-minimal cardinality enumerators. The full available author manuscript was reviewed in its relevant join sections, and no direct homotopy formula was identified.

## Limitations
This is a self-contained mathematical proof supplemented by exhaustive finite cross-checks; finite checks do not prove the unrestricted statement. This theorem does not address arbitrary block graphs. The combinatorial facet description is close to a specialization of established join-graph results, so only the topological refinement and integrated enumerators are put forward as a research contribution. Priority is provisional: an equivalent homotopy computation might appear in differently indexed topological or graph-hypergraph literature. No independent mathematical audit has been performed.

## References
1. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1 (2021), https://arxiv.org/abs/2101.08042.
2. I. Peterin, G. Semanišin, *On the Maximal Shortest Paths Cover Number*, Mathematics 9(14), 1592 (2021), https://doi.org/10.3390/math9141592.
3. I. Peterin, G. Semanišin, *Geodesic transversal problem for join and lexicographic product of graphs*, Computational and Applied Mathematics 41, article 128 (2022), https://doi.org/10.1007/s40314-022-01834-1; accessible author manuscript dated October 26, 2021 at https://mp.feri.um.si/osebne/peterin/clanki/2021_iIpgs_geod_trans_JLP.pdf.
