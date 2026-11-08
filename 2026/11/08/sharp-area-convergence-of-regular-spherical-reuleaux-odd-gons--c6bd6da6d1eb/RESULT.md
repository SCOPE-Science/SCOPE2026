# Sharp area convergence of regular spherical Reuleaux odd-gons

## Finding

On the unit sphere, fix a geodesic width \(0<w\le\pi/2\). For each odd integer \(n\ge3\), let \(W_{n,w}\) be the regular spherical Reuleaux \(n\)-gon obtained by intersecting the geodesic radius-\(w\) disks about the vertices of a regular spherical \(n\)-gon whose largest vertex distance is \(w\). Let \(A_n\) and \(L_n\) be the spherical area and perimeter of this body.

Put \(s=\sin(w/2)\), \(c=\cos(w/2)\), and
\[
\alpha_n=2\arcsin\!\left(\frac{\sin(\pi/(2n))}{c}\right).
\]
The exact metric profiles are
\[
\boxed{L_n=n\alpha_n\sin w,\qquad A_n=2\pi-n\alpha_n(1+\cos w).}
\]
Let \(A_\infty=2\pi(1-c)\) and \(L_\infty=2\pi s\) denote the area and perimeter of the geodesic disk of radius \(w/2\), and put \(\Delta_n=A_\infty-A_n\). Then
\[
0<A_3<A_5<A_7<\cdots<A_\infty,\qquad
L_3>L_5>L_7>\cdots>L_\infty.
\]
Moreover, **the renormalized deficit \(n^2\Delta_n\) is strictly decreasing** over odd \(n\ge3\), with the sharp limit
\[
\boxed{\lim_{n\to\infty,\ n\ \mathrm{odd}}n^2\Delta_n=K_w:=\frac{\pi^3\sin^2(w/2)}{12\cos(w/2)}.}
\]
Equivalently, the following **global two-sided, sharp-endpoint inequality** holds for every odd \(n\ge3\):
\[
\boxed{\frac{K_w}{n^2}<A_\infty-A_n\le\frac{9(A_\infty-A_3)}{n^2}.}
\]
The upper equality holds exactly at \(n=3\); the lower constant is optimal in the limit and is never attained at finite \(n\). The perimeter difference is exactly
\[
L_n-L_\infty=\tan(w/2)\,\Delta_n,
\]
so the same strict normalized monotonicity and sharp bound hold for perimeters after multiplication by \(\tan(w/2)\). In particular,
\[
A_\infty-A_n=\frac{K_w}{n^2}+O_w(n^{-4}),\qquad
L_n-L_\infty=\frac{K_w\tan(w/2)}{n^2}+O_w(n^{-4}).
\]

## Assumptions and scope

The ambient metric is the standard intrinsic great-circle distance on the unit \(2\)-sphere; area and arclength have curvature-one normalization. The generating regular spherical \(n\)-gon is obtained from \(n\) equally azimuthally spaced vertices on a small circle about a pole. Because \(n\) is odd, adjacent vertices have a unique cyclically opposite vertex. Its radius is uniquely chosen so that the largest of the pairwise geodesic distances between generating vertices is \(w\). The disk intersection \(W_{n,w}\) is spherical convex and of constant width \(w\) for \(0<w\le\pi/2\), as established in the literature on spherical Reuleaux constructions.

The theorem quantifies the geometry of these particular regular curved polygons. It does not assert an extremal inequality for all constant-width bodies with a prescribed number of corners. The special endpoint \(w=\pi/2\) is included; at this width the boundary arcs are great-circle segments, and the area formula reduces to the previously known one for regular spherical odd-gons.

## Proof

Write \(t=\pi/(2n)\), \(s=\sin(w/2)\), and \(c=\cos(w/2)\); in the stated domain \(0<t\le\pi/6\), \(1/\sqrt2\le c<1\), and \(\sin t<c\).

