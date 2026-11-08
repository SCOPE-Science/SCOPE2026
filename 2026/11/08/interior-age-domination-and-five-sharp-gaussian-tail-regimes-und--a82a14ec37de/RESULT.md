# Interior-age domination and five sharp Gaussian-tail regimes under anisotropic resetting

## Finding

For a centered, anisotropic Gaussian resetting distribution in an isotropic harmonic drift, extreme *joint spatial density* can be produced predominantly by an **intermediate** time since resetting, rather than by either freshly reset particles or long-unreset equilibrium particles. All directions admit a complete five-regime classification (plus an exact flat degeneracy), including sharp algebraic factors multiplying the Gaussian rate. This is distinct from a one-dimensional projected marginal, whose conditional variance depends monotonically on reset age.

For any unit direction \(e\in\mathbb R^d\), the stationary density on its ray has the general form
\[
p(te)\sim K_e\,t^{-\nu_e}\exp\!\left[-\frac{t^2}{2}f_e(y_*)\right],\qquad t\to\infty,
\]
with \(K_e>0\) and explicit \(\nu_e\). Both the minimizing age and its fluctuation law are classified below.

## Assumptions and scope

Fix \(d\ge2\), \(\kappa,r>0\), symmetric positive-definite \(d\times d\) matrices \(Q,S\), and a unit direction \(e\). Between independent Poisson resets of rate \(r\), let
\[
dX_t=-\kappa X_t\,dt+\sqrt{2\kappa}\,Q^{1/2}dW_t.
\]
Every reset independently replaces the *entire* position by a new \(N(0,S)\) vector. All noise, reset locations and reset times are independent. Let \(p\) be the unique stationary density. Define
\[
\alpha=\frac{r}{2\kappa},\quad B=S-Q,\quad C(y)=Q+yB,\quad
h(y)=\frac1{(2\pi)^{d/2}\sqrt{\det C(y)}},\quad
f(y)=e^{\mathsf T}C(y)^{-1}e,\qquad 0\le y\le1.
\]
All these functions are smooth on the closed interval and \(h>0\). Write \(d_0=f'(0)\), \(d_1=f'(1)\). If \(BQ^{-1}e\ne0\), the following alternatives are exhaustive, mutually exclusive and have \(f''(y)>0\) everywhere:

