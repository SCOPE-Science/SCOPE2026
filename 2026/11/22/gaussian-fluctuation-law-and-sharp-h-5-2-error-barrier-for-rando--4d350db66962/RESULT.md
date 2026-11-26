# Gaussian fluctuation law and sharp \(h^{5/2}\) error barrier for randomized two-stage SDIRK

## Finding

For the random two-stage diagonally implicit scheme specified below, the \(h^{-5/2}\)-rescaled **nodal error process** has a Gaussian limit for smooth autonomous vector fields. The limit may be degenerate. Its diffusion coefficient is proportional to the third-order elementary-differential combination
\[
H(y)=Df(y)\bigl[Df(y)f(y)\bigr]-\frac12D^2f(y)[f(y),f(y)].
\]
Its scalar linear specialization has the exact, strictly positive asymptotic mean-square coefficient
\[
\lim_{N\to\infty}\frac{\mathbb E|U_N-u_0e^{\lambda T}|^2}{(T/N)^5}
=\frac{\lambda^6 T u_0^2 e^{2\lambda T}}{180},
\qquad \lambda,u_0\in\mathbb R\setminus\{0\}.
\]
Thus the order \(5/2\) cannot be improved even on a smooth scalar dissipative test equation (take \(\lambda<0\)). The exact coefficient measures irreducible random stage noise, rather than an instability of the integration method.

## Assumptions and scope

