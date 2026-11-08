# Cubic separatrix and exact beta-function period blow-up in a three-oscillator reactive ring

## Finding
For three identical nearest-neighbor phase oscillators at quadrature phase lag, the phase-difference dynamics has exactly two annuli of nonstationary periodic orbits, each terminating at a three-loop degenerate separatrix at synchrony. The physical-time least period \(T(h)\), indexed by the nonzero conserved Hamiltonian value \(h\), has the sharp **nonlogarithmic** asymptotic
\[
\lim_{h\to0^\pm}|h|^{1/3}T(h)
=2^{2/3}B\left(\frac13,\frac13\right)
=\frac{2^{2/3}\Gamma(1/3)^2}{\Gamma(2/3)}
\approx8.41309263195272.
\]
The two period branches agree exactly: \(T(-h)=T(h)\) for every \(0<h<3\sqrt3/2\). At either annulus center, \(T(h)\to4\pi/3\) as \(|h|\uparrow3\sqrt3/2\). The exponent and the three-vertex beta constant are in the original, unreparameterized flow time.

## Assumptions and scope
Consider phases \(\theta_1,\theta_2,\theta_3\in\mathbb R/(2\pi\mathbb Z)\), with cyclic indices, satisfying the autonomous, identical-frequency, unit-coupling equations
\[
\dot\theta_j=\sin(\theta_{j-1}-\theta_j+\pi/2)+\sin(\theta_{j+1}-\theta_j+\pi/2).
\]
Set \(x=\theta_2-\theta_1\) and \(y=\theta_3-\theta_2\) modulo \(2\pi\). The remaining consecutive difference is \(-x-y\). The quotient by common phase is the two-torus, with equations
\[
\dot x=\cos y-\cos(x+y),\qquad
\dot y=\cos(x+y)-\cos x.
\]
Let \(H(x,y)=\sin x+\sin y-\sin(x+y)\) and \(M=3\sqrt3/2\). For \(0<|h|<M\), the unique connected orbit on \(H=h\) has least period \(T(h)\) measured in the displayed time variable. The period is that of phase differences, not necessarily a return to the identical absolute phase triple: a common phase drift may occur.

## Proof
**1. Hamiltonian reduction and exact critical-point census.** Direct differentiation gives \(\dot x=H_y\), \(\dot y=-H_x\); hence \(H\) is conserved. The factorization
\[
H(x,y)=4\sin(x/2)\sin(y/2)\sin((x+y)/2)
\]
shows that, on the fundamental square \(0<x,y<2\pi\), the positive region is the triangle \(\Delta_+=\{x>0,y>0,x+y<2\pi\}\) and the negative region is \(\Delta_-=\{x<2\pi,y<2\pi,x+y>2\pi\}\). Their boundaries together give \(H=0\), consisting of three invariant torus circles meeting at \((0,0)\) modulo \(2\pi\). Each circle minus that point is a homoclinic trajectory to synchrony: for example, on \(x=0\), \(\dot y=\cos y-1<0\) for \(0<y<2\pi\). The linearization at synchrony is zero, and the leading local Hamiltonian is \(xy(x+y)/2\), so these are cubic, nonhyperbolic separatrices.

Inside \(\Delta_+\),
\[
\log H=\log4+\log\sin(x/2)+\log\sin(y/2)+\log\sin((x+y)/2).
\]
Its Hessian is negative definite, since the first two terms already provide strictly negative diagonal curvature and the last is concave. Consequently \(H\) is strictly log-concave, has a unique interior maximum, and each nonempty positive superlevel is strictly convex. The symmetry or the equations \(H_x=H_y=0\) locate the maximum at \((2\pi/3,2\pi/3)\) with \(H=M\). By \((x,y)\mapsto(2\pi-x,2\pi-y)\), the negative triangle has a unique minimum at \((4\pi/3,4\pi/3)\) with \(H=-M\). There are no further critical points on \(H=0\) except the common vertex: the gradient on each open edge does not vanish. Thus every noncritical nonzero energy is one simple, strictly convex closed curve in one triangle. Nonvanishing Hamiltonian velocity on it makes it exactly one periodic orbit; at \(h=0\), the three loops are nonperiodic homoclinic trajectories.

**2. Exact period reflection and the center limit.** The involution \(R(x,y)=(-x,-y)\) modulo \(2\pi\) sends \(H\) to \(-H\) and sends the Hamiltonian vector field to its negative under pushforward. It therefore reverses the orientation of an orbit without changing the elapsed time, proving \(T(-h)=T(h)\). At the positive center, the Hessian of \(H\) is
\[
-\sqrt3\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix},\qquad
\det D^2H=\frac94.
\]
The linearized Hamiltonian frequency is \(3/2\); standard smooth-center linearization gives the small-oval period limit \(2\pi/(3/2)=4\pi/3\), also at the negative center by the reflection.

