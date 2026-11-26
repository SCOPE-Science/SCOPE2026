# Partition-blind Steiner curvature of orthogonal free sums of cubes

## Finding
Let \(m\ge1\) and let \(r_1,\ldots,r_m\) be positive integers with \(d=\sum_{i=1}^m r_i\ge2\). Equip the mutually orthogonal coordinate blocks with the ordinary Euclidean metric and put
\[
P_{\mathbf r}=\{(x^{(1)},\ldots,x^{(m)}):\sum_{i=1}^m\|x^{(i)}\|_\infty\le1\}.
\]
This is the free sum of the coordinate cubes \([-1,1]^{r_i}\), a coordinate Hanner polytope. Write \(s=|\{i:r_i=1\}|\), and define the first two Steiner coefficients by
\[
\operatorname{vol}_d(P_{\mathbf r}+tB_d)=V+St+C_2t^2+O_{\mathbf r}(t^3)\quad(t\downarrow0),
\]
where \(B_d\) is the Euclidean unit ball. The exact answers are
\[
V=\frac{2^d\prod_{i=1}^m r_i!}{d!},\qquad \frac SV=d\sqrt m,
\]
\[
\boxed{\frac{C_2}{V}=\frac{d(d-1)}4\left[(m-s)\sqrt{2m-1}\arccos\frac{m-1}{m}+s\sqrt{m-1}\arccos\frac{m-2}{m}\right].}
\]
For \(m=1\), the summand multiplied by \(s\) is absent. In the usual intrinsic-volume convention, \(C_2=\pi V_{d-2}(P_{\mathbf r})\).

Thus at fixed \(d,m\) both ratios are independent of all individual nonsingleton block dimensions. In particular, for \(d=10,m=3,s=0\), the dimension partitions \((2,2,6)\) and \((2,4,4)\) have the same two ratios despite having respectively \(192\) and \(256\) facets.

For fixed \(d>m\ge2\), the normalized second coefficient is strictly decreasing in the number of singleton blocks. It is minimized only, up to block permutation, by \((d-m+1,1,\ldots,1)\). It is maximized exactly when the number of singleton blocks is minimal: if \(d<2m\), the maximizing partition has \(2m-d\) singleton blocks and \(d-m\) blocks of size two; if \(d\ge2m\), every partition with all block dimensions at least two maximizes it. At \(d=m\) there is only the all-singleton partition.

## Assumptions and scope
All cubes have coordinate side length \(2\); the Euclidean metric is the ambient coordinate metric, rather than a metric subsequently optimized over affine maps. All \(r_i\) are positive integers. Facets, ridges, angles, areas, and volumes are intrinsic to \(P_{\mathbf r}\), which is full-dimensional in \(\mathbb R^d\). A ridge has intrinsic \((d-2)\)-dimensional volume; for \(d=2\) each vertex has zero-dimensional volume one. Outer dihedral angles are measured in radians. The Taylor coefficient \(C_2\) includes the factor \(1/2\) in the polyhedral exterior-angle sum.

## Proof
**Volume and facets.** The gauge of \(P_{\mathbf r}\) is \(\sum_i\|x^{(i)}\|_\infty\), and its polar is the Cartesian product \(Q=\prod_i B_1^{r_i}\). A facet of \(P_{\mathbf r}\) is therefore indexed by choosing a signed coordinate axis in every block. Its supporting equation is
\[
\sum_i\sigma_i x^{(i)}_{a_i}=1,\qquad a_i\in[r_i],\ \sigma_i\in\{-1,1\}.
\]
There are exactly \(F=\prod_i(2r_i)\) facets, and every facet plane is at distance \(1/\sqrt m\) from the origin. The pyramid decomposition into the facet pyramids therefore yields \(V=S/(d\sqrt m)\).

For an independent volume computation, the cube \(\{x^{(i)}:\|x^{(i)}\|_\infty\le u\}\) has volume \(2^{r_i}u^{r_i}\), hence radial-shell volume \(2^{r_i}r_i u^{r_i-1}\,du\). Integrating these densities over \(u_i\ge0\) with \(\sum_i u_i\le1\) by the multivariate beta integral gives
\[
V=2^d\prod_i r_i\,\frac{\prod_i\Gamma(r_i)}{\Gamma(d+1)}=\frac{2^d\prod_i r_i!}{d!}.
\]
The common facet area, also obtained by a simplex-of-block-radii parametrization, is
\[
A_F=\frac{\sqrt m\,2^{d-m}\prod_i(r_i-1)!}{(d-1)!}.
\]
Indeed, the free radii form a standard \((m-1)\)-simplex with intrinsic Jacobian \(\sqrt m\), and the transverse \((r_i-1)\)-cube coordinates range between plus and minus the respective radius. It follows again that \(FA_F=S=d\sqrt m\,V\).

