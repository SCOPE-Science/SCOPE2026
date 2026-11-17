# Barycentric projection simplices and exact deep-hole shells of multipartite PQ adjacency polytopes

## Finding
For integers \(r\ge2\) and \(p_1,\ldots,p_r\ge1\), write \(n=\sum_s p_s\), and let \(G=K_{p_1,\ldots,p_r}\) be the complete multipartite graph on \([n]\). Assume at least one part contains two or more vertices. Define
\[
Q=\Delta_{n-1}\times\Delta_{n-1},\qquad
P_G=\operatorname{conv}\{(e_u,e_v):u=v\text{ or }u,v\text{ lie in different parts}\}\subset Q,
\]
with the Euclidean metric inherited from \(\mathbb R^{2n}\). Fix distinct indices \(i,j\) in one part \(C\) of size \(p\), and set \(O=[n]\setminus C\), \(q=n-p\ge1\). The \(2(q+1)\) permitted product vertices
\[
\mathcal V_{ij}=\{(e_i,e_i),(e_j,e_j)\}\cup
 \{(e_i,e_h),(e_h,e_j):h\in O\}
\]
span an **exposed simplex face** \(F_{ij}\) of dimension \(2q+1\). Its barycenter \(\pi_{ij}\) is the unique Euclidean nearest point of the missing product vertex \(v_{ij}=(e_i,e_j)\), and
\[
\operatorname{dist}_2(v_{ij},P_G)^2=\frac{q+2}{2(q+1)},\qquad
\operatorname{vol}_{2q+1}(F_{ij})=\frac{\sqrt{2(q+1)(q+2)}}{(2q+1)!}.
\]
The complete squared-distance spectrum, including zero distances, is therefore described by the following table of **vertex multiplicities**: distance \(0\) occurs at every permitted product vertex; for each part size \(p\ge2\) appearing in the graph, squared distance \((n-p+2)/(2(n-p+1))\) occurs exactly \(\sum_{s:p_s=p}p_s(p_s-1)\) times. No two distinct part sizes give the same positive squared distance.

Let \(p_*=\max_s p_s\ge2\), \(q_*=n-p_*\). Then the **entire continuous** Hausdorff distance and all its maximizers are
\[
\boxed{d_H(Q,P_G)=\sqrt{\frac{q_*+2}{2(q_*+1)}}}.
\]
Precisely the missing ordered vertices \((e_i,e_j)\) belonging to parts of maximum size attain this distance; no nonvertex point of \(Q\) attains it.

## Assumptions and scope
The standard simplex \(\Delta_{n-1}\) has vertices \(e_1,\ldots,e_n\) and lies in \(\mathbb R^n\). Intrinsic simplex-face volumes and ambient distances always use the induced, unscaled Euclidean inner product, not normalized lattice volume. The affine dimension of \(P_G\) is \(2n-2\), since \(G\) is connected: differences between \((e_i,e_i)\) and permitted off-diagonal vertices span the row and column zero-sum subspaces. The Hausdorff distance is symmetric because \(P_G\subseteq Q\). The case of all singleton parts has \(P_G=Q\), zero Hausdorff distance, and is excluded from statements about unique deep holes. For a missing pair, its containing class size is always at least two and its complementary size \(q\) at least one.

## Proof
**1. Exact supporting-hyperplane projection.** Fix a missing pair \((i,j)\), and write \(a=1/[2(q+1)]\). Let \(\pi\) be the equally weighted average of the vertices of \(\mathcal V_{ij}\), and \(R=(e_i,e_j)-\pi\). The row block of \(R\) has coordinate \(1/2\) at \(i\), coordinate \(-a\) at \(j\) and every \(h\in O\), and zero elsewhere. The column block has coordinate \(1/2\) at \(j\), coordinate \(-a\) at \(i\) and each \(h\in O\), and zero elsewhere. Every allowed generator \((e_u,e_v)\) has inner product \(R_u^{\mathrm{row}}+R_v^{\mathrm{col}}\le b=1/2-a\). Equality holds **exactly** for the \(2(q+1)\) generators in \(\mathcal V_{ij}\): the two diagonal generators, the \(q\) pairs \((i,h)\), and the \(q\) pairs \((h,j)\). Thus \(F_{ij}\) is exposed and \(\pi\in\operatorname{relint} F_{ij}\). Since \(\langle R,z-\pi\rangle\le0\) for all \(z\in P_G\), the Euclidean projection theorem establishes that \(\pi\) is the unique nearest point of \((e_i,e_j)\). Taking the squared Euclidean norm of \(R\) yields
\[
\|R\|_2^2=2\left(\frac14+(q+1)a^2\right)
=\frac12+\frac1{2(q+1)}=\frac{q+2}{2(q+1)}.
\]

**2. The projection face is an explicit simplex, including its metric size.** Regard a generator \((e_u,e_v)\) as the incidence column of an edge from row node \(u\) to column node \(v\) in a bipartite graph with \(2n\) nodes. The \(2q+2\) active edges form two disjoint stars: one centered at row \(i\) and adjacent to column \(i\) and all columns \(h\in O\), the other centered at column \(j\) and adjacent to row \(j\) and all rows \(h\in O\). Because this is a forest, the incidence columns are linearly independent. Their convex hull is a simplex of dimension \(2q+1\), and its listed generators are all its vertices.