**1. Generating geometry and one arc.** If \(\rho\) is the spherical radius of the generating small circle, a pair of farthest vertices subtends azimuthal angle \(\pi-\pi/n\). The spherical cosine law yields
\[
\cos w=1-(1+\cos(\pi/n))\sin^2\rho,
\qquad\text{hence}\qquad
\sin\rho=\frac{s}{\cos t}.
\]
If \(a\) is the spherical side length between adjacent generating vertices, the same cosine law gives
\[
\cos a=1-2\sin^2\rho\sin^2(\pi/n)=1-8s^2\sin^2t.
\]
Every boundary arc of \(W_{n,w}\) is part of the geodesic circle of radius \(w\) centered at the unique vertex opposite to its two adjacent endpoints. Let \(\alpha\) be its azimuthal aperture as seen from that vertex. The isosceles spherical triangle with sides \(w,w,a\) gives
\[
\cos a=\cos^2w+\sin^2w\cos\alpha,
\quad\text{so}\quad
\sin(\alpha/2)=\frac{2s\sin t}{\sin w}=\frac{\sin t}{c}.
\]
As the boundary arc is the shorter one and \(0<\alpha<\pi\), this proves \(\alpha=2\arcsin(\sin t/c)=\alpha_n\).

**2. Area and perimeter.** A geodesic circle of radius \(w\) has arclength element \(\sin w\,d\varphi\), hence the \(n\) congruent arcs give \(L_n=n\alpha_n\sin w\). Its inward curvature magnitude (with positively oriented convex boundary) is \(\cot w\) and hence its total geodesic curvature contribution is \(n\alpha_n\cos w\). At each vertex, the two incident radius-\(w\) circles have their centers at the adjacent opposite vertices; the spherical isosceles triangle there has the same angle \(\alpha_n\), and this is the exterior turning angle. The spherical Gauss–Bonnet formula for a topological disk gives
\[
A_n+n\alpha_n\cos w+n\alpha_n=2\pi.
\]
This proves the area formula. In particular \(A_n+L_n\cot(w/2)=2\pi\), an instance of the existing spherical Barbier identity; that general identity is not claimed as new.

