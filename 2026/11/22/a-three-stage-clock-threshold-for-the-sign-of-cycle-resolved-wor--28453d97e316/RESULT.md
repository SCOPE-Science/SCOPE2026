# A three-stage clock threshold for the sign of cycle-resolved work memory in a flashing harmonic trap

## Finding

A Brownian particle alternately confined by a harmonic potential and released into free diffusion has a natural signed work increment per complete on–off cycle. Even when each on and off residence time has the **same fixed mean** and every protocol has **the same mean work per cycle**, the covariance of work increments from distinct cycles can change sign. The smallest equal-stage Erlang clock admitting negative successive-cycle covariance has **three stages**.

Precisely, for an integer \(m\ge1\), let consecutive on and off durations be independent \(\operatorname{Gamma}(m,mq)\) random variables, with mean \(1/q\), and put \(x=k/q>0\). Let \(W_n\) be the signed switching work in the stationary cycle-indexed process. There is an exact function \(g_m(x)\), specified below, such that for every integer lag \(j\ge1\),
\[
 \operatorname{Cov}(W_0,W_j)=\frac{D^2x^2}{4}(1-a_m)a_m^{j-1}g_m(x),\qquad a_m=(1+2x/m)^{-m}.
\]
In particular the sign is **identical at every strictly positive cycle lag**. The first three clock shapes have the complete classification
\[
\begin{aligned}
 g_1(x)&=\frac8{2x+1}>0,\\
 g_2(x)&=\frac{15x^2+28x+16}{2(x+1)^3(x+2)}>0,\\
 g_3(x)&=\frac{-8P(x)}{(2x+3)^3(4x^2+18x+27)(16x^2+36x+27)},
\end{aligned}
\]
where
\[
 P(x)=128x^5-720x^4-6480x^3-14094x^2-14580x-6561.
\]
The polynomial \(P\) has exactly one positive zero, \(x_*=11.1415229084657\ldots\), so the three-stage correlations are positive for \(0<x<x_*\), zero at \(x=x_*\), and negative for \(x>x_*\). **Every** finite Erlang shape \(m\ge3\) has positive correlations for sufficiently weak confinement and negative correlations for sufficiently strong confinement; uniqueness is asserted only for \(m=3\). In contrast, for *deterministic* on and off durations both equal to \(1/q\),
\[
 \operatorname{Cov}(W_0,W_j)=2D^2e^{-2xj}\bigl(x^2-\sinh^2 x\bigr)<0
 \qquad(j\ge1,\ x>0).
\]
All these protocols have exactly \(\mathbb EW_n=kD/q\), irrespective of their clock shape.

## Assumptions and scope

Fix \(k,D,q>0\). During a trap-on interval, \(X\) solves \(dX_t=-kX_t\,dt+\sqrt{2D}\,dB_t\); during a trap-off interval, it solves \(dX_t=\sqrt{2D}\,dB_t\). The on and off durations form independent, identically distributed families, are independent of the Brownian noise, and have mean \(1/q\). Either both durations follow \(\operatorname{Gamma}(m,mq)\) for an integer \(m\ge1\), where the second argument is the **rate**, or both durations are deterministically \(1/q\). At every switch the position is continuous.

Let \(U_n\) be the particle position just as the trap turns on for cycle \(n\); let \(V_n\) be its position when that on interval ends. Each full cycle consists of one on interval followed by one off interval. With the potential \(kX^2/2\) in the on state and zero in the off state, the mechanical switching work is
\[
 W_n=\frac{k}{2}(U_n^2-V_n^2).
\]
We use the **unique stationary distribution indexed by the beginnings of on cycles** (Palm/event-indexed stationarity). For deterministic durations this is not the same as initializing laboratory time with a fixed phase; the event-indexed stationary law exists regardless. The covariance is over **cycle index** \(j\), not fixed laboratory-time lag, and is not a covariance of positions. The model has nonzero thermal diffusion in both states.

