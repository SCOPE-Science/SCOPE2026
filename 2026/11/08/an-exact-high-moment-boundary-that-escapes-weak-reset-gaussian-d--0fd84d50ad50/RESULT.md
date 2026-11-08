# An exact high-moment boundary that escapes weak-reset Gaussian diffusion

## Finding
For a common-shock Brownian gas with proportional partial resets, **the exact process and its standard Gaussian diffusion approximation have the same stationary second moment, but different sharp higher-moment integrability thresholds**. In particular the diffusion approximation can predict infinite simultaneous-square correlation when the original model's correlation is finite. At reset size \(s\downarrow0\), the disagreement persists throughout an interval of moment orders of length asymptotic to a strictly positive constant times \(s^{-1}\).

Precisely, let \(N\ge2\), \(D,\lambda>0\), \(0<s<1\), and \(0<\gamma<\lambda\). Between common Poisson events of rate \(\lambda/s\), independent Brownian coordinates evolve by
\[
 dX_i(t)=\gamma X_i(t)\,dt+\sqrt{2D}\,dW_i(t),\quad i=1,\ldots,N,
\]
and each event simultaneously maps \(X_i\mapsto (1-s)X_i\). Write \(a=1-s\) and, for every integer \(p\ge1\),
\[
 \Delta_p=\frac{\lambda}{s}(1-a^{2p})-2p\gamma,\qquad
 \overline\Delta_p=2p(\lambda-\gamma)-p(2p-1)\lambda s.
\]
Both the exact process and the Gaussian approximation described below have unique stationary laws. Their stationary conditional variances \(V\) and \(\overline V\) satisfy
\[
 \mathbb EV^p<\infty\ \Longleftrightarrow\ \Delta_p>0,
 \qquad
 \mathbb E\overline V^p<\infty\ \Longleftrightarrow\ \overline\Delta_p>0.
\]
If the moment exists, its exact value is
\[
 \mathbb EV^p=\frac{(2D)^p p!}{\prod_{j=1}^p\Delta_j},
 \qquad
 \mathbb E\overline V^p=\frac{(2D)^p p!}{\prod_{j=1}^p\overline\Delta_j}.
\]
For distinct coordinates \(i_1,\ldots,i_k\) and integers \(m_j\ge1\), with \(p=\sum_jm_j\),
\[
 \mathbb E\prod_{j=1}^{k}X_{i_j}^{2m_j}
 =\left[\prod_{j=1}^{k}(2m_j-1)!!\right]\mathbb EV^p,
\]
and the same statement holds for the approximation with bars; the expectation is infinite exactly when the relevant variance moment is infinite. Thus this theorem governs all even joint moments in the gas, not merely its one-particle marginal.

For every \(p\ge2\) and \(0<s<1\), the exact integrability threshold strictly exceeds the Gaussian one:
\[
 \frac{1-(1-s)^{2p}}{2ps}>1-\frac{2p-1}{2}s.
\]
Equality holds for \(p=1\). When \(\Delta_2>0\), for distinct particles \(i\ne j\),
\[
 \operatorname{Cov}(X_i^2,X_j^2)
 =\frac{4D^2(\lambda/s)[1-(1-s)^2]^2}{\Delta_1^2\Delta_2}>0.
\]
At \(s=\tfrac12\), \(D=\lambda=1\), and \(\gamma=\tfrac13\), the exact stationary common variance satisfies \(\mathbb EV=\tfrac{12}{5}\), \(\mathbb EV^2=\tfrac{1152}{65}\), and \(\operatorname{Cov}(X_1^2,X_2^2)=\tfrac{3888}{325}\); the Gaussian surrogate has \(\overline\Delta_2=-\tfrac13\), hence an infinite fourth moment and an undefined finite cross-square covariance. This misclassification is possible at every reset fraction \(0<s<1\): it occurs whenever
\[
 0<\gamma<\lambda,\qquad
 \lambda(1-\tfrac32s)\le\gamma<
 \lambda(1-\tfrac32s+s^2-\tfrac14s^3).
\]

