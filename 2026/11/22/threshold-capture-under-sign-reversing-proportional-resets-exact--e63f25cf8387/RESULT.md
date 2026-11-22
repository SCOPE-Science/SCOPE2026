# Threshold capture under sign-reversing proportional resets: exact mean, jump-channel law, and a singular reflection endpoint

## Finding
Let \(D,r,L>0\) and \(0<q\leq1\). A real-valued process starts at \(X_0=0\), diffuses with generator \(D\partial_x^2\) between independent rate-\(r\) Poisson events, and changes from \(x\) to \(-qx\) at each event. It is killed at the *first entrance into the closed half-line* \([L,\infty)\): in particular, a jump from below \(-L/q\) that passes over \(L\) counts as successful capture. Let \(\tau\) be the killing time and \(J\) the event that killing happens at a Poisson jump rather than during a Brownian segment.

Write \(\beta=L\sqrt{r/D}\) and define the entire functions
\[
H_q(z)=\sum_{n=0}^{\infty}\frac{z^{2n+1}}{(2n+1)!}\prod_{j=0}^{n-1}(1+q^{2j+1}),\qquad
G_q(z)=\sum_{n=1}^{\infty}\frac{z^{2n}}{(2n)!}\prod_{j=1}^{n-1}(1-q^{2j}),
\]
with empty products equal to one, and the positive denominator
\[
\mathcal D_q(\beta)=H_q'(\beta/q)+H_q(\beta/q)+H_q(\beta).
\]
For every \(0<q\le1\) and \(\beta>0\), both the mean capture time and the jump-capture probability are exactly
\[
\boxed{\begin{aligned}
r\,\mathbb E_0\tau&=G_q(\beta)+\frac{H_q(\beta)\,[1+G_q(\beta/q)+G_q'(\beta/q)-G_q(\beta)]}{\mathcal D_q(\beta)},\\
\mathbb P_0(J)&=\frac{H_q(\beta)}{\mathcal D_q(\beta)}.
\end{aligned}}
\]
The jump-capture probability is strictly between zero and one. It has two sharp rare-event asymptotics:
\[
\boxed{\begin{aligned}
\mathbb P_0(J)&\sim\sinh(\beta)e^{-\beta/q}&&\text{as }q\downarrow0\text{ with }\beta>0\text{ fixed},\\
\mathbb P_0(J)&\sim\tfrac12e^{-\beta(1/q-1)}&&\text{as }\beta\to\infty\text{ with }0<q<1\text{ fixed}.
\end{aligned}}
\]
Define the strictly positive infinite product \(d_q=\prod_{j=1}^{\infty}(1-q^{2j})\) for \(0<q<1\). The strong-resetting mean obeys
\[
\boxed{r\,\mathbb E_0\tau\sim d_qe^\beta\qquad(\beta\to\infty,\ 0<q<1\text{ fixed}).}
\]
At the noncontractive reflection endpoint \(q=1\), the same exact formulas reduce to elementary expressions:
\[
H_1(z)=\frac{\sinh(\sqrt2 z)}{\sqrt2},\qquad G_1(z)=\frac{z^2}{2},\qquad
r\,\mathbb E_0\tau=\frac{\beta^2}{2}+\frac{(1+\beta)H_1(\beta)}{H_1'(\beta)+2H_1(\beta)}.
\]
Consequently, as \(r\to\infty\) with \(D,L\) fixed,
\[
\boxed{\mathbb E_0\tau\longrightarrow\frac{L^2}{2D},\qquad
\mathbb P_0(J)\longrightarrow\frac1{2+\sqrt2}\quad(q=1).}
\]
Thus strong resetting makes the capture time diverge exponentially for every fixed strict contraction \(0<q<1\), but leaves a finite Brownian-scale capture time at exactly \(q=1\). The strong-reset limits are singular at the reflection endpoint.

## Assumptions and scope
Brownian variance is \(2Dt\). Poisson jump times are independent of Brownian noise. A jump across the absorbing half-line is immediately detected; a jump reaching exactly \(L\) also counts, but its borderline pre-jump state has zero probability at any jump time. The initial location is zero. All formulas concern the original continuous-time process without lattice discretization. No assumption of a stationary unrestricted process is needed, so \(q=1\) is included even though the unrestricted reflected-reset process does not have a normalizable equilibrium law. The term *strong resetting* means \(r\to\infty\) with \(D,L,q\) fixed, equivalently \(\beta\to\infty\).

## Proof
**1. Finite mean and uniqueness.** For every fixed \(D,r,L>0\) and \(0<q\le1\), choose a finite \(T>0\) and \(K>L/q+1\). From each starting point in the bounded interval \([-K,L)\), there is a uniformly positive probability of Brownian crossing of \(L\) by time \(T\) and no intervening Poisson event. From each starting point below \(-K\), there is a uniformly positive probability that the Brownian displacement stays smaller than one in absolute value up to \(T\) and at least one Poisson event occurs by \(T\); the first such event sends the walker into \([L,\infty)\). Therefore a constant \(\varepsilon>0\) exists, independent of the starting point below \(L\), such that capture occurs within time \(T\) with probability at least \(\varepsilon\). The Markov property gives \(\sup_{x<L}\mathbb P_x(\tau>nT)\le(1-\varepsilon)^n\). Hence \(\sup_{x<L}\mathbb E_x\tau<\infty\). The same stopping argument makes bounded solutions to the backward boundary-value equations below unique: a bounded homogeneous solution with zero killing payoff equals its expected stopped value at time \(t\), which tends to zero as \(t\to\infty\).

**2. Two backward equations and the left reduction.** Put \(k=\sqrt{r/D}\), \(y=kx\), \(b=\beta\), and let \(u(y)=r\mathbb E_{y/k}\tau\), \(p(y)=\mathbb P_{y/k}(J)\). In the interior \(-b/q<y<b\), a reset lands below \(b\), so the backward equations are
\[
u''(y)-u(y)+u(-qy)=-1,\qquad p''(y)-p(y)+p(-qy)=0.
\]
For \(y<-b/q\), any reset reaches or jumps over \(b\); the mean pays zero future time upon such a reset and the reset-capture probability pays one. Thus
\[
u''(y)-u(y)=-1,\qquad p''(y)-p(y)=-1\qquad(y<-b/q).
\]
Both quantities vanish for the Brownian boundary start \(y=b\). Boundedness at negative infinity forces, with \(z=b/q\),
\[
u(y)=1+[u(-z)-1]e^{y+z},\qquad p(y)=1+[p(-z)-1]e^{y+z}\quad(y\le-z).
\]
The functions and their first derivatives are continuous at \(y=-z\); otherwise a spurious local-time term would appear in the diffusion generator. The resulting exact Robin conditions are
\[
u'(-z)=u(-z)-1,\qquad p'(-z)=p(-z)-1.
\]
The second derivative of \(p\) need not be continuous at \(-z\), since the reset payoff has a jump there. The single-point convention does not change the expectation.

**3. Entire-function basis and matching.** Direct differentiation of the absolutely convergent factorial series gives
\[
H_q''(y)=H_q(y)-H_q(-qy),\qquad G_q''(y)=1+G_q(y)-G_q(-qy).
\]
For example the odd coefficients satisfy \(c_{n+1}=(1+q^{2n+1})c_n\), and the even coefficients satisfy \(d_{n+1}=(1-q^{2n})d_n\). These recurrences also show that any solution with prescribed value and first derivative at the origin is unique on the compact invariant interval \([-b/q,b]\), by the integral equation and Gronwall's inequality applied simultaneously to its positive and negative arguments. Therefore the interior solutions with zero right-boundary values have the forms
\[
u(y)=B[H_q(y)-H_q(b)]-[G_q(y)-G_q(b)],\qquad
p(y)=C[H_q(y)-H_q(b)].
\]
Oddness of \(H_q\) and evenness of \(G_q\), including the parities of their derivatives, give from the Robin matching conditions
\[
B=\frac{G_q(b)-G_q(z)-G_q'(z)-1}{H_q'(z)+H_q(z)+H_q(b)},\qquad
C=-\frac1{H_q'(z)+H_q(z)+H_q(b)}.
\]
Inserting \(y=0\), where \(H_q(0)=G_q(0)=0\), proves both exact formulas. The denominator is positive because every coefficient of \(H_q\) and \(H_q'\) is positive for positive arguments. The probability lies strictly between zero and one by the explicit formula and by positivity of the competing Brownian-capture event. Finally, the piecewise solutions are bounded and continuously differentiable, so Dynkin's formula up to the stopping time, followed by the exponential tail bound in Step 1, identifies them with the desired mean and probability, not merely formal differential-equation solutions.

**4. Entire-function growth and rare-jump asymptotics.** For \(0<q<1\), define
\[
C_q=\prod_{j=0}^{\infty}(1+q^{2j+1})\in(1,\infty),\qquad
d_q=\prod_{j=1}^{\infty}(1-q^{2j})\in(0,1).
\]
The coefficients of \(H_q\) increase from one to \(C_q\), while those of \(G_q\) decrease to \(d_q\). Comparing their factorial-series weights with \(\sinh z\) and \(\cosh z\), followed by dominated convergence for the normalized odd and even exponential series as \(z\to\infty\), proves
\[
H_q(z)\sim C_q\sinh z,\quad H_q'(z)\sim C_q\cosh z,\quad
G_q(z)\sim d_q(\cosh z-1),\quad G_q'(z)\sim d_q\sinh z.
\]
For fixed \(q<1\), the argument \(b/q\) grows faster than \(b\), so the denominator is asymptotic to \(C_q e^{b/q}\), proving the fixed-\(q\) jump-probability asymptotic. The same comparison gives the mean asymptotic \(u(0)\sim d_qe^b\), where the two contributing terms each have leading size \(d_qe^b/2\). For \(q\downarrow0\) at fixed \(b>0\), the coefficient bound \(1\le\prod_{j<n}(1+q^{2j+1})\le C_q\to1\) gives uniformly for positive \(z\) the inequalities \(\sinh z\le H_q(z)\le C_q\sinh z\) and \(\cosh z\le H_q'(z)\le C_q\cosh z\). As \(z=b/q\to\infty\), these yield \(\mathcal D_q(b)\sim e^{b/q}\), while \(H_q(b)\to\sinh b\), proving the other sharp jump-probability asymptotic. The same coefficient bounds for \(G_q\) show that the exact mean tends to \((e^b-1)/r\) as \(q\downarrow0\).

**5. The noncontractive reflection endpoint.** At \(q=1\), the products in the defining series become \(2^n\) for \(H_q\) and zero beyond the first term of \(G_q\), so \(H_1(z)=\sinh(\sqrt2z)/\sqrt2\) and \(G_1(z)=z^2/2\). These functions satisfy the same boundary equations and matching conditions; Step 1 still supplies finite mean and uniqueness. Substitution proves the endpoint formulas. Since \(H_1(b)/(H_1'(b)+2H_1(b))\to1/(2+\sqrt2)\), the jump-capture limit follows. The extra term in \(r\mathbb E_0\tau\) grows only linearly in \(b\), compared with the leading \(b^2/2\). Using \(r=Db^2/L^2\), the mean therefore tends to \(L^2/(2D)\). This finite limit is incompatible with the divergent fixed-\(q<1\) strong-reset mean and proves the singular endpoint distinction.

## Verification
The standalone `verify.py` implements the factorial-series solution, exact rational recurrence checks and an independent finite-difference boundary-value solver with linear interpolation of the nonlocal argument and a second-order Robin boundary stencil. It also checks the elementary \(q=1\) limit and the two rare-jump asymptotics. Run `python verify.py` with Python 3, `mpmath`, `numpy`, and `scipy`. The recorded execution passed 250 finite diagnostic assertions. For \(D=r=L=1\) and \(q=1/2\), the formulas give \(\mathbb E_0\tau=1.246210358622894851\ldots\) and \(\mathbb P_0(J)=0.11440049594507145953\ldots\). The finite-difference method is independent of the entire-function evaluation; neither numerical procedure is offered as a proof of global statements.

## Relationship to prior work
Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387v1) analyze this sign-reversing resetting mechanism when a target is detected only upon *exact point occupation*. Their negative-rescaling backward equation extends over both sides of the target, unlike the absorbing-half-line convention here. Two separately published Fourier/Laplace resolvent results also give simulation-free exact-*point*-hitting formulas with explicit statements that resets leaping over the target do not count. None of those exact-point laws implies this new reset-capture channel or its singular \(q=1\) strong-reset conclusion. Pierce (arXiv:2204.07215v1) develops the proportional-reset pantograph framework with positive multipliers. Radice, Cristadoro and Thapa (arXiv:2410.05835v1) study barrier overshoots for a different, discrete-time random walk with independent increments and position-independent resetting. This work uses classical generator and interface-matching methods; neither those methods nor the underlying reset mechanism is claimed new.

## Limitations
The result is specific to one spatial dimension, symmetric Brownian segments, constant Poisson rate, a single negative deterministic multiplier and an absorbing half-line. It does not solve the exact-point-hit problem, optimize the reset rate, or extend the formulas to random reset multipliers. The \(q<1\) and \(q=1\) strong-rate limits are deliberately kept distinct, and their joint crossover when \(q\uparrow1\) with \(r\to\infty\) is not classified. General first-passage operator methods might provide alternative implicit representations, and exhaustive bibliographic priority has not been independently certified.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1, 12 June 2024, https://arxiv.org/abs/2406.08387.
2. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1, 14 April 2022, https://arxiv.org/abs/2204.07215.
3. M. Radice, G. Cristadoro, S. Thapa, *Optimal conditions for first passage of jump processes with resetting*, arXiv:2410.05835v1, 8 October 2024, https://arxiv.org/abs/2410.05835.
4. *A simulation-free resolvent for reflected partial-reset first passage*, publicly available research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-simulation-free-resolvent-for-reflected-partial-reset-first-pa--638f1e8ee738.
5. *Certified first-passage series for Brownian reflection–rescaling*, publicly available research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-certified-first-passage-series-for-brownian-reflection-rescaling--06fe2a2cb477.
