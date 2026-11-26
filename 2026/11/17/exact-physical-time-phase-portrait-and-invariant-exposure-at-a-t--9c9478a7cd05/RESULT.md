# Concentration occupation and exposure at a three-reaction chemical center

## Finding

At the center locus of the quadratic chemical system below, concentration occupation and integrated exposure have different limits as a periodic orbit approaches extinction. The physical-time law of the first concentration on a periodic orbit tends to a point mass at zero as the orbit approaches the critical positive pulse, yet its integrated exposure per revolution remains exactly \(2\pi/\omega\). The full critical pulse, which stays strictly in the chemical quadrant at all finite times, has that same total exposure. The occupation density and the first two concentration moments on each periodic orbit are explicit.

## Model and scalar reduction

Use the autonomous system in physical time \(t\),
\[
\dot x=x(Ax-Ay+C),\qquad \dot y=x(Dx-Ay+F),\qquad A>0,\quad D>A,\quad C>F\ge0.
\]
The physical initial conditions are \(x,y>0\). This includes the vertical-center case of the three-reaction mass-action networks studied by Banaji, Boros and Hofbauer [1]. For example, unit rates in \(2\mathsf X\to3\mathsf X+2\mathsf Y\), \(\mathsf X+\mathsf Y\to0\), and \(\mathsf X\to2\mathsf X\) give \((A,D,C,F)=(1,2,1,0)\). Write
\[
\omega=\sqrt{A(D-A)},\quad a=\frac{C-F}{D-A},\quad b=\frac CA,\qquad
u=x-a,\quad w=\frac A\omega(x-y+b),\quad E=u^2+w^2.
\]
Direct differentiation gives \(\dot u=\omega xw\), \(\dot w=-\omega xu\), so \(E\) is constant. The line \(x=0\) consists of equilibria, and the positive equilibrium is \((a,a+b)\). For \(r=\sqrt E>0\) set \(u=r\cos\theta\), \(w=-r\sin\theta\). This yields
\[
x=a+r\cos\theta,\qquad y=x+b+\frac\omega A r\sin\theta,
\qquad \dot\theta=\omega(a+r\cos\theta).
\]
The classical orbital division by \(x\) on \(x>0\) is the center reduction of [1]. The physical-time scalar phase equation is the standard Adler equation up to phase translation [2]. Its drifting, double-root, and locked regimes are not asserted as new scalar dynamics. The distinction here concerns time-weighted chemical observables and admissibility of the critical pulse in the original quadrant.

## Physical occupation and the critical pulse

For \(r\le a\) the least possible \(y\) on the ellipse is at least
\[
a+b-a\sqrt{1+(\omega/A)^2}
=\frac CA-\frac{C-F}{A(1+\sqrt{D/A})}>0.
\]
Hence the whole ellipse lies in the positive quadrant when \(0<r<a\), and the punctured critical ellipse \(r=a\) does so as well. For \(0<E<a^2\), the least physical period, obtained by integrating \(d\theta/[\omega(a+r\cos\theta)]\) over a turn, is
\[
T(E)=\frac{2\pi}{\omega\sqrt{a^2-E}}.
\]
The transform from \((u,w)\) to \((x,y)\) has absolute Jacobian \(\omega/A\), so the elliptic periodic region (including the equilibrium in computing its area) has area \(\pi\omega a^2/A\), not that area for each orbit.

To form the occupation law, choose a time uniformly on a period. The two phase-angle branches at a fixed concentration \(z\in(a-r,a+r)\) each have \(|dz/d\theta|=\sqrt{E-(z-a)^2}\). Weighting by the physical clock and dividing by \(T(E)\) gives the normalized density
\[
p_E(z)=\frac{\sqrt{a^2-E}}{\pi z\sqrt{E-(z-a)^2}},\qquad a-r<z<a+r,
\]
and zero outside that interval. In contrast, integration **against concentration** cancels the time weight: \(x\,dt=d\theta/\omega\). Thus the exposure per cycle is \(2\pi/\omega\) and the mean of \(x\) is \(\sqrt{a^2-E}\). Another factor of \(x=a+r\cos\theta\) gives \(\overline{x^2}=a\sqrt{a^2-E}\). The sine term in the reconstruction of \(y\) integrates to zero in physical time since \(\sin\theta/(a+r\cos\theta)\) has a periodic logarithmic antiderivative for \(r<a\), so \(\overline y=b+\sqrt{a^2-E}\). As \(E\uparrow a^2\), the period diverges while the exposure is unchanged; Markov's inequality applied to the nonnegative occupation law gives convergence of the law of \(x\) to \(\delta_0\).

At \(r=a\), the open arc \(-\pi<\theta<\pi\) has \(\tan(\theta/2)=\omega at\) with time origin at the maximum of \(x\). The half-angle formulas give the complete physical pulse
\[
x(t)=\frac{2a}{1+(\omega at)^2},\qquad
y(t)=b+\frac{2a[1+(\omega^2a/A)t]}{1+(\omega at)^2}.
\]
The strict lower bound on \(y\) above and positivity of \(x\) show physical admissibility for every finite time. This arc joins \((0,b)\) to itself at infinite times and is unique up to time translation on the critical level. The rational formulas give \(t^2x(t)\to2/(\omega^2a)\) and \(t(y(t)-b)\to2/A\) as \(t\to\pm\infty\). The angle sweeps \(2\pi\) just as in the periodic case. Therefore its full exposure is \(\int_{-\infty}^{\infty}x(t)\,dt=2\pi/\omega\), with no division by the infinite flight time.

## Exterior regime (phase-flow consequence)

For \(r>a\), the connected open arc \(x>0\) runs from \(-\arccos(-a/r)\) to \(\arccos(-a/r)\), modulo \(2\pi\). The physical-time integral diverges at both ends due to the simple zeros of the angular speed. Hence the arc in \(x>0\) connects \((0,b-(\omega/A)\sqrt{E-a^2})\) to \((0,b+(\omega/A)\sqrt{E-a^2})\). The logarithmic derivative \(\dot x/x=-\omega r\sin\theta\) tends in forward time to \(-\omega\sqrt{E-a^2}\), so \(\log x(t)/t\) has that limit too. Energy bounds all coordinates, and \(\dot y=x(Dx+F)>0\) on \(y=0,x>0\), so forward trajectories started in the strictly positive quadrant remain there. The backward endpoint and arc need not remain in \(y>0\). There are no other positive-quadrant nonconstant recurrent trajectories. No claim is made off the specified center locus.

## Verification and comparison

The attached `CHECK.py` provides supplementary symbolic checks of conservation and pulse substitution and spot quadratures of period, means and exposure. The displayed derivation supplies the all-parameter argument. The prior work [1] supplies the case-8 realization, center conditions and orbital division, with a related center application in four-reaction systems in [3]. The standard phase clock or quadrature in [2] explains the scalar regimes. The comparison retained here is between normalized physical occupation and unnormalized concentration exposure, including the exactly matched exposure on the complete positive critical trajectory.

1. M. Banaji, B. Boros, and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, [arXiv:2304.02303](https://arxiv.org/abs/2304.02303), Theorem 9, Case 8; DOI 10.1111/sapm.12639.
2. H. Yamaguchi and M. Asano, *Topological phase dynamics described by overtone-synthesized classical and quantum Adler equations*, [arXiv:2602.21451](https://arxiv.org/abs/2602.21451), §II, equations (1)–(2) and the conventional sinusoidal specialization.
3. M. Banaji, B. Boros, and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, [arXiv:2406.13451](https://arxiv.org/abs/2406.13451), Appendix A; DOI 10.1007/s11071-024-10068-1.