**3. Rigorous local period scaling.** It suffices to approach \(h\downarrow0\) from the positive annulus. Fix small \(\delta>0\) and examine the part of \(H=h\) in the corner \(0<x,y<\delta\). Here
\[
H(x,y)=\frac12xy(x+y)J(x,y),\quad
J(x,y)=\frac{\sin(x/2)}{x/2}\frac{\sin(y/2)}{y/2}
\frac{\sin((x+y)/2)}{(x+y)/2}.
\]
The smooth factor satisfies \(J=1+O((x+y)^2)\) and its Euler derivative \(EJ=(x\partial_x+y\partial_y)J=O((x+y)^2)\). Thus \(EH=(xH_x+yH_y)=H(3+O(\delta^2))\), uniformly in the corner, and in particular \(EH>0\) for small \(\delta\). Put \(t=y/x\in(0,\infty)\) along the positive energy curve; Hamilton's equations give the exact identity
\[
\frac{dt}{d\tau}=-\frac{EH}{x^2},\qquad
\frac{d\tau}{|dt|}=\frac{x^2}{EH}\,dt.
\]
For any fixed \(t>0\) as \(h\to0^+\), the unique point in that corner satisfies
\[
\frac{x^2}{h^{2/3}}\longrightarrow
\left(\frac{2}{t(1+t)}\right)^{2/3},
\qquad \frac{EH}{h}\longrightarrow3.
\]
The corner indicator tends to one for each fixed \(t\). Moreover \(J\) and \(EH/h\) are bounded above and below by positive constants, so
\[
0\le h^{1/3}\frac{x^2}{EH}\mathbf1_{\{x,y<\delta\}}
\le C_\delta[t(1+t)]^{-2/3},
\]
whose right side is integrable over \((0,\infty)\) (the endpoint exponents are \(-2/3\) and \(-4/3\)). Dominated convergence therefore gives the *full*, not merely truncated, corner contribution:
\[
\lim_{h\downarrow0}h^{1/3}T_{\mathrm{corner}}(h)
=\frac{2^{2/3}}3\int_0^\infty\frac{dt}{[t(1+t)]^{2/3}}
=\frac{2^{2/3}}3B(1/3,1/3).
\]
There are three corners of the triangle, whose vertices are identified on the torus. The affine changes \((u,v)=(2\pi-x-y,y)\) and \((u,v)=(x,2\pi-x-y)\) carry the Hamiltonian near either other corner **exactly** to \(H(u,v)\); their Jacobian determinants have magnitude one. Consequently physical time in each corner has the same limiting contribution (orientation reversals do not change periods). On the remainder of the level, away from these corners, \(|\nabla H|\) is bounded below uniformly as \(h\downarrow0\). The regular curves are convex and contained in a fixed triangle, so their lengths are uniformly bounded. Therefore the remaining time \(\int ds/|\nabla H|\) is \(O_\delta(1)\), negligible after multiplication by \(h^{1/3}\). Adding the three contributions yields
\[
\lim_{h\downarrow0}h^{1/3}T(h)
=3\frac{2^{2/3}}3B(1/3,1/3)
=2^{2/3}B(1/3,1/3),
\]
and reflection establishes the negative-energy limit.

## Verification
The file `verify.py` is a standalone supplementary checker using NumPy and SciPy. It checks the trigonometric factorization at 16 independent sample pairs, the central energy and Hessian implications, computes period integrals by a radial graph and numerical quadrature on four nonzero energy levels, and compares their scaled values with the beta-function constant. Its actual execution returned `VERIFY_OK factor_identity=16 center_energy=1 period_levels=4 center_limit=1 beta_constant=1`. The scaled values for \(h=0.1,0.01,0.001,0.0001\) were respectively about \(8.04340402,8.33305768,8.39584544,8.40937679\), approaching \(8.41309263\). These are **finite checks**, not a substitute for the all-energy proof above. Run `python verify.py` from a directory containing this file.

## Relationship to prior work
Yan, Ozawa, Kori and Sato's 2026 investigation introduces the same ring model and identifies the Hamiltonian at quadrature lag, as well as long transients and basin changes away from that limit. Its six-page primary text and end matter do not give an exact three-site separatrix period, the nonlogarithmic exponent, or the beta coefficient. Ahnert and Pikovsky's earlier lattice paper gives the same conservative nearest-neighbor phase-difference model and studies its nonlinear traveling waves by quasicontinuum approximation and lattice computation; it does not establish the specific finite three-site period law. Pikovsky's 2026 work concerns broad conditions for phase-volume conservation and larger-network Lyapunov spectra. The present finding uses known Hamiltonian reduction, not a newly discovered integral: its distinct assertion is the global three-site phase portrait and the sharp **original-time period constant**.

## Limitations
The theorem applies to exactly three identical oscillators, unit nearest-neighbor coupling and exactly quadrature phase lag. The critical exponent concerns the phase-difference periods as \(h\to0\), not the winding stabilization time of dissipative systems or the long-chain continuum compacton period. Nothing is claimed about coupling detuning, \(N>3\), transport through perturbed separatrices, or absolute-phase periodicity. General earlier work on neutral phase coupling is relevant; historical priority remains provisional pending independent literature review.

## References
1. J. Yan, A. Ozawa, H. Kori, Y. Sato, *Basin Metamorphosis in Coupled Phase Oscillators*, arXiv:2603.02135 (first submitted 2026-03-02; revision 2026-07-09), https://arxiv.org/abs/2603.02135 and https://arxiv.org/pdf/2603.02135.
2. A. Pikovsky, *Conservative dynamics in phase oscillator networks*, arXiv:2603.25431 (2026-03-26), https://arxiv.org/pdf/2603.25431.
3. K. Ahnert, A. Pikovsky, *Traveling waves and Compactons in Phase Oscillator Lattices*, arXiv:0806.1833, https://arxiv.org/pdf/0806.1833.
4. A. P. Kuznetsov, L. V. Turukina, N. Yu. Chernyshov, Y. V. Sedova, *Oscillations and synchronization in a system of three reactively coupled oscillators*, arXiv:1503.05313, https://arxiv.org/pdf/1503.05313.
5. P. Rosenau, A. Pikovsky, *Phase Compactons in Chains of Dispersively Coupled Oscillators*, Phys. Rev. Lett. 94, 174102 (2005), https://doi.org/10.1103/PhysRevLett.94.174102 (abstract available; full text not reviewed).
