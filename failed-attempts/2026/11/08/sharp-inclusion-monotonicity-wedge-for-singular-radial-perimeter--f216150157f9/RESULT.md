# Sharp inclusion-monotonicity wedge for singular radial perimeters of rectangles

## Finding

Let \(Q(a,b)=[-a,a]\times[-b,b]\), with \(a,b>0\). For every real \(p\), its Euclidean radial-power weighted boundary perimeter is
\[
E_p(Q(a,b))=\int_{\partial Q(a,b)}\|(x,y)\|_2^p\,d\mathcal H^1(x,y).
\]
For \(-1<p<0\), define
\[
G_p(r)=(1+r^2)^{p/2}+p\int_0^r(1+t^2)^{p/2-1}\,dt.
\]
There is a **unique** \(R_p>1\) with \(G_p(R_p)=0\), and the map \(p\mapsto R_p\) is strictly increasing and continuously differentiable from \((-1,0)\) onto \((1,\infty)\).

**Sharp monotonicity wedge.** For every \(-1<p<0\), set
\[
\mathcal C_p=\{Q(a,b):a,b>0,\  R_p^{-1}\le a/b\le R_p\}.
\]
If \(Q(a,b),Q(A,B)\in\mathcal C_p\), \(Q(a,b)\subsetneq Q(A,B)\), then
\[
E_p(Q(a,b))< E_p(Q(A,B)).
\]
The eccentricity constant \(R_p\) is best possible: for any \(R>R_p\), there exist *strictly nested* centered axis-parallel rectangles of aspect ratio at most \(R\) for which the above inequality is reversed. More precisely, whenever \(a/b>R_p\), increasing only the shorter half-side \(b\) by a sufficiently small amount *strictly decreases* \(E_p\), and similarly with \(a,b\) exchanged.

Equivalently, for each \(R>1\) there is a unique exponent \(p_R\in(-1,0)\) with \(R_{p_R}=R\). The weighted perimeter is nondecreasing on *all* ordered pairs of centered axis-parallel rectangles whose longer-to-shorter half-side ratio is at most \(R\) **if and only if** \(p\ge p_R\). For \(p>p_R\), every proper inclusion within this class yields strict increase; strict increase holds also at \(p=p_R\). For the special class \(R=1\) of centered squares, nondecrease holds precisely when \(p\ge-1\), and is strict under proper inclusion precisely when \(p>-1\).

The two singular transition laws are
\[
R_p=1+\sqrt2\,\operatorname{arsinh}(1)\,(p+1)+O((p+1)^2)
\quad(p\downarrow-1),
\]
\[
\lim_{p\uparrow0}\frac{R_p^p}{-p}=\frac\pi2,
\quad\text{and hence }R_p\to\infty.
\]

## Assumptions and scope

All rectangles have positive half-side lengths and are centered at the origin, with sides along a common orthonormal frame. Because the origin is strictly inside every rectangle, \(E_p\) is finite for every real \(p\) on this family. Proper inclusion is equivalent to \(A\ge a\), \(B\ge b\), and at least one inequality being strict. The aspect-ratio bound is \(\max\{a/b,b/a\}\le R\). Rotating every rectangle by a common Euclidean isometry fixing the origin leaves the result unchanged. The statements do not assert monotonicity for arbitrary convex bodies or differently oriented rectangles.

## Proof

**1. Exact first variation.** The four line segments comprising the boundary give, with no approximation,
\[
E_p(Q(a,b))=4\left(\int_0^b(a^2+y^2)^{p/2}\,dy
+\int_0^a(b^2+x^2)^{p/2}\,dx\right).
\]
For each fixed positive \(a,b\), differentiation under these finite, nonsingular integrals yields
\[
\frac{\partial E_p}{\partial a}(a,b)
=4a^p\left((1+(b/a)^2)^{p/2}+p\int_0^{b/a}(1+t^2)^{p/2-1}\,dt\right)
=4a^pG_p(b/a).
\]
The symmetric formula \(\partial_b E_p=4b^pG_p(a/b)\) follows on exchanging the two axes.

**2. Sign and existence of the threshold.** For every \(r\ge0\),
\[
G_p'(r)=p(1+r)(1+r^2)^{p/2-1},\qquad G_p(0)=1.
\]
If \(-1<p<0\), this derivative is strictly negative, and
\[
\lim_{r\to\infty}G_p(r)=p\int_0^\infty(1+t^2)^{p/2-1}\,dt<0.
\]
Integration by parts gives the exact identity
\[
G_p(1)=(p+1)\int_0^1(1+t^2)^{p/2}\,dt>0.
\]
Consequently there is exactly one root \(R_p\), and it is strictly larger than one. The full first-variation sign rule is
\[
\partial_a E_p\begin{cases}>0,&b/a<R_p,\\=0,&b/a=R_p,\\<0,&b/a>R_p.\end{cases}
\]
The analogous rule holds for \(\partial_b E_p\). When \(p=0\), \(G_p\equiv1\); when \(p>0\), \(G_p(r)>0\) for all \(r\ge0\). For the boundary exponent \(p=-1\), direct integration gives \(G_{-1}(r)=(1-r)/\sqrt{1+r^2}\).

**3. Global monotonicity and sharpness.** The parameter domain \(\{(a,b)>0:a\le R_pb,\ b\le R_pa\}\) is convex, being an intersection of two half-planes with the positive quadrant. Between any comparable pairs in this domain, the line segment \((a_t,b_t)=(1-t)(a,b)+t(A,B)\) remains in it. Both gradient components of \(E_p\) are nonnegative along this segment. At each point they cannot *both* vanish, since \(R_p>1\). Therefore, for every nonzero nonnegative displacement \((A-a,B-b)\), the directional derivative is positive except possibly at isolated endpoints; integration over \(0<t<1\) proves strict increase.

