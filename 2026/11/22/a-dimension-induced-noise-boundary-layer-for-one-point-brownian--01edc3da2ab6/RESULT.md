# A dimension-induced noise boundary layer for one-point Brownian-sheet quadrature

## Finding

**Theorem.** Let \(d\ge2\) be an integer, \(W_d\) the centered \(d\)-parameter Brownian sheet on \([0,1]^d\) with covariance
\[
K_d(s,t)=\prod_{j=1}^d\min(s_j,t_j),
\]
and \(J_d=\int_{[0,1]^d}W_d(t)\,dt\). An observer selects one deterministic point \(x\in[0,1]^d\), sees \(Y_x=W_d(x)+\epsilon\), where \(\epsilon\sim N(0,\eta)\) independently for a specified finite \(\eta\ge0\), and estimates \(J_d\) under squared error. Every measurable estimator is allowed.

For each \(d\ge2\) and finite \(\eta\ge0\), the **unique globally Bayes-optimal observation site** is
\[
x^*=(r_d(\eta),\ldots,r_d(\eta)).
\]
At \(\eta=0\), \(r_d(0)=2/3\). For \(\eta>0\), \(r_d(\eta)\in(2/3,1)\) is the unique solution of
\[
 r^d(3r-2)=4\eta(1-r).
\]
For positive noise it increases strictly in both \(\eta\) and integer \(d\), while always remaining strictly below \(1\). Define the variance captured by the best estimator as \(I_d^*(\eta)=3^{-d}-R_d^*(\eta)\). Then
\[
I_d^*(\eta)=\frac{[r_d(\eta)(1-r_d(\eta)/2)]^{2d}}{r_d(\eta)^d+\eta}.
\]
Its zero-noise explained-variance fraction is exactly \((8/9)^d\). For each **fixed** \(\eta>0\), writing \(W_0\) for the principal Lambert function,
\[
1-r_d(\eta)=\frac{W_0(d/(4\eta))}{d}+O_\eta\!\left(\frac{(\log d)^2}{d^2}\right),
\qquad
\frac{I_d^*(\eta)}{3^{-d}}\sim\frac1\eta\left(\frac34\right)^d
\quad(d\to\infty).
\]
There is a resolved small-noise/dimension crossover: for each fixed \(c\ge0\) and \(\eta_d=c(2/3)^d/d\), put \(y(c)=\frac23 W_0(2c/3)\). Then
\[
d\left(r_d(\eta_d)-\frac23\right)\longrightarrow y(c)
\]
and, more sharply,
\[
\log\frac{I_d^*(\eta_d)}{(8/27)^d}
=-\frac1d\left[\frac{27}{16}y(c)^2+c e^{-3y(c)/2}\right]+o(d^{-1}).
\]
All limits concern integer \(d\to\infty\), with the specified noise scaling. These are exact one-observation results, not statements about multiple-node or adaptive cubature.

## Assumptions and scope

The Brownian sheet is a jointly Gaussian, centered field with the displayed product covariance; the target is its Lebesgue integral over the unit cube. Gaussian independent observation noise has an absolute variance \(\eta\) that does not depend on the chosen site. The site is selected before observing data, and the covariance/noise parameters are known. For \(\eta=0\) and a site with a zero coordinate, the observation is identically zero; its captured variance is defined as zero. Gaussian conditioning gives a posterior-mean estimator, optimal over all measurable functions of the one observed scalar.

## Proof

1. **Exact posterior risk.** Tensor integration of the covariance gives
\[
 \operatorname{Var}J_d=3^{-d},\qquad
 \operatorname{Cov}(J_d,W_d(x))=\prod_{j=1}^d a(x_j),\qquad
 \operatorname{Var}Y_x=\prod_{j=1}^dx_j+\eta,
 \quad a(u)=u-u^2/2.
\]
For nondegenerate observations, conditional Gaussian regression yields
\[
 \widehat J_x=\frac{\prod_j a(x_j)}{\prod_jx_j+\eta}\,Y_x,
 \qquad
 R_d(x;\eta)=3^{-d}-F_d(x;\eta),
 \qquad
 F_d(x;\eta)=\frac{\prod_ja(x_j)^2}{\prod_jx_j+\eta}.
\]
The continuous extension sets \(F_d=0\) at any coordinate hyperface \(x_j=0\), including when \(\eta=0\); indeed \(a(u)^2\le u^2\), so \(F_d\le\prod_jx_j\) at zero noise. Thus a maximum exists and is positive. If \(x_i=1\), the one-sided inward variation improves \(F_d\), because the logarithmic derivative from the interior is \(-\frac{\prod_jx_j}{\prod_jx_j+\eta}<0\). Every maximizer is consequently interior.

2. **Symmetry and uniqueness without assuming it.** Put \(v=\prod_jx_j\). At every interior stationary point,
\[
 x_i\partial_{x_i}\log F_d
 =\frac{4(1-x_i)}{2-x_i}-\frac{v}{v+\eta}=0.
\]
The first term is strictly decreasing in \(x_i\) (derivative \(-4/(2-x_i)^2\)); hence all coordinates at any stationary point coincide, without a symmetry restriction on competitors. With \(x_i=r\), stationarity becomes
\[
 r^d(3r-2)=4\eta(1-r).
\]
For \(\eta>0\), necessarily \(2/3<r<1\). The function \(r\mapsto r^d(3r-2)/(1-r)\) is strictly increasing from zero to infinity there, giving exactly one stationary point and therefore exactly one global optimum. At \(\eta=0\), \(r=2/3\) is its only positive interior stationary solution. The same monotone function shows increase in \(\eta\); at any fixed \(r<1\), its value decreases as integer \(d\) grows, forcing the solution to increase with dimension.

