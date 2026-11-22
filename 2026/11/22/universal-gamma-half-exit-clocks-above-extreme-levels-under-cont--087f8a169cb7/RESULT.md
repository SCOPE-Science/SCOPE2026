# Universal Gamma-half exit clocks above extreme levels under contractive Poisson resetting

## Finding

Consider a stationary, one-dimensional driftless Brownian motion with instantaneous Poisson resetting. At each rate-\(r\) reset, the position is transformed by an independent random affine map \(z\mapsto Cz+B\), where the multiplier is uniformly contractive and the displacement is bounded, as specified below. Let \(\tau_u\) denote the first time that a trajectory *initially conditioned above* a high level \(u\) returns to that level or below. With \(\lambda=\sqrt{2r}/\sigma\), the following joint rare-excursion law holds as \(u\to\infty\):

\[
\left(Z_0-u,\tau_u\mid Z_0>u\right)
\ \Longrightarrow\ 
\left(U,\min\{S,H_U\}\right),
\]

where \(U\sim\operatorname{Exp}(\lambda)\), \(S\sim\operatorname{Exp}(r)\), and the standard Brownian motion defining \(H_U=\inf\{t\ge0:U+\sigma W_t\le0\}\) are mutually independent. In particular,

\[
\boxed{\Pr(\tau_u>t\mid Z_0>u)\ \longrightarrow\
\operatorname{erfc}(\sqrt{rt}),\qquad t\ge0.}
\]

Hence the asymptotic time spent above the very high observed level before the first downward exit has the **Gamma distribution with shape \(1/2\) and rate \(r\)**, with density

\[
f(t)=\frac{\sqrt r}{\sqrt{\pi t}}e^{-rt},\qquad t>0.
\]

This limit is independent of the Brownian diffusion scale \(\sigma\), of the law of \((C,B)\) within the stated class, and of the particular high level. The mean of the *limiting* clock is \(1/(2r)\); convergence of the original conditional means is not asserted. In the special case of resetting **exactly to zero** (\(C=B=0\) almost surely), the displayed Gamma-half exit law holds **exactly for every** \(u\ge0\), without taking a high-level limit.

## Assumptions and scope

Fix \(r>0\), \(\sigma>0\), a deterministic contraction bound \(c_*\in[0,1)\), and a deterministic shift bound \(K\in[0,\infty)\). Between resets, \(dZ_t=\sigma\,dW_t\). Resets are the jump epochs of an independent homogeneous Poisson process of rate \(r\). At each epoch \(Z_t=C_jZ_{t-}+B_j\), where the pairs \((C_j,B_j)\) are identically distributed and independent over epochs and of the driving Brownian motion and Poisson process; arbitrary dependence *within* a pair is permitted. Assume \(|C_j|\le c_*\) and \(|B_j|\le K\) almost surely. The process is observed in its unique stationary law. The event \(Z_0>u\) has positive probability for all finite \(u\). For \(u\ge0\), under this conditioned stationary law let

\[
\tau_u=\inf\{t\ge0: Z_t\le u\},\qquad Z_0>u.
\]

The limit is taken with the reset law, \(r\), and \(\sigma\) fixed as \(u\to\infty\). A downward jump at a reset counts as an exit. Only positive extremes are examined; the Brownian motion is driftless, and the contraction is *uniformly strict*. The Gamma convention is shape/rate, not shape/scale.

## Proof

**1. A Laplace leading innovation.** Let \(E\sim\operatorname{Exp}(r)\) be independent of Brownian motion. The displacement \(\xi=\sigma W_E\) has characteristic function \(r/(r+\sigma^2\theta^2/2)\), hence the symmetric Laplace density \(\frac\lambda2e^{-\lambda|x|}\) for \(\lambda=\sqrt{2r}/\sigma\). At stationary observation times, Poisson memorylessness and the embedded affine chain give the independent decomposition

\[
Z_0\stackrel d=\xi_0+R,\qquad
R=B_0+C_0(\xi_1+B_1+C_1(\xi_2+\cdots)),
\]

where \((\xi_j)\) are independent copies of \(\xi\), the reset-mark pairs are independent across indices, and \(\xi_0\) is independent of \(R\). Strict contraction and bounded shifts ensure convergence of the backward series and uniqueness of the invariant law. The existence and fixed-point representation for general reset maps are known; no novelty is claimed for them.

Select \(\eta>\lambda\) such that \(\eta c_*<\lambda\) (for \(c_*=0\), take any \(\eta>\lambda\)). The pathwise bound

\[
|R|\le\frac{K}{1-c_*}+\sum_{j=1}^\infty c_*^j|\xi_j|
\]

