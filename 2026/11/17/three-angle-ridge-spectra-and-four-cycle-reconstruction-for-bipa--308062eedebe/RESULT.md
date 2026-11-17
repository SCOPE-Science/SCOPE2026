# Three-angle ridge spectra and four-cycle reconstruction for bipartite stable-set polytopes

## Finding

Let \(G=(V,E)\) be any finite simple bipartite graph without isolated vertices, with \(n=|V|\) and \(m=|E|\). Its *canonical Euclidean stable-set polytope* is
\[
P_G=\operatorname{conv}\{\mathbf{1}_I:I\subseteq V\text{ is an independent set}\}\subset\mathbb R^V.
\]
Write \(\ell(G)=|\{v:\deg(v)=1\}|\), \(w(G)=\sum_{v\in V}\binom{\deg(v)}2\) and \(c_4(G)\) for the number of distinct unoriented subgraph four-cycles. A **ridge** is a codimension-two face. The **interior dihedral angle** at a ridge is measured using the ordinary coordinate Euclidean metric. Then the **entire dihedral-angle spectrum** (angle followed by ridge multiplicity) is
\[
N_{\pi/4}=\ell(G),\qquad
N_{\pi/2}=\binom{n+m}{2}-2m-2c_4(G)-w(G),\qquad
N_{2\pi/3}=w(G).
\]
In particular, the total ridge number is
\[
\boxed{r_{n-2}(P_G)=\binom{n+m}{2}-2m+\ell(G)-2c_4(G).}
\]
The dimension and number of facets are \(n\) and \(n+m\). Therefore, knowing \(n,m\) together with this Euclidean angle histogram recovers **exactly** \(\ell(G)\), \(w(G)\) and \(c_4(G)\); equivalently,
\[
c_4(G)=\frac12\left[\binom{n+m}{2}-2m+\ell(G)-r_{n-2}(P_G)\right].
\]

Two asymptotic consequences distinguish graph families. For **any** sequence of trees \(T_n\) on \(n\to\infty\) vertices, a uniformly sampled ridge has angle converging in probability to \(\pi/2\) **if and only if** its maximum graph degree satisfies \(\Delta(T_n)=o(n)\). For the complete bipartite graphs \(K_{p,q}\), with both \(p,q\to\infty\), the uniform-ridge proportions of angles \(2\pi/3\) and \(\pi/2\) instead tend to \(1/3\) and \(2/3\), respectively.

## Assumptions and scope

Graphs are finite, simple, bipartite, may be disconnected, and have no isolated vertices. The metric is the ordinary Euclidean metric of the original vertex-coordinate realization (not a lattice-equivalent or rescaled realization). A four-cycle is a set of four distinct vertices together with the four edges of a cyclic \(K_{2,2}\); no inducedness assumption is required. A ridge belongs to exactly two facets. All formulas include the smallest case, one edge on two vertices.

For the asymptotic statements, graph edges have unit weights and random ridges are sampled uniformly by face count, not by their codimension-two area.

## Proof

**1. Exact inequalities and facet normals.** For every bipartite \(G\), the familiar totally unimodular edge-incidence description is
\[
P_G=\{x\in\mathbb R^V:x_v\ge0\ (v\in V),\quad x_u+x_v\le1\ (uv\in E)\}.
\]
Indeed, negating one bipartition's incidence columns gives an oriented incidence matrix, and the augmented coordinate rows preserve total unimodularity; because there are no isolates, these constraints imply \(0\le x_v\le1\). All vertices are integral, hence are precisely independent-set indicators. The polytope contains a full-dimensional small positive cube, and every listed inequality defines a facet (for any chosen equality, choose the remaining free variables strictly between their permissible bounds). Denote the coordinate facets \(A_v=\{x_v=0\}\), with outward normal \(-e_v\), and the edge facets \(B_{uv}=\{x_u+x_v=1\}\), with outward normal \(e_u+e_v\).