Partition those vertices into the two \(q\)-simplices in the two star components. Each is a standard regular \(q\)-simplex of intrinsic volume \(\sqrt{q+1}/q!\); their tangent spaces are orthogonal. The vector joining their barycenters is perpendicular to both tangent spaces and has squared length \(2(q+2)/(q+1)\). The Gram determinant of the \(2q+1\) edge vectors based at one simplex vertex is consequently \(2(q+1)(q+2)\): equivalently, take a vertex from each component and use a spanning edge basis inside the two stars together with the barycenter connector; its determinant is unchanged by barycentric elementary column operations. Therefore
\[
\operatorname{vol}_{2q+1}(F_{ij})
=\frac{\sqrt{2(q+1)(q+2)}}{(2q+1)!}.
\]

**3. Complete distance shells and Hausdorff extremizers.** The product \(Q\) has exactly \(n^2\) vertices \((e_u,e_v)\). The permitted ones belong to \(P_G\) and have zero distance; each part of size \(p\) contributes \(p(p-1)\) missing ordered vertices, all with the squared distance just calculated. The function \((q+2)/(2(q+1))\) is strictly decreasing in integer \(q\ge1\), hence the maximum among product vertices occurs exactly inside largest parts. Distance to a closed convex set is a convex function, so its maximum over \(Q\) equals its maximum over the vertices.

To classify equality in the **continuous** cube-product, choose a convex representation \(x=\sum_v\lambda_vv\) using the product vertices, and let \(\pi_v\) be each nearest point in \(P_G\). Put \(R_v=v-\pi_v\). The convex combination \(\sum_v\lambda_v\pi_v\) is feasible, so
\[
\operatorname{dist}_2(x,P_G)^2\le\left\|\sum_v\lambda_vR_v\right\|^2
=\sum_v\lambda_v\|R_v\|^2
-\sum_{v<w}\lambda_v\lambda_w\|R_v-R_w\|^2.
\]
A product vertex already in \(P_G\) has residual zero. Every missing product vertex \((e_i,e_j)\) has residual with its unique positive row coordinate at \(i\) and its unique positive column coordinate at \(j\), hence distinct missing vertices have different residual vectors. The maximum distance is strictly positive. If \(x\) involves at least two distinct product vertices, either a vertex in its representation has submaximal distance or the strictly positive cross-term makes the displayed inequality strict. Thus no nonvertex point attains the maximum, and the stated list of deepest missing vertices is exhaustive.

## Verification
The standalone script `checks/check_pq.py` builds the entire permitted product-vertex set for 16 multipartite class profiles, including unequal parts, singleton parts, two-part graphs and multi-part graphs. For each of 140 forbidden ordered vertices it computes the predicted barycentric projection independently of the optimization solver, checks the supporting-normal equalities and strict inequalities against **all** permitted generators, checks affine independence and the face Gram determinant, and solves the Euclidean squared-distance minimization over all permitted generators using SciPy SLSQP. The checks passed, returning `PQ_MULTIPARTITE_METRIC_PASS cases=16 missing_vertices=140 exact_dual_and_affine_and_gram=140 independent_QP=140`. Execute using `OPENBLAS_NUM_THREADS=1 python checks/check_pq.py` with Python, NumPy and SciPy. These finite checks corroborate, but do not substitute for, the all-parameter proof above.

## Relationship to prior work
Ohsugi and Tsuchiya [1] study exactly this PQ-type graph-adjacency construction for join and complete multipartite graphs and determine Ehrhart polynomials and normalized volumes. Their formulas do not give nearest-point projection of missing product vertices, metric projection faces, Euclidean facet volumes of those faces, or the Hausdorff deep-hole classification proved here. Davis and Chen [2] establish the graph-adjacency-polytope setting and combinatorial normalized-volume formulas.

An earlier result concerning *crown-graph root polytopes* determines the Hausdorff distance when all forbidden product vertices form a perfect matching. **That earlier result covers the special case in which every multipartite class has exactly two vertices**, by permuting the column indices. The present claim does not assert novelty for that special case; its new geometric content is the general arbitrary-part-size formula, full distinct distance shells, and the growing-dimensional exposed simplex projection faces. A separate earlier calculation of Gaussian spherical-width exposure for bipartite PQ adjacency polytopes [3] concerns stochastic directional support functions rather than the full nearest-point map. Volume, Ehrhart and Gaussian-width formulas do not imply this result.

## Limitations
The metric formulas are specific to the standard coordinate realization \(\mathbb R^{2n}\) and need not survive arbitrary affine transformations or coordinate reweighting. There is no statement about noncomplete multipartite graphs or about projection of arbitrary interior points of \(Q\); the exact projection formula is for all missing **vertices**, and the continuous Hausdorff extremizer theorem covers all points. The all-singleton case is excluded. Historical priority beyond the inspected references is provisional, particularly in transportation-polytope metric-projection terminology. No independent mathematical audit has been performed.

## References
[1] H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045 (first public version 2021-03-28), *Discrete & Computational Geometry* 70 (2023), 214–235, DOI 10.1007/s00454-022-00447-z. https://arxiv.org/abs/2103.15045

[2] R. Davis and T. Chen, *Computing Volumes of Adjacency Polytopes via Draconian Sequences*, arXiv:2007.11051 (initial preprint 2020-07-21), *Electronic Journal of Combinatorics* 29 (2022), P1.61. https://arxiv.org/abs/2007.11051

[3] Published geometric work on Gaussian exposure of bipartite PQ adjacency polytopes, 2026; comparison restricted to the stated spherical-width and exposure conclusions.
