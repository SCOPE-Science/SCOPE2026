# Positive escape probability for every positive maximum-group reset rate in unconfined Brownian search

## Finding
For every integer \(N\ge 2\), initial distance \(x>0\), diffusion coefficient \(D>0\), and collective Poisson reset rate \(r>0\), the first-hit time \(T\) of the absorbing origin by an unconfined group of \(N\) independent one-dimensional Brownian particles has a strictly positive probability of being infinite. At each reset, **all** particles are moved to the current spatial maximum of the group, and the event of absorption is terminal. Consequently \(\mathbb E[T]=+\infty\) for every positive \(r\). This contrasts with the zero-reset case, where absorption occurs almost surely for every finite \(N\), and the mean is finite precisely for \(N\ge3\).

More precisely, put \(\lambda=\sqrt{r/D}\) and \(\delta=(4/\sqrt7-1)/3>0\). The eventual capture probability \(Q_N(x)=\Pr_x(T<\infty)\) satisfies the explicit universal upper bound
\[
Q_N(x)\le \min\!\left\{1,\frac{N}{\delta}e^{-\lambda x/2}\right\}.
\]
For every finite \(r>0\), \(0<\Pr_x(T=\infty)<1\); further,
\[
\lim_{r\downarrow0}\Pr_x(T=\infty)=0,\qquad
\lim_{r\uparrow\infty}\Pr_x(T=\infty)=1.
\]
For \(N=1\), resets are inert: \(\Pr_x(T=\infty)=0\) for all \(r\ge0\), with infinite mean.

## Assumptions and scope
Fix \(N\in\{1,2,\ldots\}\), \(x,D>0\), and \(r\ge0\). Begin with \(N\) particles together at \(x\) on the positive half-line. Between Poisson alarms the particles evolve independently as \(X_i(t)=X_i(0)+\sqrt{2D}W_i(t)\), with independent standard Brownian motions. At each alarm of a rate-\(r\) Poisson process independent of all Brownian motions, provided nobody has yet reached zero, relocate every particle to \(\max_i X_i(t-)\). The first hit of zero by **any** particle ends the experiment; this is the first-group-hitting criterion. No drift, confinement, reflection or post-absorption recycling is assumed. The probability \(\Pr_x\) means all particles initially share position \(x\).

## Proof
Let \(S\sim\operatorname{Exp}(r)\) be the next reset time and \(B_i(s)=\sqrt{2D}W_i(s)\) the independent within-cycle Brownian increments. Let \(H\) denote the first time one of the particles at the common start \(x\) hits zero before a reset. Write \(M_N=\max_i B_i(S)\). For \(r>0\), regeneration at a surviving reset gives the exact equation
\[
Q_N(x)=\Pr_x(H\le S)+\mathbb E\!\left[\mathbf1_{\{S<H\}}Q_N(x+M_N)\right].
\]
This uses the killed process; no independence is assumed between \(S<H\) and \(M_N\). The one-dimensional exponential killing identity and a union bound yield
\[
\Pr_x(H\le S)\le N e^{-\lambda x},\qquad \lambda=\sqrt{r/D}.
\]
Choose \(\kappa=\lambda/2\). Since \(N\ge2\), \(M_N\ge M_2=\max(B_1(S),B_2(S))\) on the same probability space, and so \(\mathbb E e^{-\kappa M_N}\le\mathbb E e^{-\kappa M_2}\). Conditional on \(S=t\), write
\[
M_2=\frac{B_1(t)+B_2(t)}2+\frac{|B_1(t)-B_2(t)|}2.
\]
The two terms on the right are independent, the first normal and the second the absolute value of a normal, each with underlying variance \(Dt\). Consequently
\[
\mathbb E[e^{-\kappa M_2}\mid S=t]
=e^{D\kappa^2t}\operatorname{erfc}\!\left(\kappa\sqrt{Dt/2}\right).
\]
Direct integration against \(r e^{-rt}\), valid for \(0<\kappa<\lambda\), gives
\[
A_2(\kappa):=\mathbb E e^{-\kappa M_2}
=\frac{r}{r-D\kappa^2}\left(1-
\frac{\kappa\sqrt{D/2}}{\sqrt{r-D\kappa^2/2}}\right).
\]
At \(\kappa=\lambda/2\), this becomes \(A_2=(4/3)(1-1/\sqrt7)<1\), so \(\delta:=1-A_2=(4/\sqrt7-1)/3>0\).

