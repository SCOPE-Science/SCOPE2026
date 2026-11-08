# Dilogarithmic mean area of random fixed-latitude spherical triangles

## Finding

Let \(0<\theta<\pi\), \(\theta\ne\pi/2\). Choose three independent points uniformly by spherical arclength on the latitude circle of colatitude \(\theta\) of the unit sphere. Join them by their unique shortest great-circle arcs, obtaining the geodesically convex spherical triangle with area \(\mathcal A_\theta\in(0,2\pi)\) almost surely. Put
\[
c=|\cos\theta|,\qquad r=\frac{1-c}{1+c},\qquad \operatorname{Li}_2(z)=\sum_{k=1}^{\infty}\frac{z^k}{k^2}.
\]
Then the **entire mean-area law** is
\[
\boxed{\mathbb E\mathcal A_\theta=-\frac6\pi\operatorname{Li}_2(-r)
=\frac6\pi\int_0^r\frac{\log(1+t)}t\,dt.}
\]
It is strictly increasing in the latitude circle's angular distance from its nearest pole. Its range is precisely \((0,\pi/2)\); hence the mean geodesic area uniquely determines \(|\cos\theta|\), with north–south reflection the only ambiguity. The limiting regimes are
\[
\mathbb E\mathcal A_\theta=\frac{3\theta^2}{2\pi}+O(\theta^4)\quad(\theta\downarrow0),\qquad
\mathbb E\mathcal A_\theta=\frac\pi2-\frac{12\log2}{\pi}|\cos\theta|+O(\cos^2\theta)\quad(\theta\to\pi/2,\ \theta\ne\pi/2).
\]
The same polar expansion holds replacing \(\theta\) by \(\pi-\theta\) near the south pole.

## Assumptions and scope

Points have independent uniformly distributed longitudes \(U_1,U_2,U_3\in[0,2\pi)\); because the latitude circle has constant speed this is uniform arclength. The sampling circle is neither a pole (which has zero length) nor the equator (where the three sampled points lie on one great circle, so the nondegenerate spherical triangle convention fails). For \(0<|\cos\theta|<1\), all three points lie strictly inside one open hemisphere and uniquely determine a geodesically convex triangle bounded by arcs of length less than \(\pi\). Every expectation is with respect to these three longitudes, and area is intrinsic unit-sphere area (solid angle in steradians), not Euclidean chordal area.

## Proof

By reflection across the equator we may assume \(c=\cos\theta\in(0,1)\), and put \(s=\sin\theta\). Rotation allows us to fix the first vertex at \(p_0=(s,0,c)\); another sampled vertex is \(p_u=(s\cos u,s\sin u,c)\) with \(u\) uniform on \([0,2\pi)\). In the tangent plane at \(p_0\), take orthonormal east and poleward directions
\[
e=(0,1,0),\qquad n=(-c,0,s).
\]
The initial velocity of the shortest geodesic toward \(p_u\) is a positive multiple of \(p_u-(p_0\cdot p_u)p_0\). Its coordinates in this tangent frame are \((s\sin u,cs(1-\cos u))\). Hence its bearing from the poleward direction, in \((-\pi/2,\pi/2)\), is
\[
\varphi(u)=\operatorname{atan2}\big(\sin u,c(1-\cos u)\big),\quad
\varphi'(u)=-\frac{c}{2(\cos^2(u/2)+c^2\sin^2(u/2))},\quad 0<u<2\pi.
\]
In particular, \(\varphi\) decreases continuously from \(\pi/2\) to \(-\pi/2\). Conditional on the first vertex, the two other longitudes \(U,V\) are independent and uniform, and the intrinsic angle at the first vertex equals \(|\varphi(U)-\varphi(V)|\) (a number in \((0,\pi)\)). Thus all three angles have the same expectation \(I\). By Girard's spherical-excess identity, \(\mathbb E\mathcal A_\theta=3I-\pi\).

