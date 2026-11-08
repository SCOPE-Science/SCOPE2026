# Exact opposite-side absorption law for a transparent blinking Brownian target under resetting

## Finding
Consider Brownian motion on the real line, reset to a positive position \(x_0\) at Poisson rate \(r\), and a target at the origin that independently switches between active and inactive states. An active encounter absorbs the particle, whereas an inactive encounter is transparent. The gate is not reset when the particle resets. Set \(\lambda=\alpha+\beta\), where \(\alpha\) is the active-to-inactive rate and \(\beta\) is the inactive-to-active rate, and let
\[
 k=\sqrt{r/D},\qquad \ell=\sqrt{(r+\lambda)/D},\qquad E=e^{-\ell x_0}.
\]
With the target initially active or inactive, respectively, the probability that absorption occurs *from the negative half-line* is exactly
\[
 P^-_A=\frac{\alpha}{2\lambda}\left(1-\frac{k}{\ell}\right)(1-E),\qquad
 P^-_I=\frac{1}{2\lambda}\left(1-\frac{k}{\ell}\right)\bigl(\alpha+(r+\beta)E\bigr).
\]
For an initially stationary gate, \(\pi_I=\alpha/\lambda\), this becomes
\[
 \boxed{P^-_{\mathrm{eq}}=\frac{\pi_I}{2}\left(1-\sqrt{\frac{r}{r+\lambda}}\right)
 \left(1+\frac{r}{\lambda}e^{-x_0\sqrt{(r+\lambda)/D}}\right).}
\]
At fixed \(r,D,x_0,\pi_I\), this probability is *strictly increasing* in the total gate-switching speed \(\lambda\), from \(\pi_I e^{-x_0\sqrt{r/D}}/4\) to \(\pi_I/2\). At fixed \(D,x_0,\alpha,\beta\), it is *strictly decreasing* in the resetting rate \(r\), from \(\pi_I/2\) to zero. The high-reset asymptotic is \(P^-_{\mathrm{eq}}\sim\alpha/(4r)\).

The positive-side probability is \(1-P^-\). In particular, the high-switching limit retains a nonzero fraction \(\pi_I/2\) of absorptions from the opposite side even as ordinary first-passage-time statistics approach those of a permanently absorbing target. This is a singular feature of directional absorption observables, not a claim that the limiting trajectories reproduce a permanently active gate.

## Assumptions and scope
- \(D,r,\alpha,\beta,x_0\) are strictly positive and finite; \(dX_t=\sqrt{2D}\,dB_t\) between independent rate-\(r\) instantaneous resets to \(x_0>0\).
- The independent gate \(J_t\in\{A,I\}\) transitions \(A\to I\) at rate \(\alpha\) and \(I\to A\) at rate \(\beta\). Resetting \(X\) does *not* reset \(J\).
- The absorption time is \(\tau=\inf\{t\ge 0:X_t=0,\ J_t=A\}\). When \(J_t=I\), the origin is freely traversable; there is neither reflection nor binding. Absorption is labelled negative-side if \(X_{\tau-\varepsilon}<0\) for all sufficiently small \(\varepsilon>0\) outside a null event. It is well-defined as a first active-state crossing from a half-line; the potential ambiguity at gate-switch instants has zero probability under independence and continuity.
- \(P^-_A,P^-_I\) condition on the deterministic initial target state. \(P^-_{\mathrm{eq}}\) averages these with stationary weights \(\pi_A=\beta/\lambda\) and \(\pi_I=\alpha/\lambda\).
- The gate-speed monotonicity holds along \(\alpha=\pi_I\lambda\), \(\beta=(1-\pi_I)\lambda\), with fixed \(\pi_I\in(0,1)\). The reset-rate monotonicity holds with \(\alpha,\beta\) fixed.

## Proof
**1. Almost-sure absorption and backward problem.** Conditional on any current gate state, there is a uniform positive probability within a fixed finite time interval that the gate is active for a subinterval, no reset occurs during that subinterval, and the Brownian particle crosses the origin. At resets the particle starts at \(x_0\), giving a uniform regeneration lower bound. Iterating implies \(\tau<\infty\) almost surely. In particular, the bounded backward-harmonic problem for the left-arrival probability has a unique probabilistic solution by stopping and dominated convergence.

