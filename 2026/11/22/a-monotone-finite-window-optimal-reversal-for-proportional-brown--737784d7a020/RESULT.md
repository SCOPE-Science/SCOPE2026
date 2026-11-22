# A monotone finite-window optimal reversal for proportional Brownian resetting

## Finding

A single Brownian particle can reduce the sampling noise of its time-averaged position by **reversing its position at Poisson reset events**, even though reversal never improves its stationary positional variance. The exact best reversal factor depends monotonically on the observation duration. It starts at zero reversal for vanishingly short observations and approaches a universal one-third reflection-contraction for long observations.

**Theorem.** Let \(D,r,T>0\). Between points of an independent rate-\(r\) Poisson process, a stationary real-valued particle follows \(dX_t=\sqrt{2D}\,dW_t\). At each Poisson point it jumps \(X_t=aX_{t-}\), with a fixed signed factor \(-1<a<1\). Put

\[
\overline X_T=\frac1T\int_0^T X_t\,dt,\qquad \tau=rT,\qquad b=1-a\in(0,2).
\]

Its exact sampling variance is

\[
\boxed{\operatorname{Var}(\overline X_T)
=\frac{4D}{r\tau^2}\,
\frac{b\tau-1+e^{-b\tau}}{b^3(2-b)}.}
\]

For every finite \(\tau>0\), this variance has **exactly one global minimizer** \(a_*(\tau)\) over \(-1<a<1\), with

