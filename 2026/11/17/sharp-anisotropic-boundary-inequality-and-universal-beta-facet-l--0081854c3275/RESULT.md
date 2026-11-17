# Sharp anisotropic boundary inequality and universal beta facet law for even-cycle edge polytopes

## Finding
Let \(m\ge2\), let \(a,b>0\), and let \(U_0,\ldots,U_{m-1},V_0,\ldots,V_{m-1}\) be distinct coordinate labels, with subscripts modulo \(m\). Define the intrinsically Euclidean \((2m-2)\)-polytope
\[
P_m(a,b)=\operatorname{conv}\{a e_{U_i}+b e_{V_i},\;a e_{U_{i+1}}+b e_{V_i}:0\le i<m\}.
\]
Write \(d=2m-2\), \(E_t=m t(m-t)\) and \(O_t=m(t+1)(m-t-1)\) for \(0\le t<m\). For a facet obtained by omitting the first matching vertex with index \(i\) and the second matching vertex with index \(j\), put \(t=(j-i)\bmod m\). Its exact \((d-1)\)-dimensional Euclidean area is
\[
\boxed{\mathcal A_t(a,b)=\frac{(ab)^{m-1}}{(d-1)!}\sqrt{\frac{E_t}{a^2}+\frac{O_t}{b^2}}.}
\]
Every \(t\) occurs exactly \(m\) times, and the total volume and surface area are
\[
\boxed{\operatorname{Vol}_d(P_m(a,b))=\frac{m^2(ab)^{m-1}}{d!},\qquad
S_m(a,b)=\frac{m(ab)^{m-1}}{(d-1)!}\sum_{t=0}^{m-1}\sqrt{\frac{E_t}{a^2}+\frac{O_t}{b^2}}.}
\]
Set \(c=\sqrt{ab}\). The **sharp global surface penalty** under all positive two-color deformations is
\[
\boxed{S_m(a,b)\ge\frac{a+b}{2\sqrt{ab}}S_m(c,c).}
\]
Equality holds for all \(a,b\) when \(m=2\); for every \(m\ge3\), equality holds exactly when \(a=b\). Hence at fixed intrinsic volume the balanced realization uniquely minimizes surface area for every \(m\ge3\).

Define the surface-area-weighted discrete facet-offset measure
\[
\mu_{m,a,b}=\frac{\sum_{t=0}^{m-1}\mathcal A_t(a,b)\,\delta_{t/m}}{\sum_{t=0}^{m-1}\mathcal A_t(a,b)}.
\]
For **every** pair of positive sequences \(a_m,b_m\), without any bounded-aspect-ratio assumption,
\[
\boxed{\mu_{m,a_m,b_m}\Longrightarrow\operatorname{Beta}(3/2,3/2),\quad
\frac{S_m(a_m,b_m)}{S_m(\sqrt{a_mb_m},\sqrt{a_mb_m})}=\sqrt{\frac{a_m^2+b_m^2}{2a_mb_m}}\,(1+o(1)).}
\]
The limit density is \(\frac8\pi\sqrt{u(1-u)}\) on \([0,1]\), and both relative asymptotics are uniform over all positive aspect ratios. In particular, changing the color scales arbitrarily strongly does not change the limiting area-weighted facet-offset law.

## Assumptions and scope
The Euclidean metric is inherited from the standard coordinate inner product, and the polytope is measured in the affine space \(\sum_i x_{U_i}=a\), \(\sum_i x_{V_i}=b\). Both \(a\) and \(b\) are strictly positive; the result is not about assigning unequal weights to individual edges or about the centrally symmetric edge polytope. The \(2m\) vertices form the ordinary unsigned edge polytope of an even cycle after color-wise coordinate stretching. The offset measure uses the ordered matching pair described above. The full surface is the sum of intrinsic facet areas.