Let \(d\ge1\), \(T>0\), \(u_0\in\mathbb R^d\), and let \(f\in C^4(\mathbb R^d;\mathbb R^d)\) have globally bounded derivatives of orders 1 through 4 (hence at most linear growth). Let \(u\) solve \(u'=f(u)\), \(u(0)=u_0\). Take \(h=T/N\), independent \(\xi_j\sim\mathrm{Unif}[1/2,1]\), and for each step use the unique small-step solution of
\[
\begin{aligned}
K_{1,n}&=f(U_n+h\xi_{n+1}K_{1,n}),\\
K_{2,n}&=f(U_n+h(1-2\xi_{n+1})K_{1,n}+h\xi_{n+1}K_{2,n}),\\
U_{n+1}&=U_n+\frac h2(K_{1,n}+K_{2,n}),\qquad U_0=u_0.
\end{aligned}
\]
The corresponding Butcher matrix is \(A(x)=\begin{psmallmatrix}x&0\\1-2x&x\end{psmallmatrix}\) and the weights are \((1/2,1/2)\). Let \(e_n=U_n-u(nh)\). Define \(Z_h\) by linearly interpolating the values \(h^{-5/2}e_n\) at the grid points. By linearity, this is exactly the scaled difference of the two piecewise linear interpolants of \(U_n\) and \(u(nh)\) on the same grid. Subtracting the continuous exact trajectory \(u(t)\) from the piecewise linear numerical trajectory instead would add a deterministic interpolation defect that can be of order \(h^2\) before scaling.

Write \(J(t)=Df(u(t))\), and let \(\Psi(t,s)\) solve \(\partial_t\Psi(t,s)=J(t)\Psi(t,s)\), \(\Psi(s,s)=I\). The claimed limit is in distribution in \(C([0,T];\mathbb R^d)\), with covariance
\[
\operatorname{Cov}(Z(t),Z(r))=
\frac1{180}\int_0^{\min(t,r)}\Psi(t,s)H(u(s))H(u(s))^\top\Psi(r,s)^\top\,ds.
\]
Here the scalar driving Brownian motion is the same across all vector coordinates because each time step uses one shared random parameter.

## Proof

**1. Exact third-order local expansion.** Let \(\varphi_h\) be the exact autonomous flow. Standard Taylor expansion of the two implicit stage equations, uniform in \(x\in[1/2,1]\) and for \(y\) in any fixed bounded set, yields
\[
\Phi_h(y,x)=\varphi_h(y)+h^3\delta(x)H(y)+O(h^4),\qquad
\delta(x)=x(1-x)-\frac16.
\]
For clarity, the order-three Runge–Kutta coefficients are \(b^\top Ac=x(1-x)\) and \(b^\top c^{\odot2}=1/2-x(1-x)\). The exact flow's order-three coefficient is \((Df)^2f/6+D^2f[f,f]/6\); subtracting gives precisely the displayed \(H\), with no missing factor. The local remainder and its Lipschitz constants are uniform under the stated derivative bounds. Direct polynomial-jet verification is included in `verify.py`.

**2. Centering and variance.** For \(\xi\sim\mathrm{Unif}[1/2,1]\), exact integration gives
\[
\mathbb E[\xi(1-\xi)]=\frac16,\qquad
\mathbb E[\xi^2(1-\xi)^2]=\frac1{30},\qquad
\mathbb E[\delta(\xi)^2]=\frac1{180}.
\]
Thus the third-order local fluctuation is conditionally centered and bounded, with a nonzero fixed variance.

**3. Global error and linearization.** For sufficiently small \(h\), each implicit stage map is a contraction since \(h\sup\|Df\|<1\); the method is well defined. Linear growth bounds keep its iterates in a common deterministic bounded set on \([0,T]\), uniformly in the stage choices. From the flow expansion,
\[
e_{n+1}=\varphi_h(U_n)-\varphi_h(u(nh))
+h^3\delta(\xi_{n+1})H(U_n)+O(h^4).
\]
The partial sums \(M_m=\sum_{n<m}h^3\delta(\xi_{n+1})H(U_n)\) form a martingale with \(\mathbb E\max_{m\le N}\|M_m\|^2=O(Nh^6)=O(h^5)\) by boundedness of the coefficients and the martingale maximal inequality. On the common bounded set, \(\varphi_h-I\) is \(O(h)\)-Lipschitz, so summing the error recursion gives \(\|e_m\|\le \max_{j\le N}\|M_j\|+C_T h^3+C h\sum_{n<m}\|e_n\|\). Discrete Gronwall thus gives \(\mathbb E\max_{0\le n\le N}\|e_n\|^2\le C_T h^5\). Because \(D\varphi_h(u)=I+hDf(u)+O(h^2)\), the recursion can be linearized:
\[
e_{n+1}=(I+hJ(nh))e_n+h^3\delta(\xi_{n+1})H(u(nh))+r_{n+1},
\qquad h^{-5/2}\max_{m\le N}\Bigl\|\sum_{n<m}r_{n+1}\Bigr\|\xrightarrow{P}0.
\]
To verify the last estimate, sum the individual uniform errors \(O(h^4)\), \(O(h^2\|e_n\|)\), \(O(h\|e_n\|^2)\), and \(O(h^3\|e_n\|)\), and apply the preceding maximal \(L^2\) estimate. Their cumulative orders are respectively \(h^3\), \(O_P(h^{7/2})\), \(O_P(h^5)\), and \(O_P(h^{9/2})\), all \(o_P(h^{5/2})\).

**4. Functional central limit theorem.** The normalized driving martingale has increments \(\sqrt h\,\delta(\xi_{n+1})H(u(nh))\). Its quadratic covariation converges uniformly to \(\frac1{180}\int_0^t H(u(s))H(u(s))^\top ds\). Increments are bounded by \(C\sqrt h\), so Lindeberg's condition is automatic. The triangular-array martingale functional CLT and convergence of the discrete fundamental matrices to \(\Psi\) establish
\[
Z_h\Rightarrow Z,\qquad dZ(t)=J(t)Z(t)\,dt+\frac1{\sqrt{180}}H(u(t))\,dB_t,\quad Z(0)=0.
\]
This is the stated one-Brownian Gaussian process with the explicit covariance.

**5. Exact scalar lower bound.** For \(f(y)=\lambda y\), the scalar one-step multiplier is
\[
R(z,x)=\frac{1+(1-2x)z+(x^2-2x+1/2)z^2}{(1-xz)^2},\quad z=\lambda h.
\]
Uniformly over \(x\in[1/2,1]\),
\[
R(z,x)=1+z+z^2/2+x(1-x)z^3+O(z^4).
\]
With \(m_1(z)=\mathbb E[R(z,\xi)]\) and \(m_2(z)=\mathbb E[R(z,\xi)^2]\), exact moment expansion yields \(m_1(z)=e^z+O(z^4)\) and \(m_2(z)-m_1(z)^2=z^6/180+O(z^7)\). Independence gives \(\mathbb E U_N=u_0m_1(z)^N\) and \(\mathbb E U_N^2=u_0^2m_2(z)^N\). Consequently the squared bias is \(O(h^6)\), whereas the variance equals \(u_0^2e^{2\lambda T}\lambda^6Th^5/180+O(h^6)\), proving the exact nonzero limit. This is an infinite-\(N\) conclusion from exact expansions, not an inference from finite simulations.

**6. Noise-cancellation classification in one dimension.** On any interval where a scalar \(C^4\) vector field \(f\) is nonzero,
\[
H(y)=f(y)f'(y)^2-\tfrac12 f(y)^2f''(y)
=\tfrac12f(y)^4\Bigl(\frac1{f(y)}\Bigr)''.
\]
Thus \(H\equiv0\) if and only if \(1/f\) is affine. Equivalently \(f(y)=1/(ay+b)\) with a nonvanishing denominator, which includes constants. In this case the third-order random term vanishes on the full trajectory region and the uniform local \(O(h^4)\) estimate yields a pathwise global \(O(h^3)\) bound for finite horizons avoiding the pole. This is a local-domain corollary; the global regularity assumption above is not asserted across a reciprocal field's pole.

## Verification

Run `python verify.py` with SymPy installed. The script independently verifies the two-stage B-series order-three jet for an arbitrary scalar cubic local vector-field Taylor polynomial, the Butcher coefficients, the exact uniform moments \(1/6\), \(1/30\), \(1/180\), the leading variance term in the scalar stability multiplier, and the differential identity characterizing scalar cancellation. The analytical step from bounded martingale increments to the Gaussian process uses the standard functional martingale CLT; the finite symbolic script is not a substitute for that theorem. It has been executed successfully on the embedded file.

## Relationship to prior work

Eisenmann, Jans, Kruse and Podhaisky (2026) define this exact uniformly randomized two-stage SDIRK method, verify the order-three conditions in expectation (Remark 3.3), and establish an \(L^2\) global convergence bound reaching order \(5/2\) (Theorem 7.5). The present result addresses the **distribution and exact leading error constant**, rather than restating that bound or the expected order conditions. Its linear scalar example demonstrates sharpness even with analytic coefficients, and its differential \(H\) identifies when the random leading error cancels. Bochacik, Przybyłowicz and Stępień (2025) study other implicit randomized RK2 constructions, with stability-region and convergence estimates rather than this method's functional error distribution. Published results on antithetically paired randomized *explicit* RK schemes have a different tableau and a different leading differential functional; their existence does not imply this SDIRK theorem. The method itself, standard B-series expansion, and functional martingale CLT are not claimed as new.

## Limitations

The result treats independently refreshed uniform random stages, fixed finite \(T\), autonomous vector fields, and a small-step limit. It is not a finite-stepsize stability bound and does not cover irregular time dependence, correlated stages, stochastic forcing, or infinite-dimensional discretizations. Gaussian weak convergence alone does not assert convergence of every moment; the scalar exact mean-square asymptotic is separately proved. Literature priority is subject to possible uncatalogued equivalent stochastic-modified-equation CLTs.

## References

1. M. Eisenmann, M. Jans, R. Kruse, H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge–Kutta Method*, arXiv:2607.18928v1, 2026-07-21, https://arxiv.org/abs/2607.18928 .
2. T. Bochacik, P. Przybyłowicz, Ł. Stępień, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, BIT Numerical Mathematics 65, article 7 (2025), https://doi.org/10.1007/s10543-024-01050-9 . Preprint https://arxiv.org/abs/2404.19059 .
3. R. Kruse, Y. Wu, *Error analysis of randomized Runge–Kutta methods for differential equations with time-irregular coefficients*, Computational Methods in Applied Mathematics 17(3) (2017), 479–498, https://arxiv.org/abs/1701.03444 .
4. Standard martingale functional central limit theorem (bounded triangular-array martingale differences); used as a classical probability limit result, not claimed as a new theorem.
