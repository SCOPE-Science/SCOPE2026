# A first-order cusp in the spherical Pál minimum-area profile
## Finding

For \(0<w<\pi\), define
\[
M(w)=\inf\{\operatorname{area}(K):K\subset S^2\text{ is a spherical convex body and }w(K)=w\}.
\]
The sharp minimizer theorem of Freyer and Sagmeister changes form at \(w=\pi/2\): a regular spherical triangle minimizes for \(0<w\le\pi/2\), while for \(\pi/2<w<\pi\) the minimizer is the polar of a spherical Reuleaux triangle of width \(\pi-w\).

The minimum value itself has the explicit branches
\[
M(w)=3\arccos\!\left(\frac{q(w)}{1+q(w)}\right)-\pi,
\qquad
q(w)=\frac{\cos^2 w+\cos w\sqrt{\cos^2 w+8}}{4},
\qquad 0<w\le\frac{\pi}{2},
\]
and, writing \(t=\pi-w\),
\[
M(w)=2\pi-3\sin t\,
\arccos\!\left(\frac{\cos t}{1+\cos t}\right),
\qquad \frac{\pi}{2}\le w<\pi.
\]
They agree at
\[
M\!\left(\frac{\pi}{2}\right)=\frac{\pi}{2},
\]
but the one-sided derivatives are
\[
M'_-\!\left(\frac{\pi}{2}\right)=\frac{3}{\sqrt2},
\qquad
M'_+\!\left(\frac{\pi}{2}\right)=3.
\]
Hence the sharp minimum-area profile has a genuine first-order cusp at the exact minimizer transition. Its slope jump is
\[
3-\frac{3}{\sqrt2}
=
3\left(1-\frac{1}{\sqrt2}\right)>0.
\]

## Assumptions and scope

All distances, widths, perimeters, and areas are spherical quantities on the unit two-sphere. The width is the minimum width used in the spherical Pál problem. The argument uses the Freyer--Sagmeister classification of all sharp minimizers and their polarity relation. It concerns the scalar sharp value \(M(w)\); it does not assert differentiability or a particular parametrization of the minimizing bodies themselves.

For the acute branch, the regular triangle is taken with side length \(s\) and width-realizing altitude \(w\). For the obtuse branch, \(U_t\) denotes the regular spherical Reuleaux triangle of width \(t=\pi-w\).

## Proof

On the acute branch, let \(s\) be the side length of the regular minimizing triangle and let \(c=\cos w\). The altitude to a side bisects that side, and the resulting right spherical triangle gives
\[
\cos s=\cos w\cos\frac{s}{2}.
\]
If \(q=\cos s\), solving this relation gives
\[
q=\frac{c^2+c\sqrt{c^2+8}}{4}.
\]
The spherical cosine law for an equilateral triangle gives its interior angle \(\alpha\) by
\[
\cos\alpha=\frac{q}{1+q}.
\]
Spherical excess therefore yields
\[
M(w)=3\alpha-\pi
=
3\arccos\!\left(\frac{q}{1+q}\right)-\pi.
\]

At \(w=\pi/2\), one has \(c=0\), \(q=0\), and hence \(\alpha=\pi/2\). Differentiating
\[
q(c)=\frac{c^2+c\sqrt{c^2+8}}{4}
\]
from \(c>0\) gives
\[
\frac{dq}{dc}\longrightarrow\frac{1}{\sqrt2}
\quad\text{as }c\downarrow0.
\]
Because \(dc/dw=-1\) at \(w=\pi/2\) and
\[
\frac{d}{dq}\arccos\!\left(\frac{q}{1+q}\right)\bigg|_{q=0}=-1,
\]
it follows that
\[
M'_-\!\left(\frac{\pi}{2}\right)=\frac{3}{\sqrt2}.
\]

For the obtuse branch, put \(t=\pi-w\). Freyer--Sagmeister identify the minimizer as \(U_t^\circ\) and use the spherical polar identity
\[
\operatorname{area}(L)=2\pi-\operatorname{per}(L^\circ).
\]
Applying this to \(L=U_t^\circ\) gives
\[
M(w)=2\pi-\operatorname{per}(U_t).
\]
Each of the three boundary arcs of \(U_t\) lies on a small circle of spherical radius \(t\). The angle subtended at its center is the angle \(\beta(t)\) of the equilateral spherical triangle of side \(t\). The spherical cosine law gives
\[
\beta(t)=\arccos\!\left(\frac{\cos t}{1+\cos t}\right).
\]
A small circle of radius \(t\) has line element scaled by \(\sin t\), so each arc has length \(\sin t\,\beta(t)\). Hence
\[
\operatorname{per}(U_t)=3\sin t\,\beta(t),
\]
which proves the stated obtuse branch.

At \(t=\pi/2\), \(\beta=\pi/2\). If
\[
r(t)=\frac{\cos t}{1+\cos t},
\]
then \(r'(\pi/2)=-1\), so \(\beta'(\pi/2)=1\). Since \(dt/dw=-1\),
\[
M'_+\!\left(\frac{\pi}{2}\right)
=
3\left(\cos t\,\beta(t)+\sin t\,\beta'(t)\right)\bigg|_{t=\pi/2}
=3.
\]
The two values at the transition both equal \(\pi/2\), while the derivatives differ, proving the cusp.

## Verification

The source theorem and its proof were checked at the regime statements, the spherical triangle area formula, the constant-width perimeter identity, the polar area--perimeter identity, and the discussion of the limiting case \(w\downarrow\pi/2\). The symbolic verification artifact independently checks both branch values at \(\pi/2\), the two one-sided derivatives, and the algebraic side-length relation. The verification uses exact symbolic limits; numerical sampling is supplementary only.

## Relationship to prior work

Freyer and Sagmeister prove the complete sharp spherical isominwidth theorem: regular triangles minimize up to width \(\pi/2\), and polars of Reuleaux triangles minimize above it. Their paper explicitly observes that the two theorems are accordant in the limiting case \(w\downarrow\pi/2\). The checked text does not state the explicit sharp value profile above, compute its one-sided derivatives at the transition, or identify a nondifferentiable scalar phase transition.

A later stability paper by Fodor and Sagmeister studies optimal stability for Pál-type inequalities in planes of constant curvature. Its publicly available abstract was checked as close literature; the exact slope discontinuity above was not stated there. No implication from the checked stability statement to the value-function cusp was found.

## Limitations

The result is a local regularity statement about the exact scalar optimum, not a new classification of minimizers. It does not determine higher-order shape variation across the transition or extend the spherical Pál theorem to higher dimensions. The originality search cannot exclude an unindexed historical observation of this elementary consequence; the claim is therefore limited to the exact formula and derivative jump established here from the published sharp theorem.

## References

1. A. Freyer and Á. Sagmeister, *The isominwidth problem on the 2-sphere*, arXiv:2411.11462v1, first public 2024-11-18.
2. F. Fodor and Á. Sagmeister, *Optimal stability of Pál's isominwidth inequality for ball convex bodies in planes of constant curvature*, arXiv:2606.02882v1, first public 2026-06-01.
