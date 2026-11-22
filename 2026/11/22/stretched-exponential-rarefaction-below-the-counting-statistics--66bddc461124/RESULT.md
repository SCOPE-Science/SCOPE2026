# Stretched-exponential rarefaction below the counting-statistics hard edge of a first-passage-reset Brownian gas

## Finding

For a finite population of Brownian particles collectively reset whenever *any* coordinate first reaches a fixed positive threshold, the limiting stationary fraction in a shrinking central interval has a strictly positive lower edge. This result determines the previously unresolved **finite-population probability of falling below that edge**, on its sharp logarithmic scale, and identifies the reset age selected by that rare event.

Fix \(\ell>0\) and \(0<\kappa<\operatorname{erf}(\ell)\). Define
\[
u_\kappa=\left(\frac{\ell}{\operatorname{erf}^{-1}(\kappa)}\right)^2>1,
\qquad
A_N^\star=\frac{\sqrt{u_\kappa}}{\sqrt{\pi\log N}}N^{1-1/u_\kappa}.
\]
(Here the symbol \(A_N^\star\) is a deterministic probability-exponent scale, *not* the random renewal age.) Then
\[
\lim_{N\to\infty}\frac{-\log\Pr\{K_N\le\lfloor\kappa N\rfloor\}}{A_N^\star}=1.
\]
If \(\mathcal A_N\) denotes the elapsed time since the last collective reset in the stationary regime, then for every \(\varepsilon>0\),
\[
\Pr\left\{\left|\frac{4D\log N}{L^2}\mathcal A_N-u_\kappa\right|>\varepsilon\ \middle|\ K_N\le\lfloor\kappa N\rfloor\right\}\longrightarrow0.
\]
Thus each fixed subedge density \(\kappa\) has its own nontrivial stretched-exponential power \(1-1/u_\kappa\), and rarefaction is carried by an unusually long surviving excursion rather than by a typical-age binomial fluctuation.

## Assumptions and scope

For every integer \(N>2\), consider \(N\) independent one-dimensional diffusions with generator \(D\partial_x^2\), with \(D>0\), started at zero at each renewal. The entire population resets instantaneously to zero at the first time any coordinate reaches \(L>0\), and repeats with independent fresh Brownian excursions. A finite mean cycle length, hence a stationary occupation law, exists precisely for \(N>2\). We observe a sample from that stationary occupation law. For all sufficiently large \(N\), the test interval
\[
I_N=[-L\ell/\sqrt{\log N},\ L\ell/\sqrt{\log N}]
\]
is strictly inside the absorbing threshold. \(K_N\) counts the sampled coordinates lying in \(I_N\). Constants \(\ell\) and \(\kappa\) do not depend on \(N\) and remain in the stated open range.

## Proof

**Exact equilibrium-age mixture.** Put \(c=L^2/(4D)\), \(b=\log N\), and \(t_u=cu/b\). For a reset-free coordinate the killed heat kernel and survival probability are
\[
G(x,t)=\frac{e^{-x^2/(4Dt)}-e^{-(x-2L)^2/(4Dt)}}{\sqrt{4\pi Dt}}\,\mathbf1_{\{x<L\}},\qquad
S_1(t)=\operatorname{erf}\left(\sqrt{c/t}\right).
\]
The probability that all \(N\) coordinates survive for time \(t\) is \(S_N(t)=S_1(t)^N\). The renewal mean is \(\mu_N=\int_0^\infty S_N(t)\,dt\) and the *stationary* age density is \(S_N(t)/\mu_N\). Conditioned on an age \(t\), positions are independent with common density \(G(x,t)/S_1(t)\). Consequently
\[
K_N\mid\{\mathcal A_N=t\}\sim\operatorname{Bin}(N,p_N(t)),\quad
\Pr(K_N\le k)=\frac1{\mu_N}\int_0^\infty S_N(t)\Pr\{\operatorname{Bin}(N,p_N(t))\le k\}\,dt.
\]
This identity is exact, including the absorptive image term, rather than merely an asymptotic Gaussian approximation.

**Two separate decay mechanisms.** Set \(z=\sqrt{b/u}\) and \(\eta=\ell/\sqrt u\). For large \(N\), direct integration of the killed heat kernel yields
\[
p_N(t_u)=\frac{\operatorname{erf}(\eta)-\tfrac12[\operatorname{erf}(2z+\eta)-\operatorname{erf}(2z-\eta)]}{\operatorname{erf}(z)}.
\]
For any fixed \(U>0\), uniformly for \(0<u\le U\),
\[
p_N(t_u)=h(u)+O\!\left(\frac{N^{-1/U}}{\sqrt b}\right),\qquad h(u)=\operatorname{erf}(\ell/\sqrt u).
\]
Indeed \(\eta/z=\ell/\sqrt b<1\) eventually, so the reflected-image correction is bounded by the Gaussian tail above \(z\), while \(\operatorname{erfc}(z)=O(N^{-1/U}/\sqrt b)\). The function \(h\) is smooth and strictly decreasing, with \(h(u_\kappa)=\kappa\). For fixed \(u>1\), the standard complementary-error-function expansion gives
\[
-\log S_N(t_u)
=N\operatorname{erfc}(\sqrt{b/u})(1+o(1))
=\frac{\sqrt u}{\sqrt{\pi b}}N^{1-1/u}(1+o(1)),
\]
locally uniformly on \(u>1\). In particular this is the claimed exponent at \(u=u_\kappa\). The renewal mean satisfies \(\mu_N\sim c/b\): \(S_N(t_u)\to1\) for \(u<1\) and \(S_N(t_u)\to0\) for \(u>1\), and the tail is uniformly integrable after rescaling, as shown next.