Let \(L=2\pi\) and set
\[
F_c(t)=-2\varphi'(t)=\frac{c}{\cos^2(t/2)+c^2\sin^2(t/2)}.
\]
Since \(\varphi\) decreases, Fubini's theorem on the interval between two independent uniform longitudes gives the **exact angle integral**
\[
I=\frac{2}{L^2}\int_0^L t(L-t)(-\varphi'(t))\,dt
=\frac1{L^2}\int_0^L t(L-t)F_c(t)\,dt.
\]
Put \(r=(1-c)/(1+c)\in(0,1)\). Direct algebra gives the Poisson kernel identity
\[
F_c(t)=\frac{1-r^2}{1+2r\cos t+r^2}
=1+2\sum_{k=1}^\infty(-r)^k\cos(kt).
\]
The series is absolutely uniformly convergent for every fixed \(r<1\), so termwise integration is justified. The integrals are
\[
\int_0^{L}t(L-t)\,dt=\frac{L^3}{6},\qquad
\int_0^L t(L-t)\cos(kt)\,dt=-\frac{2L}{k^2}\quad(k\ge1).
\]
Consequently,
\[
I=\frac\pi3-\frac2\pi\sum_{k=1}^\infty\frac{(-r)^k}{k^2}
=\frac\pi3-\frac2\pi\operatorname{Li}_2(-r).
\]
Girard's identity yields the boxed law exactly.

For \(0<r<1\), differentiation of the integral form gives
\[
\frac{d}{dr}\mathbb E\mathcal A_\theta=\frac6\pi\frac{\log(1+r)}r>0.
\]
Meanwhile \(r\) decreases strictly with \(c\), proving strict invertibility up to pole reflection. The endpoint limits follow from \(\operatorname{Li}_2(0)=0\), \(\operatorname{Li}_2(-1)=-\pi^2/12\), and Taylor expansion. Near a pole \(r=\theta^2/4+O(\theta^4)\); near the equator \(1-r=2c+O(c^2)\), producing the stated sharp coefficients. No asserted identity uses an equatorial degenerate triangle.

## Verification

The accompanying `checker.py` uses independent solid-angle and Girard-angle formulas on the same sampled triples. At four nondegenerate colatitudes it compares empirical means against the dilogarithm expression and verifies agreement between the two geometric area formulas pointwise. The checker includes a near-equatorial test and the exact endpoint identity \(\operatorname{Li}_2(-1)=-\pi^2/12\). These tests are numerical corroboration; the preceding Fourier calculation proves the infinite-series statement.

## Relationship to prior work

Finch and Jones, *Random Spherical Triangles* (arXiv:1009.5329; first posted 2010-09-27), study triangles from three points independent and uniform on the **entire sphere**, including their area distribution, rather than arclength sampling on one fixed latitude circle. Le, *Random spherical triangles II: Shape densities* (1989), studies shape density for three points **area-uniform within a spherical cap**, not the latitude-circle boundary law stated here. The full Le article was unavailable for inspection, leaving a historical-priority risk. The spherical-excess identity itself is classical and is not claimed as new. The contribution asserted here is the parameter-dependent closed dilogarithm mean, its exact strict inverse, and its polar and equatorial asymptotics for the fixed-latitude boundary model.

## Limitations

The formula does not describe the full area distribution, variance, or sampling from an entire spherical cap. At the equator the nondegenerate triangle convention fails; the displayed equatorial value \(\pi/2\) is a **one-sided limit**, not a claim about the exactly degenerate equatorial model. The formula assumes independent uniform arclength points and the unit sphere. It is derived without numerical approximation, but priority beyond the inspected sources remains subject to independent literature verification.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, initial public version 2010-09-27; https://arxiv.org/abs/1009.5329.
2. H. Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* **21** (1989), 581–594, doi:10.1017/S0001867800018826; https://doi.org/10.1017/S0001867800018826.
3. *Spherical Excess*, MathWorld, https://mathworld.wolfram.com/SphericalExcess.html (classical Girard identity).
