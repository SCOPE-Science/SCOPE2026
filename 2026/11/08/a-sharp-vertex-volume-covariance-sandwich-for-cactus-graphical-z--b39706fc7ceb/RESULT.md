# A sharp vertex–volume covariance sandwich for cactus graphical zonotopes

## Finding

Let \(G=(V,E)\) be any connected finite simple cactus graph with \(n=|V|\ge2\), meaning every edge belongs to at most one undirected simple cycle. Equip \(\mathbb R^V\) with its ordinary Euclidean metric and put
\[
Z_G=\sum_{\{u,v\}\in E}
\left[-\frac{e_u-e_v}{2},\frac{e_u-e_v}{2}\right]
\subset\mathbf 1^\perp.
\]
Let \(X_{\mathrm v}\) be uniform over the **distinct vertices** of \(Z_G\), and let \(X_{\mathrm a}\) be uniform by intrinsic \((n-1)\)-dimensional Euclidean volume. Define \(C_{\mathrm v}=\operatorname{Cov}(X_{\mathrm v})\) and \(C_{\mathrm a}=\operatorname{Cov}(X_{\mathrm a})\).

Write \(B\) for the set of bridges, \(\mathcal C\) for the set of simple cycles, \(\ell_C=|E(C)|\), and \(L_F=\sum_{\{u,v\}\in F}(e_u-e_v)(e_u-e_v)^{\mathsf T}\). Then the two covariance matrices are **exactly**
\[
\begin{aligned}
C_{\mathrm v}&=\frac14L_B+
\sum_{C\in\mathcal C}
\frac{2^{\ell_C-1}}{4(2^{\ell_C-1}-1)}L_{E(C)},\\
C_{\mathrm a}&=\frac1{12}L_B+
\sum_{C\in\mathcal C}
\frac{\ell_C+2}{12\ell_C}L_{E(C)}.
\end{aligned}
\]
Both have kernel precisely \(\operatorname{span}\{\mathbf1\}\). In the positive-semidefinite (Loewner) ordering, the **sharp universal comparison** is
\[
\boxed{\frac{16}{7}C_{\mathrm a}\preccurlyeq C_{\mathrm v}
\preccurlyeq 3 C_{\mathrm a}.}
\]
Equality of the *matrices* in the upper bound holds exactly for trees. Equality in the lower bound holds exactly when the graph has no bridges and every cycle has length \(4\) or \(5\); in particular the cycles of both lengths have **identical** vertex-to-volume covariance ratio \(16/7\). Both constants are attained, so neither can be improved over the class of all cacti.

The generalized-variance ratio is an exact cycle-length invariant:
\[
\boxed{
\frac{\operatorname{pdet} C_{\mathrm v}}
{\operatorname{pdet} C_{\mathrm a}}
=3^{|B|}\prod_{C\in\mathcal C}
\left(\frac{3\ell_C\,2^{\ell_C-1}}
{(\ell_C+2)(2^{\ell_C-1}-1)}\right)^{\ell_C-1}.}
\]
Here \(\operatorname{pdet}\) is the product of the \(n-1\) positive eigenvalues. This ratio depends only on bridge count and cycle lengths, not on the pattern of articulation-vertex attachments.

## Assumptions and scope

All edge generators have unit coefficient. Covariances use the normalized **probability** measures, not sums over vertices or unnormalized moments. The convex body has intrinsic dimension \(n-1\) in \(\mathbf1^\perp\), and all positive eigenvalues, determinants, and semidefinite comparisons are interpreted on this fixed canonical Euclidean realization. The empty cycle product equals \(1\). The statement includes trees as cacti with no cycles and a single-edge graph as its smallest case. Neither variable edge weights nor graphs with overlapping simple cycles are covered.

## Proof

