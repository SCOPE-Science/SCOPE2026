# Three exact marginal logarithmic transport laws in power-law-reset exclusion dynamics

## Finding

**Theorem (critical resetting currents).** For the infinite-volume symmetric simple exclusion process with the step state and Pareto renewal resetting defined below, let \(D_\alpha(t)\) be the expected signed number of particle hops across the step bond from left to right, accumulated over all excursions up to time \(t\); let \(N_\alpha(t)\) be the expected *net* current across that bond, including changes induced by resetting. For every fixed \(t_0>0\), the three marginal values satisfy

\[
\begin{aligned}
D_{1/2}(t)&\sim \frac{\sqrt t}{\pi^{3/2}}\log(t/t_0),\\[3pt]
D_1(t)&\sim\frac{G(t_0)}{t_0}\frac{t}{\log(t/t_0)},\\[3pt]
N_{3/2}(t)&\sim \frac{\sqrt{t_0}}{3\sqrt\pi}\log(t/t_0),\qquad t\longrightarrow\infty,
\end{aligned}
\]

where \(G(t_0)\) is the strictly positive finite constant
\[
G(t_0)=\int_0^{t_0}e^{-2a}I_0(2a)\,da+t_0\int_{t_0}^{\infty}\frac{e^{-2a}I_0(2a)}{a}\,da.
\]
In particular, neither a pure square-root law at the first boundary, nor a pure linear law at the second, nor convergence to a finite current at the third describes the corresponding marginal asymptotic. The three statements are one classification of logarithmic boundary terms in the same renewal-transport phase diagram.

## Assumptions and scope

Take continuous-time symmetric simple exclusion on \(\mathbb Z\), with attempted jumps independently at rate one in each direction, suppressed if the destination is occupied. Initially all \(x\le0\) are occupied and all \(x\ge1\) are empty. At each independent renewal time the entire configuration is instantaneously restored to this step. The i.i.d. waiting times have density
\[
\psi_\alpha(a)=\alpha t_0^\alpha a^{-1-\alpha}\mathbf1_{\{a\ge t_0\}},\quad
q_\alpha(a)=\mathbb P(\tau>a)=\begin{cases}1,&0\le a<t_0,\\(t_0/a)^\alpha,&a\ge t_0.\end{cases}
\]
The renewal clock is independent of the exclusion dynamics. The signed hopping current counts left-to-right crossings as positive and right-to-left as negative; the net current also counts reset-induced backward transport. The thermodynamic infinite-volume system is defined before the long-time limit. The formula concerns expectations, not fluctuation distributions.

Write \(j_0(a)\) and \(J_0(a)\) for the no-reset instantaneous mean current and accumulated mean current. Their exact values for this normalization are
\[
j_0(a)=e^{-2a}I_0(2a),\qquad
J_0(a)=a e^{-2a}\bigl[I_0(2a)+I_1(2a)\bigr]=\int_0^a j_0(s)\,ds.
\]
Thus \(j_0(a)\sim 1/(2\sqrt{\pi a})\) and \(J_0(a)\sim\sqrt{a/\pi}\). For example, \(G(1)=1.103030746080\ldots\).

## Proof

