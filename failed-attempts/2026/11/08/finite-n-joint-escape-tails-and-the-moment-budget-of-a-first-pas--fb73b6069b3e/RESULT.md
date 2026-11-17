# Finite-\(N\) joint escape tails and the moment budget of a first-passage resetting gas

## Finding

Consider the stationary first-passage resetting gas with \(N\ge3\) particles and threshold \(L>0\), as defined below. Write \(Y_i=L-X_i\) for the nonnegative distance from particle \(i\) to its common upper resetting barrier. Put
\[
\alpha_N=\frac{N-2}{2},\qquad
\tau_N=\frac12\int_0^\infty\frac{\operatorname{erf}(u)^N}{u^3}\,du,\qquad
C_N=\frac{2^{N-2}\Gamma(\alpha_N)}{\pi^{N/2}\tau_N}.
\]
The normalizer \(\tau_N\) is positive and finite. For every integer \(1\le k\le N\) and every fixed vector \(a_1,\ldots,a_k>0\), the simultaneous negative-excursion probability obeys the sharp, finite-\(N\) law
\[
\lim_{R\to\infty}\left(\frac RL\right)^{N-2}
\Pr\bigl(Y_i>a_iR\text{ for }1\le i\le k\bigr)
=C_N\left(\sum_{i=1}^ka_i^2\right)^{-\alpha_N}.
\tag{1}
\]
In particular, all fixed numbers of simultaneous large excursions have the *same* power-law exponent \(N-2\), and their equal-threshold upper-tail dependence is
\[
\lim_{R\to\infty}\Pr(Y_2>R,\ldots,Y_k>R\mid Y_1>R)
=k^{-\alpha_N}.
\tag{2}
\]
Let \(A\) be the stationary elapsed time since the most recent collective reset. Conditional on the event in (1), the rescaled age \(V_R=4DA/R^2\) converges in distribution to the inverse-gamma law
\[
\Pr(V\in dv)=\frac{B^{\alpha_N}}{\Gamma(\alpha_N)}v^{-\alpha_N-1}
 e^{-B/v}\,dv,\qquad v>0,\qquad B=\sum_{i=1}^ka_i^2.
\tag{3}
\]
Finally, for every collection of exponents \(p_i\ge0\) with \(p_1+\cdots+p_k>0\), the exact stationary mixed-moment criterion is
\[
\mathbb E\prod_{i=1}^kY_i^{p_i}<\infty
\quad\Longleftrightarrow\quad \sum_{i=1}^kp_i<N-2.
\tag{4}
\]
At equality the associated large-age integral diverges logarithmically. Thus the stationary distance has infinite mean for \(N=3\), infinite variance for \(N\le4\), and infinite fourth moment for \(N\le6\), despite the existence of a stationary probability distribution throughout \(N\ge3\). The results apply to the distances below the absorbing threshold, not to excursions *above* that threshold.

## Assumptions and scope

The particles are independent one-dimensional Brownian motions between resets, each with generator \(D\partial_{xx}\), where \(D>0\). At a collective reset all coordinates instantaneously become zero. The next reset occurs at the first subsequent hitting of the common upper level \(L>0\) by any coordinate. The joint process has a regenerative stationary law when \(N>2\), a fact and an exact stationary mixture representation established in [1]. All probability statements above refer to that stationary law, with fixed finite \(N,k,L,D\); the limit in (1) has \(R\to\infty\), not \(N\to\infty\). The tagged particles may be any distinct labels by exchangeability. At positive times, \(X_i<L\) almost surely, so \(Y_i>0\).

Define the killed one-particle heat kernel and its survival function by
\[
G(x,t)=\frac{e^{-x^2/(4Dt)}-e^{-(x-2L)^2/(4Dt)}}{\sqrt{4\pi Dt}},\quad x<L,
\qquad S(t)=\operatorname{erf}\!\left(\frac L{\sqrt{4Dt}}\right).
\tag{5}
\]
Both are derived by the reflection principle. The stationary joint distribution is exactly the regenerative mixture
\[
\Pr((X_1,\ldots,X_N)\in d\mathbf{x})
=\frac1T\int_0^\infty\prod_{i=1}^NG(x_i,t)\,dt\,d\mathbf{x},
\quad T=\int_0^\infty S(t)^Ndt=\frac{L^2}{D}\tau_N.
\tag{6}
\]
The stationary reset age has density \(S(t)^N/T\). Given its value, particles are independent with conditional density \(G(x,t)/S(t)\). Equation (6), including its normalization, is prior work [1]; it is the starting point rather than a novelty claim.

## Proof

