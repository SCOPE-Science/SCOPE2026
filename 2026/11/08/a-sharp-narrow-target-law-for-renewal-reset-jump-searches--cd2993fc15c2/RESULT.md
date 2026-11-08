# A sharp narrow-target law for renewal-reset jump searches

## Finding

In a continuous-time random walk made of **instantaneous** jumps with independent competing jump/reset clocks, a target consisting of a point away from the reset origin is never hit if jump lengths have a continuous density. Nevertheless, a small absorbing interval has a universal, quantitatively sharp capture law.

Write \(p=\Pr(T_d<T_s)\), \(q=1-p\), \(m=\mathbb E\min(T_d,T_s)\), and let \(f\) be the jump-length density. For \(a\ne0\) define
\[
G(a)=\sum_{n=1}^{\infty}p^n f^{*n}(a),\qquad \pi_c(a)=qG(a).
\]
If \(0<m<\infty\) and \(G(a)>0\), then for first **landing** in \(I_\varepsilon=(a-\varepsilon,a+\varepsilon)\), with \(0<\varepsilon<|a|\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\mathbb E\tau_\varepsilon=\frac{m}{2\pi_c(a)},\qquad
\frac{2\varepsilon\pi_c(a)}m\tau_\varepsilon\ \Longrightarrow\ \mathrm{Exp}(1).}
\]
The coefficient is the reciprocal of twice the *continuous part* of the time-stationary occupation density, multiplied by the mean event time. It applies even when the time until a jump and the time until a reset individually have infinite mean.

For independent clocks with Pareto survival functions \(\Pr(T_d>t)=(1+t)^{-\alpha}\), \(\Pr(T_s>t)=(1+t)^{-\beta}\), \(\alpha,\beta>0\), and Gaussian jump lengths, the mean first interval-landing time is finite for every fixed \(0<\varepsilon<|a|\) **if and only if** \(\alpha+\beta>1\). In the finite-mean regime,
\[
q=\frac\beta{\alpha+\beta},\quad p=\frac\alpha{\alpha+\beta},\quad
m=\frac1{\alpha+\beta-1},\quad
\pi_c(a)=q\sum_{n\ge1}\frac{p^n}{\sqrt{2\pi n\sigma^2}}
\exp\!\left(-\frac{a^2}{2n\sigma^2}\right).
\]

## Assumptions and scope

At each event, draw a fresh i.i.d. pair \((T_d,T_s)\) of independent, positive, almost surely finite, atomless competing times, independent of all positions and jump lengths; ties have probability zero. The next event occurs after \(T=\min(T_d,T_s)\). If the jump clock wins, add an independent increment with probability density \(f\); otherwise instantaneously reset to 0. The process starts at 0. Assume \(0<p,q<1\). The jump increments are independent and identically distributed, have a bounded Lebesgue density \(f\), and their convolution densities are continuous at a fixed \(a\ne0\), with \(G(a)>0\). These assumptions hold for all nondegenerate Gaussian jumps and, away from the origin, for the symmetric Laplace density. An interval is detected upon an actual jump landing inside it, **not** when a straight segment drawn between jump locations crosses it. The reset at zero is outside the interval. A point target has exactly zero landing probability.

The result concerns a single starting location and each fixed pair of clock laws; it does not assert uniformity in model parameters, crossing detection, finite absorption by spatially continuous Brownian trajectories, or full process limit theorems for heavy-tailed residence times.

## Proof

**1. Independent reset-delimited excursions and their length.** Label a jump event \(J\) and reset event \(R\). Their unconditional probabilities are \(p\) and \(q\), respectively. Between resets, the count \(N\) of jumps has \(\Pr(N\ge n)=p^n\), for \(n\ge1\). The count of all events through the terminal reset is geometric with mean \(1/q\). The i.i.d. event times \(T_i=\min(T_{d,i},T_{s,i})\) may be dependent on event types, but the stopping index \(N+1\) is a stopping time for the successive i.i.d. pairs of duration/type marks. Wald's identity for nonnegative i.i.d. durations yields mean excursion duration \(\mathbb EC=m/q\) if \(m<\infty\). All excursions, including all jump lengths, are i.i.d.