## Proof
**1. Free sum and metric volume.** Translate by the common barycenter \(c_0=(a\mathbf1_U/m,b\mathbf1_V/m)\). The two vertex matchings each give an \((m-1)\)-simplex containing the origin in its relative interior. Their direction spans are complementary within \(H=\{(x_U,x_V):\sum x_U=\sum x_V=0\}\), because the only coefficient relations on the connected even-cycle edge-incidence vectors, after centering, are the separate sums within each matching. Thus the translated polytope is their free sum. Each facet omits exactly one vertex from each matching; there are exactly \(m^2\) simplex facets. Coning all facets to \(c_0\) partitions the polytope into \(m^2\) simplices, each with exactly \(1/m^2\) of its volume (the coefficients in the two matching simplices have equal barycentric weights).

For completeness, the Euclidean wedge of the unscaled \(d\) difference vectors \(A_i-A_{m-1}\) and \(B_i-B_{m-1}\), \(0\le i<m-1\), equals \(m^2\). One way to check this without a volume convention is to orient all cycle edges from the \(V\)-class to the \(U\)-class. The oriented incidence map \(R\) has a one-dimensional alternating edge kernel. Its nonzero singular values have product \(2m\), since the nonzero cycle-Laplacian eigenvalues \(2-2\cos(2\pi k/(2m))\) multiply to \((2m)^2\). The edge-coordinate all-ones vector is orthogonal to the alternating kernel and has singular value \(2\). Its orthogonal complement inside the kernel complement is exactly the subspace of coefficient vectors whose sums on each perfect matching vanish; the product of singular values there is therefore \(m\). The two blocks of \(m-1\) standard differences \(e_i-e_{m-1}\) have joint wedge \(m\), as each Gram block is \(I+\mathbf1\mathbf1^{\mathsf T}\) of determinant \(m\). Their images under \(R\) consequently have wedge \(m^2\). Reversing signs on a vertex color preserves Euclidean lengths. Stretching the two color coordinate subspaces multiplies this wedge by \((ab)^{m-1}\). Each cone simplex has volume \((ab)^{m-1}/d!\), so the total volume is as stated.

**2. Exact supporting normals.** By cyclic symmetry omit \(A_0=a e_{U_0}+b e_{V_0}\) and \(B_t=a e_{U_{t+1}}+b e_{V_t}\). The uniquely normalized support functional \(\ell\) equals \(1\) on each retained centered vertex and \(1-m\) on the two omitted vertices. In the unscaled coordinate metric, its normal \((x,y)\in H\) satisfies
\[
x_i+y_i=1-m\mathbf1_{i=0},\qquad x_{i+1}+y_i=1-m\mathbf1_{i=t}.
\]
Subtracting yields \(x_{i+1}-x_i=m(\mathbf1_{i=0}-\mathbf1_{i=t})\). The two zero-sum coordinate blocks are therefore
\[
x_i=\begin{cases}m-t&1\le i\le t,\\-t&\text{otherwise},\end{cases}\qquad
y_i=\begin{cases}-(m-t-1)&0\le i\le t,\\t+1&\text{otherwise}.\end{cases}
\]
Their squared norms are exactly \(\|x\|^2=E_t\) and \(\|y\|^2=O_t\). Under the color-wise stretching, the support normal becomes \((x/a,y/b)\), with norm \(\sqrt{E_t/a^2+O_t/b^2}\). The distance from \(c_0\) to the supporting plane is the reciprocal of that norm. Every cone simplex has volume \((ab)^{m-1}/d!\); the elementary pyramid volume identity \(\operatorname{Vol}_d=(\mathcal A_t/d)\times\operatorname{height}\) gives the displayed facet areas and total surface area.

**3. Sharp penalty.** Put \(a=c e^z\) and \(b=c e^{-z}\), so \(c^2=ab\). After factoring out the common positive scale \(c^{2m-3}\), the summand of the surface area is \(f_t(z)=\sqrt{E_t e^{-2z}+O_t e^{2z}}\). The exact identity \(E_{m-1-t}=O_t\) implies \(f_{m-1-t}(z)=f_t(-z)\). By the triangle inequality in \(\mathbb R^2\),
\[
f_t(z)+f_t(-z)\ge 2\cosh(z)\sqrt{E_t+O_t}.
\]
Summing and pairing gives \(S_m(a,b)\ge\cosh(z) S_m(c,c)\), which is the claimed factor. For \(m=2\), every offset has one of \(E_t,O_t\) equal to zero, and equality holds. For \(m\ge3\), a summand with \(E_t O_t>0\) makes the triangle inequality strict whenever \(z\ne0\). The volume depends only on \(ab\), proving the unique fixed-volume minimizer.