3. **Fixed positive-noise high-dimensional limit.** Write \(s_d=1-r_d(\eta)\) and \(t_d=ds_d\). The defining equation becomes
\[
 (1-s_d)^d(1-3s_d)=4\eta s_d.
\]
For fixed \(\eta>0\), it forces \(s_d\to0\). From \((1-s_d)^d\le e^{-ds_d}\) and \(1-3s_d\le1\),
\[
 t_d e^{t_d}\le\frac{d}{4\eta},
\]
so \(t_d=O_\eta(\log d)\). Taking logarithms of the defining equation and expanding uniformly at \(t_d/d\to0\) gives
\[
 t_d+\log t_d=\log\frac d{4\eta}
 +O_\eta\left(\frac{(\log d)^2}{d}\right).
\]
The function \(t+\log t\) has derivative at least one; its exact reference solution is \(W_0(d/(4\eta))\). This establishes the stated expansion for \(r_d\). Moreover
\[
 I_d^*(\eta)=\frac{4^{-d}(1-s_d^2)^{2d}}{(1-s_d)^d+\eta}.
\]
Because \(ds_d^2\to0\) and \((1-s_d)^d=4\eta s_d/(1-3s_d)\to0\), the latter is asymptotic to \(4^{-d}/\eta\). Dividing by \(3^{-d}\) proves the explained-variance fraction.

4. **Exponential-noise crossover.** Set \(\eta_d=c(2/3)^d/d\) with fixed \(c\ge0\). For \(c>0\), let \(y_d=d(r_d(\eta_d)-2/3)\ge0\). Rewriting stationarity gives
\[
 c=\frac{3y_d}{4(1/3-y_d/d)}\left(1+\frac{3y_d}{2d}\right)^d.
\]
For fixed nonnegative \(y\), the right-hand side tends strictly increasingly to \(\frac94 y e^{3y/2}\). Monotonicity and comparison at two fixed bounding values force \(y_d\to y(c)\), the unique solution \(y e^{3y/2}=4c/9\). This is \(y(c)=2W_0(2c/3)/3\). For \(c=0\), \(y_d=0\) identically.

Finally use \(h(r)=r(1-r/2)^2\), for which \(h(2/3)=8/27\), \(h'(2/3)=0\), and \((\log h)''(2/3)=-27/8\). The identity
\[
 I_d^*(\eta_d)=\frac{h(r_d)^d}{1+\eta_d/r_d^d}
\]
and \(y_d\to y(c)\) give
\[
 d\left[\log h(r_d)-\log h(2/3)\right]
 =-\frac{27}{16}\frac{y(c)^2}{d}+o(d^{-1}),
 \qquad
 \log(1+\eta_d/r_d^d)
 =\frac{c e^{-3y(c)/2}}d+o(d^{-1}).
\]
Subtraction yields the claimed sharp logarithmic information expansion. \(\square\)

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The script independently integrates the one-dimensional covariance by numerical Simpson quadrature; checks the exact scalar root equation and strict-coordinate first-order conditions; compares optimal designs with random unrestricted site choices; tests the high-dimensional Lambert asymptotic; and checks the crossover coefficient on finite dimensions. The analytic argument, not finite grid checks, proves all-dimensional/global assertions. In particular, experiments neither certify historical originality nor prove asymptotic convergence.

## Relationship to prior work

Pronzato and Zhigljavsky's 2018 preprint, Sections 2, 3.6 and 4, establishes the generic Gaussian-process quadrature/energy framework and tensor kernel-potential factorization. That framework supplies the starting covariance objective but does not state the noisy **unrestricted one-site** optimality classification or its sharp high-dimensional/exponentially-small-noise asymptotics. Karvonen, Kanagawa and Särkkä (2019), Sections 2–3, analyze positive and stable quadrature weights and tensor product rules, not this noise/dimension location optimization. Agram, Øksendal, Proske and Tymoshenko (2024), Sections 2–7, investigate continuous time-space filtering of Brownian-sheet-driven systems, rather than a single offline point sample for an integral. Classical Brownian sheet average-case integration and discrepancy principles are acknowledged, not claimed as new. The noiseless one-dimensional rule and its ordinary noisy one-dimensional generalization are pre-existing special cases and **not** the contribution here. The mathematical contribution asserted is the globally unique unrestricted multidimensional noisy design together with the singular dimension/noise boundary layer and two distinct sharp information-decay exponents.

## Limitations

The result is one observation of a Gaussian Brownian sheet with known product covariance and absolute independent Gaussian noise. It does not characterize multiple or adaptively selected points, heterogeneous or location-dependent noise, arbitrary tensor kernels, the non-Gaussian case, or a growing number of observations. The noise-free and fixed-positive-noise dimensional limits are distinct; interchanging limits is unjustified. Originality comparisons are limited to the sources identified below and related searches, so publication priority is not independently certified.

## References

- L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1, first public 2018-08-31, https://arxiv.org/abs/1808.10722 .
- T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, *Statistics and Computing* 29 (2019), https://doi.org/10.1007/s11222-019-09901-0 .
- N. Agram, B. Øksendal, F. Proske and O. Tymoshenko, *A Kalman filter for linear systems driven by time-space Brownian sheet*, arXiv:2407.06386v1, 2024-07-08, https://arxiv.org/abs/2407.06386 .
- H. Kempka, C. Schneider and J. Vybiral, *Path Regularity of the Brownian Motion and the Brownian Sheet*, *Constructive Approximation*, published online 2023-04-19, https://doi.org/10.1007/s00365-023-09647-z .