**3. Strict monotonicity and disk limit.** Define
\[
h(t)=\arcsin\left(\frac{\sin t}{c}\right),\qquad 0\le t\le\pi/6.
\]
Then \(h(0)=0\), \(h'(0)=1/c\), and direct differentiation gives
\[
h''(t)=\frac{s^2\sin t}{(c^2-\sin^2t)^{3/2}}>0\quad(t>0).
\]
Thus \(h(t)/t\) is strictly increasing with \(t\), and its limit at zero is \(1/c\). Since \(n\alpha_n=\pi h(t)/t\) and \(t=\pi/(2n)\), the quantity \(n\alpha_n\) decreases strictly as odd \(n\) increases, to \(\pi/c\). The area and perimeter formulas give the asserted strict monotonicity and the disk limits.

**4. A sharp monotone normalized deficit.** From the formulas already proved,
\[
\Delta_n=2\pi c^2\left(\frac{h(t)}t-\frac1c\right),
\qquad
n^2\Delta_n=\frac{\pi^3c^2}{2}\,\frac{h(t)-t/c}{t^3}.
\]
Differentiate once more:
\[
h'''(t)=\frac{s^2\cos t(c^2+2\sin^2t)}{(c^2-\sin^2t)^{5/2}}.
\]
To see that \(h'''\) is strictly increasing, set \(z=\sin^2t\). On \(0\le z\le1/4\), \(1/2\le c^2<1\), its logarithmic derivative with respect to \(z\) (ignoring the positive constant \(s^2\)) is
\[
-\frac1{2(1-z)}+\frac2{c^2+2z}+\frac5{2(c^2-z)}>0.
\]
Indeed it equals \[\frac2{c^2+2z}+\frac2{c^2-z}+\frac{1-c^2}{2(c^2-z)(1-z)},\] whose three summands are positive. The identity \(h''(0)=0\) and the integral form of Taylor's formula therefore give
\[
\frac{h(t)-t/c}{t^3}
=\frac12\int_0^1(1-u)^2h'''(ut)\,du,
\]
which is strictly increasing in \(t>0\). Therefore \(n^2\Delta_n\) strictly decreases as \(n\) increases. At \(t\downarrow0\), \(h'''(0)=s^2/c^3\), so the integral tends \(s^2/(6c^3)\), yielding
\[
\lim_{n\to\infty}n^2\Delta_n
=\frac{\pi^3c^2}{2}\frac{s^2}{6c^3}
=\frac{\pi^3s^2}{12c}=K_w.
\]
Its largest value among odd \(n\ge3\) is \(9\Delta_3\). Strictness proves precisely the stated equality and nonattainment cases. Finally the Barbier identity and the disk formulas yield \(L_n-L_\infty=\tan(w/2)\Delta_n\). Analyticity of \(h\) about zero gives the displayed \(O_w(n^{-4})\) remainders after the cubic Taylor term.

## Verification

The standalone script `verify.py` derives the expression for \(h'''\) independently with symbolic differentiation; checks 212 exact-formula high-precision parameter instances, including near-flat and hemispherical widths; verifies all sharp inequalities and monotonicities; recomputes twelve boundary-arc apertures directly from spherical cosine laws; checks the previously known \(w=\pi/2\) endpoint formula in five instances; and samples 960,000 area-uniform orientations across four disk intersections without using the Gauss–Bonnet area formula. It returned:

`VERIFY_OK symbolic_third_derivative=1 strict_normalized_cases=212 spherical_arc_cases=12 endpoint_cases=5 monte_carlo_orientation_samples=960000 max_area_deviation=0.00805753`

The samples are numerical consistency tests, not infinite proofs. The inequalities and limit follow from the displayed derivative signs and the integral Taylor formula.

## Relationship to prior work

Lassak (first publicly available December 6, 2013) introduced and analyzed the spherical Reuleaux odd-gon construction and its constant-width property. Lassak and Musielak further developed spherical constant-width bodies. These sources establish the object but do not state the present all-width finite-\(n\) area hierarchy and normalized sharp bounds.

Araújo established a spherical analogue of Barbier's theorem; the area-perimeter identity for arbitrary constant-width bodies is prior knowledge. Leichtweiss and later authors established spherical Blaschke–Lebesgue minimum-area results; in particular, the Reuleaux triangle is the fixed-width area minimizer, and this fact is not a new contribution here. Liu and Chang (2022) explicitly obtain the area \(2\pi-2n\arcsin(\sqrt2\sin(\pi/(2n)))\) for a regular spherical \(n\)-gon at the endpoint width \(w=\pi/2\). That endpoint formula is prior-covered and provides an exact check on our normalization.

A published exact area-and-perimeter profile exists for **hyperbolic** regular Reuleaux odd-gons. Its curvature, arc-aperture equation, and Gauss–Bonnet sign are different; it neither gives the spherical family at \(0<w<\pi/2\) nor implies the new strict normalized \(n^2\)-deficit hierarchy. The contribution isolated here is the complete spherical fixed-width regular-family hierarchy for all \(0<w\le\pi/2\), with best lower asymptotic and upper finite-corner constants.

## Limitations

The result does not extend automatically to irregular spherical constant-width curves, widths greater than \(\pi/2\), or nonconstant curvature surfaces. It does not prove an optimal rate uniformly as \(w\to0\) without width-dependent normalization, or a quantitative Hausdorff approximation theorem. Exact metric formulas and special width-\(\pi/2\) and \(n=3\) results have important precedents; the originality assessment is limited to the stated sharp full-family comparison. Leichtweiss's older full paper could not be inspected, so an unrecognized equivalent historical expression remains possible. No independent external verification has been performed.

## References

M. Lassak, “Width of spherical convex bodies,” *Aequationes Mathematicae* **89** (2015), 555–567, DOI: 10.1007/s00010-013-0237-3; first published online December 6, 2013.

M. Lassak and M. Musielak, “Spherical bodies of constant width,” *Aequationes Mathematicae* **92** (2018), 627–640, DOI: 10.1007/s00010-018-0558-3; arXiv:1801.01161.

P. V. Araújo, “Barbier's theorem for the sphere and the hyperbolic plane,” *L'Enseignement Mathématique* **42** (1996), 295–309.

C. Liu and Y. Chang, “Extremal problems for spherical convex polygons,” *Archiv der Mathematik* **118** (2022), 435–450, DOI: 10.1007/s00013-021-01698-7.

A. Freyer and Á. Sagmeister, “The isominwidth problem on the 2-sphere,” *Mathematika* **72** (2026), article e70069, DOI: 10.1112/mtk.70069; arXiv:2411.11462.

K. Leichtweiss, “Curves of constant width in the non-Euclidean geometry,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **75** (2005), 257–284, DOI: 10.1007/BF02942046 (full text not accessed).
