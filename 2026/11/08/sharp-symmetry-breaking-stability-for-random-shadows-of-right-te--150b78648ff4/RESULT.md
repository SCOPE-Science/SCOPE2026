# Sharp symmetry-breaking stability for random shadows of right tetrahedra

## Finding

Consider a nondegenerate trirectangular tetrahedron
\[
T=\operatorname{conv}\{(0,0,0),(a,0,0),(0,b,0),(0,0,c)\},\qquad a,b,c>0.
\]
Set
\[
t_1=\frac{a^{-2}}{a^{-2}+b^{-2}+c^{-2}},\quad
 t_2=\frac{b^{-2}}{a^{-2}+b^{-2}+c^{-2}},\quad
 t_3=\frac{c^{-2}}{a^{-2}+b^{-2}+c^{-2}},\quad
V=\sum_{i=1}^3(t_i-1/3)^2.
\]
For a uniformly oriented planar orthogonal projection, let \(p_3(T)\) be the probability that the shadow has three vertices (rather than four). Let \(p_*=\bigl(6\arccos(1/\sqrt3)-\pi\bigr)/(2\pi)\).

**Sharp global stability theorem.** Every such tetrahedron satisfies
\[
\boxed{p_3(T)-p_*\ge\frac{C_*}{2\pi}\,V,}
\]
where the exact, optimal constant is obtained by the following **one-variable** specification. Put \(g(u)=\arccos\sqrt u\), \(b_x=(1-x)/2\) and
\[
R(x)=\frac{2[g(x)+2g(b_x)-3g(1/3)]}{(3/2)(x-1/3)^2},\qquad 0<x<1,\ x\ne1/3.
\]
The function \(R\) has a **unique global minimum** at \(x=x_*\in(1/3,1)\), the unique root in that interval of
\[
\boxed{(x-1/3)[g'(x)-g'(b_x)]
      -2[g(x)+2g(b_x)-3g(1/3)]=0.}
\]
Then \(C_*=R(x_*)\). For orientation only, numerical evaluation gives
\[
x_*\approx0.7849911511512952530,\quad
C_*\approx0.5861870196912077486,\quad
\frac{C_*}{2\pi}\approx0.0932945617601618998.
\]
Equality holds **exactly** in the equiaxial case \(t_1=t_2=t_3=1/3\), and in the three permutations of
\[
(t_1,t_2,t_3)=(x_*,(1-x_*)/2,(1-x_*)/2).
\]
Thus the optimal stability coefficient is not controlled by an infinitesimal deformation of the equality shape; it is attained by a second, asymmetric family with two equal physical legs.

## Assumptions and scope

The tetrahedron is Euclidean and nondegenerate; the three displayed legs are mutually perpendicular. Directions are Haar-uniform on the projective sphere, equivalently unit normals uniform on \(S^2\) up to sign. A polygonal shadow is defined by its convex hull, with exceptional nongeneric directions ignored (probability zero). All probabilities are population probabilities, not sampling estimates.

The quantities \(t_i\) have a direct metric meaning: writing \(A_i\) for the area of the right-angled face opposite leg \(i\) and \(A_B\) for the oblique triangular face, de Gua's theorem gives
\[
 t_i=\frac{A_i^2}{A_B^2},\qquad \sum_i A_i^2=A_B^2.
\]
Accordingly, \(V\) is the squared dispersion of the normalized squared areas of the three perpendicular faces, not an arbitrary coordinate scale. The result is invariant under scaling and permutation of the legs.

## Proof

