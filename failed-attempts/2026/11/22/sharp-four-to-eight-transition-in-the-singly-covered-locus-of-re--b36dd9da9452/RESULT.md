# Sharp four-to-eight transition in the singly covered locus of rectangular Thales disks

## Finding
Let \(t\ge1\), let \(P_t=[-t,t]\times[-1,1]\subset\mathbb R^2\), and for each of its four vertices \(v\) let \(D_v\) be the closed Euclidean disk whose diameter is the segment from the origin to \(v\). Define the **singly covered interior**
\[
U_t=\{z\in\operatorname{int}(P_t):\#\{v:z\in D_v\}=1\},\qquad F(t)=\frac{\operatorname{area}(U_t)}{4t}.
\]
All four disks together cover \(P_t\). The region \(U_t\) has exactly **four connected components** if \(1\le t<2\sqrt2\), and exactly **eight connected components** if \(t\ge2\sqrt2\). Thus the critical aspect ratio is attained at the topology-changing parameter itself, not strictly beyond it.

The area fraction has the exact profile
\[
F(t)=\frac32-\frac\pi8\left(t+\frac1t\right)+\begin{cases}
0,&1\le t\le 2\sqrt2,\\[3pt]
\displaystyle\frac{G_t(\theta_+)-G_t(\theta_-)}{2t},&t>2\sqrt2,
\end{cases}
\]
where for \(t>2\sqrt2\),
\[
u_\pm=\frac{t\pm\sqrt{t^2-8}}4,\qquad
\theta_\pm=\arctan u_\pm,
\]
\[
G_t(\theta)=\frac{t^2+1}{2}\theta+\frac{t^2-1}{4}\sin(2\theta)-t\sin^2\theta+\cot\theta.
\]
The correction is strictly positive for \(t>2\sqrt2\). At the transition \(t_0=2\sqrt2\), it has the sharp nonanalytic onset
\[
F(t)-\left[\frac32-\frac\pi8\left(t+\frac1t\right)\right]
=\frac{2\,2^{1/4}}9(t-t_0)^{3/2}+O((t-t_0)^2)
\quad(t\downarrow t_0,\ t>t_0).
\]
In particular, \(F\) is continuously differentiable but is not twice differentiable at \(t_0\). Its square value, \(F(1)=\frac32-\frac\pi4\), was previously obtainable from the exact disk-depth spectrum of regular polygons; the new assertions concern the entire non-square rectangle family and its critical phase.

## Assumptions and scope
The geometry is **Euclidean** and the four disks have their actual origin-to-corner segments as diameters, not adjustable radii. \(t\) is the ratio of the longer to the shorter side; uniform scaling does not alter \(F\). Area means ordinary planar Lebesgue measure; all disk boundaries and rectangle edges have zero area. For topology we work in the open interior, so a point lying on the boundary of a second disk is *not* singly covered. All assertions hold for every real \(t\ge1\), including the critical value.

## Proof
**1. The exact incidence condition.** For \(z=(x,y)\), the disk condition is
\[
z\in D_{(\sigma t,\tau)}\iff x^2+y^2\le \sigma tx+\tau y,\qquad \sigma,\tau\in\{-1,1\}.
\]
In the first open quadrant \(x>0,y>0\), the largest right-hand side is \(tx+y\); the second largest is \(|tx-y|\). The largest disk always covers the first-quadrant part of \(P_t\), since \(x^2\le tx\) and \(y^2\le y\) for \(0<x<t\), \(0<y<1\). The point is singly covered precisely when
\[
|tx-y|<x^2+y^2<tx+y.
\]
The other quadrants follow by reflection; no point on a coordinate axis is singly covered because the relevant largest vertex projections tie. Consequently distinct open quadrants can never be connected through \(U_t\).

**2. Radial intervals and critical quadratic.** Put \(x=r\cos\theta\), \(y=r\sin\theta\) for \(0<\theta<\pi/2\). The first-quadrant rectangle has radial endpoint
\[
R_t(\theta)=\min\left\{\frac{t}{\cos\theta},\frac1{\sin\theta}\right\},
\]
and the one-coverage radial interval is
\[
|t\cos\theta-\sin\theta|<r<R_t(\theta).
\]
For \(0<\theta\le\arctan(1/t)\), the interval is nonempty by \(t/\cos\theta>t\cos\theta-\sin\theta\). For \(\arctan t\le\theta<\pi/2\), it is nonempty by \(1/\sin\theta>\sin\theta-t\cos\theta\). In the intermediate angular interval, with \(u=\tan\theta\), nonemptiness is exactly
\[
2u^2-tu+1>0.
\]
Its discriminant is \(t^2-8\). When \(t<2\sqrt2\) the inequality holds for every angular direction; when \(t=2\sqrt2\), precisely the ray \(u=1/\sqrt2\) has no singly covered point; when \(t>2\sqrt2\), the closed forbidden angular interval is \([\arctan u_-,\arctan u_+]\). Both roots satisfy \(1/t<u_-<u_+<t\). Each connected angular interval supports a nonempty *continuous open radial interval*, so the first quadrant has one component below the transition and two at or above it. Reflecting into four quadrants proves the component counts. No boundary or axis can reconnect them.

**3. Area profile.** The area in the first quadrant equals
\[
\frac12\int_0^{\pi/2}
\left[R_t(\theta)^2-(t\cos\theta-\sin\theta)^2\right]_+\,d\theta.
\]
The rectangle radial-area identity and a direct trigonometric integral give
\[
\frac12\int_0^{\pi/2} R_t(\theta)^2\,d\theta=t,
\qquad
\int_0^{\pi/2}(t\cos\theta-\sin\theta)^2\,d\theta
=\frac\pi4(t^2+1)-t.
\]
Before the transition the integrand is nonnegative everywhere. After the transition its negative part lies *only* on \((\theta_-,\theta_+)\). On this interval \(R_t=1/\sin\theta\), and
\[
\frac{d}{d\theta}G_t(\theta)=
(t\cos\theta-\sin\theta)^2-\frac1{\sin^2\theta}.
\]
Adding back the omitted negative part and dividing the first-quadrant area by \(t\) establishes the exact formula for \(F(t)\).

**4. Sharp onset.** With \(u=\tan\theta\), the correction integrand, including its angular Jacobian, is
\[
q_t(u)=\frac{(tu+1)(tu-2u^2-1)}{u^2(1+u^2)^2},\qquad
F(t)-F_0(t)=\frac1{2t}\int_{u_-}^{u_+}q_t(u)\,du,
\]
where \(F_0(t)=\frac32-\frac\pi8(t+t^{-1})\) and \(t>t_0\). At \(t_0=2\sqrt2\), \(u_0=1/\sqrt2\), direct differentiation yields
\[
q_t(u)=\frac{4\sqrt2}{3}(t-t_0)-\frac{16}{3}(u-u_0)^2
+O\bigl((t-t_0)|u-u_0|+|u-u_0|^3+(t-t_0)^2\bigr).
\]
The integration interval has center \(u_0+O(t-t_0)\) and half-width \(\frac{2^{1/4}}2\sqrt{t-t_0}+O((t-t_0)^{3/2})\). Integrating the displayed quadratic cap and dividing by \(2t_0\) gives \(\frac{2\,2^{1/4}}9(t-t_0)^{3/2}\). The Taylor remainder contributes \(O((t-t_0)^2)\), proving the claimed onset and its differentiability consequences.

## Verification
The included standard-library Python 3 script `verify.py` recomputes the area by piecewise polar Simpson quadrature and, independently, directly counts disk membership on a Cartesian grid without using the radial incidence reduction. It also checks the rational identity for \(q_t\) with exact fractions, the discriminant/root inequalities, and the cusp coefficient. Executing `python3 verify.py` from the package directory printed `PASS` for ten tested aspect ratios. These finite checks support but do not substitute for the proof covering every real \(t\ge1\).

## Relationship to prior work
Pavlík, *Thales's theorem in higher dimensions* (arXiv:2611.14277v1, November 2026), Theorem 5.1 proves existence of the vertex-to-point diameter-ball covering for every convex polytope; Corollary 5.3 constructs power-diagram cells. Those facts imply neither the area nor the number of connected components of the region covered by exactly one disk. A published *Exact multiplicity spectrum of vertex-to-center diameter disks of regular polygons* (November 2026) determines all multiplicity areas for **regular** polygons; it includes the square \(t=1\), explicitly excluded from the novelty claim by itself, but its hypotheses do not cover any rectangle with \(t>1\) or the sharp eccentricity transition. The separate *Exact diameter-disk depth of a regular polygon* gives a mean and a circle limit for the same regular-only family, not the rectangular bifurcation. Huemer and Pérez-Lantero (2014) and Herrera and Pérez-Lantero (2018) study disks built on **polygon sides** instead of center-to-vertex segments; their intersection graphs do not imply this one-coverage phase diagram.

## Limitations
The result addresses axis-aligned Euclidean rectangles with their center fixed as the common endpoint; rotation and scaling give equivalent copies. It does not optimize the placement of the common endpoint, cover other parallelograms, or determine a complete overlap-multiplicity distribution. Area integration and topology use the open rectangle interior, so isolated boundary coincidences are irrelevant. Literature searches do not certify historical priority. Independent mathematical audit has not been performed.

## References
- J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, first submitted 2026-11-10, https://arxiv.org/html/2611.14277v1, particularly Section 5 and Corollary 5.3.
- *Exact multiplicity spectrum of vertex-to-center diameter disks of regular polygons*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-multiplicity-spectrum-of-vertex-to-center-diameter-disks-o--1b3f060ecc28.
- *Exact diameter-disk depth of a regular polygon: mean redundancy and a quantitative limit law*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-diameter-disk-depth-of-a-regular-polygon-mean-redundancy-a--a85d54c61c1a.
- C. Huemer and P. Pérez-Lantero, *The intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1410.4126 (2014), https://arxiv.org/abs/1410.4126.
- L. H. Herrera and P. Pérez-Lantero, *On the intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1805.10847 (2018), https://arxiv.org/abs/1805.10847.
