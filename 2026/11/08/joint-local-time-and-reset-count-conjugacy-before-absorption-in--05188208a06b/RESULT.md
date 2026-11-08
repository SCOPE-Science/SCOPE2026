# Joint local-time and reset-count conjugacy before absorption in one-dimensional diffusion

## Finding

Let a regular one-dimensional diffusion be absorbed at the left endpoint and restarted at its initial interior point after each independent exponential reset. The occupation-density local time at that very reset point and the number of resets before absorption have a universal joint distribution. In the notation below, for every \(s\geq0\) and \(z\in[0,1]\),

\[
\boxed{\mathbb E_a[e^{-sL}z^N]=\frac{h}{1+sG-(1-h)z}.}
\]

Equivalently, for every integer \(n\geq0\) and \(\ell>0\),

\[
\boxed{\Pr\{N=n,L\in d\ell\}=\frac{h}{G}e^{-\ell/G}\frac{((1-h)\ell/G)^n}{n!}\,d\ell.}
\]

Consequently \(N\) is geometric with success parameter \(h\); \(L\mid\{N=n\}\) is Gamma with shape \(n+1\) and scale \(G\); \(L\) is exponential with scale \(G/h\); and

\[
\boxed{N\mid\{L=\ell\}\sim\operatorname{Poisson}\!\left(\frac{1-h}{G}\ell\right),\qquad \operatorname{Corr}(N,L)=\sqrt{1-h}.}
\]

The conditional Poisson law and correlation hold for the complete accumulated local time, not for a finite observation time or a single excursion.

## Assumptions and scope

Take \(a>0\), \(D>0\), and \(r>0\). Between resets the particle follows a nonexplosive regular diffusion \(dX_t=b(X_t)\,dt+\sqrt{2D}\,dB_t\) on \((0,\infty)\), killed at its first hitting time \(\tau_0\) of zero. Assume the killed semigroup has a jointly continuous transition density \(p_t^{(0)}(x,y)\), the occupation-density local time exists at \(a\), and the resolvent quantities below satisfy \(0<h<1\) and \(0<G<\infty\). Sufficient standard conditions include locally Lipschitz drift, nonexplosion, regular accessibility of zero, and a finite discounted diagonal Green density.

Set

\[
h=\mathbb E_a[e^{-r\tau_0};\tau_0<\infty],\qquad
G=\int_0^\infty e^{-rt}p_t^{(0)}(a,a)\,dt.
\]

Reset intervals are independent exponential random variables of rate \(r\), independent of all diffusive Brownian drivers; a reset instantaneously relocates the particle to the same position \(a\). The experiment stops at the first absorption. Let \(N\in\{0,1,\ldots\}\) count only actual resets strictly before absorption. Define the accumulated occupation-density local time by

\[
L=\lim_{\varepsilon\downarrow0}\frac{1}{2\varepsilon}
\int_0^{T_{\rm abs}}\mathbf1_{\{|X_t-a|<\varepsilon\}}\,dt,
\]

with the usual continuous local-time version on each diffusion segment; reset instants contribute zero ordinary time. The theorem starts at \(a\). The result is not asserted for random reset positions, non-Poisson clocks, sticky boundaries, or local time at a point distinct from the reset location.

## Proof

**1. One segment and its terminal event.** Let \(R\sim\operatorname{Exp}(r)\) be independent of the diffusion and let \(S=\tau_0\wedge R\). Let \(J\) be the segment's terminal type: success \(J=0\) if \(\tau_0<R\), and reset \(J=1\) otherwise. Then \(\Pr(J=0)=h\), \(\Pr(J=1)=1-h\), and both probabilities are strictly positive. Write \(\Lambda\) for the local time at \(a\) accrued before \(S\).

**2. The terminal-event Kac identity.** For \(j\in\{0,1\}\), write \(p_j=\Pr_a(J=j)\). For every integer \(m\ge1\), the ordered-time form of the Kac local-time moment formula and the strong Markov property give

