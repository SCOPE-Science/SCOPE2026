# Gamma-product equilibrium and the reset-site mode transition

## Finding
Fix an integer \(d\geq3\), an exponent \(\alpha>0\), a diffusivity coefficient \(\kappa>0\), and a reset rate \(\lambda>0\). Start a rotationally invariant diffusion at the origin, with generator \(Lf(x)=\kappa |x|^{-\alpha}\Delta f(x)\) away from the origin, taking the conservative time-changed-Brownian entrance realization specified below. Independently reset the position to the origin at rate \(\lambda\). Write \(X_\infty\) for its unique stationary position, \(R=|X_\infty|\), \(n=\alpha+2\), and \(a=(d+\alpha)/n\). Then the **exact stationary radial law** is
\[
\frac{\lambda R^n}{\kappa n^2}\ \overset{\mathrm d}=\ G_1G_a,
\]
where \(G_1\) and \(G_a\) are independent unit-rate gamma variables with respective shapes \(1\) and \(a\). In particular, for every real \(q>-n\),
\[
\mathbb E R^q=\left(\frac{\kappa n^2}{\lambda}\right)^{q/n}\frac{\Gamma(1+q/n)\Gamma(a+q/n)}{\Gamma(a)},
\]
whereas \(\mathbb E R^q=+\infty\) for \(q\leq-n\). This gives an exact two-gamma simulation procedure without solving a spatial boundary-value problem.

Let \(\omega_d=2\pi^{d/2}/\Gamma(d/2)\) be the surface area of the unit sphere and \(p_*(x)=p_*(|x|)\) the stationary Lebesgue density. Its behavior at the reset site has a **sharp mode transition**:

* If \(0<\alpha<d-2\), \(p_*(r)\) decreases strictly on \((0,\infty)\) and diverges at zero.
* If \(\alpha=d-2\), \(p_*(r)\) decreases strictly on \((0,\infty)\) and extends continuously to \(p_*(0)=\lambda/[\kappa(d-2)\omega_d]\).
* If \(\alpha>d-2\), \(p_*(0)=0\), and the spatial density has a unique strict global mode at a positive radius.

All cases obey the universal inner-ball law
\[
\lim_{\varepsilon\downarrow0}\frac{\mathbb P(R\leq\varepsilon)}{\varepsilon^{\alpha+2}}
=\frac{\lambda}{\kappa(d-2)(\alpha+2)}.
\]
Thus the small-ball exponent is independent of the ambient dimension \(d\geq3\), even though the density at the injection point changes from divergent to finite to zero at \(\alpha=d-2\).

## Assumptions and scope
Take a Brownian motion \(B_s\) in \(\mathbb R^d\) with generator \(\kappa\Delta\), started at zero. For \(\alpha>0\) set \(A_s=\int_0^s |B_u|^\alpha\,du\), let \(T_t\) be its right-continuous inverse, and set \(X_t=B_{T_t}\). In dimensions \(d\geq3\), the origin is polar after departure, \(A_s\) is strictly increasing for positive \(s\) and tends to infinity, and this construction is conservative. It specifies the origin entrance law despite the singular coefficient in the formal Itô equation. Its generator on smooth test functions supported away from zero is \(\kappa |x|^{-\alpha}\Delta\). The reset process concatenates independent copies of this diffusion from zero at the times of an independent rate-\(\lambda\) Poisson process. The theorem concerns the Itô/time-change interpretation, not the Stratonovich or kinetic prescriptions.

The spatial mode refers to the \(d\)-dimensional Lebesgue density \(p_*(x)\), **not** the one-dimensional density of the random radius \(R\). The latter distinction is essential in dimensions greater than one.

## Proof
**1. Exact radial diffusion reduction.** For \(r>0\), the generator on radial test functions is
\[
L_r=\kappa r^{-\alpha}\left(\frac{d^2}{dr^2}+\frac{d-1}{r}\frac d{dr}\right).
\]
Apply it to a smooth function of \(Y=r^n/(\kappa n^2)\). As \(n=\alpha+2\), elementary differentiation gives
\[
L_r[f(Y)]=Yf''(Y)+af'(Y),\qquad a=\frac{d+\alpha}{\alpha+2}>1.
\]
Consequently \(Y_t=|X_t|^n/(\kappa n^2)\) is the squared-Bessel/CIR-type entrance diffusion with generator \(y\partial_{yy}+a\partial_y\), started at zero. Its Laplace transform solves the backward equation (or follows from the squared-Bessel transition law):
\[
\mathbb E_0[e^{-sY_t}]=(1+st)^{-a},\quad s,t\geq0,
\]
so \(Y_t\overset{\mathrm d}=tG_a\). The standard squared-Bessel entrance solution with \(a>1\) is unique, and the time change fixes this version.

**2. Reset equilibrium and product law.** Poisson resetting provides a coupling: from any two starts, synchronize at the first reset, so total variation distance between the two transition laws is at most \(e^{-\lambda t}\). The stationary law exists as the age mixture of an independent origin-started excursion \(X_E\), where \(E\) is exponential with rate \(\lambda\). This mixture is invariant by the memoryless property, and the coupling makes it unique. As \(Y_E\overset{\mathrm d}=EG_a\), with \(E\overset{\mathrm d}=G_1/\lambda\) independent of \(G_a\), the product identity follows. Gamma negative moments exist precisely for exponents greater than the negative shape. Since \(a>1\), the \(G_1\) factor fixes the sharp negative-moment cutoff at \(q=-n\).

