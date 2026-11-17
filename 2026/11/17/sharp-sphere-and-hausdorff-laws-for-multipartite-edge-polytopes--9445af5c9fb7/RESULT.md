# Sharp sphere and Hausdorff laws for multipartite edge polytopes

## Finding
For any complete multipartite graph \(G=K_{a_1,\ldots,a_r}\) with \(r\ge2\) and all \(a_j\ge1\), put \(N=\sum_j a_j\), \(A=\max_j a_j\), and \(B=N-A\). In standard Euclidean \(\mathbb R^N\), write
\[
 P_G=\operatorname{conv}\{e_u+e_v:uv\in E(G)\},\qquad
 \Delta_{2,N}=\operatorname{conv}\{e_u+e_v:1\le u<v\le N\}.
\]
The minimum enclosing Euclidean ball of \(P_G\) is unique and has squared radius
\[
 R_G^2=\begin{cases}
 2-4/N,&2A\le N,\\
 2-1/A-1/B,&2A>N.
 \end{cases}
\]
If \(2A\le N\), its center is \(c=(2/N)\mathbf1\), and **every** edge vertex contacts its sphere. If \(2A>N\), the largest class \(V_*\) is unique; the center has coordinates \(1/A\) on \(V_*\) and \(1/B\) off \(V_*\). Exactly the \(AB\) edge vertices meeting \(V_*\) contact the sphere. Every other edge vertex lies strictly inside, with squared-radius clearance \(2(1/B-1/A)\) (when such an edge exists).

If \(A\ge2\), the Euclidean Hausdorff distance to the full second hypersimplex is
\[
 d_H(P_G,\Delta_{2,N})=\sqrt{\frac12+\frac1B}.
\]
The **entire farthest-point set** in \(\Delta_{2,N}\) consists exactly of its missing edge vertices \(e_u+e_v\) for which \(u,v\) belong to a part of size \(A\). For an arbitrary missing edge vertex \(z=e_u+e_v\) inside a class \(V_j\) of size \(a_j\ge2\), the unique nearest point in \(P_G\) is
\[
 y_z=\frac12(e_u+e_v)+\frac{1}{N-a_j}\mathbf1_{V\setminus V_j},
\]
with squared distance \(\|z-y_z\|^2=\tfrac12+1/(N-a_j)\). If \(A=1\), then \(P_G=\Delta_{2,N}\) and the Hausdorff distance is zero.

In particular, when \(A\ge2\) but \(2A\le N\), the two polytopes share their **exact same minimum enclosing ball** even though their Hausdorff gap is at least \(1/\sqrt2\). At the sharp threshold \(2A=N\), no edge vertex has left the optimal sphere; strict loss of contact begins only for \(2A>N\) (provided the complement contains an edge). For instance, \(K_{3,3,3}\) has the same smallest Euclidean sphere as \(\Delta_{2,9}\) but has Hausdorff gap \(\sqrt{2/3}\). In contrast, for \(K_{8,2,2}\), the four edges between the two smaller classes are strictly interior to the optimal sphere, with squared-distance clearance \(1/4\).

## Assumptions and scope
All edges are undirected, graphs are simple, the multipartite classes are nonempty, and Euclidean distances use the inherited ambient coordinate metric. The affine hull of \(P_G\) is allowed to have lower dimension (in particular for bipartite graphs). Radius means the smallest Euclidean radius of a ball containing the entire polytope, not the radius of an arbitrarily selected sphere through its vertices. Hausdorff distance is symmetric, and the direction from \(P_G\) to \(\Delta_{2,N}\) is zero by inclusion. The case \(N=2\) is covered by the all-singleton exception.

## Proof
**1. A fixed-norm minimax lemma.** Let \(V\subset\mathbb R^d\) be finite, all of whose members have the same squared norm \(s\), and let \(p\) be the unique point of least squared norm in \(\operatorname{conv}(V)\). Then the smallest enclosing ball of \(V\) has center \(p\) and squared radius \(s-\|p\|^2\). Indeed the projection inequality \(\langle p,v-p\rangle\ge0\) gives \(\|v-p\|^2\le s-\|p\|^2\). Conversely, choose weights \(w_v\ge0\), summing to one, with \(p=\sum_v w_vv\). For any candidate center \(z\),
\[
 \max_v\|v-z\|^2\ge\sum_vw_v\|v-z\|^2=s-\|p\|^2+\|z-p\|^2.
\]
These inequalities establish optimality, uniqueness, and the contact condition \(\langle p,v\rangle=\|p\|^2\).

**2. Projecting zero onto the multipartite edge polytope.** For \(x\in P_G\), let \(t_j=\sum_{u\in V_j}x_u\). Every edge uses two different classes, so \(0\le t_j\le1\) and \(\sum_jt_j=2\). Conversely, the class-incidence vectors of allowed edges are precisely the vertices of the rank-two hypersimplex \(\Delta_{2,r}\). Consequently every \(t\in[0,1]^r\) with \(\sum_jt_j=2\) is feasible; uniformly distributing class-pair edge weights over each complete bipartite block realizes an \(x\) constant on every class. For fixed class sums, Cauchy--Schwarz gives
\[
 \sum_{u\in V_j}x_u^2\ge t_j^2/a_j,
\]
with equality only for constant coordinates on that class. It therefore suffices to minimize \(\sum_jt_j^2/a_j\) over \(0\le t_j\le1\), \(\sum t_j=2\). Strict convexity makes the minimizer unique; the elementary KKT conditions give \(t_j=\min\{1,\lambda a_j\}\) for a nonnegative \(\lambda\), with the obvious forced-value interpretation for \(r=2\). At most one class can be strictly capacity-saturated when \(r\ge3\).

