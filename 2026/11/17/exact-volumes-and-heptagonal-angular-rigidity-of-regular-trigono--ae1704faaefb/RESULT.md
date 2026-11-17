# Exact volumes and heptagonal angular rigidity of regular trigonometric cyclic four-polytopes

## Finding

For each integer \(n\geq5\), put \(\theta_j=2\pi j/n\) and
\[
v_j=\frac1{\sqrt2}(\cos\theta_j,\sin\theta_j,\cos2\theta_j,\sin2\theta_j)\in S^3,\qquad
P_n=\operatorname{conv}\{v_0,\ldots,v_{n-1}\}.
\]
Then the Euclidean four-volume is **exactly**
\[
\operatorname{vol}_4(P_n)=\frac{n^2}{48}\cos\frac{2\pi}{n}\sin^2\frac{2\pi}{n}.
\tag{1}
\]
These volumes increase strictly with \(n\) and converge to \(\pi^2/12\). More precisely,
\[
\frac{\pi^2}{12}-\operatorname{vol}_4(P_n)
=\frac{5\pi^4}{18n^2}+O(n^{-4}).\tag{2}
\]
In particular, the regular seven-vertex cyclic four-polytope has volume
\[
V_7=\frac{49}{48}\cos\frac{2\pi}{7}\sin^2\frac{2\pi}{7}
=0.389054556345294\ldots.\tag{3}
\]
There is an additional **local geometric rigidity** statement. Allow the seven angular parameters to vary independently in increasing cyclic order, while retaining the same unit-sphere trigonometric curve. At the regular heptagonal configuration the volume is stationary, and its angular Hessian has eigenvalues \(0\) (multiplicity one) and \(\lambda_1,\lambda_2,\lambda_3\) (each multiplicity two), where, for \(u=\cos(2\pi/7)\),
\[
\begin{aligned}
\lambda_1&=-\frac7{64}-\frac7{24}u+\frac7{48}u^2,\\
\lambda_2&=\frac{175}{384}-\frac{175}{192}u-\frac{35}{24}u^2,\\
\lambda_3&=\frac7{24}-\frac{259}{192}u-\frac{119}{96}u^2.
\end{aligned}\tag{4}
\]
All three are negative. Thus equal spacing is a **strict local volume maximum modulo common rotation** in the seven-angle family; no global optimality is asserted.

## Assumptions and scope

Volumes are ordinary four-dimensional Euclidean Lebesgue measure (not normalized volume); vertices lie on the unit sphere. The formula (1) holds for **every integer \(n\geq5\)**, with no limiting or genericity hypothesis. The local statement concerns only curves \(\theta\mapsto(\cos\theta,\sin\theta,\cos2\theta,\sin2\theta)/\sqrt2\), with seven distinct, cyclically ordered angular parameters. It does not concern arbitrary seven-point sphere configurations or arbitrary inscribed realizations of the cyclic combinatorial type.

## Proof

**Facet structure and determinant normalization.** The trigonometric moment curve in four dimensions realizes the cyclic combinatorial type [2, 3]. A four-vertex facet consists of two disjoint adjacent cyclic pairs \((i,i+1)\) and \((j,j+1)\). For completeness, an affine hyperplane restricted to the curve is a real trigonometric polynomial of degree at most two. Its four distinct zeros on the circle alternate its sign at each simple zero. Therefore a supporting hyperplane at four sampled parameters can have all other samples on one side precisely when the two negative-sign arcs each contain no sampled point; this is the two-disjoint-adjacent-pair condition. Conversely the degree-two interpolating trigonometric polynomial vanishing at any such four points has constant sign at every remaining sample, giving the facet. Thus there are \(n(n-3)/2\) tetrahedral facets.

Because \(n\geq5\), the sums of both the first and second roots of unity vanish, so the average of all vertices is the origin. The polytope is full dimensional and its origin lies strictly inside it. The tetrahedral facets therefore produce nonoverlapping origin-cones; each has volume \(|\det(v_i,v_{i+1},v_j,v_{j+1})|/4!\).