If \(R>R_p\), choose \(R_p<a/b<R\). The derivative with respect to the shorter half-side \(b\) is strictly negative. By differentiability, there is \(\varepsilon>0\) sufficiently small that \(E_p(Q(a,b+\varepsilon))<E_p(Q(a,b))\), while both rectangles remain in the aspect-\(R\) class. This proves optimality, not merely a local necessary condition. At \(p=-1\) the same argument applies to every \(R>1\), since \(G_{-1}(r)<0\) for \(r>1\). For \(p<-1\), the scaling identity
\[
E_p(Q(sa,sb))=s^{p+1}E_p(Q(a,b))
\]
provides a violation even among squares. At \(p=-1\) this identity makes all centered squares have equal energy. Together with positivity of both partial derivatives for \(p\ge0\), these observations establish the asserted if-and-only-if classification for every real \(p\) and \(R\ge1\).

**4. Strict variation of \(R_p\) in \(p\).** The function \((p,r)\mapsto G_p(r)\) is smooth for \(p<0,r>0\), and \(\partial_rG_p(R_p)<0\). The implicit-function theorem gives smooth dependence. Put \(J_p(r)=\int_0^r(1+t^2)^{p/2-1}dt\). At the root, \((1+R_p^2)^{p/2}=-pJ_p(R_p)\). Therefore
\[
\left.\frac{\partial G_p(r)}{\partial p}\right|_{r=R_p}
=J_p(R_p)+\frac p2\int_0^{R_p}
\log\left(\frac{1+t^2}{1+R_p^2}\right)
(1+t^2)^{p/2-1}\,dt>0.
\]
Indeed, \(p<0\) and the logarithm is nonpositive; the first summand is strictly positive. Thus
\(R_p'=-\partial_pG_p(R_p)/\partial_rG_p(R_p)>0\). We will show its endpoint limits below; it then follows that the map covers \((1,\infty)\), and the unique inverse \(p_R\) exists.

**5. Endpoint laws.** At \(p=-1\) the explicit formula for \(G_{-1}\) has its root at \(r=1\), with \(\partial_rG_{-1}(1)=-1/\sqrt2\). The integration-by-parts identity in Step 2 implies
\(\partial_pG_p(1)|_{p=-1}=\int_0^1(1+t^2)^{-1/2}dt=\operatorname{arsinh}(1)\).
The implicit-function theorem therefore yields the stated Taylor expansion as \(p\downarrow-1\).

As \(p\uparrow0\), any bounded sequence of roots would contradict \(G_0(r)=1\), by continuity on bounded \(r\)-intervals; hence \(R_p\to\infty\). At the root,
\[
\frac{(1+R_p^2)^{p/2}}{-p}
=\int_0^{R_p}(1+t^2)^{p/2-1}\,dt.
\]
For \(-1<p<0\), the integrand extended by zero beyond \(R_p\) is bounded by \((1+t^2)^{-1}\), and converges pointwise to it. Dominated convergence gives \(\pi/2\) for the right side. Since \((1+R_p^{-2})^{p/2}\to1\), replacing \((1+R_p^2)^{p/2}\) with \(R_p^p\) preserves the limit. This completes the proof.

## Verification

The self-contained standard-library script `verification/check_rectangles.py` numerically evaluates the boundary integrals and the derivative formula by adaptive Simpson quadrature, checks roots and their ordering for six exponents, checks local failures outside the wedge, compares finite differences of the boundary functional with exact analytic derivatives, and checks homogeneity. Executed in a clean Python interpreter, it printed `RECTANGLE_WEIGHTED_PERIMETER_OK 902`. These numerical tests supplement Steps 1–5; they do not establish any universal quantifier or historical originality. The explicit root at \(p=-1\), the positivity at equal sides, and the two limiting laws are justified analytically above.

## Relationship to prior work

Csató, Giovagnoli and Roy (arXiv:2608.19851, first public version 2026-08-20) investigate radial weighted boundary perimeters, including singular negative powers, under fixed-perimeter constraints and identify needle extremizers in a symmetric planar class. They do not state an inclusion monotonicity threshold for the centered-rectangle family. Csató and Giovagnoli (arXiv:2610.11677, first public version 2026-10-08) establish monotonicity for **nonnegative increasing** radial weights when the inner convex body contains the origin and explain failures for decreasing weights in general. The new criterion gives the exact largest aspect-bounded rectangle class where monotonicity **survives** for each singular negative power. Saracco and Stefani (2023 preprint / 2024 journal publication) classify weights globally monotone on *all* nested convex bodies; this broader rigidity statement neither asserts nor implies the restricted positive wedge with negative powers.

## Limitations

The classification is for concentric, commonly oriented Euclidean rectangles; it does not assert anything for general convex bodies, translations, differing orientations, or higher-dimensional boxes. The power weight is singular at the origin when \(p<0\), but every rectangle here has boundary a positive distance from that point. Historical priority is provisional; earlier specialist literature could contain an unlocated version. No independent mathematical audit has been performed.

## References

1. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851 (first posted 2026-08-20), https://arxiv.org/abs/2608.19851.
2. G. Csató, D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677 (first posted 2026-10-08), https://arxiv.org/abs/2610.11677.
3. G. Saracco, G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, Mathematische Nachrichten 297 (2024), 1444–1450; first posted arXiv:2306.07770 (2023-06), https://doi.org/10.1002/mana.202300280.