\[
\boxed{-\frac13<a_*(\tau)<0,\qquad a_*'(\tau)<0.}
\]

Here the derivative exists for every positive \(\tau\). Its value is determined without parameter fitting: \(b_*(\tau)=1-a_*(\tau)\) is the unique solution in \((1,4/3)\) of

\[
\boxed{
\frac{\int_0^\tau s(\tau-s)e^{-b s}\,ds}
{\int_0^\tau(\tau-s)e^{-b s}\,ds}
=\frac1{2-b}-\frac1b.}
\]

The short- and long-window limits, with dimensionless duration \(\tau=rT\), are

\[
\boxed{a_*(\tau)=-\frac{\tau}{6}+O(\tau^2)\quad(\tau\downarrow0),\qquad
 a_*(\tau)=-\frac13+\frac1{6\tau}+O(\tau^{-2})\quad(\tau\to\infty).}
\]

In particular, the long-window variance rate obeys the sharp optimization law

\[
\boxed{
\min_{-1<a<1}\lim_{T\to\infty}T\operatorname{Var}(\overline X_T)
=\frac{27D}{8r^2},\qquad
\operatorname{argmin}=\left\{-\frac13\right\}.}
\]

Relative to complete resetting \(a=0\), optimal signed proportional resetting reduces the asymptotic variance rate by exactly \(5/32=15.625\%\). By contrast, the instantaneous stationary positional variance \(2D/[r(1-a^2)]\) is uniquely minimized at \(a=0\). Consequently, snapshot minimization and trajectory-averaging minimization select different reset protocols for every nonzero observation duration.

## Assumptions and scope

The model is one-dimensional, has zero drift, constant diffusivity \(D>0\), independent Poisson jump clock of constant rate \(r>0\), and strictly contractive deterministic **signed** jump multiplier \(a\in(-1,1)\). Reflection means \(a<0\), so the position jumps to the opposite side of the origin with reduced magnitude. All observations begin in the unique invariant probability law, rather than at a freshly reset initial state. The objective is the ordinary variance of the **signed average position** over a finite time interval. It is not the variance of squared displacement, a first-passage observable, a reset-work cost, or the time integral of an absolute position.

The stationary law exists with finite second moment: after any common driving Brownian noise and Poisson clock, differences between two initial conditions are multiplied by \(a^{N_t}\), with \(N_t\to\infty\) almost surely. A stationary two-sided Poisson/Brownian construction gives a centered invariant limit; its second moment is finite because \(r(1-a^2)>0\). This also gives uniqueness of the invariant law, and stationary expectations below are well defined.

## Proof

**1. Exact stationary covariance.** The Markov generator on polynomials of degree at most two is

\[
\mathcal L f(x)=Df''(x)+r\bigl(f(ax)-f(x)\bigr).
\]

It satisfies \(\mathcal Lx=-r(1-a)x\) and \(\mathcal Lx^2=2D-r(1-a^2)x^2\). Stationarity therefore gives \(\mathbb E X_t=0\) and

\[
\mathbb E X_t^2=\frac{2D}{r(1-a^2)}.
\]

The backward semigroup is exact on linear functions: \(\mathbb E[X_t\mid X_0=x]=e^{-r(1-a)t}x\) for \(t\ge0\). The stationary covariance is accordingly

\[
C(t)=\operatorname{Cov}(X_0,X_t)
=\frac{2D}{r(1-a^2)}e^{-r(1-a)t}\qquad(t\ge0).
\]

No Gaussian or reversibility assumption is used. Integrating \(C(|t-s|)\) over the observation square gives

\[
\operatorname{Var}(\overline X_T)
=\frac2{T^2}\int_0^T(T-s)C(s)\,ds
=\frac{4D}{r\tau^2}\frac{J_\tau(b)}{b(2-b)},
\]

where \(J_\tau(b)=\int_0^\tau(\tau-s)e^{-bs}\,ds=(b\tau-1+e^{-b\tau})/b^2\). Substitution proves the finite-window formula.

**2. A unique optimizer for every duration.** Constants independent of \(b\) do not influence the minimizer, so set

\[
F_\tau(b)=\frac{J_\tau(b)}{b(2-b)}\qquad(0<b<2),
\]

and let \(\mu_\tau(b)=-\partial_b\log J_\tau(b)\). Since \(J_\tau\) is a positive Laplace integral, explicitly

\[
\mu_\tau(b)=\frac{\int_0^\tau s(\tau-s)e^{-bs}\,ds}
{\int_0^\tau(\tau-s)e^{-bs}\,ds}>0.
\]

Direct differentiation gives

\[
\partial_b\log F_\tau(b)
=\left(\frac1{2-b}-\frac1b\right)-\mu_\tau(b).
\]

For \(0<b\le1\) this is strictly negative. For \(1<b<2\), define \(R(b)=1/(2-b)-1/b\), increasing strictly from zero to infinity. The distribution on \((0,\tau)\) with normalized density proportional to \((\tau-s)e^{-bs}\) has strictly positive variance, so

\[
\partial_b\mu_\tau(b)=-\operatorname{Var}_{\tau,b}(s)<0.
\]

Thus \(R(b)-\mu_\tau(b)\) is strictly increasing on \((1,2)\), negative at \(b=1\), and positive near \(b=2\). Exactly one critical point exists; the derivative changes from negative to positive there. Since \(F_\tau(b)\to\infty\) at both \(b\downarrow0\) and \(b\uparrow2\), this critical point is the **unique global minimum**.

For the claimed tighter interval, compare \(\mu_\tau(b)\) with the mean \(1/b\) of an untruncated exponential variable \(S\) of rate \(b\). Reweighting its density by the nonincreasing function \((\tau-S)_+\) strictly reduces its mean, giving \(\mu_\tau(b)<1/b\). At \(b=4/3\), \(R(b)=1/b\). Therefore \(R(4/3)-\mu_\tau(4/3)>0\), and the unique optimizer satisfies \(1<b_*(\tau)<4/3\), or \(-1/3<a_*(\tau)<0\).

**3. Strict monotonicity in the observation duration.** Fix \(b>0\) and compare \(0<\tau_1<\tau_2\). On \((0,\tau_1)\), the ratio of the unnormalized weights at the two durations is \((\tau_2-s)/(\tau_1-s)\), a strictly increasing function of \(s\); the second weight also has positive mass in \((\tau_1,\tau_2)\). The normalized laws are therefore strictly ordered in the monotone likelihood-ratio sense, so \(\mu_{\tau_2}(b)>\mu_{\tau_1}(b)\). Because \(R(b)\) increases with \(b\) while \(\mu_\tau(b)\) decreases with \(b\), their unique intersection \(b_*(\tau)\) strictly increases with \(\tau\). Smooth dependence follows from the implicit-function theorem, since \(R'(b)-\partial_b\mu_\tau(b)>0\). Hence \(a_*'(\tau)<0\).

**4. Both endpoint expansions.** At small \(\tau\), \(\mu_\tau(b)=\tau/3+O(\tau^2)\) uniformly for \(b\) in a compact neighborhood of one, whereas \(R(b)=2(b-1)+O((b-1)^2)\). Hence \(b_*(\tau)=1+\tau/6+O(\tau^2)\).

As \(\tau\to\infty\), the Laplace-integral mean tends uniformly on compact positive \(b\)-intervals to \(1/b\). Its first correction is \(\mu_\tau(b)=1/b-1/(b^2\tau)+O(\tau^{-2})\), with exponentially small truncation terms. The only solution of \(R(b)=1/b\) in \((1,2)\) is \(b=4/3\). At that point the derivative of \(R(b)-1/b\) equals \(27/8\), giving \(b_*(\tau)=4/3-1/(6\tau)+O(\tau^{-2})\) by expansion of the unique root.

**5. Long-window noise limit and competing objectives.** Integrating the exponential covariance on the half-line,

\[
\lim_{T\to\infty}T\operatorname{Var}(\overline X_T)
=2\int_0^\infty C(s)\,ds
=\frac{4D}{r^2b^2(2-b)}.
\]

The cubic \(b^2(2-b)\) has its unique interior maximum at \(b=4/3\), yielding \(27D/(8r^2)\). At \(a=0\), the rate is \(4D/r^2\), and the ratio is \(27/32\). The instantaneous variance \(2D/[r(1-a^2)]\) is instead strictly minimized at \(a=0\). All assertions follow.

## Verification

The standalone `checker.py` evaluates the independent weighted-integral root equation, minimizes the variance directly with a bounded numerical optimizer, compares two algebraically different covariance-integration formulas, tests endpoint expansions and strict optimizer ordering across 11 durations, and compares the predicted time-average variance with 88,000 independently generated stationary Brownian-jump trajectories. The supplied run passed 83 assertions. Reproduce with `python checker.py` using Python 3, NumPy and SciPy. The simulation uses exact Poisson segments, Gaussian Brownian endpoints, and independent conditional bridge areas; it is a finite numerical corroboration, not a proof of universal optimality.

For illustration, at \(rT=1\) the optimal multiplier is approximately \(-0.1351710458\), at \(rT=3\) it is approximately \(-0.2539189488\), and at \(rT=10\) it is approximately \(-0.3145204059\). The exact theorem and monotone-likelihood-ratio proof, rather than these sampled values, establish the result for every duration.

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387v1, public 2024-06-12) analyze the **same signed-rescaling Brownian model** and establish its stationary position law and optimized **first-passage** search time, including advantageous negative rescaling. The present observable is instead finite-window, stationary **signed-position averaging noise**; the cited paper does not provide this horizon-dependent optimum. The stationary law, the generator and simple moment equations themselves are not claimed as novel.