Let \(h=2\pi/n\), \(c=\cos h\), and \(x=\cos(kh)\). Direct expansion of the four-by-four determinant, or the Vandermonde factorization of the Fourier exponents \((-2,-1,1,2)\), gives
\[
D(k)=\det(v_0,v_1,v_k,v_{k+1})
=2\sin^2\frac h2\,(1-x)(c-x)(1+c+x).\tag{5}
\]
For \(k=2,\ldots,n-2\), all factors are positive: \(c>0\), \(x<c\), and \(1+c+x\geq c\). Consequently the absolute values can be dropped with the chosen row ordering. An ordered sum over \(i\) and cyclic edge separation \(k\) counts every unordered pair of disjoint edges twice. Hence
\[
\operatorname{vol}_4(P_n)=\frac n{48}\sum_{k=2}^{n-2}D(k).\tag{6}
\]
The polynomial expansion
\[
(1-x)(c-x)(1+c+x)=c+c^2-(1+c+c^2)x+x^3
\]
with \(\sum_{k=0}^{n-1}\cos(kh)=\sum_{k=0}^{n-1}\cos^3(kh)=0\) (valid for \(n\geq5\)) yields \(\sum_{k=2}^{n-2}D(k)=2n\sin^2(h/2)c(1+c)=nc\sin^2 h\). Substitute into (6) to obtain (1).

**Monotonicity and asymptotics.** Write the right side of (1) as \((\pi^2/12)\cos h\,(\sin h/h)^2\). For \(0<h\leq2\pi/5<\pi/2\), both \(\cos h\) and \(\sin h/h\) are positive and strictly decreasing in \(h\). Thus volume increases strictly as \(n\) increases. Taylor expansion at \(h=0\) gives (2).

**Seven-parameter Hessian.** For a sufficiently small perturbation of the ordered seven angles, the facet structure and signs in (6) remain unchanged, so the volume is a smooth function of those angles. Equal spacing is stationary by cyclic symmetry: all first partial derivatives agree, while changing all seven angles together is a rigid rotation and has zero directional derivative; hence every first derivative vanishes.

Here is an exact reproducible second-derivative calculation rather than a numerical Hessian assertion. Write \(\zeta=\exp(2\pi i/7)\). Replace the four real coordinates of a point on the curve by the complex rows with Fourier weights \((1,-1,2,-2)\); the fixed change-of-basis factor in its determinant is \(-1/16\). After differentiating twice with respect to angular arguments, the factor is \(+1/16\), since \(i^2=-1\). Summing the **ordered** facet pairs with factor \(1/48\) gives a real symmetric circulant Hessian \(H\). Each matrix entry can be represented exactly by an integer coefficient vector \((a_0,\ldots,a_6)\) meaning \(\sum_{r=0}^6 a_r\zeta^r/768\). Its first four entries \(H_{0,j}\), for \(j=0,1,2,3\), have coefficient vectors

| \(j\) | exact coefficients \((a_0,a_1,a_2,a_3,a_4,a_5,a_6)\) |
|---|---|
| 0 | \((0,-140,0,140,140,0,-140)\) |
| 1 | \((28,56,-14,-56,-56,-14,56)\) |
| 2 | \((0,14,-28,14,14,-28,14)\) |
| 3 | \((-28,0,42,-28,-28,42,0)\) |

The remaining entries follow from symmetry and circulancy. The Fourier mode \(k\) has eigenvalue \(\sum_{j=0}^6H_{0,j}\zeta^{kj}\). In the quotient algebra \(\zeta^7=1\), \(1+\zeta+\cdots+\zeta^6=0\), let \(u=(\zeta+\zeta^{-1})/2\). Then \(8u^3+4u^2-4u-1=0\). Substituting the table and reducing all terms to degree two gives \(\lambda_0=0\) and exactly the three expressions in (4). All reductions are checked using integer arithmetic by `VERIFY.py`.

