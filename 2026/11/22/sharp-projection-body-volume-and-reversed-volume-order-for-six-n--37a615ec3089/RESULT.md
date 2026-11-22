# Sharp projection-body volume and reversed volume order for six-normal spherical designs

## Finding
Let \(X=\{x_1,\ldots,x_6\}\subset S^2\) consist of **six distinct unit vectors** satisfying the equally weighted spherical \(2\)-design equations
\[
\sum_{i=1}^6x_i=0,\qquad \sum_{i=1}^6x_ix_i^{\mathsf T}=2I_3.
\]
Let \(P_X\) be the convex polytope unique up to translation whose facet normals are these vectors and whose six facet areas are each \(2\pi/3\). Its total surface area is \(4\pi\). Write \(\Pi P_X\) for its projection body, so \(h_{\Pi P_X}(w)\) is the orthogonal projected area of \(P_X\) onto \(w^\perp\).

Every such design admits a unique twist modulus \(\phi\in[0,\pi/3]\) up to Euclidean congruence. The **exact projection-body volume** is
\[
\boxed{\operatorname{Vol}_3(\Pi P_X)=\frac{32\pi^3}{27}(1+2\cos\phi).}
\]
Thus its sharp global range, over **all** such six-node designs, is
\[
\boxed{\frac{64\pi^3}{27}\leq\operatorname{Vol}_3(\Pi P_X)\leq\frac{32\pi^3}9.}
\]
The lower equality holds precisely for the cube normals (\(\phi=\pi/3\)), and the upper equality precisely for the aligned-triangle normals of a triangular bipyramid (\(\phi=0\)); the maximum-to-minimum ratio is exactly \(3/2\).

Moreover, the affine-invariant projection-volume quotient is strictly decreasing along this family, with sharp range
\[
\boxed{8\leq\frac{\operatorname{Vol}_3(\Pi P_X)}{\operatorname{Vol}_3(P_X)^2}\leq\frac{27}2.}
\]
The minimum is again the cube and the maximum the triangular bipyramid. In contrast, the ordinary volume \(\operatorname{Vol}_3(P_X)\) itself **strictly increases** from the triangular bipyramid to the cube. Hence the two canonical volume invariants have exactly opposite orderings throughout this smallest continuous family of equal-weight spherical \(2\)-designs.

## Assumptions and scope
The ambient space is Euclidean \(\mathbb R^3\); volumes are Euclidean three-dimensional Lebesgue volumes. The normals are six distinct equally weighted nodes of strength at least two; they are not arbitrary balanced six-tuples. The positive surface-area measure is \((2\pi/3)\sum_i\delta_{x_i}\), which meets the necessary and sufficient Minkowski existence conditions and determines \(P_X\) up to translation. The claim concerns all such six-normal designs and no larger or weighted classes. All trigonometric parameters are in radians.

A convenient canonical representation uses \(a=\sqrt{2/3}\), \(b=1/\sqrt3\), and \(j\in\{0,1,2\}\):
\[
 u_j=(a\cos(2\pi j/3),a\sin(2\pi j/3),b),\qquad
 v_j=(a\cos(\phi+2\pi j/3),a\sin(\phi+2\pi j/3),-b).
\]
The two triples each form an orthonormal basis, and their sums are opposite.

