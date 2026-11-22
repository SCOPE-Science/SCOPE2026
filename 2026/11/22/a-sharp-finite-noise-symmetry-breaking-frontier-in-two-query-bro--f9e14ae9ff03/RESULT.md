# A sharp finite-noise symmetry-breaking frontier in two-query Brownian-bridge quadrature

## Finding

Let \(B\) be a standard centered Brownian bridge on \([0,1]\), and let \(J=\int_0^1 B(t)\,dt\). Choose any two deterministic observation locations, including coincident locations or endpoints, and observe the bridge with centered Gaussian measurement errors of common variance \(\eta>0\) and nonnegative correlation \(0\le\rho<1\). The complete globally optimal two-query design has exactly two possible geometries: a distinct symmetric interior pair or one endpoint used only to estimate the other observation's correlated error.

Put
\[
 A=4+8\eta(1+\rho),\qquad
 w=\frac{2}{A+\sqrt{A^2-12}},\qquad
 G_S=\frac{w-w^3}{4},\qquad
 G_E=\frac{1}{16[1+4\eta(1-\rho^2)]}.
\]
The minimum Bayes squared error (the conditional variance) over every ordered site pair is exactly
\[
 R_*(\eta,\rho)=\frac1{12}-\max\{G_S,G_E\}.
\]
If \(G_S>G_E\), the only optimal site pair up to label exchange is \(\{(1-w)/2,(1+w)/2\}\). If \(G_E>G_S\), the only optimal site pairs up to label exchange are \(\{0,1/2\}\) and \(\{1/2,1\}\). At equality these three pairs, and no others, are optimal.

There is a unique \(w_c\in(0,1/3)\) satisfying \(4w_c(1-w_c^2)=1\), and define
\[
 \eta_c=\frac{1-4w_c+3w_c^2}{16w_c}=0.0323786667908285\ldots.
\]
For every \(0<\eta\le\eta_c\), the symmetric pair is uniquely optimal up to swapping for all \(0\le\rho<1\). For each \(\eta>\eta_c\), there is exactly one \(\rho_c(\eta)\in(1/2,1)\), characterized uniquely by \(G_S=G_E\), with the symmetric pair optimal below this critical correlation and an endpoint reference optimal above it. The critical correlation tends to \(1\) as \(\eta\downarrow\eta_c\), and to \(1/2\) as \(\eta\to\infty\). The change in optimal site placement is discontinuous, with a tie of distinct geometries at the transition.

## Assumptions and scope

The covariance kernel is \(K(s,t)=\min(s,t)-st\); thus \(\operatorname{Var}(J)=1/12\) and \(\operatorname{Cov}(J,B(t))=t(1-t)/2\). Measurement errors are jointly Gaussian, independent of the entire bridge, and have covariance \(\eta\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\). Observation locations are fixed before measurements. The risk is the unconditional squared error of the conditional-mean estimator, equal here to the deterministic posterior variance. The endpoints are allowed because they offer pure-noise measurements that may be useful under correlated errors. No zero-noise or perfectly correlated noise case is asserted.

## Proof

**1. Joint site and coefficient optimization.** By joint Gaussianity, for fixed ordered sites \(0\le a\le b\le1\) the conditional mean is linear in the observations. For any real coefficients \(u,v\), direct covariance calculation gives the exact risk
\[
\begin{aligned}
\mathcal E(a,b;u,v)={}&\frac1{12}-ua(1-a)-vb(1-b)
+u^2a(1-a)+v^2b(1-b)\\
&+2uv\,a(1-b)+\eta(u^2+v^2+2\rho uv).
\end{aligned}
\]
The observation covariance is positive definite because \(\eta>0\) and \(\rho<1\), so the regression coefficients are unique. Its normal equations use right-hand side \((a(1-a)/2,b(1-b)/2)\). Both right-hand sides and all covariance entries are nonnegative. Thus both optimal coefficients cannot be negative. If the optimal coefficients are nonnegative, each is strictly less than \(1/2\) unless it vanishes; this follows by dropping its nonnegative off-diagonal term from the normal equation.

**2. Nonnegative-coefficient branch.** Fix \(0\le u,v<1/2\). As a function of ordered sites, \(\mathcal E\) is convex, with Hessian
\[
 2\begin{pmatrix}u(1-u)&-uv\\-uv&v(1-v)\end{pmatrix}.
\]
For positive \(u,v\) its determinant is \(4uv(1-u-v)>0\). The unique unconstrained minimizer in the site variables is feasible and equals \(a=(1-v)/2\), \(b=(1+u)/2\). Write its value as \(F(u,v)\). Exact expansion yields
\[
 F(u,v)-F\left(\frac{u+v}2,\frac{u+v}2\right)
 =\frac{(u-v)^2}{16}\,[8\eta(1-\rho)+u+v]\ge0,
\]
strictly unless \(u=v\). By continuity, the same lower bound holds on coefficient axes. The diagonal value is
\[
 F(w,w)=\frac1{12}-\frac{w}{2}+w^2-\frac{w^3}{2}+2\eta(1+\rho)w^2.
\]
Its derivative is \([-1+(4+8\eta(1+\rho))w-3w^2]/2\), and its second derivative is positive for \(0\le w\le1/2\). The unique minimizer is the displayed smaller quadratic root \(w\in(0,1/3)\). Substituting the stationary equation gives the minimum \(1/12-(w-w^3)/4\). This branch is attained by the asserted symmetric pair and by no other distinct sites.

