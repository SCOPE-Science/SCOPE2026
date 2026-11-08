# Exact variance-edge law and Gaussian-tail prefactor under partial Ornstein–Uhlenbeck resetting

## Finding

Consider a one-dimensional overdamped particle in a harmonic potential, subject to independent Poisson resets that multiply its instantaneous position by a constant factor. Its stationary position distribution has a universal, Gaussian rather than exponential, far-tail exponent; yet resetting imprints an exact algebraic depletion relative to the equilibrium Gaussian.

Let \(D,\gamma,r>0\), \(0\le q<1\), and define \(\sigma^2=D/\gamma\) and \(\alpha=r/(2\gamma)\). For the unique stationary position density \(p_q\),
\[
p_q(x)\sim \frac{\Gamma(\alpha+1)(2\sigma^2)^\alpha B_{\alpha,q}}{\sqrt{2\pi\sigma^2}}\,|x|^{-2\alpha}\exp\!\left(-\frac{x^2}{2\sigma^2}\right),\qquad |x|\to\infty,
\]
where the positive, computable coefficient is
\[
 B_{\alpha,q}=\sum_{n=0}^{\infty}\frac{(\alpha)_n}{n!}\,q^{2n}\prod_{j=1}^{n}\frac{j}{j+\alpha(1-q^{2j})}.
\]
For every fixed \(\alpha>0\), the coefficient is strictly increasing in \(q\), starts at \(B_{\alpha,0}=1\), and diverges as \(q\uparrow1\). The exponent \(2\alpha=r/\gamma\) is independent of reset amplitude throughout \(0\le q<1\), but disappears exactly at \(q=1\) because the stationary law then is the unmodified equilibrium Gaussian.

More precisely, the stationary position has the representation \(X\stackrel d=\sigma\sqrt V\,Z\), where \(Z\) is independent standard normal, and the stationary normalized conditional variance \(V\in(0,1)\) has **exact** endpoint density
\[
 f_{1-V}(u)=\alpha B_{\alpha,q}u^{\alpha-1},\qquad 0<u<1-q^2.
\]
This exact edge identity determines the complete leading far-tail coefficient, not merely its exponent.

## Assumptions and scope

Between resets, the position satisfies the Itô equation
\[
 dX_t=-\gamma X_t\,dt+\sqrt{2D}\,dW_t.
\]
A homogeneous Poisson process \(N\) of rate \(r\), independent of the Wiener process \(W\), imposes the instantaneous update \(X_t=qX_{t-}\) at each jump. All assertions concern the unique stationary regime on the full real line with the parameters held fixed before taking \(|x|\to\infty\). The parameter \(q\) may equal zero (complete resets) but not one (ineffective resets). Let \((\alpha)_n=\alpha(\alpha+1)\cdots(\alpha+n-1)\), with \((\alpha)_0=1\), and interpret empty products as one.

## Proof

**Step 1: existence, uniqueness, and conditional Gaussian form.** Construct a two-sided stationary Poisson process and independent two-sided Brownian driving noise. The resulting stationary stochastic convolution is well-defined in second moment because between any two times a difference of trajectories under the same noises contracts by \(e^{-\gamma t}q^{N_t}\); in particular, its magnitude is bounded by \(e^{-\gamma t}\) times the initial difference. This gives a unique invariant law. Conditional on the complete Poisson trajectory, the stochastic convolution is centered Gaussian. Its variance divided by \(\sigma^2\) is
\[
 V=2\gamma\int_0^\infty e^{-2\gamma s}q^{2N((-s,0])}\,ds,
\]
where \(q^0=1\), including when \(q=0\). It satisfies \(0<V<1\) almost surely, because the Poisson process has a strictly positive most recent backward gap and contains a reset strictly before the observation time. Consequently \(X\stackrel d=\sigma\sqrt V Z\) for an independent standard Gaussian \(Z\). For \(q=0\), the same expression reduces to the OU variance accumulated since the most recent complete reset.

