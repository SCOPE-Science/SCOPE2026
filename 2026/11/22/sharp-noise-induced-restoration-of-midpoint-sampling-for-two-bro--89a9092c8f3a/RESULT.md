# Sharp noise-induced restoration of midpoint sampling for two Brownian-bridge moments

## Finding

One noisy point sample can be placed optimally to estimate *both* the mean and the first antisymmetric polynomial moment of a Brownian bridge. For the variance-normalized squared-error loss, there is a sharp noise threshold: when \(0\leq\eta<1/2\), exactly two reflected off-midpoint sampling times are optimal; at and above \(\eta=1/2\), the midpoint is the unique optimum. In particular, without noise the two optimal sites are \(\bigl(1\pm1/\sqrt5\bigr)/2\). As \(\eta\uparrow1/2\), the optimal displacement from the midpoint is \(\sqrt{(1/2-\eta)/42}+O((1/2-\eta)^{3/2})\).

More generally, if the squared error on the antisymmetric moment has arbitrary relative weight \(w>0\), the *complete* global design phase boundary is
\[
 w_c(\eta)=\frac{9+72\eta}{1+4\eta}.
\]
For \(w\leq w_c(\eta)\) the midpoint is the sole global optimum; for \(w>w_c(\eta)\) exactly two reflected off-midpoint times are globally optimal. The boundary increases strictly from \(9\) to \(18\) as \(\eta\) grows from zero to infinity.

## Assumptions and scope

Let \(B\) be the standard centered pinned Brownian bridge on \([0,1]\), with \(\operatorname{Cov}(B_s,B_t)=\min(s,t)-st\). Define the two scalar polynomial moments
\[
 J_0=\int_0^1 B_s\,ds,\qquad J_1=\int_0^1(2s-1)B_s\,ds.
\]
The weights \(1\) and \(2s-1\) are the first two *unnormalized shifted Legendre polynomials*. The observation at a freely chosen deterministic \(t\in[0,1]\) is \(Y_t=B_t+\sqrt\eta Z\), where \(\eta\geq0\) and \(Z\sim N(0,1)\) is independent of the bridge. Each target is estimated by its exact conditional mean given \(Y_t\). For \(w>0\), minimize
\[
 R_{w,\eta}(t)=\mathbb E[(J_0-\mathbb E[J_0\mid Y_t])^2]+w\,\mathbb E[(J_1-\mathbb E[J_1\mid Y_t])^2].
\]
At \(\eta=0\) the deterministic endpoint observations supply no information. The prior variances are \(\operatorname{Var}(J_0)=1/12\) and \(\operatorname{Var}(J_1)=1/180\), so choosing \(w=15\) is equivalent, after common scaling, to minimizing the *sum of squared errors normalized by each target's prior variance*.

## Proof

**Step 1: Exact conditional risk.** Direct integration of the bridge Green kernel gives, for every \(0\le t\le1\),
\[
 \operatorname{Cov}(B_t,J_0)=\frac{t(1-t)}2,\qquad
 \operatorname{Cov}(B_t,J_1)=\frac{t(1-t)(2t-1)}6.
\]
Since the vector \((J_0,J_1,Y_t)\) is centered Gaussian, its Bayes variance reduction equals the squared covariance with the observation divided by observation variance. Put \(u=t(1-t)\in[0,1/4]\); then \((2t-1)^2=1-4u\) and
\[
 R_{w,\eta}(t)=\frac1{12}+\frac w{180}
 -\frac{u^2(9+w-4wu)}{36(u+\eta)},\quad u+\eta>0.
\]
The zero-denominator endpoint at \(u=\eta=0\) is defined by its original probabilistic conditional-risk interpretation; the variance reduction is zero there. Thus minimizing risk is equivalent to maximizing the last nonnegative term.

**Step 2: Exact global maximizers.** Write the reduction as \(F(u)=u^2(9+w-4wu)/(36(u+\eta))\). For interior \(u>0\),
\[
 F'(u)=\frac{u}{36(u+\eta)^2}\,P(u),\qquad
 P(u)=2\eta(9+w)+(9+w-12w\eta)u-8wu^2.
\]
For each \(\eta>0\), the quadratic \(P\) has a positive constant and a negative leading coefficient, hence exactly one positive zero; \(P\) is positive below it and negative above it. For \(\eta=0\), \(P(u)=u(9+w-8wu)\), which has the same one-crossing sign property for \(u>0\). Therefore \(F\) first increases and then decreases, or increases throughout \([0,1/4]\); the global maximizing \(u\) is unique and equals
\[
 u_*(w,\eta)=\min\left\{\frac14,\frac{A+\sqrt{A^2+64w\eta(9+w)}}{16w}\right\},\quad A=9+w-12w\eta.
\]
The set of optimal sampling times is *exactly* \(\{(1\pm\sqrt{1-4u_*})/2\}\), interpreted as one point when \(u_*=1/4\). This argument includes the physical endpoints and the noiseless case.