**2. Rare capture probability.** Let \(S_n=\xi_1+\cdots+\xi_n\), where the \(\xi_j\) have density \(f\), and let \(H_\varepsilon\) mean that at least one jump in the first excursion lands in \(I_\varepsilon\). Its union bound has exact sum
\[
U_\varepsilon=\sum_{n\ge1}p^n\Pr(S_n\in I_\varepsilon).
\]
Put \(M=\|f\|_\infty\). Since convolution with a probability density does not increase the \(L^\infty\)-norm, every \(f^{*n}\) is bounded by \(M\). For \(n<k\), independence of the intervening increments implies
\[
\Pr(S_n\in I_\varepsilon,S_k\in I_\varepsilon)
\le(2\varepsilon M)^2.
\]
Indeed the first landing has probability at most \(2\varepsilon M\); conditioning on \(S_n\), the probability that the independent displacement \(S_k-S_n\) takes the particle into that interval is also at most \(2\varepsilon M\). Thus second-order Bonferroni bounds give
\[
0\le U_\varepsilon-\Pr(H_\varepsilon)
\le(2\varepsilon M)^2\sum_{k\ge2}(k-1)p^k
=\frac{(2\varepsilon M)^2p^2}{q^2}.
\]
Continuity at \(a\), combined with dominated convergence in the geometric sum, gives \(U_\varepsilon/(2\varepsilon)\to G(a)\). Hence the excursion success probability \(h_\varepsilon=\Pr(H_\varepsilon)\) obeys
\[
h_\varepsilon=2\varepsilon G(a)+o(\varepsilon),
\]
and is positive for sufficiently small \(\varepsilon\). For every fixed width in the Gaussian case it is positive because the first jump can land in the interval.

**3. Mean capture time.** Define \(D_\varepsilon\) as the time spent in an excursion, stopped at its first successful landing or at the terminal reset, whichever happens first. The strong-reset renewal equation yields
\[
\mathbb E\tau_\varepsilon
=\frac{\mathbb ED_\varepsilon}{h_\varepsilon}.
\]
For almost every finite excursion, none of its finitely many continuous jump positions equals \(a\). Consequently \(D_\varepsilon\to C\) almost surely as \(\varepsilon\downarrow0\); also \(0\le D_\varepsilon\le C\). Dominated convergence yields \(\mathbb ED_\varepsilon\to m/q\). Substitution gives the claimed sharp mean coefficient.

**4. Exponential rare-event limit.** The excursions before the first success are i.i.d. failed excursions. For \(s\ge0\), set \(u_\varepsilon=s h_\varepsilon/\mathbb EC\). Independence across excursions gives
\[
\mathbb E e^{-u_\varepsilon\tau_\varepsilon}
=\frac{\mathbb E[e^{-u_\varepsilon D_\varepsilon}\mathbf1_{H_\varepsilon}]}{1-\mathbb E[e^{-u_\varepsilon C}\mathbf1_{H_\varepsilon^c}]}.
\]
Since \(\mathbf1_{H_\varepsilon}\to0\) almost surely and \(\mathbb EC<\infty\), dominated convergence shows that the numerator divided by \(h_\varepsilon\) tends to 1. For the denominator, \(\mathbb E[C\mathbf1_{H_\varepsilon^c}]\to\mathbb EC\); applying \((1-e^{-uC})/u\le C\) and dominated convergence gives denominator divided by \(h_\varepsilon\) tending to \(1+s\). The Laplace transform tends to \((1+s)^{-1}\), proving \(h_\varepsilon\tau_\varepsilon/\mathbb EC\Rightarrow\mathrm{Exp}(1)\). Use the asymptotic for \(h_\varepsilon\) and \(\mathbb EC=m/q\) to obtain the displayed normalization.