\[
\begin{aligned}
\mathbb E_a[\Lambda^m\mathbf1_{\{J=j\}}]
&=m!\int_{0<t_1<\cdots<t_m<\infty}
\Pr_a\big(X_{t_1}\in da,\ldots,X_{t_m}\in da,\,t_m<S\big)
\Pr_a(J=j)\\
&=m!\,p_j\left(\int_0^\infty e^{-rt}p_t^{(0)}(a,a)\,dt\right)^m
=m!\,p_jG^m.
\end{aligned}
\]

Here the symbolic \(da\) factors mean occupation-density evaluation at \(a\), not probabilities of a single-point event. More formally the first equality follows by regularizing \(\delta_a\) with \((2\varepsilon)^{-1}\mathbf1_{(a-\varepsilon,a+\varepsilon)}\), applying the semigroup Markov property, and passing to the local-time limit. The waiting-time factors multiply to \(e^{-rt_m}\), which is why each ordered interval contributes the same discounted Green factor. At the last visit the probability of terminal type \(j\) is \(p_j\), independently of prior visits, by exponential-clock memorylessness.

For \(m=0\) the same identity is \(\Pr(J=j)=p_j\). These are the moments of an exponential random variable of mean \(G\) multiplied by \(p_j\). Because the exponential distribution is moment-determinate (indeed has a moment-generating function near zero),

\[
\mathbb E[e^{-s\Lambda};J=j]=\frac{p_j}{1+sG},\qquad s\ge0.
\]

In particular \(\Lambda\sim\operatorname{Exp}(\text{scale }G)\) and is independent of \(J\). This independence, rather than merely the exponential marginal, is the key structural step.

**3. Renewal decomposition.** By the strong Markov property, all segments beginning at \(a\) are independent identically distributed copies of \((\Lambda,J)\). The process ends at its first success; thus \(N\) is the number of failure segments before a success, with probabilities \(h(1-h)^n\). The completed trajectory contains \(N+1\) independent segment local times. Independence of \(\Lambda\) from \(J\) implies their conditional sum given \(N=n\) is Gamma with shape \(n+1\) and scale \(G\).

Equivalently, summing the geometric series of Laplace/probability-generating transforms yields

\[
\sum_{n=0}^\infty z^n\left(\frac{1-h}{1+sG}\right)^n\frac{h}{1+sG}
=\frac{h}{1+sG-(1-h)z}.
\]

Inverting the gamma transform produces the displayed joint density. Summing the density over \(n\) gives \(\Pr(L\in d\ell)=(h/G)e^{-h\ell/G}\,d\ell\). Dividing the joint density by this marginal yields the conditional Poisson law.

**4. Correlation.** The geometric and exponential marginals give

\[
\begin{aligned}
\mathbb E N&=\frac{1-h}{h},&\operatorname{Var}(N)&=\frac{1-h}{h^2},\\
\mathbb E L&=\frac Gh,&\operatorname{Var}(L)&=\frac{G^2}{h^2}.
\end{aligned}
\]

Moreover \(\mathbb E[N\mid L]=(1-h)L/G\), so \(\operatorname{Cov}(N,L)=(1-h)G/h^2\) and \(\operatorname{Corr}(N,L)=\sqrt{1-h}\), strictly between zero and one.

**5. Physical specializations.** For free Brownian diffusion, put \(k=\sqrt{r/D}\). Standard killed half-line resolvents give

\[
h=e^{-ka},\qquad G=\frac{1-e^{-2ka}}{2Dk},\qquad
\frac{1-h}{G}=\frac{2Dk}{1+e^{-ka}}.
\]

For the killed Ornstein–Uhlenbeck diffusion \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dB_t\) with \(\kappa>0\), the hitting transform and image kernel give

