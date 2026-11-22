# The elliptic random-width law and logarithmic polar localization of the Steinmetz bicylinder

## Finding
For the *Steinmetz bicylinder*, the intersection of two equal-radius orthogonal circular cylinders, the complete isotropic random-caliper-width law is an explicit complete elliptic integral. Its density has a logarithmic divergence at its minimum, unlike a typical isolated smooth extremum. The same logarithm forces a uniform law for the scale at which extreme viewing directions approach the two intersecting minimizing great circles.

Write \(\mathbf K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\) for the complete elliptic integral of the first kind with **modulus** \(k\).

For independent Haar-uniform \(U\in S^2\), let \(W_r\) denote the width normal to \(U\). Its entire support is \([2r,2\sqrt2r]\), and its interior density is
\[
 f_{W_r}(w)=\frac{2}{\pi r}\mathbf K\left(\sqrt{\frac{8r^2}{w^2}-1}\right),\qquad 2r<w<2\sqrt2r.
\]
The CDF vanishes below \(2r\), equals one above \(2\sqrt2r\), and in between is the integral of this density from \(2r\) to \(w\). There are no endpoint atoms.

Writing \(\delta>0\) and letting \(\delta/r\downarrow0\) at fixed \(r>0\), the sharp endpoint laws are
\[
 \Pr(W_r<2r+\delta)=\frac{\delta}{\pi r}\left(\log\frac{8r}{\delta}+1\right)+O\!\left(\frac{\delta^2}{r^2}\log\frac r\delta\right),
\]
\[
 \Pr(W_r>2\sqrt2r-\delta)=\frac{\delta}{r}+O\!\left(\frac{\delta^2}{r^2}\right).
\]
The exact second moment is \(\mathbb E[W_r^2]=4r^2(1+4/(3\pi))\).

A marked conditional limit refines the lower tail. For \(S=2|U_xU_z|\), as \(s\downarrow0\), conditional on \(S<s\),
\[
 \left(\frac{\log|U_x|}{\log s},\operatorname{sgn}(U_y)\right)
 \ \Longrightarrow\ (V,\Sigma),
\]
where \(V\sim\mathrm{Unif}[0,1]\), \(\Sigma\) is a fair sign, and the two are independent. Consequently the conditional direction \(U\) converges weakly to \(\frac12\delta_{(0,1,0)}+\frac12\delta_{(0,-1,0)}\). This is a singular localization onto the intersections of the two great circles of minimizing directions, not uniform selection on either circle.

## Assumptions and scope
Fix any \(r>0\), and define the full-dimensional compact convex body
\[
 K_r=\{(x,y,z)\in\mathbb R^3:\ x^2+y^2\le r^2,\ y^2+z^2\le r^2\}.
\]
The viewing direction \(U=(U_x,U_y,U_z)\) is Haar-uniform on \(S^2\). Width means the distance between the two parallel support planes normal to \(U\), not the area of the orthogonal projection, a geodesic width, or a random chord length. No independence of Cartesian coordinates is assumed. All asymptotic constants are absolute after normalization by \(r\); logarithms are natural.

## Proof
**1. Support formula.** For any fixed \(-r\le y\le r\), the horizontal section of \(K_r\) is a square with independent coordinate bounds \(|x|,|z|\le\sqrt{r^2-y^2}\). Thus, for any \(u\in\mathbb R^3\),
\[
 h_{K_r}(u)=\max_{|y|\le r}\left(yu_y+(|u_x|+|u_z|)\sqrt{r^2-y^2}\right)
 =r\sqrt{u_y^2+(|u_x|+|u_z|)^2}.
\]
The last equality is Cauchy–Schwarz, attained by choosing the semicircle point proportional to \((u_y,|u_x|+|u_z|)\). Central symmetry implies \(W_r(U)=2h_{K_r}(U)\). For \(U\in S^2\),
\[
 W_r=2r\sqrt{1+2|U_xU_z|}.
\]
The product \(2|U_xU_z|\in[0,1]\), so the stated support is exact. Equality at its minimum occurs on the union of the great circles \(U_x=0\) and \(U_z=0\), crossing at \((0,\pm1,0)\); maxima occur at the four choices \(U_y=0\), \(|U_x|=|U_z|=1/\sqrt2\).

**2. Density by independent spherical factors.** A uniform direction may be represented as
\[
 U=(\sqrt{1-Y^2}\cos\Phi,\ Y,\sqrt{1-Y^2}\sin\Phi),
\]
where \(Y\sim\mathrm{Unif}[-1,1]\) and \(\Phi\sim\mathrm{Unif}[0,2\pi)\) are independent. Put \(A=1-Y^2\), \(B=|\sin2\Phi|\), \(S=AB\). Their densities on \((0,1)\) are
\[
 f_A(a)=\frac1{2\sqrt{1-a}},\qquad f_B(b)=\frac2{\pi\sqrt{1-b^2}}.
\]
Ordinary product-density integration therefore yields, for \(0<s<1\),
\[
 f_S(s)=\frac1\pi\int_s^1\frac{db}{\sqrt{b(b-s)(1-b)(1+b)}}.
\]
Set \(b=s/[1-(1-s)t^2]\). Direct simplification gives
\[
 f_S(s)=\frac2{\pi\sqrt{1+s}}\mathbf K\left(\sqrt{\frac{1-s}{1+s}}\right).
\]
Finally \(s=w^2/(4r^2)-1\), so \(ds/dw=w/(2r^2)\) and \(1+s=w^2/(4r^2)\). The Jacobian cancels the prefactor, giving exactly the claimed density, with elliptic modulus \(k=\sqrt{8r^2/w^2-1}\). Its total integral is one because it is a pushforward of a probability law; the endpoint sets are finite unions of measure-zero curves/points.

