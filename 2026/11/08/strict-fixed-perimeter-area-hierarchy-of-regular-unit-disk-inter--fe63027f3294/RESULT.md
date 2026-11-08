# Strict fixed-perimeter area hierarchy of regular unit-disk intersections

## Finding
Let \(0<P<2\pi\), and let \(m\ge2\) be an integer. Set
\[
 u=\pi-P/2,\quad \alpha=\pi/m,\quad
 t_m=\frac{\sin(u/m)}{\sin(\pi/m)},\quad
 c_j=t_m\bigl(\cos(2\pi j/m),\sin(2\pi j/m)\bigr).
\]
For closed Euclidean unit disks \(B(c_j,1)\), define
\[
 K_m(P)=\bigcap_{j=0}^{m-1}B(c_j,1),\qquad A_m(P)=\operatorname{area}(K_m(P)).
\]
Each \(K_m(P)\) has perimeter exactly \(P\). For \(m=2\), it is a nondegenerate lens; for \(m\ge3\), a regular disk-polygon with \(m\) genuine circular arcs. Its area is
\[
 \boxed{A_m(P)=\pi-u-\frac{m\sin(u/m)\sin((\pi-u)/m)}{\sin(\pi/m)}.}
\]
The strict hierarchy and limiting disk-area are
\[
 \boxed{A_2(P)<A_3(P)<A_4(P)<\cdots<\frac{P^2}{4\pi}.}
\]
The precise large-\(m\) deficit, for each fixed \(P\), is
\[
 \frac{P^2}{4\pi}-A_m(P)
 =\frac{u^2(\pi-u)^2}{3\pi m^2}+O_P(m^{-4}).
\]
The lens endpoint has a different small-perimeter exponent:
\[
 A_2(P)=\frac{P^3}{48}+O(P^5),
\]
whereas each fixed \(m\ge3\) satisfies
\[
 A_m(P)=\frac{\cot(\pi/m)}{4m}P^2+\frac{P^3}{12m^2}+O_m(P^4).
\]
For fixed \(m\ge3\), at the near-ball endpoint \(u\downarrow0\),
\[
 A_m(P)-A_2(P)=\frac{\cot(\pi/m)}{m}u^2+O_m(u^3).
\]

## Assumptions and scope
All disks have radius one in the Euclidean plane. The generating centers form a regular \(m\)-point orbit of radius \(t_m\); no minimization over irregular centers is asserted. Perimeter denotes the arclength of the full convex boundary. Every inequality is strict for finite \(m\) and \(0<P<2\pi\). Endpoints \(P=0\) and \(P=2\pi\) are excluded: at the latter the centers coincide and there are no \(m\) distinct arcs; at the former the intersection collapses. The error terms hold with \(P\), respectively \(m\), fixed as indicated.

## Proof
**Arc geometry.** Fix \(m\), abbreviate \(t=t_m\), \(\alpha=\pi/m\), and let \(0<t<1\). The intersection of adjacent unit-circle boundaries in the direction opposite the bisector of their centers gives the unique exposed corner of the disk intersection in that angular sector. Indeed, at a point of fixed radius the farthest center is a center nearest to the opposite radial direction; the two adjacent centers tie exactly on the bisector, and all other disk inequalities are then weaker. The intersection is rotationally symmetric and has exactly \(m\) equally spaced boundary vertices. In the degenerate \(m=2\) case there are two vertices and the regular polygon joining them has zero area.

Let \(\beta\in(0,\alpha)\) be half the angular span of any circular boundary arc as viewed from its generating center. The triangle formed by the origin, one center, and an adjacent boundary vertex yields
\[
 \sin(\alpha-\beta)=t\sin\alpha,
 \qquad \beta=\alpha-\arcsin(t\sin\alpha).
\]
The defining relation \(t=\sin(u/m)/\sin\alpha\), together with \(0<u/m<\alpha\le\pi/2\), gives
\[
 \beta=\frac{\pi-u}{m}.
\]
Thus the \(m\) arcs, each of radius one and angle \(2\beta\), have total perimeter \(2m\beta=2(\pi-u)=P\).

**Exact area.** The radial distance \(s\) of a boundary corner from the origin is \(s=\sin\beta/\sin\alpha\), by the sine rule in the same triangle. Connect successive corners. The regular polygon they enclose has area \(m s^2\sin\alpha\cos\alpha\), valid as zero also for \(m=2\). The cap between a circular arc of angle \(2\beta\) and its chord has area \(\beta-\sin\beta\cos\beta\). Caps have disjoint interiors, and their union with the polygon is the disk intersection. Therefore
\[
 A_m=m\left(\frac{\sin^2\beta\cos\alpha}{\sin\alpha}
 +\beta-\sin\beta\cos\beta\right)
 =m\beta-\frac{m\sin\beta\sin(\alpha-\beta)}{\sin\alpha}.
\]
Substitution of \(\beta=(\pi-u)/m\) and \(\alpha-\beta=u/m\) gives the displayed formula. In particular, \(A_2(P)=\pi-u-\sin u\).