Fix \(c=\gamma/\lambda\in(0,1)\), and let \(z_c>0\) be the unique root of
\[
 \frac{1-e^{-2z_c}}{2z_c}=c.
\]
Write \(P_s\) and \(\overline P_s\) for the largest positive integer with finite stationary variance moment in the exact and Gaussian models, respectively. Then
\[
 P_s=\frac{z_c}{s}+O(1),\qquad
 \overline P_s=\frac{1-c}{s}+O(1),\qquad
 P_s-\overline P_s=\frac{z_c-(1-c)}{s}+O(1),
\]
where \(z_c>1-c\). Equivalently, for moment orders \(p_s=\lfloor z/s\rfloor\), the exact cutoff is \(z_c\), whereas the surrogate cutoff is \(1-c\), away from their respective boundary points. The resulting \(s^{-1}\)-scale discrepancy is nonuniformity of the diffusion approximation in the moment order, **not** a claim of failure for each fixed finite moment as \(s\to0\).

## Assumptions and scope
The exact reset clock is homogeneous Poisson of intensity \(\lambda/s\), independent of all independent, standard real Brownian motions. A reset multiplies every position by the deterministic factor \(a=1-s\). There is no additive advection, interaction or independent reset clock. The stated range \(0<\gamma<\lambda\) guarantees stationarity for every \(s\in(0,1)\) in both compared models. The Gaussian approximation is the common-noise Itô system
\[
 d\overline X_i=(\gamma-\lambda)\overline X_i\,dt
 +\sqrt{\lambda s}\,\overline X_i\,dB_0
 +\sqrt{2D}\,dW_i,
\]
where \(B_0\) is one Brownian motion shared across all particles and independent of the \(W_i\). This is the multi-particle diffusion approximation of Galla [1, main Eq. (6) and supplement Eq. (S24)] in the linear drift specialization.

## Proof
**1. Stationary Gaussian mixtures.** With a two-sided stationary Poisson reset clock, conditioned on its history, the \(X_i\) are independent centered Gaussians with common random variance
\[
 V=2D\int_0^\infty e^{2\gamma u}a^{2N_u}\,du,
\]
where \(N_u\) counts resets in a backward interval of length \(u\). By the Poisson strong law, \(N_u/u\to\lambda/s\) almost surely, so the integral is finite since \(\gamma<\lambda<-(\lambda/s)\log(1-s)\). Contractivity of the difference of two solutions driven by the same Brownian and reset noises supplies uniqueness of the invariant law; the logarithmic decay exponent is strictly negative.

Likewise, conditional on the shared environmental Brownian motion, the Gaussian surrogate has i.i.d. centered normal coordinates with the common variance
\[
 \overline V=2D\int_0^\infty
 \exp\!\left([2(\gamma-\lambda)-\lambda s]u
      +2\sqrt{\lambda s}\,B_u\right)\,du.
\]
This is finite almost surely since \(B_u/u\to0\) and \(\gamma<\lambda\), and the same coupling argument establishes uniqueness. Both mixtures have conditional independence, giving the claimed mixed even moments by Gaussian moment factorization, with nonnegative random integrands.

**2. Exact necessary and sufficient moment thresholds.** The two conditional variances are stationary versions of Markov processes with, respectively, the generators
\[
 \mathcal L f(v)=(2\gamma v+2D)f'(v)
 +\frac\lambda s[f(a^2v)-f(v)],
\]
\[
 \overline{\mathcal L}f(v)=
 [2(\gamma-\lambda)+\lambda s]v f'(v)
 +2D f'(v)+2\lambda s v^2 f''(v).
\]
For \(p\ge1\), applying these to \(v^p\) yields
\[
 \mathcal L v^p=-\Delta_p v^p+2Dp v^{p-1},\quad
 \overline{\mathcal L}v^p=-\overline\Delta_p v^p+2Dp v^{p-1}.
\]
If the stationary \(p\)-th moment is finite, then the generators are integrable. Stationarity, justified by stopping and then dominated convergence, implies \(\Delta_p\mathbb EV^p=2Dp\mathbb EV^{p-1}>0\), and similarly with bars. Thus positive denominators are necessary, including at equality where the moment diverges.

Conversely, if \(\Delta_p>0\), Minkowski's inequality in \(L^p\), applied to the nonnegative Poisson integral, gives
\[
 \|V\|_p\le2D\int_0^\infty
 \left(\mathbb E e^{2p\gamma u}a^{2pN_u}\right)^{1/p}du
 =\frac{2Dp}{\Delta_p}<\infty.
\]
The same argument for the geometric-Brownian integral gives \(\|\overline V\|_p\le2Dp/\overline\Delta_p\) whenever \(\overline\Delta_p>0\). The ratio \((1-a^{2p})/p\) decreases in \(p>0\), as does the corresponding Gaussian scaled denominator, so positivity at order \(p\) implies positivity at all smaller integer orders. Induction in the generator identities proves both product formulas. The equality and negative cases were already excluded by necessity.