**3. Sharp endpoints and a moment.** For \(k\uparrow1\), the standard elliptic expansion is
\[
 \mathbf K(k)=\log\frac4{\sqrt{1-k^2}}+O\!\left((1-k^2)\log\frac1{1-k^2}\right).
\]
Applied to the density in step 2, this gives
\[
 f_S(s)=\frac1\pi\log\frac8s+O(s\log(1/s)),\qquad s\downarrow0.
\]
Integration from zero to \(s\) gives \(\Pr(S<s)=s(\log(8/s)+1)/\pi+O(s^2\log(1/s))\). Since \(S=(W_r/(2r))^2-1\), substitution of \(w=2r+\delta\) proves the lower-width formula. As \(s\uparrow1\), continuity of \(\mathbf K(0)=\pi/2\) gives \(f_S(1-)=1/\sqrt2\), hence \(f_{W_r}(2\sqrt2r-)=1/r\) and a smooth upper endpoint yielding the other tail. For the moment, the independent factors give \(\mathbb E[S]=\mathbb E[1-Y^2]\,\mathbb E|\sin2\Phi|=(2/3)(2/\pi)=4/(3\pi)\), completing the formula.

**4. Log-uniform conditional localization.** The joint law of \((U_x,U_z)\) on the open unit disk has density
\[
 g(x,z)=\frac{1}{2\pi\sqrt{1-x^2-z^2}}.
\]
Fix any \(0<a<b<1\). On the event \(s^b<|U_x|<s^a\) and \(2|U_xU_z|<s\), the coordinate bounds force both \(U_x,U_z\to0\) uniformly, and \(g(x,z)=(1+o(1))/(2\pi)\) uniformly. Integrating over the four sign quadrants,
\[
 \Pr\left(S<s,\ s^b<|U_x|<s^a\right)
 =\frac{s}{\pi}\int_{s^b}^{s^a}\frac{dx}{x}(1+o(1))
 =\frac{s\log(1/s)}{\pi}(b-a)(1+o(1)).
\]
Divide by \(\Pr(S<s)\sim (s/\pi)\log(1/s)\) from step 3. Since \(\log s<0\), the condition \(s^b<|U_x|<s^a\) is equivalent to \(a<\log|U_x|/\log s<b\). Thus the logarithmic exponent converges to \(\mathrm{Unif}[0,1]\) (intervals interior to \((0,1)\) determine the weak limit, and their limiting masses exhaust one). The two sheets \(U_y=\pm\sqrt{1-U_x^2-U_z^2}\) have identical conditional weights by reflection symmetry, independently of the other coordinates, proving the fair sign and its independence. The same bounds make \(U_x,U_z\to0\) in probability, so the directional weak limit follows. This argument is a genuine limit theorem, not a consequence inferred merely from finite numerical tests.

## Verification
Run the accompanying standalone `verify_steinmetz.py` with Python, NumPy and SciPy. It derives the density independently from a quartic integral, numerically normalizes the law, checks the exact mean square against independent spherical samples, tests the endpoint asymptotics, and checks the support maximum for independent directions by explicit section optimization. A fixed seed is used. Numerical checks support but do not establish the infinite-dimensional quantifiers or asymptotic limits; steps 1–4 are the proof.

## Relationship to prior work
The classical Steinmetz bicylinder, its square slices, volume, and surface area are documented in Weisstein, *Steinmetz Solid* (MathWorld), and in Bourke's *Intersecting cylinders* (December 2003). Those formulas do not imply the distribution of isotropic supporting-plane widths. Finch's 2012 *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, studies a different object built by **convex hull** rather than the **intersection of two infinite cylinders**, and calculates mean widths, not the present full distribution and conditional logarithmic localization. Related published results on planar-section areas and extremal ellipsoids for Steinmetz bicylinders concern mathematically distinct observables. General product laws for spherical coordinates remain the closest potential source of indirect equivalence; historical priority should be checked independently.

## Limitations
Equal circular radii and perpendicular axes are essential for the displayed density. This result does not determine distributions for unequal-radius or nonorthogonal cylinder intersections, nor does it characterize projection area. The conditional localization involves the specified isotropic direction sampling and fixed body; it is not a claim about randomly sampled boundary points. The logarithmic boundary law is asymptotic at fixed radius, not a uniform estimate over varying radii. Independent mathematical audit and exhaustive historical-priority verification have not been performed.

## References
- E. W. Weisstein, *Steinmetz Solid*, Wolfram MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html (classical defining equations and volume/surface-area results).
- S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first submitted 2012-11-19, https://arxiv.org/abs/1211.4514 (related random-width methodology on a different solid).
- P. Bourke, *Intersecting cylinders*, dated December 2003, https://paulbourke.net/geometry/cylinders/index.html (historical geometry; full-text access restricted during comparison).