**5. Polarity and the infinite-mean boundary.** Each excursion has finitely many jumps almost surely. There are countably many jump times over the entire walk, and every sum \(S_n\) has a density; hence the probability of ever landing on \(a\ne0\) is zero. If \(\mathbb ET=\infty\), any interval capture time is at least the first waiting period \(T_1\), so its expectation is infinite. If \(\mathbb ET<\infty\) and jump density is positive everywhere, the mean is finite for every fixed \(\varepsilon\) because excursions have positive success probability and finite mean duration. For the two Pareto clocks, the minimum has survival \((1+t)^{-(\alpha+\beta)}\), giving the claimed exact threshold. Integrating the two hazard contributions gives \(p=\alpha/(\alpha+\beta)\) and \(q=\beta/(\alpha+\beta)\).

**6. Interpretation of stationary density.** At event epochs the Markov chain on positions solves the reset/jump equation \(\pi=q\delta_0+p\,\pi*f\). Therefore \(\pi=q\sum_{n\ge0}p^n f^{*n}\), whose continuous density at \(a\ne0\) equals \(qG(a)\). Because the next event duration is independent of the position inherited from the preceding event, this is also the time-stationary occupation law when \(m<\infty\). This identification uses the published stationary renewal transform, but the small-target time law is obtained from the preceding excursion calculation.

## Verification

The standard-library-only script `checker.py` computes the Gaussian-jump geometric convolution coefficient at a specified target, and bounds finite-interval excursion success probabilities between a single-visit sum minus an explicit double-visit correction and the single-visit sum. The geometric-tail remainder is rigorously bounded. Its rational-parameter Pareto cases also check the exponent regimes. The script is a diagnostic; the universal proof is steps 1–6, not extrapolation from tests. Run `python3 checker.py` from the extracted package.

At Gaussian variance \(\sigma^2=1\), symmetric competing exponential clocks of rate 1, and target \(a=1\), the script yields \(\pi_c(1)\approx0.1103771160614431\) and \(\lim_{\varepsilon\downarrow0}\varepsilon\mathbb E\tau_\varepsilon\approx2.264962239644255\).

## Relationship to prior work

Li, Zhang and Liu (2026) define the competing-clock instantaneous-jump process and give its stationary transform (their (63)–(64)); their point-target first-arrival formulas (including (115)–(116)) use diffusion/long-wave approximations for the Gaussian case, rather than the exact landing convention and shrinking positive-width targets. This theorem therefore does not assert that their diffusive interpolations are mathematically erroneous; it isolates the different physical detection convention and computes an exact scaling law for the literal jump model.

The general stochastic-resetting literature treats hitting-time renewal relations, discrete/lattice targets and diffusion with nonzero-size targets. The earlier narrow-capture results for Brownian paths in dimensions 2 and 3 concern continuous-path absorption and produce different small-radius singularities. Their results do not imply this exact one-dimensional *jump-landing* coefficient and its competing-clock Pareto boundary without additional reduction. Standard renewal and rare-event arguments are used openly; no claim of inventing those techniques is made.

## Limitations

The time-stationary density interpretation and exponential scaled-time law require the finite mean of the minimum clock. For infinite-mean competing clocks the first-interval mean is infinite, but no limiting distribution is asserted. The jump density must be bounded and continuous at the target after each convolution; no uniform-in-parameter limit, multiple-target competition, crossing detection, target at the reset origin or multidimensional geometry is covered. A broader unindexed rare-event theorem could subsume the limiting-law component; publication-priority verification is not independent.

## References

1. G. Li, H. Zhang and Y. Liu, *Intermittent continuous-time random walks under renewal reset mechanism*, arXiv:2609.09738, first posted 2026-09-09. https://arxiv.org/abs/2609.09738
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568. https://arxiv.org/abs/1910.13568
3. P. C. Bressloff and R. D. Schumm, *The Narrow Capture Problem with Partially Absorbing Targets and Stochastic Resetting*, Multiscale Modeling & Simulation, DOI:10.1137/21M1449580. https://doi.org/10.1137/21M1449580
4. R. Flaquer-Galmés, D. Campos and V. Méndez, *Intermittent random walks under stochastic resetting*, Phys. Rev. E 109, 034103 (2024). https://doi.org/10.1103/PhysRevE.109.034103
5. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A 53 (2020) 193001. https://arxiv.org/abs/1910.07993
