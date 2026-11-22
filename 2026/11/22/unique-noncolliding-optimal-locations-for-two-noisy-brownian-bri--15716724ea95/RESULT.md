# Unique noncolliding optimal locations for two noisy Brownian-bridge quadrature observations

## Finding
Let \(B\) be the standard centered Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\), and let \(J=\int_0^1 B(t)\,dt\). For an arbitrary deterministic ordered pair \((x,y)\in[0,1]^2\), take two readings \(Y_1=B(x)+\varepsilon_1\), \(Y_2=B(y)+\varepsilon_2\), with independent \(\varepsilon_i\sim N(0,\eta)\) also independent of \(B\), where \(\eta>0\). Repeated observation locations are allowed, but the observation noises are still independent.

Among **all** such pairs, the conditional-mean estimator \(\widehat J=\mathbb E[J\mid Y_1,Y_2]\) uniquely minimizes the posterior mean-square error (equivalently, the posterior variance) at the unordered pair
\[
\left\{x_\eta,y_\eta\right\}=\left\{\frac{1-d_\eta}{2},\frac{1+d_\eta}{2}\right\},\qquad
 d_\eta=\frac{2+4\eta-\sqrt{16\eta^2+16\eta+1}}{3}\in(0,1/3).
\]
Its exact minimum posterior variance and the optimal information gain are
\[
 V_\eta^{\min}=\frac1{12}-\frac{d_\eta(1-d_\eta^2)}4,
\qquad \operatorname{Var}(J)-V_\eta^{\min}=\frac{d_\eta(1-d_\eta^2)}4.
\]
The gap \(d_\eta\) decreases strictly from \(1/3\) as \(\eta\downarrow0\) to zero as \(\eta\to\infty\), with \(d_\eta\sim1/(8\eta)\) at high noise. Thus **two noisy measurements should never be exactly collocated at any finite positive noise variance**, even though their optimal locations approach the midpoint as noise grows.

## Assumptions and scope
All observations and the target integral are jointly Gaussian. Locations are chosen in advance, not adapted to readings, and every admissible pair has the same count and independent additive Gaussian noise variance \(\eta>0\). The objective is \(\operatorname{Var}(J\mid Y_1,Y_2)\), which does not depend on the observed numerical values. The estimator may use the two optimal (noise-calibrated) Gaussian conditional-mean weights; weights are not forced to be equal or to sum to one. No claim is made for non-Gaussian priors, correlated observation noise, unequal noise costs or general sample counts. The same value is the minimum of the regularized kernel-quadrature criterion \(\min_w\{\|k_J-\sum_i w_i K(\cdot,t_i)\|_{H_0^1}^2+\eta\sum_iw_i^2\}\) over both weights and locations.

## Proof
**1. Gaussian reduction.** The bridge covariance gives \(\operatorname{Var}(J)=1/12\) and \(k(t):=\operatorname{Cov}(J,B(t))=t(1-t)/2\). For \(0\le x\le y\le1\) define
\[
 M=\begin{pmatrix}x(1-x)+\eta&x(1-y)\\x(1-y)&y(1-y)+\eta\end{pmatrix},\quad
 v=\begin{pmatrix}k(x)\\k(y)\end{pmatrix},\quad R(x,y)=v^{\mathsf T}M^{-1}v.
\]
For positive \(\eta\), \(M\) is positive definite even if \(x=y\). The conditional variance is \(1/12-R(x,y)\), so it suffices to maximize \(R\). By reflection and swapping, write \(d=y-x\in[0,1]\) and \(u=x+y-1\in[-(1-d),1-d]\), with \(x=(1+u-d)/2\), \(y=(1+u+d)/2\). Denote the corresponding function by \(R_\eta(u,d)\).

**2. No asymmetric interior maximizer.** Direct differentiation and cancellation of the positive Gram determinant yield
\[
 \frac{\partial R_\eta}{\partial u}=
 \frac{u\,[d(1-d)+2\eta]\,[(1-d)^2-u^2+4\eta]\,F_\eta(u,d)}{128\,\det(M)^2},
\quad
 F_\eta(u,d)=d[u^2-(1-d)^2]+2\eta[3d^2+u^2-1].
\]
For any fixed \(d\), the factors preceding \(F_\eta\) are positive when \(u>0\). The function \(F_\eta(u,d)\) is **strictly increasing in \(u^2\)**, since its coefficient is \(d+2\eta>0\). Hence as \(u\) runs from zero to \(1-d\), the sign of the derivative may only go from negative to positive, never positive to negative. There can therefore be no strict interior maximum for positive \(u\). By symmetry, for every fixed \(d\) the largest value occurs at \(u=0\) or \(u=\pm(1-d)\). This covers the edges and repeated-location case as well.

