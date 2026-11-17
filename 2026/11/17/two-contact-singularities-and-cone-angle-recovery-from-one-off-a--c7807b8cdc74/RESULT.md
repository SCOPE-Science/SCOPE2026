# Two contact singularities and cone-angle recovery from one off-apex ball-area profile

## Finding
Let \(C_\alpha\) be the complete two-dimensional flat metric cone with total angle \(0<\alpha<\pi\). Fix a point \(p\ne o\), where \(o\) is the apex, at intrinsic distance \(s=d(p,o)>0\). Put \(\beta=\alpha/2\) and \(d=s\sin\beta\). Define the intrinsic ball-area profile \(V(r)=\operatorname{area}(B_r(p))\), for every real \(r\ge0\), using the two-dimensional intrinsic area measure. Then
\[
V(r)=\begin{cases}
\pi r^2,&0\le r\le d,\\[2pt]
\pi r^2-2\left[r^2\arccos\frac d r-d\sqrt{r^2-d^2}\right],&d<r<s,\\[2pt]
\beta r^2+\frac{s^2}{2}\sin(2\beta)
+d\sqrt{r^2-d^2}+r^2\arcsin\frac d r,&r\ge s.
\end{cases}
\]
There are exactly two positive radii where \(V\) is not real analytic: \(r=d\) and \(r=s\). At the first, the sharp onset is
\[
\pi(d+\varepsilon)^2-V(d+\varepsilon)
=\frac83\sqrt{2d}\,\varepsilon^{3/2}+O_d(\varepsilon^{5/2})
\quad(\varepsilon\downarrow0).
\]
At the second, \(V\) is continuously differentiable, with exact jump
\[
\boxed{V''(s+)-V''(s-)=2\tan\beta>0.}
\]
Consequently the intrinsic area profile of balls centered at a **single nonapical point** recovers the cone angle and the point's distance from the apex in either of two ways: the two contact radii give \(s\) and \(\alpha=2\arcsin(d/s)\); or the *location* \(s\) and *size* \(J\) of the unique finite jump in \(V''\) give \(\alpha=2\arctan(J/2)\). In either description, the first contact is a fractional-power singularity and the second is a finite curvature jump.

## Assumptions and scope
The complete flat cone is the length-metric quotient of the polar sector \(\{(u,\theta):u\ge0,\ -\beta\le\theta\le\beta\}\), with the two boundary rays identified isometrically and the Euclidean metric off the origin. All distances are **intrinsic geodesic distances** in this quotient; the area is its intrinsic Euclidean area, not area of a three-dimensional cone's solid or planar footprint. The center is any point with radial coordinate \(s>0\); rotational symmetry permits placing it on \(\theta=0\). The cone-angle restriction \(0<\alpha<\pi\) ensures \(0<d<s\), so the contact radii are distinct; no statement is made at the merging endpoint \(\alpha=\pi\) or for larger cone angles. The area profile is over all finite radii and is not normalized to finite total area (the cone has infinite area).

## Proof
**1. Intrinsic distance and convex development.** Every point of \(C_\alpha\) has a representative at angular coordinate \(\theta\in[-\beta,\beta]\). The shorter angular separation from the representative of \(p\) is \(|\theta|\le\beta<\pi/2\). A radial sector of angle less than \(\pi\) is convex, so unfolding along the shorter angular arc supplies a straight geodesic of length \(\sqrt{s^2+u^2-2su\cos\theta}\), contained in the sector. It is minimizing: a competing path with winding is at least as long, by the standard metric-cone distance formula, or directly by unfolding and minimizing angular separation up to \(\pi\). Hence \(B_r(p)\) develops exactly into the intersection of the ordinary Euclidean disk of radius \(r\) centered at \((s,0)\) with the convex sector bounded by the rays at angles \(\pm\beta\). The seam has zero area. In particular, \(V(r)\) is exactly this planar intersection area.

**2. The Euclidean-ball phase.** The distance from \((s,0)\) to either sector boundary line is \(d=s\sin\beta\). For \(r\le d\) the whole disk lies in the sector, proving \(V(r)=\pi r^2\) (equality at tangency is harmless). For \(d<r<s\) the disk protrudes past both boundary lines. Because the disk is entirely in the half-plane of positive axial coordinate, the two protruding circular caps are disjoint. Each has area \(r^2\arccos(d/r)-d\sqrt{r^2-d^2}\), proving the middle branch.

**3. The apex-entering phase.** For \(r\ge s\) the disk contains the apex, so along each direction \(|\theta|\le\beta\) its intersection with the positive radial ray is precisely \(0\le u\le u_+(\theta)\), where
\[
u_+(\theta)=s\cos\theta+\sqrt{r^2-s^2\sin^2\theta}.
\]
Integrating the polar area element gives
\[
V(r)=\frac12\int_{-\beta}^{\beta}u_+(\theta)^2\,d\theta
=\beta r^2+\frac{s^2}{2}\sin(2\beta)
+2s\int_0^\beta\cos\theta\sqrt{r^2-s^2\sin^2\theta}\,d\theta.
\]
The substitution \(z=s\sin\theta\) evaluates the remaining integral to \(d\sqrt{r^2-d^2}+r^2\arcsin(d/r)\), proving the last branch. Direct substitution checks agreement at the branch endpoints.