For a rational sign check, the root \(u\) lies in \((3/5,1)\): the cubic is negative at \(3/5\) and strictly increasing on \([3/5,1]\), and its root on that interval is \(\cos(2\pi/7)\). For \(0<u<1\), the expression for \(\lambda_1\) is negative; substituting the lower bound \(u>3/5\) makes each of the other two expressions strictly negative as well. Thus the Hessian is negative definite on the zero-sum angle subspace, and the only zero mode corresponds to common rotation. The second-derivative test proves strict local maximality modulo this rotation.

## Verification

`VERIFY.py` is standalone Python 3 code using only the standard library. It computes 4-by-4 determinants independently by the 24-term permutation formula, compares every ordered pair of disjoint cyclic edges for \(n=5,6,7,8,9,10,11,12,15,20,32\) against (5), and checks all total volumes against (1). It builds the seven-dimensional angular Hessian by *exact integer cyclotomic coefficient arithmetic*, verifies all 49 symmetry/circulant relations and the four algebraic Fourier eigenpolynomials, and compares all seven distinct first-row Hessian entries with central finite differences of the geometric volume expression.

Execution result: `PASS: 11 complete ordered-facet determinant sweeps ... exact heptagonal Hessian coefficients and symmetry, seven numerical Hessian entry comparisons.` The finite checks are not used to replace either the all-\(n\) proof or the exact algebraic sign argument.

## Relationship to prior work

Medgyes [1, Theorem 4.1 and Remark 4.4] proves the universal upper bound \(2/5\) for **all** sphere-inscribed seven-vertex cyclic four-polytopes and reports a numerical best near \(0.3891\), without claiming sharpness. The exact value (3) provides an analytic lower benchmark consistent with that number, while (4) proves local optimality only within the narrower seven-angle trigonometric family. Neither finding improves the published general upper bound. Olarte and Santos [2, Section 2.3] define the equally spaced trigonometric cyclic configuration and its combinatorial equivalence to ordinary cyclic polytopes but do not state (1)–(4). Sanyal, Sottile and Sturmfels [3, Section 5] analyze continuous Carathéodory orbitopes and their face structure, rather than these discrete Euclidean four-volumes and their heptagonal Hessian. These distinctions concern mathematical implications, not titles. Searches also checked alternate descriptions as finite cyclic orbitopes, regular trigonometric moment-curve polytopes, and Fourier moment polytopes; no dominating statement was identified, but historical priority cannot be established exhaustively.

## Limitations

The strict-local-maximality theorem is **not** a proof that the regular configuration maximizes volume among all cyclic seven-vertex polytopes, all seven-tuples on the unit sphere, or even globally among all seven-angle choices on the trigonometric curve. The numerical proximity of (3) to the best reported value in [1] is suggestive only. Formula (1) concerns the specified normalized first/second-harmonic sampling curve; it is not asserted for arbitrary cyclic combinatorial realizations. The exact Hessian calculation gives local second-order control, not a global stability constant. Historical originality remains provisional, especially against potentially unindexed earlier calculations of discrete trigonometric orbitopes.

## References

[1] C. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886 (first publicly available 2026-10-12), especially Sections 2.3 and 4, Theorem 4.1 and Remark 4.4. https://arxiv.org/abs/2610.26886

[2] J. A. Olarte and F. Santos, *Hypersimplicial subdivisions*, Selecta Mathematica 28, article 4 (2022), first online 2021-11-03, Section 2.3. https://doi.org/10.1007/s00029-021-00722-6

[3] R. Sanyal, F. Sottile and B. Sturmfels, *Orbitopes*, Mathematika 57 (2011), Section 5. https://franksottile.github.io/research/pdf/Orbitope.pdf
