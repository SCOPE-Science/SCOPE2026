# Cap-centroid defect determines equiaffine curvature

## Finding
Let \(\Gamma\) be a \(C^4\) plane curve with positive Euclidean curvature at a point \(P\). For small \(h>0\), take the bounded convex cap \(K_h\) cut off from the local convex side by the line parallel to the tangent at \(P\), at inward normal separation \(h\). Write \(S(h)>0\) for its area, and \(d(h)\) for the perpendicular distance of its area centroid from the tangent at \(P\). With the standard equiaffine curvature \(k_{\rm ea}(P)\), normalized by \(\det(\Gamma_s,\Gamma_{ss})=1\) for equiaffine arclength \(s\),

\[
\boxed{\lim_{h\downarrow0}\frac{\frac35-\frac{d(h)}h}{S(h)^{2/3}}=\frac{3}{175}\left(\frac{3}{4\sqrt2}\right)^{2/3}k_{\rm ea}(P).}
\]

This identity recovers the signed equiaffine curvature from **area and centroid depth alone**, without measuring a derivative of the curve. It refines the classical universal leading law \(d(h)/h\to3/5\). In particular, whenever \(k_{\rm ea}(P)\ne0\), the sign of \(3/5-d(h)/h\) for sufficiently small \(h\) is the sign of \(k_{\rm ea}(P)\).

For a nondegenerate conic arc of positive curvature, the stronger finite-cap comparison holds on every range of heights for which the chord and local cap are bounded and the same connected arc is used: the ratio \(d(h)/h\) is strictly less than \(3/5\) for an ellipse, identically \(3/5\) for a parabola, and strictly greater than \(3/5\) for a hyperbola.

## Assumptions and scope
The curve is \(C^4\) on an open neighborhood of \(P\), with strictly positive curvature in a possibly smaller neighborhood. The tangent-parallel chord has two intersections with the chosen local convex arc for all sufficiently small positive heights. If \(\Gamma\) is only locally convex, \(K_h\) means the bounded region between these intersections and the arc; no global closed convex body is required. Density is uniform with respect to planar Euclidean area. The centroid is the ordinary area centroid. Equiaffine curvature is defined with the convex orientation and positive determinant; its sign and value are invariant under orientation-preserving area-preserving affine coordinate changes.

