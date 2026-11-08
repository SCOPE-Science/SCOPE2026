# A parity-and-minimum-cycle-degree law for enclosing spheres of unicyclic in-in zonotopes

## Finding

Let \(G=(V,E)\) be any finite connected simple **unicyclic** graph, with unique cycle \(C\) of length \(L\ge3\), and write \(d_v=\deg_G(v)\). For any real \(t>0\), form the Euclidean zonotope
\[
\mathcal I_t(G)=
\sum_{v\in V}[-t e_v,t e_v]
+\sum_{\{u,v\}\in E}[-(e_u-e_v),e_u-e_v]
\subset\mathbb R^V.
\]
The case \(t=1\) is the equal-parameter in-in zonotope introduced by Glew [1]. All radii and distances use the displayed orthonormal vertex-coordinate metric.

The unique center of the minimum enclosing Euclidean ball is the origin. Define
\[
B_t(G)=\sum_{v\in V}(d_v+t)^2,
\qquad
\delta_C=\min_{v\in V(C)}d_v,
\qquad
k_C=|\{v\in V(C):d_v=\delta_C\}|.
\]
Then the squared radius, the total number of distinct touching vertices, and the Euclidean diameter are **exactly**
\[
\boxed{R_t(G)^2=\begin{cases}
B_t(G),&L\text{ even},\\
B_t(G)-4(\delta_C+t-1),&L\text{ odd},
\end{cases}}
\qquad
\boxed{N_t(G)=\begin{cases}2,&L\text{ even},\\4k_C,&L\text{ odd},\end{cases}}
\qquad
\boxed{\operatorname{diam}_2(\mathcal I_t(G))=2R_t(G)}.
\]
Exactly \(N_t(G)/2\) unordered antipodal pairs attain the diameter, and no other pairs attain it.

More precisely, orient every edge of \(G\), write \(b_v=\operatorname{outdeg}(v)-\operatorname{indeg}(v)\), and at every vertex choose a coordinate-box endpoint \(s_v\in\{-t,t\}\). A contact point has coordinates \(b_v+s_v\); the following rules list **all** contacts, without repetition:

* If \(L\) is even, use either of the two bipartition orientations, in which every vertex is a pure source or a pure sink, and set \(s_v=t\operatorname{sign}(b_v)\).
* If \(L\) is odd, choose one defect vertex \(w\) on \(C\) with \(d_w=\delta_C\). Every other vertex must be a pure source or a pure sink. The two cycle edges at \(w\) point one in and one out; all pendant-tree edges at \(w\), if any, point in the same direction, giving exactly one minority incident edge if \(d_w>2\). Set \(s_v=t\operatorname{sign}(b_v)\) wherever \(b_v\ne0\). At \(w\) with \(d_w=2\), \(b_w=0\) and either choice \(s_w=\pm t\) is allowed. Exactly four distinct contacts arise for each allowed defect \(w\).

## Assumptions and scope

The graph is simple, undirected before orientation, connected, and has exactly one cycle; trees may be attached at arbitrary cycle vertices. Edge generators have unit coefficient and all coordinate segments have the same positive half-length \(t\); the result is not stated for general edge weights, disconnected graphs, multigraphs, or graphs with multiple cycles. In-in zonotopes are defined through the explicit Minkowski sum, so no facet-description or change-of-metric convention is implicit. At \(t=0\), some contact points coalesce; the count formula therefore assumes \(t>0\).

## Proof

**1. Center and endpoint reduction.** The zonotope is compact, full-dimensional (because \(t>0\)), and centrally symmetric about zero. If \(R=\max_{x\in\mathcal I_t(G)}\|x\|_2\), any ball centered at \(c\) containing antipodal points \(x,-x\) with \(\|x\|=R\) must have squared radius at least
\[
\tfrac12(\|x-c\|^2+\|-x-c\|^2)=R^2+\|c\|^2.
\]
The origin ball has radius \(R\); thus it is uniquely minimal. The function \(x\mapsto\|x\|_2^2\) is strictly convex. Any norm-maximizing point in the Minkowski sum must use endpoints for every nonzero generating segment: varying an interior segment coefficient would express the point as the midpoint of two distinct points of the zonotope and strictly lower its norm square relative to at least one of them. Hence all contacts arise from signed edge-incidence and signed coordinate generators.

