# A universal persistence-scale critical autocorrelation crossover in the active spherical Debye model

## Finding
For the exactly specified critical, uncondensed, continuum Debye version of the stationary active spherical model, the persistent-force correlation is the leading correlation on the persistence time scale. Its first positive correction has a universal scaling function and two different sharp power laws.

Fix a real Debye spectral dimension \(4<d<6\). For force persistence \(\tau>0\), let \(C_\tau(t)\) be the normalized thermodynamic-limit stationary mode-averaged autocovariance at the critical temperature defined below. At every \(s>0\),
\[
\lim_{\tau\to\infty}\tau^{(d-4)/2}\bigl[C_\tau(\tau s)-e^{-s}\bigr]=\Phi_d(s),\qquad
\Phi_d(s)=(d-4)\int_0^\infty\frac{z^{d-3}(e^{-sz^2}-e^{-s})}{1-z^4}\,dz>0.
\]
The quotient at \(z=1\) takes its continuous value \(se^{-s}/2\) before multiplication by \(z^{d-3}\). Convergence is locally uniform for \(s\in(0,\infty)\), and
\[
\Phi_d(s)\sim\frac{(d-4)\Gamma((d-4)/2)}{6-d}s^{(6-d)/2}\quad(s\downarrow0),
\qquad
\Phi_d(s)\sim\frac{d-4}{2}\Gamma((d-2)/2)s^{-(d-2)/2}\quad(s\to\infty).
\]
The integer-dimensional interior case has a closed form:
\[
\Phi_5(s)=\frac\pi4\bigl[e^{-s}(1+\operatorname{erfi}(\sqrt{s}))-e^s\operatorname{erfc}(\sqrt{s})\bigr],
\quad \Phi_5(1)=0.429969029096485\ldots.
\]
Here \(\operatorname{erfi}(x)=2\int_0^xe^{y^2}dy/\sqrt\pi\), while \(\operatorname{erfc}(x)=2\int_x^\infty e^{-y^2}dy/\sqrt\pi\).

## Assumptions and scope
We work in the infinite-mode continuum Debye model, **not** at finite particle number. The positive-mode spectral measure is the probability density \(d\omega^{d-1}\,d\omega\) on \(0<\omega<1\). Mode-wise dynamics are independent stationary Gaussian systems
\[
 du_\omega=-\omega^2 u_\omega\,dt+f_\omega\,dt,\qquad
 df_\omega=-\tau^{-1}f_\omega\,dt+\sqrt{2T}\,\tau^{-1}dW_\omega.
\]
The notation for continuum independent modes is interpreted through their spectral integrals; the zero spectral point has zero mass. The Lagrange multiplier is exactly \(\mu=0\), and the force amplitude equals the \(\tau\)-dependent **critical** value
\[
T=T_c(\tau)=\left[d\int_0^1\frac{\omega^{d-3}}{1+\tau\omega^2}\,d\omega\right]^{-1}.
\]
This imposes \(C_\tau(0)=1\). In particular \(T_c(\tau)/\tau\to(d-4)/d\). We study two-time stationary covariances at \(t\ge0\), with no assumption of a time-dependent spherical multiplier or a below-critical condensate. Dimension \(d\) need not be an integer except for the \(d=5\) illustration.

## Proof
**1. Single-mode stationary covariance.** Put \(a=\omega^2>0\). The triangular Ornstein–Uhlenbeck moment equations give \(\mathbb E f^2=T/\tau\), \(\mathbb E(uf)=T/(1+a\tau)\) and \(\mathbb E u^2=T/[a(1+a\tau)]\). Differentiating the stationary two-time covariance and conditioning on the two-dimensional Markov state yields
\[
 c_a(t)=\frac{T}{a(1+a\tau)}\,
 \frac{e^{-at}-a\tau e^{-t/\tau}}{1-a\tau}\quad(t\ge0).
\]
At \(a\tau=1\), the quotient extends continuously to \((1+t/\tau)e^{-t/\tau}\). This extension is required at the resonance and eliminates an artificial pole. In particular \(c_a(0)=T/[a(1+a\tau)]\).

**2. Exact critical spectral identity.** Integrating against the Debye probability measure, and using the critical normalization \(C_\tau(0)=1\), gives exactly
\[
 C_\tau(\tau s)-e^{-s}
 =dT_c(\tau)\int_0^1\omega^{d-3}
 \frac{e^{-s\tau\omega^2}-e^{-s}}{1-\tau^2\omega^4}\,d\omega.
\]
This is an ordinary continuous integrand at \(\tau\omega^2=1\). After \(z=\sqrt\tau\,\omega\),
\[
\tau^{(d-4)/2}[C_\tau(\tau s)-e^{-s}]
 =\frac{dT_c(\tau)}\tau\int_0^{\sqrt\tau}
 \frac{z^{d-3}(e^{-sz^2}-e^{-s})}{1-z^4}\,dz.
\]

