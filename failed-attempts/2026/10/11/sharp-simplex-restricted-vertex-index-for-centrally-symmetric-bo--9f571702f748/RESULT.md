# Sharp simplex-restricted vertex index for centrally symmetric bodies
## Finding
Let
\[
K=-K\subset\mathbb R^d,
\qquad d\ge2,
\]
be a centrally symmetric convex body, and let
\[
P=\operatorname{conv}\{p_0,\ldots,p_d\}
\]
be any simplex containing \(K\). Then
\[
\boxed{\sum_{i=0}^d\|p_i\|_K\ge d(d+1)}.
\tag{1}
\]
Here \(\|\cdot\|_K\) is the Minkowski norm with unit ball \(K\).

The constant in (1) is sharp for every dimension. More precisely, if
\[
\Delta=\operatorname{conv}\{a_0,\ldots,a_d\},
\qquad
\sum_{i=0}^d a_i=0,
\]
is any nondegenerate simplex and
\[
K=\Delta-\Delta,
\]
then the simplex
\[
P=(d+1)\Delta
\]
contains \(K\), and each of its vertices satisfies
\[
\|(d+1)a_i\|_K=d.
\tag{2}
\]
Thus equality holds in (1).

Define the simplex-restricted vertex index by
\[
\operatorname{vein}_{d+1}(K)
=
\inf\left\{
\sum_{i=0}^d\|p_i\|_K:
K\subset\operatorname{conv}\{p_0,\ldots,p_d\}
\right\}.
\]
Then
\[
\operatorname{vein}_{d+1}(K)\ge d(d+1)
\tag{3}
\]
for every centrally symmetric \(K\), and every simplex difference body attains equality.

In dimension three this gives the exact finite-vertex statement
\[
\operatorname{vein}_{4}(T-T)=12
\tag{4}
\]
for every tetrahedron \(T\) centered at its centroid. Consequently, any outer polytope giving cost strictly below \(12\) for such a body must have at least five vertices.

## Assumptions and scope
A convex body is compact, convex, full-dimensional, and contains the origin in its interior. Central symmetry means \(K=-K\). The Minkowski norm is
\[
\|x\|_K
=
\inf\{t>0:x\in tK\}.
\]

The original vertex index permits any finite number of outer vertices. The quantity in (3) is its restriction to the smallest possible number, \(d+1\). Therefore
\[
\operatorname{vein}(K)
\le
\operatorname{vein}_{d+1}(K),
\]
and (3) is not a lower bound for the unrestricted vertex index.

The result is affine invariant. No Euclidean structure is used in the proof.

## Proof
Because \(K\) has nonempty interior, contains the origin, and lies in \(P\), the origin is an interior point of the simplex \(P\). Let
\[
\lambda_0,\ldots,\lambda_d>0,
\qquad
\sum_{i=0}^d\lambda_i=1,
\]
be its barycentric coordinates:
\[
\sum_{i=0}^d\lambda_i p_i=0.
\tag{5}
\]

Fix \(i\). Rearranging (5) gives
\[
-\frac{\lambda_i}{1-\lambda_i}p_i
=
\sum_{j\ne i}
\frac{\lambda_j}{1-\lambda_i}p_j.
\tag{6}
\]
The right side is a convex combination of the vertices of the facet opposite \(p_i\). Hence the point in (6) is exactly where the ray from the origin opposite to \(p_i\) meets that facet. If \(\|\cdot\|_P\) denotes the gauge of \(P\) about the origin, then
\[
\|-p_i\|_P
=
\frac{1-\lambda_i}{\lambda_i}.
\tag{7}
\]

Since \(K\subset P\), gauges reverse inclusion:
\[
\|x\|_P\le\|x\|_K.
\]
Using the symmetry of \(K\), equations (7) give
\[
\|p_i\|_K
=
\|-p_i\|_K
\ge
\|-p_i\|_P
=
\frac{1-\lambda_i}{\lambda_i}.
\tag{8}
\]
Summing (8),
\[
\sum_{i=0}^d\|p_i\|_K
\ge
\sum_{i=0}^d\frac1{\lambda_i}-(d+1).
\tag{9}
\]
By Cauchy--Schwarz,
\[
\left(\sum_{i=0}^d\lambda_i\right)
\left(\sum_{i=0}^d\frac1{\lambda_i}\right)
\ge(d+1)^2.
\]
Together with \(\sum_i\lambda_i=1\), this turns (9) into (1).

We now prove sharpness. Let \(\Delta=\operatorname{conv}\{a_0,\ldots,a_d\}\) have centroid zero. For every \(i\),
\[
-\frac1d a_i
=
\frac1d\sum_{j\ne i}a_j
\in\Delta.
\tag{10}
\]
Thus \(-a_i\in d\Delta\) for every vertex, and by convexity
\[
-\Delta\subset d\Delta.
\]
Consequently
\[
K=\Delta-\Delta
\subset
\Delta+d\Delta
=(d+1)\Delta=P.
\tag{11}
\]

