# Sharp geodesic-convexity failure probability for uniform pairs in spherical caps

## Finding
For the unit sphere \(S^2\), choose two independent points \(X,Y\) uniformly with respect to surface area on the geodesic cap \(C_\rho\) of radius \(\rho\). Let \(E_\rho\) denote the event that the unique minimizing great-circle arc \([X,Y]_{\min}\) exits that cap. Then
\[
\Pr(E_\rho)=\begin{cases}
0,&0<\rho\le\pi/2,\\
\frac12\,t(1-t)^2,&\pi/2<\rho<\pi,\quad t=\tan\frac{\pi-\rho}{2},\\
0,&\rho=\pi.
\end{cases}
\]
The probability is uniquely maximized at \(\rho_*=\pi-2\arctan(1/3)\) and its maximum equals \(2/27\). Its one-sided endpoint laws are
\[
\Pr(E_{\pi/2+\varepsilon})\sim\varepsilon^2/2,
\qquad \Pr(E_{\pi-\varepsilon})\sim\varepsilon/4.
\]

## Assumptions and scope
The sphere has radius one and its standard Riemannian surface-area measure. A geodesic cap is the closed set \(C_\rho=\{x\in S^2:d_{S^2}(x,N)\le\rho}\), where \(N\) is any fixed pole. The sampling law is area measure restricted to \(C_\rho\), divided by its total area. Coincident or antipodal sampled points have probability zero and may be discarded. The relevant arc is the globally minimizing spherical geodesic of length strictly less than \(\pi\), not an arbitrary great-circle arc. In particular, \(\rho>\pi/2\) describes a large cap that is not geodesically convex, despite occupying more than a hemisphere. All probabilities are for two independent sampled points, not for boundary-uniform samples or central-plane sampling.

## Proof
**Convex regime.** A cap of radius at most \(\pi/2\) is the intersection of the sphere with a convex Euclidean cone, and the normalized positive great-circle combination of any two of its nonantipodal points stays in it. Thus the shorter geodesic arc remains inside.

**Excluded small cap.** Fix \(\pi/2<\rho<\pi\), set \(\beta=\pi-\rho\in(0,\pi/2)\), \(s=\sin\beta\), and \(c=\cos\beta\). The complement of \(C_\rho\) is the open cap of angular radius \(\beta\) around the opposite south pole \(S\). The fraction of full-sphere area belonging to \(C_\rho\) is \(q=(1+c)/2\). Write \(E\) for the event that two full-sphere area-uniform points lie in \(C_\rho\) but their short geodesic intersects the excluded cap. The desired conditional probability is \(\Pr(E)/q^2\).

**Spherical two-point disintegration.** Let \(\sigma\) denote spherical area. For a unit normal \(n\in S^2\), choose any unit-speed arclength parametrization \(\gamma_n(u)\), \(0\le u<2\pi\), of the great circle perpendicular to \(n\). For every nonnegative measurable symmetric pair function \(F\), the spherical Blaschke–Petkantschin change of variables gives
\[
\int_{S^2\times S^2}F(x,y)\,d\sigma(x)d\sigma(y)
=\frac12\int_{S^2}\int_0^{2\pi}\int_0^{2\pi}
F(\gamma_n(u),\gamma_n(v))\,|\sin(u-v)|\,du\,dv\,d\sigma(n).
\]
The factor \(|\sin(u-v)|\) is the absolute Jacobian for the two endpoint parameters and the normal; the two oriented normal choices contribute the factor \(1/2\). One may check the normalization by setting \(F\equiv1\): both sides are \(16\pi^2\). The formula is invariant under a change of origin of the circle parameter, and the antipodal exceptional set has zero area.

**Conditional circle integral.** Write \(z=|n\cdot S|\), which is uniform on \([0,1]\) under normalized area measure on the normal sphere. The great circle meets the excluded cap only when \(0\le z<s\). Its intersection is a single open arc of length \(2h(z)\), where
\[
 h(z)=\arccos\left(\frac{c}{\sqrt{1-z^2}}\right),\quad0\le z\le s;
\qquad h(s)=0.
\]
For endpoints outside this excluded arc, their minimizing geodesic crosses it precisely when the endpoints lie on opposing sides of the arc at nonnegative offsets \(a,b\) with \(2h+a+b<\pi\). Such configurations have two orderings, and the integral of \(|\sin(u-v)|\) on those configurations is
\[
I(h)=2\int_{a,b\ge0\atop a+b<\pi-2h}
\sin(2h+a+b)\,da\,db
=2\int_0^{\pi-2h}w\sin(2h+w)\,dw
=2(\pi-2h-\sin2h).
\]
Since the normal-sphere area is \(4\pi\) and the pair area on the full sphere is \((4\pi)^2\), disintegration yields
\[
\Pr(E)=\frac{1}{8\pi}\int_0^s I(h(z))\,dz
=\frac{1}{4\pi}\int_0^s[\pi-2h(z)-\sin 2h(z)]\,dz.
\]
The integral limits follow from the geometry of the excluded cap, not an approximation.

