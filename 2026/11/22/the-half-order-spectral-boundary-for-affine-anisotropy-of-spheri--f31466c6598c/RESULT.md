# The half-order spectral boundary for affine anisotropy of spherical fractional heat kernels

## Finding

Let \(d\ge 2\) be an integer and let \(\mathbb S^{d-1}\subset\mathbb R^d\) have normalized rotation-invariant measure. Denote by \(\mathcal H_\ell\) the degree-\(\ell\) spherical harmonics, and by \(\Pi_\ell(x,y)\) their orthogonal-projector kernels. For \(t>0\) and \(0<\alpha\le1\), put
\[
H_{t,\alpha}(x,y)=\sum_{\ell=0}^\infty
 e^{-t[\ell(\ell+d-2)]^\alpha}\Pi_\ell(x,y),
\qquad
K_{a,v}(x,y)=\bigl(a+\langle v,x+y\rangle\bigr)H_{t,\alpha}(x,y),
\]
where \(a\in\mathbb R\) and \(v\in\mathbb R^d\). The series is uniformly absolutely convergent. Positive semidefiniteness means nonnegativity of every finite evaluation Gram matrix.

**Sharp spectral-order transition.** If \(1/2<\alpha\le1\), then \(K_{a,v}\) is positive semidefinite if and only if \(v=0\) and \(a\ge0\). If \(0<\alpha\le1/2\), then there exists a finite, strictly positive constant \(\rho_{d,t,\alpha}\), depending only on the indicated parameters, such that
\[
K_{a,v}\succeq0\quad\Longleftrightarrow\quad
 a\ge \rho_{d,t,\alpha}\|v\|,
\qquad
2\le\rho_{d,t,\alpha}\le4\cosh\!\left(\frac{t(d-1)^\alpha}{2}\right).
\]
The exact (possibly non-elementary) threshold is the operator norm specified below, not merely an existence constant. In particular, \(\alpha=1/2\) belongs to the nontrivial-admissibility side, while the ordinary spherical heat kernel \(\alpha=1\) admits no nonzero affine perturbation of this form, however small.

**General adjacent-ratio criterion.** More generally, let \((c_\ell)_{\ell\ge0}\) be any strictly positive real sequence with \(\sum_\ell c_\ell\dim\mathcal H_\ell<\infty\), and replace \(H_{t,\alpha}\) by \(H_c=\sum c_\ell\Pi_\ell\). A nonzero \(v\) admits some finite \(a\) making \((a+\langle v,x+y\rangle)H_c\) positive semidefinite if and only if
\[
\sup_{\ell\ge0}\max\left\{\frac{c_\ell}{c_{\ell+1}},\frac{c_{\ell+1}}{c_\ell}\right\}<\infty.
\]
When this holds, the sharp coefficient threshold is \(a\ge\|v\|\|J_c\|\), where \(J_c\) is the following selfadjoint degree-neighbor operator on \(L^2(\mathbb S^{d-1})\): its only nonzero harmonic blocks are
\[
\Pi_{\ell+1}J_c\Pi_\ell
=\frac{c_\ell+c_{\ell+1}}{\sqrt{c_\ell c_{\ell+1}}}
\,\Pi_{\ell+1}M_z\Pi_\ell,
\qquad M_z f(x)=x_d f(x),
\]
and their adjoints. If the ratios are unbounded, set \(\|J_c\|=+\infty\); in this case no nonzero affine coefficient is admissible. This is an equality characterization, including the boundary when the operator norm is finite.

## Assumptions and scope

The sphere is the unit sphere with its usual Laplace–Beltrami eigenvalues \(\ell(\ell+d-2)\); the coefficient \(\alpha\) is the *spectral power of the Laplacian*, not a power of geodesic distance. All quantities are real except auxiliary harmonic test functions. There is no restriction on the sign of \(a\) or coordinates of \(v\). The center \(v=0,a=0\) gives the zero kernel. For positive \(a\) and \(v=0\), strictly positive harmonic coefficients make the isotropic kernel strictly positive definite on distinct finite sites. No claim is made that every nonzero admissible affine kernel at its boundary is strictly positive definite.

## Proof

