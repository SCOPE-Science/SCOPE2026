# Maximal induced bipartite subgraphs of rook graphs: an exact facet enumerator and a square-board transition

## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with vertices the \(mn\) cells of an \(m\)-by-\(n\) board; two distinct cells are adjacent when they share a row or a column. Let \(\mathcal B_{m,n}(z)=\sum_S z^{|S|}\), where the sum ranges over all **inclusion-maximal** vertex sets \(S\) for which \(R_{m,n}[S]\) is bipartite. Define the rational formal power series
\[
 g(t)=\exp(-t/2)(1-t)^{-1/2},\qquad h(t)=\frac{2-t}{2(1-t)},
\]
and the integers
\[
 F_{m,n}=\frac{m!n!}{(n-m)!}[t^m]\,g(t)h(t)^{n-m}\quad(1\le m\le n),
 \qquad B_n=(n!)^2[t^n]g(t),\quad B_1=0.
\]
Then the complete inclusion-maximal cardinality polynomial is
\[
 \boxed{\mathcal B_{m,n}(z)=
 \begin{cases}
 F_{m,n}z^{2m},&2\le m<n,\\
 B_nz^{2n}+n^2B_{n-1}z^{2n-1},&m=n\ge2.
 \end{cases}}
\]
The coefficients count **labeled cell sets**, not isomorphism classes. In particular, the complex of vertex sets inducing bipartite subgraphs of \(R_{m,n}\), equivalently the \(2\)-matching complex of \(K_{m,n}\), is pure if \(m<n\) or \(m=n=2\), and is nonpure with exactly two adjacent facet dimensions if \(m=n\ge3\). Its facets have size \(2m\) for a rectangular board; on a square board of side \(n\ge3\) they have size \(2n-1\) or \(2n\), and both sizes occur.

Examples are \(\mathcal B_{3,3}(z)=9z^5+6z^6\), \(\mathcal B_{3,4}(z)=114z^6\), \(\mathcal B_{3,5}(z)=690z^6\), and \(\mathcal B_{4,4}(z)=96z^7+90z^8\). These particular finite board counts are consistency examples, not separate novelty claims.

## Assumptions and scope
All graphs are finite, undirected, and simple. A vertex-induced subgraph is bipartite exactly when it has no odd cycle. “Maximal” always means inclusion-maximal among vertex sets, not merely maximum cardinality. The board has at least two rows and at least two columns. The formal coefficient \([t^k]\) extracts the coefficient of \(t^k\) in a power series over \(\mathbb Q\). In the equivalent complete bipartite graph, each selected edge can occur only once; this is not a multigraph with repeated cells.

## Proof
**1. Bipartite subgraphs are exactly bounded-degree edge sets.** Identify a cell \((i,j)\) with the edge joining row vertex \(i\) and column vertex \(j\) in \(K_{m,n}\); then \(R_{m,n}=L(K_{m,n})\). For a chosen cell set \(S\), let \(H\) be the corresponding spanning subgraph of \(K_{m,n}\). If a vertex of \(H\) has degree at least three, its incident selected edges induce a triangle in \(L(H)=R_{m,n}[S]\), so the latter is not bipartite. Conversely, if all degrees of \(H\) are at most two, each connected component of \(H\) is a path, a cycle, or an isolated vertex. Since \(H\) is bipartite, every cycle has even length. Its line graph is therefore a disjoint union of paths and even cycles (isolated edges of \(H\) give isolated vertices of \(L(H)\)), hence bipartite. Thus admissible \(S\) correspond bijectively to edge sets with every row and column degree at most two.

**2. Classify maximal edge sets.** Let \(U\) and \(V\) be the row and column vertices, respectively, of selected degree less than two. An omitted edge can be inserted while preserving the degree bound exactly when both endpoints belong to \(U\) and \(V\). Thus maximality is equivalent to requiring that every edge in \(U\times V\) is already selected. If \(U\) and \(V\) are both nonempty, each vertex in either set has selected degree at most one, forcing \(|U|=|V|=1\); their unique connecting edge is selected. Those two vertices have degree exactly one, and this selected edge is an isolated component. Every other vertex has degree two. By counting the selected edges from each side, \(2m-1=2n-1\), so \(m=n\). Conversely, any isolated selected edge together with a two-regular bipartite graph on the remaining \((n-1)+(n-1)\) vertices is maximal.

If one of \(U,V\) is empty, its entire side has degree two. When \(m<n\), the column side cannot be saturated: it would require \(2n\) selected edges but the row capacity is only \(2m\). Therefore every maximal set has all \(m\) row vertices of degree two and has exactly \(2m\) cells. Conversely, every such selected edge set is maximal. When \(m=n\), saturating either side saturates both, producing precisely the two-regular spanning subgraphs, each with \(2n\) edges. The other maximal sets have the isolated-edge form and \(2n-1\) selected edges. For \(n=2\), there is no two-regular simple bipartite graph on the remaining \(1+1\) vertices, so the smaller type does not occur. For \(n\ge3\), an even spanning cycle supplies such a graph, so both sizes occur.

