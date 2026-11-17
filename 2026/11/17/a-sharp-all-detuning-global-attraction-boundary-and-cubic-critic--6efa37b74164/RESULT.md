# A sharp all-detuning global-attraction boundary and cubic critical slowing in Miles’ whirling-string flow

## Finding

For the four-dimensional averaged whirling-string flow defined below, write \(C_*=16\sqrt{3}/27\). If \(\alpha^2\le C_*\gamma^3\), the flow has exactly one equilibrium for **every** real detuning, and every forward orbit converges to it. The inequality is sharp as a uniform-in-detuning uniqueness assertion: for each \(\alpha^2>C_*\gamma^3\) there is a detuning with three distinct equilibria. At the unique nonhyperbolic boundary point the center direction has a cubic restoring drift and the exact inverse-square relaxation coefficient \(\lim_{\tau\to\infty}\tau u(\tau)^2=\sqrt3/4\). Moreover, throughout the larger strict strip \(\alpha^2<2\gamma^3\), every bounded complete solution is planar and every forward trajectory loses its transverse component exponentially.

## Assumptions and scope

Let \(\gamma>0\), \(\alpha>0\), \(\Delta\in\mathbb R\) and \(V,W\in\mathbb C\). Time \(\tau\) is the *slow time* used in the averaged equations. Define \(E=|V|^2+|W|^2\), \(J=\operatorname{Im}(\overline W V)\), and \(\Omega=\Delta-3E/2\). The autonomous equations are
\[
\begin{aligned}
V'&=-\gamma V-i\Omega V+JW-i\alpha,\\
W'&=-\gamma W-i\Omega W-JV.
\end{aligned}
\]
Here \(C_*=16\sqrt3/27\) and a 'bounded complete solution' is a solution on \(\mathbb R\) with bounded state. This theorem concerns this averaged ordinary differential equation, not the underlying partial differential equation or the two-mode string without averaging.

Precisely: (i) when \(\alpha^2<2\gamma^3\), every forward solution has \(|W(\tau)|\le M e^{-\eta\tau}\) for some trajectory-dependent \(M,\eta>0\) and all sufficiently large \(\tau\); every bounded complete solution has \(W\equiv0\). (ii) when \(0<\alpha^2\le C_*\gamma^3\), exactly one equilibrium exists and is globally asymptotically attracting. For a strict inequality its Jacobian is Hurwitz, as it is at equality for all \(\Delta\ne\sqrt3\gamma\). (iii) when \(\alpha^2=C_*\gamma^3\) and \(\Delta=\sqrt3\gamma\), the unique equilibrium is
\[
V_*=-\sqrt\gamma\bigl(3^{-3/4}+i3^{-1/4}\bigr),\qquad W_*=0.
\]
For \(u=\operatorname{Im}V-\operatorname{Im}V_*\), every nonstationary solution of the local one-dimensional center-manifold reduced equation obeys \(\lim_{\tau\to\infty}\tau u(\tau)^2=\sqrt3/4\). (iv) for every \(\alpha^2>C_*\gamma^3\), some \(\Delta>\sqrt3\gamma\) yields exactly three positive-energy roots and therefore at least three distinct equilibria.

## Proof

