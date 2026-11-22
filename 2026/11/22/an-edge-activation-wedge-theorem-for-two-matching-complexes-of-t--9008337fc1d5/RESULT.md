# An edge-activation wedge theorem for two-matching complexes of triangular books

## Finding
Let \(B_n=K_2\vee\overline{K_n}\) be the triangular-book graph with \(n\) triangle pages sharing one edge, and let \(H_n=B_n-uv=K_{2,n}\), where \(uv\) denotes the shared hub edge. For every integer \(n\ge2\), the degree-two matching complexes satisfy the following integral homotopy equivalences:
\[
\begin{aligned}
M_2(H_n)&\simeq\bigvee^{\left(\binom{n-1}{2}\right)^2}S^3,\\
M_2(B_n)&\simeq\bigvee^{(n-1)^2}S^2\vee\bigvee^{\left(\binom{n-1}{2}\right)^2}S^3.
\end{aligned}
\]
The zero-fold wedge denotes a point. Moreover the natural simplicial inclusion \(M_2(H_n)\hookrightarrow M_2(B_n)\) has a homotopy retraction. In particular, adding the shared hub edge creates exactly \((n-1)^2\) new integral two-sphere summands, preserves the three-sphere summands, and gives mixed-dimensional homotopy for every \(n\ge3\). The boundary case \(n=2\) is a single two-sphere, and for \(n=1\) both complexes are contractible.

## Assumptions and scope
All graphs are finite, undirected, simple and without loops. The simplicial complex \(M_2(G)\) has the edges of \(G\) as vertices; a face is a set of edges in which every graph vertex has selected degree at most two. Each graph edge can be used once. This is distinct from an ordinary matching complex (degree at most one), a perfect-matching complex, a vertex-induced dissociation complex and a directed multipath complex.

The two distinguished adjacent hub vertices are \(u,v\). The page vertices \(w_1,\ldots,w_n\) are mutually nonadjacent and incident to both hubs. Define the disjoint spoke sets \(A_n=\{uw_i:1\le i\le n}\), \(D_n=\{vw_i:1\le i\le n}\), and the central-edge vertex \(c=uv\) of \(M_2(B_n)\).

## Proof
**Exact face decomposition.** Let \(J_n\) be the simplicial complex on \(n\) vertices consisting of all subsets of cardinality at most two, including the empty face; it is the one-skeleton of an \((n-1)\)-simplex. If \(c\) is absent, a set of spokes is a two-matching precisely when it uses at most two \(A_n\)-spokes and at most two \(D_n\)-spokes. The selected degree at any page vertex is at most two automatically. Therefore the subcomplex with no \(c\) is exactly \(X_n=J_n*J_n\), where the two factors use the disjoint spoke sets. This is precisely \(M_2(H_n)\).

When \(c\) is selected, each hub has only one remaining degree slot. Thus a face containing \(c\) has at most one spoke from each set. Their allowable subsets form the simplicial graph \(Y_n=\Delta_{n-1}^{(0)}*\Delta_{n-1}^{(0)}\), where \(\Delta_{n-1}^{(0)}\) denotes \(n\) isolated vertices; equivalently \(Y_n\) is the one-dimensional complete bipartite graph \(K_{n,n}\). Consequently, as simplicial complexes,
\[
M_2(B_n)=X_n\cup_{Y_n}(c*Y_n),\qquad Y_n\subseteq X_n.
\]
The cone \(c*Y_n\) intersects \(X_n\) in exactly \(Y_n\), so the union realizes the homotopy cofiber of the inclusion \(j_n:Y_n\hookrightarrow X_n\).

**Nullhomotopy of the attaching graph.** For \(n\ge2\), \(J_n\) is nonempty and path-connected. The join of two connected nonempty complexes is simply connected (indeed at least two-connected). Hence \(\pi_1(X_n)=0\). Since \(Y_n\) is a connected graph and therefore homotopy equivalent to a wedge of circles, every based map \(Y_n\to X_n\), in particular \(j_n\), is nullhomotopic. The homotopy-cofiber theorem for a null map gives a homotopy equivalence, under \(X_n\) up to homotopy,
\[
M_2(B_n)\simeq X_n\vee\Sigma Y_n.
\]
The equivalence under \(X_n\) means the inclusion \(X_n\hookrightarrow M_2(B_n)\) admits a retraction up to homotopy, so its induced maps on all integral homotopy and homology groups are split injections where defined.

