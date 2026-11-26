# The two-obstruction cone for mixed circular Poisson covariance modulation

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), \(0<r<1\), and
\[
P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2}.
\]
For arbitrary real \(a,b,c\), consider the continuous symmetric kernel
\[
K_{a,b,c}(x,y)=P_r(x-y)\bigl(a+b\cos(x+y)+c\cos(x-y)\bigr).
\]
Write
\[
\mu=\frac{r+r^{-1}}2,\qquad
\delta=\frac{r^{-1}-r}2,\qquad
h=a+\mu c.
\]
**Theorem.** The Gram matrix of \(K_{a,b,c}\) is positive semidefinite for every finite configuration of points of \(\mathbb T\) if and only if
\[
\boxed{h\ge\mu|b|\quad\text{and}\quad
h\ge\sqrt{b^2+\delta^2\max(c,0)^2}.}
\]
Moreover, within this closed cone, the kernel is **strictly** positive definite on every finite set of distinct points if and only if
\[
\boxed{h>\mu|b|.}
\]
In particular, an entire nonempty part of the boundary of the positive-semidefinite cone is strictly positive definite on finite sets. For \(c>0\) and \(-rc\le a<0\), the sharp allowed amplitude is
\[
|b|\le\sqrt{(a+rc)(a+c/r)},
\]
whereas for \(a\ge0,c\ge0\), or \(c\le0,a\ge-\mu c\), it is
\[
|b|\le c+a/\mu.
\]
These branches meet at \(a=0,c>0\), but have different one-sided slopes as a function of \(a\). The negative-baseline branch is not detected by the simpler one-frequency nonstationary Poisson cutoff.

For a concrete distinction, take \(r=1/2\), \(a=-1/4\), and \(c=1\). Then the exact admissible interval is \(|b|\le\sqrt7/4\), while testing all antipodal pairs only gives \(|b|\le11/16\). The antisymmetric test on those pairs by itself gives \(|b|\le4/5\). At the sharp value \(|b|=\sqrt7/4\), all finite Gram matrices at distinct sites remain positive definite. For \(b=67/100\), which passes all antipodal-pair tests, the eight equispaced sites \(x_j=j\pi/4\) with coefficients \((0,-1,-7,-1,0,-1,-7,-1)\) give the **exact negative** quadratic form
\[
\sum_{i,j=0}^7z_i z_j K_{-1/4,67/100,1}(x_i,x_j)
=-\frac{1217}{1275}<0,
\]
even though all eight diagonal variances are positive.

## Assumptions and scope
The circle carries angles modulo \(2\pi\). Positive semidefinite means nonnegative complex Hermitian Gram forms on every finite node set; strict positive definiteness means strictly positive quadratic forms on each nonzero coefficient vector at pairwise distinct nodes. No normalization \(K(x,x)=1\) is presumed; the parameters \(a,b,c\) can have either sign. All statements hold for each individual fixed \(r\in(0,1)\), including sharp equality cases. The kernel is nonstationary when \(b\ne0\).

## Proof
**Fourier matrix reduction.** The absolutely convergent Poisson expansion is
\[
P_r(t)=\sum_{n\in\mathbb Z}r^{|n|}e^{int}.
\]
For a finite complex measure \(\nu=\sum_j z_j\delta_{x_j}\), define \(F_n=\sum_jz_j e^{-inx_j}\), \(v_n=r^{|n|/2}F_n\). Its energy equals the bounded infinite Hermitian form
\[
\begin{split}
Q(\nu)&=\sum_{n\in\mathbb Z}d_n|v_n|^2+
 b\operatorname{Re}\sum_{n\in\mathbb Z}w_n\overline{v_{n+1}}v_{n-1},\\
d_0&=a+cr,\qquad d_n=h\quad(n\ne0),\\
w_0&=r^{-1},\qquad w_n=1\quad(n\ne0).
\end{split}
\]
This follows by multiplying the Fourier series by \(\cos(x-y)\) and \(\cos(x+y)\); absolute summability justifies all interchanges. Conversely, positivity for all finite atomic measures implies positivity of this bounded form on every finitely supported sequence: approximate any trigonometric-polynomial density by atomic Riemann sums and use dominated convergence in weighted \(\ell^2\). The weight \(r^{|n|/2}\) is nonzero on every index. Thus the all-configuration condition is **equivalent** to positivity of the infinite Fourier operator, not merely implied by it.

