# Sharp renewal-reset sign decorrelation and a heavy-tail occupation transition

## Finding

For the symmetric, nonsticky continuum sluggish diffusion restarted independently from the origin at stationary renewal times, let \(W>0\) denote the independent inter-reset time, \(m=\mathbb EW<\infty\), \(\mu=(\alpha+2)^{-1}\), and \(S_t=\operatorname{sgn}(X_t)\). For every \(t>0\), its stationary sign autocorrelation is exactly
\[
C_W(t)=\mathbb E[S_0S_t]=\frac1m\int_0^\infty\Pr(W>a+t)I_{a/(a+t)}(\mu,1-\mu)\,da
=\frac{\mathbb E[H_t(W)]}{m},
\quad H_t(w)=\mathbf1_{\{w>t\}}\int_0^{w-t}I_{a/(a+t)}(\mu,1-\mu)\,da.
\]
Here \(I_z\) is the regularized incomplete beta function. For every reset-time distribution of prescribed mean \(m\), the periodic clock \(W\equiv m\) simultaneously minimizes \(C_W(t)\) for *every* positive lag, with strict inequality for all \(0<t\le m\) if \(W\) is nondegenerate. Its normalized occupation-fraction variance is consequently smallest at every finite observation horizon.

The complete stationary correlation mass has the exact extended-real identity
\[
\int_0^\infty C_W(t)\,dt=\frac{1-\mu}{2m}\mathbb E[W^2].
\]
Thus if \(\mathbb E W^2<\infty\), the positive-half-line occupation fraction \(A_T=T^{-1}\int_0^T\mathbf1_{\{X_s>0\}}ds\) obeys
\[
\operatorname{Var}(A_T)\sim\frac{(1-\mu)\mathbb E W^2}{4mT}.
\]
If instead \(\Pr(W>t)\sim c t^{-\beta}\) for \(c>0\), then for \(1<\beta<2\),
\[
C_W(t)\sim \frac{c}{m}Q_{\mu,\beta}t^{1-\beta},\qquad
\operatorname{Var}(A_T)\sim\frac{cQ_{\mu,\beta}}{2m(2-\beta)(3-\beta)}T^{1-\beta},
\quad Q_{\mu,\beta}=\frac{\Gamma(\beta-\mu)}{(\beta-1)\Gamma(1-\mu)\Gamma(\beta)}.
\]
At the critical exponent \(\beta=2\),
\[
C_W(t)\sim\frac{c(1-\mu)}{mt},\qquad
\operatorname{Var}(A_T)\sim\frac{c(1-\mu)}{2m}\frac{\log T}{T}.
\]
For \(\beta>2\), the finite-second-moment formula applies. No assertion of a Gaussian limiting distribution follows solely from these variance statements.

## Assumptions and scope

Fix \(\alpha\ge0\) and \(\mu=1/(\alpha+2)\in(0,1/2]\). Between resets, the particle follows the regular, symmetric, nonsticky zero-crossing diffusion with backward generator \(\mathcal Lf(x)=|x|^{-\alpha}f''(x)\) away from zero, started from the origin, interpreted via its signed Bessel construction (the radial part reflects instantly at zero and successive excursion signs are unbiased). Each reset restarts a completely independent copy at the origin. Reset times are an independent, stationary *equilibrium* renewal process with iid positive intervals \(W\), positive finite mean \(m\); its age/residual pair has the standard length-biased equilibrium law even if \(W\) has atoms. A deterministic clock uses a uniform random stationary phase. The zero set of the diffusion has zero Lebesgue measure and is almost surely avoided at a fixed stationary time. No assumptions on the second reset-time moment are imposed except where stated. The heavy-tail assertions require an ordinary asymptotic constant \(\Pr(W>t)\sim c t^{-\beta}\), not merely unspecified regular variation.

The primary claim concerns the continuum diffusion with complete renewal resetting, not an exact finite-spacing lattice model, threshold resets, clocks chosen adaptively from the trajectory, or infinite-mean reset intervals.

## Proof

**1. A free-cycle sign kernel.** The signed Bessel representation of the free diffusion is strong Markov and symmetric about zero. Its last zero before time \(u>0\), divided by \(u\), has the \(\operatorname{Beta}(\mu,1-\mu)\) law; this is an established generalized last-passage/arcsine law [2,3]. For \(0<a<u\), decompose by the first zero after \(a\). If a zero is reached before \(u\), reflection symmetry and the strong Markov property give zero conditional expectation of the later sign given the earlier sign. Otherwise the signs agree. Hence
\[
\mathbb E[S_aS_u]=\Pr(\text{no zero in }(a,u])
=\Pr(L_u<a)=I_{a/u}(\mu,1-\mu).
\]
The same formula holds when \(a=0\) by continuity, with expectation zero. The last-zero law concerns the free diffusion started at the origin, not the stationarized reset process.