**Strict monotonicity.** Extend the index to \(x\in(0,1/2]\) via
\[
 F(x)=\frac{\sin(ux)\sin((\pi-u)x)}{x\sin(\pi x)},
 \qquad A_m(P)=\pi-u-F(1/m).
\]
Put \(f(z)=z\cot z\) for \(0<z\le\pi/2\) and \(f(0)=1\). Direct differentiation yields
\[
 f''(z)=2\csc^2z\,(z\cot z-1)<0
 \qquad(0<z\le\pi/2),
\]
where the strict sign follows from \(\tan z>z\). Thus \(f\) is strictly concave on \([0,\pi/2]\). For \(a=ux>0\), \(b=(\pi-u)x>0\), \(a+b=\pi x\le\pi/2\), strict concavity implies
\[
 f(a)+f(b)>f(0)+f(a+b)=1+f(a+b).
\]
Consequently
\[
 x\frac{d}{dx}\log F(x)
 =f(a)+f(b)-1-f(a+b)>0.
\]
Since \(F\) strictly increases with \(x\), the areas strictly increase as integer \(m\) increases. Moreover \(\lim_{x\downarrow0}F(x)=u(\pi-u)/\pi\), giving \(A_\infty(P)=(\pi-u)^2/\pi=P^2/(4\pi)\), strictly greater than each finite member.

**Sharp endpoint expansions.** Taylor-expanding \(\sin\) at zero gives, for fixed \(u\in(0,\pi)\),
\[
 F(1/m)=\frac{u(\pi-u)}{\pi}
 +\frac{u^2(\pi-u)^2}{3\pi m^2}+O_u(m^{-4}).
\]
For \(P\downarrow0\), put \(q=P/2\). The exact formula becomes
\[
 A_m=q-m\sin(q/m)\cos(q/m)
       +m\cot(\pi/m)\sin^2(q/m).
\]
The first two terms equal \(P^3/(12m^2)+O_m(P^5)\); the third equals \(\cot(\pi/m)P^2/(4m)+O_m(P^4)\). At \(m=2\) this quadratic part vanishes and the exact lens formula \(A_2=P/2-\sin(P/2)\) yields the stated cubic leading term. The near-ball lens comparison follows from the same Taylor expansion at \(u=0\).

## Verification
The accompanying standard-library script `verify.py` recomputes the intersection area independently from the radial function
\[
 \varrho(\theta)=\min_j\bigl(t\cos(\theta-2\pi j/m)+
 \sqrt{1-t^2\sin^2(\theta-2\pi j/m)}\bigr)
\]
and midpoint integration of \(\frac12\int_0^{2\pi}\varrho(\theta)^2\,d\theta\). It additionally tests strict order and the limiting expansions at finite sample points. The independent quadrature and finite tests are corroboration only; the proof above is analytic and applies to all real \(P\) in the stated interval and all integers \(m\ge2\).

## Relationship to prior work
Drach and Tatarko prove that the unit-disk lens minimizes area among *all* unit-ball intersections at prescribed perimeter (2026, arXiv:2610.40291). The classical isoperimetric inequality makes the disk the maximum. Neither endpoint theorem supplies the strict, common-perimeter hierarchy between regular \(m\)-disk intersections, its exact areas, or the quantified degeneration at \(m=2\). Basit and Lángi (2023, arXiv:2307.04026) study Dowker-type extrema of disk-polygons inscribed in or circumscribed about a *fixed* convex body, rather than a fixed-perimeter family. Kratky (1978) gives area calculations for equal-disk intersections and is relevant to the formula, without an identified fixed-perimeter strict-order theorem. A separate published area formula for disk intersections with generating centers constrained to one circle and a fixed disk radius concerns a different normalization and objective; the relationship remains a priority caveat, not an assertion of general uniqueness.

## Limitations
No theorem is claimed for irregular placements of \(m\) centers, higher dimensions, spherical/hyperbolic curvature, or fixed width instead of fixed perimeter. The intersection-area identity may overlap older computational literature; the fixed-perimeter strict comparison and endpoint rates have been compared against accessible records, but historical priority remains provisional. No independent mathematical audit has been performed.

## References
- K. Drach and K. Tatarko, *A complete solution to the reverse isoperimetric problem for λ-convex bodies*, arXiv:2610.40291v1 (first public 2026-10-29), https://arxiv.org/abs/2610.40291.
- B. Basit and Z. Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026 (2023), https://arxiv.org/abs/2307.04026.
- K. W. Kratky, *The area of intersection of n equal circular disks*, J. Phys. A: Math. Gen. 11 (1978), 1017, https://doi.org/10.1088/0305-4470/11/6/006.
