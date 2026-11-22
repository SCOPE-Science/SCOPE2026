# A frozen-rate Ornstein–Uhlenbeck window and algebraic sign memory in Brownian-squared confinement

## Finding

Let \(B\) and \(W\) be independent standard Brownian motions beginning at zero. Fix \(a\geq0\), \(b>0\), \(D>0\), and deterministic \(x_0\in\mathbb R\). Let \(X\) be the unique continuous solution of
\[
 dX_t=-(a+bB_t^2)X_t\,dt+\sqrt{2D}\,dW_t,\qquad X_0=x_0.
\]
For every finite \(H>0\), as \(T\to\infty\), the **joint process** converges in \(\mathbb R\times C([0,H])\):
\[
 \left(\frac{B_T}{\sqrt T},\ \bigl(\sqrt T X_{T+u/T}\bigr)_{0\leq u\leq H}\right)
 \ \Longrightarrow\ (G,(Y_u)_{0\leq u\leq H}). \tag{1}
\]
Here \(G,Z\) are independent standard normal variables, \(\widetilde W\) is a standard Brownian motion independent of both, and, conditionally on \(G\ne0\),
\[
 Y_0=\sqrt{\frac D b}\frac{Z}{|G|},\qquad
 dY_u=-bG^2Y_u\,du+\sqrt{2D}\,d\widetilde W_u. \tag{2}
\]
Thus \(Y\) is a mixture of **stationary** Ornstein–Uhlenbeck processes with the random, time-independent relaxation rate \(bG^2\). The event \(G=0\) has probability zero and may be defined arbitrarily.

Write \(\operatorname{sgn}(0)=0\). For each fixed \(u\geq0\), the microscopic-lag sign correlation has the exact limiting law
\[
 C_b(u):=\lim_{T\to\infty}\mathbb E\bigl[\operatorname{sgn}(X_T)\operatorname{sgn}(X_{T+u/T})\bigr]
 =\frac2\pi\mathbb E\bigl[\arcsin(e^{-bG^2u})\bigr]. \tag{3}
\]
As \(u\to\infty\), this **limiting** correlation has the sharp, non-integrable algebraic tail
\[
 C_b(u)\sim\frac{K}{\sqrt{bu}},\qquad
 K=\frac{\sqrt2}{\pi}\sum_{n=0}^{\infty}
 \frac{\binom{2n}{n}}{4^n(2n+1)^{3/2}}
 =0.538851623662\ldots. \tag{4}
\]
The limiting sign correlation is independent of \(a,D,x_0\). Equation (4) is a sequential limit, first \(T\to\infty\) at fixed \(u\), then \(u\to\infty\); it does **not** assert a uniform estimate when \(u\) grows with \(T\).

## Assumptions and scope

Time is in units for which \(\langle B\rangle_t=\langle W\rangle_t=t\). The fluctuating stiffness is the square of an **unconfined**, unreset Brownian environment, with strictly positive coupling \(b\); the thermal noise is independent and nondegenerate. The static stiffness \(a\) is nonnegative. The observation window is the physical interval \([T,T+H/T]\), and the statement is weak convergence in the uniform path topology, not almost-sure convergence or convergence of unbounded moments. All lag and large-time limits have the order stated above.

## Proof

**1. Exact conditional Gaussian law.** Set \(A_t=at+b\int_0^tB_s^2ds\). The integrating-factor solution gives, conditional on the entire environment up to \(t\), a normal variable with mean
\[
 m_t=x_0e^{-A_t}
\]
and variance
\[
 V_t=2D\int_0^t\exp\!\left[-2as-2b\int_{t-s}^tB_v^2dv\right]ds. \tag{5}
\]
This is exact by independence of \(W\) and \(B\), not a quasistatic approximation.

