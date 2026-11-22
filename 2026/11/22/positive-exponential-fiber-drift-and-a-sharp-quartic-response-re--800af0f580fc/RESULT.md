# Positive exponential-fiber drift and a sharp quartic response reversal on forced Duffing cycles

## Finding
Fix \(\delta,\kappa,B,\omega,\alpha,\beta>0\), an arbitrary phase \(g\in\mathbb R\), and let \(T=2\pi/\omega\). Consider
\[
\dot x=y,\qquad
\dot y=-\delta y-\kappa x-Bx^3+\varepsilon\cos(\omega t+g),\qquad
\dot z=\alpha x e^{\beta x}.
\]
There is \(\varepsilon_0>0\) such that every \(0<|\varepsilon|<\varepsilon_0\) admits a unique \(T\)-periodic planar solution \((x_\varepsilon,y_\varepsilon)\) in a fixed neighborhood of the origin. It is locally exponentially attracting under the period-\(T\) return map, is nonzero, and obeys
\[
(x_\varepsilon,y_\varepsilon)(t+T/2)=-(x_\varepsilon,y_\varepsilon)(t).
\]
For **every** initial fiber height \(z_0\), its lift has the exact form
\[
z(t)=v_\varepsilon t+p_\varepsilon(t),\qquad
p_\varepsilon(t+T)=p_\varepsilon(t),\qquad v_\varepsilon>0,
\]
where the bounded periodic term depends on \(z_0\). Thus the planar attracting cycle does not lift to a bounded cycle, nor does its entire lifted orbit support a compact invariant probability measure.

Write
\[
D=(\kappa-\omega^2)^2+\delta^2\omega^2>0.
\]
The drift speed is an even real-analytic function of the forcing amplitude near zero, with the exact expansion
\[
\boxed{
v_\varepsilon=
\frac{\alpha\beta}{2D}\varepsilon^2+
\frac{\alpha\beta}{D^3}
\left[\frac{\beta^2D}{16}-\frac{3B(\kappa-\omega^2)}4\right]\varepsilon^4
+O(\varepsilon^6).
}
\]
The **quartic coefficient** is strictly positive whenever \(\kappa\le\omega^2\). When \(\kappa>\omega^2\) it changes sign exactly once, from negative to positive, at the natural threshold
\[
\boxed{
\beta_* = \sqrt{\frac{12B(\kappa-\omega^2)}D}.
}
\]
In particular, the positive drift's first nonlinear correction can be either reinforcing or suppressing, even though the sign of the total drift never changes for nonzero sufficiently small forcing.

## Assumptions and scope
The above is a damped, stable, single-well parameter slice of the periodically forced Duffing/exponential-fiber system of Liu et al., with their parameter identification \(a=-\delta\), \(\zeta=-\kappa\), \(b=B\), \(c=\varepsilon\), \(d=\omega\). All six fixed coefficients are strictly positive; \(g\) is unrestricted. The smallness bound \(\varepsilon_0\) may depend on the fixed coefficients, and only the locally selected planar cycle is classified. There is no claim that all planar initial conditions approach this cycle, nor any assertion about the large-forcing attractors studied numerically in the originating paper.

A time-periodic nonautonomous system is understood as a flow on \(\mathbb R^3\times\mathbb S^1\) when invariant measures are mentioned, with the added phase \(\theta=\omega t+g\pmod{2\pi}\). The unboundedness assertion is for the actual fiber coordinate \(z\), without reducing it modulo a lattice.

## Proof
**Periodic planar branch.** At \(\varepsilon=0\), \((x,y)=(0,0)\) is a hyperbolic sink of the planar equation. Its constant Jacobian is
\[
J_0=\begin{pmatrix}0&1\\-\kappa&-\delta\end{pmatrix},
\]
whose eigenvalues have negative real parts since \(\delta,\kappa>0\). Its period map therefore has no eigenvalue one. The time-\(T\) map depends real-analytically on nearby planar initial data and \(\varepsilon\); the analytic implicit-function theorem applied to \(P_\varepsilon(w)-w=0\) supplies a unique nearby periodic solution, real analytic in \(\varepsilon\). The eigenvalues of its period-map derivative remain strictly inside the unit disk for sufficiently small \(\varepsilon\), yielding local exponential attraction. It is nonzero if \(\varepsilon\ne0\), since a zero planar solution would contradict the nonzero harmonic forcing.

**Half-period symmetry.** The planar equation is invariant under
\[
(x(t),y(t))\longmapsto(-x(t+T/2),-y(t+T/2)).
\]
The transformed orbit remains in the same local uniqueness neighborhood. Hence it coincides with the original orbit. Similarly \((x_{-\varepsilon},y_{-\varepsilon})=-(x_\varepsilon,y_\varepsilon)\), so its Taylor series contains only odd powers of \(\varepsilon\).

**Strict fiber drift.** For a periodic function write \(\langle h\rangle=T^{-1}\int_0^T h(t)\,dt\). Half-period symmetry yields
\[
\langle x_\varepsilon e^{\beta x_\varepsilon}\rangle
=\langle x_\varepsilon\sinh(\beta x_\varepsilon)\rangle.
\]
Since \(\beta>0\), the integrand is nonnegative at every time and strictly positive on a set of positive measure whenever the planar cycle is nontrivial. Thus
\[
v_\varepsilon=\alpha\langle x_\varepsilon\sinh(\beta x_\varepsilon)\rangle>0.
\]
Integrating the periodic right-hand side of \(\dot z\) produces \(z(t)=v_\varepsilon t+p_\varepsilon(t)\), where \(p_\varepsilon\) is periodic. Each period translates the fiber coordinate by \(Tv_\varepsilon>0\). Every such lift is therefore unbounded; a compactly supported invariant probability over this one periodic planar base would contradict invariance under this nonzero translation.

