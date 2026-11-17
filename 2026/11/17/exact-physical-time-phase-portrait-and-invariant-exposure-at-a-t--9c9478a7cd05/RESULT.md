# Exact physical-time phase portrait and invariant exposure at a three-reaction chemical center

## Finding

Consider the quadratic kinetic system
\[
\dot x=x(Ax-Ay+C),\qquad \dot y=x(Dx-Ay+F),
\]
with real parameters \(A>0\), \(D>A\), \(C>F\geq0\), on the positive quadrant. Put
\[
\omega=\sqrt{A(D-A)},\quad a=\frac{C-F}{D-A},\quad b=\frac CA,
\quad u=x-a,\quad w=\frac A\omega(x-y+b),\quad E=u^2+w^2.
\]
Here \(E\) is conserved, the positive equilibrium is \((a,a+b)\), and the line \(x=0\) consists of equilibria. The entire forward-positive-quadrant dynamics is determined by the sharp energy boundary \(E=a^2\).

**Interior.** For \(0<E<a^2\), the positive energy level is one periodic orbit, with original physical-time least period, enclosed physical-coordinate area, and per-cycle first-species exposure
\[
T(E)=\frac{2\pi}{\omega\sqrt{a^2-E}},\qquad
\mathcal A_{\mathrm{basin}}=\frac{\pi\omega a^2}{A},\qquad
\int_0^{T(E)}x(t)\,dt=\frac{2\pi}{\omega}.
\]
The area displayed is the area of the *entire periodicity basin* \(0\le E<a^2\), not the area of each individual orbit. The exact time means on each nonstationary periodic orbit are
\[
\overline x=\sqrt{a^2-E},\quad
\overline y=b+\sqrt{a^2-E},\quad
\overline{x^2}=a\sqrt{a^2-E}.
\]
For \(r=\sqrt E\), the physical-time distribution of \(x\) has density
\[
p_E(z)=\frac{\sqrt{a^2-E}}{\pi z\sqrt{E-(z-a)^2}},\qquad
 a-r<z<a+r.
\]
Consequently, the growing period near the boundary coexists with a *constant integrated concentration per revolution* and the occupation measures concentrate at \(x=0\). Precisely, \(T(E)\sim2\pi/[\omega\sqrt{a^2-E}]\) as \(E\uparrow a^2\).

**Critical boundary.** At \(E=a^2\), the only nonstationary positive-half-plane trajectory, up to time translation, is a complete homoclinic pulse to \((0,b)\):
\[
x(t)=\frac{2a}{1+(\omega at)^2},\qquad
 y(t)=b+\frac{2a[1+(\omega^2a/A)t]}{1+(\omega at)^2}.
\]
It remains in the strictly positive quadrant, and
\[
\lim_{t\to\pm\infty}t^2x(t)=\frac2{\omega^2a},\qquad
\lim_{t\to\pm\infty}t(y(t)-b)=\frac2A,\qquad
\int_{-\infty}^{\infty}x(t)\,dt=\frac{2\pi}{\omega}.
\]

**Exterior.** For every initial condition \(x(0)>0,y(0)>0\) with \(E>a^2\), the solution is forward complete, and as \(t\to+\infty\)
\[
(x(t),y(t))\longrightarrow
\left(0,b+\frac\omega A\sqrt{E-a^2}\right),\qquad
\lim_{t\to\infty}\frac{\log x(t)}t=-\omega\sqrt{E-a^2}.
\]
Within the entire open half-plane \(x>0\), each such energy arc is heteroclinic between the two equilibria at \(y=b\mp(\omega/A)\sqrt{E-a^2}\); the backward arc need not remain in \(y>0\). There are no further positive-quadrant nonconstant recurrent trajectories.

## Assumptions and scope

All assertions refer to the stated autonomous quadratic ODE in **original physical time** \(t\), with \(A>0\), \(D>A\), \(C>F\ge0\). Its positive-quadrant interpretation includes the case-8 vertical-center mass-action networks with reactants \(2\mathsf X\), \(\mathsf X+\mathsf Y\), \(\mathsf X\), with equal negative reaction-vector coordinates \((-1,-1)\) on the mixed reactant and the corresponding equality of rates. One concrete network is \(2\mathsf X\to3\mathsf X+2\mathsf Y\), \(\mathsf X+\mathsf Y\to0\), \(\mathsf X\to2\mathsf X\), all with unit rates, yielding \((A,D,C,F)=(1,2,1,0)\).

The periodicity basin is the elliptic region \(E<a^2\) contained in the strictly positive quadrant, and its boundary passes through the degenerate equilibrium \((0,b)\). The phase portrait on \(x=0\) is the pre-existing line of equilibria. The formulas do not apply away from the indicated center rate locus, where the divided linear system may have nonzero trace.

## Proof

**1. Integral and clock.** Differentiate the coordinates. With \(\omega^2=A(D-A)\) and \((D-A)a=C-F\), direct substitution gives
\[
\dot u=\omega xw,\qquad \dot w=-\omega xu.
\]
Thus \(dE/dt=0\). On \(x>0\), the positive change of time \(d\tau=x\,dt\) makes \((u,w)\) a harmonic oscillator \(du/d\tau=\omega w\), \(dw/d\tau=-\omega u\). Set \(u=r\cos\theta\), \(w=-r\sin\theta\), so that \(d\theta/d\tau=\omega\), \(x=a+r\cos\theta\), and
\[
\frac{dt}{d\theta}=\frac{1}{\omega(a+r\cos\theta)},\qquad
 y=x+b+\frac\omega A r\sin\theta.
\]
This is an exact physical-time parametrization, not an unproved topological conjugacy.

