# Exact geodesic-transversal polynomials of triangular graphs from ordinary path saturation

## Finding
For every integer \(n\ge4\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, with one vertex for each edge of the labelled complete graph \(K_n\). A **geodesic transversal** is a set of vertices meeting every inclusion-maximal shortest path. Let \(N=\binom n2\), and let \(A_n(t)\) count all geodesic transversals by their selected cardinality; let \(B_n(t)\) count the inclusion-minimal ones. Define the following formal bivariate power series:

\[
\begin{aligned}
\mathcal A(x,u)&=\exp\!\left(xe^{xu}-\frac{x^2u}{2}+\frac{x^3u^3}{6}\right),\\
\mathcal B(x,u)&=\exp\!\left(xe^{xu}-x-\frac{x^2u}{2}-\frac{x^3u^2}{2}+\frac{x^3u^3}{6}\right)
+x\exp\!\left(\frac{x^3u^3}{6}\right).
\end{aligned}
\]

**Theorem.** For every \(n\ge4\),
\[
\boxed{A_n(t)=t^N n!\,[x^n]\mathcal A(x,t^{-1}),\qquad
B_n(t)=t^N n!\,[x^n]\mathcal B(x,t^{-1}).}
\]
All powers of \(t\) in these expressions are nonnegative. This is a complete coefficient-by-coefficient census, not merely an extremal count.

The map identifying a vertex of \(T_n\) with an edge of \(K_n\) gives the following exact structural description. The complement \(H\) of the selected edges is an ordinary (not necessarily induced) \(P_4\)-free subgraph of \(K_n\). Its components are isolated vertices, stars, or triangles. The transversal is inclusion-minimal precisely when either (i) \(H\) has no isolated vertices and all its components are edges, triangles, or stars with at least three leaves; or (ii) \(H\) is a disjoint union of triangles and exactly one isolated vertex.

As a consequence, the minimum transversal cardinality is
\[
\boxed{\operatorname{gt}(T_n)=\begin{cases}
\binom n2-n,&3\mid n,\\
\binom n2-n+1,&3\nmid n,
\end{cases}}
\]
whereas the largest size of an inclusion-minimal transversal is
\[
\boxed{\operatorname{gt}^{+}(T_n)=\begin{cases}
\binom n2-\frac n2,&n\text{ even},\\
\binom n2-\frac{n+3}{2},&n\text{ odd}.
\end{cases}}
\]
The scalar extremal edge-saturation facts underlying these last two identities are previously known; the claim here concerns the full two generating functions and their exact geodesic-transversal interpretation.

For even \(n=2m\), the number of inclusion-minimal transversals of largest cardinality is exactly \((2m)!/(2^m m!)\). For odd \(n=2m+1\ge5\), that number is exactly
\[
\binom n3\frac{(n-3)!}{2^{m-1}(m-1)!}
+5\binom n5\frac{(n-5)!}{2^{m-2}(m-2)!}.
\]

## Assumptions and scope
Graphs are finite, simple, undirected and labelled. A \(P_4\) is a path on four distinct vertices with three edges, with **ordinary subgraph** containment: additional chords do not nullify a copy. The geodesic transversal meets *every* maximal shortest path, not merely one shortest path per vertex pair. For inclusion-minimality, no vertex of the selected set can be removed while preserving transversalhood. Formal coefficient extraction uses exponential generating functions in \(x\), and \(u\) records the number of unselected vertices of \(T_n\), i.e. edges of \(H\). The theorem assumes \(n\ge4\); the \(n=3\) triangular graph is a clique and has different maximal-geodesic behavior.

## Proof
**1. Exact geodesics.** Two vertices of \(T_n\) are adjacent exactly when their corresponding edges of \(K_n\) meet. For \(n\ge4\), two disjoint edges have distance two; an intermediate edge joins one endpoint of the first to one endpoint of the second. Thus the three \(K_n\)-edges along any length-two geodesic form an ordinary \(P_4\). Conversely, the three edges along any ordinary \(P_4\) form a length-two geodesic of \(T_n\). Every adjacent pair in \(T_n\), represented after relabeling by \(ab\) and \(ac\), extends to the length-two geodesic \(ab,ac,cd\), choosing \(d\notin\{a,b,c\}\). Since \(T_n\) has diameter two, its maximal geodesics are **exactly** these three-vertex paths. A selected set meets all of them if and only if its complement edge set in \(K_n\) contains no ordinary \(P_4\).

**2. All admissible complements.** A connected graph with no ordinary \(P_4\) is a star or a triangle. Indeed, if it contains a cycle of length at least four, that cycle contains a \(P_4\); a triangle with any further connected vertex also gives a \(P_4\) using two triangle edges and an edge toward that extra vertex. Otherwise the connected graph is a tree, and diameter at least three would give a \(P_4\), so it is a star. This also includes isolated vertices and single edges. A component of size one contributes \(x\), one of size two contributes \(x^2u/2\), and the two types of size three contribute \(x^3u^2/2\) (three labelled two-leaf stars) and \(x^3u^3/6\) (one triangle). For size \(j\ge4\), only a \(j\)-vertex star occurs; it has \(j\) labelled center choices and \(j-1\) edges, contributing \(x^j u^{j-1}/(j-1)!\). The exponential formula for labelled component sets gives
\[
\exp\left(x+\frac{x^2u}{2}+\frac{x^3u^2}{2}+\frac{x^3u^3}{6}+\sum_{j\ge4}\frac{x^j u^{j-1}}{(j-1)!}\right)
=\mathcal A(x,u).
\]
Substituting \(u=t^{-1}\) and multiplying by \(t^N\) converts the omitted-edge count to selected-set cardinality, proving the first expression.

**3. Maximal admissible complements.** A transversal is inclusion-minimal precisely when its omitted-edge graph is edge-maximal among ordinary \(P_4\)-free graphs (i.e. \(P_4\)-saturated). A component which is a three-vertex two-edge star cannot occur: adding its missing leaf-to-leaf edge creates a triangle, still with no \(P_4\). Components of size at least four must be stars, as above. Inside a star with at least three leaves, adding a leaf-to-leaf edge creates a \(P_4\) via a third leaf; edges and triangles have no internal missing edges. Adding any edge between two distinct nontrivial components creates a \(P_4\), by extending the new connecting edge with one existing edge at each endpoint. If an isolated vertex coexists with another isolated vertex, their joining edge is harmless. If it coexists with an edge or star component, a joining edge extending that component as a star is harmless. But one isolated vertex together with triangles only is saturated, since any new edge from that vertex to a triangle gives a \(P_4\). Therefore the two stated types, and no others, are edge-maximal \(P_4\)-free graphs.

The first type has component EGF
\[
\exp\left(\frac{x^2u}{2}+\frac{x^3u^3}{6}+\sum_{j\ge4}\frac{x^j u^{j-1}}{(j-1)!}\right)
=\exp\left(xe^{xu}-x-\frac{x^2u}{2}-\frac{x^3u^2}{2}+\frac{x^3u^3}{6}\right).
\]
The second type has EGF \(x\exp(x^3u^3/6)\). They are disjoint for \(n\ge4\), proving \(\mathcal B\) and the second cardinality formula.

**4. Endpoints and multiplicities.** In an arbitrary ordinary \(P_4\)-free graph, each triangle component has as many edges as vertices, and every other component has exactly one fewer edge than vertices. Thus it has at most \(n\) edges, attained only by a partition into triangles (requiring \(3\mid n\)); otherwise at most \(n-1\) edges. Saturated examples attain these maxima: triangles only when \(3\mid n\); triangles plus one isolated vertex when \(n\equiv1\pmod3\); triangles plus one edge when \(n\equiv2\pmod3\). The minimum selected-set formula follows.

For the opposite end, a saturated graph of even order \(2m\) has at least \(m\) edges, with equality only for a perfect matching. A saturated graph of odd order \(2m+1\ge5\) has at least \(m+2\) edges: if it has no isolated vertex, the permitted components have sizes \(2,3,\ge4\), with per-component edge excess over half the vertex count minimized by exactly one triangle and the rest edges, or exactly one five-vertex star and the rest edges. More than one non-edge component increases the excess. The exceptional triangle-plus-singleton family has \(n-1\) edges and does not improve this bound. The two minimizing component forms attain \(m+2\) and are exhaustive. Matching partitions give the stated exact multiplicities. This proves every claimed boundary and count.

## Verification
The standalone `verify.py` independently constructs \(T_n\), finds graph distances by breadth-first search, enumerates maximal geodesics and tests all possible edge-selected sets for \(n=4,5,6\). The results match the ordinary-\(P_4\) characterization and both formal exponential-formula counts coefficient by coefficient. The verification checked \(33{,}856\) subsets, identifying \(873\) geodesic transversals and \(117\) inclusion-minimal ones; the directly computed maximal-geodesic counts summed to \(252\). Execution: `python3 verify.py`. The program does not assert an unrestricted theorem from finite enumeration; the unrestricted proof is above.

## Relationship to prior work
Manuel, Brešar and Klavžar introduced geodesic transversals in their January 20, 2021 public preprint and studied trees, cacti and extremal inequalities. Gould, Tang, Wei and Zhang (2012) give the existing edge spectrum of ordinary \(P_4\)-saturated graphs, including the classical saturation and extremal edge counts, and Burr (2017) explains the saturation-minimum component arguments. These preexisting results entail the **extreme cardinality bounds**, but not directly the full distributions of *all* triangular-graph geodesic transversals and *all* inclusion-minimal ones. The new mathematical focus is the exact bijection and closed bivariate exponential generating functions. Do not confuse ordinary \(P_4\)-subgraph-freeness with induced \(P_4\)-freeness (the cograph condition), which is much weaker.

## Limitations
The claim concerns the specified labelled triangular-graph family, not arbitrary Johnson graphs or arbitrary line graphs. The source comparison did not establish universal publication priority; an unindexed enumeration or a formula in uninspected full text could overlap. The 2018 Balister–Dogan paper on path-saturation spectra was available only at the abstract level in this investigation. The elementary matching and saturation extremal cardinalities are explicitly **not** asserted to be new. Independent mathematical audit and independent publication-priority certification have not been performed.

## References
1. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, preprint publicly posted January 20, 2021, arXiv:2101.08042; https://arxiv.org/abs/2101.08042.
2. R. J. Gould, W. Tang, E. Wei, C.-Q. Zhang, *The edge spectrum of the saturation number for small paths*, Discrete Mathematics 312 (2012), 2682–2689; https://doi.org/10.1016/j.disc.2012.01.012. Open manuscript: https://www.math.emory.edu/~rg/P149Y12.pdf.
3. E. Burr, *A Study of Saturation Number*, University of Alaska Fairbanks MSc thesis (2017), §4.2; https://scholarworks.alaska.edu/bitstream/11122/7864/1/Burr_E_2017.pdf.
4. P. Balister, A. Dogan, *On the edge spectrum of saturated graphs for paths and stars*, Journal of Graph Theory 89 (2018), 364–385; https://doi.org/10.1002/jgt.22256. (Abstract inspected; full text unavailable here.)