**Boundedness and planarization.** Direct differentiation gives
\[
E'=-2\gamma E-2\alpha\operatorname{Im}V\le-2\gamma E+2\alpha\sqrt E.
\]
Interpreting the resulting scalar differential inequality at \(E=0\) by continuity yields
\[
\sqrt{E(\tau)}\le e^{-\gamma(\tau-\tau_0)}\sqrt{E(\tau_0)}+\frac\alpha\gamma(1-e^{-\gamma(\tau-\tau_0)})
\]
for all \(\tau\ge\tau_0\). In particular solutions are forward complete and bounded. Put \(K=\operatorname{Re}(\overline W V)\). Then
\[
(|W|^2)'=-2\gamma|W|^2-2JK,
\quad J^2+K^2=|V|^2|W|^2,
\]
so \((|W|^2)'\le(-2\gamma+|V|^2)|W|^2\). If \(\alpha^2<2\gamma^3\), the energy estimate eventually makes the coefficient strictly negative. This gives the claimed exponential transverse decay. For a bounded complete solution apply the energy estimate from \(\tau_0\to-\infty\) to obtain \(E(\tau)\le\alpha^2/\gamma^2<2\gamma\) at every time. Integrating the strict transverse decay inequality backwards and using backward boundedness forces \(W\equiv0\). The same conclusion applies to all full trajectories within a compact two-sided invariant set and hence to every invariant probability supported on such a set.

**The planar response cusp.** On \(W=0\) put \(Q=|V|^2\). The equilibrium equation has the exact scalar form
\[
F_{\Delta,\gamma}(Q):=Q\bigl[\gamma^2+(\Delta-3Q/2)^2\bigr]=\alpha^2,\qquad Q>0.
\]
Each root determines one complex equilibrium \(V=-i\alpha/[\gamma+i(\Delta-3Q/2)]\). The derivative \(F'_Q=\gamma^2+\Delta^2-6\Delta Q+27Q^2/4\). When \(\Delta\le\sqrt3\gamma\), this derivative is nonnegative on \(Q\ge0\) and vanishes only at an isolated point (when equality holds), implying strict increase. When \(\Delta>\sqrt3\gamma\), both positive critical energies are
\[
Q_\pm=\frac{2\Delta\pm\sqrt{\Delta^2-3\gamma^2}}{9/2}.
\]
At either stationary point the partial derivative of the critical value with respect to \(\Delta\) is \(2Q_\pm(\Delta-3Q_\pm/2)>0\), since \(\Delta-3Q_\pm/2=(\Delta\mp\sqrt{\Delta^2-3\gamma^2})/3>0\). Both fold heights therefore increase strictly from the common value
\[
F_{\sqrt3\gamma,\gamma}(4\sqrt3\gamma/9)=C_*\gamma^3.
\]
Thus below or at that forcing level there is exactly one planar root for every detuning. Conversely, for every larger forcing level the higher fold height first crosses it while the lower fold height remains strictly below; at such a detuning the cubic has three positive roots. (Equivalently, continuity and the strict ordering of the two fold heights give an open interval of three-root detunings.)

**Stability and global attraction.** At any planar equilibrium the two in-plane eigenvalues have sum \(-2\gamma\) and product \(F'_Q\); the two transverse eigenvalues are
\[
-\gamma\pm\sqrt{-(\Delta-3Q/2)(\Delta-Q/2)}.
\]
The real part of either is bounded by \(-\gamma+Q/2\), because the positive part of the discriminant is at most \(Q^2/4\). For the unique equilibrium under \(\alpha^2\le C_*\gamma^3\), the energy equation implies \(Q\le\alpha^2/\gamma^2\le C_*\gamma<2\gamma\). Hence the transverse block is strictly stable. The planar block is Hurwitz except when \(\alpha^2=C_*\gamma^3\), \(\Delta=\sqrt3\gamma\), where one planar eigenvalue vanishes and the other is \(-2\gamma\).

The planar vector field has divergence identically \(-2\gamma<0\), and all its forward trajectories are bounded. It has exactly one equilibrium, which is a sink except at the cusp. At the cusp the center reduction below has an attracting cubic drift; thus the equilibrium is locally asymptotically stable there too. Bendixson's criterion rules out periodic orbits, and a sink has no outgoing orbit to make a homoclinic or polycyclic limiting set. The Poincaré–Bendixson theorem therefore gives convergence of every planar forward trajectory to that equilibrium. Since \(C_*<2\), transverse decay holds uniformly eventually along each full-system forward trajectory. Its planar equation differs from the actual planar equation only by \(O(|W|^2)\) on bounded sets. Finite-horizon Gronwall comparison, together with uniform attraction by the planar flow on compact bounded subsets, then implies convergence of the full solution to the same equilibrium. At the strict parameter cases hyperbolicity additionally gives an eventual trajectory-dependent exponential convergence rate.

**Cubic slowdown at the cusp.** Rescale \(V=\sqrt\gamma\,v\) and time by \(s=\gamma\tau\). At the cusp the rescaled parameters are \(\gamma=1\), \(\Delta=\sqrt3\), \(\alpha=4/3^{5/4}\). Put \(v=x+iy\), \(x_*=-3^{-3/4}\), \(y_*=-3^{-1/4}\), \(u=y-y_*\) and \(z=x-x_*+u/\sqrt3\). Direct Taylor expansion gives a stable \(z\)-direction with eigenvalue \(-2\) and center manifold
\[
z=\frac{2\,3^{3/4}}3u^2+O(u^3).
\]
Substitution into the center equation yields
\[
\frac{du}{ds}=-\frac2{\sqrt3}u^3+O(u^4).
\]
The normalization \(u_{\rm physical}=\sqrt\gamma\,u\), \(s=\gamma\tau\) preserves the displayed cubic coefficient. Separation/integration of \((u^{-2})'=4/\sqrt3+O(u)\) gives \(\tau u_{\rm physical}(\tau)^2\to\sqrt3/4\), for each nonzero local center orbit. The center manifold of the planar invariant subspace is also a center manifold of the full system since all three complementary directions are strictly stable.

## Verification

Run the standalone file `check_whirling.py` with Python 3, NumPy, SciPy and SymPy. It checks the energy and transverse identities symbolically, the exact cubic-fold conditions, an exact three-root counterexample above threshold, the cubic center-reduction coefficient and finite-time numerical illustrations for both signs of the center coordinate. Expected final line: `VERIFY_OK`. The infinite-parameter and infinite-time assertions follow from the proof, not from this finite checker.

## Relationship to prior work

Tufillaro's 2026 comparison derives these four-dimensional averaged equations, supplies the planar Duffing-response cubic and linear planar/transverse eigenvalues, and studies a numerical route to whirling chaos. These ingredients are prior results, as is the general Duffing hysteresis cusp. What is asserted here is the *global* all-detuning boundary for the full averaged dynamics, the transverse recurrence-exclusion strip, and the explicit critical-time coefficient. Historical priority remains provisional: early whirling-string literature including Miles' original averaged-equation paper and O'Reilly's global-bifurcation analysis was not fully accessible for exhaustive comparison.

## Limitations

The threshold \(C_*\) is sharp for **uniform detuning-independent uniqueness of the global equilibrium**, not asserted sharp for the stronger recurrence-exclusion condition \(\alpha^2<2\gamma^3\). At forcing above \(C_*\), the theorem proves only existence of a detuning with multiple *equilibria*, not existence of multiple attractors or whirling motions. The cubic rate applies to center-manifold trajectories at the single cusp detuning; exceptional strong-stable trajectories can decay exponentially. Physical string equations and higher-mode effects are outside scope. This work has received self-review only, not independent scientific validation.

## References

1. N. B. Tufillaro, *A comparison of three models of a whirling string as it becomes chaotic*, arXiv:2611.06567v1, publicly posted November 4, 2026, https://arxiv.org/html/2611.06567v1.
2. J. W. Miles, *Resonant non-planar motion of a stretched string*, 1984 (cited as a source of the averaged model by Tufillaro); full text not inspected.
3. O. M. O'Reilly, *Global bifurcations in the forced vibration of a damped string*, *International Journal of Non-linear Mechanics* 28 (1993), 337–351, https://doi.org/10.1016/0020-7462(93)90040-R; abstract-level comparison only.