**Odd Fourier sector.** The indices \(n=2k+1\) carry constant diagonal \(h\), ordinary off-diagonal couplings \(b/2\), and one exceptional edge between \(-1\) and \(1\) with coupling \(b/(2r)\). On the path indexed by \(k\), let \(T\) be the weighted adjacency with ordinary edge weight \(1\) and exceptional edge weight \(J=1/r\) from \(k=-1\) to \(k=0\). The positive sequence \(\phi_k=J^{-\min(|k|,|k+1|)}\) lies in \(\ell^2\) and satisfies \(T\phi=(J+J^{-1})\phi\). For any finitely supported \(u\), with \(w_{ij}\) denoting the weight of the undirected edge \(\{i,j\}\), one has
\[
(J+J^{-1})\|u\|^2-\langle u,Tu\rangle
=\sum_{\{i,j\}}w_{ij}\phi_i\phi_j\left|u_i/\phi_i-u_j/\phi_j\right|^2\ge0.
\]
This follows by expanding and using the eigenvector equation. Alternating signs conjugate \(T\) to \(-T\), so both endpoints of the resulting two-sided spectral bound are attained. Thus the bottom of \(hI+(b/2)T\) is \(h-\mu|b|\), including \(b=0\).

**Even Fourier sector.** Under \(n=2k\), the off-diagonal coupling is uniformly \(b/2\), while the central diagonal is \(h-c\delta\) and all others are \(h\). This is the full-line Jacobi operator
\[
H_{\rm even}=hI+\frac b2(S+S^*)-c\delta\,|e_0\rangle\langle e_0|.
\]
For \(b\ne0\), the unperturbed essential spectrum is \([h-|b|,h+|b|]\). A nonzero one-site defect \(\Delta=-c\delta\) adds one simple outlying eigenvalue \(h+\operatorname{sgn}(\Delta)\sqrt{b^2+\Delta^2}\). To see this directly, insert \(u_k=t^{|k|}\), \(|t|<1\), into the recurrence away from and at \(k=0\):
\[
\lambda-h=\frac b2(t+t^{-1}),\qquad
\lambda-h=\Delta+bt.
\]
The decaying solution exists uniquely when \(\Delta\ne0\); the spectral interval and this single outlier exhaust the spectrum by the elementary resolvent equation for a rank-one perturbation. At \(b=0\), the operator is diagonal, with the same lower-bound formula by inspection. Hence its lower bound is \(h-|b|\) if \(c\le0\), and \(h-\sqrt{b^2+c^2\delta^2}\) if \(c>0\). Combining the two sector bounds, and using \(\mu>1\), proves the boxed positivity cone.

**Strictness and boundary.** If \(h=\mu|b|\) and \(b\ne0\), an alternating signed measure on an antipodal pair has zero energy. For \(b<0\) use \(\delta_0-\delta_\pi\); for \(b>0\) use \(\delta_{\pi/2}-\delta_{3\pi/2}\). This is checked either from the odd-sector bound-state eigenvector or directly from the two Poisson values at angle \(0\) and \(\pi\). If \(h=|b|=0\) in the positive cone, then \(c\le0\), \(a=-\mu c\), and \(K=-c\delta\) is a constant kernel (the zero kernel if \(c=0\)); hence not strictly positive definite.

Now suppose \(h>\mu|b|\). The odd sector is strictly positive, so a hypothetical zero-energy finite complex atomic measure must have every odd Fourier coefficient zero. The even sector is also strictly positive except possibly at its one-site-defect boundary; such equality necessarily has \(c>0\) and \(-rc\le a<0\). For \(b=0\), its nullspace is the span of \(e_0\), which cannot be the weighted Fourier sequence of a nonzero finite atomic measure. For \(b\ne0\), its one-dimensional nullspace has components \(u_k=t^{|k|}\) with
\[
|t|=\frac{a+rc}{|b|},\qquad
|t|^2=\frac{a+rc}{a+c/r}<r^2
\quad\text{when }-rc<a<0.
\]
Consequently the even Fourier coefficients \(F_{2k}\) of such an atomic measure would tend to zero as \(k\to+\infty\), while \(F_0\ne0\). This is impossible: any finite exponential sum \(F_{2k}=\sum_jz_je^{-2ikx_j}\) that converges to zero has zero coefficients after aggregating equal frequencies, by Cesàro averaging against each conjugate frequency, and therefore also \(F_0=0\). Thus no nonzero finite atomic measure has zero energy. This proves the strictness criterion, including the even-sector boundary.