\[
h=\frac{e^{\kappa a^2/(4D)}D_{-r/\kappa}(a\sqrt{\kappa/D})}{D_{-r/\kappa}(0)},
\]

\[
G=\int_0^\infty\frac{e^{-rt}}{\sqrt{2\pi v_t}}\left[
\exp\left(-\frac{a^2(1-e^{-\kappa t})^2}{2v_t}\right)-
\exp\left(-\frac{a^2(1+e^{-\kappa t})^2}{2v_t}\right)
\right]dt,\quad v_t=\frac D\kappa(1-e^{-2\kappa t}),
\]

where \(D_\nu\) denotes the parabolic-cylinder function. For \((D,\kappa,r,a)=(1,0.9,0.7,1)\), independent quadrature gives \(h\simeq0.599800082553\), \(G\simeq0.504146804919\), conditional reset-count intensity per unit local time \(\simeq0.793816232775\), and correlation \(\simeq0.632613560910\).

## Verification

The self-contained script `verify.py` evaluates the same joint transform by **two distinct constructions** on discretized killed Ornstein–Uhlenbeck chains: (i) independent killed absorption/diagonal Green resolvents and (ii) direct solutions of a backward equation with a point occupation penalty and reset-count weight. It covers three coefficient sets and twenty-five transform pairs per set, checks the Brownian closed forms and integrates the killed OU image heat kernel independently of its hitting-function formula. Running `python verify.py` in an environment with NumPy and SciPy yields 462 successful deterministic assertions. This is a diagnostic consistency test, **not** a proof of the continuum or infinite-dimensional assertion. The mathematical proof is in the four steps above.

## Relationship to prior work

Dubey and Pal (2023) study first-passage local time, residence time and first-passage time of an Ornstein–Uhlenbeck diffusion with resets; their accessible manuscript's Sections 2–3 supply the same physical setup and the marginal local-time transform, but do not state a bivariate reset-count/local-time law. Singh and Pal (2022), Sections 2–3, give the Brownian first-passage local-time marginal and Feynman–Kac framework. Pal, Chatterjee, Reuveni and Kundu (2019), Sections III–IV, analyze local time accumulated up to a **fixed** observation time (often conditioned on survival), not the reset-count-conditioned first-absorption observable. Toledo-Marin and Boyer (2022) analyze mean reset counts in models with random reset positions. The new object here is the exact joint law, its conditional Poisson/Gamma conjugacy and drift-independent correlation identity for general regular diffusions.

Kac's formula, the strong Markov property and one-dimensional Green kernels are standard tools and are not claimed as novel. The result may be derivable from older excursion-theoretic marked-Poisson process identities, and priority against unindexed general results has not been independently established. A related first-absorption maximum/reset-count joint result concerns a different trajectory functional and does not imply this one.

## Limitations

The conditional Poisson statement requires reset *to the same point* where occupation local time is measured, a memoryless external reset clock, and independent fresh diffusion segments. The initial location must equal that reset point. The model has a nonsticky, absorbing boundary and a finite killed resolvent. No corresponding claim is made for renewal clocks, spatially distributed resets, local-time-dependent reset hazards, sticky diffusions, or joint distributions with absorption time. Numerical checks validate finite approximations only. Publication-priority comparison remains qualified by the possibility of general excursion-theory coverage.

## References

1. A. Dubey and A. Pal, *First-passage functionals for Ornstein Uhlenbeck process with stochastic resetting*, arXiv:2304.05226, first posted 2023-04-11. https://arxiv.org/abs/2304.05226
2. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715, first posted 2022-02-06. https://arxiv.org/abs/2202.02715
3. A. Pal, R. Chatterjee, S. Reuveni and A. Kundu, *Local time of diffusion with stochastic resetting*, arXiv:1902.00907, first posted 2019-02-03. https://arxiv.org/abs/1902.00907
4. J. Q. Toledo-Marin and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387, first posted 2022-06-29. https://arxiv.org/abs/2206.14387
