# Periodic-cylinder collapse and asymmetric separatrix scattering in an exponential Duffing extension

## Finding

For the autonomous integrable boundary of the three-coordinate exponential Duffing system of Liu et al., exponential weight controls whether periodic planar oscillations lift to periodic three-coordinate orbits. The transition is sharp at \(\beta=0\): all above-barrier planar oscillations lift to periodic cylinders exactly there, while no nonconstant periodic full-system trajectory survives for \(\beta\ne0\). There is a complete classification of bounded two-sided motions, invariant probabilities, and the vertical displacement of both separatrices.

For \(\beta\ne0\), all Borel invariant probability measures of the full real flow are supported on the equilibrium line, and its only bounded complete nonstationary trajectories are two families of heteroclinic connections between different points on that line. On the separatrices, the two exact axial displacements have unequal large-positive-\(\beta\) scales: one exponential and one algebraic.

## Assumptions and scope

Consider the originally published family
\[
\dot x=y,\qquad \dot y=a y+\zeta x-bx^3+c\cos(dt+g),\qquad \dot z=\alpha x e^{\beta x}.
\]
We study only its **autonomous Hamiltonian boundary** \(a=c=0\), with \(\zeta>0\), \(b>0\), \(\alpha\ne0\) and arbitrary real \(\beta\). No assertion is made for nonzero damping or forcing, and this boundary is not claimed chaotic. The first two coordinates have the conserved energy
\[
E=\frac{y^2}{2}-\frac{\zeta x^2}{2}+\frac{b x^4}{4},\qquad E_{\min}=-\frac{\zeta^2}{4b}.
\]
For \(E_{\min}<E<0\), each of the two potential wells contains one periodic planar orbit; for \(E>0\), one periodic planar oval crosses both wells; the level \(E=0\) consists of the planar origin and two homoclinic separatrices. At \(E=E_{\min}\) the two planar well equilibria are stationary. A *bounded complete trajectory* means its image for all \(t\in\mathbb R\) is bounded in all three coordinates. Every solution on this parameter boundary is complete because the planar Hamiltonian is coercive.

Write
\[
A=\sqrt{\frac{2\zeta}{b}},\qquad k=\sqrt\zeta,\qquad
J(s)=2\int_0^1\frac{e^{sv}}{\sqrt{1-v^2}}\,dv.
\]
Then each planar separatrix has the explicit representation \(x_\pm(t)=\pm A\operatorname{sech}(kt)\), \(y_\pm=\dot x_\pm\), up to time translation. Its full-system limits are distinct equilibria \((0,0,z_-)\) and \((0,0,z_+)\) with
\[
\Delta_+(\beta)=z_+-z_- = \frac{\alpha A}{k}J(\beta A),\qquad
\Delta_-(\beta)=-\frac{\alpha A}{k}J(-\beta A).
\]
Both are nonzero for every real \(\beta\). At the critical weight they are \(\Delta_\pm(0)=\pm\alpha\pi\sqrt{2/b}\). For \(\beta\to+\infty\),
\[
\Delta_+(\beta)\sim\frac{\alpha A}{k}e^{\beta A}\sqrt{\frac{2\pi}{\beta A}},\qquad
\Delta_-(\beta)\sim-\frac{2\alpha}{k\beta}.
\]
For negative \(\beta\), the positive/negative branches exchange the exponentially large and algebraically small magnitudes.

## Proof

**Planar foliation.** The potential \(V(x)=-\zeta x^2/2+bx^4/4\) tends to \(+\infty\) at both ends, has one saddle maximum at the origin and two equal minima at \(\pm\sqrt{\zeta/b}\). Its energy levels are therefore exactly the three planar types above. Differentiating the displayed \(x_\pm\) shows \(\ddot x_\pm=\zeta x_\pm-bx_\pm^3\) and \(E=0\), giving the two complete separatrices. In each planar well equilibrium, \(x\ne0\) and hence \(\dot z=\alpha x e^{\beta x}\ne0\); the full-system equilibrium set is precisely \((0,0,z)\).

**Periodic lift obstruction.** In each well, \(x\) has a fixed strict sign on any planar periodic orbit, so \(\int_0^T x(t)e^{\beta x(t)}dt\ne0\) for every real \(\beta\). On each above-barrier oval the symmetry and uniqueness of planar trajectories imply \(x(t+T/2)=-x(t)\), hence
\[
\int_0^T x(t)e^{\beta x(t)}dt
=2\int_0^{T/2}x(t)\sinh(\beta x(t))dt.
\]
The integrand on the right has the strict sign of \(\beta\) except at isolated zeros. Thus the full-system return displacement is nonzero exactly when \(\beta\ne0\), with sign \(\alpha\beta\). At \(\beta=0\) all above-barrier ovals lift to periodic orbits for every initial height. Otherwise each lifted planar periodic orbit has unbounded linear-in-period axial drift in forward and backward time.