**1. Block decomposition.** Each edge is either a bridge or lies in one simple cycle. Any directed cycle must occur entirely within one of those cycle blocks, so an edge orientation is acyclic precisely when each simple-cycle orientation avoids its two coherent cyclic orientations; bridge orientations are unrestricted. Thus uniformly chosen acyclic orientations factor independently across these edge-disjoint blocks. The standard graphical-zonotope vertex correspondence identifies distinct vertices bijectively with acyclic orientations. The edge-incidence spans of the blocks are a direct sum: every linear dependence among the edge-incidence vectors is supported on cycles, and different blocks have disjoint edge sets. Their dimensions sum to \(n-1\). Consequently addition of block zonotopes is the image of a Cartesian product under a nonsingular linear map with constant Jacobian. Uniform intrinsic volume likewise factors into independent uniform block-volume measures.

**2. Vertex-uniform covariance on a cycle.** Orient the edges of a cycle of length \(\ell\ge3\) cyclically and denote the resulting incidence columns by \(b_1,\ldots,b_\ell\). Their sum is zero. The centered vertex random vector from this block is \(Y=\frac12\sum_i\sigma_i b_i\), where \(\sigma\) is uniform on \(\{-1,1\}^\ell\) with its all-plus and all-minus points removed. By global sign reversal, \(\mathbb E\sigma_i=0\); direct enumeration gives
\[
\mathbb E[\sigma_i\sigma_j]=
\begin{cases}1&i=j,\\-\dfrac1{2^{\ell-1}-1}&i\ne j.\end{cases}
\]
Let \(c=(2^{\ell-1}-1)^{-1}\). Then \(\operatorname{Cov}(\sigma)=(1+c)I-c\mathbf1\mathbf1^{\mathsf T}\). As \(\sum_i b_i=0\), the rank-one term disappears upon multiplication by the incidence matrix. Therefore
\[
\operatorname{Cov}(Y)=\frac{2^{\ell-1}}{4(2^{\ell-1}-1)}
\sum_i b_ib_i^{\mathsf T}.
\]
For a bridge, independent symmetric choice of its endpoints yields \(b_eb_e^{\mathsf T}/4\). Adding independent blocks gives the first covariance formula.

**3. Intrinsic-volume covariance on a cycle.** Consider the same cycle zonotope as the image of \([0,1]^\ell\) by \(t\mapsto\sum_i t_i b_i\); this is the centered zonotope because \(\sum_i b_i=0\). Modulo the common-shift direction \(\mathbf1\), every cube image has a unique representative with minimum coordinate zero, except on measure-zero boundaries. These representatives split into \(\ell\) nonoverlapping full-dimensional parallelotopes, one for each omitted index \(j\):
\[
(t_1,\ldots,t_\ell)=(U_1,\ldots,U_{j-1},0,U_{j+1},\ldots,U_\ell),
\quad U_i\stackrel{\rm iid}{\sim}\operatorname{Unif}[0,1].
\]
All parallelotopes have equal Euclidean volume because \(b_j=-\sum_{i\ne j}b_i\) makes their maximal incidence minors equal in absolute value. Consequently uniform cycle-volume sampling is exactly: choose \(j\) uniformly, then choose the remaining \(U_i\) independently uniformly. Conditional on \(j\), the mean is \(-b_j/2\) and covariance is \(\sum_{i\ne j}b_ib_i^{\mathsf T}/12\). The law of total covariance yields
\[
\operatorname{Cov}_{\mathrm a}(Y)
=\frac{\ell-1}{12\ell}\sum_i b_ib_i^{\mathsf T}
+\frac1{4\ell}\sum_i b_ib_i^{\mathsf T}
=\frac{\ell+2}{12\ell}\sum_i b_ib_i^{\mathsf T}.
\]
The bridge interval contributes \(b_eb_e^{\mathsf T}/12\). The block direct-sum argument proves the second covariance identity for the full zonotope.