**2. Renewal conditioning.** A stationary renewal observation lies in a length-biased interval; the joint density of elapsed age \(a\) and residual time at least \(t\), integrated over the interval law, is \(\Pr(W>a+t)da/m\). If there is a reset in \((0,t]\), the sign after the first reset is conditionally symmetric and independent of the preceding sign, contributing zero correlation. If not, the two observations belong to one free trajectory and Step 1 supplies \(I_{a/(a+t)}\). This gives the first expression for \(C_W(t)\). Tonelli and conditioning on \(W=w\) give the \(H_t\) expression. In particular \(0\le C_W(t)\le1\), and \(C_W(0+)=1\).

**3. Sharp all-lag deterministic optimality.** For \(w\le t\), \(H_t(w)=0\). For \(w>t\), differentiation of the integral upper limit gives
\[
H_t'(w)=I_{1-t/w}(\mu,1-\mu).
\]
The right-hand side increases strictly from zero to one on \((t,\infty)\); it matches the zero left derivative at \(w=t\). Therefore \(H_t\) is convex on the entire nonnegative line and strictly convex above \(t\). Jensen's inequality yields \(C_W(t)=\mathbb EH_t(W)/m\ge H_t(m)/m\). When \(t<m\), the tangent at \(m\) contacts the graph only at \(m\): strict convexity gives strict separation at every other point above \(t\), and at \(t\) the tangent is strictly below zero because \(H_t(m)=\int_t^m H_t'(w)\,dw<(m-t)H_t'(m)\). It stays below zero for \(w<t\). Thus equality requires \(W=m\) almost surely. When \(t=m\), the tangent instead coincides with the graph on \([0,m]\). A nondegenerate \(W\) with mean \(m\) must have \(\Pr(W>m)>0\), and \(H_m(w)>0\) there, so the inequality is still strict. Since the variance in Step 5 is a positive integral of these covariances, the periodic clock also minimizes \(\operatorname{Var}(A_T)\) for each fixed \(T>0\); strictness for a nondegenerate clock follows by integrating positive lag differences over \((0,\min(m,T))\).

**4. Correlation mass.** By Tonelli, integrate over the triangle \(a>0,t>0,a+t<w\). Setting \(u=a+t\) and \(v=a/u\), its Jacobian is \(u\), so
\[
\int_0^\infty H_t(w)dt
=\frac{w^2}{2}\int_0^1 I_v(\mu,1-\mu)dv
=\frac{(1-\mu)w^2}{2}.
\]
The last integral equals \(1-\mathbb E B=1-\mu\) for \(B\sim\operatorname{Beta}(\mu,1-\mu)\), as follows from Fubini. Division by \(m\) and expectation yield the formula even when \(\mathbb EW^2=+\infty\).

**5. Occupation variance.** By symmetry \(\mathbb E\mathbf1_{\{X_t>0\}}=1/2\), and the stationary occupation-indicator covariance equals \(C_W(t)/4\). Exact stationary double integration gives
\[
\operatorname{Var}(A_T)=\frac1{2T^2}\int_0^T(T-t)C_W(t)dt.
\]
When \(C_W\) is integrable, dominated convergence applied to \((1-t/T)_+C_W(t)\) gives \(\operatorname{Var}(A_T)\sim(2T)^{-1}\int_0^\infty C_W(t)dt\), yielding the displayed finite-second-moment constant.

**6. Heavy-tail coefficients and transition.** Suppose \(\Pr(W>t)\sim ct^{-\beta}\) with \(\beta>1\). Set \(a=tx\) in the renewal formula. A Potter bound for the survival function, the bounded beta kernel, and \(\beta>1\) permit dominated convergence, giving
\[
C_W(t)\sim \frac{c}{m}t^{1-\beta}
\int_0^\infty(1+x)^{-\beta} I_{x/(1+x)}(\mu,1-\mu)dx.
\]
With \(y=x/(1+x)\) and integration by parts, the integral is
\[
\frac{1}{\beta-1}\int_0^1(1-y)^{\beta-1}\frac{y^{\mu-1}(1-y)^{-\mu}}{B(\mu,1-\mu)}dy
=\frac{\Gamma(\beta-\mu)}{(\beta-1)\Gamma(1-\mu)\Gamma(\beta)}.
\]
For \(1<\beta<2\), substitute this regularly varying covariance into Step 5 and rescale \(t=Ts\): the beta integral \(\int_0^1(1-s)s^{1-\beta}ds=[(2-\beta)(3-\beta)]^{-1}\) gives the exact variance constant. For \(\beta=2\), the coefficient simplifies to \(Q_{\mu,2}=1-\mu\) and integration gives the \((\log T)/T\) law. For \(\beta>2\), \(\mathbb EW^2<\infty\) and Step 5 applies. These are exact first-order equivalents; no finite-time error bound is claimed.