**1. Joint event integral and normalization.** Integrating the killed kernel to the position \(L-y\) gives the one-particle unnormalized survival-and-excursion probability
\[
H(y,t)=\int_{-\infty}^{L-y}G(x,t)dx
=\frac12\left[\operatorname{erf}\!\left(\frac{y+L}{\sqrt{4Dt}}\right)
-\operatorname{erf}\!\left(\frac{y-L}{\sqrt{4Dt}}\right)\right],\qquad y>0.
\tag{7}
\]
Integrating (6) in all untagged coordinates therefore yields exactly
\[
P_R=\Pr(Y_i>a_iR\text{ for }1\le i\le k)
=\frac1T\int_0^\infty\prod_{i=1}^k H(a_iR,t)S(t)^{N-k}\,dt.
\tag{8}
\]
With \(u=L/\sqrt{4Dt}\), a change of variables proves the expression for \(T\) in (6). Near zero, \(\operatorname{erf}(u)\sim2u/\sqrt\pi\), so \(\tau_N\) is finite precisely for \(N>2\), while the integrand is integrable at infinity for all \(N\). Integration by parts also gives a numerically useful second representation,
\[
\tau_N=\frac N{2\sqrt\pi}\int_0^\infty
\frac{e^{-u^2}\operatorname{erf}(u)^{N-1}}{u^2}\,du.
\tag{9}
\]
The boundary term at zero vanishes for \(N>2\).

**2. Sharp simultaneous-tail limit.** Set \(\varepsilon=L/R\) and \(w=R/\sqrt{4Dt}\). Equation (8) becomes
\[
P_R=\frac{(R/L)^2}{2\tau_N}\int_0^\infty\frac{dw}{w^3}
\prod_{i=1}^k\frac{\operatorname{erf}((a_i+\varepsilon)w)-\operatorname{erf}((a_i-\varepsilon)w)}2
\operatorname{erf}(\varepsilon w)^{N-k}.
\tag{10}
\]
At each fixed \(w>0\), division of each of the \(N\) probability factors by \(\varepsilon\) gives limits \((2w/\sqrt\pi)e^{-a_i^2w^2}\) for the tagged factors and \(2w/\sqrt\pi\) for the rest. For \(0<\varepsilon<\min_i a_i/2\), monotonicity of the Gaussian derivative gives the uniform bounds
\[
0\le\frac{H(a_iR,t)}\varepsilon\le\frac{2w}{\sqrt\pi}
 e^{-a_i^2w^2/4},\qquad
0\le\frac{S(t)}\varepsilon\le\frac{2w}{\sqrt\pi}.
\tag{11}
\]
Thus the normalized integrand is bounded by a constant times \(w^{N-3}e^{-Bw^2/4}\), which is integrable at both endpoints because \(N>2\) and \(B=\sum a_i^2>0\). Dominated convergence, together with
\[
\int_0^\infty w^{N-3}e^{-Bw^2}dw
=\frac12\Gamma(\alpha_N)B^{-\alpha_N},
\tag{12}
\]
proves the coefficient and every quantifier in (1). Dividing the joint equal-threshold limit by its single-particle instance yields (2); positivity of the denominator follows from \(C_N>0\).

**3. Conditional age law.** In the \(w\)-representation (10), after conditioning on the event, the normalized limiting measure has density proportional to \(w^{N-3}e^{-Bw^2}\). Equation (11) supplies the required dominated convergence for all bounded continuous test functions of \(w\). Under \(v=w^{-2}=4Dt/R^2\), this limiting density transforms into the inverse-gamma density (3), since \(\alpha_N=(N-2)/2\). The escape event has positive probability for sufficiently large \(R\), and the inverse-gamma density integrates to one by \(z=B/v\).

**4. Exact mixed-moment boundary.** Under (6), conditional on age \(t\), the distances \(Y_i\) are independent and have normalized density
\[
q_t(y)=\frac{e^{-(y-L)^2/(4Dt)}-e^{-(y+L)^2/(4Dt)}}
{\sqrt{4\pi Dt}\,S(t)},\qquad y>0.
\tag{13}
\]
Set \(s=\sqrt{4Dt}\), \(z=y/s\), and \(\delta=L/s\). The density of \(Y/s\) is
\[
f_\delta(z)=\frac{e^{-(z-\delta)^2}-e^{-(z+\delta)^2}}
{\sqrt\pi\operatorname{erf}(\delta)},\qquad z>0.
\tag{14}
\]
As \(t\to\infty\), \(\delta\downarrow0\), and \(f_\delta(z)\to2ze^{-z^2}\). For \(0<\delta\le1/2\), the difference-of-exponentials formula and \(\operatorname{erf}(\delta)\asymp\delta\) bound \(f_\delta(z)\) by an integrable multiple of \(z e^{-z^2/4}\). Consequently, for every real \(p\ge0\), dominated convergence yields
\[
\mathbb E(Y^p\mid A=t)
\sim (4Dt)^{p/2}\Gamma(1+p/2).
\tag{15}
\]
Here the conditional expectation is with respect to the *surviving* particle. By (6), the stationary mixed moment equals
\[
\frac1T\int_0^\infty S(t)^N
\prod_{i=1}^k\mathbb E(Y_i^{p_i}\mid A=t)\,dt.
\tag{16}
\]
Since \(S(t)\sim L/(\sqrt{\pi Dt})\), the positive integrand at infinity is asymptotic to a strictly positive finite constant times \(t^{(\sum_i p_i-N)/2}\). This is integrable if and only if \(\sum_i p_i<N-2\), and has logarithmic divergence at equality. Near \(t=0\), Brownian Gaussian moment bounds together with \(0\le G\le\) the free heat kernel and \(S(t)\to1\) show bounded conditional moments; hence no short-age obstruction occurs. Equation (4) follows, including necessity for equality and above.

