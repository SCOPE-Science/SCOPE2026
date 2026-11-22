# A sharp origin-curvature transition for Poisson mixtures of Barenblatt packets

## Finding
Let \(\sigma>0\), \(r>0\), \(\ell>0\), \(a=(\sigma+2)^{-1}\), \(\nu=\sigma^{-1}\), and \(I_\sigma=\mathrm B(1/2,1+1/\sigma)\). An exactly normalized one-dimensional Barenblatt excursion packet at age \(t>0\) is
\[
g_t(x)=\frac{t^{-a}}{\ell I_\sigma}\left(1-\frac{x^2}{\ell^2t^{2a}}\right)_+^{\nu}.
\]
Define the **renewal-mixture** stationary density \(p_\sigma(x)=r\int_0^\infty e^{-rt}g_t(x)\,dt\). Its behavior at the reset origin changes sharply at \(\sigma=1\):
\[
p_\sigma(0)-p_\sigma(x) \sim
\begin{cases}
\displaystyle \frac{r J_\sigma}{\ell^{\sigma+2}I_\sigma}|x|^{1+\sigma},&0<\sigma<1,\\[5pt]
\displaystyle \frac{3r}{\ell^3I_1}x^2\log\frac{\ell}{|x|},&\sigma=1,\\[5pt]
\displaystyle \frac{\nu\Gamma(1-3a)r^{3a}}{\ell^3I_\sigma}x^2,&\sigma>1,
\end{cases}
\]
where
\[
J_\sigma=\frac{\nu}{1-a}\,\mathrm B\left(\frac{1-\sigma}{2},\nu\right)>0.
\]
For every positive \(\sigma\), the density has derivative zero at the origin. Its classical second derivative at zero exists and is finite **if and only if** \(\sigma>1\); then it equals \(-2\nu\Gamma(1-3a)r^{3a}/(\ell^3 I_\sigma)\). The logarithmic law at \(\sigma=1\) is a non-power-law boundary between the fractional cusps and finite curvature. In the standard porous-medium normalization \(\partial_t u=D\partial_x(u^\sigma\partial_xu)\), the \(\sigma=1\) choice has \(\ell^3=9D/2\), giving the universal logarithmic prefactor \(r/(2D)\).

## Assumptions and scope
All parameters above are strictly positive, \(x\in\mathbb R\), and \(z_+\) denotes \(\max(z,0)\). The packet is a normalized Barenblatt–Pattle point-source profile. The random age has exactly the \(\mathrm{Exp}(r)\) law, independent of the packet's within-age position. The result is about that **linear renewal mixture of nonlinear free-diffusion profiles**. No statement equates it with the stationary solution of a nonlinear source PDE: such an equation generally does not obey a linear restart-renewal superposition.

The integral is a probability density because the substitution \(y=x/(\ell t^a)\) yields \(\int_\mathbb Rg_t(x)dx=I_\sigma^{-1}\int_{-1}^1(1-y^2)^\nu dy=1\). Moreover \(p_\sigma(0)=r^a\Gamma(1-a)/(\ell I_\sigma)<\infty\).

## Proof
For \(x\ne0\) set \(s=(|x|/\ell)^{1/a}\). At ages below \(s\) the spatial packet vanishes. Hence exactly
\[
p_\sigma(0)-p_\sigma(x)=\frac{r}{\ell I_\sigma}s^{1-a}\int_0^\infty e^{-rsu}u^{-a}F(u)du,
\qquad F(u)=1-(1-u^{-2a})_+^{\nu}.
\tag{1}
\]
Here \(F(u)=1\) for \(u<1\) and \(F(u)=\nu u^{-2a}+O(u^{-4a})\) as \(u\to\infty\). Thus the positive integrand has tail \(\nu u^{-3a}\). Its unweighted integral is finite exactly when \(3a>1\), equivalent to \(0<\sigma<1\). Dominated convergence in (1) then gives the first case. Integrating by parts, using \(u^{1-a}F(u)\to0\) at both endpoints and substituting \(v=u^{-2a}\), yields
\[
J_\sigma=\frac{2a\nu}{1-a}\int_1^\infty u^{-3a}(1-u^{-2a})^{\nu-1}du
=\frac{\nu}{1-a}\int_0^1v^{-\frac{\sigma+1}{2}}(1-v)^{\nu-1}dv,
\]
which is the stated positive beta constant.