**2. Endpoint variance concentration.** Brownian scaling identifies the joint law of \((B_T/\sqrt T,TV_T)\) with
\[
 \left(\mathcal B_1,\ 2D\int_0^{T^2}
 \exp\!\left[-\frac{2ay}{T}-2bT^2\int_{1-y/T^2}^1\mathcal B_v^2dv\right]dy\right), \tag{6}
\]
where \(\mathcal B\) is standard Brownian motion on \([0,1]\). On every continuous path with \(\mathcal B_1=g\ne0\), choose \(0<\delta<1\) and \(c>0\) such that \(\mathcal B_v^2\ge c\) for \(v\in[1-\delta,1]\). For fixed \(y\), the integrand in (6) converges to \(e^{-2bg^2y}\). On \(0\le y\le\delta T^2\) it is dominated by \(e^{-2bcy}\); on the rest of the interval the integral is bounded by \(T^2e^{-2bc\delta T^2}\). Dominated convergence therefore yields \(TV_T\to D/(bg^2)\) on this coupling, almost surely. Also
\[
 \sqrt T\,m_T=\sqrt T\,x_0\exp\!\left[-aT-bT^2\int_0^1\mathcal B_v^2dv\right]\longrightarrow0
\]
for almost every Brownian path. Conditional Gaussian representation now gives
\[
 (B_T/\sqrt T,\sqrt T X_T)
 \Longrightarrow(G,\sqrt{D/b}\,Z/|G|), \tag{7}
\]
with \(Z\) independent of \(G\). This endpoint identity is also independently established in earlier work and is cited below; it is a premise here, not asserted as the novel part.

**3. Frozen-coefficient convergence on the whole window.** Put \(Y_T(u)=\sqrt T X_{T+u/T}\), \(G_T=B_T/\sqrt T\), and \(\widetilde W_T(u)=\sqrt T(W_{T+u/T}-W_T)\). Exactly, without approximation,
\[
 dY_T(u)=-\biggl(\frac aT+b\frac{B_{T+u/T}^2}{T}\biggr)Y_T(u)du
 +\sqrt{2D}\,d\widetilde W_T(u). \tag{8}
\]
For each \(H<\infty\), the Brownian maximal inequality gives
\[
 \mathbb E\sup_{0\le u\le H}\left|\frac{B_{T+u/T}-B_T}{\sqrt T}\right|^2
 \le\frac{4H}{T^2}\longrightarrow0. \tag{9}
\]
Since \(G_T\) is tight, the drift coefficient in (8) converges uniformly in probability on \([0,H]\) to \(bG_T^2\). Future increments of \(W\) are independent of \((B_T,X_T)\), and \(\widetilde W_T\) is standard Brownian motion. Replace the random drift of (8) by \(bG_T^2\), preserving its initial condition and Brownian driver. On \([0,H]\), the difference vanishes uniformly in probability: the integrating-factor representation and the nonnegative drift yield the bound
\[
 \sup_{u\le H}|Y_T(u)|\le |Y_T(0)|+2\sqrt{2D}\sup_{u\le H}|\widetilde W_T(u)|,
\]
so the supremum is tight, while Gronwall's inequality bounds the drift perturbation by its uniform size times this tight supremum times \(H\). The frozen-rate OU solution is a continuous function in its initial position, nonnegative rate and driving Brownian path (by integration by parts of the stochastic convolution). Applying (7), future-noise independence, and the continuous mapping theorem proves (1)–(2). Because the normal variance in (7) equals the OU invariant variance \(D/(bG^2)\), the conditional limit starts in its stationary law.

**4. Sign correlations.** Every limiting one-time variable is nonzero almost surely. Likewise, for every fixed \(u\ge0\), the limiting pair has no mass on either coordinate axis, so weak convergence of the pair and bounded convergence through continuity sets imply the first equality in (3). Conditional on \(G=g\ne0\), the pair \((Y_0,Y_u)\) is a centered Gaussian pair with correlation \(\rho=e^{-bg^2u}\). The classical Gaussian quadrant identity, obtained by a polar-angle calculation, is \(\mathbb E[\operatorname{sgn}(U)\operatorname{sgn}(V)]=2\arcsin(\rho)/\pi\). Averaging over the standard normal \(G\) proves (3).