**3. Strict threshold gap and exact cross-square covariance.** For every integer \(p\ge2\), Taylor's theorem applied to \((1-s)^{2p}\) at \(s=0\) through quadratic order has a strictly negative remainder on \(0<s<1\), because its third derivative is negative. Rearrangement proves the stated strict inequality. For \(p=1\), the quadratic truncation is exact. Conditional Gaussian independence gives \(\operatorname{Cov}(X_i^2,X_j^2)=\operatorname{Var}(V)\). Substitution of the product formulas yields
\[
 \operatorname{Var}(V)=\frac{4D^2(2\Delta_1-\Delta_2)}{\Delta_1^2\Delta_2},\qquad
 2\Delta_1-\Delta_2=\frac\lambda s(1-a^2)^2.
\]
The rational example follows by direct substitution. The nonempty parameter strip follows by setting \(\overline\Delta_2\le0<\Delta_2\); its width is \(\lambda(s^2-s^3/4)>0\).

**4. Singular high-order window.** For integer \(p_s\) with \(sp_s\to z>0\),
\[
 \frac{\Delta_{p_s}}{2p_s\lambda}\to
 F(z)-c,\quad F(z)=\frac{1-e^{-2z}}{2z},
 \qquad
 \frac{\overline\Delta_{p_s}}{2p_s\lambda}\to 1-c-z.
\]
The function \(F(z)=\int_0^1e^{-2zt}\,dt\) is continuous, strictly decreasing from \(1\) to \(0\); hence \(z_c\) exists and is unique. For every \(z>0\), \(F(z)>1-z\) by strict second-order Taylor comparison for the exponential. Thus \(F(1-c)>c\) and \(z_c>1-c\). Uniformly near the simple root \(z_c\), \((1-s)^{2z/s}=e^{-2z}(1+O(s))\); the implicit-root estimate places the exact real-order cutoff at \(z_c/s+O(1)\). The Gaussian cutoff is \((1-c)/s+1/2\) exactly at real order. Integer rounding changes either by at most one, proving the three integer estimates. This completes the proof.

## Verification
Run `python3 check.py` with Python's standard library. It independently evaluates generator recurrences over rational parameters, directly compares two equivalent exact cross-square covariance expressions, certifies the explicit rational example, tests the strict polynomial inequality over bounded rational grids, checks the singular-window scaling for five drift ratios, and samples the Poisson history integral against its exact first two moments. The packaged program records the number of checks and raises an assertion on discrepancy. The exact rational checks are identities at the sampled inputs; the finite numerical tests and Monte Carlo sample do **not** constitute proofs of the universal claims, which instead follow from the preceding arguments.

## Relationship to prior work
Galla [1] introduced the weak-reset diffusion approximation, the common environmental noise of the multi-particle Gaussian surrogate, and its stationary square-correlation formula (main Eq. (8), supplement section S2.2). Its primary and supplemental text were examined. These are prior results, **not** claimed here. The additional claims established here concern finite-reset *exact* moment existence for arbitrary joint even moments, a sharp strict integrability-threshold comparison and the \(p\asymp s^{-1}\) nonuniform breakdown, including the explicit finite-versus-infinite cross-square counterexample. Pierce [2] treats partial resetting with constant advection and derives moment relations in that different model. Biroli and collaborators [3] analyze one free diffusing particle under position rescaling, without the unstable linear drift or a common-clock multi-particle Gaussian approximation. The general phenomenon of heavy tails in multiplicative stochastic processes predates these works; the underlying generator and Gaussian-mixture principles are not presented as new techniques.

## Limitations
This is an analytical result for one linear, common-clock Brownian model with deterministic proportional partial resets and its specified leading Gaussian approximation. It makes no claim of uniform accuracy of the approximation for tail probabilities, of an exact full stationary density, or of a broader nonlinear universality class. Moment divergence cannot be inferred from finite numerical samples. The high-order discrepancy does not contradict fixed-order convergence as \(s\to0\). Earlier general theorems on stochastic affine recursions or Poisson-driven perpetuities could imply parts of the moment criterion; the assessed potentially new content is the integrated sharp comparison for the specific simultaneous-reset model, and publication-priority verification remains non-independent.

## References
[1] T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (2026-02-25), https://arxiv.org/html/2602.21635.

[2] J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (2022), https://arxiv.org/abs/2204.07215.

[3] M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (2024), https://arxiv.org/abs/2406.08387.