**2. Classification of facet-pair intersections.** Two distinct facets form a ridge exactly when a point satisfies their equalities and all *other* listed facet inequalities strictly. To see the reverse implication, a relative-interior point of a codimension-two intersection cannot lie on a third facet distinct from its defining facets (the face lattice of a polytope identifies a ridge with exactly two facets); conversely strictness leaves a relative open set of the two-equation affine subspace.

For distinct vertices \(u,v\), every \(A_u\cap A_v\) is a ridge: set these coordinates to zero and all others to a sufficiently small positive \(\varepsilon\). For a coordinate facet \(A_w\) and an edge facet \(B_{uv}\), the intersection is a ridge when \(w\notin\{u,v\}\): set \(x_w=0\), \(x_u=x_v=1/2\), and every other coordinate to a sufficiently small positive \(\varepsilon\). If \(w=u\), the equality forces \(x_v=1\); this can be part of a ridge **if and only if** \(\deg(v)=1\). If \(v\) has another neighbor \(z\), \(x_z=0\) is a third forced facet. If \(v\) is a leaf, set all other coordinates to small positive values; all remaining inequalities can be made strict. The case \(w=v\) is symmetric. Thus the number of coordinate–edge facet pairs that form ridges is \(nm-2m+\ell(G)\).

For two edge facets \(B_{ab}\) and \(B_{cd}\) that share a vertex, choose their common endpoint equal to \(3/4\), their other endpoints equal to \(1/4\), and all remaining coordinates sufficiently small and positive. Since \(G\) is bipartite, those two other endpoints are not adjacent; hence the intersection is a ridge. There are \(w(G)\) such pairs. If the edges are disjoint, and both possible cross-edges join their endpoints (a four-cycle), adding the two defining equalities forces *both* cross-edge inequalities tight, so the intersection has codimension at least three and is not a ridge. Conversely, if the four endpoints have at most one cross-edge, their coordinates can be chosen strictly positive on both defining edge equations with all other edge sums strictly less than one: use \(1/2\) at all four endpoints if there is no cross-edge, or assign \(1/4\) to the two endpoints of the sole cross-edge and \(3/4\) to the other two, then sufficiently small positive coordinates elsewhere. In the latter case the cross-edge sum is \(1/2\) and no extra equality is forced. Exactly two unordered pairs of opposite cycle edges occur for each four-cycle, and any such pair determines that cycle uniquely. Hence **exactly** \(2c_4(G)\) of the \(\binom m2\) edge–edge facet pairs fail to be ridges.

Combining the \(\binom n2\) coordinate–coordinate, \(nm-2m+\ell(G)\) coordinate–edge, and \(\binom m2-2c_4(G)\) edge–edge ridge counts proves the total.

**3. Euclidean angles.** For outward facet normals \(a,b\), the interior angle is \(\theta=\pi-\arccos(\langle a,b\rangle/(\|a\|\|b\|))\). Two coordinate normals are perpendicular. Two distinct edge normals have cosine \(1/2\) precisely for incident edges, and zero for disjoint edges. Coordinate and edge normals have cosine \(-1/\sqrt2\) when the vertex lies in the edge, and zero otherwise. Therefore the only possible interior angles are \(\pi/2\), \(2\pi/3\), \(\pi/4\). Step 2 counts the nonright ones as \(w(G)\) and \(\ell(G)\), respectively; subtraction proves the remaining multiplicity.