## Verification

`verify.py` uses only the Python standard library. It numerically compares the two distinct integral representations of \(\tau_N\), evaluates the *exact* renewal event probability (10), checks convergence toward (1) for multiple \(N,k\), thresholds and large finite \(R\), and checks Rayleigh conditional-moment limits. Execute `python verify.py` in the directory containing the file. These are finite consistency checks and do not establish any limit; the integral domination and positive-integrand comparison above are the proof.

For reference, \(\tau_3\approx0.757602154837\) and \(C_3\approx0.840308819481\). Since the stationary position law in (6) is independent of \(D\), neither the tail constant nor the moment boundary depends on diffusivity, whereas the conditional reset age in (3) requires the factor \(D\).

## Relationship to prior work

Biroli, Majumdar and Schehr [1] establish the first-passage reset gas, its exact stationary mixture (6), its conditionally independent structure, and extensive large-\(N\) density, order-statistic, gap and counting formulas. Equations (5) and (6) above are imported from [1] and are **not** claimed as new. The present finite-\(N\) statement instead identifies the sharp joint negative-excursion tail including its all-threshold coefficient, the posterior age law under a rare simultaneous event, and the complete boundary of positive mixed moments. In particular, stationarity for \(N\ge3\) is *not* the same as finite physical moments.

Biswas, Majumdar and Pal [2] study threshold-reset target-search times, not these stationary multivariate spatial tails. Das, Majumdar and Pal [3] study threshold resetting for drift-diffusion; their one-particle steady-state and transient results do not give this collective Brownian-gas law. Majumdar and Schehr [4] survey dynamically emergent correlations, mostly through other resetting and mixture models. Huser, Opitz and Thibaud [5] demonstrate the **already-known** general principle that heavy-tailed random scales can create asymptotic dependence in Gaussian mixtures. The non-Gaussian killed-Brownian kernel, the \(N\)-dependent renewal-age tail, and exact finite-\(N\) constants and moment budget require the model-specific derivation above. More general regular-variation techniques may alternatively recover portions of (1)–(2), and an undiscovered published special case remains a publication-priority risk.

## Limitations

These claims concern fixed finite \(N\ge3\), the one-dimensional unbiased Brownian model with identical diffusivities and a *common* upper level, and stationary observations. They do not extend without new analysis to unequal diffusivities, independent resetting, drift, finite observation times, or simultaneous \(N,R\to\infty\) scalings. Formula (3) is conditional on the specified rare-event region, not the unconditional stationary age law. The proof establishes no finite-sample estimation rate or uniformity as any \(a_i\downarrow0\). Correlation observables involving fourth moments are undefined for \(N\le6\), so the large-\(N\) finite-fourth-moment comparison in [1] cannot simply be imported to such sizes. Scientific novelty is qualified by incomplete universal literature coverage; no independent audit has been performed.

## References

[1] M. Biroli, S. N. Majumdar and G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440 (publicly listed December 2, 2025), https://arxiv.org/abs/2512.00440 .

[2] A. Biswas, S. N. Majumdar and A. Pal, *Target search optimization by threshold resetting*, arXiv:2504.13501, https://arxiv.org/abs/2504.13501 .

[3] R. Das, S. N. Majumdar and A. Pal, *Non-equilibrium dynamics of drift-diffusion process under threshold resetting*, arXiv:2609.24438, https://arxiv.org/abs/2609.24438 .

[4] S. N. Majumdar and G. Schehr, *Dynamically Emergent Correlations*, arXiv:2603.03162, https://arxiv.org/abs/2603.03162 .

[5] R. Huser, T. Opitz and E. Thibaud, *Bridging Asymptotic Independence and Dependence in Spatial Extremes Using Gaussian Scale Mixtures*, arXiv:1610.04536, https://arxiv.org/abs/1610.04536 .
