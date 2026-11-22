# The thirteen-generator anticanonical ring of an octagonal-prism toric Fano threefold

## Finding

Let \(X\) be the complex projective toric threefold of Petracci–Villa's octagonal-prism Fano polytope (defined explicitly below). Its anticanonical section ring, with reflexive powers,
\[
R(X,-K_X)=\bigoplus_{m\ge0}H^0(X,\mathcal O_X(-mK_X)),
\]
has an **irredundant monomial Hilbert basis of exactly thirteen elements**: three in degree one, six in degree two and four in degree three. In particular the ring has no necessary algebra generators of degree greater than three. Its Hilbert series is
\[
\boxed{\sum_{m\ge0}h^0(X,\mathcal O_X(-mK_X))t^m
=\frac{1+2t+7t^2+15t^3+20t^4+21t^5+21t^6+20t^7+15t^8+7t^9+2t^{10}+t^{11}}{(1-t)(1-t^2)(1-t^3)(1-t^6)}.}
\]
The Cartier index of \(K_X\) is exactly six. The rational map defined by \(|-K_X|\) has one-dimensional image, a smooth conic, but the rational map defined by \(|-2K_X|\) is birational onto its image. Thus two is the smallest positive anticanonical multiple producing a birational rational map. These are assertions about the **toric degeneration \(X\)**, not about any K-stable nearby deformation.

## Assumptions and scope

Work over \(\mathbb C\). Let \(N=\mathbb Z^3\). Put
\[
F=\operatorname{conv}\{(2,2),(1,2),(-1,1),(-2,-1),(-2,-2),(-1,-2),(1,-1),(2,1)\}\subset\mathbb R^2,
\]
\[P=F\times[-1,1]\subset N_{\mathbb R}.\]
Let \(X\) be the normal projective toric variety with fan consisting of cones over the faces of \(P\), with anticanonical Weil divisor given by the toric boundary. The source proves that this \(X\) is K-polystable with \((-K_X)^3=11/3\), and uses it to construct K-stable Fano deformations with obstructed deformation spaces. Those conclusions are prior work.