For the general calculation write \(T\) for a generic on duration, \(S\) for a generic off duration, and define
\[
 a=\mathbb E e^{-2kT},\quad b=\mathbb E e^{-4kT},\quad Q=D/k,\quad L=2D\mathbb ES,\quad H=12D^2\mathbb ES^2.
\]
These parameters satisfy \(0<b<a<1\), \(Q,L>0\), and \(H<\infty\) for every protocol in the theorem. Set
\[
 G=-2Q^2(1-a)+\frac{aL^2(6a-5b-1)}{(1-a)(1-b)}+\frac{H(a-b)}{1-b}.
\]
Then **for all** such on/off clocks with independent durations and finite second off-duration moment,
\[
 \boxed{\operatorname{Cov}(W_0,W_j)=\frac{k^2}{4}(1-a)a^{j-1}G,\quad j\ge1.}
\]
The Erlang statements are its matched-mean specialization: \(a=a_m\), \(b=(1+4x/m)^{-m}\), \(Q=(D/q)/x\), \(L=2D/q\), and \(H=12(D/q)^2(1+1/m)\). Thus \(G=(D/q)^2g_m(x)\).

## Proof

**Existence, Gaussian transitions, and moments.** Let \(T_n,S_n\) be consecutive on and off durations. Conditional on \(T_n\), the exact Ornstein–Uhlenbeck transition is
\[
 V_n=e^{-kT_n}U_n+\xi_n,\qquad \xi_n\mid T_n\sim\mathcal N\!\left(0,Q(1-e^{-2kT_n})\right).
\]
The off transition is \(U_{n+1}=V_n+\eta_n\), with \(\eta_n\mid S_n\sim\mathcal N(0,2DS_n)\). All innovations have the appropriate conditional independence. The resulting affine random recurrence multiplies previous positions by \(e^{-kT_n}\), which contracts strictly in \(L^p\) for every positive \(p\) for which the innovations have finite \(p\)-moments. Both the Erlang and deterministic laws have all needed moments, yielding a unique stationary cycle-indexed distribution with moments of every order.

**Stationary second and fourth moments.** Put \(A=\mathbb EU_n^2\), \(B=\mathbb EV_n^2\), \(U_4=\mathbb EU_n^4\), \(V_4=\mathbb EV_n^4\). The Gaussian transitions give
\[
 B=aA+Q(1-a),\qquad A=B+L,
 \qquad A=Q+\frac{L}{1-a},\quad B=Q+\frac{aL}{1-a}.
\]
Consequently \(\mathbb E W_n=kL/2=kD\mathbb ES\). Using the conditional Gaussian fourth-moment formula gives the exact recursions
\[
\begin{aligned}
 V_4&=bU_4+6Q(a-b)A+3Q^2(1-2a+b),\\
 U_4&=V_4+6LB+H,\\
 \mathbb E(U_n^2V_n^2)&=aU_4+Q(1-a)A.
\end{aligned}
\]
Hence
\[
 U_4=\frac{6Q(a-b)A+3Q^2(1-2a+b)+6LB+H}{1-b}.
\]
Subtracting the relevant products of second moments and simplifying, one obtains the **explicit** identity
\[
 \operatorname{Cov}(U_n^2,V_n^2)-\operatorname{Var}(V_n^2)=G,
\]
with precisely the expression stated above. This is an algebraic identity, not an assumption of Gaussian stationary positions.

**Propagation of cycle-work correlations.** Because the off noise is centered and independent conditional on the current release state, \(\operatorname{Cov}(W_n,U_{n+1}^2)=\operatorname{Cov}(W_n,V_n^2)=kG/2\). Meanwhile
\[
 \mathbb E[U_{n+1}^2\mid U_n]=aU_n^2+Q(1-a)+L,
\qquad
 \mathbb E[W_n\mid U_n]=\frac{k}{2}(1-a)(U_n^2-Q).
\]
Conditional expectation over the future and the stationary affine second-moment map imply
\[
 \operatorname{Cov}(W_0,U_j^2)=a^{j-1}\frac{k}{2}G
\]
for every integer \(j\ge1\). Applying the work conditional mean then proves the boxed universal lag formula. No independence between consecutive cycle works was assumed.

**Exactly three stages are first.** Substituting the Erlang Laplace transforms and the off-duration second moment into \(G\) yields the three rational expressions in the Finding. All their denominators are strictly positive for \(x>0\). The first two numerators are strictly positive. For \(m=3\), the coefficient signs of \(P\), in descending powers, are \((+,-,-,-,-,-)\), so Descartes' sign rule gives *at most one* positive root. Since \(P(0)=-6561<0\) and \(P(x)\to\infty\), exactly one positive root exists. Exact substitution gives \(P(11.141522)<0<P(11.141523)\), certifying its numerical bracket.