and \(\mathbb E e^{s|\xi|}=\lambda/(\lambda-s)\) for \(s<\lambda\) show that \(\mathbb E e^{\eta|R|}<\infty\): every factor in the convergent infinite product is finite, and the sum of its logarithms is finite because \(\sum_{j\ge1}c_*^j<\infty\). Thus \(R\) has a strictly lighter right tail than \(\xi_0\).

For each \(v>0\), independence and the Laplace right tail give

\[
\Pr(Z_0>v)=\frac12e^{-\lambda v}
\mathbb E[e^{\lambda R}\mathbf1_{\{R\le v\}}]
+\mathbb E[\Pr(\xi_0>v-R)\mathbf1_{\{R>v\}}].
\]

The second term is bounded by \(\Pr(R>v)=o(e^{-\lambda v})\), and monotone convergence applies to the first term. Consequently, with \(m_R=\mathbb Ee^{\lambda R}\in(0,\infty)\),

\[
\Pr(Z_0>v)\sim\tfrac12m_R e^{-\lambda v},\qquad
\Pr(Z_0-u>y\mid Z_0>u)\to e^{-\lambda y}
\quad(y\ge0).
\]

The conditional overshoot \(V_u=Z_0-u\) therefore converges to the independent exponential variable \(U\) described above. Its tightness is a key ingredient below.

**2. A high excursion is terminated by its first reset.** Conditional on \(Z_0>u\), the future driving Brownian motion and reset process are independent of \(V_u\). Let \(S\sim\operatorname{Exp}(r)\) be the first future reset epoch and let \(H_{V_u}=\inf\{t\ge0:V_u+\sigma W_t\le0\}\) be the no-reset return time to the original level. For any deterministic observation horizon \(T<\infty\), tightness of \(V_u\) and the almost sure finiteness of \(\sup_{0\le s\le T}|\sigma W_s|\) imply that, with conditional probability tending to one, both are less than \(\delta u\), for any fixed \(\delta>0\). Choose \(\delta\) small enough that \(c_*(1+2\delta)<1\). If a first reset occurs by \(T\) while the process is still above \(u\), its position immediately before that reset is between \((1-\delta)u\) and \((1+2\delta)u\) on this high-probability event. Its position just after resetting is at most

\[
C_1Z_{S-}+B_1\le c_*|Z_{S-}|+K
\le c_*(1+2\delta)u+K<u
\]

for all sufficiently large \(u\). Thus, on every fixed horizon, a first reset that occurs before a Brownian downcrossing also causes a downcrossing, with probability tending to one. Precisely, for every fixed \(t\ge0\),

\[
\Pr(\tau_u>t\mid Z_0>u)
=\Pr(S>t,H_{V_u}>t\mid Z_0>u)+o(1).
\]

The same approximation holds with a bounded measurable factor depending only on \(V_u\); in particular it proves the claimed joint overshoot/exit limit by bounded-continuous test functions and continuity of the Brownian first-hitting-time law in its positive initial distance.

**3. The Gamma-half mixture.** The reflection principle gives, for every \(z>0\) and \(t>0\),

\[
\Pr(H_z>t)=\operatorname{erf}\!\left(\frac{z}{\sigma\sqrt{2t}}\right).
\]

With the independent exponential overshoot and reset clock, dominated convergence yields

\[
\begin{aligned}
\lim_{u\to\infty}\Pr(\tau_u>t\mid Z_0>u)
&=e^{-rt}\int_0^\infty\lambda e^{-\lambda z}
\operatorname{erf}\!\left(\frac{z}{\sigma\sqrt{2t}}\right)dz\\
&= e^{-rt}\exp\!\left(\frac{\lambda^2\sigma^2t}{2}\right)
\operatorname{erfc}\!\left(\lambda\sigma\sqrt{\frac t2}\right)\\
&=\operatorname{erfc}(\sqrt{rt}).
\end{aligned}
\]

For the middle equality, interchange the exponential tail integral with the standard integral representation of \(\operatorname{erf}\), or integrate by parts and complete the Gaussian square; all integrands are nonnegative, so Tonelli's theorem applies. Since the resulting survival function is continuous, decreases from one to zero, and has derivative \(-\sqrt{r/(\pi t)}e^{-rt}\), it is the Gamma shape-\(1/2\), rate-\(r\) survival function. Integrating that survival function gives the mean \(1/(2r)\). The equality \(\lambda\sigma=\sqrt{2r}\) explains exactly why the diffusion scale disappears.