**3. Count the saturated family.** In a selected edge graph whose \(m\) row vertices all have degree two and whose \(n\) column vertices have degree at most two, every component is either an isolated column vertex, an alternating path with \(k\ge1\) row vertices and \(k+1\) column vertices, or an alternating cycle with \(k\ge2\) vertices of each kind. On fixed labeled sets of the appropriate sizes there are \(k!(k+1)!/2\) such paths and \((k!)^2/(2k)\) such cycles. These identities count undirected paths/cycles by dividing their oriented listings by two (or by \(2k\) for a cycle).

The labeled bivariate exponential generating function is therefore
\[
 \Phi(x,y)=\exp\!\left(y+\frac12\sum_{k\ge1}x^ky^{k+1}
 +\frac12\sum_{k\ge2}\frac{(xy)^k}{k}\right)
 =g(xy)\exp\bigl(yh(xy)\bigr).
\]
The desired count is \(m!n![x^my^n]\Phi(x,y)\). Substituting \(t=xy\) and extracting the coefficient of \(y^{n-m}\) gives precisely \(F_{m,n}\). In the square case \(n=m\), only cycles occur (no isolated column vertices or paths), so the same formula specializes to \(B_n=(n!)^2[t^n]g(t)\).

**4. Count the isolated-edge family.** For \(m=n\ge3\), choose the sole unsaturated row vertex and column vertex in \(n^2\) ways, include their joining edge, and choose a two-regular bipartite graph on the other \((n-1)+(n-1)\) labeled vertices in \(B_{n-1}\) ways. This accounts for exactly \(n^2B_{n-1}\) distinct maximal sets, all of size \(2n-1\). Disjointness from the \(2n\)-edge family and the preceding exhaustive characterization yield the displayed polynomial. This also proves the stated purity criterion.

## Verification
Run `python3 verify_rook_bipartite.py` with Python 3 and no external packages. The checker constructs rook-graph adjacency directly and, for every cell subset in boards of at most sixteen cells, separately uses graph two-coloring to test induced bipartiteness, compares it with the row/column capacity rule, and checks every one-cell extension for inclusion-maximality. It additionally enumerates larger boards by the independently cross-checked degree rule. An exact rational recurrence derived from the path/cycle generating function calculates the predicted coefficients without floating point arithmetic. Its output concludes:

`VERIFY_OK cases=11 examined_subsets=1419088 bipartite_sets=59904 maximal_sets=6506 GF=PASS classification=PASS`

Eleven board sizes from \(2\times2\) to \(4\times5\) were tested, including \(3\times6\). The tests are finite and do not establish the infinite theorem by themselves; Steps 1–4 are the proof.

## Relationship to prior work
Conte, Marino, Grossi, Uno and Versari (arXiv:1912.13446, first public version 2019-12-31) give general polynomial-delay algorithms for listing maximal induced bipartite subgraphs. This supplies the motivating listing problem but no rook-graph facet classification or enumerator in the inspected full-text sections. Vega (arXiv:1909.10406, first public version 2019-09-23) defines and studies two-matching complexes using discrete Morse theory on different graph families. Singh (arXiv:2006.13632, first public version 2020-06-24) studies the homotopy type of higher matching complexes of complete and complete bipartite graphs, particularly the balanced capacity \(n-1\) case, rather than the present all-board degree-two facet polynomial. Reiner and Roberts (2000) study homology of chessboard complexes with multiplicities; their homological framework and the general bounded-degree-complex terminology are prior knowledge.

Specific finite examples for the two-matching complexes of \(K_{3,4}\), \(K_{3,5}\), and \(K_{4,4}\) were previously computed in publicly available research records, including facet-size data for those boards. Those cases are **not** claimed new. The result here is the all-parameter structural theorem, the exact coefficient formula, and the sharp transition between pure rectangular and nonpure square boards, which do not follow solely from the cited finite homotopy computations or general listing algorithms.

## Limitations
This result is about facet enumeration and purity, **not** a homotopy equivalence, a shelling, or a Cohen–Macaulay classification. Existing homology formulas for bounded-degree complexes are not contradicted. The exponential generating function reuses classical labeled path-and-cycle counting; novelty, if any, is in the complete maximal induced-bipartite correspondence, the all-parameter facet count, and the square-board transition. The indicated literature inspection and public-record comparison do not establish absolute publication priority; an unindexed equivalent enumeration remains a residual risk. Independent mathematical audit has not been performed.

## References
1. A. Conte, A. Marino, R. Grossi, T. Uno, L. Versari, *Proximity Search for Maximal Subgraph Enumeration*, arXiv:1912.13446 (first posted 2019-12-31), SIAM J. Comput., DOI:10.1137/20M1375048.
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first posted 2019-09-23).
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first posted 2020-06-24), Discrete Mathematics 345 (2022), 112761.
4. V. Reiner, J. Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, J. Algebraic Combin. 11 (2000), 135–154, DOI:10.1023/A:1008728115910.
5. J. M. Byskov, B. A. Madsen, B. Skjernaa, *On the number of maximal bipartite subgraphs of a graph*, J. Graph Theory 48 (2005), 127–132, DOI:10.1002/jgt.20041.
