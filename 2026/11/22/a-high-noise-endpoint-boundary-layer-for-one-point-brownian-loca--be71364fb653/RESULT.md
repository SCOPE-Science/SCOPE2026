# A high-noise endpoint boundary layer for one-point Brownian local-time estimation

## Finding
Let \(B\) be standard Brownian motion started at zero, and let \(L=L_1^0\) be its occupation-density local time at zero up to time one. For any observation-noise variance \(\eta>0\), select one deterministic time \(t\in[0,1]\) and observe \(Y_t=B_t+\sqrt\eta\,Z\), where \(Z\) is independent standard normal. Estimate \(L\) by its conditional mean, minimizing Bayes mean-square error.

**Exact all-noise risk formula.** Put \(c_k=\binom{2k}{k}/4^k\) and
\[
A_k(t)=\frac{2k\,t^{k+1/2}}{k^2-1/4}-\frac{t^{2k}}{k-1/2}\quad(k\ge1,\;0\le t\le1).
\]
The explained variance is exactly
\[
I_\eta(t)=\operatorname{Var}(\mathbb E[L\mid Y_t])
=\frac1{2\pi}\sum_{k=1}^\infty c_k\frac{A_k(t)^2}{(t+\eta)^{2k}},
\]
and the minimum risk for this chosen observation time is
\[
R_\eta(t)=1-\frac2\pi-I_\eta(t).
\]
For every finite \(\eta>0\), every maximizing observation time is strictly interior. There exists \(\eta_0>0\) such that for all \(\eta\ge\eta_0\) the maximizer \(t_\eta\) is unique, and
\[
\boxed{t_\eta=1-\frac1{3\eta}+\frac{11}{36\eta^2}+O(\eta^{-3})}\qquad(\eta\to\infty).
\]
The corresponding maximum explained variance obeys
\[
\boxed{I_\eta(t_\eta)=\frac1{9\pi\eta^2}-\frac2{9\pi\eta^3}+O(\eta^{-4})}.
\]
These expansions are asymptotic statements for noise variance tending to infinity, not approximations uniformly accurate for arbitrary noise levels. No uniqueness claim is made for all positive \(\eta\).

## Assumptions and scope
The local-time normalization is \(L_1^0=\lim_{\varepsilon\downarrow0}(2\varepsilon)^{-1}\int_0^1\mathbf1_{\{|B_s|<\varepsilon\}}\,ds\) in the standard occupation-density sense. The target is the *realized* local time, not its deterministic expectation. Only one nonadaptive point observation is available; Gaussian noise is independent of the path, its variance is known, and squared-error loss is used. The admissible times are the entire closed interval \([0,1]\). The estimator may be any square-integrable measurable function of the observation. Local time and the observation are square-integrable.

## Proof
**Step 1: the exact conditional predictor.** Write \(q_s(t)=\min(s,t)\), \(v_s=s-q_s(t)^2/(t+\eta)\), and \(m_s(y)=q_s(t)y/(t+\eta)\). Gaussian conditioning gives \(B_s\mid(Y_t=y)\sim N(m_s(y),v_s)\). Using Gaussian mollifiers of the occupation density, then \(L^2\) convergence, proves
\[
\widehat L_t(y)=\mathbb E[L\mid Y_t=y]
=\int_0^1\frac{\exp[-m_s(y)^2/(2v_s)]}{\sqrt{2\pi v_s}}\,ds.
\]
For \(\eta>0\), the integrand is defined for all \(s>0\). The standard local-time identity \(L_1^0\overset d=|N(0,1)|\) implies \(\operatorname{Var}(L)=1-2/\pi\). Conditional expectation is the unique squared-error optimal estimator (up to observation-null sets).

**Step 2: exact explained variance.** Let two independent path copies be conditionally independent given the same \(Y_t\). Averaging the product of their conditional local-time densities amounts to evaluating a bivariate centered Gaussian density at zero, with marginal variances \(s,u\) and cross-covariance \(q_s(t)q_u(t)/(t+\eta)\). Thus
\[
I_\eta(t)=\frac1{2\pi}\int_0^1\!\int_0^1\frac1{\sqrt{su}}
\left[\left(1-\frac{q_s(t)^2q_u(t)^2}{su(t+\eta)^2}\right)^{-1/2}-1\right]ds\,du.
\]
The bracket is nonnegative and its argument is uniformly bounded away from one for \(\eta>0\), so the binomial expansion and Tonelli's theorem apply. Evaluating
\[
\int_0^1\frac{q_s(t)^{2k}}{s^{k+1/2}}\,ds
=\frac{t^{k+1/2}}{k+1/2}+t^{2k}\int_t^1s^{-k-1/2}\,ds=A_k(t)
\]
yields the asserted series, including at \(t=0\) by continuity.