**Uniform age-tail bound.** Since \(S_1(t)\) decreases and \(S_1(t)=O(t^{-1/2})\) at infinity, the fixed constant \(C=\int_c^\infty S_1(t)^4dt\) is finite. For every \(t_0<c\) and \(N\ge5\),
\[
\int_{t_0}^\infty S_N(t)dt\le cS_N(t_0)+C S_1(c)^{N-4}.
\]
This proves both the stated normalization and control of ages beyond any given \(t_u\) with \(u>1\), to logarithmic precision. (For the normalization, one may use any fixed \(u_0<1<u_1\), integrate below \(t_{u_0}\), and bound the rest above \(t_{u_1}\), then send \(u_0,u_1\to1\).)

**Sharp probability sandwich.** Choose \(0<\beta<1/(2u_\kappa)\), put \(\delta_N=N^{-\beta}\), and write \(u_-=u_\kappa-\delta_N\), \(u_+=u_\kappa+\delta_N\), \(u_2=u_\kappa+2\delta_N\). For some constant \(a>0\), the uniform kernel estimate and strict monotonicity of \(h\) ensure
\[
p_N(t_u)\ge\kappa+a\delta_N\quad(0<u\le u_-),\qquad
p_N(t_u)\le\kappa-a\delta_N\quad(u_+\le u\le u_2).
\]
Hoeffding bounds show that the unwanted binomial tail in the first region, and the failure of the desired binomial event in the second region, are at most \(\exp(-c_1N\delta_N^2)\), for a constant \(c_1>0\). Since \(1-2\beta>1-1/u_\kappa\), these errors are negligible compared with \(\exp(-A_N^\star)\).

For the upper bound, split the exact age mixture at \(t_{u_-}\). The young part contributes only the binomial error and the older part is bounded by the age tail estimated above. For the lower bound, restrict the mixture to the interval \([t_{u_+},t_{u_2}]\), where the binomial event has conditional probability tending to one. Its width is \(c\delta_N/b\), and its age density is at least \(S_N(t_{u_2})/\mu_N\). Therefore
\[
-\log \Pr\{K_N\le\lfloor\kappa N\rfloor\}
=A_N^\star(1+o(1)),
\]
because the polynomial-width logarithm is \(O(\log N)=o(A_N^\star)\) and \(\delta_N\log N=o(1)\) makes the ages \(u_-,u_2\) exponentially equivalent at this scale.

**Conditional age localization.** Fix \(\varepsilon>0\) with \(u_\kappa-\varepsilon>0\). Ages with \(u\le u_\kappa-\varepsilon\) have the forbidden count only with probability \(e^{-c_2N}\) (by the same uniform estimate and Chernoff). Ages with \(u\ge u_\kappa+\varepsilon\) cost \(\exp[-N^{1-1/(u_\kappa+\varepsilon)+o(1)}]\) by the survival bound; this is smaller than the total rarefaction probability by a stretched-exponential factor. Division by the preceding probability equivalent proves the asserted conditional concentration. Larger \(\varepsilon\) follow from smaller positive ones.

## Verification

The exact one-dimensional mixture integral was evaluated independently of the limiting calculation using a discretized age quadrature and a numerical binomial cumulative distribution. With \(\ell=1\) and \(\kappa=0.7\), for \(N=100,300,1000,3000,10000\), the respective ratios of the exact numerical \(-\log\Pr\) to \(A_N^\star\) were approximately \(1.32560,1.27930,1.21010,1.14903,1.09281\). The convergence toward one is consistent with the theorem and is *not* used as proof. Standalone reproduction: `python verify.py` (requires NumPy and SciPy). The proof above, not finite numerical tests, establishes the limit for all fixed admissible parameters.

## Relationship to prior work

Biroli, Majumdar and Schehr give the **exact finite-population stationary conditionally independent mixture** and the large-population full-counting-statistics law supported on fractions \(\kappa\ge\operatorname{erf}(\ell)\), specifically their Eqs. (10)–(15), (36)–(38). All those ingredients and the lower support edge are prior work. Their article notes that below-edge rarefaction is very unlikely but does **not** give its finite-size logarithmic rate or the accompanying conditioned-age law. The present proof extracts those two finer statements from the exact mixture rather than reproducing the known limiting density. The earlier general conditional-independence study by Biroli et al. provides a broad framework but does not address the population-dependent first-passage clock or this lower-support rarefaction. Other existing threshold-reset results describe far-left excursions of a fixed collection of coordinates or rare occupancy beyond the opposite physical threshold, not macroscopic deficiency in the shrinking central interval.

## Limitations

The theorem is a *logarithmic probability equivalent*, not a multiplicative probability asymptotic or a full uniform crossover at the support edge. It assumes exactly one positive absorbing trigger level, all coordinates reset together, independent Brownian excursions, and fixed \(0<\kappa<\operatorname{erf}(\ell)\). It does not establish a finite-size prefactor, behavior when \(\kappa\) or \(\ell\) varies with population size, or a quenched dynamical observation-window result. Publication priority relative to inaccessible supplements or unindexed equivalent derivations has not been independently assessed.

## References

- M. Biroli, S. N. Majumdar and G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440 (first public version 29 November 2025), https://arxiv.org/abs/2512.00440; *Europhysics Letters* 153, 31002 (2026). Primary model, exact finite-population mixture, and known large-population counting edge.
- M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, https://arxiv.org/abs/2307.15351, *Physical Review E* 109, 014101 (2024). Generic conditionally independent framework.
- Published research records: *Logarithmic mirror-threshold occupations in a first-passage resetting Brownian gas* (26 October 2026) and *Multivariate Pareto excursions and a Gamma reset-age law in a first-passage-resetting Brownian gas* (2 November 2026), via https://github.com/published-finding corpus/2026 (distinct observables).