If \(2A\le N\), the unconstrained minimizer \(t_j=2a_j/N\) is feasible. Therefore \(p=(2/N)\mathbf1\), with \(\|p\|^2=4/N\). If \(2A>N\), exactly the largest class saturates, with \(t_*=1\) and \(t_j=a_j/B\) for other classes, so \(p\) has coordinates \(1/A\) and \(1/B\) and norm squared \(1/A+1/B\). Each edge vector has squared norm \(2\). The lemma gives the stated centers and radii. In the balanced regime every edge has the same inner product \(4/N\) with \(p\). In the dominant regime, meeting edges have inner product \(1/A+1/B=\|p\|^2\), whereas edges entirely outside the largest class have inner product \(2/B\), exceeding \(\|p\|^2\) by \(1/B-1/A>0\). This yields all contacts and clearances, including equality at \(2A=N\).

**3. Exact projection of every forbidden vertex.** Fix \(z=e_u+e_v\) with \(u,v\in V_j\) and \(a_j\ge2\), and write \(b=N-a_j\). For any \(x\in P_G\), the mass \(t=\sum_{i\in V_j}x_i\) lies in \([0,1]\), while the mass on the complement is \(2-t\). Since \(x_u+x_v\le t\), Cauchy--Schwarz applied first to the two target coordinates and then to the \(b\) complement coordinates gives
\[
 \|z-x\|^2\ge\frac{(2-t)^2}{2}+\frac{(2-t)^2}{b}
 \ge\frac12+\frac1b.
\]
Equality requires \(t=1\), \(x_u=x_v=1/2\), zero mass on the other coordinates of \(V_j\), and a uniform complement of mass one. These conditions specify \(y_z\) uniquely. The candidate is feasible, because it is the average of the \(2b\) allowed cross-edge vertices \(e_u+e_w\) and \(e_v+e_w\), for \(w\notin V_j\). This proves the claimed nearest point and distance.

**4. Global Hausdorff gap and all farthest points.** The convex function \(x\mapsto\operatorname{dist}(x,P_G)\) attains its largest value on \(\Delta_{2,N}\) at a vertex, and step 3 shows the maximum among omitted vertices is \(\sqrt{1/2+1/(N-A)}\). For completeness, let \(x=\sum_v\alpha_vv\) be any convex combination of hypersimplex vertices and let \(y_v\) denote the closest point of \(P_G\) to each such vertex. Then
\[
 \operatorname{dist}(x,P_G)\le\Bigl\|\sum_v\alpha_v(v-y_v)\Bigr\|
 \le\sum_v\alpha_v\|v-y_v\|\le D,
\]
where \(D\) is the maximum vertex distance. Equality at positive \(D\) requires every positively weighted vertex to have distance \(D\) and all its nonzero residual vectors \(v-y_v\) to be identical (equality in the Euclidean triangle inequality with equal lengths). Such residuals have positive entries exactly at the two missing endpoints and negative entries on the complement of their class, so different missing vertices give different residuals. Hence equality can hold only at one omitted vertex from a largest class. This also proves the complete farthest-point classification.

## Verification
The exact-rational script `checker.py` enumerates all unordered positive integer part-size profiles with totals from three through twelve and at least two classes. It checks the squared-radius formulas, equality/strictness of every allowable edge contact, the projected distance of every forbidden edge, and nonnegative first-order projection certificates against every permissible edge vertex. The reproducible result is `MULTIPARTITE_EDGE_METRIC_EXACT_PASS profiles=258 contact_edges=8704 strictly_inner_edges=198 missing_vertex_projections=3150`. Ten additional sample profiles were checked by an independently formulated numerical minimax optimization for the enclosing ball. Finite tests are not used in lieu of any infinite-parameter proof step.

## Relationship to prior work
Tran and Ziegler (arXiv:1307.6708, 2013) describe general graph edge polytopes as subpolytopes of the second hypersimplex and study their face structure and extremal face counts. Higashitani and Matsushita (arXiv:2102.02349, first public 2021-02-04) study the same complete multipartite edge polytopes through their edge rings, levelness and almost Gorensteinness. Neither inspected full article states the Euclidean smallest-ball, sphere-contact, Hausdorff, and deep-point classification here. A 2023 MathOverflow discussion about whether the equidistant circumcenter belongs to a matroid base polytope gives a negative parallel-element example, motivating the distinction between a vertex sphere and the minimum enclosing ball. Related published work on rank-two matroid base polytopes concerns inradii, Minkowski asymmetry, or Gaussian angles; these invariants do not imply the stated nearest-point and optimal-sphere formulas. The separate ingredients (Euclidean projection and convexity inequalities) are standard, but their sharp all-profile synthesis is not credited to an earlier source in the accessible comparisons.

## Limitations
The theorem is for standard equal-coordinate Euclidean metric and the rank-two complete multipartite family only. It does not treat general graph edge polytopes, weighted edge vectors, or higher-rank partition-matroid bases. Historical priority is provisional: semantic searches and primary text inspection are not a proof of novelty, and some published records were available only as indexed summaries. Independent mathematical audit has not been performed.

## References
- A. Higashitani and K. Matsushita, *Levelness versus almost Gorensteinness of edge rings of complete multipartite graphs*, arXiv:2102.02349 (2021-02-04 first public submission), Sections 1 and 3--4, https://arxiv.org/abs/2102.02349.
- T. Tran and G. M. Ziegler, *Extremal Edge Polytopes*, arXiv:1307.6708 (2013-07-25 first public submission), Sections 1--2 and 3--5, https://arxiv.org/abs/1307.6708.
- M. Winter and F. Petrov, *Does a matroid base polytope contain its circumcenter?*, MathOverflow question and answer (2023-08-12), https://mathoverflow.net/questions/452600/does-a-matroid-base-polytope-contain-its-circumcenter.