Choose oriented orthonormal coordinates with \(P=(0,0)\), tangent \(y=0\), and inward normal pointing toward \(y>0\). Then locally \(\Gamma\) is \(y=f(x)\), where \(f(0)=f'(0)=0\) and \(f''(0)>0\). The graph normalization used here is
\[
k_{\rm ea}(P)=\frac{f''''(0)}{3f''(0)^{5/3}}-\frac{5f'''(0)^2}{9f''(0)^{8/3}}.
\]
Under a positive-determinant affine map with determinant \(\lambda\), the left-hand limit and \(k_{\rm ea}\) both scale by \(\lambda^{-2/3}\). The dimensionless depth ratio is unchanged and cap area scales by \(\lambda\).

## Proof
Write the fourth-order Taylor expansion as
\[
f(x)=ax^2+bx^3+cx^4+o(x^4),\quad a=\tfrac12 f''(0)>0,\ b=\tfrac16 f'''(0),\ c=\tfrac1{24}f''''(0).
\]
Let \(x_-(y)<0<x_+(y)\) solve \(f(x)=y\) near zero. Inverting the signed square-root coordinate \(z=\operatorname{sgn}(x)\sqrt{f(x)/a}\) gives, uniformly as \(z\to0\),
\[
x=z-\frac{b}{2a}z^2+\left(\frac{5b^2}{8a^2}-\frac{c}{2a}\right)z^3+o(z^3).
\]
Substituting \(z=\pm\sqrt{y/a}\), the separation of the intersections is
\[
L(y)=x_+(y)-x_-(y)=\frac{2}{\sqrt a}y^{1/2}\left[1+\left(\frac{5b^2}{8a^3}-\frac{c}{2a^2}\right)y+o(y)\right].
\]
Set \(q=5b^2/(8a^3)-c/(2a^2)\). Fubini's theorem on the cap, using its horizontal slices, gives the area and its first normal moment as
\[
S(h)=\int_0^hL(y)\,dy=\frac{4h^{3/2}}{3\sqrt a}\left(1+\frac35 qh+o(h)\right),
\]
\[
S(h)d(h)=\int_0^h yL(y)\,dy=\frac{4h^{5/2}}{5\sqrt a}\left(1+\frac57 qh+o(h)\right).
\]
Consequently,
\[
\frac{d(h)}h=\frac35+\frac{12}{175}qh+o(h)
=\frac35-\frac{3f''(0)f''''(0)-5f'''(0)^2}{525f''(0)^3}h+o(h).
\]
The graph formula for the equiaffine curvature yields
\[
\frac35-\frac{d(h)}h=\frac{3}{175}k_{\rm ea}(P)\,f''(0)^{-1/3}h+o(h).
\]
Finally \(S(h)^{2/3}=(4\sqrt2/3)^{2/3}f''(0)^{-1/3}h+o(h)\); division proves the boxed formula. A \(C^4\) hypothesis suffices because the inverse series has an \(o(z^3)\) remainder, and integration preserves the required little-oh estimates.

For the finite conic comparison, write a nondegenerate conic near the tangent point as
\[
A x^2+2Bxy+C y^2=Dy,\qquad A>0,\ D>0.
\]
The exact chord width is
\[
L(y)=\frac{2\sqrt{AD}}{A}\,y^{1/2}\sqrt{1+\frac{B^2-AC}{AD}y}.
\]
After rescaling \(y=hu\), the centroid ratio is the mean of \(u\in(0,1)\) under density proportional to \(u^{1/2}Q(hu)\), where \(Q(y)=\sqrt{1+(B^2-AC)y/(AD)}\). The baseline density proportional to \(u^{1/2}\) has mean \(3/5\). A strictly increasing weighting factor strictly increases its mean, a strictly decreasing factor strictly decreases it, and a constant factor leaves it unchanged; this follows from the positivity of the covariance of two increasing functions on an interval. Ellipse, parabola and hyperbola respectively have \(B^2-AC<0\), \(=0\), and \(>0\), giving the stated strict trichotomy.

## Verification
The self-contained script `check_cap_curvature.py` evaluates the exact conic width integrals for three conic types at four shrinking heights, checking the inequality signs and convergence to the stated coefficient. It separately solves the two chord endpoints of the asymmetric quartic graph \(f(x)=x^2+0.2x^3+0.1x^4\), integrates the cap moments at four heights, and checks the mixed third- and fourth-derivative formula. Running `python check_cap_curvature.py` returned `CAP_CENTROID_AFFINE_CURVATURE_CHECKS_OK`. These finite computations corroborate, but do not prove, the limit; the argument above supplies the infinite statement.

## Relationship to prior work
Kim and Kim (2013), arXiv:1305.3337, proved the exact Archimedean area property characterizes parabolas and gave the first chord-length curvature limit. Kim, Kim and Park (2015), arXiv:1502.00188, proved \(d(h)/h\to3/5\) and that exact equality for all sufficiently small cuts characterizes a parabola. Kim and Kim (2015), arXiv:1502.01205, studied first-order limits of associated triangle centroids. Their inspected statements and proofs do not give the pointwise second-order equiaffine-curvature coefficient, the cap-area normalization, or this measurement recovery formula. The standard equiaffine-curvature normalization is part of classical affine differential geometry; the graph formula is not claimed new. The finite conic comparison is a consequence of elementary conic chord widths, and is not asserted as an independent priority claim. No exhaustive historical-priority claim is made.

## Limitations
The result is local, pointwise and planar, and needs four derivatives; it does not supply a uniform convergence rate on an entire curve without uniform regularity assumptions. If the equiaffine curvature vanishes at an isolated point, the theorem only gives a zero second-order coefficient and does not by itself establish that the curve is parabolic. At finite heights, the sign follows from the equiaffine curvature only sufficiently near a point with nonzero curvature; the global finite-height trichotomy is specific to conic arcs. Independent validation and exhaustive historical-priority checking are not provided.

## References
- D.-S. Kim and Y. H. Kim, *On the Archimedean characterization of parabolas*, first public preprint 2013-05-15, https://arxiv.org/abs/1305.3337 .
- D.-S. Kim, Y. H. Kim and S. Park, *Center of gravity and a characterization of parabolas*, first public preprint 2015-02-01, https://arxiv.org/abs/1502.00188 .
- D.-S. Kim and D. S. Kim, *Centroid of triangles associated with a curve*, first public preprint 2015-02-04, https://arxiv.org/abs/1502.01205 .
- M. Craizer, R. Teixeira and M. A. H. B. da Silva, *Affine properties of convex equal-area polygons*, *Discrete & Computational Geometry* (2012), https://doi.org/10.1007/s00454-012-9448-y (background equiaffine definitions).
