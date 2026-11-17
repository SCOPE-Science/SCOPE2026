# Phase-dependent critical extinction after staggered competition pulses

## Finding
Consider a two-species competitive Lotka–Volterra flow with periodic, species-specific, nonsimultaneous multiplicative pulses. At the exact boundary where species 2 has neutral invasion multiplier into the attracting species-1 resident periodic state, the sign of invasion is **independent** of relative pulse phase, but the leading nonlinear rate of species-2 extinction is **strictly phase dependent**.

Precisely, for every parameter set and initial condition in the scope below, if \(y_n=y(nT^+)\), measured immediately after the pulse applied to species 1, then
\[
\lim_{n\to\infty} n y_n = \frac{1}{(f-ec/b)\,\mathcal I_\phi},\qquad
\mathcal I_\phi=\int_0^\phi E(t)\,dt+m_y\int_\phi^T E(t)\,dt,
\]
where
\[
E(t)=e^{dt}\left(\frac{1+C}{e^{at}+C}\right)^{e/b},\qquad
C=\frac{a}{bX_0}-1,\qquad
X_0=\frac{a(m_xe^{aT}-1)}{b(e^{aT}-1)}.
\]
The coefficient is positive and finite. Moreover,
\[
\frac{d\mathcal I_\phi}{d\phi}=(1-m_y)E(\phi),
\]
so the critical coefficient is strictly monotonic in the timing \(\phi\) whenever the pulse factor \(m_y\ne1\). At a neutral invasion threshold, postponing a suppressive species-2 pulse (\(m_y<1\)) strictly decreases the leading sampled species-2 density.

This is a local asymptotic theorem near a resident periodic orbit, not a claim of global attraction for arbitrary positive initial conditions.

## Assumptions and scope
Fix \(a,b,c,d,e,f,T>0\), pulse factors \(m_x,m_y>0\), and an offset \(0<\phi<T\). Between pulses,
\[
\dot x=x(a-bx-cy),\qquad \dot y=y(d-ex-fy).
\]
At every \(t=nT\) apply \(x(nT^+)=m_x x(nT^-)\), leaving \(y\) unchanged; at every \(t=nT+\phi\) apply \(y((nT+\phi)^+)=m_y y((nT+\phi)^-)\), leaving \(x\) unchanged. The Poincaré section is just after the \(x\)-pulse. Define
\[
R_x=aT+\log m_x,\qquad R_y=dT+\log m_y.
\]
Assume
\[
R_x>0,\qquad R_y=\frac eb R_x,\qquad bf>ce.
\]
There exists a neighborhood of the positive boundary point \((X_0,0)\) in the nonnegative quadrant such that every solution starting in it with \(x(0^+)>0\) and \(y(0^+)>0\) remains positive, converges to the species-1 resident cycle, and satisfies the displayed limit. The neighborhood can depend on the parameters and the phase; no assertion of a common uniform neighborhood is made.

For arbitrary \(R_y\), the species-2 linear invasion multiplier at that resident cycle equals \(\exp(R_y-eR_x/b)\), independently of \(\phi\). Thus the neutrality condition used above is genuinely the phase-independent zero-Floquet-exponent boundary.

## Proof
**1. Resident state.** Along \(y=0\), the scalar flow is logistic. Its positive post-pulse fixed point exists uniquely when \(m_xe^{aT}>1\), equivalently \(R_x>0\), and is
\[
X_0=\frac{a(m_xe^{aT}-1)}{b(e^{aT}-1)},\qquad
X(t)=\frac{a/b}{1+Ce^{-at}},\qquad C=\frac{a}{bX_0}-1>-1.
\]
Here \(0\le t<T\). The integrated resident abundance is
\[
A(t):=\int_0^tX(s)\,ds
=\frac1b\log\frac{e^{at}+C}{1+C},\qquad
bA(T)=R_x.
\]
The last identity also follows by integrating \(d\log X/dt=a-bX\) across a period and including the \(x\)-pulse. The scalar Poincaré multiplier is \(\mu_x=e^{-R_x}\in(0,1)\).

