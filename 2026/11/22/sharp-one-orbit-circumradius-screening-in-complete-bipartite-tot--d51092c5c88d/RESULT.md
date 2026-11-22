# Sharp one-orbit circumradius screening in complete-bipartite total-matching polytopes

## Finding
Let \(1\le p<q\) be integers, let \(K_{p,q}\) have bipartition \(A\sqcup B\) with \(|A|=p\), \(|B|=q\), and let \(P_{p,q}\subset\mathbb R^{p+q+pq}\) be the convex hull of characteristic vectors of all total matchings (pairwise nonadjacent vertices and edges). Distances use the ordinary ambient coordinatewise Euclidean norm, with one coordinate for each graph vertex and edge. Set \(d=q-p\).

Let \(\mathcal M_{p,q}\) be the family obtained by selecting a matching saturating \(A\) and adjoining **every** unmatched vertex of \(B\). This is one orbit of size \(q!/(q-p)!\). Define \(c\) by assigning coordinate \(0\) to every vertex in \(A\), \(d/q\) to every vertex in \(B\), and \(1/q\) to every edge.

**Sharp sphere-screening theorem.** If
\[
 d(p-d)\ge 2p,
\]
then the unique smallest enclosing Euclidean ball of \(P_{p,q}\) has center \(c\) and squared radius
\[
 R^2=\frac{p(2q-p-1)}q.
\]
Every member of \(\mathcal M_{p,q}\) is on its boundary. If the inequality is strict, **these are exactly the contacting vertices**. If equality holds, one additional vertex contacts the ball, namely the characteristic vector of the whole smaller class \(A\). Equality occurs at exactly \((p,q)=(8,12),(9,12),(9,15)\).

Conversely, if the minimum ball has **only** the saturated-matching orbit \(\mathcal M_{p,q}\) as its contacts, then \(d(p-d)>2p\). Thus the one-orbit phase occurs precisely for \(p=9\), \(q\in\{13,14\}\), or for every \(p\ge10\) with \(p+3\le q\le2p-3\). For \(p\le8\) there is no strict one-orbit phase. No assertion is made here about the full circumradius or all contacts outside the displayed inequality.

## Assumptions and scope
A total matching is a subset of the graph's vertices and edges containing no two adjacent vertices, incident edges, or vertex–edge incidence. Every characteristic vector is a genuine vertex of \(P_{p,q}\): a zero-one vector cannot be a nontrivial convex combination of other distinct zero-one vectors. The ambient metric treats the \(p+q+pq\) coordinates as orthonormal. The theorem concerns the full-dimensional canonical realization, not a projected, rescaled, or solely edge-coordinate matching polytope.

## Proof
**1. Contact-orbit mean and variance certificate.** In each member of \(\mathcal M_{p,q}\), all \(p\) vertices in \(A\) are absent; exactly \(d\) vertices in \(B\) are selected; and exactly \(p\) disjoint edges are selected. Averaging uniformly over all injections \(A\hookrightarrow B\) yields \(c\): a fixed right-hand vertex is unmatched with probability \(d/q\), and a fixed edge belongs to the injection with probability \(1/q\). Every characteristic vector \(v\in\mathcal M_{p,q}\) has \(\|v\|^2=q\), while
\[
 \|c\|^2=\frac{d^2+p}{q},\qquad
 \langle v,c\rangle=\|c\|^2.
\]
Consequently every such vector lies at squared distance
\[
 \|v-c\|^2=q-\|c\|^2
 =\frac{p(2q-p-1)}q=:R^2.
\]
For any potential enclosing-ball center \(z\), the variance identity gives
\[
 \frac1{|\mathcal M_{p,q}|}\sum_{v\in\mathcal M_{p,q}}\|v-z\|^2
 =R^2+\|z-c\|^2.
\]
Thus every ball containing this orbit, hence every ball containing \(P_{p,q}\), has squared radius at least \(R^2+\|z-c\|^2\). In particular equality with \(R^2\) is possible only at \(z=c\).