**4. Sharp Loewner comparison.** Both matrices are weighted graph Laplacians with positive weights. The ratio of the vertex to volume weights is \(3\) on bridges and, on a cycle of length \(\ell\),
\[
R_\ell=\frac{3\ell\,2^{\ell-1}}
{(\ell+2)(2^{\ell-1}-1)}.
\]
Direct exact arithmetic gives \(R_3=12/5\) and \(R_4=R_5=16/7\). The sign of \(R_{\ell+1}-R_\ell\) for \(\ell\ge3\) is the sign of \(2(2^\ell-2)-\ell(\ell+3)\), negative for \(\ell=3\), zero for \(\ell=4\), and positive for all \(\ell\ge5\): the last assertion follows by induction from its positive value at \(\ell=5\), since its next difference is \(2^{\ell+1}-2\ell-4>0\). Hence \(R_\ell\ge16/7\). Moreover \(R_\ell<3\) is equivalent to \(2^\ell>\ell+2\), valid for \(\ell\ge3\). Each block contribution is positive semidefinite. Summing its coefficient inequalities proves the matrix sandwich. A nonzero positive coefficient difference gives a nonzero positive-semidefinite matrix because its trace is positive. Thus matrix equality holds in exactly the stated block configurations.

**5. Generalized variance.** For any positive-weighted connected graph Laplacian \(L_w\), the matrix-tree theorem gives \(\operatorname{pdet}L_w=n\tau_w(G)\). Every spanning tree of a cactus contains each bridge and removes precisely one edge from each cycle. If all edges of a cycle of length \(\ell\) have common weight \(w_C\), the total weighted tree count is \(w_B^{|B|}\prod_C\ell_Cw_C^{\ell_C-1}\). Applying this identity to the two covariance Laplacians and dividing cancels the cycle-length factors and produces the stated product.

## Verification

Run `python3 artifacts/verify.py` with standard-library Python. It exhaustively enumerates acyclic orientations, reconstructs their distinct vertices, and computes exact-rational vertex covariance for thirteen cacti; separately it integrates the parallelotope-tile mixture to obtain exact volume covariances. It compares both matrices entry-by-entry against the formulas, checks their Laplacian cofactors against the cactus spanning-tree product, and checks the local ratio at cycle lengths from \(3\) through \(150\). It also checks a noncactus counterexample to unqualified sparsity extension. The reported successful replay is `CACTUS_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED profiles=13 vertices=2318 matrix_entries=900 cycle_lengths=148`. The infinite assertions follow from the proof, not from finite enumeration.

## Relationship to prior work

The acyclic-orientation/graphical-zonotope correspondence and standard unit-incidence realization are classical, and are reviewed by Padrol, Pilaud, and Poullot, *Deformed Graphical Zonotopes* (first public version 2021-11-24), and Bach, Beck, and Rehberg, *Acyclotopes and Tocyclotopes* (first public version 2024-09-23). Pešović and Stojadinović (first public version 2022-09-24) study interpolations between graphical zonotopes and graph associahedra. Their deformation-cone, Ehrhart, and combinatorial enumerator statements do not yield the covariance sandwich or generalized-variance ratio. An independently recorded volume-only covariance formula for cactus zonotopes is logically weaker: it does not determine the vertex-uniform law, the two-sampling sharp constants, or their equality cases.

## Limitations

The graph must be a connected simple cactus and the Euclidean generators must be unweighted. The covariance inequalities need not be valid for other graph families or weighted realizations. For example, with vertex labels in the two parts of \(K_{2,3}\), uniform vertex covariance between the two nonadjacent vertices of the two-vertex part is \(-3/92\), unlike the sparse weighted-Laplacian formula above. No distributional comparison stronger than second moments is claimed. The literature comparison is evidence of noncoverage among inspected sources, not a proof of global historical priority. Independent mathematical audit has not been performed.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first public 2021-11-24); open-access journal text: https://doi.org/10.1007/s00454-023-00586-x .
2. M. Pešović, T. Stojadinović, *Between Graphical Zonotope and Graph-Associahedron*, arXiv:2209.12053 (first public 2022-09-24); https://doi.org/10.55730/1300-0098.3434 .
3. E. Bach, M. Beck, S. Rehberg, *Acyclotopes and Tocyclotopes*, arXiv:2409.15227 (first public 2024-09-23).
4. Matrix-tree theorem and the standard acyclic-orientation correspondence for graphical zonotopes, used as established background in References 1 and 3.