**2. Positive quadrant and periods.** For \(r\le a\), the minimum possible \(y\) on the ellipse is
\[
a+b-r\sqrt{1+(\omega/A)^2}
\ge b-a\bigl(\sqrt{D/A}-1\bigr)
=\frac CA-\frac{C-F}{A(1+\sqrt{D/A})}>0.
\]
Therefore all closed levels \(0<r<a\), and the nonstationary part of the critical level \(r=a\), lie in \(y>0\). Since \(a+r\cos\theta>0\) for \(r<a\), each inner circle is traversed in finite original time. The classical elementary integral, obtained for example by the substitution \(s=\tan(\theta/2)\), is
\[
\int_0^{2\pi}\frac{d\theta}{a+r\cos\theta}
=\frac{2\pi}{\sqrt{a^2-r^2}}.
\]
Hence the exact least period. The coordinate transformation from \((u,w)\) to \((x,y)\) has absolute Jacobian \(\omega/A\), yielding the basin area. Also \(x\,dt=d\theta/\omega\), proving invariant exposure. For averages,
\[
\int_0^T y\,dt=\int_0^T x\,dt+bT
+\frac\omega A r\int_0^{2\pi}\frac{\sin\theta}{\omega(a+r\cos\theta)}d\theta,
\]
where the last integral vanishes as an exact derivative of \(\log(a+r\cos\theta)\). Similarly \(\int_0^T x^2dt=(1/\omega)\int_0^{2\pi}(a+r\cos\theta)d\theta=2\pi a/\omega\). Two angular branches contribute to the time spent in \(x\in(z,z+dz)\), giving the stated normalized density. Its concentration at zero follows since the time mean \(\overline x\to0\), \(x\ge0\), and Markov's inequality bounds \(\Pr(x>\varepsilon)\le\overline x/\varepsilon\).

**3. Rational critical pulse.** At \(r=a\), restrict \(-\pi<\theta<\pi\). Then
\[
\omega at=\tan(\theta/2),\quad
x=a(1+\cos\theta),\quad
w=-a\sin\theta,
\]
with the time origin at the maximum of \(x\). The half-angle formulas yield the two rational expressions. They are defined for every real \(t\), give the asserted exact tail constants, and have total exposure \(2\pi/\omega\). There is only one open critical arc because the circle is tangent to \(x=0\) at exactly one point. This proves uniqueness up to time translation, without claiming that the other stationary points on the line are homoclinic.

**4. Exterior and all-orbit classification.** If \(r>a\), the accessible portion of each invariant circle in \(x>0\) is the unique connected arc satisfying \(a+r\cos\theta>0\). Its endpoints occur at \(u=-a\) and \(w=\pm\sqrt{r^2-a^2}\). Original time diverges logarithmically as either endpoint is approached because \(dt/d\theta\) has a simple pole. The future endpoint has \(w=-\sqrt{E-a^2}\), hence \(y\to b+(\omega/A)\sqrt{E-a^2}\). Linearizing the *scalar original-time equation for \(x\)* along the fixed-energy arc gives \(\dot x/x\to-\omega\sqrt{E-a^2}\). Time averaging this logarithmic derivative proves the sharp exponential rate. Boundedness on each fixed ellipse prevents forward finite-time escape. On \(y=0,x>0\), \(\dot y=x(Dx+F)>0\), so positive-quadrant solutions stay positive. Any initial condition lies on one of the levels just classified, including \(E=0\) and \(x=0\).

## Verification

The accompanying standalone Python script `CHECK.py` derives \(dE/dt=0\) by symbolic differentiation and substitution of \(\omega^2=A(D-A)\), substitutes the rational critical pulse directly into both original equations, and numerically checks the period, physical-time concentration means, and integrated pulse for several noncritical energy levels in the exact network example. It prints `VERTICAL_HOPF_FULL_PHASE_CLOCK_AND_PULSE_OK` when its checks pass. The infinite statements are proved analytically above, rather than inferred from numerical checks.

## Relationship to prior work

Banaji, Boros, and Hofbauer (2023/2024), in their classification of three-reaction quadratic mass-action oscillators, prove that the case with reactants \(2\mathsf X\), \(\mathsf X+\mathsf Y\), and \(\mathsf X\) has a positive center precisely on the relevant linear-trace locus, and explicitly reduce its dynamics by division by \(x\). Their 2024 work on quadratic networks further invokes the same division to show existence of centers. Those **known center classifications, network constraints, and the oscillator reduction are not new claims here**. The contribution is the combined *global original-time* distinction between periodic occupation, the sharp degenerate homoclinic boundary, and exponential line-of-equilibria capture, with the exact period, time distribution, and concentration-exposure identities. The related homoclinic Bogdanov–Takens systems in the 2024 article have a different vector field and nondegenerate local-bifurcation mechanism.

## Limitations

The theorem covers only the specified positive coefficients and equality-of-rates center locus, not perturbations away from it. On an exterior level the backward continuation may leave the positive quadrant, so the two-ended heteroclinic statement is deliberately made on \(x>0\) rather than the chemical state space. The formula for \(p_E\) concerns time sampling *on a specified periodic orbit*, not transient ensemble distributions. The proof is self-contained, but equivalently phrased unpublished or poorly indexed prior results cannot be excluded. No independent mathematical audit has been performed.

## References

1. M. Banaji, B. Boros, and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, arXiv:2304.02303 (first posted 2023-04-05), Studies in Applied Mathematics, DOI: 10.1111/sapm.12639. https://arxiv.org/abs/2304.02303 ; https://doi.org/10.1111/sapm.12639
2. M. Banaji, B. Boros, and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, arXiv:2406.13451 (first posted 2024-06-19), Nonlinear Dynamics 112 (2024), DOI: 10.1007/s11071-024-10068-1. https://arxiv.org/abs/2406.13451 ; https://doi.org/10.1007/s11071-024-10068-1