It remains to compute the norms of the vertices of \(P\). Let \(\ell_i\) be the affine barycentric coordinate on \(\Delta\) satisfying
\[
\ell_i(a_j)=\delta_{ij}.
\]
Since the centroid is zero,
\[
\ell_i(0)=\frac1{d+1}.
\]
Therefore
\[
L_i(x)=\ell_i(x)-\frac1{d+1}
\]
is linear. If \(x=u-v\in K\) with \(u,v\in\Delta\), then
\[
L_i(x)=\ell_i(u)-\ell_i(v),
\]
so
\[
|L_i(x)|\le1
\qquad(x\in K).
\tag{12}
\]
For \(p_i=(d+1)a_i\), linearity gives
\[
L_i(p_i)=d,
\]
and (12) implies
\[
\|p_i\|_K\ge d.
\tag{13}
\]
On the other hand, (10) shows that both
\[
a_i
\quad\text{and}\quad
-\frac1d a_i
\]
belong to \(\Delta\). Hence
\[
\frac{d+1}{d}a_i
=
a_i-\left(-\frac1d a_i\right)
\in K,
\]
which is equivalent to
\[
p_i=(d+1)a_i\in dK.
\]
Thus
\[
\|p_i\|_K\le d.
\tag{14}
\]
Equations (13)--(14) prove (2), and hence sharpness.

Equality in the universal estimate forces equality in the reciprocal Cauchy inequality, so the origin must be the centroid of the outer simplex. It also forces equality in every comparison in (8). No stronger classification of all equality bodies is asserted.

## Verification
The bundled `verify.py` replays the barycentric part of the proof in exact rational arithmetic for deterministic families of positive barycentric weights in dimensions \(2\) through \(12\). It verifies both
\[
\sum_i\frac{1-\lambda_i}{\lambda_i}
=
\sum_i\frac1{\lambda_i}-(d+1)
\]
and the lower bound \(d(d+1)\), with equality at uniform weights.

For the sharpness family it uses the standard centered simplex barycentric-coordinate model. The linear coordinates of
\[
p_i=(d+1)a_i
\]
are exactly \(d\) in coordinate \(i\) and \(-1\) in every other coordinate. The checker verifies that their difference-body gauge is exactly \(d\), and that the containment certificate \(-a_i/d\in\Delta\) holds for every vertex.

The computation is a regression check only. The quantified theorem is the exact barycentric and gauge argument above.

## Relationship to prior work
Bezdek and Litvak introduced the vertex index
\[
\operatorname{vein}(K)
=
\inf\left\{
\sum_i\|p_i\|_K:
K\subset\operatorname{conv}\{p_i\}
\right\}.
\]
Their paper proves sharp low-dimensional estimates and, in dimension three, conjectures that every centrally symmetric body has vertex index at most \(12\), with equality on the family \(T-T\) generated by tetrahedra.

The same paper also records a Euclidean special fact: if a simplex contains the Euclidean unit ball, then the sum of the Euclidean norms of its vertices is at least \(d(d+1)\), with equality only for regular circumscribed simplices. The proof above replaces the Euclidean ball by an arbitrary centrally symmetric unit ball. This extension is not obtained by affine normalization, because a general centrally symmetric convex body is not affinely equivalent to a Euclidean ball.

Gluskin and Litvak subsequently proved the universal unrestricted lower bound
\[
\operatorname{vein}(K)\ge2d
\]
and developed an average-asymmetry estimate for polytopes with \(d+k\) vertices. Their stated \(d+1\)-vertex estimate is weaker than (1); the full-text statement does not give the exact simplex-restricted value \(d(d+1)\) for arbitrary symmetric unit balls.

Thus (4) settles the minimal-outer-vertex regime of the \(T-T\) family singled out by the three-dimensional conjecture. It does not settle the unrestricted conjecture, because outer polytopes with five or more vertices remain possible.

## Limitations
The lower bound is restricted to outer polytopes with exactly \(d+1\) vertices. It gives no lower bound of order \(d^2\) for the unrestricted vertex index.

The equality examples \(K=\Delta-\Delta\) are not claimed to exhaust all centrally symmetric bodies attaining equality with some outer simplex.

The Euclidean simplex inequality in the motivating source is prior work; the contribution here is its normed, all-symmetric-body extension and the exact finite-vertex consequence for simplex difference bodies.

Because the proof reduces to barycentric coordinates and gauges, an equivalent lemma may exist in older Minkowski-asymmetry literature under different terminology. Targeted searches did not locate such a statement, but this remains the principal historical risk.

## References
1. K. Bezdek and A. E. Litvak, *On the vertex index of convex bodies*, arXiv:1110.4334v1, 19 October 2011; *Advances in Mathematics* 215 (2007), 626--641. DOI: 10.1016/j.aim.2007.04.016.
2. E. D. Gluskin and A. E. Litvak, *Asymmetry of convex polytopes and vertex index of symmetric convex bodies*, *Discrete & Computational Geometry* 40 (2008), 528--536. DOI: 10.1007/s00454-008-9075-9.
