# Exact mode and edge transitions of the Poisson-reset Adler phase

## Finding
For two positively detuned sinusoidally coupled phase oscillators whose phases are simultaneously returned to zero at independent Poisson times, the stationary relative-phase density has a complete and sharp morphology classification. It has two independent reset-rate thresholds in the phase-locked sector: the linear relaxation rate \(\gamma=\sqrt{K^2-\Delta^2}\) controls whether the locking-edge density diverges, stays finite, or vanishes, whereas the coupling \(K\) controls whether the density mode is at the reset point or strictly inside the occupied arc. At the saddle-node \(\Delta=K\), the locking-edge density becomes super-algebraically flat with an explicit essential exponential factor. In the rotating sector \(\Delta>K\), the density develops exactly one interior maximum and one interior minimum if and only if the reset rate is below \(K\).

These statements are made precise below, including every positive parameter and equality boundary.

## Assumptions and scope
Let \(K>0\), \(\Delta>0\), and \(r>0\). Two oscillator phases obey
\[
\dot\theta_1=\omega_1+\frac K2\sin(\theta_2-\theta_1),\qquad
\dot\theta_2=\omega_2+\frac K2\sin(\theta_1-\theta_2),\qquad \omega_1-\omega_2=\Delta.
\]
At the points of an independent rate-\(r\) Poisson process both phases are simultaneously set to zero, instantaneously, with no phase diffusion between resets. The relative phase \(\phi=(\theta_1-\theta_2)\bmod 2\pi\) follows \(\dot\phi=v(\phi)=\Delta-K\sin\phi\) between resets and returns to \(0\) at every reset. All statements concern the unique stationary law sampled at a typical physical time, not a deterministic no-reset invariant distribution or a reset-epoch distribution.

Write \(A(\phi)=\int_0^\phi v(u)^{-1}\,du\), with this integral restricted to the interval reached monotonically before any equilibrium. If \(\Delta>K\), put \(T=\int_0^{2\pi}v(u)^{-1}\,du=2\pi/\sqrt{\Delta^2-K^2}\). The unique stationary density on the circular interval \(0<\phi<2\pi\) is
\[
p(\phi)=\frac{r\exp[-rA(\phi)]}{v(\phi)(1-\exp[-rT])}.
\]
It has a jump at the identified reset point, with \(p(0+)/p(2\pi-)=\exp(rT)\), and has no atom there. When \(r\ge K\) the density strictly decreases along the open arc. When \(0<r<K\) it first increases to its unique interior maximum at \(\phi_+=\arccos(r/K)\), then decreases to its unique interior minimum at \(\phi_-=2\pi-\arccos(r/K)\), and then increases up to the right reset boundary. These are its only interior critical points. Both locations are independent of detuning \(\Delta\).

If \(0<\Delta<K\), put \(\phi_s=\arcsin(\Delta/K)\in(0,\pi/2)\) and \(\gamma=K\cos\phi_s=\sqrt{K^2-\Delta^2}\). The stationary measure is supported on \([0,\phi_s]\), has no atoms, and has density
\[
p(\phi)=\frac{r\exp[-rA(\phi)]}{v(\phi)},\qquad 0<\phi<\phi_s.
\]
At the locking edge, for a finite constant \(C=C(\Delta,K,r)>0\),
\[
p(\phi_s-\delta)\sim C\delta^{r/\gamma-1}\qquad(\delta\downarrow0).
\]
The complete density-shape classification is: if \(0<r<\gamma\), it strictly increases and diverges at the locking edge; if \(r=\gamma\), it strictly increases to the finite positive edge value \(C\); if \(\gamma<r<K\), it has exactly one interior maximum at \(\phi_+=\arccos(r/K)\) and vanishes at the locking edge; if \(r\ge K\), it strictly decreases from the reset point and vanishes at the locking edge. At \(r=K\), the derivative at \(0+\) is zero but the density is strictly decreasing on the open arc.

If \(\Delta=K\), the support is \([0,\pi/2]\), with no atoms, and
\[
p(\phi)=\frac{r}{K(1-\sin\phi)}\exp\left[-\frac rK(\tan\phi+\sec\phi-1)\right],\qquad 0<\phi<\frac\pi2.
\]
Writing \(\delta=\pi/2-\phi\), the sharp essential locking-edge law is
\[
p\left(\frac\pi2-\delta\right)\sim\frac{2re^{r/K}}K\,\delta^{-2}\exp\left[-\frac{2r}{K\delta}\right],\qquad\delta\downarrow0.
\]
Thus this density and all its algebraic rescalings tend to zero at the critical locking point. It has one interior maximum at \(\arccos(r/K)\) if \(r<K\), and is strictly decreasing if \(r\ge K\). The above cases exhaust every \(K,\Delta,r>0\).

## Proof
1. **Uniqueness and reset-age representation.** Couple any two initial states using the same Poisson reset times. They agree from the first reset onward. Their total-variation discrepancy is therefore bounded by \(e^{-rt}\), establishing uniqueness of an invariant law if it exists. The stationary elapsed time since the most recent reset is exponential of rate \(r\), so the invariant law is the pushforward of \(r e^{-ra}\,da\) under the deterministic solution starting at \(\phi=0\). This also constructs existence. For any finite age the deterministic solution is not at a limiting equilibrium, and a continuous age law assigns no mass to a single phase point; therefore no stationary atoms occur.

