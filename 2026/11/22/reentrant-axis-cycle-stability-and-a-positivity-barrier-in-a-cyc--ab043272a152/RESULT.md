# Reentrant axis-cycle stability and a positivity barrier in a cyclic three-species map

## Finding
For the real quadratic cyclic Lotka–Volterra update
\[
F_{R,\alpha,\beta}(x,y,z)=\left(
 x+Rx(1-x-\alpha y-\beta z),\quad
 y+Ry(1-\beta x-y-\alpha z),\quad
 z+Rz(1-\alpha x-\beta y-z)
\right),
\]
with \(R>0\), \(\alpha,\beta\in\mathbb R\), there are exactly three positive **axis-supported primitive two-cycles** when \(R>2\): one on each positive coordinate axis, cyclic permutations of \(\{(u_+,0,0),(u_-,0,0)\}\), where
\[
u_\pm=\frac{R+2\pm\sqrt{R^2-4}}{2R}.
\]
There are no positive primitive two-cycles supported on a coordinate axis for \(0<R\le2\). The three cycles have the same full-space two-step Floquet spectrum,
\[
\boxed{\left\{5-R^2,\ p_R(\alpha),\ p_R(\beta)\right\}},\qquad
p_R(c)=1+(R+2)(c-1)(c-R).
\]
Consequently, all three are simultaneously hyperbolically attracting (and otherwise none is) if and only if \(2<R<\sqrt6\) and both \(\alpha,\beta\) belong to the **exact stability set** \(I_R=\{c:|p_R(c)|<1\}\). This set is
\[
I_R=\begin{cases}
 (1,R),&2<R<R_*,\\
 (1,c_*)\cup(c_*,R),&R=R_*,\\
 (1,c_-(R))\cup(c_+(R),R),&R_*<R<\sqrt6,
\end{cases}
\]
where \(R_*\) is the unique root \(>2\) of \(R^3-3R-6=0\), \(c_*=(R_*+1)/2\), and
\[
 c_\pm(R)=\frac{R+1}{2}\pm\frac12\sqrt{\frac{R^3-3R-6}{R+2}}.
\]
For \(R>R_*\), the open unstable interval \((c_-,c_+)\) is created with square-root width
\[
 c_+(R)-c_-(R)\sim
\sqrt{\frac{3R_*^2-3}{R_*+2}}\,\sqrt{R-R_*}
\quad(R\downarrow R_*).
\]
This gives an exact stable–unstable–stable *reentrance* for transverse competition, and four disconnected components in the two-interaction stability locus once \(R\ge R_*\).

The full-space criterion must not be confused with biological accessibility. Define
\[
 q(R)=\frac{2(R+1)}{R+2+\sqrt{R^2-4}}.
\]
For \(2<R<\sqrt6\), \(1<q(R)<(R+1)/2\) and \(p_R(q(R))=0\). If \(1<\alpha,\beta<q(R)\), each of the three axis-cycles attracts an open set of **strictly positive** initial population vectors whose entire forward orbits remain strictly positive. Conversely, if either \(\alpha>q(R)\) or \(\beta>q(R)\), no strictly positive forward orbit that stays positive at every step can converge to any of the three axis-cycles. In particular, the upper reentrant hyperbolic-sink band is dynamically attracting in \(\mathbb R^3\) but inaccessible to perpetually positive populations.

## Assumptions and scope
The dynamics is the polynomial update on \(\mathbb R^3\), not a globally positivity-preserving update on all of \(\mathbb R_{\ge0}^3\). Here *positive axis cycle* means its two occupied-coordinate values are strictly positive and the other coordinates are zero. A *hyperbolic sink* means all eigenvalues of the derivative of the second iterate have modulus strictly smaller than one. *Strictly positive forward orbit* means every coordinate at every finite iterate is strictly positive. The exceptional boundary interactions \(\alpha=q(R)\), \(\beta=q(R)\) are not asserted inaccessible. At \(R=R_*\) and \(c=c_*\), a transverse multiplier is \(-1\), so that boundary is excluded from hyperbolicity.

## Proof
**Axis two-cycle census.** The axes are invariant; on any one of them the occupied coordinate evolves by \(f_R(t)=(1+R)t-Rt^2\). Direct composition gives
\[
 f_R(f_R(t))-t=-Rt(t-1)
 \left[R^2t^2-R(R+2)t+(R+2)\right].
\]
Besides the fixed points \(0\) and \(1\), the quadratic has discriminant \(R^2(R^2-4)\), hence precisely two distinct positive roots \(u_\pm\) if \(R>2\), mutually exchanged by \(f_R\). At \(R=2\) the roots merge with the fixed point \(1\), and below it they are nonreal. Cyclic permutation produces exactly one axis-supported two-cycle on each axis.

**Full-space multipliers.** At \((t,0,0)\), the Jacobian is upper triangular:
\[
 DF(t,0,0)=\begin{pmatrix}
 1+R-2Rt & -R\alpha t & -R\beta t\\
 0&1+R-R\beta t&0\\
 0&0&1+R-R\alpha t
\end{pmatrix}.
\]
Its two-step product remains upper triangular. Since
\[
 u_++u_-=(R+2)/R,\qquad u_+u_-=(R+2)/R^2,
\]
the longitudinal product equals \(5-R^2\), and a transverse product is
\[
 (1+R-Rcu_+)(1+R-Rcu_-)
 =(R+1)^2-(R+1)(R+2)c+(R+2)c^2
 =p_R(c).
\]
Cyclic coordinate permutation leaves the spectrum unchanged. Thus the full-space sink criterion is necessary and sufficient as stated.