**4. Exact complete-reset benchmark.** When \(C=B=0\) almost surely, the stationary law is exactly the Laplace innovation \(\xi_0\). Conditioning \(Z_0>u\) for any \(u\ge0\) produces an *exact* independent exponential overshoot by the Laplace memoryless tail. Any reset maps the position to zero, which is at or below \(u\). Thus \(\tau_u=\min(S,H_{V_u})\) exactly, and Step 3 proves the Gamma-half law for every such \(u\).

## Verification

The standalone `verify.py` uses only the Python 3 standard library. It checks exact-rational partial-fraction and moment identities for finite Laplace perpetuities at several contraction factors; their high-level tail asymptotics; a numerical evaluation of the independent Brownian-exit/exponential-overshoot integral against the closed complementary-error-function identity across independent parameters; and the mean of the limiting Gamma law. Run `python verify.py` in the extracted package. Its tests are finite corroborative checks of the constants, not replacements for the infinite proof.

## Relationship to prior work

Palmowski and Vlasiou (2026) establish general reset-process ergodicity and stationary distribution transforms, including Brownian affine resets. Their Theorem 2.1 and Section 2.6 supply the stationary fixed-point representation used in Step 1, but the inspected sections concern stationary distributions and moments, not a conditional downward exit after a rare stationary exceedance. Di Bello and collaborators (2023) provide exact time-dependent and stationary densities for partial resetting, not this high-threshold duration law. Kolb and Wübker (2026) study long-horizon conditioning on remaining positive from a fixed initial position and the resulting Doob-transformed process; the asymptotic parameter in the present theorem is instead the *initial stationary height* conditioned above a diverging threshold, with a finite-time exit clock. The results are not implications of one another merely from having a first-passage event.

Previously published sharp stationary-tail and conditional extreme-reset-age results (listed below) were compared at the level of conditioning and target variables: a weak-contraction double-scaling tail probability, a shared-reset multiparticle joint tail, and a hidden phase/age law for Gamma-reset finite-speed return systems do not determine the conditional one-coordinate **time to cross downward from an initially rare level** under bounded random affine resetting. Singh and Pal (2022) establish first-passage Brownian functionals for a process reset to a fixed *positive* state and absorbed at a fixed zero boundary, with fixed initial position. Their first-passage kernel covers the Brownian hitting ingredient and can reproduce the elementary complete-reset benchmark after specialization, but it does not imply the uniform contraction limit for a random affine reset map when the absorbing threshold is itself the rare stationary starting height. The classical reflection principle and exponential-mixture identity are standard tools, not claimed as discoveries. A more general pre-existing theorem on rare-level clusters or conditioned excursion lifetimes could imply this specialization; publication priority is not independently certified.

## Limitations

Strict uniform contraction and bounded reset shifts matter: sufficiently heavy-tailed shifts can dominate the exponential Brownian innovation, while noncontractive maps need not have the same stationary tail or immediate-reset exit mechanism. There is no claim of uniformity as \(c_*\uparrow1\), \(r\downarrow0\), \(\sigma\downarrow0\), or in the threshold when parameters change. The theorem does not identify the whole excursion *before* the observation time, the number of subsequent resets, or the asymptotics of conditional moments of the unscaled finite-threshold exit time. Distributional convergence alone does not establish convergence of means. No independent mathematical assessment or comprehensive publication-priority certification has been performed.

## References

1. Z. Palmowski and M. Vlasiou, *Steady-state of Lévy process with general resetting: unreflected and reflected cases*, arXiv:2611.14692v1 (first publicly posted 2026-11-10), Sections 2.2–2.6. https://arxiv.org/html/2611.14692v1
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722v1 (first publicly posted 2023-05-23). https://arxiv.org/abs/2305.13722
3. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, *Bulletin of the London Mathematical Society* **58** (2026), e70314 (published online 2026-03-05). https://doi.org/10.1112/blms.70314
4. *Sharp weak-partial-reset stationary tails with a dilogarithmic rate and boundary prefactor*, published mathematical finding, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-weak-partial-reset-stationary-tails-with-a-dilogarithmic-r--3e4e01201dc0
5. *Universal hidden-phase and Gaussian age laws for extreme Gamma-reset diffusion with finite-speed returns*, published mathematical finding, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-universal-hidden-phase-and-gaussian-age-laws-for-extreme-gamma-r--5c356dfeaeaf
6. *Multivariate Pareto excursions and a Gamma reset-age law in a first-passage-resetting Brownian gas*, published mathematical finding, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-multivariate-pareto-excursions-and-a-gamma-reset-age-law-in-a-fi--c03a80e1262c
7. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715v1 (2022). https://arxiv.org/abs/2202.02715
