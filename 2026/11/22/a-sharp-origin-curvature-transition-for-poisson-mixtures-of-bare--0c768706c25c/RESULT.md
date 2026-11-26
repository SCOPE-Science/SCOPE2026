# A sharp origin-curvature transition for Poisson mixtures of Barenblatt packets

## Finding

Let \(\sigma>0\), \(r>0\), \(\ell>0\), \(a=(\sigma+2)^{-1}\), \(\nu=\sigma^{-1}\), and \(I_\sigma=\mathrm B(1/2,1+1/\sigma)\). The normalized one-dimensional Barenblatt packet at age \(t>0\) is
\[
g_t(x)=\frac{t^{-a}}{\ell I_\sigma}\left(1-\frac{x^2}{\ell^2t^{2a}}\right)_+^{\nu}.
\]
The **renewal-mixture** stationary density \(p_\sigma(x)=r\int_0^\infty e^{-rt}g_t(x)\,dt\) satisfies, as \(x\to0\),
\[
p_\sigma(0)-p_\sigma(x) \sim
\begin{cases}
\displaystyle \frac{r J_\sigma}{\ell^{\sigma+2}I_\sigma}|x|^{1+\sigma},&0<\sigma<1,\\[5pt]
\displaystyle \frac{3r}{\ell^3I_1}x^2\log\frac{\ell}{|x|},&\sigma=1,\\[5pt]
\displaystyle \frac{\nu\Gamma(1-3a)r^{3a}}{\ell^3I_\sigma}x^2,&\sigma>1,
\end{cases}
\qquad
J_\sigma=\frac{\nu}{1-a}\,\mathrm B\left(\frac{1-\sigma}{2},\nu\right).
\]
For every \(\sigma>0\), \(p_\sigma'(0)=0\). Its classical second derivative at zero exists and is finite if and only if \(\sigma>1\); then it equals \(-2\nu\Gamma(1-3a)r^{3a}/(\ell^3 I_\sigma)\). In the unit-mass porous-medium normalization \(\partial_t u=D\partial_x(u^\sigma\partial_xu)\), the \(\sigma=1\) choice has \(\ell^3=9D/2\), so the logarithmic prefactor is \(r/(2D)\).

## Assumptions and scope

Here \(x\in\mathbb R\) and \(z_+=\max(z,0)\). Substituting \(y=x/(\ell t^a)\) in the packet integral gives \(I_\sigma^{-1}\int_{-1}^1(1-y^2)^\nu dy=1\). The age is independent of the normalized within-packet spatial variable and has the exponential law of rate \(r\); thus the mixture is a probability density. It is a **linear mixture of nonlinear free-diffusion profiles**. It is not assumed to solve a nonlinear stationary source PDE. Direct integration gives \(p_\sigma(0)=r^a\Gamma(1-a)/(\ell I_\sigma)\).

## Proof

### The three deficit regimes

For \(x\ne0\), put \(s=(|x|/\ell)^{1/a}\), the minimum age whose packet reaches \(x\). Changing variables \(t=su\) gives
\[
p_\sigma(0)-p_\sigma(x)=\frac{r}{\ell I_\sigma}s^{1-a}\int_0^\infty e^{-rsu}u^{-a}F(u)\,du,
\qquad F(u)=1-(1-u^{-2a})_+^\nu. \tag{1}
\]
Here \(F(u)=1\) on \((0,1]\), and \(F(u)=\nu u^{-2a}+O(u^{-4a})\) at infinity. The undamped integrand is integrable exactly when \(3a>1\), i.e. \(0<\sigma<1\). In that case dominated convergence gives the integral limit \(J_\sigma\). Integration by parts, with \(u^{1-a}F(u)\to0\) at both endpoints, and the substitution \(v=u^{-2a}\) give
\[
J_\sigma=\frac{2a\nu}{1-a}\int_1^\infty u^{-3a}(1-u^{-2a})^{\nu-1}\,du
=\frac{\nu}{1-a}\int_0^1 v^{-(1+\sigma)/2}(1-v)^{\nu-1}\,dv.
\]
Since \(s^{1-a}=(|x|/\ell)^{1+\sigma}\), this proves the first line.

At \(\sigma=1\), \(a=1/3\) and \(\nu=1\), so the integral in (1) is \(\int_0^1 e^{-rsu}u^{-1/3}\,du+E_1(rs)\), where \(E_1(z)=\int_z^\infty e^{-v}\,dv/v\). Splitting at \(v=1\) yields \(E_1(z)=-\log z+O(1)\) as \(z\downarrow0\). Here \(s^{1-a}=(|x|/\ell)^2\) and \(-\log(rs)=3\log(\ell/|x|)-\log r\); the remainder in the deficit is \(O(x^2)\). To obtain the claimed unit-mass scale, write the packet as \(t^{-1/3}U(xt^{-1/3})\) with \(U(y)=(1-y^2/\ell^2)/(\ell I_1)\) inside its support. The similarity equation integrated from zero gives \(DUU'=-yU/3\). Comparing \(DU'=-2Dy/(\ell^3 I_1)\) with \(-y/3\) gives \(\ell^3 I_1=6D\). Since \(I_1=4/3\), this gives \(\ell^3=9D/2\).

For \(\sigma>1\), set \(z=x^2/(\ell^2 t^{2a})\) in the integrand without changing the age variable:
\[
\frac{p_\sigma(0)-p_\sigma(x)}{x^2}=
\frac{r}{\ell^3I_\sigma}\int_0^\infty e^{-rt}t^{-3a}\frac{1-(1-z)_+^\nu}{z}\,dt. \tag{2}
\]
The quotient is bounded on \((0,\infty)\) (it tends to \(\nu\) at zero, is continuous at \(1\), and equals \(1/z\) above \(1\)). Since \(3a<1\), dominated convergence gives the last line of the asymptotic from the gamma integral.

### Classical differentiation at the origin

All three deficits are \(o(|x|)\), so the ordinary two-sided derivative exists at zero and vanishes. To establish the classical second derivative, rather than just a symmetric difference limit, put \(q=x^2/\ell^2\). For each \(t>0\), write the packet deficit factor as
\[
1-(1-q/t^{2a})_+^\nu=\int_0^q \nu t^{-2a}(1-y/t^{2a})^{\nu-1}\mathbf1_{\{y<t^{2a}\}}\,dy,
\]
where the integrand is defined to be zero off the indicated domain. This identity follows by direct integration, including when \(q\ge t^{2a}\), because \(\nu>0\). Tonelli's theorem gives the exact primitive
\[
p_\sigma(0)-p_\sigma(x)=\frac{r\nu}{\ell I_\sigma}\int_0^q K(y)\,dy,
\qquad K(y)=\int_{y^{1/(2a)}}^\infty e^{-rt}t^{-3a}(1-y/t^{2a})^{\nu-1}\,dt. \tag{3}
\]
For every \(y>0\), substituting \(t=y^{1/(2a)}u\) proves continuity of \(K(y)\): on any compact interval of such \(y\), the transformed integrand is bounded by an integrable multiple of \((u-1)^{\nu-1}\) near \(u=1\) and by an exponentially decaying function at infinity. Thus (3) and the chain rule yield
\[
\frac{p_\sigma'(x)}{x}=-\frac{2r\nu}{\ell^3 I_\sigma}K(x^2/\ell^2),\qquad x\ne0. \tag{4}
\]
For \(3a<1\), write \(s=y^{1/(2a)}\) and split \(K\) at \(2s\). The contribution on \([s,2s]\) is at most
\[
s^{1-3a}\int_1^2 u^{-3a}(1-u^{-2a})^{\nu-1}\,du=O(s^{1-3a})=o(1).
\]
On \([2s,\infty)\) the factor \((1-y/t^{2a})^{\nu-1}\) is uniformly bounded because \(y/t^{2a}\le2^{-2a}<1\), and tends to \(1\) at each fixed \(t>0\). Dominated convergence, extending the integrand by zero below \(2s\), gives \(K(y)\to\int_0^\infty e^{-rt}t^{-3a}dt\). Equation (4) now gives the stated finite value of \(p_\sigma''(0)\). For \(3a\ge1\), the nonnegative integrands in (3), extended by zero below \(s\), converge pointwise for \(t>0\) to \(e^{-rt}t^{-3a}\), whose integral diverges. Fatou's lemma yields \(K(y)\to+\infty\), so the classical derivative quotient in (4) does not have a finite limit. No twice-differentiated packet integral is used.

## Verification

The companion `checker.py` (Python 3 with `mpmath`) is a finite diagnostic for normalization, the \(\sigma=1/2\) beta integral, the critical exponential-integral identity and convergence of the deficit coefficients at representative parameters. It is not a proof of the asymptotics or of classical differentiability. Equations (1)–(4) and the bounds at the moving support edge establish these for every parameter in the stated regimes.

## Relationship to prior work

Chełminiak's 2021 initial version gives the Poisson last-reset representation (v1 Eq. (21)) and the Barenblatt kernel (v1 Eq. (6)). The revised 2022 version gives the exact stationary age integral (v2 Eq. (28)) and the two closed profiles (v2 Eqs. (31)–(32), \(\sigma=1,2\)). The logarithmic critical term follows from the published exponential-integral profile, and the quadratic \(\sigma=2\) case is also encoded in the corresponding closed form. The present calculation concerns the explicit all-parameter origin classification, not the renewal model or those two individual cases.

Lenzi et al. (2023) instead treat the stationary nonlinear source PDE with a point source, for which mixing the free profiles is not in general a solution method. Global standardized moments of the Barenblatt renewal mixture address a different observable and do not supply a pointwise derivative criterion. These comparisons do not certify historical priority over all asymptotic analyses of such mixtures.

## Limitations

This is a stationary one-point result for one-dimensional normalized packets with independent exponential ages. It does not give convergence for a nonlinear resetting PDE, multiparticle dynamics, first-passage properties, or a general higher-order regularity classification.

## References

1. P. Chełminiak, *Non-linear diffusion with stochastic resetting*, [arXiv:2107.14680v1 (2021)](https://arxiv.org/abs/2107.14680v1), [v2 (2022)](https://arxiv.org/abs/2107.14680v2), [doi:10.1088/1751-8121/ac870a](https://doi.org/10.1088/1751-8121/ac870a).
2. E. K. Lenzi et al., *Results for Nonlinear Diffusion Equations with Stochastic Resetting*, Entropy **25** (2023), 1647, https://doi.org/10.3390/e25121647.
3. M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, J. Phys. A **53** (2020) 193001, https://arxiv.org/abs/1910.07993.