**Exact reentrant threshold.** The strict longitudinal condition \(|5-R^2|<1\) is exactly \(2<R<\sqrt6\). As \(R>2\), \(p_R(c)<1\) holds exactly on \((1,R)\). The quadratic is convex with unique minimum at \((R+1)/2\), where
\[
 \min p_R=-\frac{(R+1)^2(R-2)}4.
\]
The minimum crosses \(-1\) when \((R+1)^2(R-2)=4\), equivalently \(R^3-3R-6=0\). This cubic has strictly positive derivative for \(R>2\), and its unique such root lies between \(2\) and \(\sqrt6\). Solving \(p_R(c)=-1\) yields \(c_\pm\). At the root the single equality \(p=-1\) excludes \(c_*\); above it the entire closed interval \([c_-,c_+]\) is excluded. Taylor expansion of \(R^3-3R-6\) at its simple root gives the square-root width.

**Positive-orbit accessibility.** The one-step multiplier of a small absent-species coordinate at a phase with resident population \(u_+\) is \(1+R-Rcu_+\), positive exactly when \(c<q(R)\) and negative when \(c>q(R)\). The corresponding multiplier at \(u_-\) is strictly positive whenever \(c<q(R)\). For \(1<\alpha,\beta<q(R)\), both phases have strictly positive per-capita factors in a neighborhood of each axis-cycle. Each such cycle is a full-space hyperbolic sink because \(1<q(R)\), \(p_R(q)=0\), and \(q<(R+1)/2\) imply \(q\) lies in the first stability band. A sufficiently small trapping neighborhood for the two-step map, intersected with the strict positive cone, provides a nonempty open set of positive initial states staying positive and converging to the cycle.

For \(c>q(R)\), a resident coordinate sufficiently close to \(u_+\), with the other two coordinates sufficiently small and positive, has a **negative** absent-species next-step per-capita factor associated to \(c\), by continuity. Any purported strictly positive orbit converging to the axis-cycle eventually visits this neighborhood in the \(u_+\) phase, giving a negative coordinate on the next iterate: contradiction. Finally \(p_R(q)=0\), \(1<q<(R+1)/2\), and the quadratic shape show \(q\) is in the lower stable band while the entire upper reentrant band lies above \(q\).

## Verification
Run `python check.py` with SymPy installed. It independently checks the scalar cycle polynomial identities, the complete two-step Jacobian diagonal, the exact transverse factorization, the cubic critical equation, the positivity threshold, and three rational parameter cases. For \(R=12/5\), the longitudinal Floquet multiplier is \(-19/25\); setting \(\alpha=\beta=11/10\) gives transverse multipliers \(107/250\) (positive-basin sinks), setting both to \(17/10\) gives \(-289/250\) (transverse instability), and setting both to \(11/5\) gives \(-7/125\) (real-space reentrant sinks inaccessible to persistently positive trajectories). These examples corroborate but do not replace the proof's exhaustive real-parameter argument.

## Relationship to prior work
Muni's 2024 study introduced the specific cyclic three-species update for numerical investigations of tori, period-six structures, and hyperchaotic behavior; its analyzed bifurcations have different parameter regimes and do not supply the precise axis-supported two-cycle sink diagram. Joshi–Savescu–Syed–Blackmore (2021) study the general discrete three-species Lotka–Volterra family, including invariant coordinate axes and period-doubling, but their detailed concrete examples use weak interspecies interactions and do not derive this cyclic strong-competition reentrant threshold or the positivity-accessibility barrier. Other published notes on neutral May–Leonard invariant simplices or two-site logistic transverse reentrance concern different maps and do not imply this result without the new exact Jacobian and positivity analysis. General logistic-map period-two formulas are used as known building blocks, not claimed original.

## Limitations
Only the three **axis-supported** primitive period-two orbits are counted; other off-axis periodic orbits are not classified. No claim about global attraction, invariant measures, or a globally invariant positive octant is made. The critical equalities \(c=q(R)\), \(|p_R(c)|=1\), and \(R=\sqrt6\) are not assigned nonlinear stability types. The full text of the related 2010 three-dimensional economic Lotka–Volterra article was not available for complete comparison; priority remains provisional pending inspection of that source and any unindexed equivalent result. The proof and checks have not undergone independent mathematical audit.

## References
- S. S. Muni, *Torus and hyperchaos in 3D Lotka–Volterra map*, arXiv:2408.15054v1 (first posted 2024-08-27), https://arxiv.org/html/2408.15054.
- Y. Joshi, M. Savescu, M. Syed, D. Blackmore, *Interesting Features of Three-Dimensional Discrete Lotka-Volterra Dynamics*, Applied Mathematics 12 (2021), 694–722, https://doi.org/10.4236/am.2021.128049.
- G. I. Bischi, F. Tramontana, *Three-dimensional discrete-time Lotka–Volterra models with an application to industrial clusters*, Communications in Nonlinear Science and Numerical Simulation 15 (2010), 3000–3014, https://doi.org/10.1016/j.cnsns.2009.10.021 (abstract consulted; full text not inspected).
- D. Blackmore, J. Chen, J. Perez, M. Savescu, *Dynamical properties of discrete Lotka–Volterra equations*, Chaos, Solitons & Fractals 12 (2001), 2553–2568, https://doi.org/10.1016/S0960-0779(00)00214-9 (abstract consulted).