For every fixed integer \(m\ge1\), the binomial Taylor expansions of \((1+2x/m)^{-m}\) and \((1+4x/m)^{-m}\) substituted into the displayed \(G\) give
\[
 g_m(x)=\frac8m+O(x)\qquad(x\downarrow0).
\]
For fixed \(m\ge3\) and \(x\to\infty\), both \(a,b=O(x^{-m})\), while \(Q=(D/q)/x\). The last two terms of \(g_m\) are \(o(x^{-2})\), and the first is \(-2x^{-2}(1+o(1))\), so
\[
 x^2g_m(x)\longrightarrow-2\qquad(m\ge3).
\]
Continuity gives at least one zero for each such \(m\). It is not used to infer uniqueness for larger shapes.

**Perfectly periodic clock.** For \(T=S=1/q\), one has \(a=e^{-2x}\), \(b=e^{-4x}\), \(H=12(D/q)^2\). The same universal formula simplifies exactly to
\[
 \operatorname{Cov}(W_0,W_j)=2D^2e^{-2xj}(x^2-\sinh^2x).
\]
Since \(\sinh x>x\) for every \(x>0\), these correlations are strictly negative. The coincident means follow from the earlier second-moment identity.

## Verification

The standalone `verify.py` rederives the relevant fourth-moment expression in a separate algebraic form, compares exact rational expressions for Erlang shapes one through eight, verifies the root's rational bracketing, and checks the deterministic-clock formula. It also generates independent Brownian–Ornstein–Uhlenbeck transitions over sampled on and off intervals to compare cycle-mean and adjacent-work covariance with the analytic formula. Execute `python verify.py` using Python 3, SymPy and NumPy; Numba is optional for speed. All exact analytic steps are in the proof. Monte Carlo checks use finite samples with uncertainty allowances and are **not** proofs of global signs or uniqueness.

## Relationship to prior work

Santra, Das and Nath (2021) establish the flashing harmonic Brownian model with *Poisson* switching and study stationary position laws, relaxation and first passage, not cycle-work memory. Alston, Cocconi and Bertrand (2022) develop energetic descriptions of fluctuating potentials; Frydel (2024) analyzes the same on/off harmonic family and mean injected power. These are the sources for the model and mean-energy context, not novel ingredients of the claim. Published work on Poisson accumulated-work fluctuations already gives a Gaussian long-time CLT, explicit **physical-time** variance rate, and a finite-horizon exponential-moment obstruction. A related semimarkov harmonic study gives stationary position moments and the **integrated position** autocovariance for two positive stiffnesses. These do not directly establish the *event-indexed work increment covariance* or the minimal three-stage Erlang sign boundary proved here. General renewal recurrences and Gaussian moment techniques could recover these identities after further calculation, so methodology and potential implicit coverage are acknowledged.

## Limitations

The sharp smallest-stage classification is for matching integer-shape Erlang on and off clocks with equal means; it does not claim a classification over arbitrary renewal distributions, unmatched on/off means, or every higher Erlang shape's root count. The deterministic protocol is a separate limiting clock. The result characterizes pairwise work covariance at nonzero **cycle lags**, not physical-time lag correlations, full work-count large deviations, or its sign after normalizing by fluctuating elapsed time. It presumes independently sampled durations and thermal noise, linear overdamped confinement, and stationarity at the beginning of a complete cycle. No independent mathematical audit or comprehensive publication-priority certification has been performed.

## References

- I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609v1 (first public 2021-04-01), https://arxiv.org/abs/2104.00609.
- H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (2022), https://arxiv.org/abs/2202.02630.
- D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (2024), https://arxiv.org/abs/2407.12213.
- D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (2026), https://arxiv.org/abs/2607.05173.
- *Gaussian work fluctuations without finite exponential moments in an intermittent harmonic trap*, research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-gaussian-work-fluctuations-without-finite-exponential-moments-in--82e1d04ffdf8.
- *A spectral discriminator for semi-Markov switching harmonic traps*, research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-spectral-discriminator-for-semi-markov-switching-harmonic-trap--0dffd78bb5f6.