**All ridges.** Polarity identifies each ridge of \(P_{\mathbf r}\) with precisely one edge of \(Q\). Since \(Q\) is a product, an edge changes the selected signed axis in one and only one block. In a nonsingleton block \(r_i\ge2\), the cross-polytope has \(2r_i(r_i-1)\) edges, joining nonopposite axes. For such a ridge there are \(F(r_i-1)\) occurrences as block \(i\) varies, the outward unit normals have inner product \((m-1)/m\), and the exterior angle is
\[
\alpha_2=\arccos\frac{m-1}{m}.
\]
Its intrinsic ridge area is
\[
A_i^{(2)}=\frac{\sqrt{2m-1}\,2^{d-m-1}(r_i-2)!\prod_{j\ne i}(r_j-1)!}{(d-2)!}.
\]
The area formula follows from parametrizing the ridge by the \(m\) block radii: the distinguished block is constrained to the intersection of two coordinate cube facets, while the other blocks are constrained to one cube facet each. The radius simplex has intrinsic Jacobian \(\sqrt{2m-1}\); its Dirichlet integral has exponents \(r_i-2\) in the distinguished block and \(r_j-1\) in the others.

A singleton block has a cross-polytope consisting of a segment, whose unique edge changes the sign of that coordinate. There are \(F/2\) such ridges for each singleton block. Their normal inner product is \((m-2)/m\), so their exterior angle is
\[
\alpha_1=\arccos\frac{m-2}{m}.
\]
Their common ridge area for a singleton block \(i\) is
\[
A_i^{(1)}=\frac{\sqrt{m-1}\,2^{d-m}\prod_{j\ne i}(r_j-1)!}{(d-2)!}.
\]
This time the changing coordinate is zero, so the radius-simplex parametrization has \(m-1\) block radii and Jacobian \(\sqrt{m-1}\). These two edge types exhaust all edges of the product of cross-polytopes, so they exhaust the ridges without omissions.

**Steiner coefficient.** The polyhedral tube formula gives
\[
C_2=\frac12\sum_{R\text{ ridge}}\mathcal H^{d-2}(R)\alpha_R.
\]
For each nonsingleton block, substitution of the count and area above gives total area
\[
F(r_i-1)A_i^{(2)}=\frac{d(d-1)V}{2}\sqrt{2m-1}.
\]
For each singleton block, similarly
\[
\frac F2 A_i^{(1)}=\frac{d(d-1)V}{2}\sqrt{m-1}.
\]
There are exactly \(m-s\) nonsingleton and \(s\) singleton blocks. Multiplying the corresponding total ridge areas by their outer angles and by \(1/2\) proves the displayed formula for \(C_2/V\). In dimension two this uses the standard exterior-angle formula for polygonal parallel bodies and agrees with \(C_2=\pi\).

**Extremal block partitions.** Set \(g(u)=\sqrt{u-1}\arcsin(u^{-1/2})\) for \(u>1\). The nonsingleton and singleton contributions in the square bracket are respectively \(2g(2m)\) and \(2g(m)\). Write \(v=u^{-1/2}\). Direct differentiation gives
\[
2g'(u)=\frac{\arcsin v}{\sqrt{u-1}}-\frac1u>0,
\]
since \(\arcsin v>v\sqrt{1-v^2}\) for \(0<v<1\). Thus the nonsingleton contribution strictly exceeds the singleton contribution for every \(m\ge2\), and the normalized coefficient decreases strictly as \(s\) increases. For \(d>m\), the possible singleton counts run from \(\max(0,2m-d)\) to \(m-1\). Maximizing and minimizing this count yield exactly the stated partitions and equality classes.

## Verification
The standalone `verify.py` reconstructs every coordinate-cube vertex and every polar-product facet normal in thirteen small parameter cases, computes the convex hull's ambient volume and surface area, intersects each facet pair, selects precisely rank-\((d-2)\) intersections, and computes their Euclidean intrinsic volumes and exterior angles from actual vertex coordinates. It checks their types, areas, totals, and the closed Steiner coefficient. It terminates with `HANNER_STEINER_CHECK_PASS`. The mathematical proof above is valid for all positive integer block sizes; finite enumeration is an independent diagnostic, not an infinite certificate.

## Relationship to prior work
Hanner polytopes, their Cartesian products and free sums, and their minimal combinatorial face counts are established; see Sanyal–Winter (2023). The formulas here concern Euclidean tube coefficients, ridge area, and their cancellation of all nonsingleton block-size data, not face-minimality, isotropic constants, or affine Mahler products. The standard polyhedral Steiner angle sum is used without a novelty claim. No earlier equivalent complete formula was identified in the literature and indexed research records inspected, but exhaustive historical priority is not asserted.

## Limitations
The formulas apply to this coordinate realization and its orthogonal congruent copies, not to arbitrary affine realizations of Hanner polytopes or general iterative mixtures of products and free sums. In particular, this theorem does not classify all Hanner bodies by Steiner data. Historical priority beyond the accessed sources remains provisional. No independent mathematical audit has been performed.

## References
1. Raman Sanyal and Martin Winter, *Kalai's \(3^d\) conjecture for unconditional and locally anti-blocking polytopes*, arXiv:2308.02909, first publicly posted 2023-08-05. https://arxiv.org/abs/2308.02909
2. E. W. Weisstein, *Hanner Polytope*, MathWorld, https://mathworld.wolfram.com/HannerPolytope.html (general construction and duality).
3. Classical Steiner parallel-body formula and the Euclidean polyhedral exterior-angle formula (standard background identity, not claimed as new).
