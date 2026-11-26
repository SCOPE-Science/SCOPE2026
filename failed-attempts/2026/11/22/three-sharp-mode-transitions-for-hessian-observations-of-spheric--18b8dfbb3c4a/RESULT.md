# Three sharp mode transitions for Hessian observations of spherical quadrupoles on antipodal caps

## Finding

For every integer \(d\ge3\) and every \(0<t<1\), let \(S^{d-1}\subset\mathbb R^d\) carry normalized Haar surface measure \(\sigma\) and its round metric. Let \(E_t=\{x\in S^{d-1}:x_d^2\ge t\}\), an antipodal pair of polar caps. On the complex space \(\mathcal H_2(d)=\{x\mapsto x^{\mathsf T}Ax:A=A^{\mathsf T},\ \operatorname{tr}A=0\}\) of pure degree-two spherical harmonics, define the *covariant-Hessian concentration operator* by the Rayleigh quotient
\[
R_t(f)=\frac{\int_{E_t}\|\nabla^2_S f(x)\|_{\mathrm{HS}}^2\,d\sigma(x)}{\int_{S^{d-1}}\|\nabla^2_S f(x)\|_{\mathrm{HS}}^2\,d\sigma(x)}.
\]
Here \(\nabla^2_S\) is the spherical covariant Hessian, and the norm is the Hilbert–Schmidt norm on complexified symmetric tangent tensors. There are precisely three spectral branches: \(\lambda_Z(t)\) on the zonal line \(\mathbb C\,(x_d^2-1/d)\); \(\lambda_M(t)\) on the mixed space \(\operatorname{span}_{\mathbb C}\{x_ix_d:1\le i<d\}\); and \(\lambda_T(t)\) on the space of trace-free quadratics involving only \(x_1,\ldots,x_{d-1}\). Their multiplicities are respectively \(1\), \(d-1\), and \((d-2)(d+1)/2\). Each eigenvalue is strictly between zero and one.

Define
\[
B_d=B\bigl(\tfrac12,\tfrac{d-1}{2}\bigr),\qquad C_d(t)=\frac{\sqrt t\,(1-t)^{(d-1)/2}}{B_d}.
\]
The following *exact identities* give all relative eigenvalue orders:
\[
\begin{aligned}
\lambda_Z-\lambda_M&=\frac{2C_d(t)}{d-1}\bigl((d+2)t-2\bigr),\\
\lambda_M-\lambda_T&=\frac{2C_d(t)}{(d-1)(d+1)}\bigl(d+3-2(d+2)t\bigr),\\
\lambda_Z-\lambda_T&=\frac{2C_d(t)}{d+1}\bigl((d+2)t-1\bigr).
\end{aligned}
\]
Consequently, writing \(t_1=1/(d+2)\), \(t_2=2/(d+2)\), and \(t_3=(d+3)/(2(d+2))\), the strict order from greatest to least is
\[
\begin{array}{c|c}
0<t<t_1&M>T>Z\\
t_1<t<t_2&M>Z>T\\
t_2<t<t_3&Z>M>T\\
t_3<t<1&Z>T>M.
\end{array}
\]
Here a letter denotes the corresponding spectral branch. At \(t_1\), the \(Z\) and \(T\) branches coincide as the *least* eigenvalue; at \(t_2\), \(Z\) and \(M\) coincide as the *greatest* eigenvalue; and at \(t_3\), \(M\) and \(T\) coincide as the *least* eigenvalue. There are no other interior coincidences. Thus the uniquely best-observed symmetry sector switches from mixed to zonal at \(t_2\), while the least-observed sector switches twice. At the three crossings, the corresponding extremal eigenspace dimensions are \(d(d-1)/2\), \(d\), and \(d(d+1)/2-2\), respectively. The sharp squared observation condition number is \(\max\{\lambda_Z,\lambda_M,\lambda_T\}/\min\{\lambda_Z,\lambda_M,\lambda_T\}\), with the active branches fixed by this table.

## Assumptions and scope

The observation is *continuous full covariant Hessian*, with no scalar value or gradient data; it is not the Euclidean ambient Hessian. The input is restricted to *one exact harmonic degree*, not all degrees through two, and the target region is exactly two equal antipodal round caps. The source and target norms are tensor energy norms; a constant multiple of both norms makes no difference. The theorem includes all complex inputs by polarization of the real-symmetric calculation. Endpoints \(t=0,1\) are excluded because the region is then the whole sphere or a zero-measure set and branch equalities become degenerate. The stated eigenvalues are observation-energy ratios, not singular values of a discrete sensor matrix.

