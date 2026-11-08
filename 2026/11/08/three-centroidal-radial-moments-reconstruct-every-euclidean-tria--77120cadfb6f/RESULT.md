# Three centroidal radial moments reconstruct every Euclidean triangle

## Finding

Let \(T\subset\mathbb R^2\) be any nondegenerate Euclidean triangle, let \(G\) be its area centroid, and let \(X\) be uniform in the interior with respect to normalized area. Define \(m_j=\mathbb E[\lVert X-G\rVert^{2j}]\) for \(j=1,2,3\). **The three numbers \((m_1,m_2,m_3)\) determine the unordered side lengths of \(T\), hence its congruence class. The initial pair \((m_1,m_2)\) does not.**

Write \(a,b,c\) for the three side lengths and \(A=a^2\), \(B=b^2\), \(C=c^2\). Put \(e_1=A+B+C\), \(e_2=AB+BC+CA\), and \(e_3=ABC\). The exact forward identities are

\[
 m_1=\frac{e_1}{36},\qquad
 m_2=\frac{e_1^2-2e_2}{270},\qquad
 m_3=\frac{163e_1^3}{408240}-\frac{19e_1e_2}{22680}-\frac{e_3}{756}.
\]

The explicit inverse is

\[
 e_1=36m_1,\quad
 e_2=\frac{e_1^2-270m_2}{2},\quad
 e_3=756\left(\frac{163e_1^3}{408240}-\frac{19e_1e_2}{22680}-m_3\right).
\]

The three squared side lengths are the roots, with multiplicities, of \(z^3-e_1z^2+e_2z-e_3=0\). This remains valid at isosceles and equilateral triangles.

The exact feasible-moment criterion is that \(e_1>0\), the above cubic has three **positive real roots**, counting multiplicities, and \(4e_2>e_1^2\). These conditions are simultaneously necessary and sufficient for a nondegenerate Euclidean triangle.

An additional consequence is the exact area identity

\[
 \operatorname{Area}(T)^2=81m_1^2-\frac{135}{4}m_2,
 \qquad \frac85m_1^2\le m_2<\frac{12}{5}m_1^2,
\]

with equality on the left precisely for equilateral triangles. Thus the first two radial moments already fix the area, even though they do not fix the shape.

## Assumptions and scope

The sampling measure is normalized two-dimensional Lebesgue measure over a triangle of strictly positive area. Distances are ordinary Euclidean distances in the original scale; no affine normalization is applied. Congruence allows reflections and vertex relabelings. Moments are exact population quantities, not sample estimates. The symbols \(a,b,c\) refer to the full edge lengths (not their halves).

## Proof

Choose the vertices \(v_1,v_2,v_3\), let \(G=(v_1+v_2+v_3)/3\), and represent a uniform point as \(X=\lambda_1v_1+\lambda_2v_2+\lambda_3v_3\). The barycentric vector \((\lambda_1,\lambda_2,\lambda_3)\) is uniform on \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\), so for nonnegative integers \(p,q,r\),

\[
 \mathbb E[\lambda_1^p\lambda_2^q\lambda_3^r]
 =\frac{2p!q!r!}{(p+q+r+2)!}.
\]

Put \(d_i=\lambda_i-1/3\); then \(\sum_i d_i=0\). The Euclidean squared-distance identity for any zero-sum coefficients gives

\[
 Z:=\lVert X-G\rVert^2=-A d_2d_3-Bd_3d_1-Cd_1d_2,
\]

where \(A=\lVert v_2-v_3\rVert^2\), \(B=\lVert v_3-v_1\rVert^2\), \(C=\lVert v_1-v_2\rVert^2\). Expand \(Z\), \(Z^2\), and \(Z^3\), apply the preceding Dirichlet monomial formula to each term, and collect the resulting symmetric polynomials. This yields respectively

\[
 \mathbb E[Z]=\frac{e_1}{36},\quad
 \mathbb E[Z^2]=\frac{e_1^2-2e_2}{270},\quad
 \mathbb E[Z^3]=\frac{163e_1^3}{408240}-\frac{19e_1e_2}{22680}-\frac{e_3}{756}.
\]