## Proof
**1. Exhaustiveness of the twist parameter.** Let \(M\) be the \(3\times6\) matrix with columns \(x_i\). Then \(M\mathbf1=0\) and \(MM^\mathsf T=2I_3\), so \(E=M^\mathsf TM/2\) is a rank-three orthogonal projector, with diagonal entries \(1/2\) and \(E\mathbf1=0\). Consequently \(F=I_6-E-\mathbf1\mathbf1^\mathsf T/6\) is a rank-two orthogonal projector with diagonal entries \(1/3\). Write \(F=Y^\mathsf TY\), where the two rows of \(Y\) are orthonormal, and define \(z_i=\sqrt3(Y_{1i}+\mathrm iY_{2i})\). The six numbers have modulus one and satisfy \(\sum z_i=\sum z_i^2=0\). Newton's identities and the reciprocal-conjugate identities for a monic polynomial with unit-circle roots show that the polynomial with roots \(z_i\) has the form \(z^6-cz^3+d\). Its roots therefore split into two equilateral triples (with multiplicities allowed). For two indices within one triple, \(F_{ij}=-1/6\); since \(E_{ij}=-1/6-F_{ij}\) for distinct indices, the corresponding normals are orthogonal. Thus the six normals partition into two orthonormal triples, whose vector sums are opposite and each of length \(\sqrt3\). Aligning their common sum axis vertically gives the two latitude rings displayed above. Rotations, reflections, and relabelings reduce their relative twist to exactly one value \(\phi\in[0,\pi/3]\). Conversely every such twist satisfies the stated design identities.

**2. Projection body as a zonotope.** Cauchy's projection formula gives, for every unit \(w\),
\[
 h_{\Pi P_X}(w)=\frac12\sum_{i=1}^6\frac{2\pi}3|w\cdot x_i|=\frac\pi3\sum_{i=1}^6|w\cdot x_i|.
\]
Consequently \(\Pi P_X=\sum_i[-\pi x_i/3,\pi x_i/3]\). The three-dimensional zonotope determinant formula (obtained by successive Minkowski additions of segments, or by mixed volumes) is
\[
 \operatorname{Vol}_3(\Pi P_X)=8\left(\frac\pi3\right)^3\sum_{1\leq i<j<k\leq6}|\det(x_i,x_j,x_k)|.
\]
This is an identity for the complete three-dimensional body, not a directional brightness estimate.

**3. Exact evaluation of all twenty minors.** There are two triples wholly contained in one ring; because each ring is orthonormal, both determinants have absolute value one. For any mixed triple, two normals belong to one orthonormal basis. Its absolute determinant is the absolute inner product between the remaining normal and the omitted vector of that basis. Thus each of the two mixed-triple types contributes exactly \(\sum_{i,j=0}^2|u_i\cdot v_j|\).

For \(j=0,1,2\), put
\[
 q_j=\frac{2\cos(\phi+2\pi j/3)-1}3.
\]
Every \(q_j\) appears exactly three times among the nine cross-inner products. Throughout \(0\leq\phi\leq\pi/3\), \(q_0\geq0\), \(q_1\leq0\), \(q_2\leq0\), and \(q_0+q_1+q_2=-1\). Therefore
\[
 \sum_{i,j=0}^2|u_i\cdot v_j|
 =3(q_0-q_1-q_2)=3(1+2q_0)=1+4\cos\phi.
\]
The full absolute minor sum is exactly \(2+2(1+4\cos\phi)=4+8\cos\phi\). Substitution into the zonotope formula yields \(32\pi^3(1+2\cos\phi)/27\), including both endpoints without a limiting argument.

**4. Sharp extrema and opposite order.** The formula is strictly decreasing on the open interval because its derivative is \(-64\pi^3\sin\phi/27<0\). At \(\phi=0\) and \(\phi=\pi/3\) the values are respectively \(32\pi^3/9\) and \(64\pi^3/27\), with uniqueness up to congruence from Step 1. The already established exact volume of the original equal-area Minkowski polytope is
\[
 \operatorname{Vol}_3(P_\phi)=\frac{4\pi^{3/2}}{9\sqrt3}\,\frac{1+t}{\sqrt t},\qquad t=2\cos(\pi/3-\phi)\in[1,2].
\]
Here \(t\) strictly increases with \(\phi\), while \((1+t)/\sqrt t\) has derivative \((t-1)/(2t^{3/2})>0\) for \(t>1\). Thus \(\operatorname{Vol}_3(P_\phi)\) strictly increases while \(\operatorname{Vol}_3(\Pi P_\phi)\) strictly decreases. Dividing gives
\[
 \frac{\operatorname{Vol}_3(\Pi P_\phi)}{\operatorname{Vol}_3(P_\phi)^2}
 =18\frac{t(1+2\cos\phi)}{(1+t)^2},
\]
which is strictly decreasing, with endpoint values \(27/2\) and \(8\). For any invertible linear map \(A\), the standard covariance \(\Pi(AP)=|\det A|A^{-\mathsf T}\Pi P\) implies \(\operatorname{Vol}(\Pi AP)/\operatorname{Vol}(AP)^2=\operatorname{Vol}(\Pi P)/\operatorname{Vol}(P)^2\); hence the quotient is genuinely affine invariant.

