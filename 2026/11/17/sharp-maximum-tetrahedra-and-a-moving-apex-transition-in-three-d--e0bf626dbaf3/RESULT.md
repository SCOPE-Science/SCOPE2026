# Sharp maximum tetrahedra and a moving-apex transition in three-dimensional generalized parking-function polytopes

## Finding
Let \(b_1,b_2,b_3\) be positive integers and let \(P\subset\mathbb R^3\) be the convex hull of the \((b_1,b_2,b_3)\)-parking functions, as defined in Bayer et al. [1]: a positive integral triple belongs to the defining set if, after increasing rearrangement, its \(i\)-th entry is at most \(S_i=\sum_{j=1}^i b_j\). Define
\[
C=b_1-1\ge0,\quad d=b_2>0,\quad e=b_3>0,\quad A=C+d=S_2-1,\quad B=A+e=S_3-1.
\]
The largest ordinary Euclidean volume of a tetrahedron contained in \(P\), with its corners allowed anywhere in \(P\), is
\[
\boxed{V_{\max}(P)=\frac16\max\{A^3+B^3,\;B^2(C+A)\}.}
\]
Write \(\Delta=A^3+B^3-B^2(C+A)\). The complete equality classification is as follows.

If \(\Delta>0\), there are precisely **two rigid** maximizing tetrahedra: the common corner \((1,1,1)\) together with one of the two three-element alternating-permutation classes of \((1,S_2,S_3)\). If \(\Delta<0\), every maximizing tetrahedron has the fixed triangular base consisting of the three permutations of \((1,1,S_3)\), and its fourth corner may be **any point** of the hexagonal permutahedral face
\[
F=\operatorname{conv}\{\sigma(S_1,S_2,S_3):\sigma\in\mathfrak S_3\}.
\]
At \(\Delta=0\), exactly both described families maximize. In the second regime there are six vertex-supported maximizers and a two-dimensional continuous family; in the first, exactly two vertex-supported maximizers and no nonvertex ones. At equality there are eight vertex-supported maximizers and the continuous family.

There is one sharp transition. Exactly,
\[
\Delta=(d-e)C^2+(2d^2+e^2)C+d^3+d^2e+2de^2+e^3.
\]
For \(e\le d\), necessarily \(\Delta>0\) for every \(C\ge0\). For \(e>d\), the sign changes exactly once, at
\[
\boxed{C_* =\frac{2d^2+e^2+\sqrt{(2d^2+e^2)^2+4(e-d)(d^3+d^2e+2de^2+e^3)}}{2(e-d)}.}
\]
Thus \(C<C_*\) gives the two rigid optimizers, \(C>C_*\) gives the movable-apex family, and \(C=C_*\), if attained by an integral input, gives both. The formulas also hold for the three-parameter convex-hull family with arbitrary real \(C\ge0,d,e>0\).

## Assumptions and scope
The metric is the standard Euclidean metric in the original coordinate realization; tetrahedral volume is ordinary three-dimensional Lebesgue volume, with no requirement that its corners be original vertices. The source vertex theorem [1, Theorem 2.3] says that after translation by \((-1,-1,-1)\), the vertex candidate set is precisely the permutations of
\[
(0,0,0),\quad(0,0,B),\quad(0,A,B),\quad(C,A,B).
\]
There are sixteen different vertices for \(C>0\), and ten for \(C=0\); the last two permutation classes coincide when \(C=0\). The proof below uses this published description as its only source-specific premise.

## Proof
**Vertex reduction.** For four points \(z_0,z_1,z_2,z_3\in P\), six times the oriented volume is \(\det(z_1-z_0,z_2-z_0,z_3-z_0)\). In homogeneous coordinates \((1,z_i)\), this is affine in each corner separately. Expressing each corner as a convex combination of polytope vertices proves that the maximal absolute determinant is attained by a vertex quadruple.

**Two attaining configurations.** Translate by \((-1,-1,-1)\). The three vertices in either alternating permutation class of \((0,A,B)\), with the origin as fourth corner, give absolute determinant \(T_1=A^3+B^3\). The three axial vertices \(Be_1,Be_2,Be_3\), with any one permutation of \((C,A,B)\) as fourth corner, give absolute determinant \(T_2=B^2(C+A)\): the base plane has coordinate sum \(B\), and the fourth point has coordinate sum \(C+A+B\).

