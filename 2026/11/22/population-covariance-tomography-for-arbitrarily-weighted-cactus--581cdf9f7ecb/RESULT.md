# Population-covariance tomography for arbitrarily weighted cactus graphical zonotopes

## Finding
Let \(G=(V,E)\) be a finite connected simple cactus graph with \(n=|V|\ge2\), and assign an **independent positive real length** \(a_e\) to every edge. Write \(b_e=e_u-e_v\in\mathbb R^V\) with either orientation, and form the centered graphical zonotope
\[
Z(G,a)=\sum_{e\in E}\left[-\frac{a_e}{2}b_e,\frac{a_e}{2}b_e\right]\subset\mathbf1^\perp.
\]
Sample \(X\) uniformly from its intrinsic \((n-1)\)-dimensional Euclidean volume, and write \(\Sigma=\operatorname{Cov}(X)\). For each cycle \(C\), set
\[
H_C=\sum_{f\in E(C)}\frac1{a_f}.
\]
Then the complete covariance is the following **positive weighted graph Laplacian**:
\[
\boxed{\displaystyle
\Sigma=\sum_{e\text{ bridge}}\frac{a_e^2}{12}b_eb_e^{\mathsf T}+
\sum_{C}\sum_{e\in E(C)}\left(\frac{a_e^2}{12}+\frac{a_e}{6H_C}\right)b_eb_e^{\mathsf T}.}
\tag{1}
\]
Moreover, **the exact labeled covariance matrix alone uniquely determines both the unknown cactus graph and all its positive edge lengths**. For distinct vertices, \(uv\in E\) if and only if \(\Sigma_{uv}<0\); otherwise \(\Sigma_{uv}=0\). Put \(c_{uv}=-\Sigma_{uv}>0\) on recovered edges. Bridge lengths are \(a_e=\sqrt{12c_e}\). On each recovered simple cycle \(C\), find the unique \(t>0\) solving
\[
\boxed{\displaystyle
 t\sum_{e\in E(C)}\frac1{\sqrt{t^2+12c_e}-t}=1.}
\tag{2}
\]
Then \(a_e=\sqrt{t^2+12c_e}-t\) for every edge of that cycle. This determines every edge length, without requiring other moments or a sample of vertices.

## Assumptions and scope
A cactus is a finite connected simple undirected graph in which each edge belongs to at most one simple cycle; distinct cycles may meet at articulation vertices. Every weight is strictly positive, with no rationality, equality, or upper-bound restriction. The Euclidean coordinates are the labeled vertex-incidence coordinates, and the measure is **uniform intrinsic volume** on the full-dimensional body in \(\mathbf1^\perp\), not uniform over its discrete vertices or over independent generator coefficients. Covariance is normalized by volume. The formula holds for a tree (an empty cycle sum), for an individual cycle, and for any arrangement of bridges and vertex-glued cycles. It is not claimed for graphs whose distinct simple cycles share an edge. The inverse theorem is a statement about exact population covariance; it makes no finite-sample error or computational-complexity guarantee.

## Proof
**1. Direct-sum decomposition by cactus blocks.** Choose any orientation for bridges and a coherent cyclic orientation within each cycle. The incidence vectors of a connected graph span \(H=\mathbf1^\perp\). Their dependence space is the cycle space. For a cactus, the supports of its simple-cycle dependence vectors are disjoint, and those vectors form a basis of the entire dependence space. Thus the incidence spans of all bridge and full-cycle blocks form an internal direct sum of total dimension \(n-1\). Addition from the Cartesian product of their block zonotopes onto \(Z(G,a)\) is an invertible linear map between spaces of equal dimension, with constant positive Jacobian. Consequently uniform intrinsic-volume sampling on \(Z(G,a)\) is the sum of **independent** uniform block-volume samples. For a bridge the centered sample is \(a_e b_e U\), where \(U\) is uniform on \([-1/2,1/2]\), and therefore its covariance is \(a_e^2b_eb_e^{\mathsf T}/12\).

**2. Exact volume-disjoint tiling of an unequally weighted cycle.** Consider a single cycle of length \(r\ge3\), orient its incidence columns cyclically as \(b_1,\ldots,b_r\); then \(\sum_i b_i=0\) and this is the only linear dependence. The uncentered cycle zonotope is the image of \(\prod_i[0,a_i]\) under \(t\mapsto\sum_i t_i b_i\). All coefficient vectors of any one image point differ by a common scalar. Subtracting their minimum coordinate selects a unique representative in the union of the \(r\) boxes
\[
T_j=\left\{(t_1,\ldots,t_r):t_j=0,\ 0\le t_i\le a_i\ (i\ne j)\right\}.
\]
Distinct such representatives can meet only on lower-dimensional boundaries. Hence the cycle zonotope is tiled, up to null sets, by the images of these parallelotopes. Their Euclidean volumes are proportional to \(\prod_{i\ne j}a_i\), since omitting any one cycle incidence column gives the same absolute maximal determinant. Therefore the probability of the omitted index is
\[
 p_j=\frac{\prod_{i\ne j}a_i}{\sum_k\prod_{i\ne k}a_i}
 =\frac{a_j^{-1}}{H_C}.
\]
Conditional on this index, the other coefficients are independent uniform variables on their entire ranges.