## Verification
The standalone Python file `verify_projection.py` directly constructs the six normals at 32 twists, checks their first and second moments, and sums **all twenty** absolute determinant minors without using the closed form in its summand. If NumPy and SciPy are available, it additionally constructs all 64 signed generator sums and obtains the zonotope's volume by an independent three-dimensional convex-hull calculation at five twists. It checks exact rational endpoint quotient ratios and the opposite volume ordering on a fine grid. Its observed output was `PASS including five independent convex-hull volume calculations`. The proof of the all-parameter identities and strict inequalities is the symbolic argument above; finite checks do not substitute for that proof.

## Relationship to prior work
An, *Minkowski Polytopes of Spherical Designs* (public author upload **2026-08-11**, arXiv version first posted 2026-08-12), establishes the equal-area Minkowski realization, the Cauchy projection-body relation, and general quantitative design-strength bounds. The available complete author manuscript was examined in its general setup, realization theorem, and projection-body section; it gives no six-normal exact projection-volume or sharp volume quotient. A prior published treatment, *Sharp volume interval for six-node spherical two-design Minkowski polyhedra*, provides the six-node twist parametrization and the **original** polytope volume formula quoted in Step 4. Neither result entails the new projection-volume ordering without the all-minor computation. *Sharp random-shadow variance across six-normal spherical-design polytopes* gives a different functional (variance of random projected area), strictly increasing in twist; that does not determine the three-dimensional volume of the projection body. *Sharp projection-body volume in a twisted eight-normal spherical three-design family* concerns a different eight-normal, higher-strength class and does not imply the six-normal identity. The classical Cauchy and zonotope determinant identities are acknowledged inputs rather than claimed innovations. An older exact formula under another terminology remains a historical-priority possibility.

## Limitations
Only six distinct, equally weighted spherical \(2\)-design nodes in three dimensions, and the canonical facet-area normalization \(2\pi/3\), are classified. The classification of six-node designs and the original polyhedron-volume formula are prior results; the claim is the sharp **projection-body volume and reversed-order quotient classification**. No claim is made for all six-facet polytopes without a spherical-design normal condition, for weighted designs, or for arbitrary spherical designs. Unindexed historical zonotope calculations could contain an equivalent formula, and one later general directional-kernel paper was available only at abstract level. Independent external audit is not represented.

## References
1. C. An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, public author-upload 2026-08-11, arXiv:2608.11570v1 first posted 2026-08-12, https://arxiv.org/abs/2608.11570; author-uploaded full text https://www.researchgate.net/publication/412115876_Minkowski_Polytopes_of_Spherical_Designs_High-Order_Isotropy_and_Quantitative_Sphericity.
2. *Sharp volume interval for six-node spherical two-design Minkowski polyhedra*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-volume-interval-for-six-node-spherical-two-design-minkowsk--666fc2b5c6c6.
3. *Sharp random-shadow variance across six-normal spherical-design polytopes*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-random-shadow-variance-across-six-normal-spherical-design--99907a4a8d4a.
4. *Sharp projection-body volume in a twisted eight-normal spherical three-design family*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-projection-body-volume-in-a-twisted-eight-normal-spherical--770182a65fe2.
5. C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869v1, https://arxiv.org/abs/2609.05869 (abstract-level comparison only).
6. E. Gover, *Congruence and Metrical Invariants of Zonotopes*, arXiv:1401.4749, https://arxiv.org/abs/1401.4749; classical zonotope volume determinant identity.
