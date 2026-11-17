# Complete Euclidean dihedral-angle spectrum and sharp acute–obtuse transition of cycle Laplacian simplices

## Finding
For every integer \(n\ge 3\), let \(L_n\) be the ordinary unweighted cycle graph Laplacian of \(C_n\), with cyclic indices, and form the canonical Euclidean Laplacian simplex
\[
T_n=\operatorname{conv}\{L_ne_0,\ldots,L_ne_{n-1}\}\subset\mathbf1^\perp\subset\mathbb R^n.
\]
For two distinct facets opposite vertices with cyclic separation \(d=\min(|i-j|,n-|i-j|)\), set \(u=d(n-d)\) and \(D_n=(n^2-1)(n^2+11)\). Their **interior** dihedral angle is exactly
\[
\boxed{\Theta_{n,d}=\pi-\arccos\left(1-\frac{30u(u+2)}{D_n}\right),\quad 1\le d\le\lfloor n/2\rfloor.}
\]
All \(\lfloor n/2\rfloor\) values are distinct and strictly decrease with \(d\). The multiplicity of \(\Theta_{n,d}\) among the \(\binom n2\) ridges is \(n\) when \(2d<n\), and \(n/2\) when \(2d=n\). Thus the formula gives the complete metric ridge-angle multiset, not merely the extremal angle.

For \(n=3,4\), **every** interior dihedral angle is acute. For **every** \(n\ge5\), the simplex has both acute and obtuse interior dihedral angles. More precisely, an angle is obtuse, right, or acute according as
\[
30u(u+2)\quad <,\ =,\ >\quad D_n,
\]
respectively. This is an exact finite classification with no unresolved integer rounding.

For a uniformly chosen ridge, let \(\Theta_n\) denote its interior dihedral angle. If \(U\) is uniform on \([0,1/2]\) with density \(2\), then
\[
\boxed{\Theta_n\ \xrightarrow{\mathrm d}\ \pi-\arccos\!\bigl(1-30U^2(1-U)^2\bigr).}
\]
The limiting angle distribution is continuous and nondegenerate, supported on \([\arccos(7/8),\pi]\). Writing
\[
\tau=\frac{1-\sqrt{1-4/\sqrt{30}}}{2},
\]
the limiting fraction of obtuse ridges is \(2\tau=1-\sqrt{1-4/\sqrt{30}}\approx0.4806703776\), and that of acute ridges is \(1-2\tau\). The mean cosine has the exact identity \(\mathbb E[\cos\Theta_n]=1/(n-1)\), and \(\mathbb E[\cos^2\Theta_n]\to3/7\).

## Assumptions and scope
Here \(C_3\) is the simple triangle and \(C_n\) for \(n\ge4\) is the simple cycle; all graph edges have unit weight. Euclidean inner products are those inherited from the standard orthonormal coordinates of \(\mathbb R^n\) restricted to the zero-sum hyperplane \(\mathbf1^\perp\). This metric **must not** be replaced by the generally nonorthogonal lattice coordinates used for Ehrhart calculations. Every ridge of the \((n-1)\)-simplex is incident to exactly two facets; the interior dihedral angle is \(\pi\) minus the angle between their inward normals. No probability distribution on the solid simplex is involved: the random ridge is uniform among the \(\binom n2\) unordered facet pairs.

## Proof
**Facets and normals.** Since \(L_n\) is symmetric, \(L_n\mathbf1=0\), and its kernel consists exactly of constants, the \(n\) vectors \(v_i=L_ne_i\) form the affinely independent vertices of an \((n-1)\)-simplex in \(\mathbf1^\perp\). Let \(H=L_n^+\) be the Moore–Penrose pseudoinverse. For every \(x\in\mathbf1^\perp\), its barycentric coordinate at \(v_i\) is \(1/n+\langle He_i,x\rangle\), because \(L_nH=I-\mathbf1\mathbf1^{\mathsf T}/n\). Therefore the inward normal of the facet opposite \(v_i\) is \(w_i=He_i\). In particular, the cosine between inward facet normals is
\[
\frac{\langle w_i,w_j\rangle}{\|w_i\|\|w_j\|}
=\frac{(H^2)_{ij}}{\sqrt{(H^2)_{ii}(H^2)_{jj}}}.
\]

**First and second cycle Green kernels.** For cyclic separation \(d\in\{0,\ldots,n-1\}\), put \(u_d=d(n-d)\). The cyclic sequence
\[
h_d=\frac{n^2-1}{12n}-\frac{u_d}{2n}
\]
has zero sum and satisfies \(2h_d-h_{d-1}-h_{d+1}=\mathbf1_{\{d=0\}}-1/n\), with indices interpreted modulo \(n\). Indeed \(2u_d-u_{d-1}-u_{d+1}=2\) away from \(d=0\), while direct substitution verifies \(d=0\); its zero sum follows from \(\sum_{d=0}^{n-1}u_d=n(n^2-1)/6\). Thus \(H_{ij}=h_{|i-j|\bmod n}\).