2. **Exact density.** In the rotating case \(\Delta>K\), the drift is strictly positive everywhere. One circuit takes exactly \(T=2\pi/\sqrt{\Delta^2-K^2}\); every phase \(0<\phi<2\pi\) is reached at ages \(A(\phi)+nT\), for integers \(n\ge0\). The Jacobian of age against phase is \(1/v(\phi)\). Summing \(r\exp[-r(A+nT)]/v\) as a convergent geometric series gives the stated density and jump ratio. In the locked and critical cases the forward trajectory from \(0\) increases strictly to its first equilibrium \(\phi_s\), taking infinite time. There is one arrival age \(A(\phi)\) for each interior \(\phi\), giving the stated density with no geometric factor. Both formulas have total mass one by the age pushforward.

3. **All modes and their uniqueness.** In every interior support interval, differentiate the logarithm of the density:
\[
\frac{p'(\phi)}{p(\phi)}=-\frac{r+v'(\phi)}{v(\phi)}=\frac{K\cos\phi-r}{\Delta-K\sin\phi}.
\]
The denominator is strictly positive on the relevant intervals. On the locked support \((0,\phi_s)\), \(K\cos\phi\) decreases strictly from \(K\) to \(\gamma\), so the derivative has exactly the signs and zero described in the four regimes. At criticality it decreases from \(K\) to zero, giving the stated two regimes. In the rotating case the cosine crosses the level \(r/K\) twice if \(r<K\), with sign changes \(+,-,+\), and never crosses in the interior if \(r\ge K\). Hence there are no other interior extrema, including at equality thresholds.

4. **Ordinary locking edge.** For \(0<\Delta<K\) and \(\delta=\phi_s-\phi\), Taylor expansion gives \(v(\phi_s-\delta)=\gamma\delta+O(\delta^2)\). Consequently the difference between \(1/v(\phi_s-\delta)\) and \(1/(\gamma\delta)\) is bounded near zero, and there exists a finite real \(B\) for which
\[
A(\phi_s-\delta)=-\gamma^{-1}\log\delta+B+o(1).
\]
Substituting in the exact stationary density yields \(C=(r/\gamma)e^{-rB}>0\) and the sharp power exponent \(r/\gamma-1\). The sign and equality limits follow directly. This derivation excludes a hidden point mass at \(\phi_s\).

5. **Saddle-node locking edge.** At \(\Delta=K\), rationalizing the integrand gives the *exact* antiderivative
\[
A(\phi)=K^{-1}(\tan\phi+\sec\phi-1).
\]
As \(\delta=\pi/2-\phi\downarrow0\), \(\tan\phi+\sec\phi=\cot(\delta/2)=2/\delta+O(\delta)\), while \(v(\phi)=K\delta^2/2\,[1+O(\delta^2)]\). Substitution proves the explicit essential edge coefficient and exponential exponent. In particular, for every finite \(m\), \(\delta^{-m}p(\pi/2-\delta)\to0\). This is qualitatively different from every ordinary-locked algebraic edge.

## Verification
The symbolic transformations in the proof include the exact derivative of the logarithmic density and the critical antiderivative, each checkable by direct differentiation. A standalone numerical diagnostic program in `verify.py` reconstructs the density by quadrature and checks normalization, including the explicit omitted equilibrium-neighborhood tail mass, in eleven rotating/locked/critical parameter configurations. It also compares finite differences with the exact score function, checks ordinary-edge logarithmic slopes, the critical essential asymptotic, and the rotating period integral. Executing `python verify.py` with Python 3.9+ and SciPy produces `Passed 97 deterministic numerical checks`. These computations are finite diagnostics; all-parameter classification follows from the analytic sign and asymptotic arguments above.

## Relationship to prior work
Sarkar and Gupta, arXiv:2203.00339, establish Poisson resetting in the Kuramoto model and calculate stationary *macroscopic Lorentzian Ott–Antonsen order-parameter* distributions. They do not classify the detuned finite two-oscillator relative phase. Majumder, Chattopadhyay and Gupta, arXiv:2402.14921, instead reset only an oscillator subsystem in an infinite-frequency-distribution model. The 2023 general resetting-moment literature supports the reset-age methodology, which is not claimed as new. Grange, arXiv:2111.15241, develops winding renewal relations for Brownian motion on a circle with shortest-arc return; it does not give the present deterministic phase-density morphology.

The contribution assessed here is the *complete sharp model-specific stationary density shape and edge classification*, not the general renewal formula, the classical Adler drift itself, or the generic power law near a linearly stable equilibrium. Related results on the Lorentzian collective order-parameter spectrum and heavy-tail renewal-clock synchronization do not imply these finite detuned Adler thresholds. Equivalent results in unindexed or uninspected literature cannot be excluded and should be checked before a publication-priority claim.

## Limitations
The theorem assumes positive detuning, sine coupling, simultaneous full-phase Poisson resets to a common phase, and no continuous phase noise. It says nothing about local/subsystem resets, unequal reset phase values, heterogeneous non-Poisson reset intervals, non-sinusoidal coupling or the joint distribution of individual oscillator phases. A stationary phase-density mode is not by itself a dynamical phase-locking criterion; phase locking is determined here by \(\Delta\le K\). The generic reset-age representation is established prior methodology; only the sharp classification for this model is assessed as a new contribution. No independent audit has been performed.

## References
- M. Sarkar and S. Gupta, *Synchronization in the Kuramoto model in presence of stochastic resetting*, first public preprint 2022-03-01, https://arxiv.org/abs/2203.00339 .
- R. Majumder, R. Chattopadhyay and S. Gupta, *Kuramoto model subject to subsystem resetting*, first public preprint 2024-02-22, https://arxiv.org/abs/2402.14921 .
- P. Grange, *Winding number of a Brownian particle on a ring under stochastic resetting*, first public preprint 2021-11-30, https://arxiv.org/abs/2111.15241 .
- K. S. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E **108**, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120 .