**3. Exclude interval endpoints.** At \(|u|=1-d\), at least one observation is at zero or one and contains only observation noise. The other location \(t\) has information gain
\[
 \frac{k(t)^2}{K(t,t)+\eta}=
 \frac{[t(1-t)]^2}{4[t(1-t)+\eta]}
 \le\frac{1}{16(1+4\eta)}.
\]
The inequality follows since \(s^2/(s+\eta)\) strictly increases for \(s\ge0\), while \(s=t(1-t)\le1/4\). By contrast, two independent readings at the midpoint give
\[
 R_\eta(0,0)=\frac{1}{16(1+2\eta)}>\frac{1}{16(1+4\eta)}.
\]
Thus no endpoint-containing design can be optimal. Every global maximizer must belong to the centered family \(u=0\).

**4. Unique centered optimum.** A direct inversion now gives
\[
 R_\eta(0,d)=\frac{(1-d^2)^2}{16(1+2\eta-d)},\quad
 \frac{\partial R_\eta(0,d)}{\partial d}
 =\frac{(1-d^2)[3d^2-(4+8\eta)d+1]}{16(1+2\eta-d)^2}.
\]
The quadratic factor starts positive at zero, is negative at one, and has precisely one root in \((0,1)\); the root is the stated \(d_\eta\) and lies in \((0,1/3)\). This gives the unique global centered maximizer \(d=d_\eta\). Its stationarity equation is \(8\eta d_\eta=(1-d_\eta)(1-3d_\eta)\), so \(1+2\eta-d_\eta=(1-d_\eta^2)/(4d_\eta)\). Substitution produces \(R_\eta(0,d_\eta)=d_\eta(1-d_\eta^2)/4\), establishing the exact risk and uniqueness up to swapping.

**5. Noise dependence.** The equation \(8\eta=(1-d)(1-3d)/d=1/d-4+3d\) is strictly decreasing in \(d\in(0,1/3)\), since its derivative is \(-1/d^2+3<0\). It therefore gives strictly decreasing optimal separation with increasing noise. It also immediately yields \(d_\eta\to1/3\) at vanishing noise and \(d_\eta\sim1/(8\eta)\) at high noise. The nodes remain distinct for every finite \(\eta>0\).

## Verification
The standalone `verify.py` uses exact SymPy simplification to check the Gaussian inversion formula, the full asymmetry derivative factorization, the centered reduction, the derivative of the centered objective, and the optimal-risk identity. It independently evaluates 765 ordered rational-location pairs across five strictly positive rational noise levels and compares each gain with the exact symbolic optimum at 60-digit precision. All checks passed in the included `checks.txt`. These finite diagnostics are not used as a proof of optimality on the continuum: Steps 1–5 supply that proof. Run from the package directory with `python verify.py` and SymPy installed.

## Relationship to prior work
Santin (2022, arXiv:2210.15959v1) derives equally spaced nodes for a **noiseless** Brownian-bridge interpolation **supremum power-function** criterion; its positive parameter changes the differential operator defining the kernel and is not independent measurement-noise variance. It does not imply the present noise-dependent integral-risk optimum. Briol and collaborators (2017, arXiv:1706.03369v1) study the law of random nodes in kernel quadrature, not these deterministic, optimally noise-calibrated two sites. Cai, Lam and Scarlett (2022, arXiv:2202.10615v1) develop noisy-kernel-quadrature complexity bounds, rather than an exact two-point Brownian-bridge design. Karvonen, Kanagawa and Särkkä (2019, DOI:10.1007/s11222-019-09901-0) analyze positivity and bounds of kernel quadrature weights and general local optimality, but do not derive this location theorem. Ji and Müller (arXiv:1604.05375v1) formulate general noisy longitudinal and scalar-response designs, including integration-based responses, without the explicit Brownian-bridge two-node global classification. A published related Brownian-bridge result determines the **i.i.d. random-node sampling law** for noiseless quadrature, a different admissible class and objective; see its distinct theorem at the identifier listed in the prior-work comparison in the structured review.

## Limitations
Only two independent equal-variance Gaussian-noisy readings, known bridge covariance, a single integral target, and nonadaptive deterministic sites are covered. No asymptotic optimality in general node count, other kernels, or computational acceleration is claimed. Exact scholarly publication priority is not independently verified; a specialized classical optimal-design theorem expressed through an equivalent Gaussian response or spline regularization could still subsume the claim.

## References
1. G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959v1, first public 2022-10-28; Sections 2 and 4.2, Theorem 5, https://arxiv.org/abs/2210.15959.
2. F.-X. Briol, C. J. Oates, J. Cockayne, W. Y. Chen and M. Girolami, *On the Sampling Problem for Kernel Quadrature*, arXiv:1706.03369v1, first public 2017-06-11, Sections 1–3, https://arxiv.org/abs/1706.03369.
3. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1, first public 2022-02-22, Sections 1–3, https://arxiv.org/abs/2202.10615.
4. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing 29 (2019), https://doi.org/10.1007/s11222-019-09901-0.
5. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1, first public 2016-04-18, Sections 1–3, https://arxiv.org/abs/1604.05375.
6. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4 (different noiseless random-node theorem).