Define the rational polygon
\[
Q=\{(a,b)\in\mathbb R^2:\ a u+b v\ge-1\text{ for all }(u,v)\in F\}.
\]
Its eight vertices are
\[
\pm(0,1/2),\quad\pm(1/2,0),\quad\pm(1/3,-2/3),\quad\pm(2/3,-1/3).
\]
For every nonnegative integer \(m\), put \(E(m)=\#(mQ\cap\mathbb Z^2)\). Equations involving \(\mathcal O_X(-mK_X)\) mean the standard rank-one reflexive toric sheaves; linear systems need not be everywhere basepoint-free.

## Proof

**1. Polar and sections.** From the two opposite height facets of the prism,
\[
P^\circ=\{(a,b,c)\in\mathbb R^3:|c|\le1,\ (a,b)\in(1-|c|)Q\}.
\]
The usual toric monomial basis of global sections gives, for \(m\ge0\),
\[
H^0(X,\mathcal O_X(-mK_X))
=\bigoplus_{(a,b,c)\in mP^\circ\cap\mathbb Z^3}\mathbb C\chi^{(a,b,c)}.
\]
Consequently its dimension is exactly
\[
h_m=E(m)+2\sum_{j=0}^{m-1}E(j),\qquad h_0=1,
\]
with an empty sum interpreted as zero. The fact that the polar is a *bipyramid* over \(Q\), not a product with an interval, is essential here.

**2. Exact Hilbert basis.** Consider the planar degree cone
\[
C_Q=\{(m,a,b)\in\mathbb R_{\ge0}\times\mathbb R^2:(a,b)\in mQ\}.
\]
Besides the central ray \((1,0,0)\), its integer semigroup has the following ten boundary generators in cyclic order:
\[
\begin{gathered}
(2,1,0),(2,0,1),(3,-1,2),(2,-1,1),(3,-2,1),\\
(2,-1,0),(2,0,-1),(3,1,-2),(2,1,-1),(3,2,-1).
\end{gathered}
\]
Every displayed ray lies on the polygonal boundary and the rays include all polygon vertices, with the two extra degree-two mid-edge points. The ten three-dimensional cones spanned by the central ray and each successive pair of boundary rays cover \(C_Q\). The determinants of these ten ordered triples are **all +1**: consecutive \((a,b)\)-coordinates have determinant +1. Hence these cones are unimodular. Every lattice point of \(C_Q\) is therefore a nonnegative integer sum of the eleven displayed rays. These generators are indecomposable: the only degree-one planar lattice point is the origin; the six nonzero degree-two points cannot split into two degree-one points; the four new degree-three points lie outside \(2Q\) and cannot split into degree-one and degree-two points.

For the actual four-dimensional anticanonical semigroup \(C=\{(m,a,b,c): |c|\le m,\ (a,b)\in(m-|c|)Q\}\), a point with \(c>0\) can be reduced by subtracting \(c\) copies of \((1,0,0,1)\); a point with \(c<0\) is similarly reduced using \((1,0,0,-1)\). The remainder has \(c=0\) and lies in \(C_Q\). Thus the complete minimal semigroup basis is
\[
\begin{aligned}
&\{(1,0,0,c):c=-1,0,1\},\\
&\{(2,a,b,0):(a,b)=(\pm1,0),(0,\pm1),(1,-1),(-1,1)\},\\
&\{(3,a,b,0):(a,b)=(2,-1),(-2,1),(1,-2),(-1,2)\}.
\end{aligned}
\]
The degree-one part contributes no nonzero planar coordinate, and the degree-three planar points lie outside \(2Q\), proving minimality also in the four-dimensional semigroup. Its semigroup ring is exactly \(R(X,-K_X)\).

**3. Cartier index and rational maps.** The denominators of the vertices of \(P^\circ\) are two and three (besides the integral north and south tips). Thus the smallest integer \(r\) making \(rP^\circ\) a lattice polytope, equivalently making \(rK_X\) Cartier, is \(r=6\). At \(m=1\) the only lattice points of \(P^\circ\) are \((0,0,-1),(0,0,0),(0,0,1)\). On the dense torus the corresponding rational map is \([z^{-1}:1:z]=[1:z:z^2]\), whose image is a smooth conic and whose generic fiber has dimension two. At \(m=2\), the four lattice points \((0,0,0),(1,0,0),(0,1,0),(0,0,1)\) of \(2P^\circ\) yield character ratios generating all three independent torus coordinates. Hence the degree-two rational map is birational onto its image, and minimality follows from the degree-one case.

**4. Hilbert series.** Rational Ehrhart theory implies that \(E(m)\) is a degree-two quasipolynomial whose period divides six (the common vertex denominator of \(Q\)). Direct integer-inequality enumeration for the eighteen values \(0\le m\le17\) fixes the three coefficients on each of six residue classes. The resulting exact formula, for all \(m\ge0\), is
\[
E(m)=\frac{11m^2+b_rm+c_r}{12},\qquad r\equiv m\pmod6,
\]
where
\[
\begin{array}{c|rrrrrr}r&0&1&2&3&4&5\\\hline
b_r&14&8&14&8&14&8\\
c_r&12&-7&12&9&-4&9\end{array}.
\]
Using \(h_m=E(m)+2\sum_{j<m}E(j)\), rational generating-function algebra gives the claimed Hilbert series. In particular \((h_0,h_1,h_2,h_3,h_4,h_5,h_6)=(1,3,11,29,59,105,173)\). The leading asymptotic coefficient \(11m^3/18\) is consistent with the known anticanonical volume \((-K_X)^3=11/3\).

## Verification

The standalone Python 3 program `verify_anticanonical.py` uses only the standard library. It checks all feasible intersections of the defining rational half-planes of \(Q\); checks the ten boundary-ray determinants and boundary inequalities; enumerates the degree-one, -two and -three planar sections; checks the residue-class Ehrhart formulas against exact lattice counts through degree forty-one; and checks the rational Hilbert series coefficient identity in the same range. The infinite semigroup-generation claim is supplied by the unimodular-cone proof, and the all-degree section-count formula uses the rational Ehrhart theorem, not finite extrapolation alone.

## Relationship to prior work

Petracci and Villa [1, Theorem 4.1] construct the octagonal-prism toric Fano threefold, write its sixteen prism vertices and its ten polar vertices, and calculate its anticanonical volume and deformation space. Their work does **not** state the thirteen-generator section-ring basis, the explicit all-degree Hilbert series or the threshold between the first two anticanonical rational maps. The toric monomial-section correspondence and polytope technique are standard [2, §3]; the novelty asserted here is the exact evaluated algebra and its birational-geometric consequence for this particular newly constructed example. Earlier obstructed K-polystable toric Fano examples [3] have different polytopes and anticanonical volumes, and do not imply these exact numbers. This comparison establishes no global guarantee against unpublished computations or unpublished classification tables.

## Limitations

The result concerns the central **K-polystable toric** threefold \(X\) and makes no claim that its thirteen-generator presentation persists for an arbitrary K-stable deformation. The rational maps may have base loci on the singular variety; only the induced maps on dense tori, image dimensions and birationality are asserted. A minimal *algebra generating set* is given, but a minimal defining ideal and its graded syzygies are not computed. Nothing here is an independent audit or a complete classification of Fano threefolds with these invariants.

## References

[1] A. Petracci and A. Villa, *K-stable Fano varieties can have obstructed deformations*, arXiv:2611.15330v1, posted November 11, 2026, especially Theorem 4.1 and its proof. https://arxiv.org/html/2611.15330v1

[2] A. Grassi, G. Gugiatti, W. Lutz and A. Petracci, *Reflexive polygons and rational elliptic surfaces*, Rend. Circ. Mat. Palermo (2023), §3 (toric monomial sections and polar geometry). https://doi.org/10.1007/s12215-023-00922-3

[3] A.-S. Kaloghiros and A. Petracci, *On toric geometry and K-stability of Fano varieties*, Trans. Amer. Math. Soc. Ser. B 8 (2021), 548–577; arXiv:2009.02271. https://arxiv.org/abs/2009.02271