**2. Linear invasion and its phase cancellation.** A small invader satisfies \(\dot Y=(d-eX(t))Y\) between pulses, with \(Y(\phi^+)=m_yY(\phi^-)\) and \(Y(0^+)=1\). Therefore
\[
Y_\phi(t)=E(t)\,m_y^{\mathbf1_{\{t\ge\phi\}}},\qquad E(t)=\exp(dt-eA(t)).
\]
Its one-period multiplier is \(m_y\exp(dT-eR_x/b)=\exp(R_y-eR_x/b)\). Under neutrality this is exactly one, so \(Y_\phi(T^+)=Y_\phi(0^+)=1\). The integral \(\mathcal I_\phi=\int_0^T Y_\phi(t)dt\) is the stated strictly positive formula. Differentiation at the moving pulse time yields \(\mathcal I_\phi'=(1-m_y)E(\phi)\) with \(E(\phi)>0\).

**3. Quadratic normal form from exact logarithmic balance.** The time-\(T\) map is smooth in initial values near \((X_0,0)\) (the pulse times are fixed and the ODE vector field is polynomial). Its eigenvalues are \(e^{-R_x}\) and \(1\), and its second eigenvector has strictly positive invader component. The local center-manifold theorem supplies a smooth one-dimensional center manifold, parameterized by its initial invader density \(u>0\), with
\[
x(0^+)=X_0+\alpha u+O(u^2),\quad y(0^+)=u,\quad
x(t)=X(t)+u\xi(t)+O(u^2),\quad y(t)=uY_\phi(t)+O(u^2).
\]
At first order, the \(x\)-component is periodic over the pulse cycle because the center multiplier is one. The **exact** pulse-period log identity is
\[
\log\frac{x(T^+)}{x(0^+)}=R_x-b\int_0^Tx(t)dt-c\int_0^Ty(t)dt.
\]
Its left side is \(O(u^2)\) along the center manifold and the zeroth-order term vanishes. Hence
\[
\int_0^T\xi(t)dt=-\frac cb\,\mathcal I_\phi.
\]
Likewise,
\[
\log\frac{y(T^+)}{y(0^+)}=R_y-e\int_0^Tx(t)dt-f\int_0^Ty(t)dt,
\]
and the neutrality relation gives
\[
\log\frac{u'}u=-\left(f-\frac{ec}{b}\right)\mathcal I_\phi u+O(u^2).
\]
Thus the reduced section map is
\[
u'=u-\kappa_\phi u^2+O(u^3),\qquad
\kappa_\phi=\left(f-\frac{ec}{b}\right)\mathcal I_\phi>0.
\]
This cancellation eliminates the unknown center-eigenvector tilt and gives the exact nonlinear coefficient rather than a merely formal local expansion.

**4. Attraction and universal sampled amplitude.** On the positive side of the center manifold, the last recurrence decreases small \(u\) toward zero and
\[
\frac1{u'}-\frac1u=\kappa_\phi+O(u).
\]
Summation or Stolz–Cesàro implies \(n u_n\to1/\kappa_\phi\). The other multiplier is strictly inside the unit circle; the local center-stable foliation transfers this asymptotic to all sufficiently near positive initial states (stable-fiber errors decay exponentially and do not affect the \(n^{-1}\) leading term). Continuity of the flow over each bounded inter-pulse time interval yields convergence of the complete trajectory to the resident periodic state. Both phase monotonicity and the invasion phase-independence follow from the exact expressions in Steps 1–2.

## Verification
Run `python verify.py` with Python 3, NumPy, and SciPy installed. The checker independently constructs the full two-kick stroboscopic map by integrating the polynomial ODE, obtains its Jacobian numerically, projects onto the neutral eigenvector, and compares its quadratic coefficient against the analytic expression at three distinct offsets. It also checks the neutral multiplier, resident integral identity, and strict phase ordering. A numerical Taylor check corroborates but does not replace the universal proof above.

## Relationship to prior work
Courcelle, Shaw MacDonald, and Patel (2026) study periodic **simultaneous** multiplicative pulses and establish robust permanence conditions based on invasion growth rates. Their two-species specialization gives the familiar adjusted-growth threshold; it neither considers the offset \(\phi\) nor evaluates an extinction law at equality. Schreiber (2025) establishes a broad flow-kick invasion-growth framework; such general Floquet results do not by themselves give the phase-dependent **quadratic critical coefficient** or the sampled \(n^{-1}\) law. Liu and Chen (2004) investigate bifurcations near boundary periodic solutions, and Jin, Han, and Li (2005) study impulsive two-species competition: full texts of those older studies were not accessible in this investigation, so an unrecognized equivalent computation there is a residual historical-priority risk. This contribution is not a novelty claim about logistic resident cycles, invasion multipliers, or generic center-manifold theory; it is the explicit staggered-pulse critical amplitude and its strict timing derivative.

## Limitations
The theorem concerns a local neighborhood of the attracting species-1 boundary cycle and requires \(bf>ce\), positive demographic parameters, and exactly one fixed-time pulse per species per period. At \(bf=ce\) the quadratic coefficient vanishes and a higher-order analysis is necessary. The statement does not classify globally attracting states, global basins, delayed impulses, or random pulse times. Full-text historical-priority comparisons remain incomplete for the two older publications noted above.

## References
1. E. Courcelle, J. Shaw MacDonald, and S. Patel, *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses*, arXiv:2609.09343v1 (first posted 2026-09-08), https://arxiv.org/abs/2609.09343 .
2. S. J. Schreiber, *Coexistence and Extinction in Flow-Kick Systems: An invasion growth rate approach*, J. Math. Biol. 91 (2025), article 50; arXiv:2507.02157, https://arxiv.org/abs/2507.02157 .
3. B. Liu and L. Chen, *The periodic competing Lotka–Volterra model with impulsive effect*, Math. Med. Biol. 21 (2004), 129–145, https://doi.org/10.1093/imammb/21.2.129 .
4. Z. Jin, H. Maoan, and L. Guihua, *The persistence in a Lotka–Volterra competition systems with impulsive*, Chaos Solitons Fractals 24 (2005), 1105–1117, https://doi.org/10.1016/j.chaos.2004.09.065 .