**1. Exact shadow formula.** A projected vertex of a tetrahedron is hidden precisely when the projection direction enters one of the two opposite spherical tangent cones at that vertex. These four pairs are disjoint except on measure-zero directions. Therefore (as in Feldman--Klain's solid-angle probability formula) the triangle-shadow probability equals the sum \(S\) of the tetrahedron's four inner vertex solid angles divided by \(2\pi\). For a trirectangular tetrahedron, the outward normal to its oblique face has positive direction cosines \(\sqrt{t_i}\), while the remaining three coordinate faces are perpendicular. The spherical-excess/dihedral-angle identity gives, **exactly**,
\[
 S=2\sum_{i=1}^3\arccos\sqrt{t_i}-\pi,
 \qquad p_3(T)=\frac S{2\pi}.
\]
This also follows by direct spherical-triangle integration. Hence the theorem is equivalent to
\[
 D(t):=2\sum_i g(t_i)-6g(1/3)\ge C_*V(t).
\]

**2. Positivity, boundary and center.** Here \(g'(u)=-1/(2\sqrt{u(1-u)})\). At any interior stationary point of \(\sum_i g(t_i)\) on \(\sum_i t_i=1\), the three numbers \(t_i(1-t_i)\) coincide. Two distinct positive values with equal such product must sum to one, which would force the third coordinate to vanish. Thus the unique interior stationary point is the equilateral triple. On a boundary edge, \(\sum_i g(t_i)=\pi\), whereas \(3g(1/3)<\pi\). This proves \(D(t)>0\) away from the center.

The ratio \(D/V\) extends continuously to the center, with limit
\[
 C_0=g''(1/3)=\frac9{8\sqrt2}.
\]
On the boundary its numerator is constant, and \(V\le 2/3\), so the minimum boundary ratio is
\[
 C_{\partial}=3\pi-9g(1/3)>C_0.
\]
For an entirely rational check of the last strict comparison, use the positive Taylor coefficients of \(\arcsin\) at \(z=1/\sqrt3>577/1000\), the upper bounds \(\pi<22/7\) and \(1/\sqrt2<708/1000\), and the exact rational inequality
\[
 z_0+\frac{z_0^3}{6}+\frac{3z_0^5}{40}+\frac{5z_0^7}{112}
 >\frac{22}{42}+\frac{708}{8000},\qquad z_0=577/1000.
\]
This proves \(\arcsin(1/\sqrt3)>\pi/6+1/(8\sqrt2)\), exactly equivalent to \(C_{\partial}>C_0\). Along \(t=(x,(1-x)/2,(1-x)/2)\), the derivative of the continuously extended ratio at \(x=1/3\) is \(g'''(1/3)/6<0\); consequently some noncentral interior point has ratio below \(C_0\). The global minimum of \(D/V\) is therefore attained away from the center and the boundary.

**3. The two-equal-coordinate reduction.** At a global interior minimizer of \(D/V=C\), a Lagrange multiplier gives
\[
  g'(t_i)-C(t_i-1/3)=\lambda\quad(i=1,2,3).
\]
Direct differentiation yields
\[
 g'''(u)=-\frac{8u^2-8u+3}{8[u(1-u)]^{5/2}}<0
 \quad(0<u<1).
\]
Thus \(g''(u)-C\) strictly decreases from \(+\infty\) to \(-\infty\). The function \(g'(u)-C(u-1/3)\) first increases and then decreases: every horizontal level is met at most twice. Among the three \(t_i\), at least two are equal. Writing the distinct coordinate as \(x\) reduces the entire global optimization to \(R(x)\), and conversely every point of that curve represents a tetrahedron.

**4. Uniqueness and exact sharpness.** Let \(b_x=(1-x)/2\),
\[
F(x)=2[g(x)+2g(b_x)-3g(1/3)],\quad
G(x)=(x-1/3)F'(x)-2F(x).
\]
For \(x\ne1/3\), the sign of \(R'(x)\) equals the sign of \(G(x)/(x-1/3)^3\), and
\[
G(1/3)=G'(1/3)=0,\quad G''(x)=(x-1/3)F'''(x).
\]
Writing \(h(u)=-g'''(u)>0\), direct differentiation gives
\[
F'''(x)=\frac12\bigl(h(b_x)-4h(x)\bigr),\quad
\frac{h(b_x)}{h(x)}=
\frac{1+2x^2}{8x^2-8x+3}\left(\frac{4x}{1+x}\right)^{5/2}.
\]
On \(0<x<1/3\), \(h\) decreases for arguments in \((0,1/2)\) and \(x<b_x\); therefore \(F'''(x)<0\). Integrating the sign of \(G''\) twice from \(x=1/3\) proves \(G(x)>0\), hence \(R'(x)<0\) throughout that interval. No optimizer lies to the left of \(1/3\).

For \(1/3<x<1\), clearing positive factors and squaring the positive ratio above shows that \(F'''(x)=0\) exactly when
\[
P(x)=192x^9-192x^8+144x^7+128x^6+135x^5-109x^4-42x^3+38x^2+3x-9=0.
\]
The exact Sturm sequence of \(P\) has sign variations **five** at \(1/3\) and **four** at \(1\), with neither endpoint a root. Thus there is exactly one root \(x_0\) between them. Since \(F'''(1/3)<0\) and \(F'''(x)>0\) near \(1\), the sign changes once, from negative to positive. It follows that \(G''\) first is negative and then positive. Starting from \(G(1/3)=G'(1/3)=0\) and noting \(G(x)\to+\infty\) as \(x\uparrow1\) (because \(F'(x)\to+\infty\)), \(G\) has exactly one zero \(x_*\in(x_0,1)\). Hence \(R\) decreases before \(x_*\) and increases after it: the stated constant is globally optimal, with the complete equality characterization.

## Verification

Run `python verify.py` with Python 3 plus `numpy`, `scipy`, `sympy`, and `mpmath`. The verifier computes exact rational Sturm variations \((5,4)\); checks the rational Taylor comparison; isolates \(x_*\) and \(C_*\) numerically; evaluates the inequality on 130,000 random positive parameter triples; and independently projects 54,000 randomly oriented tetrahedra as planar point sets, comparing hull vertex counts to the solid-angle law. Its completed output was:

`VERIFY_OK sturm=(5,4) sharp_constant= 0.586187019691207749 optimizer= 0.784991151151295253 random_simplex_tests= 130000 geometric_projection_trials= 54000 max_projection_error= 0.002235`

The infinite inequality and uniqueness follow from the analytic and exact Sturm arguments above, not from finite random sampling. The numeric digits are descriptive, not a substitute for the exact root specification.

## Relationship to prior work

The projection probability identity is due to Feldman--Klain (2008); it is used, not claimed as new. The unrefined sharp lower bound for the sum of solid angles in trirectangular tetrahedra is explicitly Theorem 2 of Katsuura (2020). The present contribution is the **optimal global quadratic remainder measured by normalized squared right-face areas**, the scalar computation of its sharp constant, and its unusual off-center equality shapes. Korotov (2026) treats different tetrahedral classes, including an isogonic-family defect estimate, but does not furnish this sharp remainder for the right-tetrahedron family. The 2015 Brandts--Cihangir--Křížek nonobtuse-simplex bounds are relevant background; the accessible abstract does not settle the proposed sharp coefficient. External priority remains provisional.

## Limitations

The result covers only trirectangular tetrahedra and Haar-uniform directions, not all orthocentric or nonobtuse tetrahedra. It gives a globally sharp deterministic bound but no statistical inference rates from finitely many projections. The comparator for general nonobtuse simplices was available only in abstract form; this introduces residual priority risk. No independent audit has been performed.

## References

- D. V. Feldman and D. A. Klain, *Angles as probabilities*, first public arXiv version September 19, 2008, `arXiv:0809.3459`, https://arxiv.org/abs/0809.3459 .
- H. Katsuura, *Solid Angle Sum of a Tetrahedron*, *Journal for Geometry and Graphics* 24 (2020), 29--34, https://www.heldermann-verlag.de/jgg/jgg24/j24h1kats.pdf .
- J. Brandts, A. Cihangir and M. Křížek, *Tight bounds on angle sums of nonobtuse simplices*, *Applied Mathematics and Computation* 267 (2015), 397--408, https://doi.org/10.1016/j.amc.2015.02.035 .
- S. Korotov, *On Exact Dihedral Angle Sum Ranges for Orthocentric and Isogonic Tetrahedra*, first public arXiv version October 19, 2026, `arXiv:2610.26529`, https://arxiv.org/abs/2610.26529 .