**3. Existence and positivity of the crossover.** For each fixed \(s>0\), the integrand behaves as \(O(z^{d-3})\) at zero and as \(O(z^{d-7})\) at infinity. The first is integrable because \(d>2\); the second because \(d<6\). The removable value at \(z=1\) is positive. Moreover \(e^{-sz^2}-e^{-s}\) has exactly the same sign as \(1-z^4\), so the integrand is strictly positive for \(z>0\). Since \(dT_c(\tau)/\tau\to d-4\) by dominated convergence after multiplying the critical-temperature integral by \(\tau\), the stated limit follows. Uniform majorants for \(s\) in compact subsets of \((0,\infty)\) prove local uniformity.

**4. The short scaled-time power.** With \(z=y/\sqrt{s}\), write the scaled kernel as \(s^{(6-d)/2}y^{d-7}(1-e^{-y^2})\) times a factor tending to one for \(y>0\). Splitting at \(y=\sqrt{s}\), and using \(1-e^{-y^2}\le\min(y^2,1)\), supplies an integrable dominator in the regime \(4<d<6\). The limiting integral equals
\[
 \int_0^\infty y^{d-7}(1-e^{-y^2})dy
 =\frac{\Gamma((d-4)/2)}{6-d},
\]
by the substitution \(q=y^2\) and integration by parts. This gives the first asymptotic and shows why it is nonanalytic for \(4<d<6\).

**5. The long scaled-time power.** Split the integral at any fixed \(0<\epsilon<1\). On \((0,\epsilon)\), substitute \(z=y/\sqrt{s}\) and apply dominated convergence to obtain \(\frac12\Gamma((d-2)/2)s^{-(d-2)/2}\). The remaining portion is exponentially small in \(s\) (with a harmless removable point at \(z=1\)); the far tail beyond \(z=1\) is \(O(e^{-s})\) after a fixed separation from that point. Therefore the second asymptotic follows.

**6. Exact five-dimensional profile.** For \(d=5\), decompose \(z^2/(1-z^4)=\frac12[(1-z^2)^{-1}-(1+z^2)^{-1}]\). The numerator vanishes at \(z=1\), so the first integral can be evaluated by the real principal-value Gaussian integral \(\int_0^\infty e^{-sz^2}(1-z^2)^{-1}dz=\frac\pi2 e^{-s}\operatorname{erfi}(\sqrt{s})\), while its constant numerator term has zero principal value. The second integral uses \(\int_0^\infty e^{-sz^2}(1+z^2)^{-1}dz=\frac\pi2e^s\operatorname{erfc}(\sqrt{s})\), and \(\int_0^\infty(1+z^2)^{-1}dz=\pi/2\). These yield the claimed closed form. Every equality is between finite quantities when the two terms are combined before evaluation.

## Verification
The embedded \`verify.py\` uses only Python 3 standard-library numerical quadrature. It independently evaluates the finite-\(\tau\) critical autocovariance in the original mode variable and the transformed spectral variable; checks their agreement, their convergence to the five-dimensional closed form, and the two endpoint scaling regimes. It passed 38 deterministic assertions when executed from the final package. These checks sample finite parameters and **do not** prove the uniform or infinite-limit statements; Steps 1–6 constitute the proof.

## Relationship to prior work
Ikeda, *Active Spherical Model*, arXiv:2208.10200 (first public version 22 August 2022), supplies the same Gaussian active spherical Debye setup, the stationary mode variance, and the static critical-temperature/critical-dimension analysis. Its Sections III–V and concluding discussion do not present the persistence-scale stationary temporal autocorrelation correction or the two sharp scaling-function exponents. They are specifically credited as premises, not re-presented as new results. Ikeda, *Interaction-free ergodicity-breaking driven by temporally hyperuniform noise*, arXiv:2503.06590 (9 March 2025), studies a distinct force spectrum and a different norm-constrained stochastic model. Generic covariance formulas for linear Gaussian systems give the first-mode computation, but not by themselves the stated critical Debye continuum asymptotics. Available source searches have not established publication priority conclusively; a structurally equivalent but unindexed temporal-crossover theorem remains a risk.

## Limitations
The result applies only to stationary Gaussian modes at \(\mu=0\), the exactly specified Debye density, and \(4<d<6\), with \(T=T_c(\tau)\). It does not establish behavior for a finite-\(N\) zero mode, a hard spherical constraint at every instant, a nonlinear interacting model, other driving-noise spectra, or dimensions at/beyond the logarithmic borderlines \(d=4,6\). The limit is first \(\tau\to\infty\) at fixed \(s>0\), followed separately by \(s\downarrow0\) or \(s\to\infty\); no joint-rate uniformity beyond compact positive \(s\)-intervals is asserted.

## References
- H. Ikeda, *Active Spherical Model*, arXiv:2208.10200v1, publicly posted 2022-08-22, https://arxiv.org/abs/2208.10200 ; full text https://arxiv.org/html/2208.10200v2 .
- H. Ikeda, *Interaction-free ergodicity-breaking driven by temporally hyperuniform noise*, arXiv:2503.06590v1, publicly posted 2025-03-09, https://arxiv.org/abs/2503.06590 .
- T. H. Berlin and M. Kac, *The Spherical Model of a Ferromagnet*, Physical Review **86** (1952), 821–835 (classical background, not a source of the persistence correction).