The standalone verifier performs this entire coefficient expansion over exact rationals, checking every polynomial coefficient, rather than only evaluating example triangles. Since the coefficient of \(e_3\) is nonzero, the displayed inverse formulas follow by consecutive elimination. Vieta's formulas then recover the multiset \(\{A,B,C\}\) uniquely, and the side-side-side congruence criterion finishes the reconstruction.

For feasibility, three positive roots are exactly three positive squared prospective side lengths. Their square roots form a nondegenerate triangle precisely when Heron's identity gives strictly positive area:

\[
 16\operatorname{Area}(T)^2
 =2(AB+BC+CA)-(A^2+B^2+C^2)
 =4e_2-e_1^2>0.
\]

Indeed the positive-side condition and the strict inequality are equivalent to the strict triangle inequalities by the factorization of Heron's polynomial. Conversely every nondegenerate triangle yields such roots. Substituting the first two moment identities proves the stated area formula. The lower moment inequality follows from \(A^2+B^2+C^2\ge (A+B+C)^2/3\), with equality precisely at \(A=B=C\); the strict upper inequality follows from positive area.

Finally, the squared side-length triples

\[
 (A,B,C)=(1,2,3),\qquad
 (A',B',C')=\left(\frac32,\frac{9+\sqrt{13}}4,\frac{9-\sqrt{13}}4\right)
\]

both have \(e_1=6\) and \(A^2+B^2+C^2=14\), hence \(e_2=11\) and \((m_1,m_2)=(1/6,7/135)\). Both have strictly positive area since \(4e_2-e_1^2=8\). However their products are \(e_3=6\) and \(e_3'=51/8\), so the third moments differ by \(1/2016\). They are noncongruent, establishing the sharp two-versus-three threshold.

## Verification

Run `python3 check_radial.py` using Python 3 and its standard library. The checker expands \(Z^j\), for \(j=1,2,3\), as exact five-variable polynomials in the squared side lengths and the barycentric integration variables; it integrates each coefficient with the exact simplex beta integral and compares every coefficient with the claimed formulas. It also checks 201 rational configurations with positive area, both explicit two-moment witnesses, and the area identity. It reports `VERIFY_OK universal_polynomial_identities=3 exact_triangle_cases=201 sharp_two_moment_pair=1 exact_area_formula=checked`.

The polynomial verification is a finite exact check of the fully specified algebraic identities. The mathematical proof additionally explains why those identities imply unique reconstruction for **every** positive-area triangle, rather than merely the tested configurations.

## Relationship to prior work

Gravin, Pasechnik, Shapiro and Shapiro (arXiv:1210.3193; first posted 11 October 2012) develop multivariate polytope moment generating functions, including a simplex formula (Corollary 3), and inverse problems under known candidate vertex sets. Those results provide a general integration framework but do not themselves give this rotation-invariant three-scalar inverse or the sharp two-scalar obstruction. Golub, Milanfar and Varah (1999) reconstruct planar polygon shapes from harmonic/complex moments through matrix pencils, which are a different, direction-sensitive measurement family. Davis (1964) likewise treats complex-plane triangle formulas. Our claim is limited to the three centroidal *radial* moments and their exact inverse; no general polytopal moment algorithm is claimed.

## Limitations

No claim is made that the algebraic moment formulas or barycentric integration are new methods. The historical priority of the precise three-scalar theorem remains provisional, particularly because full versions of the older Davis and Golub--Milanfar--Varah sources were not available for an exhaustive textual comparison. The inverse uses exact moments; near repeated roots and nearly degenerate triangles can be ill-conditioned, and no quantitative statistical stability theorem is claimed. The theorem does not extend automatically to nonuniform densities, arbitrary polygons, or higher-dimensional simplices.

## References

1. N. Gravin, D. V. Pasechnik, B. Shapiro, M. Shapiro, *On moments of a polytope*, first arXiv submission 11 October 2012, arXiv:1210.3193, https://arxiv.org/abs/1210.3193. In particular, Corollary 3 and sections on inverse moments.
2. G. H. Golub, P. Milanfar, J. Varah, *A Stable Numerical Method for Inverting Shape from Moments*, SIAM Journal on Scientific Computing 21 (1999), 1222–1243, DOI:10.1137/S1064827597328315.
3. P. J. Davis, *Triangle Formulas in the Complex Plane*, Mathematics of Computation 18 (1964), 569–577, DOI:10.2307/2002943.