**7. Known Poisson consistency.** If \(W\sim\operatorname{Exp}(r)\), the renewal integral evaluates to \(C_W(t)=\Gamma(1-\mu,rt)/\Gamma(1-\mu)\), which is consistent with the already-known reset last-passage Gamma law [2]; its mass is \((1-\mu)/r\). The occupation-fraction coefficient is \((1-\mu)/(2rT)\), agreeing with the earlier Poisson-reset occupation result [1]. These specializations are *not* asserted to be novel.

## Verification

The accompanying `verify.py` is a standalone numerical diagnostic requiring Python, NumPy and SciPy; run `python verify.py`. It independently integrates the survival and incomplete-beta kernels, tests the Poisson/Gamma reduction at twelve parameter points, checks 350 random four-point reset-time mixtures against the periodic optimum, tests twenty Pareto tail coefficient instances, validates six exact integrated-covariance identities and six free last-zero beta identities. Numeric tolerance and finite samples do not replace the analytic proof of infinitely many distributions, lags, or exponents. All package code and references needed to reproduce these numerical checks are included.

## Relationship to prior work

[1] Frimpong, Bresque and Roldán study **Poisson** and spatial-threshold reset rules and derive Poisson occupation fluctuations. [2] Frimpong derives the **Poisson** last-zero Gamma distribution and quotes the free generalized arcsine law, which we use as an explicit input, not as a claimed discovery. [3] Del Vecchio Del Vecchio and Majumdar establish the free sluggish-walk arcsine law. [4] Akimoto derives equilibrium occupation/correlation laws, including anomalous variance decay, for alternating renewal sign signals. In that two-state model, signs flip at holding-time transitions; here the diffusion can cross zero within each separately renewed external reset cycle. The general complete-renewal autocorrelation formula of [5, Eq. (32)] is closely related: for regular nonarithmetic finite-mean clocks its stationary limit, applied to the free sign process, gives the renewal averaging formula by the key renewal theorem. The equilibrium argument above also applies to atomic clocks, including the periodic clock with a stationary phase. Neither the generic renewal autocorrelation mechanism nor the free Beta law is claimed as new. The distinctive conclusions are the sharp all-lag fixed-mean minimization for this sign kernel and the explicit integrated and heavy-tail occupation-variance constants, including the critical logarithmic coefficient.

The indexed searches included exact and alias queries for renewal-reset sign autocorrelation, incomplete-beta persistence, fixed-mean deterministic resetting, and heavy-tail occupation variance. The general representation and the related equilibrium occupation results noted above overlap with parts of the argument. The sources compared do not establish the all-lag strict optimum or the stated heavy-tail coefficients for the specified sluggish diffusion. These comparisons do not establish historical priority.

## Limitations

All claims are mathematical claims for the specified regular continuum diffusion and **independent complete** reset cycles, in the equilibrium renewal regime with finite mean. They do not extend without further proof to adaptive reset clocks, persistent internal clocks, initial nonstationarity, finite lattices, infinite-mean renewals, nonlinear occupation statistics, or observational noise. Strict minimization at an individual lag \(t>m\) is not claimed (equality can occur). Heavy-tail constants assume \(\Pr(W>t)\sim ct^{-\beta}\) with a positive constant. Only leading-order large-time variances are proved, not distributional CLTs. Uninspected general renewal-reward or Bessel-persistence work may overlap with these conclusions.

## References

1. T. D. Frimpong, L. Bresque and E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962 (first publicly submitted 2026-10-15), https://arxiv.org/abs/2610.21962 .
2. T. D. Frimpong, *Extremal and global-time statistics of sluggish random walks with stochastic resetting*, arXiv:2610.34568 (first publicly submitted 2026-10-25), https://arxiv.org/abs/2610.34568 .
3. G. Del Vecchio Del Vecchio and S. N. Majumdar, *Generalized arcsine laws for a sluggish random walker with subdiffusive growth*, arXiv:2410.22097 (2024), https://arxiv.org/abs/2410.22097 .
4. T. Akimoto, *Statistics of the number of renewals, occupation times and correlation in ordinary, equilibrium and aging alternating renewal processes*, arXiv:2306.00359 (2023), https://arxiv.org/abs/2306.00359 .
5. Taźbierski, Metzler and Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting*, *New Journal of Physics* 27 (2025), 074603, https://doi.org/10.1088/1367-2630/adee40 .
