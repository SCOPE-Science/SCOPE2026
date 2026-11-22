# Airy transverse dichotomy and sharp linearized departure time near a drifting quadratic-flow axis

## Finding
Consider the real polynomial flow
\[
\dot x=a(y-x),\qquad \dot y=-cy-xz,\qquad \dot z=y^2-b+kxy
\]
with arbitrary \(a,b,c,k>0\). For every \(z_0\in\mathbb R\) the trajectory \(\Gamma_{z_0}(t)=(0,0,z_0-bt)\), \(t\ge0\), is an exact unbounded forward solution. Its transverse linearization has an exact one-dimensional rapidly decaying subspace. Every other nonzero transverse linearized perturbation grows at a universal stretched-exponential rate, despite the flow's constant negative divergence.

Put
\[
h=\frac{a+c}{2},\quad q=(ab)^{1/3},\quad
\tau=\frac{a(c+z_0)-h^2}{ab},\quad s(t)=q(t-\tau).
\]
Given a nonzero initial transverse vector \((u_0,v_0)\), let \((u(t),v(t))\) solve the variational system. Its Airy coefficients \(C_A,C_B\) are uniquely determined by
\[
\begin{split}
 u(t)&=e^{-ht}[C_A\operatorname{Ai}(s(t))+C_B\operatorname{Bi}(s(t))],\\
 v(t)&=u(t)+\dot u(t)/a,\\
 C_B&=\pi\left[\frac{a(v_0-u_0)+hu_0}{q}\operatorname{Ai}(s(0))-u_0\operatorname{Ai}'(s(0))\right].
\end{split}
\]
The condition \(C_B=0\) defines exactly one line in the transverse tangent plane. For any nonzero vector on that line,
\[
\lim_{t\to\infty}\frac{\log\sqrt{u(t)^2+v(t)^2}}{t^{3/2}}=-\frac23\sqrt{ab},
\qquad \lim_{t\to\infty}\frac{v(t)}{u(t)\sqrt t}=-\sqrt{b/a}.
\]
For all vectors off this line both signs are reversed to plus:
\[
\lim_{t\to\infty}\frac{\log\sqrt{u(t)^2+v(t)^2}}{t^{3/2}}=\frac23\sqrt{ab},
\qquad \lim_{t\to\infty}\frac{v(t)}{u(t)\sqrt t}=\sqrt{b/a}.
\]
In particular the linearized growth coefficient is independent of \(c,k,z_0\).

Fix any transverse unit vector off the decaying line and multiply it by \(\varepsilon>0\). Let \(T_\varepsilon\) be the first time its **linearized**, not nonlinear, transverse norm reaches one. Writing \(L=\log(1/\varepsilon)\) and
\[
 U_L=\left(\frac{3L}{2\sqrt{ab}}\right)^{2/3},
\]
one has the sharper three-term law
\[
\boxed{T_\varepsilon=U_L+\frac h{\sqrt{ab}}\sqrt{U_L}
+\tau+\frac{3h^2}{4ab}+o(1)\qquad(\varepsilon\downarrow0).}
\]
For every time for which the smooth flow is defined, its Jacobian determinant is \(e^{-(a+c)t}\), in particular along \(\Gamma_{z_0}\). Thus the transverse superexponential stretching and contraction coexist with exponential volume contraction.

## Assumptions and scope
All four flow parameters are strictly positive and real, \(z_0\) is arbitrary real, and all variational initial vectors are real. \(\operatorname{Ai}\) and \(\operatorname{Bi}\) are the standard real Airy solutions of \(w''(s)=sw(s)\) with Wronskian \(\operatorname{Ai}(s)\operatorname{Bi}'(s)-\operatorname{Ai}'(s)\operatorname{Bi}(s)=1/\pi\). The norm is Euclidean on the \((u,v)\) plane. The assertion about \(T_\varepsilon\) concerns the **variational equation on the unbounded axial orbit**, not the first exit time of a nonlinear perturbed orbit; it does not assert a compact attractor, physical instability threshold or a Lyapunov exponent for an invariant probability.

## Proof
**Axial solution and transverse reduction.** Both the first and second right-hand sides vanish at \(x=y=0\), and the third is then \(-b\). Linearizing at \(\Gamma_{z_0}\) yields
\[
\dot u=a(v-u),\qquad \dot v=-cv-(z_0-bt)u,\qquad \dot\zeta=0.
\]
Thus \(v=u+\dot u/a\) and
\[
\ddot u+(a+c)\dot u+a(c+z_0-bt)u=0.
\]
Substituting \(u=e^{-ht}w\), with \(h=(a+c)/2\), gives \(\ddot w=ab(t-\tau)w\), where \(\tau=(a(c+z_0)-h^2)/(ab)\). The change of variable \(s=q(t-\tau)\), \(q^3=ab\), yields exactly \(w_{ss}=sw\). This proves the displayed Airy form. At \(t=0\), \(w_0=u_0\) and \(\dot w_0=a(v_0-u_0)+hu_0\). Inverting the Airy fundamental matrix with Wronskian \(1/\pi\) gives the stated \(C_B\). Since the fundamental matrix is invertible, \(C_B=0\) defines a line, not the entire plane.

**Sharp dichotomy and slopes.** As \(s\to+\infty\), standard Airy asymptotics give
\[
\begin{split}
 \operatorname{Bi}(s)&=\pi^{-1/2}s^{-1/4}e^{2s^{3/2}/3}(1+O(s^{-3/2})),\\
 \operatorname{Bi}'(s)&=\pi^{-1/2}s^{1/4}e^{2s^{3/2}/3}(1+O(s^{-3/2})),\\
 \operatorname{Ai}(s)&=(2\sqrt\pi)^{-1}s^{-1/4}e^{-2s^{3/2}/3}(1+O(s^{-3/2})),\\
 \operatorname{Ai}'(s)&=-(2\sqrt\pi)^{-1}s^{1/4}e^{-2s^{3/2}/3}(1+O(s^{-3/2})).
\end{split}
\]
Because \(s(t)=q(t-\tau)\), the derivative contribution \((q/a)w_s\) dominates \((1-h/a)w\) in \(v\) by a factor proportional to \(\sqrt t\). Consequently the transverse norm has, if \(C_B\ne0\), the precise leading equivalent
\[
\frac{|C_B|q}{a\sqrt\pi}s(t)^{1/4}
\exp\left(\frac23s(t)^{3/2}-ht\right)(1+O(s(t)^{-1/2})).
\]
If \(C_B=0\), the corresponding equivalent is
\[
\frac{|C_A|q}{2a\sqrt\pi}s(t)^{1/4}
\exp\left(-\frac23s(t)^{3/2}-ht\right)(1+O(s(t)^{-1/2})).
\]
These formulas prove both logarithmic rates and both component-ratio limits. They also imply that every off-line norm is eventually strictly increasing and unbounded, while every on-line norm decays to zero.

**First-passage inversion.** For the fixed off-line unit vector, its unscaled norm \(G(t)\) satisfies
\[
\log G(t)=\frac23\sqrt{ab}(t-\tau)^{3/2}-ht+\frac14\log t+O(1).
\]
It has no zero for a nonzero variational initial vector, is bounded on compact time intervals and is eventually strictly increasing. Hence the first threshold time exists for sufficiently small \(\varepsilon\), tends to infinity and solves \(\log G(T_\varepsilon)=L\). Put \(W=\sqrt{U_L}\) and substitute \(T=W^2+pW+r\) into the preceding expansion. The coefficients of \(W^2\) and \(W\) vanish successively precisely when
\[
 p=h/\sqrt{ab},\qquad r=\tau+3h^2/(4ab).
\]
The remaining logarithmic error divided by \(\partial_T\log G(T)\sim\sqrt{abT}\) is \(O(\log W/W)=o(1)\). Monotonicity makes this inversion rigorous, proving the three-term law.

**Volume.** The vector-field divergence is \(-a-c\) everywhere. Liouville's formula gives the exact determinant \(\det D\phi_t=e^{-(a+c)t}\) along every existing trajectory, completing the proof.

## Verification
Run `python verify_airy.py` with `mpmath>=1.3`. The checker directly substitutes Airy solutions into both linearized first-order equations at independent parameter choices, tests the Wronskian, tests signs and slope scaling, and numerically checks that the three-term exit-time error decreases for \(L=1000,10000\). All reported checks passed. These finite tests support reproducibility but do not establish the asymptotic theorem: the preceding proof uses the Airy differential equation, Wronskian and classical asymptotics.

## Relationship to prior work
The 2022 Wang–Dong–Li article defines precisely the positive-parameter flow studied here, analyzes finite attractors and their periodic orbits, and records its negative divergence. The 2012 Wei–Pehlivan paper studies the earlier \(k=0\) generalized Sprott-C flow; its governing equations have the same axial linearization, so the result's leading mechanism is not produced by the extra \(kxy\) term. Neither inspected article presents the Airy transverse splitting or the three-term linearized departure law. An indexed compact-recurrence moment result for the 2022 model concerns invariant measures supported on bounded sets; it does not imply growth of the derivative along the noncompact escaping axis. Related sharp proximity laws for other planar models use different variational equations and exponents.

## Limitations
This is a theorem about a single explicit family of **noncompact** base trajectories and the flow derivative along them. The stable tangent line is not claimed to be a nonlinear stable manifold. The calculated \(T_\varepsilon\) does not establish a nonlinear first-exit law. Neither existence of a chaotic attractor nor any encryption performance follows. Equivalent results in unindexed sources cannot be excluded by the inspected literature and mathematical-index searches alone.

## References
1. J. Wang, C. Dong and H. Li, *A New Variable-Boostable 3D Chaotic System with Hidden and Coexisting Attractors: Dynamical Analysis, Periodic Orbit Coding, Circuit Simulation, and Synchronization*, Fractal and Fractional 6 (2022), 740, first published 2022-12-14. https://doi.org/10.3390/fractalfract6120740
2. Z. Wei and I. Pehlivan, *Chaos, coexisting attractors, and circuit design of the generalized Sprott C system with only two stable equilibria*, Optoelectronics and Advanced Materials – Rapid Communications 6 (2012), 742–745. https://oam-rc.inoe.ro/articles/chaos-coexisting-attractors-and-c-ircuit-d-esign-of-the-generalized-s-prott-c-system-with-only-two-stable-equilibria/fulltext
3. NIST Digital Library of Mathematical Functions, Chapter 9, *Airy and Related Functions*, §§9.2, 9.7 (standard Airy Wronskian and large-positive-argument expansions). https://dlmf.nist.gov/9
