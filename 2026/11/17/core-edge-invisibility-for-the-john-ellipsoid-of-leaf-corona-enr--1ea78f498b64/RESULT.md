# Core-edge invisibility for the John ellipsoid of leaf-corona enriched chain polytopes

## Finding
Let \(H\) be any finite simple bipartite graph on labeled core vertices \(c_1,\ldots,c_r\), with \(r\ge1\). To each \(c_i\) attach \(p_i\ge1\) private pendant vertices \(\ell_{i,1},\ldots,\ell_{i,p_i}\), with no other edges incident to these new vertices. Denote the resulting graph by \(G\) and let \(N=r+\sum_i p_i\). Choose a bipartition of \(G\) and orient its edges from one color class to the other to obtain the height-two poset \(P_G\). Its enriched chain polytope is
\[
K_G=\operatorname{conv}\{x\in\{-1,0,1\}^{V(G)}:\operatorname{supp}(x)\text{ is an independent set of }G\}.
\]
The unique maximum-volume Euclidean inscribed ellipsoid, expressed in the standard coordinate metric, is
\[
\boxed{J_G=\left\{x:\sum_{i=1}^r\left((p_i+1)x_{c_i}^{2}+\frac{p_i+1}{p_i}\sum_{a=1}^{p_i}x_{\ell_{i,a}}^{2}\right)\le1\right\}.}\tag{1}
\]
Consequently **its entire center, shape, and volume are independent of all core edges of \(H\)**. Writing \(\kappa_N\) for the volume of the Euclidean unit ball,
\[
\boxed{\operatorname{Vol}_N(J_G)=\kappa_N\prod_{i=1}^r\left(\frac{p_i^{p_i}}{(p_i+1)^{p_i+1}}\right)^{1/2}.}\tag{2}
\]
Every pendant-edge facet \(\sigma x_{c_i}+\tau x_{\ell_{i,a}}\le1\), with \(\sigma,\tau\in\{-1,1\}\), is tangent to \(J_G\). A core-edge facet \(\sigma x_{c_i}+\tau x_{c_j}\le1\) is tangent **if and only if** \(p_i=p_j=1\). If at least one of these two leaf multiplicities is at least two, that facet is strictly nontangent; the exact Euclidean plane-to-ellipsoid clearance is
\[
\boxed{\delta_{ij}=\frac{1-\sqrt{(p_i+1)^{-1}+(p_j+1)^{-1}}}{\sqrt2}\ge\frac{1-\sqrt{5/6}}{\sqrt2}>0.}\tag{3}
\]
There are exactly \(4\bigl(\sum_i p_i+\#\{\{i,j\}\in E(H):p_i=p_j=1\}\bigr)\) tangent signed-edge facets. Thus an arbitrarily dense bipartite core can be added without changing the optimal ellipsoid; only the contact set remembers some of those edges.

## Assumptions and scope
The core \(H\) may be disconnected or have isolated vertices, but is bipartite and simple. The multiplicities \(p_i\) are positive integers. Pendant vertices have exactly one neighbor, their own core vertex. All norms, distances, and volumes refer to the original orthonormal coordinate basis of \(\mathbb R^{N}\). The ellipsoid is the maximum-**volume** inscribed ellipsoid, not the largest Euclidean ball or the minimum-volume enclosing ellipsoid. If \(r=1\), the result gives the exact star case. The graph \(G\) has no isolated vertices; its bipartiteness makes \(P_G\) a height-two poset with graph \(G\) as comparability graph.

## Proof
**1. The exact polytope and facet system.** Because \(G\) is bipartite, every clique has at most two vertices. A height-two poset with comparability graph \(G\) has chains of size one or two. The enriched chain-polytope inequalities are therefore precisely
\[
K_G=\left\{x\in\mathbb R^{V(G)}:\ |x_a|+|x_b|\le1\quad\text{for all }ab\in E(G)\right\}.\tag{4}
\]
The singleton coordinate restrictions follow from the edge inequalities because each vertex lies on an edge. Equivalence to the convex hull of signed independent sets follows from the chain-polytope description, or by applying the perfect-graph stable-set theorem separately in each orthant. In particular the body is full-dimensional and invariant under independent coordinate sign reversals. Every signed edge inequality is a genuine facet: at its point with the selected two coordinates equal to their prescribed signs times \(1/2\), all other coordinates zero, its own inequality is tight and every other edge inequality is strict. Varying locally within its hyperplane proves a codimension-one relative interior.

**2. Reduction to a strictly concave diagonal problem.** The John ellipsoid is unique. Invariance under each coordinate sign reversal forces its center to be the origin and its symmetric shape matrix to be diagonal. Write the squared coordinate semiaxes as \(u_v>0\). The support of the ellipsoid in any signed edge normal \(\sigma e_a+\tau e_b\) is \(\sqrt{u_a+u_b}\). Thus inclusion in (4) is exactly \(u_a+u_b\le1\) for every edge. Its volume is \(\kappa_N\sqrt{\prod_v u_v}\), and determining it is equivalent to
\[
\max\ \sum_{v\in V(G)}\log u_v\quad\text{over }u_v>0,\quad u_a+u_b\le1\ (ab\in E(G)).\tag{5}
\]
The objective is strictly concave, hence any feasible solution satisfying the supporting hyperplane inequality with nonnegative edge multipliers is the unique maximizer.

**3. Exact primal solution and positive dual weights.** Define
\[
\boxed{u_{c_i}=\frac1{p_i+1},\qquad u_{\ell_{i,a}}=\frac{p_i}{p_i+1}.}\tag{6}
\]
For a pendant edge these numbers add to one. For a core edge, their sum is at most \(1/2+1/2=1\). Thus (6) is feasible for **any** core edge set. Assign the nonnegative multiplier
\[
\lambda_{i,a}=\frac{p_i+1}{p_i}>0\tag{7}
\]
to each pendant-edge constraint and multiplier zero to every core edge. At a leaf the log-objective gradient is \(1/u_{\ell_{i,a}}=(p_i+1)/p_i=\lambda_{i,a}\). At its core it is
\[
\frac1{u_{c_i}}=p_i+1=\sum_{a=1}^{p_i}\lambda_{i,a}.\tag{8}
\]
Therefore \(\nabla \sum_v\log u_v\) is the positive linear combination of the active pendant-edge normals with weights (7). To prove global optimality without invoking any unverified regularity condition, let \(z\) be any other feasible positive vector. By concavity of log,
\[
\sum_v\log z_v-\sum_v\log u_v
\le\sum_v\frac{z_v-u_v}{u_v}
=\sum_{i,a}\lambda_{i,a}\bigl[(z_{c_i}+z_{\ell_{i,a}})-1\bigr]\le0.\tag{9}
\]
Strict concavity gives equality only when \(z=u\). The unique John ellipsoid is exactly (1). Taking the product of its squared semiaxes gives (2).

**4. Contact classification and sharp screening.** Every signed pendant-edge normal has ellipsoid support equal to \(1\), proving its facet is tangent. A core edge \(c_ic_j\) has support \(\sqrt{1/(p_i+1)+1/(p_j+1)}\). Since \(p_i,p_j\ge1\), this equals one precisely when both equal one. If at least one is at least two, the sum is at most \(1/2+1/3=5/6\), with equality possible. The support difference divided by the normal length \(\sqrt2\) is exactly the Euclidean distance between the supporting hyperplane and the ellipsoid, proving (3). All the facet inequalities are distinct, each edge has four independent signs, and there are no other facets by (4); counting tangent facets completes the classification.

**5. Sharp role of private leaves.** The condition of at least one leaf at every core vertex is not cosmetic: a core vertex with no private leaf would have squared semiaxis \(1\) in the free graph's box coordinate, and adding even one core edge would violate \(u_{c_i}+u_{c_j}\le1\) for every positive neighboring squared semiaxis. Thus a private leaf is the minimal local shield against arbitrary added core adjacencies. The sharp *contact* change occurs between one leaf (possible tangent core edge) and at least two leaves (uniform positive clearance), not at a graph-density threshold.

## Verification
The standalone `verify.py` checks every bipartite core edge subset on alternating-color labeled cores for \(1\le r\le5\) with all \(p_i\in\{1,2,3\}\), using exact rational arithmetic for primal feasibility, stationarity, contact classification, uniform clearance, and determinant volume. This consists of 363 multiplicity profiles and 16,977 core graphs and 215,979 exact edge checks. Independent constrained numerical log-volume optimization additionally checks 34 selected graphs against the formula. Running `python3 verify.py` prints:

`LEAF_CORONA_JOHN_PASS profiles=363 bipartite_graphs=16977 exact_edge_checks=215979 independent_numeric=34`

The exact rational tests and independent numerical optimization corroborate (1)--(3) in finite instances; arbitrary-size correctness follows from (4)--(9), not from enumeration.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes and the signed-antichain construction, while Okada and Tsuchiya gave explicit defining inequalities and enriched transfer-map results. Kohl, Olsen and Sanyal independently studied unconditional chain polytopes and their perfect-graph description. These papers provide the foundational polytope identification but do not present a Euclidean John-ellipsoid screening theorem for bipartite leaf coronae.

A subsequent geometric result, *A sharp entropy bound for John ellipsoids of enriched chain polytopes* (public finding `86ee65f9050d`), proves the general diagonal variational program (5), a width-sensitive volume lower bound, and a roundness criterion for all posets. Equation (5) is therefore background and **not** claimed as new here. The present contribution is the explicit exact solution for every bipartite leaf-corona graph, **arbitrary-core-edge invariance**, a positive all-dimensional dual certificate, and the precise contact-screening/clearance law for the added facets. An arbitrary core with heterogeneous \(p_i\) is generally not a layered poset; existing layered equality cases do not determine the result. Exact KKT specialization is a possible earlier formulation, so historical priority is not claimed as established. Ordinary nonnegative chain polytopes and stable-set relaxations do not have the independent-sign-reflection symmetry used here and their John ellipsoids need not agree.

## Limitations
The construction requires bipartiteness of the core and at least one pendant vertex per core vertex; it makes no claim for arbitrary non-bipartite cores, for an absent private leaf, or under nonorthogonal changes of metric. A sufficient local shielding condition is proved, not a classification of every graph whose core edges are invisible. Classical graph-entropy formulations might encode the same optimum and are a residual novelty risk. The case of identical leaf multiplicities can be simplified by symmetry, but heterogeneous multiplicities and arbitrary core topology are essential to the stated structural scope.

## References
1. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097, first public posting 2018-12-05; Israel J. Math. 237 (2020), 485--500.
2. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271, first public posting 2020-03-27; Ann. Comb. 28 (2024), 257--282.
3. F. Kohl, M. Olsen and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete Comput. Geom. 64 (2020), 427--452, DOI:10.1007/s00454-020-00199-8.
4. *A sharp entropy bound for John ellipsoids of enriched chain polytopes*, publicly accessible geometric research record `2026/11/8/SCOPE-a-sharp-entropy-bound-for-john-ellipsoids-of-enriched-chain-poly--86ee65f9050d`, online 2026-11-08.
5. F. John, *Extremum problems with inequalities as subsidiary conditions*, in Studies and Essays Presented to R. Courant (1948), 187--204, the classical existence and uniqueness theory for maximal-volume inscribed ellipsoids.