## Proof

**1. Tensor geometry and global normalization.** For a complex symmetric trace-free \(d\)-by-\(d\) matrix \(A\), let \(f_A(x)=x^{\mathsf T}Ax\), \(P_x=I-xx^{\mathsf T}\), and \(q_A(x)=x^{\mathsf T}A^*Ax\). The spherical second fundamental form gives
\[
\nabla_S^2 f_A=2\bigl(P_xAP_x-f_A(x)P_x\bigr)\big|_{T_xS^{d-1}}.
\]
Taking the Hilbert–Schmidt norm, using \(\operatorname{tr}A=0\), yields the pointwise identity
\[
\frac14\|\nabla_S^2 f_A(x)\|_{\rm HS}^2
=\|A\|_F^2-2q_A(x)+(d+2)|f_A(x)|^2.
\]
The isotropic moments \(\int q_A\,d\sigma=\|A\|_F^2/d\) and \(\int|f_A|^2\,d\sigma=2\|A\|_F^2/[d(d+2)]\) therefore show
\[
\int_{S^{d-1}}\|\nabla_S^2f_A\|_{\rm HS}^2\,d\sigma=4\|A\|_F^2.
\]
This equality also proves that the Hessian map has no nonzero kernel on the stated space.

**2. The three invariant sectors and explicit eigenvalues.** Write \(n=d-1\) and \(u=x_d^2\). Under \(O(n)\), the trace-free symmetric matrices split orthogonally into a one-dimensional zonal block, an \(n\)-dimensional mixed block, and an \(n(n+1)/2-1\)-dimensional transverse trace-free block. Reflection in the last coordinate and transverse orthogonal invariance eliminate all off-block terms in the regional Hessian form. The law of \(u\) under \(\sigma\) has density
\[
p_d(u)=\frac{u^{-1/2}(1-u)^{n/2-1}}{B(1/2,n/2)},\qquad 0<u<1.
\]
For unit-Frobenius representatives, the conditional mean of the right side of the pointwise identity in Step 1 is, respectively,
\[
\begin{aligned}
F_T(u)&=1-\frac{2(1-u)}n+\frac{2(n+3)(1-u)^2}{n(n+2)},\\
F_M(u)&=1-u-\frac{1-u}{n}+\frac{2(n+3)u(1-u)}n,\\
F_Z(u)&=1-\frac{2[1+(n^2-1)u]}{n(n+1)}+\frac{(n+3)[1-(n+1)u]^2}{n(n+1)}.
\end{aligned}
\]
Indeed, take matrices \(A_T=\operatorname{diag}(B,0)\) with \(\operatorname{tr}B=0,\|B\|_F=1\); \(A_M=\left(\begin{smallmatrix}0&b\\b^{\mathsf T}&0\end{smallmatrix}\right)\) with \(2\|b\|^2=1\); and \(A_Z=\operatorname{diag}(I_n,-n)/\sqrt{n(n+1)}\). Conditional on \(u\), the first \(n\) coordinates are a uniform vector of squared length \(1-u\). The identities \(\mathbb E_y(y^{\mathsf T}By)^2=2\|B\|_F^2/[n(n+2)]\) for traceless real symmetric \(B\), and \(\mathbb E_y(b\cdot y)^2=\|b\|^2/n\), give the three formulas. For complex matrices, replace squares by moduli and polarize.

It follows that **each individual eigenvalue is explicit**:
\[
\boxed{\lambda_J(t)=\int_t^1F_J(u)p_d(u)\,du\quad(J\in\{Z,M,T\}).}
\]
This is a finite linear combination of incomplete beta integrals of orders \(1/2,3/2,5/2\), so no unknown spectral operator remains. Positivity and strict upper bounds follow because a nonzero analytic tensor Hessian cannot vanish on either of the two open sets \(E_t^\circ\) and \((S^{d-1}\setminus E_t)^\circ\). If its Hessian vanished on one, its pointwise polynomial-norm formula need not itself force vanishing globally, but analyticity of every Hessian component in spherical charts does; by continuation the Hessian would vanish everywhere, contradicting the global normalization.