**4. Arbitrarily anisotropic beta limit.** Put \(\lambda=(1/a^2)/(1/a^2+1/b^2)\in(0,1)\), and \(u=t/m\). Exactly
\[
\frac{E_t}{m^3}=u(1-u),\qquad \frac{O_t}{m^3}=(u+1/m)(1-u-1/m).
\]
The second expression differs from \(u(1-u)\) by at most \(1/m\), uniformly in \(t\). Consequently
\[
\sup_{t,\lambda}\left|\sqrt{\lambda E_t/m^3+(1-\lambda)O_t/m^3}-\sqrt{u(1-u)}\right|\le m^{-1/2}.
\]
The Riemann-sum limit is therefore uniform even when \(a/b\) diverges or vanishes:
\[
\sum_t\sqrt{E_t/a^2+O_t/b^2}=m^{5/2}\sqrt{a^{-2}+b^{-2}}\left(\frac\pi8+o(1)\right).
\]
The same uniform approximation holds with any continuous test function of \(t/m\); normalizing proves the stated beta weak limit. Dividing the resulting surface-area asymptotic by its value at \(a=b=c\) proves the exact displayed uniform relative penalty \(\sqrt{(a^2+b^2)/(2ab)}(1+o(1))\).

## Verification
`verify.py` performs exact rational Gram-determinant checks directly from the stated vertex matrices in every dimension parameter \(2\le m\le6\), for three rational color-scale pairs, validating all \(270\) facets and the full-volume determinant against the theorem. Running `python3 verify.py` prints `CYCLE_ANISOTROPIC_PASS cases=270 m=2..6 distinct_scales=3`. This finite verification is supplemental; Steps 1–4 prove all claims for every permitted \(m,a,b\). The limiting assertions are ordinary weak convergence, not pointwise convergence of atomic measures to a density.

## Relationship to prior work
Kálmán and Tóthmérész [1] establish general root-polytope dimensions, dissection theory, and their connection to semi-balanced directed graphs. Kálmán and Postnikov [2] establish triangulation and lattice-enumeration methods for bipartite root polytopes. The closest pre-existing exact Euclidean result [3] gives the **unscaled** support-plane norm of every facet of the bipartite-cycle root polytope, namely \(E_t+O_t\); the present unscaled norm is explicitly credited as prior information. That result does not give two-color stretched area contributions, a fixed-volume sharp surface inequality, or a beta law **uniform even across unbounded aspect ratios**. The latter new claims require the individual color-block norm split, a global paired triangle inequality, and a uniform-in-ratio Riemann-sum argument. The unsigned-edge version is orthogonally equivalent to the color-oriented root version at equal scales. Ehrhart or facet-count data alone do not imply Euclidean surface area. The relation between this theorem and published distance data is thus explicit rather than inferred merely from differing terminology.

## Limitations
This is a two-color coordinate-stretching family, not arbitrary weights on all graph vertices or graph edges. The geometry uses the inherited coordinate Euclidean metric; arbitrary affine transformations do not preserve the area or limiting law. The sharp global inequality is optimal uniformly over the indicated dimensions because the \(m=2\) equality cases attain it; for a fixed \(m\ge3\) and unequal scales the inequality is strict. Although named primary texts and published exact-distance claims were checked, equivalent work outside indexed sources cannot be excluded. No independent mathematical audit has been performed.

## References
[1] T. Kálmán and L. Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, first public 2021-05-03, arXiv:2105.00960, https://arxiv.org/html/2105.00960v3. Primary MSC 52B20.

[2] T. Kálmán and A. Postnikov, *Root polytopes, Tutte polynomials, and a duality theorem for bipartite graphs*, 2016-02-14, arXiv:1602.04449, https://arxiv.org/html/1602.04449v1.

[3] *Euclidean support-plane shells and an incenter parity law for bipartite-cycle root polytopes*, published mathematical finding, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-euclidean-support-plane-shells-and-an-incenter-parity-law-for-bi--2c6fea9ced07/RESULT.md (explicit complete support-normal formula, inspected).