**Universal exact upper bound.** There are \(\binom{16}{4}=1820\) quadruples of distinct symbolic vertices for \(C>0\). The standalone `verify.py` in this package constructs each oriented determinant as an integer-coefficient homogeneous cubic polynomial in \((C,d,e)\), without floating-point calculations. Exactly two quadruples have determinant \(\pm T_1\), and exactly six (the axial base with one of six top permutations) have determinant \(\pm T_2\). For *each other* quadruple, **both** polynomials \(T_1-\det\) and \(T_1+\det\) have nonnegative coefficients in \(C,d,e\) and are not identically zero. This exhaustive polynomial-identity certificate establishes \(|\det|<T_1\) whenever \(C,d,e>0\), hence the claimed maximum \(\max\{T_1,T_2\}\) without any sampling assumption. For \(C=0\), the checker additionally shows symbolically that any equality candidate from the other quadruples collapses, upon identifying the duplicated vertices, to one of the two specified \(T_1\) quadruples; all remaining candidates have a strictly positive polynomial gap in \(d,e\). Thus the same maximum and equality classification hold at the boundary. The enumerated certificate is independently inspectable in the complete Python source and requires only the standard library.

**Nonvertex equality.** Expanding the oriented determinant into convex combinations of four vertex decompositions yields a convex average of signed vertex determinants. If this average has maximal absolute value, every term with positive weight has the same maximal oriented determinant. Consequently, if any corner admits a nontrivial vertex decomposition, then two distinct maximizing vertex quadruples must agree at the other three vertices. When \(T_1>T_2\), the two maximizing quadruples share only the origin; hence no nonvertex maximizing corner exists. When \(T_2>T_1\), the six maximizing quadruples share exactly the same three axial vertices and differ only in their top corner; therefore every maximizing tetrahedron uses those three axial vertices and a point of their top-vertex convex hull \(F\). Conversely every apex in \(F\) works because its coordinate sum is constant. At \(T_1=T_2\), there are two additional isolated \(T_1\) quadruples; neither has three vertices in common with any axial quadruple, so these and the same movable-apex family exhaust all optimizers.

**Single transition.** Expanding \(T_1-T_2\) yields the displayed quadratic in \(C\). When \(e\le d\), every coefficient is nonnegative and the constant coefficient is positive. When \(e>d\), the quadratic is strictly concave, positive at zero and negative for sufficiently large \(C\). Its two roots have opposite signs, so the positive root \(C_*\) is unique and given by the quadratic formula. This completes the all-parameter proof.

## Verification
Run `python3 verify.py` (Python standard library only). The checker regenerates all sixteen symbolic vertices and all 1,820 tetrahedra, verifies the six and two attaining polynomial identities, and proves coefficientwise positivity for every signed determinant in the other 1,812 quadruples. It checks the special \(C=0\) coincidences symbolically and independently enumerates seventy-two integer parameter triples, including cases deep in the movable-apex regime. The successful replay printed `PARKING_TETRA_EXACT_PASS symbolic_quadruples=1820 coefficientwise=1812 rigid=2 facet=6 sample_parameter_triples=72 zero_first_checks=5`. The symbolic certificate verifies the arbitrary-real parameter inequalities; the finite parameter examples are corroboration rather than a substitute for that certificate.

## Relationship to prior work
Bayer et al. [1] give the complete vertex and face structure of all generalized parking-function polytopes, and study their graph/circuit diameters, not maximum-volume inscribed tetrahedra. The earlier Hanada–Lentfer–Vindas-Meléndez work [2] provides total volume formulas for the special two-parameter subclass; total polytope volume does not determine the largest contained simplex. Both open-access primary texts were checked for tetrahedral extremal statements, with no covering statement found. Liu and Thawinrak [3] treat broader normal fans, faces, and Ehrhart/volume data in related parking-function polytope families; their abstract does not assert the present contained-tetrahedron optimum. The previously published exact asymmetric-simplex-difference-body tetrahedral theorem [4] concerns a different twelve-vertex Minkowski-sum body, not the present sixteen-vertex family; the maxima have different optimizer structures and there is no evident affine equivalence or logical implication.

## Limitations
The original mathematical result concerns the natural three-dimensional family (the first dimension of full-dimensional tetrahedral optimization). It does not assert an analogue in dimension four or higher, nor characterize next-largest nonmaximal tetrahedral volumes. The polynomial checker is an exhaustive transparent exact-arithmetic certificate, not an independent formal proof assistant. An unindexed historical source may still cover an equivalent statement; independent audit has not yet been performed.

## References
1. M. M. Bayer, S. Borgwardt, T. Chambers et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first posted 2024-03-12; DOI 10.1007/s00454-025-00770-1. Source and full text: https://arxiv.org/abs/2403.07387 and https://link.springer.com/article/10.1007/s00454-025-00770-1.
2. M. Hanada, J. Lentfer, A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, arXiv:2212.06885, first posted 2022-12-13; DOI 10.1007/s00026-023-00671-1. Full text: https://link.springer.com/article/10.1007/s00026-023-00671-1.
3. F. Liu, W. Thawinrak, *Parking Function Polytopes*, arXiv:2512.14199, first posted 2025-12-16. Abstract: https://arxiv.org/abs/2512.14199.
4. *Sharp inscribed-tetrahedron law for three-dimensional asymmetric simplex difference bodies*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-inscribed-tetrahedron-law-for-three-dimensional-asymmetric--16ed3ed4444b.