**3. Boundary primitives and all three sharp crossings.** Let \(w(u)=u^{-1/2}(1-u)^{n/2-1}\). For arbitrary constants \(a,b\),
\[
\frac{d}{du}\left[u^{1/2}(1-u)^{n/2}(a+bu)\right]
=w(u)\left[\frac a2+\frac{3b-(n+1)a}{2}u-\frac{n+3}{2}bu^2\right].
\]
By direct expansion, the pairwise polynomial gaps are exactly the bracketed polynomials with
\[
\begin{array}{c|cc}
F_Z-F_M& a=4/n& b=-2(n+3)/n\\
F_M-F_T& a=-2(n+4)/[n(n+2)]&b=4(n+3)/[n(n+2)]\\
F_Z-F_T& a=2/(n+2)&b=-2(n+3)/(n+2).
\end{array}
\]
The primitive vanishes at \(u=1\). Integrating from \(t\) to \(1\) and dividing by the beta normalization produces precisely the three stated boundary-gap identities. Since \(C_d(t)>0\) and \(0<t_1<t_2<t_3<1\) for every \(d\ge3\), their signs prove the four strict order regions and all equality multiplicities. No unexamined eigenvalues can occur because the three invariant spaces exhaust \(\mathcal H_2(d)\). This completes the all-dimensional proof.

## Verification

Run \(\texttt{python check_hessian.py}\) with \(\texttt{numpy}\) and \(\texttt{sympy}\) installed. The checker verifies the three polynomial primitive identities symbolically for unrestricted dimension parameter, the three global beta-moment normalizations, and the pointwise trace identity. Independently it evaluates the entire \(5\)-by-\(5\) regional Hessian Gram matrix in dimension three, using Gauss–Legendre polar integration and equispaced azimuthal quadrature for nine cap widths, and checks all off-diagonal entries and every branch against independent integrated polynomials. Expected terminal line: \(\texttt{HESSIAN_CAP_CHECKS_PASS 115}\). The general proof relies on the algebraic identities above, not on numerical evidence. The test is supplementary, not an independent certification of the original result.

## Relationship to prior work

Simons and Dahlen (2006) formulate the scalar polar-gap/double-cap spherical Slepian operator and its low-pass harmonic computation, but do not compute the covariant Hessian energy spectrum on the image of one harmonic degree. Michel, Plattner and Seibert (arXiv first public 2021-03-26) construct a general spin-weighted tensor Slepian framework, especially Section 4.3, for arbitrary tensor field coefficients on the two-sphere. That tensor-field operator is substantially broader in domain, but the specific **coupled Hessian image** of scalar pure quadrupoles with its norm, all-dimensional three-branch formulas and three precise crossing thresholds are not stated there. The published 2026 exact scalar-quadrupole polar-cap theorem compares scalar values and has only the threshold \(t=1/d\); its full result does not imply the different Hessian observation eigenvalues or their two additional least-mode crossings. Thus the present result is a concrete, analytically solved derivative-observation problem, rather than a claim that polar-cap concentration, tensor harmonics, or the three ambient symmetry sectors were discovered here.

## Limitations

The novelty assessment is best-knowledge and historical priority is not independently certified; a specialized tensor-geodesy treatment or a computation implicit in a general spin-weighted framework could give equivalent formulas. Only full covariant-Hessian continuous observations of *pure degree two* are proved; no noisy/discrete sensor theorem, higher-degree theorem, non-antipodal geometry, or arbitrary tensor-field claim follows. Numerical checks are finite and cannot prove the general theorem. The three equalities occur for the given squared coordinate threshold \(t\), not directly for latitude angle or area fraction without conversion.

## References

1. V. Michel, A. Plattner and K. Seibert, “A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator,” arXiv:2103.14650v1, posted March 26, 2021, https://arxiv.org/abs/2103.14650 (especially Section 4.3).
2. F. J. Simons and F. A. Dahlen, “Spherical Slepian functions and the polar gap in geodesy,” *Geophysical Journal International* **166** (2006), 1039–1061, https://doi.org/10.1111/j.1365-246X.2006.03065.x, https://geoweb.princeton.edu/people/simons/PDF/reprints/GJI-2006.pdf.
3. “A sharp quadrupolar concentration-mode transition for antipodal caps in every sphere dimension,” (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-quadrupolar-concentration-mode-transition-for-antipodal--979df7aea2e4 (scalar-value comparison; different observation functional).
