# Exact geodesic escape probability for equatorial spherical zones

## Finding

Fix \(0<\theta<\pi/2\) and let
\[
Z_\theta=\{(x_1,x_2,x_3)\in S^2:|x_3|\leq\sin\theta\},
\]
with the round unit-sphere metric and normalized surface-area probability. If \(X,Y\) are independent samples from \(Z_\theta\), their shorter great-circle arc \([X,Y]_{\min}\) is unique almost surely. Its probability of leaving the zone is exactly
\[
\boxed{\mathbb P\bigl\{[X,Y]_{\min}\not\subset Z_\theta\bigr\}
=\frac{\cos\theta}{2(1+\cos\theta)}.}
\]
The escape probability is strictly decreasing in \(\theta\), with values in \((0,1/4)\). It has the endpoint expansions
\[
\mathbb P(\text{escape})=\frac14-\frac{\theta^2}{16}+O(\theta^4)
\quad(\theta\downarrow0),
\]
\[
\mathbb P(\text{escape})=\frac{\varepsilon}{2}-\frac{\varepsilon^2}{2}
+O(\varepsilon^3),\qquad\varepsilon=\frac\pi2-\theta\downarrow0.
\]
In contrast, when the limiting equator is endowed with uniform arclength measure, both endpoints and their minimizing arc lie on that equator almost surely, so its escape probability is zero. Thus the positive limit \(1/4\) is a genuine singular behavior of normalized two-point surface-area sampling.

## Assumptions and scope

All areas and arclengths are those of the round unit sphere; no Euclidean chords are involved. The equatorial zone has full latitudinal half-width \(\theta\) and area \(4\pi\sin\theta\). Samples are independent and uniform by surface area, not uniform in colatitude or on boundary circles. Antipodal and identical pairs are null events and are excluded when selecting the minimizing arc. No assertion is made for other surfaces, higher-dimensional spheres, or nonuniform measures. The endpoint \(\theta=\pi/2\) (the whole sphere) has escape probability zero; \(\theta=0\) requires a separate one-dimensional sampling convention.

## Proof

**1. Two-point spherical integration.** Let \(H\) range over unoriented two-planes through the origin of \(\mathbb R^3\), equivalently great circles, parametrized by a unit normal \(n\) in a fixed closed hemisphere. Give these normals surface-area measure \(d\sigma(n)\), whose total mass is \(2\pi\). For a nonnegative measurable function \(F\), the two-point spherical Blaschke--Petkantschin identity is
\[
\int_{S^2}\!\int_{S^2} F(x,y)\,dA(x)dA(y)
=\int_{n\in S^2_+}\int_0^{2\pi}\!\int_0^{2\pi}
 F(x_n(u),x_n(v))\,|\sin(u-v)|\,du\,dv\,d\sigma(n).
\tag{1}
\]
Here \(x_n(u)\) is a unit-speed angular parametrization of the great circle perpendicular to \(n\). This is the dimension-two specialization of the established spherical formula; the normalization also follows by taking \(F=1\), since \(\int_0^{2\pi}\int_0^{2\pi}|\sin(u-v)|du\,dv=8\pi\) and \((2\pi)(8\pi)=(4\pi)^2\).

**2. Exactly which pairs escape.** Write \(i\in[0,\pi/2]\) for the inclination of the great circle to the equator. Its maximum absolute latitude is \(i\). With azimuth \(\phi\in[0,2\pi)\), the normal-area element is \(\sin i\,di\,d\phi\). For \(i\le\theta\), the entire great circle lies within \(Z_\theta\), hence no pair escapes. For \(i>\theta\), its intersection with the zone consists of two opposite arcs of equal length
\[
L(i)=2\arcsin\left(\frac{\sin\theta}{\sin i}\right),\qquad 0<L(i)<\pi.
\tag{2}
\]
Pairs in one of these components have their minimizing geodesic contained in the same component, because its length is less than \(\pi\). Pairs in different components must traverse one of the two complementary polar arcs along the great circle and escape. Thus opposite-component pairing is necessary and sufficient, outside null boundary events.

**3. Pair integral over opposite components.** Center the two component arcs at angular parameters \(0\) and \(\pi\). Each ordered integral with the first endpoint in the first component and the second endpoint in the opposite one is
\[
\int_{-L/2}^{L/2}\int_{\pi-L/2}^{\pi+L/2}
 |\sin(u-v)|\,dv\,du
=2\int_0^L (L-t)\sin t\,dt=2(L-\sin L).
\tag{3}
\]
Both orders contribute, yielding \(4(L-\sin L)\). Substituting (2)--(3) into (1), integrating the azimuth, and dividing by the square of the area \((4\pi\sin\theta)^2\), gives
\[
P(\theta)=\frac{I(\sin\theta)}{2\pi\sin^2\theta},\qquad
I(s)=\int_{\arcsin s}^{\pi/2}\sin i\,[L(i)-\sin L(i)]\,di.
\tag{4}
\]