**Explicit quadrature.** By integration by parts, using
\[
h'(z)=-\frac{cz}{(1-z^2)\sqrt{s^2-z^2}},
\]
one obtains
\[
\int_0^s h(z)\,dz
=c\int_0^s\frac{z^2}{(1-z^2)\sqrt{s^2-z^2}}\,dz
=\frac\pi2(1-c).
\]
Also \(\sin(2h(z))=2c\sqrt{s^2-z^2}/(1-z^2)\), so the substitution \(z=s\sin\theta\) gives
\[
\int_0^s\sin(2h(z))\,dz
=2cs^2\int_0^{\pi/2}\frac{\cos^2\theta}{1-s^2\sin^2\theta}\,d\theta
=\pi c(1-c).
\]
Here both evaluations use the elementary integral \(\int_0^{\pi/2}(1-s^2\sin^2\theta)^{-1}d\theta=\pi/(2c)\). Consequently
\[
\Pr(E)=\frac1{4\pi}[\pi s-\pi(1-c)-\pi c(1-c)]
=\frac{s-(1-c)(1+c)}4=\frac{s-s^2}4.
\]
Divide by \(q^2=(1+c)^2/4\) to get
\[
\Pr(E_\rho)=\frac{s-s^2}{(1+c)^2}.
\]
Using \(t=\tan(\beta/2)\), \(s=2t/(1+t^2)\), and \(c=(1-t^2)/(1+t^2)\), yields \(\Pr(E_\rho)=\tfrac12 t(1-t)^2\).

**Sharp maximizer and endpoints.** The parameter \(t\) ranges bijectively over \((0,1)\) as \(\rho\) ranges over \((\pi/2,\pi)\). Differentiating the cubic gives \(\tfrac12(1-t)(1-3t)\): the only interior maximum is at \(t=1/3\), where its value is \(2/27\). Both endpoints give zero. For \(\rho\downarrow\pi/2\), \(1-t\sim\rho-\pi/2\); for \(\rho\uparrow\pi\), \(t\sim(\pi-\rho)/2\). The asymptotic laws follow. The cap at \(\rho=\pi\) is the entire sphere and has zero failure probability.

## Verification
Execute the standard-library checker using `python3 check.py`. It independently evaluates the disintegration integral by numerical quadrature, directly samples area-uniform spherical point pairs, evaluates the true minimum latitude along each shortest arc, and compares six parameter values. It also verifies the sharp maximum at \(t=1/3\). The recorded successful message is `SPHERICAL_CAP_SHARP_GEODESIC_NONCONVEXITY_OK`. Simulation and quadrature are corroborations, not substitutes for the analytic proof.

## Relationship to prior work
Santaló's 1946 spherical convexity paper studies diameter/inradius and spherical Jung-type inequalities; Lassak's 2013 publicly available work (journal volume dated 2015) develops spherical widths, lunes, and convex/reduced bodies. Neither inspected article derives a probability of minimizing-arc escape for area-uniform pairs from a **large** spherical cap or a sharp worst-case cap radius. The classical invariant disintegration is used here as an integration method, not claimed as a new identity. The qualitative loss of geodesic convexity beyond a hemisphere is classical; the quantitative normalized failure law and unique sharp maximizer are the claim. Relevant earlier studies of random spherical triangles involve three-point shape distributions and do not directly cover this two-point event.

## Limitations
No claim is made for spherical dimensions other than two, nonuniform point distributions, boundary-only sampling, or arbitrary domains. Historical priority cannot be established conclusively by finite literature searches. The original geometric-probability literature could contain an unindexed equivalent calculation; the exact theorem needs independent historical and mathematical review before publication.

## References
1. L. A. Santaló, “Convex Regions on the n-Dimensional Spherical Surface,” *Annals of Mathematics* **47** (1946), 448–459; DOI `10.2307/1969084`.
2. M. Lassak, “Width of spherical convex bodies,” first published online 2013-12-06, *Aequationes Mathematicae* **89** (2015), 555–567; DOI `10.1007/s00010-013-0237-3`. Primary classification 52A55.
3. H. Le, “Random spherical triangles II: Shape densities,” *Journal of Applied Probability* (1989); available abstract concerns random spherical triangle shapes, not the stated two-point probability law.