**Step 3: finite-noise optimality is interior.** The exact series is continuous on \([0,1]\), zero at \(t=0\), and strictly positive for \(t>0\). Differentiation at the right endpoint is legitimate for \(\eta>0\). Since \(A_k'(1)=0\) and \(A_k(1)=1/(k+1/2)\),
\[
I_\eta'(1)=-\frac1\pi\sum_{k\ge1}\frac{k\,c_k}{(k+1/2)^2(1+\eta)^{2k+1}}<0.
\]
Consequently neither endpoint maximizes \(I_\eta\), and at least one maximizer lies in \((0,1)\).

**Step 4: uniqueness at sufficiently high noise.** For \(t>0\),
\[
A_k'(t)=\frac{2k}{k-1/2}t^{k-1/2}(1-t^{k-1/2}).
\]
The upper estimate \(A_k(t)\le\frac{2k}{k^2-1/4}t^{k+1/2}\) implies
\[
\frac{A_k'(t)}{kA_k(t)}\ge\frac{1-\sqrt t}{t}.
\]
For \(0<t\le1/2\) and \(\eta\ge2\), \((t+\eta)A_k'(t)>kA_k(t)\); each summand of \(I_\eta\) is therefore strictly increasing in that range.

On \([1/2,1]\), differentiating the geometrically dominated series twice shows convergence in \(C^2\):
\[
\eta^2 I_\eta(t)\longrightarrow \frac{A_1(t)^2}{4\pi},
\quad A_1(t)=\frac83t^{3/2}-2t^2.
\]
The limit has positive first derivative on \([1/2,3/5]\). Furthermore,
\[
A_1'(t)^2+A_1(t)A_1''(t)
=\frac43t(16-35\sqrt t+18t)<0\quad(3/5\le t\le1).
\]
Therefore \(I_\eta'\) is positive on \([1/2,3/5]\), and \(I_\eta''<0\) on \([3/5,1]\), for all sufficiently large \(\eta\). Together with \(I_\eta'(1)<0\) these signs give exactly one zero of \(I_\eta'\), hence one global maximizer. The existence statement does not require an explicit numerical threshold \(\eta_0\).

**Step 5: sharp boundary layer and information.** The unique maximum tends to one by uniform convergence in Step 4. Write \(t=1-\delta\). Because \(A_k'(1)=0\), the sum of derivatives for \(k\ge2\) is \(O(\eta^{-5})\) when \(\delta=O(\eta^{-1})\). The leading \(k=1\) critical equation is \((t+\eta)A_1'(t)-A_1(t)=0\). It first gives \(\delta=O(\eta^{-1})\), and the remaining terms perturb its solution by \(O(\eta^{-3})\). With \(u=\sqrt t\), the leading equation becomes
\[
2\eta(1-u)=u^2(u-2/3).
\]
Its expansion \(u=1-(6\eta)^{-1}+5/(36\eta^2)+O(\eta^{-3})\) gives \(t=1-(3\eta)^{-1}+11/(36\eta^2)+O(\eta^{-3})\). At this time \(A_1(t)=2/3+O(\eta^{-2})\), while all \(k\ge2\) terms of the information series contribute \(O(\eta^{-4})\). Expanding \((t+\eta)^{-2}\) gives the stated explained-variance expansion.

## Verification
`check_local_time.py` is a complete standalone standard-library verifier. It independently compares the series to a transformed two-dimensional Gaussian-density integral, compares analytic and finite-difference derivatives, checks the closed \(A_k\) formula, computes stationary observation locations for six finite noise levels, and tests the boundary-layer approximation and explained-variance expansion. Its finite experiments supplement the proof, not establish global uniqueness or asymptotics.

## Relationship to prior work
Ivanovs and Podolskij (arXiv:2001.02517, Sections 3.1–3.2 and Appendix B) derive Brownian local-time conditional-mean estimators and their high-frequency-grid asymptotics; in particular they derive the basic Brownian endpoint conditioning ingredients. Altmeyer and Le Guével (arXiv:2108.11632, Sections 1–2 and Section 3) study asymptotically optimal high-frequency approximation for occupation and local times of stable processes. Amorino, Jaramillo, and Podolskij (arXiv:2210.07672, introduction and main results in Sections 1–2) extend this high-frequency framework to pure-jump stable local times. None of the inspected theorems optimizes the location of a *single noisy* Brownian measurement or establishes the \(1/(3\eta)\) endpoint boundary layer. The conditional-expectation principle and elementary Gaussian conditioning are existing tools, not claimed as new.

## Limitations
This is an exact known-law one-measurement design theorem. Uniqueness is proved for sufficiently high observation noise, not asserted for every noise variance. The work does not establish optimality of multi-time, adaptive, threshold, or nonlinear sensor designs; unknown diffusion coefficients and non-Gaussian sensor noise are not treated. Historical priority beyond the inspected relevant sources remains open to independent scrutiny. A numerical root at low noise is not an infinite-domain uniqueness certificate.

## References
1. Jevgenijs Ivanovs and Mark Podolskij, *Optimal estimation of some random quantities of a Lévy process*, arXiv:2001.02517 (first public version 2020-01-08), https://arxiv.org/abs/2001.02517.
2. Randolf Altmeyer and Ronan Le Guével, *Optimal \(L^2\)-approximation of occupation and local times for symmetric stable processes*, arXiv:2108.11632 (first public version 2021-08-26), https://arxiv.org/abs/2108.11632.
3. Chiara Amorino, Arturo Jaramillo, and Mark Podolskij, *Optimal estimation of local time and occupation time measure for an \(\alpha\)-stable Lévy process*, arXiv:2210.07672 (first public version 2022-10-14), https://arxiv.org/abs/2210.07672.