Let \(f_A(x)\) and \(f_I(x)\) be the negative-side absorption probabilities from position \(x\) and indicated gate state. Away from the origin the generator equations are
\[
 D f_A''+\alpha(f_I-f_A)+r[f_A(x_0)-f_A(x)]=0,
 \qquad D f_I''+\beta(f_A-f_I)+r[f_I(x_0)-f_I(x)]=0.
\]
At an active encounter, \(f_A(0^-)=1\) and \(f_A(0^+)=0\). The inactive-state solution and its first derivative are continuous at zero because the origin is transparent while the gate is inactive. Both solutions are bounded at spatial infinity.

**2. Decoupling.** Define \(u=\beta f_A+\alpha f_I\) and \(v=f_A-f_I\). Writing \(U=u(x_0)\) and \(V=v(x_0)\), their equations reduce to
\[
 D u''-r(u-U)=0,\qquad D v''-(r+\lambda)v+rV=0.
\]
The bounded solutions on the two half-lines have the forms
\[
 \begin{array}{ll}
 x>0:&u_+(x)=U,\quad v_+(x)=C+B e^{-\ell x},\\
 x<0:&u_-(x)=U+\beta e^{kx},\quad v_-(x)=C+(B+1)e^{\ell x}.
 \end{array}
\]
Indeed, active absorption imposes \(u_-(0)-u_+(0)=\beta\) and \(v_-(0)-v_+(0)=1\); the coefficient of the growing exponential in \(u_+\) is zero because \(U=u(x_0)\).

