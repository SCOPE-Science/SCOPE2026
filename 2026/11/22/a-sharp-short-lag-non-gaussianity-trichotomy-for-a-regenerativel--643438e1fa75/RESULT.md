# A sharp short-lag non-Gaussianity trichotomy for a regeneratively accelerated diffusion clock

## Finding

A regenerative acceleration of an internal-state random walk has *exactly linear* displacement mean-square growth but three sharply different short-lag excess-kurtosis regimes. Let \(\gamma=a/b\), \(\eta=bt/d\), and let \(K(t)\) denote excess kurtosis of stationary-age displacements. For the model defined below,

\[
\mathbb E[(X_t-X_0)^2]=\frac{2D(a+b)}{ad}\,t,
\]

and, as \(t\downarrow0\),

\[
\begin{aligned}
0<\gamma<1:\quad &\eta^{1-\gamma}K(t)\longrightarrow
 \frac{6\pi\gamma}{(1+\gamma)^2\sin(\pi\gamma)},\\
\gamma=1:\quad &\frac{K(t)}{\log(1/\eta)}\longrightarrow\frac32,\\
\gamma>1:\quad &K(t)\longrightarrow\frac3{\gamma^2-1}.
\end{aligned}
\]

All displacement fourth moments are finite at any fixed positive lag, even in the regimes where the normalized fourth moment diverges as the lag decreases. The critical transition occurs when the stationary instantaneous operational speed changes from infinite to finite second moment.

## Assumptions and scope

Fix \(a,b,d,D>0\). In *operational time* \(u\), an internal age \(Y\) increases at unit speed and jumps to zero according to an independent Poisson process of rate \(a\). Define physical time by \(t(u)=\int_0^u d\exp[-bY_s]ds\), and its inverse \(U_t=\inf\{u\ge0:t(u)>t\}\). Let \(B\) be standard Brownian motion independent of the internal age and set \(X_t-X_0=\sqrt{2D}\,B_{U_t}\). No spatial resetting occurs when the internal age resets. Initialize \(Y_0\) with the invariant *physical-time* distribution, not a freshly reset age. The spatial displacement law is then stationary in its increments; the absolute position does not have a stationary distribution.

This is a precisely defined continuous-time transport model motivated by the internal renewal and geometric holding-time construction of Huang [1]. The assertion does not claim a finite-mesh convergence theorem or cover arbitrary state-dependent reset rates, waiting-time distributions, or initial internal ages.

## Proof

**1. Existence and invariant physical-time age.** A complete operational reset cycle has length \(E\sim\operatorname{Exp}(a)\) and physical duration \((d/b)(1-e^{-bE})\). Its mean equals \(d/(a+b)>0\); independent cycle durations therefore have an almost surely divergent sum, so the physical clock has no finite-time accumulation. Renewal reward gives the stationary physical-age density

\[
\frac{d e^{-by}\Pr(E>y)}{\mathbb E[(d/b)(1-e^{-bE})]}dy
=(a+b)e^{-(a+b)y}dy,\qquad y\ge0.
\]

Thus \(Y_0\sim\operatorname{Exp}(a+b)\). The physical-time operational speed is \(V_t=e^{bY_t}/d\) and satisfies

\[
\mathbb EV_t=\frac{a+b}{ad}=:v,
\qquad U_t=\int_0^tV_sds,\qquad \mathbb EU_t=vt.
\]

**2. A uniform first-excursion tail identity.** Denote by \(H_t\) the operational time accumulated before the first post-initial age reset, truncated at physical time \(t\). The residual reset waiting time in operational units is \(E\sim\operatorname{Exp}(a)\), independent of \(Y_0\). For every \(u>0\), the physical time needed to advance \(u\) without a reset is \(d e^{-bY_0}(1-e^{-bu})/b\). Independence gives

\[
\Pr(H_t>u)=e^{-au}\min\left\{1,
\left[\frac{bt}{d(1-e^{-bu})}\right]^{1+a/b}\right\}.
\tag{1}
\]

Set \(\gamma=a/b\) and \(\eta=bt/d\). By tail integration,

\[
\mathbb EH_t^2=2\int_0^\infty
u e^{-au}\min\left\{1,
\left[\frac{\eta}{1-e^{-bu}}\right]^{1+\gamma}\right\}du.
\tag{2}
\]

The factor \(u\) in this integral is ordinary operational time.

**3. Completed cycles are negligible at the relevant orders.** Put \(R_t=U_t-H_t\). Once the first post-initial reset has occurred, a subsequent current age cannot exceed \(-b^{-1}\log(1-bt/d)\) by physical time \(t\), because an uninterrupted age of \(y\) requires physical duration \((d/b)(1-e^{-by})\). Therefore, for \(0<t<d/(2b)\),

\[
0\le R_t\le\frac{t}{d(1-bt/d)}.
\]

Since \(\mathbb EH_t\le\mathbb EU_t=vt\), it follows from \(U_t^2-H_t^2=2H_tR_t+R_t^2\) that \(0\le\mathbb EU_t^2-\mathbb EH_t^2=O(t^2)\). Equation (1) also gives \(\mathbb EH_t^2<\infty\); hence the second moment of \(U_t\) is finite for all sufficiently small \(t\), and by subdivision plus stationarity it is finite for every fixed \(t>0\).