**3. Density and universal origin asymptotics.** Put \(\nu=a-1=(d-2)/n>0\) and \(u=\lambda r^n/(\kappa n^2)\). Conditioning the product on one gamma factor and using the classical Bessel integral yields the density of \(U=G_1G_a\):
\[
f_U(u)=\frac{2}{\Gamma(a)}u^{\nu/2}K_\nu(2\sqrt u),\qquad u>0.
\]
Rotational invariance and the radial Jacobian imply
\[
p_*(r)=\frac{2\lambda}{\kappa n\omega_d\Gamma(a)}\,r^{n-d}\,u^{\nu/2}K_\nu(2\sqrt u),\qquad r>0.
\]
The Bessel asymptotic \(K_\nu(z)\sim 2^{\nu-1}\Gamma(\nu)z^{-\nu}\) for \(\nu>0\) gives
\[
p_*(r)\sim \frac{\lambda}{\kappa(d-2)\omega_d}\,r^{\alpha+2-d}
\quad\text{as }r\downarrow0.
\]
Integrating this radial density over the ball of radius \(\varepsilon\) proves the stated small-ball limit, including its exact coefficient. The asymptotic also establishes the three possible origin values.

**4. Global monotonicity and uniqueness of the off-origin mode.** Set \(z=2\sqrt u\) and \(F_\nu(z)=z^\nu K_\nu(z)\). Up to a positive constant,
\[
p_*(r)=r^{\beta}F_\nu(z),\qquad \beta=\alpha-d+2,\qquad z\propto r^{n/2}.
\]
The identity \(F_\nu'(z)=-z^\nu K_{\nu-1}(z)<0\) shows that \(p_*(r)\) is strictly decreasing whenever \(\beta\leq0\). When \(\beta>0\), necessarily \(0<\nu<1\). Define \(h(z)=zK_{\nu-1}(z)/K_\nu(z)\). Its Bessel equation yields the Riccati identity
\[
h'(z)=\frac{h(z)^2+2\nu h(z)-z^2}{z}.
\]
The standard small- and large-argument expansions imply \(h'(z)>0\) near zero and \(h'(z)\to1\) at infinity. At any hypothetical zero of \(h'\), differentiation of the displayed Riccati identity gives \(h''=-2\). Thus every zero would cross from positive to negative derivative, making a return to a positive derivative impossible. Therefore \(h'\) stays strictly positive on \((0,\infty)\); also \(h(0+)=0\) and \(h(z)\to\infty\). Finally,
\[
\frac{d\log p_*(r)}{d\log r}=\beta-\frac n2 h(z),
\]
which changes sign exactly once, from positive to negative. Its zero is the unique strict off-origin mode, characterized implicitly by \(h(z)=2\beta/n\). This proves all three regimes.

## Verification
A standalone Python diagnostic, `verification.py`, evaluates independently (i) Mellin moments by integration of the Bessel-product density, (ii) the stationary density by an exponential mixture of the free gamma heat kernel, (iii) the universal origin coefficient, and (iv) signs and root of the analytic radial logarithmic derivative across subcritical, critical and supercritical parameters. It completed 78 numerical checks successfully. These computations check formula consistency; the infinite-dimensional claims and uniqueness of the mode follow from the analytical proof above, not finite numerical sampling.

To reproduce: install Python 3 and `mpmath>=1.3`, then run `python verification.py` in the directory containing this file and the script. No external data, network service, or previously generated artifact is needed.

## Relationship to prior work
Frimpong, Bresque and Roldán (arXiv:2610.21962v1, 15 October 2026) analyze one-dimensional sluggish diffusion with Poisson and threshold resets; its stationary profile, first passage and costs do not state the \(d\geq3\) radial mode transition. Sandev, Fumeron, Henkel and Lenzi (arXiv:2609.24427v1, 21 September 2026) derive the planar stationary law for the specific power \(D(\rho)=D_0/\rho^2\) and several noise conventions. Their \(d=2\), \(\alpha=2\) Itô case is a **covered special case**, not part of the present \(d\geq3\) claim. Evans and Majumdar (arXiv:1404.4574v1) treat arbitrary dimension with **constant** diffusivity, the excluded \(\alpha=0\) face. Lenzi and collaborators (arXiv:2201.05598v1) address a **one-dimensional** power-law diffusion with a divergence-form forward operator different from the multidimensional Itô adjoint treated here. Classical gamma and squared-Bessel identities are acknowledged as ingredients, not claimed as inventions. The new content is their combined exact \(d\geq3\), \(\alpha>0\) stationary classification, reset-site mode threshold and dimension-independent small-ball law.

## Limitations
The theorem only covers integer dimensions \(d\geq3\), pure isotropic power-law Itô diffusivity, resetting exactly to the origin by an independent exponential clock, and the specified conservative entrance law. It gives no result for other stochastic conventions, general drift, spatially varying reset rates, or random reset positions. A previous implicit reduction through a radial Bessel kernel in older heterogeneous-diffusion literature remains a possible originality risk. Nothing here constitutes an independent mathematical audit.

## References
1. T. D. Frimpong, L. Bresque, É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first posted 15 October 2026), https://arxiv.org/abs/2610.21962 .
2. T. Sandev, S. Fumeron, M. Henkel, E. K. Lenzi, *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting*, arXiv:2609.24427v1 (first posted 21 September 2026), https://arxiv.org/abs/2609.24427 .
3. M. R. Evans, S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, arXiv:1404.4574v1 (2014), https://arxiv.org/abs/1404.4574 .
4. M. K. Lenzi et al., *Transient anomalous diffusion in heterogeneous media with stochastic resetting*, arXiv:2201.05598v1 (2022), https://arxiv.org/abs/2201.05598 .
5. Standard squared-Bessel transition laws and the classical modified-Bessel integral \(\int_0^\infty t^{\rho-1}e^{-at-b/t}\,dt=2(b/a)^{\rho/2}K_\rho(2\sqrt{ab})\) for \(a,b>0\).