**3. Interface matching and evaluation.** Continuity of \(f_I=(u-\beta v)/\lambda\) and of \(f_I'\) gives
\[
 B=\frac12\left(\frac{k}{\ell}-1\right).
\]
The self-consistency \(V=v_+(x_0)=C+BE\) gives \(C=rBE/\lambda\), while \(f_A(0^+)=0\) gives \(U=-\alpha(C+B)\). Hence
\[
 f_A(x_0)=\frac{\alpha}{\lambda}(-B)(1-E),\qquad
 f_I(x_0)=\frac{-B}{\lambda}\left[\alpha+(r+\beta)E\right].
\]
These are the claimed conditional formulas. The stationary average equals
\[
 P^-_{\mathrm{eq}}=\frac{\beta f_A(x_0)+\alpha f_I(x_0)}{\lambda}
 =\frac{\alpha}{2\lambda}\left(1-\frac{k}{\ell}\right)
 \left(1+\frac{r}{\lambda}E\right).
\]
The resolved boundary-value solution is bounded, satisfies all jump/continuity conditions and the generator on both open half-lines. The almost-sure stopping argument identifies it with the desired probability, without relying on any finite lattice approximation.

**4. Strict parameter monotonicity and endpoints.** Introduce \(a=\sqrt{1+\lambda/r}>1\) and \(s=x_0\sqrt{r/D}>0\), so that
\[
 P^-_{\mathrm{eq}}=\frac{\pi_I}{2}H(a,s),\qquad
 H(a,s)=1-\frac1a+\frac{e^{-as}}{a(a+1)}.
\]
Clearly \(\partial_sH=-e^{-as}/(a+1)<0\). Direct differentiation gives
\[
 a^2\partial_aH=1-Q(a,s),\qquad
 Q(a,s)=e^{-as}\left(\frac{as}{a+1}+\frac{2a+1}{(a+1)^2}\right).
\]
For fixed \(a>1\), \(Q(a,0)=(2a+1)/(a+1)^2<1\) and
\[
 \partial_sQ=-e^{-as}\left(\frac{a^2}{(a+1)^2}+\frac{a^2s}{a+1}\right)<0.
\]
Therefore \(\partial_aH>0\) for every \(a>1,s\ge0\). Increasing \(\lambda\) at fixed \(r,D,x_0,\pi_I\) increases \(a\) with \(s\) fixed, hence increases \(P^-_{\mathrm{eq}}\). Increasing \(r\) with the other physical parameters fixed decreases \(a\) while increasing \(s\), so *both* changes strictly decrease the probability. The limits follow directly from \(H(1,s)=e^{-s}/2\), \(\lim_{a\to\infty}H(a,s)=1\) at fixed \(s\), \(\lim_{r\downarrow0}a=\infty\), and \(1-\sqrt{r/(r+\lambda)}\sim\lambda/(2r)\) as \(r\to\infty\). The high-\(r\) exponential correction is negligible and gives \(\alpha/(4r)\).

## Verification
Run `python verify_splitting.py` with Python 3, SymPy, NumPy and SciPy. The program checks twelve symbolic identities; evaluates the exact conditional and equilibrium formulas; solves independent finite-difference backward equations on the two half-lines for six parameter tuples and three successively finer meshes; and checks two strict monotonicity trends on a product parameter grid. In the packaged run it passed 12 symbolic identities and 714 numerical comparisons/inequalities. Finite-difference evidence is corroborative: the proof above, not the finite grid, establishes the global statements. A separate event-driven first-passage simulation at three switching speeds was used to examine the same directional observable; sampling errors preclude its use as a proof.

## Relationship to prior work
Żbik, Dybiec, Capała, Palmowski and Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739 (first publicly submitted 10 December 2025), introduced the **same full-line transparent target with gate preserved at resets**. They derived first-passage-time transforms, mean passage times and survival statistics. Their Section III.3 and Fig. 5 report simulated fractions of hits from each side, but no closed expression or proof of global directional monotonicity. The present result is the exact analytic law for that directional statistic, its full monotonicity and singular fast-gating limit. It does not claim the underlying model, time-transform machinery, or ordinary resetting backward equations as new. Their prose in Section III.3 describes a qualitative speed trend that is not the same as the exact monotonicity proved here; this discrepancy warrants direct numerical reconciliation before any empirical interpretation.

Mercado-Vásquez and Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148, analyze a **reflecting** inactive target and mean search time; negative-side arrival is then excluded by their boundary model. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739, studies time statistics and a gate protocol that can also be renewed by resetting; it does not give the claimed transparent-crossing side probability. Bressloff, *Renewal theory for Brownian motion with stochastically gated targets*, arXiv:2601.01588, is framed on a reflecting half-line or bounded domains, and *Renewal theory for Brownian motion across a stochastically gated interface*, arXiv:2601.13414, concerns a gate that reflects in one state and transmits in the other, with diffusion continuing after interface crossing; neither matches **absorption on the active gate and transmission on the inactive gate** with reset to a fixed positive location. Classical resetting and other splitting-probability literature provides methods, not the reported formula for this specific observable.

## Limitations
The theorem is for exact continuous-time Brownian dynamics with a point target, no drift, stationary exponential gate switches, and resetting of position only. It does not apply unchanged to a finite-width target, resetting of the gate, reflected inactive targets, Lévy motion, discrete-time crossing conventions or imperfect detection on active encounters. A stationary-initial-gate monotonicity is not a claim of monotonicity for every fixed nonequilibrium gate initialization. Publication priority is not independently certified, and closely related general gated first-passage frameworks exist. The qualitative side-arrival trend stated in the source simulation discussion has not been reconciled with its time-step or crossing-counting convention. Independent mathematical audit is not performed. The \(r\downarrow0\), \(\lambda\downarrow0\) and \(\lambda\to\infty\) limits concern probabilities in the strictly positive-rate model; they should not be substituted blindly into singular exactly zero-rate models.

## References
1. B. Żbik, B. Dybiec, K. Capała, Z. Palmowski and I. M. Sokolov, *Hitting the blinking target under stochastic resetting* (2025/2026), arXiv:2512.09739, https://arxiv.org/html/2512.09739 ; submission history https://arxiv.org/abs/2512.09739 .
2. G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting* (2021), arXiv:2107.02148, https://arxiv.org/abs/2107.02148 .
3. P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting* (2020), arXiv:2009.02739, https://arxiv.org/abs/2009.02739 .
4. P. C. Bressloff, *Renewal theory for Brownian motion with stochastically gated targets* (2026), arXiv:2601.01588, https://arxiv.org/abs/2601.01588 .
5. P. C. Bressloff, *Renewal theory for Brownian motion across a stochastically gated interface* (2026), arXiv:2601.13414, https://arxiv.org/abs/2601.13414 .
6. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Physical Review Letters 106, 160601 (2011), https://doi.org/10.1103/PhysRevLett.106.160601 .
