# Convex-order concentration bias and a sharp boundary-layer law for least-squares Poisson mixtures

## Finding

Let \(P_r(\theta)=(1-r^2)/(1-2r\cos\theta+r^2)\) be the circle Poisson kernel, normalized to have mean one. Let \(\mu\) be any probability measure supported in \([0,R]\), where \(R<1\), and put \(M_\mu=\int P_x\,d\mu(x)\). Suppose its mean \(m=\int x\,d\mu(x)\) is positive. In the class of **single concentric kernels** \(P_t\), \(0\le t<1\), the squared boundary \(L^2(d\theta/(2\pi))\) approximation error

\[
\mathcal E_\mu(t)=\int_0^{2\pi}|M_\mu(\theta)-P_t(\theta)|^2\frac{d\theta}{2\pi}
\]

has exactly one minimizer \(t_\mu\). Its defining equation is

\[
\frac{t_\mu}{(1-t_\mu^2)^2}
 =\int\frac{x}{(1-t_\mu x)^2}\,d\mu(x).
\tag{1}
\]

For every non-point-mass \(\mu\) with \(m>0\), the best-fit radius obeys the **strict concentration bias**

\[
 m<t_\mu<\sup\operatorname{supp}\mu.
\tag{2}
\]

Furthermore, if \(\mu_1\preceq_{\mathrm{cx}}\mu_2\) in convex order and both have the same positive mean, then \(t_{\mu_1}\le t_{\mu_2}\), with strict inequality if their laws differ. Thus a mean-preserving spread of Poisson source radii strictly increases the radius of their best single-kernel fit.

For a bounded centered random variable \(Y\), a fixed \(0<m<1\), and sufficiently small real \(\delta\) so \(X_\delta=m+\delta Y\in[0,1)\), the local quantitative law is

\[
 t_{\mathcal L(X_\delta)}=m+\frac{m(2+m^2)}{(1-m^2)(1+m^2)}\operatorname{Var}(Y)\,\delta^2+O_{m,Y}(|\delta|^3).
\tag{3}
\]

A distinct singular limit holds when the sources approach the circle. Fix \(0<a\le b<\infty\), and let \(A\) have any probability law \(\nu\) supported in \([a,b]\). For \(0<\varepsilon<1/b\), define \(X_\varepsilon=1-\varepsilon A\) and its best-fit radius \(t_\varepsilon\). There is a unique \(\tau_\nu>0\) solving

\[
 4\tau_\nu^2\int\frac{d\nu(A)}{(\tau_\nu+A)^2}=1.
\tag{4}
\]

Then, as \(\varepsilon\downarrow0\),

\[
 t_\varepsilon=1-\varepsilon\tau_\nu+O_\nu(\varepsilon^2),
\qquad
\min_t\mathcal E_{\mathcal L(X_\varepsilon)}(t)
 =\frac{\mathscr C_\nu}{\varepsilon}+O_\nu(1),
\tag{5}
\]