**5. Sharp algebraic memory.** For \(u>0\), the substitution \(y=\sqrt{bu}\,g\) in (3) yields
\[
 \sqrt{bu}\,C_b(u)=\frac{2}{\pi\sqrt{2\pi}}
 \int_{\mathbb R}e^{-y^2/(2bu)}\arcsin(e^{-y^2})\,dy. \tag{10}
\]
The integrand is nonnegative and integrable: it is bounded by \(\pi/2\) near zero and is \(O(e^{-y^2})\) at infinity. Dominated convergence applies. Expanding the positive Taylor series
\[
 \arcsin z=\sum_{n=0}^{\infty}\frac{\binom{2n}{n}}{4^n(2n+1)}z^{2n+1}
\]
and applying Tonelli's theorem and \(\int_0^\infty e^{-cy^2}dy=\sqrt\pi/(2\sqrt c)\), the limiting integral in (10) is exactly the positive convergent series in (4). Its numerical value is checked independently by quadrature and series truncation in the companion file. Since \(K>0\), \(\int_0^\infty C_b(u)du=\infty\) for the limiting sign process. This is non-integrable memory induced by a random spectral edge at zero, **not** a claim of nondecaying correlations at any fixed physical time window.

## Verification

`verify_local_sign.py` (run using `python verify_local_sign.py`, with NumPy and SciPy) tests the exact Gaussian-mixture integral against its positive series representation, the parameter scaling \(C_b(u)=C_1(bu)\), the large-lag prefactor, the small-lag square-root cusp, deterministic endpoint-variance localization and independent Gaussian-pair Monte Carlo. All 26 checks passed. The central path convergence follows from the analytic estimates in Steps 1–3; finite-sample tests do not establish it. No formal proof assistant or outside certification was used.

## Relationship to prior work

Gupta and Klapp [1] introduced this exact Brownian-square fluctuating-stiffness model and obtained conditional-Gaussian formulas, the first four positional moments, and thermodynamic expectations. Their published discussion concerns one-time moments and thermodynamics, and does not supply a microscopic-time process limit or sign-memory law. Their earlier model [2] uses an OU-driven (stationary, possibly negative) stiffness, not the unconfined Brownian-square environment. The previously published finding [3] establishes the one-time scaling and Cauchy limit used in (7), expressly leaving multitime/pathwise limits open. A second finding [4] resolves *fixed-nonzero-displacement* tail intensities but not this bounded sign-correlation or process-level law. The present theorem cannot be inferred from a one-time weak limit alone: the dependence of the future thermal noise on the slowly varying random stiffness must also be controlled on the rescaled time window.

The frozen-rate Gaussian-quadrant/arcsine calculation is standard and not separately claimed to be new. Originality here concerns the **model-specific temporal weak limit**, the exact consequential sign-correlation profile and its sharp non-integrable decay. A more general unpublished quasi-static diffusion theorem could implicitly cover some of the convergence; no universal novelty certification is implied.

## Limitations

The result assumes a finite fixed microtime horizon \(H\) before taking \(T\to\infty\), nonnegative baseline stiffness, independent Gaussian thermal forcing, and the unreset Brownian-square environment. It does not establish joint limits on growing horizons, any interchange of \(T\) and \(u\), convergence of position moments, or physical-time stationarity of \(X\). Because limiting Cauchy variables have infinite variance, the sign correlation is intentionally used in place of a second-moment autocorrelation. The result has not undergone independent audit.

## References

1. D. Gupta and S. H. L. Klapp, *Non-stationary Statistics and Energetics of Brownian Motion under Stochastic Harmonic Confinement*, arXiv:2609.33751v1 (first public 2026-09-27), https://arxiv.org/abs/2609.33751 .
2. D. Gupta and S. H. L. Klapp, *Nonequilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, arXiv:2507.20915v2 (first public 2025-07-28), https://arxiv.org/abs/2507.20915 .
3. *Brownian-powered stochastic traps have sharp heavy-tailed scaling laws*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-brownian-powered-stochastic-traps-have-sharp-heavy-tailed-scalin--0700df2bd162 .
4. *Rare-excursion intensity in Brownian-squared harmonic confinement*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-rare-excursion-intensity-in-brownian-squared-harmonic-confinemen--ac0f8defa0e9 .