**3. The weighted-cycle covariance.** After centering the zonotope by \(-\frac12\sum_i a_i b_i\), the conditional mean given omitted index \(j\) is \(-a_j b_j/2\), and its conditional covariance is \(\sum_{i\ne j}a_i^2b_ib_i^{\mathsf T}/12\). Since \(p_j a_j=H_C^{-1}\), the unconditional mean is \(-(2H_C)^{-1}\sum_jb_j=0\). The law of total covariance gives
\[
\begin{aligned}
\operatorname{Cov}(X_C)
&=\sum_i\frac{(1-p_i)a_i^2}{12}b_ib_i^{\mathsf T}
+\sum_i\frac{p_i a_i^2}{4}b_ib_i^{\mathsf T}\\
&=\sum_i\left(\frac{a_i^2}{12}+\frac{a_i}{6H_C}\right)b_ib_i^{\mathsf T}.
\end{aligned}
\]
Add independent block covariances from Step 1 to prove (1), including all cycle lengths and all positive real edge weights.

**4. Exact graph recovery.** Each coefficient in (1) is strictly positive. Because \(G\) is simple, for distinct \(u,v\), \(\Sigma_{uv}\) equals minus the unique coefficient of edge \(uv\) when it exists, or zero otherwise. The negative off-diagonal support of the population covariance therefore recovers the labeled edge set exactly, hence its cycle/bridge decomposition.

**5. Exact length recovery and uniqueness.** A bridge has \(c_e=a_e^2/12\). On any cycle abbreviate \(t=1/H_C\); (1) says \(12c_e=a_e^2+2ta_e\). The unique positive solution is
\[
 a_e(t)=\sqrt{t^2+12c_e}-t=\frac{12c_e}{\sqrt{t^2+12c_e}+t}.
\]
Each \(a_e(t)\) is continuous and **strictly decreasing** for \(t\ge0\). Thus \(F_C(t)=t\sum_e1/a_e(t)\) is continuous and strictly increasing on \((0,\infty)\). It tends to zero at the left endpoint and to infinity at the right endpoint (indeed \(a_e(t)\sim6c_e/t\)). Hence equation (2) has a unique positive solution. The actual weights supply a solution with \(t=1/H_C\), proving existence. The unique solution reconstructs all original weights. All reconstructions are cycle-local, so articulation arrangements create no ambiguity.

## Verification
The self-contained standard-library script `artifacts/verify.py` constructs the **actual weighted cycle zonotope** from its projected hypercube corners in dimensions two and three. It independently computes convex hulls and integrates the second moments through a polygonal triangulation or a facet-pyramid decomposition, rather than using the weighted omitted-index formula. Exact rational covariances match (1) for seven different unequal and equal weight profiles of three- and four-edge cycles. The script also verifies the exact algebraic inverse identities on those profiles. Its successful completion marker is `WEIGHTED_CACTUS_COVARIANCE_AND_INVERSE_PASS`. Finite tests do not prove an infinite-family theorem; Steps 1–5 do. Reproduce with `python3 artifacts/verify.py` from the artifact root.

## Relationship to prior work
Padrol, Pilaud and Poullot [1] establish the deformation-cone structure and graphical-zonotope realization, supplying the natural weighted geometry but not its uniform-volume covariance or inversion. A previously published calculation [2] gives the exact vertex-uniform and volume-uniform covariances of **unit-incidence cactus** zonotopes, which is recovered by putting all \(a_e=1\) in (1). A different published calculation [3] gives a full parameterwise uniform-volume covariance for a **single cycle with exactly one independent edge weight**, with the remaining cycle weights all equal; it does not treat independently weighted edges, multiple cycles, or covariance recovery of the weights. The covariance-precision recovery theorem for the **polar Lipschitz ball** [4] concerns a distinct convex body and unit-length edges; its Laplacian is the inverse of the covariance on \(\mathbf1^\perp\), whereas the graphical zonotope here has a Laplacian as the covariance itself. The present assertion is the arbitrary-positive-weight covariance formula together with its exact **lossless second-moment inverse**. Classical zonotope tilings and support-function uniqueness are background, not claimed as new; inversion from only the second-moment matrix is narrower data than knowing the entire body.

## Limitations
The covariance-to-edge recovery is for exact labeled population data, not noisy samples. The simplicity and cactus hypotheses are essential in the derivation; the proof does not establish uniqueness or support recovery for all connected weighted graphs with overlapping cycles, nor does it imply Gaussian graphical conditional independence. Convex-hull triangulation checks cover only low-dimensional cycles and are not an exhaustive infinite proof. No claim of historical priority beyond the materially inspected sources is made: an earlier general weighted-zonotope moment identity or inverse-tomography theorem may exist under box-spline terminology. The special unit-weight formula and one-edge weighted profile are already known; their credited claims are not asserted as novel. Independent audit has not been performed.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first public 2021-11-24), https://arxiv.org/abs/2111.12422 ; open full HTML https://arxiv.org/html/2111.12422v2 .
2. *A sharp vertex–volume covariance sandwich for cactus graphical zonotopes*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-vertex-volume-covariance-sandwich-for-cactus-graphical-z--b39706fc7ceb .
3. *Exact covariance and quantitative isotropic profile of one-edge-weighted cycle zonotopes*, published mathematical research record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-covariance-and-quantitative-isotropic-profile-of-one-edge--8efca44e3b81 .
4. *A sparse covariance precision and exact graph recovery for uniform Lipschitz potentials on cactus graphs*, published mathematical research record (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sparse-covariance-precision-and-exact-graph-recovery-for-unifo--6d8eaf369ca2 .
5. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353 (first public 2024-07-01), https://arxiv.org/abs/2407.01353 ; cited for existing affine-isotropy optimization of minimal-generator zonotopes, not as an assumption.