**Separatrix displacement.** Along the explicit separatrices, \(x e^{\beta x}\) is exponentially integrable at both temporal ends. The substitution \(v=\operatorname{sech}(kt)\) on positive and negative half-times gives the displayed \(J\)-integral and the formulas for \(\Delta_\pm\). Since \(J(s)>0\) and \(J(0)=\pi\), the displacements are always nonzero and have the stated values at \(\beta=0\). Thus these are heteroclinic connections between *distinct* points of the equilibrium line, never full-system homoclinic loops. As \(s\to+\infty\), Laplace's method at \(v=1\) yields \(J(s)\sim e^s\sqrt{2\pi/s}\); at \(v=0\), \(J(-s)\sim2/s\), proving the stated unequal scales. In particular, for \(\beta>0\) one has \(\Delta_+(\beta)+\Delta_-(\beta)\ne0\) with sign \(\alpha\beta\).

**Completeness of bounded motions and invariant measures.** Every planar initial condition lies on a stationary, periodic, or separatrix energy component, and all these planar motions are bounded for all time. The preceding return-displacement classification therefore gives *all* bounded complete full-system orbits. For \(\beta\ne0\), the only recurrent full-system points are the stationary line: drifting periodic lifts cannot recur in height, and heteroclinic points have unequal forward/backward equilibrium limits. The Poincaré recurrence theorem forces any invariant Borel probability measure to be supported on this line. For \(\beta=0\), in addition the above-barrier lifted periodic circles support uniform-in-time invariant measures. Every invariant probability is a mixture (in the ergodic-decomposition sense) of the point masses on the equilibrium line and, when \(\beta=0\), those periodic-orbit uniform measures.

**Approach to the separatrix.** Above-barrier planar return displacement is the integral of \(\alpha x e^{\beta x}\) against the Hamiltonian travel-time density \([2(E-V(x))]^{-1/2}\). Splitting at the origin and using local bounds \(|x|/\sqrt{E+\zeta x^2/4}\le C\) for small \(|x|\), while shifting each simple turning point as \(E\downarrow0\), proves convergence to the sum of the two homoclinic integrals: \(\Delta_E(\beta)\to\Delta_+(\beta)+\Delta_-(\beta)\). The corresponding one-well displacements converge to the appropriate individual \(\Delta_\pm\) as \(E\uparrow0\).

## Verification

The standalone `checker.py` uses only the Python standard library. Run `python checker.py` to numerically cross-check the explicit separatrix against the differential equations, the two equivalent displacement integrals, the critical value, and finite large-weight convergence toward both asymptotic scales. These checks are supportive, not a substitute for the analytical all-parameter proof. Energy-level and recurrence claims are proved above, not inferred from finite experiments.

## Relationship to prior work

Liu et al. (2023, DOI: 10.1002/advs.202204269, first published 28 March 2023) introduced the exponential coordinate and investigated numerical projected attractors, Poincaré sections, Lyapunov data and entropy; the inspected full-text sections do not give this zero-damping/zero-forcing global recurrence census, the exact pair of heteroclinic displacements or their unequal large-weight asymptotics. The conservative Duffing energy geometry and the general zero-average criterion for lifted skew-flow cycles are classical and are used, not claimed new. The specialized complete classification and explicit scattering law are the assessed contributions.

Related published published-finding corpus findings study periodic cylinders in **different** polynomial skew flows and Hamiltonian foliation in **different** models, not a stronger theorem whose hypotheses contain this exponential Duffing system. Their related use of drift integrals is a methodological antecedent, not evidence of uniqueness. Publication-priority searches are incomplete and unindexed equivalent work is a residual risk.

## Limitations

Only \(a=c=0\), \(\zeta,b>0\), \(\alpha\ne0\) are covered; conclusions must not be extrapolated to the article's forced/damped numerical parameter settings. The two-dimensional base at this boundary is integrable, not chaotic. The word 'heteroclinic' refers to the full three-coordinate flow joining different points on its equilibrium line. No quantitative rate for the energy-to-separatrix limit is claimed, and no independent mathematical audit has been performed. The empirical checker does not establish infinite-time claims by itself.

## References

1. S. Liu, Q. Wang, C. Liu, Y. Sun and L. He, *Natural Exponential and Three-Dimensional Chaotic System*, Advanced Science 10 (2023), e2204269, https://doi.org/10.1002/advs.202204269 (first publicly available 2023-03-28).
2. J. Guckenheimer and P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer, 1983 (classical Duffing separatrix background; not relied upon for novel identities).