**2. Exact orientation objective.** Orienting the edge generators yields a vector \(b=(b_v)\) with \(b_v=\operatorname{outdeg}(v)-\operatorname{indeg}(v)\). For fixed \(b\), the maximum over independent signs \(s_v\in\{-t,t\}\) is
\[
F_t(b)=\sum_{v\in V}(|b_v|+t)^2.
\]
The maximizing \(s_v\) is forced to have the sign of \(b_v\) when \(b_v\ne0\), and either sign is optimal when \(b_v=0\). Since \(|b_v|\le d_v\), we always have \(F_t(b)\le B_t(G)\). Equality at a vertex means that all incident edges point uniformly inward or uniformly outward, namely that vertex is a pure sink or a pure source.

**3. Even cycle.** The graph is bipartite. Direct every edge from one bipartition side to the other, making every vertex pure. This attains \(B_t(G)\). Conversely, equality forces every vertex pure, which on a connected graph gives precisely the two orientations induced by swapping the bipartition sides. Each has unique optimal box signs, yielding exactly two antipodal contacts.

**4. Odd-cycle loss.** An odd cycle cannot have every cycle vertex pure: if its cycle edges were both incoming or both outgoing at each vertex, sources and sinks would have to alternate around an odd cycle. Thus some cycle vertex \(w\) is incident to at least one incoming and at least one outgoing edge. For such a vertex,
\[
|b_w|\le d_w-2,
\qquad
(d_w+t)^2-(|b_w|+t)^2
\ge(d_w+t)^2-(d_w-2+t)^2
=4(d_w+t-1)\ge4(\delta_C+t-1).
\]
All other coordinate losses are nonnegative. Consequently \(F_t(b)\le B_t(G)-4(\delta_C+t-1)\).

Choose any cycle vertex \(w\) of minimum cycle degree. On the odd cycle, direct successive cycle edges alternately so every other cycle vertex is pure and exactly \(w\) has one incoming and one outgoing cycle edge. Orient each tree edge recursively so all off-cycle vertices are pure. At cycle vertices other than \(w\), orient attached tree edges in the same local direction as the cycle edges. At \(w\), orient all attached tree edges in one common direction, choosing either direction; exactly one of the two incident cycle edges then disagrees with the others when \(d_w>2\). For \(d_w=2\), the two cycle edges are the entire incident edge set. In either case \(|b_w|=d_w-2\), all other vertices satisfy \(|b_v|=d_v\), and the upper bound is attained.

**5. Equality cases and counting.** Equality in the odd-cycle upper bound forces precisely one mixed vertex, which must lie on the cycle and have degree \(\delta_C\); every other vertex is pure, and the defect has exactly one minority incident edge when \(d_w>2\) (with a one-in/one-out tie when \(d_w=2\)). The two cycle edges at the defect must have opposing local directions, since a directed odd cycle otherwise requires another mixed cycle vertex. Once \(w\) is fixed, there are exactly two globally opposite alternating orientations of the cycle, and all off-cycle orientations are forced except for the common choice of direction of attached tree edges at \(w\) when \(d_w>2\). Thus when \(d_w>2\) there are four maximizing orientation/box-sign choices, with box signs forced. When \(d_w=2\) there are two cycle choices and two independent optimal signs for its zero-imbalance box coordinate, again four points.

These four points are distinct: the unique coordinate whose absolute value is less than \(d_v+t\) identifies \(w\); with \(w\) fixed, reversal changes a pure cycle coordinate, while the remaining choice changes the defect coordinate. No further maximizers exist. Summing over the \(k_C\) minimum-degree cycle vertices proves \(N_t(G)=4k_C\).

