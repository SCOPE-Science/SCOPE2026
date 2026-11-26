# Exact Gaussian stationary tails and a Gamma endpoint law for partial Ornstein–Uhlenbeck resetting

## Finding
For a mean-reverting Brownian particle with independent proportional Poisson contractions, the stationary far tail is **Gaussian with an exact algebraic prefactor**. A hidden variance-deficit variable has an exact endpoint power law, and conditioning on an extreme observed position produces a Gamma law for the rescaled deficit.

Set \(v_*=D/\kappa\), \(\alpha=r/(2\kappa)\). Then the stationary density \(p\) satisfies
\[
p(x)\sim\frac{\Gamma(1+\alpha)K}{\sqrt{2\pi v_*}}
\left(\frac{2v_*}{x^2}\right)^\alpha
\exp\!\left(-\frac{x^2}{2v_*}\right),\qquad |x|\longrightarrow\infty,
\]
where the exact strictly positive prefactor \(K\) is specified below. Equivalently, \(\Pr(|X|>x)\sim 2v_*p(x)/x\) as \(x\to\infty\).

This supplies a precise *far-tail boundary* for a frequent-weak-reset diffusion approximation: for each strictly positive reset fraction, its algebraic asymptotic density differs qualitatively from the exact jump process's Gaussian tail. The approximation can remain accurate for typical fluctuations.

## Assumptions and scope
Fix real \(\kappa,D,r>0\) and \(a\in[0,1)\). Between resets, \(X\) is the unique strong solution of
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t.
\]
At the points of an independent rate-\(r\) Poisson process, set \(X_t=aX_{t-}\); no dwell time or extra noise occurs. All assertions refer to its unique invariant law, at a stationary ordinary observation time, not only immediately after a jump. The exponent \(\alpha\) is fixed and strictly positive. The endpoint \(a=1\) is **excluded** from all displayed tail asymptotics: at that endpoint the process is the ordinary Gaussian Ornstein–Uhlenbeck diffusion.

Let \(V\) denote the variance of \(X\) conditional on the entire reset-time history. Define \(U=V/v_*\in(0,1)\). For positive integers \(n\), put
\[
m_0=1,\qquad
m_n=\prod_{j=1}^{n}\frac{j}{j+\alpha(1-a^{2j})},
\qquad K=\sum_{n=0}^{\infty}\frac{(\alpha)_n}{n!}a^{2n}m_n.
\]
Here \((\alpha)_n=\Gamma(\alpha+n)/\Gamma(\alpha)\) and \((\alpha)_0=1\). The series converges absolutely for \(a<1\); \(K=1\) at \(a=0\).

## Proof
**1. Unique Gaussian variance mixture.** Couple two trajectories by the same Brownian motion and Poisson events. Their difference at time \(t\) is the initial difference times \(e^{-\kappa t}a^{N_t}\), so initial conditions are forgotten. A two-sided stochastic convolution therefore constructs the unique invariant distribution. Conditioned on the Poisson event times, that convolution is Gaussian of mean zero and variance \(V\) satisfying \(0<V<v_*\). Between events, its normalized variance obeys \(\dot U=2\kappa(1-U)\); at each event it changes to \(a^2U\).