**Counting spheres integrally.** The connected graph \(J_n\) has \(n\) vertices and \(\binom n2\) edges, hence its first integral Betti number is \(\binom n2-n+1=\binom{n-1}2\). Collapsing a spanning tree yields \(J_n\simeq\bigvee^{\binom{n-1}2}S^1\). The join is the suspension of the smash product, so
\[
X_n=J_n*J_n\simeq\bigvee^{\left(\binom{n-1}{2}\right)^2}S^3.
\]
Here the displayed exponent denotes the square of the binomial coefficient; in unambiguous notation it is \(\left(\binom{n-1}2\right)^2\). Likewise the connected graph \(Y_n=K_{n,n}\) has \(2n\) vertices and \(n^2\) edges, so \(Y_n\simeq\bigvee^{n^2-2n+1}S^1\). Its reduced suspension is thus \(\Sigma Y_n\simeq\bigvee^{(n-1)^2}S^2\). Combining with the cofiber splitting proves the theorem over \(\mathbb Z\), without a finite-search extrapolation, homology-only inference or coefficient-field assumption.

For \(n=2\), both \(J_2\) factors are contractible edges, and the cofiber is \(\Sigma K_{2,2}\simeq S^2\). For \(n=1\), both complexes are simplices and hence contractible. All quantified cases are covered.

## Verification
The standalone Python 3 script `verify_book.py` (standard library only) independently constructs every allowed edge subset by graph-incidence degree tests and by the cone–join formula for \(2\le n\le10\); it compares the complete sets of faces, their counts and dimension vectors. It also recomputes the simplicial boundary ranks over \(\mathbb F_2\) by direct binary elimination, obtaining reduced Betti ranks \((n-1)^2\) in degree two and \(\left(\binom{n-1}2\right)^2\) in degree three, with all others zero. The saved `verification_output.txt` contains the actual successful output. These finite tests corroborate, but do not replace, the arbitrary-\(n\) topological proof above.

## Relationship to prior work
Singh (arXiv:2006.13632, Section 4) explicitly gives a join decomposition for appropriate complete-bipartite bounded-degree complexes, so the formula for \(M_2(K_{2,n})\) is **background, not new**. The new assertion is the effect of adjoining the missing central hub edge: a natural inclusion with a uniform homotopy retraction and precisely determined additional two-spheres. Vega (arXiv:1909.10406) develops two-matching complexes for wheel, forest and other families but does not give this triangular-book classification. Caputi, Collari and Smith (arXiv:2601.05670, first submitted January 9, 2026) study a different directed multipath construction. A later finite report for *the same underlying triangular books* determines multipath complexes with integral torsion at some page counts; those complexes have directed arcs as vertices and do not imply the present degree-two edge-subset splitting. Another finite two-matching study concerns the complete bipartite \(K_{3,5}\), which has three hubs instead of two adjacent hubs. The ordinary matching result for quadrilateral books is also distinct in both page geometry and allowed degrees. Search and comparison do not establish absolute priority.

## Limitations
No equivariant splitting, arbitrarily varying degree bounds, generalized book with page chords, or result for directed multipath complexes is asserted. The comparison with the finite triangular-book directed multipath report is about genuinely different simplicial complexes. The exact arbitrary-page theorem follows from elementary join and cofiber topology; the finite computation checks only \(2\le n\le10\). External, independent mathematical validation has not been performed. Unindexed equivalent statements or abstract cofiber results specialized elsewhere remain a priority risk.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first version 2026-01-09, https://arxiv.org/abs/2601.05670.
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, https://arxiv.org/abs/1909.10406.
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, especially Section 4, https://arxiv.org/abs/2006.13632.
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, first submitted 2026-08-31, https://arxiv.org/abs/2608.30601.
5. *Integral torsion migration in multipath complexes of triangular books*, published finite research report, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-torsion-migration-in-multipath-complexes-of-triangular--74926e9df2bd.
6. *The two-matching complex of \(K_{3,5}\) is a wedge of 91 five-spheres*, published finite research report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-two-matching-complex-of-k-3-5-is-a-wedge-of-91-five-spheres--ea5e14157f12.
7. *A three-page collapse threshold for quadrilateral book matching complexes*, published research report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-page-collapse-threshold-for-quadrilateral-book-matching--aa4a830c7ccd.