Di Bello, Chechkin, Hartmann, Palmowski and Metzler (arXiv:2305.13722, 2023) derive time-dependent one-position distributions under positive proportional resetting. Tal-Friedman, Roichman and Reuveni (arXiv:2205.03363, 2022) establish stationary distributions and propagators for positive partial resetting. Olsen and Löwen (arXiv:2406.10039v1, 2024) include frozen refractory intervals and one-time cumulants, rather than the optimization of the integrated signed position under reflection. General spectral descriptions of additive-functional variance, such as Lapolla, Hartich and Godec (arXiv:2004.09387, 2020), explain why covariance integrals are legitimate, but do not provide the strict global reset-multiplier classification for this model.

Related previously published calculations explicitly include conditional-moment decay rates for signed proportional resets (the published-finding corpus finding *Hidden reset reflection and moment-rate tomography for contractive Brownian jumps*) and a long-run integrated-position variance for **positive** partial resets followed by refractory pauses (the published-finding corpus finding *Refractory-time variance is identifiable through integrated fluctuations under partial Brownian resetting*). The former contains the exponential-covariance ingredient; the latter's no-pause limit yields the long-run variance formula on its stated positive-multiplier domain. Neither supplies the new, all-finite-duration optimizer or its strict horizon monotonicity; those distinctions depend on comparing claims, not merely titles. General semigroup technology may be used to rederive the finite-window formula and is credited as standard machinery.

## Limitations

The claim is an exact second-moment optimization for a stationary, symmetric, zero-drift single particle and is not a universal optimal protocol for other observables, nonstationary starts, random multipliers, refractory waiting times, drift, or finite-speed returns. It makes no claim of entropy-production minimization or of a Gaussian law for the finite-time average. Although the optimization theorem is proved analytically, absence of an identical specialized theorem from the searched sources is not a proof of global publication priority; some claims could be implicit in general Markov-process functional methods. Numerical examples and Monte Carlo have finite precision and do not certify continuous-parameter claims.

## References

1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1, first submitted 2024-06-12, https://arxiv.org/html/2406.08387v1 .
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722, first submitted 2023-05-23, https://arxiv.org/html/2305.13722v2 .
3. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, first submitted 2022-05-06, https://arxiv.org/html/2205.03363v2 .
4. K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1, first submitted 2024-06-14, https://arxiv.org/html/2406.10039v1 .
5. A. Lapolla, D. Hartich and A. Godec, *Spectral theory of fluctuations in time-average statistical mechanics of reversible and driven systems*, arXiv:2004.09387, first submitted 2020-04-20, https://arxiv.org/abs/2004.09387 .
6. published-finding corpus, *Hidden reset reflection and moment-rate tomography for contractive Brownian jumps*, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-hidden-reset-reflection-and-moment-rate-tomography-for-contracti--6dfc6932c2a0 .
7. published-finding corpus, *Refractory-time variance is identifiable through integrated fluctuations under partial Brownian resetting*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-refractory-time-variance-is-identifiable-through-integrated-fluc--09a242f30c6d .