where, for independent \(A,A'\) with law \(\nu\),

\[
\mathscr C_\nu=\frac1{\tau_\nu}-4\mathbb E\frac1{\tau_\nu+A}
+2\mathbb E\frac1{A+A'}
=2\int_0^\infty\!\left(e^{-\tau_\nu u}-\mathbb E e^{-Au}\right)^2du.
\tag{6}
\]

The constant \(\mathscr C_\nu\) is strictly positive exactly when \(\nu\) is not a point mass; otherwise it vanishes and the fit is exact. For nondegenerate \(\nu\), \(\inf\operatorname{supp}\nu<\tau_\nu<\mathbb EA\). This is an explicit sharp boundary concentration law with a nonzero leading approximation error for heterogeneous source depths.

## Assumptions and scope

All measures are Borel probabilities and all mixing radii are nonnegative and strictly less than one. All component Poisson kernels are centered at the **same boundary direction**, set to angle zero by rotation. The optimization varies only the radial parameter of the approximating kernel, not its center, amplitude, or class of general probability densities. In (3), the distribution of \(Y\) is fixed, bounded, and centered. In (4)–(6), \(\nu\) is fixed and has depths uniformly separated from zero and infinity; constants in remainders depend on this law. For a mass concentrated at radius zero, the unique optimum is \(t=0\), an endpoint case excluded from the positive-mean formulations.

## Proof

**1. Exact Fourier objective.** The uniformly and absolutely convergent expansion \(P_x=1+2\sum_{k\ge1}x^k\cos(k\theta)\), valid uniformly for \(x\le R<1\), gives by Parseval

\[
\mathcal E_\mu(t)=2\sum_{k=1}^\infty\bigl(t^k-\mathbb E X^k\bigr)^2
=2\left(\frac{t^2}{1-t^2}-2\mathbb E\frac{tX}{1-tX}
+\mathbb E\frac{XX'}{1-XX'}\right),
\tag{7}
\]

with \(X,X'\) independent with law \(\mu\). This equality also proves that \(\mathcal E_\mu(t)\to\infty\) as \(t\uparrow1\). Termwise differentiation on compact subintervals yields

\[
\mathcal E'_\mu(t)=4\left[\frac{t}{(1-t^2)^2}-\mathbb E\frac X{(1-tX)^2}\right].
\tag{8}
\]

**2. Existence and global uniqueness.** For \(0<t<1\), factor the right side of (8) as \(4t(1-H_\mu(t))/(1-t^2)^2\), where

\[
H_\mu(t)=\mathbb E h_X(t),\quad h_x(t)=\frac{x(1-t^2)^2}{t(1-tx)^2}.
\]

For \(x>0\), logarithmic differentiation gives

\[
\frac{d}{dt}\log h_x(t)
=\frac{xt(3+t^2)-(1+3t^2)}{t(1-t^2)(1-tx)}<0,
\]

because \(0<x\le1\) makes the numerator at most \(-(1-t)^3\). The case \(x=0\) contributes zero. Since \(\mathbb E X=m>0\), \(H_\mu\) is strictly decreasing, \(H_\mu(0+)=\infty\), and \(H_\mu(1-)=0\). Therefore (8) changes sign exactly once, from negative to positive. This proves that its unique root is the unique global minimizer, proving (1).

**3. Concentration and convex order.** For fixed \(0<t<1\), the function \(g_t(x)=x/(1-tx)^2\) has

\[
 g_t''(x)=\frac{2t(2+tx)}{(1-tx)^4}>0.
\tag{9}
\]

Jensen applied at \(t=m\) yields \(\mathbb E g_m(X)>g_m(m)=m/(1-m^2)^2\) for non-point-mass \(\mu\), so (8) is negative there and \(t_\mu>m\). At the upper endpoint \(b=\sup\operatorname{supp}\mu\), pointwise monotonicity of \(g_b\) makes \(\mathbb E g_b(X)<g_b(b)\) for nondegenerate \(\mu\), so \(t_\mu<b\). The same strict convexity in (9) implies \(\mathbb E_{\mu_1}g_t\le\mathbb E_{\mu_2}g_t\) whenever \(\mu_1\preceq_{\mathrm{cx}}\mu_2\); strictness for distinct laws follows from a nontrivial martingale coupling and strict conditional Jensen. Thus \(H_{\mu_1}(t)\le H_{\mu_2}(t)\), strictly for \(t>0\) if the laws differ. Comparing their unique level-one crossings gives the claimed order of the best-fit radii.

**4. Small variance.** Put \(F(t,\delta)=t/(1-t^2)^2-\mathbb E g_t(m+\delta Y)\). At \((m,0)\), \(F=0\) and

\[
\partial_tF(m,0)=\frac{1+m^2}{(1-m^2)^3}>0,
\qquad
\partial_{\delta\delta}F(m,0)
=-\frac{2m(2+m^2)}{(1-m^2)^4}\operatorname{Var}(Y).
\]

The first \(\delta\)-derivative vanishes by centering. Uniform Taylor expansion and the implicit-function theorem, justified by bounded \(Y\), give (3) and its third-order remainder.

**5. Boundary layer and sharp risk.** Write \(x=1-\varepsilon A\), \(t_\varepsilon=1-\varepsilon\tau_\varepsilon\). The general endpoint bounds from step 3 place \(\tau_\varepsilon\in[a,b]\). Multiply (1) by \(\varepsilon^2\). Uniformly on this compact interval, the resulting equation tends to

\[
 \frac1{4\tau^2}=\mathbb E\frac1{(\tau+A)^2}.
\]

The function \(4\tau^2\mathbb E(\tau+A)^{-2}\) is strictly increasing from zero to four, because each \(\tau/(\tau+A)\) strictly increases; it has exactly one level-one root. The limiting equation has a nonzero derivative, so a uniform implicit-function expansion implies \(\tau_\varepsilon=\tau_\nu+O_\nu(\varepsilon)\). Strict Jensen of the convex map \(A\mapsto(\tau+A)^{-2}\) at \(\tau=\mathbb EA\), and the trivial lower-depth bound at \(\tau=a\), show the stated strict interval. Substituting the uniform first-order expansions of the denominators in the exact rational formula (7) yields (5)–(6). Finally, the identity on the right of (6) follows by expanding the square and integrating the three exponential terms. Its vanishing implies equality of the Laplace transforms of \(\delta_{\tau_\nu}\) and \(\nu\) on the positive axis; uniqueness of Laplace transforms for compactly supported probabilities forces \(\nu\) to be a point mass. Conversely a point mass is fitted exactly. This completes the proof.

## Verification

The standalone `checker.py` uses bisection of the exact stationarity equation and the closed rational Parseval error (7). It checks global-optimum comparisons, strict overconcentration, convex-order examples, the quadratic variance coefficient, and the boundary scale and risk for two-component depth mixtures. It has no nonstandard dependencies. Execute `python3 checker.py`; on the supplied deterministic test set it reports 91 passed finite assertions. These finite checks are diagnostic only; all continuous-support and asymptotic claims follow from the proof above.

For equal masses at depths \(A=1\) and \(A=3\), solving (4) gives \(\tau_\nu\approx1.60113594287112\) (strictly below the average depth two) and \(\mathscr C_\nu\approx0.00431981402803\). Hence the minimal unnormalized squared approximation error diverges as this positive constant divided by \(\varepsilon\) in the common-boundary limit.

## Relationship to prior work

Bailey's 2019 thesis, Appendix C2, equations (6.10) and (6.12), already derives the Fourier least-squares objective and its formal stationary condition for a **two-component** wrapped-Cauchy mixture, and compares that fit numerically with a wrapped-normal family. Those equations, and their immediate rescaling to Poisson kernels, are **not** claimed as original. The contribution here is the global uniqueness theorem for arbitrary compactly supported mixing measures, the strict comparative-static theorem in convex order, the universal quadratic small-spread coefficient, and the sharp singular boundary-depth limit with its optimal residual constant. These claims require extra arguments absent from the cited appendix's numerical mixture-family comparison.

Bailey and Codling's 2020 deposited manuscript studies different questions of which fitted circular family best explains mixtures of wrapped normal components. Tsagris and Alzeley's 2023 preprint supplies a separate modern directional-data motivation but does not address this one-dimensional Fourier-projection geometry. Published results on curvature transitions for centered mixtures of circular Poisson semigroups concern inflection points rather than optimal single-kernel \(L^2\) projections.

## Limitations

This is a self-review; independent mathematical audit and exhaustive historical priority certification have not been performed. The chosen statistic is boundary squared \(L^2\), not likelihood, total variation, or KL divergence. All component kernels have a common angular center, and mixing laws are nonnegative probabilities supported away from radius one for the fixed-mixture theorem. The near-boundary law presumes a **fixed** compactly supported positive depth distribution and does not cover depth distributions varying with \(\varepsilon\), signed mixtures, or unconstrained re-optimization of the kernel's angular center. The previously known two-component loss formula remains explicitly credited. The thesis could have other unexamined relevant sections and older literature may contain equivalent convex-order or near-boundary statements.

## References

- J. D. Bailey, *Modelling and Analysis of Individual Animal Movement*, University of Essex doctoral thesis, December 2019, deposited 8 January 2020, Appendix C2, equations (6.9)–(6.14), https://repository.essex.ac.uk/26383/1/Thesis_2%281%29.pdf .
- J. D. Bailey and E. A. Codling, *Emergence of the wrapped Cauchy distribution in mixed directional data*, originally deposited 9 October 2020, https://repository.essex.ac.uk/28875/ .
- M. Tsagris and O. Alzeley, *Circular and spherical projected Cauchy distributions*, arXiv:2302.02468, first version 5 February 2023, https://arxiv.org/abs/2302.02468 .