| Regime | Exact criterion | Minimizer \(y_*\) | Power \(\nu_e\) | Leading coefficient \(K_e\) |
| --- | --- | --- | --- | --- |
| Old regular | \(d_0>0\) | \(0\) | \(2\alpha\) | \(h(0)\Gamma(1+\alpha)(2/d_0)^\alpha\) |
| Old tangent | \(d_0=0\) | \(0\) | \(\alpha\) | \(h(0)\Gamma(1+\alpha/2)(4/f''(0))^{\alpha/2}\) |
| Interior age | \(d_0<0<d_1\) | unique \(f'(y_*)=0\) in \((0,1)\) | \(1\) | \(2\alpha y_*^{\alpha-1}h(y_*)\sqrt{\pi/f''(y_*)}\) |
| Young tangent | \(d_1=0\) | \(1\) | \(1\) | \(\alpha h(1)\sqrt{\pi/f''(1)}\) |
| Young regular | \(d_1<0\) | \(1\) | \(2\) | \(2\alpha h(1)/(-d_1)\) |

For the remaining, flat case \(BQ^{-1}e=0\), \(f(y)\equiv f(0)\); there is no preferred age and the ray density equals exactly
\[
p(te)=e^{-t^2f(0)/2}\,\alpha\int_0^1y^{\alpha-1}h(y)\,dy.
\]

## Proof

**1. Stationary mixture.** By Poisson regeneration the stationary elapsed time \(A\) since the most recent reset is exponential with rate \(r\); the reset draw is independent of this age. Given \(A=a\), the harmonic solution is a sum of two independent centered Gaussian vectors with covariances \(e^{-2\kappa a}S\) and \((1-e^{-2\kappa a})Q\). Thus its covariance is \(C(e^{-2\kappa a})\). The transformation \(Y=e^{-2\kappa A}\) gives \(\Pr(Y\in dy)=\alpha y^{\alpha-1}dy\) for \(0<y<1\). Therefore the exact stationary density is
\[
p(x)=\alpha\int_0^1 y^{\alpha-1}h(y)\exp\!\left[-\frac12x^{\mathsf T}C(y)^{-1}x\right]dy.
\]
This positive normalized density is the unique invariant law because every reset couples all initial states by replacing them with an identical independent Gaussian draw; the probability of no reset by time \(t\) is \(e^{-rt}\).

**2. Strict convexity and age minimization.** Set \(u_y=C(y)^{-1}e\). Matrix differentiation yields the exact identities
\[
f'(y)=-u_y^{\mathsf T}Bu_y,\qquad
f''(y)=2(Bu_y)^{\mathsf T}C(y)^{-1}(Bu_y)\ge0.
\]
If \(Bu_y=0\) at even one point, then \(Qu_y=e\) and \(u_z=u_y=Q^{-1}e\) for all \(z\), so \(BQ^{-1}e=0\) and \(f\) is constant. Otherwise \(f''>0\) at every point. Strict increase of \(f'\) then proves all five slope alternatives and uniqueness of any interior minimizer. It also proves that no other age-dependent exponential rates can dominate.

**3. Sharp Laplace factors.** For a nonflat direction factor out \(\exp[-t^2 f(y_*)/2]\) from the exact density. Near an old regular minimum, \(f(y)-f(0)=d_0y+O(y^2)\); with \(z=t^2y\), the remaining integral tends to
\[
\alpha h(0)t^{-2\alpha}\int_0^\infty z^{\alpha-1}e^{-d_0z/2}dz
=h(0)\Gamma(1+\alpha)(2/d_0)^\alpha t^{-2\alpha}.
\]
For an old tangent, \(f(y)-f(0)=f''(0)y^2/2+O(y^3)\), and \(z=ty\) gives \(h(0)\Gamma(1+\alpha/2)(4/f''(0))^{\alpha/2}t^{-\alpha}\).

At an interior minimizer, \(f(y)-f(y_*)=f''(y_*)(y-y_*)^2/2+O(|y-y_*|^3)\). A whole-line Gaussian Laplace integral with \(z=t(y-y_*)\) gives \(2\alpha y_*^{\alpha-1}h(y_*)\sqrt{\pi/f''(y_*)}\,t^{-1}\). At a young tangent, the corresponding *half*-Gaussian integral near \(y=1\) gives \(\alpha h(1)\sqrt{\pi/f''(1)}\,t^{-1}\). At a young regular minimum, \(f(y)-f(1)=(-d_1)(1-y)+O((1-y)^2)\); setting \(z=t^2(1-y)\) yields \(2\alpha h(1)(-d_1)^{-1}t^{-2}\). Smoothness and strict positivity of \(C(y)\), together with the positive gap from the strict minimum outside a small neighborhood, justify domination and the stated \(1+o(1)\) ratios in every case. The flat formula follows directly from the exact mixture.

**4. Conditional age laws.** For a regular conditional distribution at the spatial point \(te\), Bayes' density is proportional to \(\alpha y^{\alpha-1}h(y)e^{-t^2f(y)/2}\). The same variable changes give the following limits, with all rates and curvatures evaluated at the stated minimizer: old regular, \(t^2Y\) tends to a Gamma law of shape \(\alpha\) and rate \(d_0/2\); old tangent, \(tY\) has limiting density proportional to \(z^{\alpha-1}e^{-f''(0)z^2/4}\) on \(z>0\); interior, \(t(Y-y_*)\) tends to \(N(0,2/f''(y_*))\); young tangent, \(t(1-Y)\) tends to a half-Gaussian density proportional to \(e^{-f''(1)z^2/4}\) on \(z>0\); young regular, \(t^2(1-Y)\) tends to an exponential law of rate \((-d_1)/2\). In the flat case, the conditional density of \(Y\) is independent of \(t\), proportional to \(\alpha y^{\alpha-1}h(y)\). These are weak limits of the conditional age laws, not statements about a point-conditioning event having positive probability.

**5. A strict interior-age witness.** In two dimensions take \(Q=I_2\), \(S=\operatorname{diag}(4,1/4)\), and \(e=(1,1)/\sqrt2\). Direct inversion gives
\[
f(y)=\frac1{2(1+3y)}+\frac1{2(1-3y/4)},\quad
f'(0)=-\frac98<0,\quad f'(1)=\frac{189}{32}>0.
\]
Solving \(f'(y)=0\) gives \(y_*=2/9\) and \(f(y_*)=9/10\), while \(f(0)=1\) and \(f(1)=17/8\). Thus, for \(\alpha>0\), the joint point density has strictly slower Gaussian decay than either endpoint conditional density along this ray; its dominant elapsed age is \(A_*=(2\kappa)^{-1}\log(9/2)\). Yet the projected scalar \(e^{\mathsf T}X\mid Y=y\) has variance \(e^{\mathsf T}C(y)e\), an affine function of \(y\), so the marginal projection's maximal Gaussian variance always occurs at an endpoint. This exhibits a genuine joint-versus-projected rare-event distinction.

## Verification

A standalone deterministic numerical checker is provided as `verify_tail.py` with reproducibility dependencies in `requirements.txt`. It constructs the exact Gaussian mixture independently from the Laplace endpoint formula, integrates the scaled density in each of the five nonflat regimes, checks derivative identities by central differences, verifies the exact rational interior witness, and checks the exact flat exception. Its execution passed 130 finite assertions; for the five nonflat regimes the ratio of quadrature to predicted asymptotic value at \(t=50\) was approximately \(0.995663\), \(1.020449\), \(0.999333\), \(1.011928\), and \(0.987391\), in table order. These finite tests do not establish the asymptotic theorem; the proof above does.

## Relationship to prior work

Olsen, *Steady-state moments under resetting to a distribution*, first posted 2023-10-07 (arXiv:2310.04840), derives the renewal framework and explicit all-order stationary moments for one-dimensional harmonic Brownian and run-and-tumble processes under arbitrary reset-location laws. The renewal mixture is prior work, not the novelty claimed here. In the full eight-page 2023 article, the main calculations address moments, variance, skewness and resetting distribution width, not the directional multivariate ray-tail minimization or its five local asymptotic regimes.

Trajanovski and collaborators, *Ornstein-Uhlenbeck process and generalizations: Particle dynamics under comb constraints and stochastic resetting* (Phys. Rev. E 107, 054129, 2023), analyze Ornstein–Uhlenbeck dynamics with fixed-point and geometry-constrained resetting, not the covariance-segment anisotropic Gaussian reset mechanism. The later paper *Resetting in a viscoelastic bath: the bath remembers* (2026) gives a related Gaussian mixture with its maximum variance at a scalar long-time endpoint; it does not provide the nonmonotone matrix-inverse optimization for multivariate **point density**. Generic Laplace asymptotics and matrix differentiation are standard tools and are not claimed independently as new.

## Limitations

The result concerns the **joint stationary point density along a fixed ray**, not the tail of the scalar projection or the probability of a spherical-shell event. The drift must be a scalar harmonic relaxation, and thermal diffusion and Gaussian reset-location covariances must be strictly positive definite; neither arbitrary drift matrices nor non-Gaussian resets are covered. Ray direction and all model parameters are fixed before taking \(t\to\infty\), so uniformity across critical angular boundaries is not asserted. Full novelty against every unindexed Gaussian-mixture asymptotic reference has not been independently established. The numerical checker is diagnostic, not an infinite-domain certificate.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first posted 2023-10-07); *Physical Review E* 108, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120.
2. P. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: Particle dynamics under comb constraints and stochastic resetting*, *Physical Review E* 107, 054129 (2023), https://doi.org/10.1103/PhysRevE.107.054129.
3. *Resetting in a viscoelastic bath: the bath remembers*, *New Journal of Physics* (2026), https://doi.org/10.1088/1367-2630/ae868c. Included for the related one-dimensional covariance-mixture comparison, not as the first public source motivating the question.
