# Exact spherical depth and fifth-order circular convergence for regular polygons

## Finding

Let \(K_n\subset\mathbb R^2\) be a centered regular Euclidean \(n\)-gon, \(n\ge3\). Choose independent points \(X,Y\) uniformly by area from \(K_n\). Write \(p_n\) for the probability that the center belongs to the closed disk with diameter \(XY\). This is the spherical depth of the center for uniform area measure. The result concerns a fixed convex polygon and its Euclidean centroid, not the spherical depth of a finite sample of its vertices.

For every even \(n\), \(p_n=1/2\). For odd \(n\ge3\), put
\[
z_n=\tan^2\!\left(\frac{\pi}{2n}\right),\qquad
B(z)=\frac{z^2-1}{z(z-3)}+
\frac{(z-1)^3(z+1)}{z^2(z-3)^2}
\log\!\left(\frac{1+z}{(1-z)^2}\right).
\]
Then the complete *elementary closed form* is
\[
\boxed{\displaystyle
p_n=\frac12+\frac{(-1)^{(n+1)/2}}{n}\left(\frac12-B(z_n)\right).}
\]
The bracket is strictly positive for every odd \(n\ge3\). In particular the sign alternation (already observed in earlier discussion) is exact. The sharp asymptotic evaluation is
\[
\boxed{\displaystyle
p_n=\frac12+(-1)^{(n+1)/2}\frac{5\pi^4}{192n^5}
+O(n^{-7}) \quad(n\to\infty,\ n\text{ odd}).}
\]
For \(n=3\) this reduces to the established \(p_3=1/3+(\log3)/6\). For \(n=5\), \(p_5=0.499054315984\ldots\). The coefficient \(5\pi^4/192\) is nonzero and thus the fifth-order decay is sharp.

## Assumptions and scope

All polygons are regular, of positive area, and centered at their ordinary centroid. Scale and orientation do not affect \(p_n\). The independent points are sampled continuously using normalized *area* measure. The disk is closed; the boundary event has probability zero. Only odd \(n\) use the logarithmic formula, but the formula for even \(n\) is unconditional. No extremality over nonregular polygons or over alternate centers is claimed.

## Proof

**1. Radial law.** Let \(\alpha=\pi/n\), scale the inradius to one, and partition directions into \(n\) sectors of width \(2\alpha\). The direction of a uniform-area point can be written
\[
\Theta=2\alpha J+T,
\]
where \(J\) is uniform on \(\{0,\ldots,n-1\}\), independent of the within-sector offset \(T\in[-\alpha,\alpha]\), with density
\[
f_\alpha(t)=\frac{\sec^2 t}{2\tan\alpha}.
\]
Indeed the polar radial function inside a sector is \(\rho(t)=\sec t\); the directional area element is \(\rho(t)^2dt/2\). Integrating over the sector gives \(\tan\alpha\), which normalizes the density.

The disk condition is \(X\cdot Y\le0\), equivalently \(\cos(\Theta_X-\Theta_Y)\le0\). If \(n\) is even, replacing \(X\) by \(-X\) preserves its distribution and reverses the sign of \(X\cdot Y\), so \(p_n=1/2\).

**2. Odd-sector count.** For \(n=2r+1\), condition on \(U=T_X-T_Y\in[-2\alpha,2\alpha]\). The sector-index difference is uniform modulo \(n\); its \(n\) angles are \(2k\alpha+U\). Counting those whose cosine is negative gives, up to measure-zero endpoints, exactly \(r+1\) or \(r\) favorable indices. The exceptional band is
\[
E_\alpha=\{\alpha/2<|U|<3\alpha/2\}.
\]
For \(n\equiv3\pmod4\), the count is \(r\) inside the band and \(r+1\) outside; for \(n\equiv1\pmod4\), the counts reverse. Hence, writing \(B_\alpha=\Pr(E_\alpha)\),
\[
p_n=\frac12+\frac{(-1)^{(n+1)/2}}{n}\left(\frac12-B_\alpha\right).
\]
This also shows why the angular law—not the random radii—controls the probability.

**3. Evaluation of the band.** By symmetry and conditioning on which offset is larger,
\[
B_\alpha=\frac1{2\tan^2\alpha}
\left[
\int_{-\alpha/2}^{\alpha/2}\!\sec^2x\{\tan(x-\alpha/2)+\tan\alpha\}\,dx
+\int_{\alpha/2}^{\alpha}\!\sec^2x\{\tan(x-\alpha/2)-\tan(x-3\alpha/2)\}\,dx
\right].
\]
(The second integrand has a finite interpretation at \(n=3\), where \(3\alpha/2=\pi/2\); its arguments lie strictly inside \((-\pi/2,\pi/2)\).) Integrating \(\sec^2 x\tan(x-\beta)\) by substituting \(u=\tan x\), and then using \(z=\tan^2(\alpha/2)\), \(\tan\alpha=2\sqrt z/(1-z)\) and \(\tan(3\alpha/2)=\sqrt z(3-z)/(1-3z)\), yields exactly \(B_\alpha=B(z)\). The apparent singularity in the last tangent at \(n=3\) cancels; the final expression is regular at \(z=1/3\), and gives \(B(1/3)=1-(\log3)/2\). All denominators in the final expression are nonzero for \(0<z\le1/3\).