**4. Geometric distinctions in high dimensions.** For a tree, \(m=n-1\), \(c_4=0\), and \(r_{n-2}(P_T)=(n-1)(2n-3)+\ell(T)\sim2n^2\). Since \(\sum_v\deg(v)=2n-2\),
\[
\binom{\Delta(T)}2\le w(T)\le\frac12\Delta(T)(2n-2)=\Delta(T)(n-1).
\]
As \(\ell(T)\le n\), the combined proportion of nonright ridges tends to zero if \(\Delta(T)=o(n)\). If that convergence holds, \(w(T)=o(n^2)\), and the lower bound then forces \(\Delta(T)=o(n)\). For \(K_{p,q}\), direct degree counting gives \(w=p\binom q2+q\binom p2=pq(p+q-2)/2\), \(\ell=0\) when \(p,q\ge2\), and \(c_4=\binom p2\binom q2\). Substitution into the exact ridge formula and division by \(w\) show the obtuse fraction tends to \(1/3\) as both parts diverge; the remaining angle is right.

## Verification

A standalone Python standard-library checker (`checker.py`) enumerates all independent-set vertices, tests facet dimensions, and determines each intersected facet-pair affine dimension by exact rational Gaussian elimination. It independently counts graph leaves, wedges, and four-cycles. The recorded finite run returned `BIPARTITE_RIDGE_SPECTRUM_EXACT_PASS graphs=81`. Additional independent checks using exact symbolic affine-rank computation passed for all 34 isolate-free bipartite graphs in the small unlabeled graph atlas through six vertices; linear-programming strict-feasibility tests passed for those same 34 graphs. These finite checks corroborate the proof but do not establish its universal quantifiers.

## Relationship to prior work

Aprile, Faenza, Fiorini, Huynh and Macchia (2017) state the exact bipartite stable-set facet inequalities, which are established background here. Aliniaeifard, Benedetti, Bergeron, Li and Saliola (2018) study the *one-skeleton* of stable-set polytopes, rather than the ridge-angle spectrum. Tran and Ziegler (2013/2014, Lemma 8 and Proposition 9) directly establish the edge count \(\binom m2-2c_4(G)\) of the **graph edge polytope** for bipartite graphs. That established result coincides with the **edge-facet versus edge-facet ridge subcount** above and is **not claimed as new**. The complete angular spectrum still involves the distinct coordinate–edge classification, its precise leaf contribution, and the associated full metric histogram and asymptotics.

Prior exact angular calculations for stable-set polytopes of *complete split graphs* already cover stars as a special case. The star case alone is not claimed as new. The present assertions cover arbitrary bipartite graphs, including disjoint unions, nonsplit trees and cyclic graphs, and give a joint three-invariant reconstruction. Relevant existing treatments have not been shown to imply this complete statement, but this comparison does not exclude unindexed equivalent work.

## Limitations

This is a mathematical derivation with self-review, **not** an independent external audit or proof of historical priority. The result concerns ordinary Euclidean coordinates, not weighted graphs, arbitrary nonbipartite graphs, ridge Hausdorff measures, or arbitrary affine embeddings. Existing results contain the bipartite inequality description and the edge-facet ridge subcount; these constituent facts should not be independently cited as new discoveries. A full bibliographic search cannot prove no equivalent theorem exists. The first source's earliest public date is dated from its first preprint rather than a later revision.

## References

1. M. Aprile, Y. Faenza, S. Fiorini, T. Huynh and M. Macchia, *Extension complexity of stable set polytopes of bipartite graphs* (2017), arXiv:1702.08741, https://arxiv.org/abs/1702.08741 (first posted 2017-02-28).
2. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li and F. Saliola, *Stable set polytopes and their 1-skeleta* (2018), arXiv:1804.00360, https://arxiv.org/abs/1804.00360.
3. T. Tran and G. M. Ziegler, *Extremal edge polytopes* (first posted 2013-07-25; published 2014), arXiv:1307.6708, https://arxiv.org/abs/1307.6708 (Lemma 8 and Proposition 9).
4. T. Hibi, A. Mori and H. Ohsugi, *The number of 4-cycles and the cyclomatic number of a finite simple graph* (2018), arXiv:1801.06169, https://arxiv.org/abs/1801.06169 (Proposition 2.3 attributes the pertinent edge-polytope 1-skeleton count to Tran and Ziegler).