**1. Reduction to the harmonic quadratic form.** Let \(C\) be the positive integral operator with eigenvalue \(c_\ell\) on \(\mathcal H_\ell\), and take \(v=\|v\|e_d\) by rotation when \(v\ne0\). Multiplication by \(x_d\), denoted \(M_z\), sends \(\mathcal H_\ell\) into \(\mathcal H_{\ell-1}\oplus\mathcal H_{\ell+1}\). The integral operator of the affine kernel is exactly
\[
T=aC+\|v\|(M_zC+CM_z).
\]
For a finite harmonic polynomial \(f\) set \(h=C^{1/2}f\). Since all \(c_\ell>0\), finite harmonic polynomials \(h\) are obtained in this way. Its quadratic form is
\[
\langle f,Tf\rangle
=\langle h,(aI+\|v\|J_c)h\rangle.
\]
The off-diagonal block formula in the finding follows by multiplication; there are no same-degree blocks by parity. The unitary parity map \(h(x)\mapsto h(-x)\) conjugates \(J_c\) to \(-J_c\), so whenever \(J_c\) is bounded its spectrum is symmetric about zero. Thus its sharp positivity criterion is \(a\ge\|v\|\|J_c\|\). If unbounded, the necessity of finite \(2\times2\) compressions below directly excludes every nonzero \(v\). Positivity of a continuous kernel on every finite site set is equivalent to nonnegativity of its integral quadratic form for every smooth test function: one direction follows by Riemann sums, the other by approximation of atomic measures by smooth densities. Consequently the harmonic criterion is exactly the finite-Gram criterion.

**2. Bounded adjacent ratios are sufficient.** Set
\[
w_\ell=\frac{c_\ell+c_{\ell+1}}{\sqrt{c_\ell c_{\ell+1}}}
=\sqrt{\frac{c_\ell}{c_{\ell+1}}}+\sqrt{\frac{c_{\ell+1}}{c_\ell}}.
\]
Each block \(\Pi_{\ell+1}M_z\Pi_\ell\) has norm at most one. For finite \(h=\sum h_\ell\), Cauchy–Schwarz and the inequality \(2uv\le u^2+v^2\) give
\[
|\langle h,J_ch\rangle|
\le 2\sup_\ell w_\ell\sum_\ell \|h_\ell\|\|h_{\ell+1}\|
\le 2\sup_\ell w_\ell\|h\|^2.
\]
Thus finite adjacent ratios imply a bounded selfadjoint \(J_c\) and a positive-width affine admissibility cone.

**3. Unbounded adjacent ratios are necessary.** On the axisymmetric normalized harmonics \(Z_\ell\in\mathcal H_\ell\) one has
\[
A_{\ell,d}:=\langle Z_{\ell+1},x_dZ_\ell\rangle=
\sqrt{\frac{(\ell+1)(\ell+d-2)}{(2\ell+d-2)(2\ell+d)}}
\quad (d\ge3,\ \ell\ge1).
\]
For \(d=2\), use \(Z_\ell(\theta)=\sqrt2\cos(\ell\theta)\), giving \(A_{\ell,2}=1/2\) for \(\ell\ge1\). These identities follow from the Gegenbauer (respectively cosine) three-term recurrence and normalization. In every fixed dimension \(A_{\ell,d}\to1/2\); in fact \(A_{\ell,d}\ge1/3\) when \(\ell\ge d\). The normalized quadratic form on the span of \(Z_\ell/\sqrt{c_\ell}\) and \(Z_{\ell+1}/\sqrt{c_{\ell+1}}\) has Hermitian matrix
\[
\begin{pmatrix}a&\|v\|A_{\ell,d}w_\ell\\
\|v\|A_{\ell,d}w_\ell&a\end{pmatrix}.
\]
If adjacent ratios are unbounded, then \(w_\ell\) is unbounded, and its least eigenvalue \(a-\|v\|A_{\ell,d}w_\ell\) is negative for some finite \(\ell\), regardless of finite \(a\) and nonzero \(v\). Approximation of the corresponding smooth signed density by a finite atomic measure yields an actual finite-site negative Gram witness. Conversely, if the ratios are bounded, Step 2 already supplies admissible nonzero \(v\). This proves the general equivalence and exact norm threshold.