**4. Strictness of the sign.** Rescale offsets to \([-1,1]\). Their density is \(F_\alpha(t)=\alpha\sec^2(\alpha t)/(2\tan\alpha)\), strictly increasing in \(|t|\). Regard \([-1,1]\) as a circle of circumference two. Translating this density by one unit gives an even profile \(G\) strictly decreasing in circular distance from zero. The circular difference of two independent offsets has density \(H=G*G\). On a circle, the convolution of two symmetric nonincreasing profiles is symmetric nonincreasing: by the layer-cake representation it suffices to convolve indicators of centered arcs, whose overlap length is nonincreasing as the separation increases from zero to half the circumference. The convolution \(H\) is not constant: \(H(0)>H(1/2)\) by strict Cauchy–Schwarz applied to the nonperiodic profile \(G\). Consequently the half-circle around zero carries strictly more than half the mass. The event \(E_\alpha\) is exactly the *opposite* half-circle for the circular difference, since it is \(\{1/2<|T_X/\alpha-T_Y/\alpha|<3/2\}\). Therefore \(B_\alpha<1/2\), as asserted.

For completeness, the arc-overlap monotonicity can be verified directly: for two centered circle arcs of half-lengths \(a,b\in(0,1)\), let \(L(d)\) be the intersection length of two intervals of half-lengths \(a,b\) on the real line separated by \(d\). For \(0\le d\le1\), the circular overlap is \(L(d)+L(2-d)\). The first term is nonincreasing, and the second can increase only where the first decreases with slope \(-1\); hence the sum is nonincreasing. Approximation extends this to continuous profiles.

**5. Sharp fifth-order asymptotic.** Uniformly for \(-1\le t\le1\),
\[
F_\alpha(t)=\frac12\left[1+\alpha^2\left(t^2-\frac13\right)+O(\alpha^4)\right].
\]
The band occupies exactly half of the circular difference range, so the constant term and all terms linear in the nonconstant part of \(F_\alpha\) vanish in \(B_\alpha-1/2\). Thus
\[
B_\alpha-\frac12=\alpha^4J+O(\alpha^6),
\]
where
\[
J=\frac14\int_{-1}^1\int_{-1}^1
\left(s^2-\frac13\right)\left(t^2-\frac13\right)
\left(\mathbf1_{\{1/2<|s-t|<3/2\}}-\frac12\right)dt\,ds.
\]
Putting \(u=|s-t|\), the polynomial convolution is
\[
\int_{u-1}^1\!\left(t^2-\frac13\right)
\left((t-u)^2-\frac13\right)dt
=-\frac{(u-2)(3u^4+6u^3-8u^2-16u+8)}{90}
\quad(0\le u\le2).
\]
Its integral over \([0,2]\) is zero, and integrating over \([1/2,3/2]\) gives \(J=-5/192\). Therefore \(1/2-B_\alpha=5\alpha^4/192+O(\alpha^6)\). Since \(\alpha=\pi/n\), the claimed \(n^{-5}\) expansion follows, with nonzero coefficient.

## Verification

The accompanying `verify.py` runs using the Python standard library. It independently compares the closed logarithmic form with numerical Simpson integration of the *unintegrated* band density for ten odd orders, checks sector counts directly for seven odd orders (more than ten thousand direction pairs), verifies the published equilateral-triangle specialization, and integrates the rational polynomial for the \(-5/192\) coefficient using exact fractions. It also checks approach to the predicted constant at larger orders. A successful run returned `PASS: 10706 checks`. Numerical checks do not replace Steps 1–5, which prove the statement for every integer \(n\ge3\).

## Relationship to prior work

Rabinowitz (arXiv:2608.27491, first submitted August 26, 2026) proves the general polygon directional-transfer principle and the complete triangle-incenter formula. The earlier Mathematics Stack Exchange discussion (question 5101873, October 2025) already gives the equilateral value, anticipates and argues the sign rule for odd regular polygons, and writes a Fourier expression for their probabilities; **none of those signs or the triangle evaluation is claimed as new here**. Bremner and Shahsavarifar (arXiv:1702.07399, first submitted February 23, 2017) develop general bivariate spherical-depth methods. The contribution evaluated here is the elementary all-order closed logarithmic evaluation together with the sharp fifth-order constant and two-order remainder, not the general cone-measure or Fourier framework.

## Limitations

This mathematical derivation has not been independently refereed or externally certified. Historical priority remains provisional; the 2025 discussion is particularly close and provides a general regular-polygon Fourier integral, so the originality claim is **limited to the explicit evaluated formula and sharp asymptotic**, not the parity sign. Any previously published closed evaluation or fifth-order coefficient would supersede that limited originality claim. The result treats only the center and regular polygons. It does not establish global maximal spherical depth, nor general convex-body extremality. Double-precision direct evaluation of the closed form suffers cancellation for very large \(n\); use the integral or higher precision there.

## References

1. S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491 (submitted 2026-08-26), https://arxiv.org/abs/2608.27491.
2. *What planar convex shape maximizes the probability that a random circle contains the centre?*, Mathematics Stack Exchange question 5101873, discussion initiated October 2025, https://math.stackexchange.com/questions/5101873/what-planar-convex-shape-maximizes-the-probability-that-a-random-circle-contains.
3. D. Bremner and R. Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane*, arXiv:1702.07399 (submitted 2017-02-23), https://arxiv.org/abs/1702.07399.