**1. Exact no-reset current.** The one-point occupation equation of symmetric exclusion is the discrete heat equation. Starting from the step, its occupation difference across \((0,1)\) is the probability that a continuous-time symmetric random walk starting at zero is at zero at time \(a\), namely \(j_0(a)=e^{-2a}I_0(2a)\). Direct differentiation of the displayed Bessel identity gives \(J'_0=j_0\), with \(J_0(0)=0\). Standard large-positive-argument asymptotics of the modified Bessel functions give the two equivalent square-root estimates.

**2. Renewal identities.** Define the renewal measure \(U=\sum_{n\ge0}\psi_\alpha^{*n}\), including the atom at zero. The law of the age since the last reset implies that the mean instantaneous *hopping* current is the convolution \(U*(q_\alpha j_0)\). Since its expectation is nonnegative, \(D_\alpha(t)\) is nondecreasing. The net current is the signed displacement since the last reset (prior net displacement is canceled by the reset) and hence \(N_\alpha=U*(q_\alpha J_0)\). Letting hats denote Laplace transforms and using \(1-\widehat\psi_\alpha(s)=s\widehat q_\alpha(s)\), we obtain the **exact** formulas, for every \(s>0\),
\[
\widehat D_\alpha(s)=\frac{\widehat{q_\alpha j_0}(s)}{s(1-\widehat\psi_\alpha(s))},\qquad
\widehat N_\alpha(s)=\frac{\widehat{q_\alpha J_0}(s)}{1-\widehat\psi_\alpha(s)}.
\]
These identities also follow directly by conditioning on all completed reset intervals and the last incomplete interval, without a stationarity assumption.

**3. First marginal exponent.** At \(\alpha=1/2\),
\[
q_{1/2}(a)j_0(a)\sim\frac{\sqrt{t_0}}{2\sqrt\pi}\frac1a,\qquad
\widehat q_{1/2}(s)\sim\sqrt{\pi t_0}\,s^{-1/2}.
\]
Positivity and integration yield \(\widehat{q_{1/2}j_0}(s)\sim\sqrt{t_0}\log(1/(st_0))/(2\sqrt\pi)\) and \(1-\widehat\psi_{1/2}(s)\sim\sqrt{\pi t_0}\sqrt s\). Thus
\[
\widehat D_{1/2}(s)\sim\frac1{2\pi}s^{-3/2}\log(1/(st_0)).
\]
The monotone form of Karamata's Tauberian theorem (applicable because \(D_{1/2}\) is nondecreasing) gives \(D_{1/2}(t)\sim [2\pi\Gamma(3/2)]^{-1}\sqrt t\log(t/t_0)=\pi^{-3/2}\sqrt t\log(t/t_0)\).

**4. Second marginal exponent.** At \(\alpha=1\), \(q_1j_0\) is integrable on \([0,\infty)\), with integral \(G(t_0)\). Meanwhile \(\widehat q_1(s)\sim t_0\log(1/(st_0))\). Consequently,
\[
\widehat D_1(s)\sim\frac{G(t_0)}{t_0s^2\log(1/(st_0))}.
\]
Monotonicity and the same Tauberian theorem imply \(D_1(t)\sim [G(t_0)/t_0]t/\log(t/t_0)\).

**5. Third marginal exponent, without a false monotonicity step.** At \(\alpha=3/2\), the renewal waiting time has mean \(\mu=3t_0\). The nonnegative kernel \(h(a)=q_{3/2}(a)J_0(a)\) obeys
\[
h(a)\sim \frac{t_0^{3/2}}{\sqrt\pi}\frac1a,
\quad\int_0^t h(a)\,da\sim\frac{t_0^{3/2}}{\sqrt\pi}\log(t/t_0).
\]
The continuous nonlattice renewal density \(u(t)=\sum_{n\ge1}\psi_{3/2}^{*n}(t)\) satisfies \(u(t)\to1/\mu\). In the convolution \(N_{3/2}(t)=h(t)+\int_0^t u(t-a)h(a)\,da\), fix \(T>0\) such that \(|u(v)-1/\mu|\le\epsilon\) for \(v\ge T\). On \(a\le t-T\), the integral differs from \(\mu^{-1}\int_0^{t-T}h(a)\,da\) by at most \(\epsilon\int_0^t h(a)\,da\). On \(a\in[t-T,t]\), \(h(a)=O(1/t)\) and the renewal measure on the remaining compact interval has finite mass, making that piece \(O(1/t)\). The initial term \(h(t)=O(1/t)\) also vanishes. Divide by \(\log(t/t_0)\), then let \(t\to\infty\) and \(\epsilon\downarrow0\). This gives \(N_{3/2}(t)\sim t_0^{3/2}(3t_0\sqrt\pi)^{-1}\log(t/t_0)\). **No monotonicity of net current is assumed**; it can fall after a reset. The finite-mean renewal-density limit holds here because \(\psi_{3/2}\) is bounded, absolutely continuous, nonlattice, and directly Riemann integrable (the standard renewal-density theorem).

## Verification

The accompanying `verify.py` uses the independent Bessel integral identity, direct quadratures of \(q_\alpha\), and the exact Laplace-domain renewal expressions at all three boundary indices. It passed 29 numerical identities and marginal-coefficient comparisons with SciPy. For \(t_0=1\), the Laplace leading-coefficient ratios at \(s=10^{-7}\) are approximately \(1.08434\), \(0.97416\), and \(0.99489\) for the three cases, respectively; slow logarithmic convergence is expected. The proof rests on the analytic renewal and Tauberian arguments, **not** on these finite computations. Reproduce with `python verify.py` after installing SciPy.

## Relationship to prior work

Mishra and Basu (2022, arXiv:2211.14120v1) introduced precisely this Pareto-reset SEP model and computed the no-reset current, general renewal identities, and phase-diagram exponents. Their main current laws in Sections 5–6 and the small-\(s\) analysis in Appendix A address open intervals, while the diagrams give pure-power labels at the three included boundaries. The present theorem supplies the three missing sharp marginal asymptotics and their constants; in particular, the boundary behavior cannot be obtained by substituting a critical index into the off-critical formula. The general renewal transforms in that paper are a fundamental input and make the correction derivable in principle; they do not themselves state or imply a *pure-power* asymptotic at a singular marginal index. Basu, Kundu and Pal (2019, arXiv:1906.11801) treat exponential (Poisson) resetting and do not have these Pareto critical exponents. Masó-Puigdellosas, Campos and Méndez (2022, arXiv:2205.01613) analyze backward/forward age laws under power-law resetting; they furnish related renewal tools but not these exclusion-current constants.

## Limitations

The result concerns only three mean-current marginal indices for the specified pure-Pareto renewal law, and presumes infinite volume before long time. Finite rings exhibit an additional finite-size crossover. It makes no statements about variance, current distributions, general waiting-time slowly varying factors, or almost-sure transport. No independent scientific audit has been performed. Although a detailed comparison of highly relevant sources was conducted, further equivalent formulations in the broader resetting literature may affect priority.

## References

1. S. Mishra and U. Basu, *Symmetric Exclusion Process under Stochastic Power-law Resetting*, arXiv:2211.14120v1 (first posted 2022-11-25), https://arxiv.org/abs/2211.14120; model Section 2, currents Sections 5–6, Appendix A.
2. U. Basu, A. Kundu, and A. Pal, *Symmetric Exclusion Process under Stochastic Resetting*, arXiv:1906.11801 (2019), https://arxiv.org/abs/1906.11801.
3. A. Masó-Puigdellosas, D. Campos, and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613 (2022), https://arxiv.org/abs/2205.01613.
4. Standard monotone Tauberian theorem for Laplace transforms of regularly varying functions; standard renewal density theorem for absolutely continuous nonlattice interarrival laws (used with conditions verified in the proof).