**4. The fractional heat frontier.** Put \(\lambda_\ell=\ell(\ell+d-2)\) and \(c_\ell=e^{-t\lambda_\ell^\alpha}\). The adjacent coefficient ratio is \(e^{t\Delta_\ell}\), where
\[
\Delta_\ell=\lambda_{\ell+1}^\alpha-\lambda_\ell^\alpha.
\]
When \(0<\alpha\le1/2\), the map \(s\mapsto[s(s+d-2)]^\alpha\) is concave on \([0,\infty)\): \(\sqrt{s(s+d-2)}\) is concave and increasing, and its \(2\alpha\)-power is also concave and increasing. Hence \(0<\Delta_\ell\le\Delta_0=(d-1)^\alpha\). Therefore
\[
w_\ell=2\cosh(t\Delta_\ell/2)
\le 2\cosh\bigl(t(d-1)^\alpha/2\bigr),
\]
proving the asserted finite upper bound on \(\rho\). The lower bound \(\rho\ge2\) follows from the diagonal necessary condition \(a+2\langle v,x\rangle\ge0\) for every \(x\), since \(H_{t,\alpha}(x,x)>0\). When \(\alpha>1/2\),
\[
\Delta_\ell=2\alpha\ell^{2\alpha-1}(1+O_{d,\alpha}(\ell^{-1}))\longrightarrow\infty.
\]
Consequently the adjacent ratios are unbounded and Step 3 excludes every \(v\ne0\). More constructively, for any \(a\ge0, v\ne0\), every sufficiently large \(\ell\ge d\) satisfying
\[
\frac{\|v\|}{3}\exp(t\Delta_\ell/2)>a
\]
provides a negative two-degree quadratic form. For \(v=0\), positivity is exactly \(a\ge0\) by the positive harmonic spectrum. The transition is therefore both necessary and sufficient at the stated endpoint.

## Verification

A standalone Python standard-library checker (`checker.py`) independently constructs exact Legendre coefficient recurrences, verifies 25 exact adjacent-degree Gaunt integrals and parity identities, and generates finite-degree negative harmonic minors for ordinary and fractional spherical heat powers. It also checks the concavity regime numerically across several dimensions, with an explicit statement in the source that these finite tests supplement rather than prove the infinite-dimensional transition. The symbolic formulas and the analytic asymptotic and operator-norm arguments above, not numerical extrapolation, prove the universal result.

## Relationship to prior work

Buhmann and Jäger (first publicly posted May 6, 2021; published 2022) develop spectral block positivity criteria for axially symmetric spherical kernels. Their general coefficient-block characterization provides a conceptual starting point, but the bounded-adjacent-ratio if-and-only-if criterion and the half-order fractional-heat boundary require the additional degree-neighbor reduction and unbounded-block argument proved here. Guella and Jäger (public preprint 2022) focus on strict positive definiteness of another nonisotropic class; their diagonal spectral hypothesis differs from the off-diagonal harmonic blocks here. The earlier explicitly solvable spherical Poisson affine perturbation has geometric coefficient ratios, whereas the present result identifies the spectral decay frontier separating such stable perturbations from rigid heat smoothing; the Poisson case is a special illustration, not a proof of the general criterion. A 2024 axial spherical space-time paper supplies broad spectral representation results; full comparison of its subscription-only main text is unavailable, so historical priority beyond inspected material is not certified.

## Limitations

The finding addresses *multiplicative affine factors in the sum of two spatial coordinates*; it does not forbid other valid nonstationary heat covariances, such as products \(g(x)g(y)H_{t,\alpha}(x,y)\). The threshold \(\rho_{d,t,\alpha}\) is specified exactly as an operator norm, but no elementary closed form is asserted in general. The explicit two-degree obstruction is an integral quadratic-form certificate; converting it to a specific finite coordinate list would require quadrature choices, although finite-site existence follows rigorously by continuity. Public-priority comparisons cannot rule out undiscovered equivalent formulations. There has been no independent mathematical audit.

## References

1. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, first posted 2021-05-06, arXiv:2105.02586; *Journal of Fourier Analysis and Applications* 28 (2022), article 40. https://arxiv.org/abs/2105.02586 ; https://doi.org/10.1007/s00041-022-09913-x
2. J. C. Guella and J. Jäger, *Strictly positive definite non-isotropic kernels on two-point homogeneous manifolds: The asymptotic approach*, first posted 2022-05-15, arXiv:2205.07396; *Positivity* 28 (2024), article 4. https://arxiv.org/abs/2205.07396 ; https://doi.org/10.1007/s11117-023-01022-3
3. X. Emery, J. Jäger and E. Porcu, *Positive semidefinite kernels that are axially symmetric on the sphere and stationary in time: spectral and semi-spectral theory, and constructive approaches*, *Stochastic Environmental Research and Risk Assessment* 38 (2024), 2315–2329. https://doi.org/10.1007/s00477-024-02681-8
4. J. Cao, J. Zhang, Z. Sun and M. Katzfuss, *Locally Anisotropic Nonstationary Covariance Functions on the Sphere*, *Journal of Agricultural, Biological and Environmental Statistics* 29 (2024), 212–231. https://doi.org/10.1007/s13253-023-00573-y