**6. Diameter.** For any centrally symmetric compact convex set inside the radius-\(R\) origin ball, antipodal contacts have distance \(2R\). Equality in the triangle inequality for any pair at distance \(2R\) requires both endpoints to be antipodal contacts. This proves both the diameter and its complete pair classification.

## Verification

The standalone `verify.py` uses Python 3's standard library and exact integer arithmetic for \(t=1\) and \(t=2\). It exhausts 4,245 canonical unicyclic graph configurations with at most eight vertices, including all connected simple unicyclic graphs of these orders up to relabeling; it compares the direct signed-edge maximum and the distinct-contact count with the formulas in 8,490 graph/parameter cases. A separate check explicitly enumerates **all** cube and edge endpoint sign choices in 216 cases through six vertices. Both checks passed. The program does not use numerical optimization or approximate comparisons. These finite checks corroborate, but do not replace, the proof for arbitrarily large graphs and real \(t>0\).

For the unit-parameter examples: \(\mathcal I_1(C_5)\) has \(R^2=37\) and 20 contacts among the 240 vertices listed for that polytope in [1, Table 1]; \(\mathcal I_1(C_6)\) has \(R^2=54\) and two contacts. Attaching one leaf at each vertex of a triangle gives \(R^2=48\) and 12 contacts.

## Relationship to prior work

Glew [1] introduced in-in zonotopes with their Minkowski-sum and facet descriptions and investigated face structure and canonical forms. The inspected manuscript does not evaluate Euclidean minimum enclosing balls or classify their contacts. Padrol, Pilaud and Poullot [2] study deformation cones for graphical zonotopes, not this Euclidean invariant.

The published complete-multipartite graphical-zonotope radius theorem [3] concerns only the edge sum in its own intrinsic metric and complete multipartite graphs. The published cone law [4] concerns the full \((|V|+1)\)-coordinate Euclidean metric of the graphical zonotope of \(G*K_1\). Although [1] observes a **combinatorial** equivalence with that cone, deleting its apex coordinate changes Euclidean distances. For example, the doubled centered cone zonotope of \(K_4=C_3*K_1\) has squared radius 20, but \(\mathcal I_1(C_3)\) has squared radius 19. Neither result implies the odd-unicyclic degree-loss and contact-count theorem. Results on maximizing the *minimum* vertex imbalance in graph orientations [5] use a different optimization objective from the *sum of squared* imbalances appearing here. Standard central symmetry and source/sink orientation facts are used as tools, not presented as new.

## Limitations

The formula depends on the orthonormal coordinate realization, and is not invariant under arbitrary affine equivalence. It does not address higher-cycle-rank graphs, arbitrary coordinate and edge weights, or the limiting case \(t=0\). Literature searches and comparisons support provisional originality but cannot rule out an unindexed equivalent orientation-optimization result. No independent mathematical audit has been performed.

## References

1. R. Glew, *Geometry of in-in correlators*, arXiv:2601.18903v1, first public 2026-01-26, Section III, equations (10)–(14), Section V. https://arxiv.org/html/2601.18903
2. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, first published online 2023-10-13, *Discrete & Computational Geometry* 73 (2025), 447–465. https://doi.org/10.1007/s00454-023-00586-x
3. *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, published research record 2026-10-11, identifier `2026/10/11/SCOPE-complete-multipartite-graphical-zonotopes-have-cubic-moment-circ--2fc427ff213b`.
4. *Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes*, published research record 2026-10-11, identifier `2026/10/11/SCOPE-universal-euclidean-cone-law-and-farthest-point-rigidity-for-gra--19096c28cee4`.
5. W. Ben-Ameur, A. Glorieux and J. Neto, *On the most imbalanced orientation of a graph*, *J. Combin. Optim.* 36 (2018), 637–669. https://doi.org/10.1007/s10878-017-0117-1