**Step 2: the deficit recursion.** Along the deterministic intervals between resets, the conditional variance follows \(\dot V=2\gamma(1-V)\), and at resets it is multiplied by \(q^2\). For stationary Poisson epochs, the elapsed backward age \(T\) is independent of the state immediately preceding the last reset, with \(T\sim\operatorname{Exp}(r)\); the pre-reset state has the same stationary law as the state at a generic time, by independence of the Poisson clock. Therefore, with an independent copy \(V'\) of \(V\),
\[
 V\stackrel d=1-e^{-2\gamma T}(1-q^2 V').
\]
Define \(U=1-V\), \(A=e^{-2\gamma T}\) and \(H=1-q^2V'\). Then \(A\sim\operatorname{Beta}(\alpha,1)\), \(U\stackrel d=AH\) with independent factors, and \(1-q^2\le H\le1\).

**Step 3: exact edge law.** For any \(0<u<1-q^2\), conditioning on \(H\) yields
\[
 \mathbb P(U\le u)=\mathbb E\left[\left(\frac uH\right)^\alpha\right]=B_{\alpha,q}u^\alpha,
 \qquad B_{\alpha,q}=\mathbb E(1-q^2V)^{-\alpha}.
\]
Differentiation establishes the asserted density *exactly* on the open interval. This also proves \(1\le B_{\alpha,q}\le(1-q^2)^{-\alpha}<\infty\).

**Step 4: computable coefficient.** The generator on the bounded variance process is
\[
 (\mathcal L\phi)(v)=2\gamma(1-v)\phi'(v)+r[\phi(q^2v)-\phi(v)].
\]
Stationarity with \(\phi(v)=v^n\) gives, for every integer \(n\ge1\),
\[
 m_n=\mathbb E[V^n]=\frac{n}{n+\alpha(1-q^{2n})}m_{n-1},\qquad m_0=1.
\]
Iterating yields the displayed product formula for \(m_n\). Because \(q<1\), the generalized binomial expansion of \((1-q^2V)^{-\alpha}\) is absolutely and monotonically integrable, giving precisely the convergent series for \(B_{\alpha,q}\).

**Step 5: sharp Gaussian tail.** Write \(s=x^2/(2\sigma^2)\). The conditional-Gaussian representation gives
\[
 p_q(x)=\frac{e^{-s}}{\sqrt{2\pi\sigma^2}}\,
 \mathbb E\left[(1-U)^{-1/2}\exp\!\left(-\frac{sU}{1-U}\right)\right].
\]
Fix \(0<\delta<1-q^2\). On \(0<u<\delta\), substitute the exact power density from Step 3, rescale \(u=z/s\), and apply dominated convergence (or the endpoint Laplace lemma) to obtain
\[
 \alpha B_{\alpha,q}\int_0^\delta u^{\alpha-1}(1-u)^{-1/2}e^{-su/(1-u)}\,du
 \sim \Gamma(\alpha+1)B_{\alpha,q}s^{-\alpha}.
\]
The complementary part is exponentially negligible: for \(s\ge1\), the function \(v^{-1/2}e^{-s(1-v)/v}\) increases on \(0<v\le1\), so the contribution with \(U\ge\delta\) is at most \((1-\delta)^{-1/2}e^{-s\delta/(1-\delta)}\). Therefore the full expectation has the same leading term. Replacing \(s\) with \(x^2/(2\sigma^2)\) establishes the claimed two-sided density asymptotic with its exact prefactor.

**Step 6: strict dependence on reset amplitude.** In the common Poisson realization of Step 1, \(V_q\) is nondecreasing with \(q\). For any \(q_2>q_1\ge0\), \(q_2^2V_{q_2}>q_1^2V_{q_1}\) almost surely, because every \(V_q>0\). Consequently \((1-q^2V_q)^{-\alpha}\) is strictly increasing in \(q\) almost surely, proving strict increase of its expectation. For \(q\uparrow1\), dominated convergence in the integral representation shows \(V_q\uparrow1\) almost surely. Thus \((1-q^2V_q)^{-\alpha}\uparrow\infty\) and monotone convergence gives \(B_{\alpha,q}\uparrow\infty\). At \(q=1\), the Poisson interventions have no effect, and the equilibrium density is exactly \((2\pi\sigma^2)^{-1/2}\exp(-x^2/(2\sigma^2))\). The limit of the fixed-\(q\) tail asymptotics is therefore nonuniform at this boundary.

## Verification

The accompanying `verify.py` checks exact rational stationary moment identities for multiple parameters, checks exact excess-kurtosis identities, evaluates the positive prefactor series at high precision, and numerically compares the exact endpoint Laplace integral with the predicted asymptotic. Run with `python verify.py` in a Python installation providing `mpmath`. In the packaged check, **336 exact identities and 10 high-precision tests passed**. The exact distributional recursion, endpoint identity, and dominated-convergence proof—not these finite checks—establish the universal assertions. For example, at \(\alpha=1\), the coefficient grows from \(1\) at \(q=0\) to approximately \(1.1729098668\) at \(q=1/2\).

## Relationship to prior work

Assefa, Keller-Ressel, and Palmowski (2026) develop general polynomial moment machinery under affine resetting, and explicitly cover multiplicative resetting of Brownian motion and polynomial base processes. The moment recurrence above is a direct special-case stationary-generator consequence, **not claimed as new by itself**. The result established here is instead the exact variance-deficit endpoint density and the sharp Gaussian-tail prefactor in a *harmonically confined* partial-reset model, including its independence of the reset amplitude in the algebraic exponent and its singular amplitude limit. These statements do not follow as stated from finite-degree moment formulas without additional distributional and Laplace analysis.

Olsen and Gupta (2024, Section III.3) already calculate the stationary second moment for *precisely the harmonic-exploration/partial-reset mechanism*, and Sections IV.2–IV.3 analyze its thermodynamic work. Their paper explicitly notes that the full exact stationary law in a nonzero potential is difficult to obtain; it does not supply the normalized conditional-variance endpoint law or the sharp far-tail coefficient. This is the closest physical-model overlap and materially narrows what is claimed as new. A separate earlier result about a synchronously fully-reset ensemble of OU particles resolves a large-particle-number energy edge, not the single-particle, partially-reset far spatial tail here.

Biroli and colleagues (2024) study unconfined diffusion with proportional resetting; its stationary far tail is exponential, not Gaussian with a power correction. Grzywny and colleagues (first posted 2024) also treat partial resetting of Lévy/stable drivers without an independent harmonic confinement term, and obtain different density and transition asymptotics. Trajanovski and colleagues (2023) study Ornstein–Uhlenbeck diffusion with *complete* resetting to a fixed position, a boundary case of the present parameter range; no novelty is claimed for that boundary alone. Frydel (2026) investigates switching harmonic stiffness and Gaussian variance mixtures, including alternating trapping and release, but not the instantaneous map \(X\mapsto qX\) at Poisson epochs; only its abstract was accessible during comparison. The possible existence of an unindexed general Gaussian-mixture endpoint theorem is a remaining priority risk.

## Limitations

The theorem requires constant positive OU drift and diffusion, an independent Poisson clock, and a fixed amplitude \(0\le q<1\). It does not assert uniformity of the tail approximation as \(q\uparrow1\), and it does not treat random reset multipliers, heavy-tailed waiting times, nonharmonic traps, nonstationary initial data, or finite-time rare-event asymptotics. The result has received self-review only, not an independent audit or external publication-priority determination.

## References

1. J. Assefa, M. Keller-Ressel, and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1, first submitted 2026-10-01. https://arxiv.org/abs/2610.01363
2. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387, first submitted 2024-06-12. https://arxiv.org/abs/2406.08387
3. T. Grzywny, K. Szczypkowski, Z. Palmowski, and B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626, first submitted 2024-12-20. https://arxiv.org/abs/2412.15626
4. P. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: particle dynamics under comb constraints and stochastic resetting*, Phys. Rev. E **107**, 054129 (2023); arXiv:2301.12304. https://arxiv.org/abs/2301.12304
5. K. Stølevik Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919, first submitted 2024-01-22; J. Phys. A 57 (2024) 245001. https://arxiv.org/abs/2401.11919
6. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173, submitted 2026-07-06. https://arxiv.org/abs/2607.05173