**Two nonzero coefficients.** Define
\[
L=\frac{d^2}{dt^2}+\delta\frac d{dt}+\kappa,
\qquad H=\frac1{\kappa-\omega^2+i\delta\omega}.
\]
Analyticity and oddness yield
\[
x_\varepsilon=\varepsilon u+\varepsilon^3 w+O(\varepsilon^5)
\quad\text{in }C^2(\mathbb R/T\mathbb Z),
\]
where
\[
u(t)=\operatorname{Re}(He^{i(\omega t+g)}),
\qquad Lw=-Bu^3.
\]
The first-harmonic part of \(u^3\) has complex amplitude \(3|H|^2H/4\), whereas the third harmonic is orthogonal to \(u\). Consequently
\[
\langle u^2\rangle=\frac1{2D},\qquad
\langle u^4\rangle=\frac3{8D^2},\qquad
\langle uw\rangle=-\frac{3B(\kappa-\omega^2)}{8D^3}.
\]
The Taylor expansion of \(x\sinh(\beta x)\), together with the odd-power expansion of \(x_\varepsilon\), gives
\[
\begin{aligned}
\frac{v_\varepsilon}{\alpha}
&=\beta\langle x_\varepsilon^2\rangle
+\frac{\beta^3}{6}\langle x_\varepsilon^4\rangle+O(\varepsilon^6)\\
&=\beta\varepsilon^2\langle u^2\rangle
+\varepsilon^4\left(2\beta\langle uw\rangle
+\frac{\beta^3}{6}\langle u^4\rangle\right)+O(\varepsilon^6).
\end{aligned}
\]
Substitution proves the displayed two-coefficient formula. The coefficient of \(\varepsilon^4\) has the sign of
\[
\beta^2D-12B(\kappa-\omega^2),
\]
which gives the asserted sharp sign diagram.

## Verification
The standalone Python program `verify_rectification.py` uses exact rational Fourier coefficient arithmetic for four rational parameter cases. It constructs the cubic response by actual Laurent-polynomial convolution and checks both closed coefficients as exact fractions, including examples on each side of the quartic threshold. It also integrates locally attracting periodic responses via fourth-order Runge–Kutta quadrature at two small forcing amplitudes for both signs of the quartic coefficient. The latter experiments are convergence diagnostics, **not** an exhaustive proof or a substitute for analytic existence and the \(O(\varepsilon^6)\) remainder.

Run `python3 verify_rectification.py` from the directory containing this file. The final output line should read `VERIFY_OK`.

## Relationship to prior work
Liu et al. (2023) introduce exactly the exponential-fiber readout \(\dot z=\alpha xe^{\beta x}\) over a forced Duffing base, and study numerical dynamical indicators and projected trajectories; their accessible full article does not state an analytic drift expansion or a parameter threshold for the first nonlinear drift correction. The Duffing oscillator and its half-period sign symmetry long predate this finding. Marti and Leonel (2026), including their discussion of Swift–Wiesenfeld's earlier symmetry theory, give a detailed classification of antiperiodic Duffing responses, but not this exponential-fiber drift law or its quartic sign transition.

Related stationary forced-Duffing results bound and relate planar velocity moments; they do not include the \(z\)-fiber or the specific quartic rectification coefficient. A different exact analysis of the **unforced, undamped** integrable boundary of the same exponential-fiber model proves axial drift over above-barrier Hamiltonian oscillations. Its hypotheses exclude the present dissipative, externally forced, locally attracting periodic branch, and it supplies no forcing-amplitude expansion or quartic cancellation locus. Neither the general fact that an antiperiodic orbit exists nor the leading strictly positive sign of an exponential observable is presented as a new generic principle; the new quantitative statement is the stable forced-cycle lift and exact two-term response boundary for this model.

## Limitations
The local forcing threshold is existential, not an explicit uniform bound. No large-forcing regime, non-antiperiodic planar cycle, stochastic perturbation, or all-initial-data global basin is classified. The sharp quartic boundary concerns only the coefficient in the weak-forcing series; it does **not** signal reversal of the positive total drift. The result uses exact real dynamics and does not assert any physical-device numerical behavior. Equivalence to unknown older perturbative literature remains a publication-priority risk. An independent mathematical audit has not been performed.

## References
1. S. Liu, Q. Wang, C. Liu, Y. Sun, L. He, “Natural Exponential and Three-Dimensional Chaotic System,” *Advanced Science* **10**, 2204269 (first published 28 March 2023), DOI: https://doi.org/10.1002/advs.202204269.
2. A. C. Marti and E. D. Leonel, “Antiperiodic orbits and spontaneous symmetry breaking in the Duffing--Holmes oscillator,” arXiv:2607.05604 (first posted 6 July 2026), https://arxiv.org/abs/2607.05604.
3. Y. Ueda, “Duffing oscillator,” *Scholarpedia*, DOI: https://doi.org/10.4249/scholarpedia.6327 (background on the forced Duffing model).