**4. Exact evaluation of the remaining integral.** Put \(c=\sqrt{1-s^2}\) and \(v=\cos i\). Then
\[
I(s)=\int_0^c\left[2\arcsin\left(\frac{s}{\sqrt{1-v^2}}\right)
-\sin\left(2\arcsin\left(\frac{s}{\sqrt{1-v^2}}\right)\right)\right]dv.
\tag{5}
\]
For \(0<s<1\), differentiation under the integral is justified: the only endpoint derivative singularity is integrable, of order \((c-v)^{-1/2}\). The bracket at \(v=c\) equals \(\pi\). Its derivative with respect to \(s\), at fixed \(v<c\), is
\[
\frac{4s^2}{(1-v^2)\sqrt{c^2-v^2}}.
\]
Consequently,
\[
\begin{aligned}
I'(s)&=-\frac{\pi s}{c}
+4s^2\int_0^c\frac{dv}{(1-v^2)\sqrt{c^2-v^2}}\\
&=-\frac{\pi s}{c}
+4s^2\int_0^{\pi/2}\frac{dt}{1-c^2\sin^2t}\\
&=-\frac{\pi s}{c}+2\pi s,
\end{aligned}
\tag{6}
\]
where the last integral equals \(\pi/(2s)\) by the tangent substitution. Since \(I(s)\to0\) as \(s\downarrow0\), integration gives
\[
I(s)=\pi\left(s^2+\sqrt{1-s^2}-1\right)=\pi c(1-c).
\tag{7}
\]
Inserting (7) into (4) yields \(P(\theta)=c/(2(1+c))\), as claimed.

**5. Monotonicity and boundaries.** Differentiating the explicit formula gives
\[
P'(\theta)=-\frac{\sin\theta}{2(1+\cos\theta)^2}<0.
\]
Taylor expansion yields both endpoint asymptotics. The equator itself is a great circle and the minimizing arc between almost every pair of equator points remains on it. Its surface-area-normalized distribution is not defined, so no continuity of the escape event under the degeneration can be inferred.

## Verification

A standalone standard-library Python checker, `verify_zone.py`, tests the independently parametrized great-circle integral against the closed expression at five distinct widths. It also samples independent surface-area-uniform pairs at three widths and determines the maximal absolute latitude of their entire minimizing arc by optimizing its vertical sinusoid, rather than by inspecting a finite set of points. The checker reports `SPHERICAL_ZONE_GEODESIC_ESCAPE_ANALYTIC_AND_DIRECT_SAMPLE_OK`. Numerical checks corroborate the normalization and event classification; the proof above, not sampling, establishes the exact identity for all \(0<\theta<\pi/2\).

## Relationship to prior work

Lassak's work on spherical widths and convex bodies supplies the standard shorter-great-circle convention and classical spherical-convexity context, but treats deterministic bodies rather than random pairwise geodesic escape. Bárány, Hug, Reitzner and Schneider provide the spherical Blaschke--Petkantschin identity used in (1), while their results concern random spherical polytopes in halfspheres. Gille treats isotropic Euclidean straight-chord lengths of a solid hemisphere; these are not intrinsic shortest arcs joining two surface-area-uniform points of a spherical zone. A related earlier exact formula for randomly sampled large spherical *caps* has different domains and conditional sampling laws and does not imply (4)--(7) by parameter substitution. The novelty claim is solely the complete zone escape law, its strict monotonicity and its singular thin-zone limit, not the pre-existing integration identity.

## Limitations

This exact formula is specific to the unit two-sphere and a symmetric equatorial band with uniform area sampling. We do not establish a law for off-center bands, general nonconvex spherical subsets, arbitrary point densities, or different ambient dimensions. Numerical agreement is not a formal external certification. Historical-priority uncertainty remains for unindexed integral-geometric literature or results using alternative terminology such as spherical annulus or belt.

## References

1. M. Lassak, *Width of spherical convex bodies*, Aequationes Mathematicae 89 (2015), 555--567. First online 2013-12-06. DOI: 10.1007/s00010-013-0237-3.
2. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1 (2015-05-18), especially Lemma 3.2.
3. W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24--28, DOI: 10.3844/jmssp.2005.24.28.