**3. Negative-coefficient branch.** Suppose the coefficient of the later site is negative, \(v<0\). For fixed \(a,u,v\), the function \(b\mapsto\mathcal E(a,b;u,v)\) on \([a,1]\) has second derivative \(2v(1-v)<0\), so its minimum lies at \(b=a\) or \(b=1\), strictly better than every interior value. If \(b=a\), both observations have the same bridge signal and the optimal two regression weights are equal and nonnegative (the noise covariance has exchange symmetry); this case is bounded below by the symmetric branch's minimum. If \(b=1\), the second observation equals pure measurement noise. Conditioning on it removes the correlated component of the first observation noise, leaving effective noise variance \(\eta(1-\rho^2)\). The remaining single-site reduction is
\[
 \frac{[a(1-a)/2]^2}{a(1-a)+\eta(1-\rho^2)},
\]
strictly maximized at \(a=1/2\), and equals \(G_E\). When the earlier site's coefficient is negative, the symmetric argument forces \(a=0\) or \(a=b\). These cases exhaust all globally admissible designs and establish the complete geometry and equality cases. A zero optimal coefficient cannot supply an additional optimal design: at \(\rho=0\) the strict two-site improvement beats one observation, and at \(\rho>0\) a correlated endpoint noise reference strictly improves a single observation.

**4. Unique correlation transition.** The smaller root \(w\) decreases strictly with \(\rho\), and \(w-w^3\) increases strictly with \(w\in(0,1/3)\); hence \(G_S\) strictly decreases with \(\rho\). The reference gain \(G_E\) strictly increases for \(\rho>0\). At \(\rho=0\), the symmetric distinct pair strictly beats the endpoint single-observation design. At \(\rho\uparrow1\), the reference gain tends to \(1/16\), while the symmetric gain crosses \(1/16\) exactly when \(w=w_c\), giving the stated \(\eta_c\). Continuity and strict monotonicity give the claimed unique crossing or its absence. At \(\rho=1/2\), the reference gain equals that of two repeated midpoint observations, and the distinct symmetric design strictly improves on that repetition; thus every critical correlation lies strictly above \(1/2\). Elementary large-noise expansions \(G_S\sim[32\eta(1+\rho)]^{-1}\) and \(G_E\sim[64\eta(1-\rho^2)]^{-1}\), uniformly away from \(\rho=1\), imply \(\rho_c(\eta)\to1/2\). The low-noise-boundary limit follows from uniqueness and the strict endpoint inequality for \(\eta<\eta_c\).

## Verification

The companion `verify.py` re-evaluates the multivariate risk polynomial, Hessian, exact symmetrization identity, stationary value and endpoint Schur complement in SymPy; it also tests 20 exact-rational endpoint covariance matrices and 9000 seeded exploratory interior comparisons. It ran successfully on the accompanying code. These finite numerical comparisons are not used as the proof of the global theorem; the concavity/convexity and one-dimensional monotonicity arguments above provide the all-parameter proof.

As numerical reference points, \(w_c=0.2695944364054445\ldots\) and \(\eta_c=0.0323786667908285\ldots\). At \(\eta=0.1\), the critical correlation is \(\rho_c=0.65714824538058\ldots\); its symmetric competitors are at approximately \(0.39328636278\) and \(0.60671363722\). At \(\eta=1\), the critical correlation is \(0.50522804524612\ldots\).

## Relationship to prior work

Karvonen, Kanagawa and Särkkä (2018, arXiv:1812.08509) analyze positivity and magnitudes of Bayesian quadrature weights, principally for noiseless fixed-site kernel quadrature. Attia and Constantinescu (2020, arXiv:2007.14476) provide a general model-constrained experimental-design formulation for correlated observation errors and numerical PDE experiments. Cai, Lam and Scarlett (2022, arXiv:2202.10615) establish noisy kernel-quadrature error bounds, emphasizing rates rather than exact two-site correlated Gaussian design. Santin (2022, arXiv:2210.15959) studies Brownian-bridge kernel *interpolation power functions*, rather than the present integral target with correlation-coupled measurement noise. The exact Gaussian regression covariance identity and the independent-noise symmetric Brownian-bridge integral design are standard/prior input, not new claims. The contribution here is the complete global finite-noise two-geometry classification and its exact noise/correlation bifurcation, including the usefulness of an endpoint that contains no bridge signal.

## Limitations

Only two predetermined observations, a standard Brownian bridge, equal marginal Gaussian noise variance and nonnegative error correlation strictly below one are covered. The precise critical correlation is implicit rather than an elementary explicit radical, though uniquely determined by explicit functions. For correlation exactly one, the observation covariance degenerates and requires a separate analysis. These formulas do not cover negative error correlation, noisy endpoints of a nonpinned process, arbitrary Gaussian kernels, adaptive designs or three or more observations. Historical priority, beyond the accessible sources and checked mathematical records, is not independently certified.

## References

1. Karvonen, T., Kanagawa, M., Särkkä, S., *On the positivity and magnitudes of Bayesian quadrature weights*, first public 2018-12-20, https://arxiv.org/abs/1812.08509.
2. Attia, A., Constantinescu, E., *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations*, first public 2020-07-28, https://arxiv.org/abs/2007.14476.
3. Cai, X., Lam, C. T., Scarlett, J., *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, first public 2022-02-22, https://arxiv.org/abs/2202.10615.
4. Santin, G., *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, first public 2022-10-28, https://arxiv.org/abs/2210.15959.