**4. Sharp first and second contact singularities.** The circular-segment expansion at the first contact is
\[
r^2\arccos(d/r)-d\sqrt{r^2-d^2}
=\frac43\sqrt{2d}\,(r-d)^{3/2}+O_d((r-d)^{5/2}).
\]
Multiplication by two establishes the claimed onset. In particular, the first derivative is continuous there but the second derivative diverges negatively on approach from above; no other earlier contact is possible. For \(d<r<s\), differentiating the middle branch gives
\[
V'(r)=2\pi r-4r\arccos(d/r),\qquad
V''(r)=2\pi-4\arccos(d/r)-\frac{4d}{\sqrt{r^2-d^2}}.
\]
For \(r>s\), the last branch instead gives
\[
V'(r)=2\beta r+2r\arcsin(d/r),\qquad
V''(r)=2\beta+2\arcsin(d/r)-\frac{2d}{\sqrt{r^2-d^2}}.
\]
As \(r\to s\), the identities \(\arcsin(d/s)=\beta\) and \(\arccos(d/s)=\pi/2-\beta\) give matching one-sided first derivatives \(4\beta s\). The respective second-derivative limits are \(4\beta-4\tan\beta\) and \(4\beta-2\tan\beta\); their positive jump is exactly \(2\tan\beta\). Each branch is real analytic on its open interval, and the first and second singularities are genuine, so the two radii are the complete nonanalytic set in \((0,\infty)\).

**5. Reconstruction and exact scope.** Because \(d/s=\sin\beta\) and \(\beta\in(0,\pi/2)\), the first and second nonanalytic radii alone uniquely recover \((s,\alpha)\) through the stated arcsine formula. Equivalently, the **unique finite positive jump** in the second derivative occurs at \(s\) and equals \(J=2\tan\beta\), giving the arctangent formula independently. Either reconstruction is exact from the full intrinsic ball-area profile and does not depend on an ambient embedding of the cone. This proves the theorem.

## Verification
The accompanying standalone `checker.py` reconstructs the area by an independent polar midpoint quadrature at five distinct cone angles and nine radii per angle, and compares it with the closed forms. It checks the first-contact \(3/2\) coefficient, the second-contact overlap coefficient \(\tan\beta\), and the angle inverse, in 70 finite checks. Execute `python3 checker.py` using only Python 3's standard library; its completion marker is `OFF_APEX_CONE_BALL_CHECKS_OK 70`. These numerical tests validate selected inputs, not universal cases: the analytic argument in the preceding section proves the universal statements and exact coefficients.

## Relationship to prior work
Izmestiev (2014) gives the framework of Euclidean cone metrics, area and isoperimetric comparison, not a complete off-apex metric-ball volume and its two separate singular contacts. Cabré, Ros-Oton and Serra (2012) solve an isoperimetric problem **inside** convex Euclidean cones, centered at the cone origin and without gluing boundary rays. Their theorem concerns minimizing weighted perimeter for fixed volume, not this intrinsic point-centered ball-growth inverse problem.

The 2010 exposition *Cone Geodesics* by Slavík explains developability and local geodesic construction, and those are classical ingredients rather than asserted novelties. An accessible later result, *Exact small-distance law on flat cone surfaces and Euclidean orbifold signature recovery*, supplies a **general integral representation** of cone-ball volume deficits when proving an area-averaged two-point law. This is strong prior coverage of the underlying distance-integral object, and the present result does **not** claim the basic representation or the metric-cone distance formula as new. Its separately assessed contribution is the closed all-radius two-contact classification, the sharp fractional onset and finite second-derivative jump, and reconstruction of an off-apex point's radial position and cone angle from these finite-radius features. The explicit computation of those features requires the branch switch and angular-sector geometry established above. Historical priority of this contact-based inverse statement remains provisional.

## Limitations
The results apply only to a complete flat **single-apex** cone of total angle strictly below \(\pi\), and to a nonapical center. They do not assert analogous formulas when cone angle is at least \(\pi\), for bounded cones with a rim, multiple singularities, smooth variable curvature, noisy ball-area measurements, or points on the apex. In particular, the two singularities merge at the excluded half-plane-cone endpoint. The inverse statements concern exact geometric profiles, not stability under measurement errors. A general prior cone-ball deficit integral may render some elementary formula components implicit, and unindexed earlier literature might include the contact thresholds: historical novelty therefore still requires independent verification.

## References
1. X. Cabré, X. Ros-Oton and J. Serra, *Euclidean balls solve some isoperimetric problems with nonradial weights*, arXiv:1210.1788v1, first posted 2012-10-05, https://arxiv.org/abs/1210.1788 .
2. I. Izmestiev, *A simple proof of an isoperimetric inequality for euclidean and hyperbolic cone-surfaces*, arXiv:1409.7681v1, first posted 2014-09-26, https://arxiv.org/abs/1409.7681 .
3. A. Slavík, *Cone Geodesics*, Wolfram Demonstrations Project (2010), https://demonstrations.wolfram.com/ConeGeodesics/ .
4. *Exact small-distance law on flat cone surfaces and Euclidean orbifold signature recovery*, mathematical research record (2026-11-08), publicly accessible full-text result. Its exact cone-ball volume-deficit integral is a closest known comparison; the present contact classification was not stated there.
