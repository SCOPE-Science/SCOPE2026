# Half-perimeter extremizers and sharp quadratic lens-gap stability for regular disk intersections

## Finding
For each integer \(m\ge3\) and \(0<P<2\pi\), let \(K_m(P)\subset\mathbb R^2\) be the intersection of \(m\) closed unit disks whose centers are equally spaced on a circle, with the center-circle radius uniquely chosen so that the intersection has boundary perimeter \(P\). Let \(L(P)\) be the two-unit-disk lens of the same perimeter, and define its area excess
\[
\Delta_m(P)=\operatorname{area}(K_m(P))-\operatorname{area}(L(P)).
\]
The endpoint values at \(P=0\) and \(P=2\pi\) are defined by continuous extension; the former is a singleton and the latter the unit disk. Define
\[
\boxed{G_m=1-\frac m2\tan\left(\frac\pi{2m}\right)>0.}
\]
**For every integer \(m\ge3\), the unique perimeter maximizing the lens-area excess is exactly \(P=\pi\)**, independent of the number of disks, and the maximum is \(G_m\). More strongly, the following **globally sharp quadratic stability inequality** holds simultaneously for all such \(m\) and every \(0\le P\le2\pi\):
\[
\boxed{0\le\Delta_m(P)\le G_m\left(1-\frac{(P-\pi)^2}{\pi^2}\right).}
\]
The upper inequality has equality precisely at \(P=0,\pi,2\pi\); the lower inequality has equality precisely at \(P=0,2\pi\). Equivalently,
\[
\boxed{G_m-\Delta_m(P)\ge\frac{G_m}{\pi^2}(P-\pi)^2,}
\]
and the coefficient \(G_m/\pi^2\) is best possible even if the two degenerate endpoint bodies are excluded, by taking their limits. The optimizing center-circle radius is
\[
\boxed{t_m^*=\frac{1}{2\cos(\pi/(2m))}.}
\]
For \(m=3\), the maximizer is the unit Reuleaux triangle and \(G_3=1-\sqrt3/2\). The maxima strictly increase with \(m\), converging to \(1-\pi/4\). That monotonicity is an already-known consequence of the fixed-perimeter regular-disk hierarchy; the present contribution is the **perimeter-independent location of every maximum and the globally optimal quadratic envelope with its complete equality cases**.

## Assumptions and scope
All distances, areas, and perimeters are Euclidean; the generating disks have common radius one and regular \(m\)-gon center configurations. A unique center radius determines each nondegenerate perimeter \(P\in(0,2\pi)\). As \(P\downarrow0\) the intersection collapses to a point, while \(P\uparrow2\pi\) the centers coalesce and the body becomes a unit disk; both are included only through continuous limits. The claim does not concern arbitrary nonregular generating centers, unequal radii, or the maximum over all unit-ball convex bodies. Arbitrary common-radius scaling is immediate and is not a separate theorem.

## Proof
**1. Exact area difference from arc geometry.** The following perimeter/area representation for regular intersections of unit disks is already available in the literature and can also be derived by adding the regular corner polygon and its equal circular segments. Set
\[
q=P/2\in[0,\pi],\qquad \alpha=\pi/m,\qquad u=\pi-q.
\]
The generating centers lie on the circle of radius
\[
t_m(P)=\frac{\sin(u/m)}{\sin\alpha}.
\]
Each exposed unit-circle arc has half-angle \(\beta=q/m\), and \(P=2m\beta\). The corner polygon has circumradius \(r=\sin\beta/\sin\alpha\), by the sine rule in the triangle connecting the origin, one generating center and one corner. Its area is \(mr^2\sin\alpha\cos\alpha\); the \(m\) circular segments between its edges and the exposed arcs each have area \(\beta-\sin\beta\cos\beta\). Summing these two explicitly disjoint pieces, with \(t_m=\sin(\alpha-\beta)/\sin\alpha\), yields the intersection area
\[
A_m(P)=q-\frac{m\sin((\pi-q)/m)\sin(q/m)}{\sin\alpha}.
\]
A symmetric two-unit-disk lens with perimeter \(P\) has area \(A_2(P)=q-\sin q\). Product-to-sum therefore gives the exact excess
\[
\boxed{\Delta_m(P)=\sin q-\frac{m}{2\sin\alpha}\left[\cos\left(\frac{\pi-2q}{m}\right)-\cos\alpha\right].}
\]
It is symmetric under \(q\mapsto\pi-q\), and has zero endpoint limits.