Let \(G=H^2\). Its cyclic entries \(g_d\) have zero sum and solve \(L_ng=h\). Write \(\delta_d=g_0-g_d\). A direct second-difference calculation yields
\[
\delta_d=\frac{u_d(u_d+2)}{24n}.
\]
For full verification, \(2u_d-u_{d-1}-u_{d+1}=2\), while \(2u_d^2-u_{d-1}^2-u_{d+1}^2=-2(n^2+1-6u_d)\) away from \(0\); these identities give \(L_n\delta=-h\), and the value at \(0\) follows from the cyclic boundary values. Since \(\sum_dg_d=0\), one has \(g_0=n^{-1}\sum_d\delta_d\). Using the elementary power sums
\[
\sum_{d=0}^{n-1}u_d=\frac{n(n^2-1)}6,\qquad
\sum_{d=0}^{n-1}u_d^2=\frac{n(n^4-1)}{30},
\]
we obtain
\[
g_0=\frac{(n^2-1)(n^2+11)}{720n},\qquad
\frac{g_d}{g_0}=1-\frac{30u_d(u_d+2)}{(n^2-1)(n^2+11)}.
\]
Cyclic symmetry makes all diagonal entries of \(H^2\) equal. Taking the supplementary angle between the inward normals proves the displayed formula for \(\Theta_{n,d}\).

**Multiplicity and transition.** For \(1\le d\le\lfloor n/2\rfloor\), \(u_d=d(n-d)\) strictly increases, so \(\Theta_{n,d}\) strictly decreases, giving exactly \(\lfloor n/2\rfloor\) distinct angles. There are \(n\) unordered index pairs at each separation \(d<n/2\), and \(n/2\) when \(d=n/2\). At \(d=1\), the normal cosine is \((n^2-19)/(n^2+11)\), which is negative for \(n=3,4\) and positive for \(n\ge5\). The smallest normal cosine, at \(d=\lfloor n/2\rfloor\), is always negative: since \(u_d\ge(n^2-1)/4\),
\[
\frac{30u_d(u_d+2)}{D_n}\ge\frac{15(n^2+7)}{8(n^2+11)}>1.
\]
This proves the sharp finite acute–obtuse transition and the sign test.

**Limit law and angular moments.** For a uniform unordered facet pair, its normalized cyclic distance \(d/n\) converges in distribution to \(U\), uniform on \([0,1/2]\) with density \(2\); this follows from the exact distance multiplicities. Uniformly along \(d/n\to t\), the normal cosine tends to \(1-30t^2(1-t)^2\). The continuous mapping theorem proves the limiting angle law. The equation \(30t^2(1-t)^2=1\) has the unique root \(\tau\) in \((0,1/2)\) given above, which proves the fraction of obtuse ridges; the equality boundary has limiting probability zero.

Finally \(\sum_iw_i=H\mathbf1=0\), all \(\|w_i\|\) are equal, and \(\cos\Theta_{ij}=-\langle w_i,w_j\rangle/(\|w_i\|\|w_j\|)\). Squaring \(\|\sum_iw_i\|=0\) gives \(\mathbb E\cos\Theta_n=1/(n-1)\). By bounded convergence, the limiting second moment is
\[
\int_0^1\bigl(1-30t^2(1-t)^2\bigr)^2\,dt
=1-60\cdot\frac1{30}+900\cdot\frac1{630}=\frac37.
\]
This completes all claims for every integer \(n\ge3\).

## Verification
Run `python verification/check_angles.py` with SymPy installed. It forms the cycle Laplacian independently for \(3\le n\le11\), computes the rational pseudoinverse by inverting \(L_n+\mathbf1\mathbf1^{\mathsf T}/n\), and compares all 219 facet-pair Gram entries to the formula. It also reconstructs each inward facet normal **directly from the vertices and hyperplane equations**, without using the pseudoinverse expression, and checks the finite acute–obtuse transition. Additional exact-integer enumeration of sign categories is performed for \(n=50,101,300,1000\). Successful completion prints `CYCLE_LAPLACIAN_DIHEDRAL_PASS`. The arbitrary-dimensional proof above is analytical; finite checks are corroboration only.

## Relationship to prior work
Braun and Meyer introduced graph Laplacian simplices and treated the cycle family through lattice reflexivity, triangulation, and Ehrhart theory (first public preprint 2017-06-21). Meyer and Pllaha continued with coding-theoretic invariants. Devriendt explains the general relation between a simplex's pseudoinverse Gram matrix and its dihedral angles, but the paper's graph-associated simplex is not, by definition, the convex hull of graph Laplacian columns. The general angle-normal principle is credited here. A separately published vertex-transitive Laplacian-simplex result provides the spectral inradius and the pseudoinverse normal formula, including cycle inspheres; it does not supply the off-diagonal squared-pseudoinverse kernel, exact distance-indexed ridge-angle spectrum, acute–obtuse threshold, or limiting angular law. These preceding statements are compatible with—and supply methods for—the present computation, but none of the inspected source statements supplies its complete outcome.

## Limitations
The metric statements concern only the canonical full-Laplacian Euclidean realization, not arbitrary unimodularly equivalent lattice representations. The result does not assert that the explicit cycle Green kernel is historically new: it is a classical computable inverse. The claimed contribution is the complete geometric angle spectrum, exact sign transition, and resulting limiting distribution in this particular family. No claim of exhaustive literature uniqueness or independent validation is made. A prior equivalent angle classification in spectral graph geometry remains a bibliographic risk; the currently inspected sources do not establish one.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085 (first public preprint 2017-06-21), *Advances in Applied Mathematics* 114 (2020), 101976, https://arxiv.org/abs/1706.07085 .
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960 (first public preprint 2018-09-09), https://arxiv.org/html/1809.02960v1 .
3. K. Devriendt, *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*, arXiv:2010.04521 (first public preprint 2020-10-09), Section II.2, https://arxiv.org/abs/2010.04521 .
4. *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, publicly available mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-vertex-transitive-laplacian-simplices-have-spectral-inradii-and--841b23980b76 .
5. K. Devriendt and P. Van Mieghem, *The Simplex Geometry of Graphs*, arXiv:1807.06475 (first public preprint 2018-07-17), https://arxiv.org/html/1807.06475v2 .