Let \(U(x)=(N/\delta)e^{-\kappa x}\) for \(x>0\). Its one-cycle first-capture plus post-reset continuation satisfies
\[
\begin{aligned}
\Pr_x(H\le S)+\mathbb E[\mathbf1_{\{S<H\}}U(x+M_N)]
&\le N e^{-\lambda x}+(N/\delta)e^{-\kappa x}A_2\\
&\le (N/\delta)e^{-\kappa x}(\delta+A_2)=U(x).
\end{aligned}
\]
Starting with the probability of capture before the first alarm and iterating this positive renewal operator, induction bounds capture by any finite reset cycle by \(U\). Any finite absorption happens after finitely many Poisson alarms almost surely; monotone convergence therefore proves \(Q_N(x)\le U(x)\), and \(Q_N(x)\le1\) is automatic.

For arbitrary \(x>0\), choose \(L>0\) so large that \(U(L)<1\). With strictly positive probability, before the first alarm all particles stay strictly positive and the rightmost reaches a point above \(L\) at that alarm (e.g. restrict \(S\) to an interval of positive length and use positivity of killed Brownian transition densities). Conditional on this event, the restarted group has capture probability at most \(U(L)<1\). Thus \(\Pr_x(T=\infty)>0\) from **every** positive start. On the other hand, a particle can reach zero before the first alarm with positive probability, giving \(\Pr_x(T=\infty)<1\). Infinite mean follows from the positive atom at \(+\infty\).

For \(r=0\), independence and the reflection principle give
\[
\Pr_x(T>t)=\operatorname{erf}\!\left(\frac{x}{\sqrt{4Dt}}\right)^N
\sim \left(\frac{x}{\sqrt{\pi D}}\right)^N t^{-N/2}
\quad(t\to\infty).
\]
Hence \(T<\infty\) almost surely, and \(\mathbb E[T]<\infty\) iff \(N>2\). At \(r>0\) with \(N=1\), resets leave the particle in place, so it remains ordinary Brownian motion. Lastly, as \(r\downarrow0\), the probability of eternal survival is no larger than \(\Pr_x(S<H)\to0\) by dominated convergence and almost-sure finite \(H\). As \(r\uparrow\infty\), the explicit exponential bound on \(Q_N(x)\) tends to zero. These limits complete the proof.

## Verification
The standalone file `checker.py` separately integrates the conditional two-particle maximum transform at several parameter values, checks the exact constant and exponential super-solution inequalities, and checks the no-reset algebraic tail. Every step controlling infinite time is analytic; numerical checks are diagnostics rather than substitutes for the renewal-super-solution proof. Run `python checker.py` with Python 3 and installed NumPy, SciPy and SymPy.

## Relationship to prior work
Lee, Yang and Lizana (2026, arXiv:2604.24406, first public April 27, 2026) introduce and simulate the same current-rightmost group-reset rule with an absorbing first-arrival criterion, but apply a **positive harmonic confining potential**; their finite-time censored estimates are not the unconfined \(r>0\) eternal-survival theorem. Lee, Yang, Park and Lizana (2024, arXiv:2412.02524, first public December 3, 2024) develop a framework for group resetting in a potential and an avoidance problem, without the present first-hit zero-confinement dichotomy. Majumdar, Sabhapandit and Schehr (2015, arXiv:1509.04516) reset a **single discrete random walk** to its historical running maximum; that is a different reset operator from collectively resetting multiple Brownian particles to their **current** maximum. Standard Brownian reflection and exponential-killing facts are used and not claimed as new.

## Limitations
The bound on capture is explicit but not sharp. The theorem proves positive nonabsorption and all positive unconditional moments are infinite; it does not determine exact survival probabilities, the conditional-on-absorption distribution, or behavior under nonzero confinement, finite spatial intervals, moving targets, median-group-hitting criteria, interacting particle motion, or random reset clocks other than Poisson. Literature coverage does not establish absolute priority; unindexed equivalent work could exist.

## References
1. Juhee Lee, Seong-Gyu Yang and Ludvig Lizana, *Beyond average: heterogeneous first-passage dynamics in many-particle systems with resetting*, arXiv:2604.24406, first submitted 2026-04-27, https://arxiv.org/abs/2604.24406.
2. Juhee Lee, Seong-Gyu Yang, Hye Jin Park and Ludvig Lizana, *General Theory for Group Resetting with Application to Avoidance*, arXiv:2412.02524, first submitted 2024-12-03, https://arxiv.org/abs/2412.02524.
3. Satya N. Majumdar, Sanjib Sabhapandit and Grégory Schehr, *Random walk with random resetting to the maximum*, arXiv:1509.04516, first submitted 2015-09-15, https://arxiv.org/abs/1509.04516.
4. Classical reflection principle and exponential-time Laplace transform for one-dimensional Brownian first passage.