**2. Every maximum is at half the full-circle perimeter.** Put \(\beta=\pi/2\) and \(k=m/(2\sin\alpha)\). Differentiating with respect to \(q\) yields
\[
\frac{d\Delta_m}{dq}=\cos q-\frac{\sin((\pi-2q)/m)}{\sin\alpha}.
\]
For \(0<q<\pi/2\), let \(z=(\pi/2-q)/(\pi/2)\in(0,1)\). The derivative is strictly positive exactly when
\[
\frac{\sin(\alpha z)}{\sin(\beta z)}<\sin\alpha.
\]
This inequality follows by differentiation: for \(0<\alpha<\beta=\pi/2\), the function \(z\mapsto\sin(\alpha z)/\sin(\beta z)\) increases strictly, since \(x\mapsto x\cot x\) decreases strictly on \((0,\pi/2]\). Its value at \(z=1\) is \(\sin\alpha/\sin\beta=\sin\alpha\). Symmetry therefore makes \(\Delta_m\) strictly increase until \(q=\pi/2\) and strictly decrease after. Substitution gives
\[
\Delta_m(\pi)=1-\frac m{2\sin\alpha}(1-\cos\alpha)=1-\frac m2\tan(\alpha/2)=G_m.
\]
At this perimeter, \(u=\pi/2\) and \(t_m=\sin(\alpha/2)/\sin\alpha=1/(2\cos(\alpha/2))\). Positivity of \(G_m\) follows, for example, from \(m\tan(\pi/(2m))/2\le\sqrt3/2<1\) for \(m\ge3\) because \(x\mapsto\tan x/x\) is strictly increasing. These facts also prove \(\Delta_m(P)>0\) for the nondegenerate interval.

**3. A uniform strict quadratic remainder.** Write \(s=(P-\pi)/\pi\in[-1,1]\), so \(q=\pi/2+(\pi/2)s\). With \(\beta=\pi/2\), \(k=m/(2\sin\alpha)\), the exact excess is
\[
\Delta_m(P)=\cos(\beta s)-k[\cos(\alpha s)-\cos\alpha].
\]
For \(0\le t\le1\) and \(0<a\le\pi/2\), define
\[
E_a(t)=1-\cos(at)-t^2(1-\cos a).
\]
Taylor's alternating cosine series, with the positive terms ordered by decreasing magnitude on the stated domain, gives
\[
\frac{a^4}{24}\left(1-\frac{a^2}{15}\right)t^2(1-t^2)
\le E_a(t)\le\frac{a^4}{24}t^2(1-t^2).
\]
Indeed, the quadratic terms cancel, the first surviving term is \(a^4t^2(1-t^2)/24\), and the next has opposite sign and magnitude at most \(a^6t^2(1-t^2)/360\), since \(t^2-t^6\le2t^2(1-t^2)\); all later alternating terms decrease in absolute magnitude.

Consequently, for every \(0<t<1\),
\[
E_\beta(t)-kE_\alpha(t)\ge
\frac{t^2(1-t^2)}{24}\left[\beta^4\left(1-\frac{\beta^2}{15}\right)-k\alpha^4\right]>0.
\]
To verify strict positivity **uniformly in all integers \(m\ge3\)**, note \(\sin\alpha\ge2/m\) for \(\alpha=\pi/m\in(0,\pi/3]\). Thus
\[
k\alpha^4\le\frac{\pi^4}{4m^2}\le\frac{\pi^4}{36}
<\frac{\pi^4}{16}\left(1-\frac{\pi^2}{60}\right)=\beta^4\left(1-\frac{\beta^2}{15}\right),
\]
where the strict middle inequality follows already from \(\pi<4\).