**Step 3: Phase boundary and uniqueness.** The derivative sign at the boundary is governed by
\[
 P(1/4)=\frac{9-w+4\eta(18-w)}4.
\]
Its sign is nonnegative precisely when \(w\le (9+72\eta)/(1+4\eta)\). Strict one-crossing of \(F'\) implies that equality still gives the unique maximizer \(u_*=1/4\), proving the complete classification. Differentiating the threshold yields \(w_c'(\eta)=36/(1+4\eta)^2>0\).

**Step 4: Canonical equal-relative-variance criterion.** At \(w=15\), the boundary condition reads \(\eta\ge1/2\). For \(\eta=0\) the positive critical root is \(u_*=1/5\), hence \(t=(1\pm1/\sqrt5)/2\). For \(\eta=1/2-\delta\), expanding \(P(u)=0\) near \((u,\eta)=(1/4,1/2)\) gives \(P_u=-126\) and \(P_\eta=3\). The implicit-function theorem thus yields \(u_*=1/4-\delta/42+O(\delta^2)\), so the two reflected times obey
\[
 t_\pm=\frac12\pm\sqrt{\frac\delta{42}}+O(\delta^{3/2}),\qquad\delta\downarrow0.
\]
More generally, for each fixed \(\eta\ge0\), approaching the phase boundary from above gives
\[
 |t_\pm-1/2|=\sqrt{\frac{1+4\eta}{72(1+12\eta)}}\sqrt{w-w_c(\eta)}+O((w-w_c(\eta))^{3/2}).
\]
This follows from \(P_u(1/4,w_c)=-18(1+12\eta)\) and \(P_w(1/4,w_c)=-(1+4\eta)/4\).

## Verification

The accompanying independent standard-library Python program `verify.py` integrates the two Green-kernel covariances exactly at rational sampling sites, checks the exact phase-polynomial identity, confirms the noiseless golden-ratio times, compares the closed-form optimum with a global grid under random positive weights/noise, and checks the square-root boundary layer. Run with `python3 verify.py`. The reported 84,948 finite comparisons **supplement** rather than establish the analytic proof. All global uniqueness and boundary statements follow from the signed quadratic \(P\), independently of numerical checks.

## Relationship to prior work

Xi, Briol and Girolami (2018) develop joint Bayesian quadrature for multiple related integrals, with Gaussian conditional-covariance formulas and convergence analysis. This supplies the multi-output motivation and generic conditioning framework; it does not identify this bridge-specific single-sample global phase boundary. Foster, Lyons and Oberhauser (2019/2020) develop polynomial approximations of Brownian paths using integrated path moments; the polynomial-moment motivation is theirs, whereas their original optimization is of a different path-approximation problem with polynomial information supplied rather than a freely placed noisy point. Karvonen, Kanagawa and Särkkä (2018/2019) study positivity and magnitude of Bayesian quadrature weights and optimality of a fixed-point rule, not competing integrated moment targets. Existing work on randomized two-point Brownian-bridge sampling addresses a *single* integral with *two* evaluations, rather than the joint two-moment/single-reading loss here. Generic Gaussian conditioning and algebraic evaluation of moment covariances are not claimed as new; the claim is the complete exact global design transition and its canonical noise and square-root constants. An unrecognized older single-sensor multi-output specialization remains possible.

## Limitations

The results require the pinned Brownian-bridge covariance, two specified unnormalized polynomial moments, a single nonadaptive point sample, independent homoscedastic Gaussian observation noise, known covariance/noise and posterior-mean squared-error loss. They do not establish claims for other target bases, multiple readings, unknown hyperparameters, adaptive sampling, arbitrary noise covariances, or frequentist integration-error optimality. Prior-literature comparison supports provisional originality only, not independent publication priority.

## References

1. X. Xi, F.-X. Briol and M. Girolami, *Bayesian Quadrature for Multiple Related Integrals* (2018), arXiv:1801.04153, https://arxiv.org/abs/1801.04153 (first posted 2018-01-12).
2. J. Foster, T. Lyons and H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, SIAM J. Numer. Anal. 58 (2020), 1393–1421, arXiv:1904.06998, https://arxiv.org/abs/1904.06998 (first posted 2019-04-15).
3. T. Karvonen, M. Kanagawa and S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, Stat. Comput. 29 (2019), 1317–1333, arXiv:1812.08509, https://arxiv.org/abs/1812.08509 (first posted 2018-12-20).