**2. Exhaustive vertex classes and their distances.** Every total matching has some \(0\le k\le p\) disjoint edges and may select additional unmatched graph vertices from **at most one** side, because all cross-side vertex pairs are adjacent. If it selects from \(A\), the number \(s\) of these vertices satisfies \(0\le s\le p-k\). If it selects from \(B\), then \(0\le s\le q-k\). Put \(H=\|c\|^2=(d^2+p)/q\). Its squared distance from \(c\) is respectively
\[
 H+k\left(1-\frac2q\right)+s
 \quad\text{or}\quad
 H+k\left(1-\frac2q\right)+s\frac{p-d}{q}.
\]
Under \(d(p-d)\ge2p\), one has \(d\ge3\) and \(p>d\). Hence both vertex coefficients and the edge coefficient are positive. At each fixed \(k\), the furthest vertex in the first class therefore has all \(p-k\) available \(A\)-vertices, and the furthest in the second has all \(q-k\) available \(B\)-vertices. Their squared distances are
\[
 L_k=H+p-\frac{2k}{q},\qquad
 B_k=H+q\frac{p-d}{q}+\frac{2k(d-1)}q.
\]
The first decreases strictly with \(k\), and the second increases strictly with \(k\). Thus among all vertices only \(L_0\) (the all-\(A\) vertex) or \(B_p\) (exactly the orbit \(\mathcal M_{p,q}\)) can attain the maximum, and
\[
 B_p-L_0=\frac{d(p-d)-2p}{q}.
\]
The assumed inequality gives \(B_p=R^2\ge L_0\), so the ball centered at \(c\) with radius \(R\) contains every vertex, hence the entire polytope. Part 1 certifies global optimality and uniqueness of its center. Strictness yields only the saturated-matching orbit as contacts. Equality adds exactly the all-\(A\) vertex; no other class can tie because both displayed sequences are strictly monotone, and the omitted-vertex choices strictly lower squared distance.

**3. Necessity of strict screening.** Any minimum enclosing ball has a unique center, hence its center is fixed by the \(S_p\times S_q\) coordinate-permutation group. Standard first-order optimality of the maximum squared-distance function implies that this center lies in the convex hull of its contacting vertices: otherwise a separating direction would strictly decrease the maximum distance. If the contacts consist exactly of \(\mathcal M_{p,q}\), that center must be the *unique group-fixed point* of \(\operatorname{conv}\mathcal M_{p,q}\), namely \(c\). At \(c\), the all-\(A\) vertex has squared-distance excess \((2p-d(p-d))/q\) over the orbit radius, so strict sole contact forces \(d(p-d)>2p\). This also proves the claimed if-and-only-if.

**4. Integer phase boundaries.** Strictness is equivalent to \(d(p-d)>2p\), whose quadratic maximum over real \(d\) can be positive only for \(p>8\). When \(p=9\), precisely \(d=4,5\) satisfy it. When \(p\ge10\), concavity and the endpoint values \(3(p-3)>2p\), \(2(p-2)<2p\) imply that precisely \(3\le d\le p-3\) satisfy it. At equality, \(d(p-d)=2p\) rearranges to \(p=d+2+4/(d-2)\). Since \(d-2\) is a positive divisor of \(4\), exactly \((p,d)=(9,3),(8,4),(9,6)\) occur, yielding the three stated \((p,q)\) pairs.

## Verification
The standalone standard-library Python program `check.py` independently evaluates the exact squared-distance formula for every feasible matching size and side-support cardinality over a parameter grid, including all boundary cases. It checks the orbit barycenter by enumerating injections for small dimensions and verifies the complete integer phase classification through a larger finite grid. The executed check reported `TOTAL_MATCHING_OUTER_SPHERE_EXACT_PASS`. These finite checks are supplementary: the unrestricted theorem follows from the variance identity and monotonic affine distance comparisons, not computational extrapolation.

## Relationship to prior work
Ferrarini and Gualandi, *Total Coloring and Total Matching: Polyhedra and Facets* (arXiv:2105.09827, first posted 2021-05-20), introduce and study the total-matching polytope and its inequalities. Faenza and Ferrarini, *The Total Matching Polytope of Complete Bipartite Graphs* (arXiv:2303.00328, first posted 2023-03-01), give a complete facet description and extended formulation for this graph class, along with the equivalence to the stable-set polytope of the total graph. These papers concern the combinatorial/optimization formulation; their inspected full texts do not state a minimum Euclidean enclosing-ball theorem or identify its contact orbit. Other nearby published findings address the **inball** of balanced total-matching polytopes, the sphere of ordinary matching polytopes, or other graph-associated polytopes. Those statements do not imply the present ambient full total-matching outer-sphere classification, because the polytope, direction of extremization, or embedding differs. This comparison does not establish exhaustive historical priority.

## Limitations
The formula is for the full characteristic-vector Euclidean metric and only for the parameter range satisfying \(d(p-d)\ge2p\). The complete circumradius in the complementary regimes is not claimed. The first-order contact argument is a finite-dimensional standard convex-optimization condition, not a statement of combinatorial polarity. Search coverage cannot exclude an unindexed equivalent geometric theorem; independent mathematical review has not been performed.

## References
- L. Ferrarini and S. Gualandi, *Total Coloring and Total Matching: Polyhedra and Facets*, arXiv:2105.09827, first public version 2021-05-20. https://arxiv.org/abs/2105.09827
- Y. Faenza and L. Ferrarini, *The Total Matching Polytope of Complete Bipartite Graphs*, arXiv:2303.00328, first public version 2023-03-01. https://arxiv.org/abs/2303.00328