At \(\sigma=1\), \(a=1/3\), \(\nu=1\), and the integrand in (1), without the exponential, equals \(u^{-1/3}\) for \(u<1\) and \(u^{-1}\) for \(u\ge1\). Its Laplace-damped integral is exactly \(\int_0^1e^{-rsu}u^{-1/3}du+E_1(rs)=-\log(rs)+O(1)\), with \(E_1(z)=\int_z^\infty e^{-v}dv/v\). Since \(s=(|x|/\ell)^3\), the middle coefficient follows, and the remainder is \(O(x^2)\).

For \(\sigma>1\), write directly
\[
\frac{p_\sigma(0)-p_\sigma(x)}{x^2}
=\frac{r}{\ell^3I_\sigma}\int_0^\infty e^{-rt}t^{-3a}\frac{1-(1-z)_+^{\nu}}{z}\,dt,
\quad z=\frac{x^2}{\ell^2t^{2a}}.
\tag{2}
\]
For every \(\nu>0\), the function \([1-(1-z)_+^\nu]/z\) is bounded for \(z>0\) and tends to \(\nu\) as \(z\downarrow0\). The remaining weight \(t^{-3a}e^{-rt}\) is integrable exactly when \(3a<1\), or \(\sigma>1\). Dominated convergence gives the third coefficient, using \(\int_0^\infty t^{-3a}e^{-rt}dt=r^{3a-1}\Gamma(1-3a)\).

Finally (1) gives \(p_\sigma(0)-p_\sigma(x)=o(|x|)\) in every regime, hence the symmetric derivative at zero is zero. The second symmetric difference is \(2[p_\sigma(x)-p_\sigma(0)]/x^2\), which tends to a finite negative number only for \(\sigma>1\), and tends to \(-\infty\) for \(0<\sigma\le1\). For \(\sigma>1\), the density's derivative exists away from zero by differentiating its moving-lower-limit integral; its difference quotient at zero gives the same second derivative, so the classical second derivative exists. (Equivalently, near the origin the second-derivative integral is uniformly locally integrable when \(3a<1\).) This establishes the full classification.

## Verification
Run \(\texttt{python3 checker.py}\) with \(\texttt{mpmath}\) installed. The checker independently tests normalizations, the \(\sigma=1/2\) beta integral by piecewise integration, the exact critical \(\sigma=1\) exponential-integral representation, and finite-\(x\) convergence to the theoretical coefficients in all three regimes. Symbolic and numerical checks are corroboration; the analytic bounds and dominated-convergence arguments above prove the quantified theorem.

## Relationship to prior work
Chełminiak (arXiv:2107.14680, initial public version 2021-07-30) gives the Barenblatt reset-age renewal formula, including closed stationary densities for \(\sigma=1\) and \(\sigma=2\) and numerical/approximate forms otherwise. The exact \(\sigma=1\) special function contains an exponential integral whose logarithmic small-distance term is implicit. The present contribution is the **all-positive-\(\sigma\) threshold separating infinite and finite central curvature**, with explicit fractional and borderline logarithmic coefficients; the renewal construction itself is not claimed new.

Lenzi et al. (2023) derive a distinct stationary profile for the **nonlinear source PDE** \(\partial_t u=D\partial_{xx}(u^{1+\sigma})-r(u-\delta_0)\), which is not identical to the linearly mixed free Barenblatt density for nonlinear diffusion. These objects must not be conflated. Earlier work on proportional Brownian resetting studies a different reset map and does not imply the nonlinear Barenblatt curvature threshold. Global-moment formulas for Barenblatt renewal mixtures likewise do not determine pointwise differentiability.

## Limitations
This is an exact stationary one-point result for the specified renewal-mixture model, not a theorem about convergence of a general nonlinear restarting PDE, multi-particle interactions, or first-passage properties. It does not classify every higher derivative or all exceptional exponents above the second-order threshold. Earlier special-function formulas may implicitly contain individual parameter cases, so an independent publication-priority audit is still needed.

## References
1. P. Chełminiak, *Non-linear diffusion with stochastic resetting*, arXiv:2107.14680, initially public 2021-07-30, https://arxiv.org/html/2107.14680v2 .
2. E. K. Lenzi et al., *Results for Nonlinear Diffusion Equations with Stochastic Resetting*, Entropy **25** (2023), 1647, https://doi.org/10.3390/e25121647 .
3. M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, J. Phys. A **53** (2020) 193001, for linear renewal-resetting context.