**4. Subcritical asymptotic, \(0<\gamma<1\).** In (2) the interval where the minimum is one has length \(-b^{-1}\log(1-\eta)=O(\eta)\) and contributes \(O(\eta^2)\). Dominated convergence outside this interval gives

\[
\lim_{\eta\downarrow0}\frac{\mathbb EH_t^2}{2\eta^{1+\gamma}}=
\int_0^\infty u e^{-au}(1-e^{-bu})^{-1-\gamma}du.
\]

With \(x=e^{-bu}\) and integration by parts, the last integral equals

\[
\frac1{\gamma b^2}\int_0^1x^{\gamma-1}(1-x)^{-\gamma}dx
=\frac{\pi}{\gamma b^2\sin(\pi\gamma)}.
\tag{3}
\]

The integral is finite precisely for \(0<\gamma<1\). Thus \(\mathbb EU_t^2\sim2\pi\eta^{1+\gamma}/[\gamma b^2\sin(\pi\gamma)]\).

**5. Critical asymptotic, \(\gamma=1\).** In (2), the integrand on the range \(\eta\ll bu\ll1\) equals \(2\eta^2/(b^2u)\) to leading order. Splitting at \(u=O(\eta/b)\), an arbitrary fixed small upper cutoff, and the remaining integrable tail yields

\[
\mathbb EU_t^2\sim\frac{2\eta^2}{b^2}\log\frac1\eta.
\tag{4}
\]

The first and last portions contribute only \(O(\eta^2)\) after the cutoff is fixed, and then the cutoff may be taken to zero.

**6. Supercritical limit, \(\gamma>1\).** The stationary instantaneous speed \(V_t=e^{bY_t}/d\) has finite second moment if and only if \(a>b\), in which case

\[
\mathbb EV_0^2=\frac{a+b}{d^2(a-b)}.
\]

The stationary piecewise deterministic age process is stochastically continuous, so \(V_t\to V_0\) in \(L^2\) as \(t\downarrow0\) (the family has uniformly integrable squares, for example by stationarity and an integrable squared envelope on short intervals, or by direct conditioning on the reset event). Hence \(U_t/t=t^{-1}\int_0^tV_sds\to V_0\) in \(L^2\), and

\[
\frac{\mathbb EU_t^2}{(\mathbb EU_t)^2}\longrightarrow\frac{a^2}{a^2-b^2}.
\tag{5}
\]

**7. Gaussian subordination.** Conditionally on \(U_t\), the displacement is centered Gaussian with variance \(2DU_t\). Thus

\[
\mathbb E[(X_t-X_0)^2]=2D\mathbb EU_t,
\quad\mathbb E[(X_t-X_0)^4]=12D^2\mathbb EU_t^2,
\quad K(t)=3\left(\frac{\mathbb EU_t^2}{(\mathbb EU_t)^2}-1\right).
\]

Substituting (3)--(5) and \(\mathbb EU_t=(1+\gamma)\eta/(\gamma b)\) yields exactly the three stated coefficients and completes the proof.

## Verification

The included dependency-free `checker.py` evaluates the positive first-excursion second-moment integral from equation (2) by logarithmically scaled Simpson quadrature, compares its normalized small-time values against (3)--(4), and separately checks physical-age normalization, first and second speed moments, Euler's beta reflection identity, and the finite-branch moment ratio. Run `python3 checker.py`. These checks are finite tests only; the proof above establishes the infinite-parameter and limiting assertions.

## Relationship to prior work

Huang [1], first publicly submitted 12 November 2026, develops a walk with internal-state renewal, state-dependent waiting times, and geometric acceleration; its model and continuum-limit machinery motivate this continuous accelerated-clock setup. The present assertion specifically concerns **physical-time stationary internal-age preparation** and the first complete short-lag fourth-moment trichotomy, not Huang's fresh-internal-state or unreset finite-time accumulation results. Chechkin, Seno, Metzler and Sokolov [2] establish the broad Brownian-yet-non-Gaussian and diffusing-diffusivity framework, including superstatistical short-time mixtures; general non-Gaussianity and the Gaussian-mixture identity are not claimed as new. The new content lies in the exact first-reset-clock cutoff and the three sharp model-specific coefficients. Prior general subordination theory could contain equivalent statements, so independent publication-priority verification remains important.

## Limitations

The proof addresses a continuum model with exponentially declining physical-time increments, constant positive operational reset rate and stationary internal age. It does not prove convergence from every discrete random walk, quantify finite-mesh errors, establish non-Gaussian measurement detectability under noise, or provide uniformity when \(\gamma\) approaches one simultaneously with \(t\downarrow0\). The finite-lag fourth moment is finite, even though its short-lag normalized value can diverge. The originality assessment is provisional pending independent literature review.

## References

[1] B. Z. Huang, *Continuous-Time Random Walks with Internal Stochastic Renewal Process*, arXiv:2611.16383v1 (first submitted 12 November 2026), https://arxiv.org/abs/2611.16383.

[2] A. V. Chechkin, F. Seno, R. Metzler and I. M. Sokolov, *Brownian Yet Non-Gaussian Diffusion: From Superstatistics to Subordination of Diffusing Diffusivities*, Physical Review X **7**, 021002 (2017), https://doi.org/10.1103/PhysRevX.7.021002.