**Antipodal tests and amplitude formulas.** Let \(u=b\cos(2x)\) for the pair \(x,x+\pi\), and write \(p=P_r(0)\), \(q=P_r(\pi)\). Its diagonal entries are \(p(a+c+u)\) and the off-diagonal is \(q(a-c-u)\). Since \((p+q)/(p-q)=\mu\), the symmetric and antisymmetric eigenvalues are \((p+q)(a+(c+u)/\mu)\) and \((p-q)(a+\mu(c+u))\), respectively. Requiring both to be nonnegative for every \(x\) is equivalent to
\[
|b|\le\min\{c+\mu a,c+a/\mu\}.
\]
For the stated example this minimum is \(\min\{11/16,4/5\}=11/16\), and \(\sqrt7/4<67/100<11/16\).

The piecewise amplitude formulas for the full cone follow from \(\mu^2-\delta^2=1\) and
\[
h^2-c^2\delta^2=(a+rc)(a+c/r).
\]
For \(c>0\), feasibility requires \(a\ge-rc\); the even bound is tighter when \(-rc\le a<0\), and the odd bound is tighter when \(a>0\). For \(c\le0\), the odd bound is the sole restriction. The displayed eight-node witness is exact arithmetic in \(\mathbb Q(\sqrt2)\), with all irrational contributions canceling.

## Verification
The accompanying standalone Python standard-library file `CHECKER.py` verifies 289 exact assertions: Fourier-neighbor and cross-coupling identities across multiple radii and indices, the even-sector boundary factorization, the eight-site rational negative witness, boundary zero rows at \(a=0,b=c\), and a constant-kernel endpoint. Run `python3 CHECKER.py`; the output is `PASS: 289 exact rational/quadratic-field assertions`. The infinite-dimensional equivalence, the Jacobi spectra, the all-radius sharpness and the strictness statement are mathematical proofs above, not consequences of finite numerical tests.

## Relationship to prior work
Buhmann and Jäger (2021/2022, arXiv:2105.02586) develop spherical harmonic criteria for nonisotropic and convolutional kernels and discuss the circle Fourier-matrix framework in their Section 5; that framework does not provide this explicit mixed-modulation cone or its two competing spectral defects. Guella and Jäger (2022, arXiv:2205.07396, Sections 2–3) characterize strict positivity for a distinct class of diagonal-eigenfunction expansions, rather than the off-diagonal Jacobi matrix here. Jäger (2020, arXiv:2005.02798) treats general two-sphere coefficient blocks, not this exact circle Poisson cone. The earlier harmonic-modulation result [4] gives the sharp threshold and polygonal singularities of \(P_r(x-y)(1+\varepsilon\cos(k(x+y)))\); it covers the \(c=0, a>0\) slice by taking \(k=1\) and scaling. The same-day stationary finite-knot classification [5] covers the \(b=0\) slice: for \(Q(t)=a+c\cos t\) its knots are \(a+rc\) and \(rh\), and strictness within the stationary positive cone is equivalent to \(rh>0\). No precedence within that day is asserted. The addition here is the full mixed cone, including the competition between the spectral defects and the nonstationary, finite-site strict part of the even-sector boundary.

## Limitations
The classification concerns first-harmonic separation and sum-angle modulations on a single circle, with real scalar coefficients and \(0<r<1\). It does not classify arbitrary nonstationary or multi-frequency kernels. The sharp even-sector boundary need not have a finite singular Gram matrix, although arbitrarily close exterior parameters have negative finite witnesses by approximation. Novelty is assessed against the listed inspected sources and searchable records, not independently certified; a differently parameterized covariance construction or an unindexed equivalent Jacobi computation is a residual priority risk. Independent validation of the new theorem has not been performed.

## References
1. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, arXiv:2105.02586 (first public 2021-05-06), https://arxiv.org/abs/2105.02586; open journal full text https://link.springer.com/article/10.1007/s00041-022-09913-x.
2. J. C. Guella and J. Jäger, *Strictly positive definite non-isotropic kernels on two-point homogeneous manifolds: the asymptotic approach*, arXiv:2205.07396 (first public 2022-05-15), https://arxiv.org/abs/2205.07396; open journal full text https://link.springer.com/article/10.1007/s11117-023-01022-3.
3. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798 (first public 2020-05-06), https://arxiv.org/abs/2005.02798.
4. *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances*, public result (2026), https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-harmonic-modulation-cutoff-and-polygonal-singularities-for--0f4219b7a6a9.
5. *Finite-knot positivity cones for signed periodic Poisson covariances*, public result (2026), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-finite-knot-positivity-cones-for-signed-periodic-poisson-covaria--2dc7842600c0.