**2. Exact variance-deficit endpoint.** At a stationary ordinary observation time, the age \(T\) since the latest Poisson event is exponential with rate \(r\). The pre-event variance \(U'\) has the stationary ordinary-time distribution by Poisson arrivals seeing time averages and is independent of \(T\). Consequently,
\[
U\ \overset{d}{=}\ 1-(1-a^2U')e^{-2\kappa T},
\qquad U'\overset{d}{=}U,
\qquad T\mathrel{\perp}U'.
\]
Write \(B=e^{-2\kappa T}\). Its cumulative distribution is \(\Pr(B\le b)=b^\alpha\), for \(0<b<1\). Set \(H=1-a^2U'\), which lies in \([1-a^2,1]\). Thus \(1-U=HB\) and, **exactly for** \(0<z<1-a^2\),
\[
\Pr(1-U<z)=z^\alpha\,\mathbb E H^{-\alpha}=Kz^\alpha.
\]
The equality \(K=\mathbb E(1-a^2U)^{-\alpha}\) is well-defined since \(1-a^2U\ge1-a^2>0\).

**3. Computable coefficient.** The stationary generator of \(U\), applied to \(u^n\), yields
\[
0=2\kappa n(m_{n-1}-m_n)+r(a^{2n}-1)m_n.
\]
This gives the product formula for \(m_n=\mathbb E U^n\). Expanding \((1-a^2U)^{-\alpha}\) using its absolutely convergent binomial series gives the specified series for \(K\). Every term is nonnegative and the bound \(K\le(1-a^2)^{-\alpha}\) controls convergence.

**4. Density asymptotic.** Put \(q=x^2/(2v_*)\) and \(\delta=1-U\). Conditional Gaussianity gives
\[
p(x)=\frac{e^{-q}}{\sqrt{2\pi v_*}}
\int_{(0,1)}(1-\delta)^{-1/2}
\exp\!\left(-\frac{q\delta}{1-\delta}\right)dF_\delta(\delta).
\]
On any fixed interval \(0<\delta<\delta_0<1-a^2\), step 2 gives the **exact** density \(\alpha K\delta^{\alpha-1}\). Substitute \(y=q\delta\); the integrand converges to \(\alpha Kq^{-\alpha}y^{\alpha-1}e^{-y}\). Dominated convergence applies on the small-deficit region, using \(e^{-q\delta/(1-\delta)}\le e^{-q\delta}\) and a bounded factor \((1-\delta)^{-1/2}\). The complement \(\delta\ge\delta_0\) is exponentially smaller after factoring \(e^{-q}\): for \(q\) sufficiently large its integrand is bounded uniformly by an exponentially decaying constant, even as \(\delta\uparrow1\). Hence
\[
p(x)\sim\frac{e^{-q}}{\sqrt{2\pi v_*}}
\alpha K\Gamma(\alpha)q^{-\alpha},
\]
which is the claim. The one-sided tail follows by a standard integration by parts or l'Hôpital's rule applied to the displayed asymptotic and the explicit Gaussian decay.

**5. Extreme conditional localization.** The conditional law of \(\delta\) given a position \(X=x\) is tilted by the integrand in step 4. The same substitution and dominated-convergence calculation shows that \(q\delta\mid(X=x)\) converges in distribution to the Gamma law with density \(y^{\alpha-1}e^{-y}/\Gamma(\alpha)\) on \(y>0\). All stationary \(X\)-moments are finite because \(V\le v_*\) in the Gaussian mixture.

**6. Comparison at the frequent-weak-reset scale.** Parameterize the reset as \(a=1-s\) with \(0<s<1\), set \(r=\lambda/s\), and keep \(\kappa,D,\lambda>0\) fixed. The standard second-order Kramers–Moyal approximation is
\[
d\widetilde X_t=-(\kappa+\lambda)\widetilde X_t\,dt
+\sqrt{2D}\,dW_t+\sqrt{\lambda s}\,\widetilde X_t\,dB_t,
\]
with independent Brownian drivers. Its invariant density is proportional to
\[
(2D+\lambda sx^2)^{-1-(\kappa+\lambda)/(\lambda s)},
\]
and has a polynomial far tail for every \(s>0\). In contrast, the **exact jump process** has the Gaussian asymptotic proved above, and all positive moments. Therefore the diffusion approximation is not uniform in the spatial far tail. The result makes no claim about an order of limits jointly sending \(s\to0\) and \(|x|\to\infty\).

## Verification
The accompanying `verify.py` checks the exact variance-moment recurrence for orders one through six against an independent stationary variance recursion (180,000 iterates), evaluates \(K\) in two independent ways (series and simulation), and computes exact conditional-age integrals for four increasingly extreme values of \(q\). For \(\kappa=D=1\), \(r=1.2\), \(a=0.35\), the observed normalized density coefficient approaches \(0.9401107588\): the ratios at \(q=8,20,45,90\) were \(0.9314,0.9702,0.9866,0.9935\), respectively. These numerical checks support normalization and convergence but are not a replacement for the infinite-asymptotic proof.

Reproduce using `python verify.py` with the dependencies listed in `requirements.txt`. No archived data are required.

## Relationship to prior work
Galla (arXiv:2602.21635v1, February 25, 2026) derives a **diffusion approximation** for frequent weak partial resets, and in its linear example and supplemental section S1.1 obtains the stationary density of the approximating stochastic differential equation. That density has algebraic tails at fixed positive approximation parameter. The present result concerns the *exact* Poisson-jump model with confining drift and proves the Gaussian extreme-density law, exact coefficient and hidden Gamma localization; it does not rederive the published approximation as a novel claim.

Olsen and Gupta (arXiv:2401.11919) study thermodynamic work of partial resetting and provide exact second moments in a harmonic exploration potential (section III.3) without an exact stationary large-position asymptotic. Pierce (arXiv:2204.07215) develops proportional resetting with constant advection and free diffusion, not the mean-reverting Gaussian variance mixture studied here. Trajanovski et al. (arXiv:2301.12304) treat Ornstein–Uhlenbeck motion with *full* resetting to a fixed point (including comb geometries), which does not give the coefficient for \(0<a<1\). A general endpoint Laplace principle underlies step 4; the model-specific deficit identity and explicit coefficient are the distinguishing parts.

## Limitations
The finding applies only to centered one-dimensional Ornstein–Uhlenbeck motion with **constant-rate, state-independent Poisson** contractions, fixed \(0\le a<1\), and positive \(\kappa,D\). It does not establish joint weak-reset/large-position uniform error bounds, first-passage properties, multidimensional extensions, or results for randomly distributed contraction factors. Its novelty is relative to the inspected sources and remains subject to implicit coverage by broader Gaussian-mixture and piecewise deterministic Markov-process theory.

## References
1. Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1, publicly submitted February 25, 2026. https://arxiv.org/html/2602.21635v1
2. Kristian Stølevik Olsen and Deepak Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919v2 (first publicly submitted January 22, 2024). https://ar5iv.org/html/2401.11919v2
3. J. Kevin Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1, April 14, 2022. https://arxiv.org/html/2204.07215v1
4. Pece Trajanovski et al., *Ornstein–Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304v1, January 28, 2023. https://arxiv.org/abs/2301.12304