Finally, since \(1-\cos\beta=1\), direct rearrangement gives the exact identity
\[
G_m-\Delta_m(P)-G_ms^2=E_\beta(|s|)-kE_\alpha(|s|).
\]
The right side is strictly positive when \(0<|s|<1\), and is zero at \(s=0,\pm1\). This proves the sharp quadratic upper envelope, all equality cases, and optimality of its coefficient by the endpoint limits. The lower bound and its equality cases were proved in Step 2.

**4. The number-of-disks endpoint.** The maximum formula satisfies \(G_m\uparrow1-\pi/4\) as \(m\to\infty\), because \(\tan x/x\) is strictly increasing and \(\tan x/x\to1\) as \(x\to0\). At \(m=3\) the optimizing center radius is \(1/\sqrt3\), so the equilateral center separation is one and the intersection is exactly the unit Reuleaux triangle.

## Verification
The accompanying `verify.py` reconstructs the algebraic area-difference identity, verifies the optimizer formula and equality endpoints symbolically, and independently integrates the radial function of the original intersection of regular-center unit disks for several disk counts and perimeters. Numerical sweeps also corroborate strict interior sharp-stability inequalities. The continuum and all-integer statements follow from the analytic arguments, not from finite tests.

## Relationship to prior work
Drach and Tatarko (2026) prove that a unit lens is the universal minimum-area unit-ball intersection for its perimeter. Their result supplies the baseline \(\Delta_m\ge0\), not the global **maximum of excess** as the perimeter varies or a best upper stability constant. Their earlier (2026) planar reverse-isoperimetric stability theorem concerns Hausdorff closeness to the **minimum** lens rather than a quantitative **maximum-of-gap** regime.

The published *Strict fixed-perimeter area hierarchy of regular unit-disk intersections* (2026) supplies the exact functions \(A_m(P)\) for all \(m\), their strict monotonicity in \(m\) at each fixed perimeter, and the circle limit. These are **credited as prior results**, including the exact area inputs in Step 1 and the increasing-\(m\) observation. The additional statement established here is a simultaneous optimization of the differences \(A_m(P)-A_2(P)\) over the *variable perimeter*, identifying the same unique maximizer for every \(m\), and deriving a globally best quadratic stability envelope with complete equality cases. No claim of inventing the full area profile is made. *A sharp Steiner-area phase diagram for regular disk triangles* (2026) treats parallel-body area at **fixed minimum width**, and Fodor, Robock, and Sagmeister (2026) also optimize under fixed-width constraints; neither supplies the present variable-perimeter gap envelope. Older area formulas for equal disks may permit related deductions, so historical priority remains provisional.

## Limitations
The family is regular (equally spaced) congruent-disk intersections in the Euclidean plane. The sharp constant depends on \(m\), and no area-gap maximization is asserted over arbitrary configurations of \(m\) disk centers. The formula for \(A_m(P)\) is prior art; this is an optimization and stability theorem for its difference from the lens profile. Unindexed historical analyses of the same optimal difference remain an originality risk. Independent mathematical audit has not been performed.

## References
- K. Drach and K. Tatarko, *A complete solution to the reverse isoperimetric problem for \(\lambda\)-convex bodies*, arXiv:2610.40291v1 (first public 2026-10-29), https://arxiv.org/abs/2610.40291.
- K. Drach and K. Tatarko, *Stability of reverse isoperimetric inequalities in the plane: Area, Cheeger, and inradius*, *Bulletin of the London Mathematical Society* 58 (2026), e70292, https://doi.org/10.1112/blms.70292.
- *Strict fixed-perimeter area hierarchy of regular unit-disk intersections* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-strict-fixed-perimeter-area-hierarchy-of-regular-unit-disk-inter--fe63027f3294.
- *A sharp Steiner-area phase diagram for regular disk triangles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-steiner-area-phase-diagram-for-regular-disk-triangles--3d6ed11c0577.
- F. Fodor, N. Robock and Á. Sagmeister, *Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2602.19300 (2026), https://arxiv.org/abs/2602.19300.
- K. W. Kratky, *The area of intersection of n equal circular disks*, *J. Phys. A* 11 (1978), 1017, https://doi.org/10.1088/0305-4470/11/6/006.
