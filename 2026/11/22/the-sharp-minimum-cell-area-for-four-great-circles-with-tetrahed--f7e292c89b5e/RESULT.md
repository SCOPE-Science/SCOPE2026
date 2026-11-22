# The sharp minimum-cell area for four great circles, with tetrahedral rigidity

## Finding
For four distinct great circles in general position on the unit sphere \(S^2\), write \(m(\mathcal A)\) for the smallest spherical area among the fourteen cells of their arrangement. Then
\[
\boxed{\sup_{\mathcal A}m(\mathcal A)=2\pi-3\arccos(-1/3)
=3\arccos(1/3)-\pi=0.551285598432530\ldots.}
\]
The supremum is attained if and only if, after independently choosing the orientations of the four circle normals, the normals are vertices of a regular tetrahedron. Thus the maximizing *unoriented* four-circle arrangement is unique up to orthogonal isometry and relabeling. At that arrangement exactly eight cells are spherical triangles with the displayed area, and the six remaining cells are spherical quadrilaterals of area \(4\arccos(-1/3)-2\pi\).

## Assumptions and scope
The sphere is the unit sphere in \(\mathbb R^3\) with intrinsic spherical area in steradians. The four great circles are distinct and no three intersect at a common point. Equivalently, any three of their unit normal vectors are linearly independent. An arrangement is an unordered set of *unoriented* great circles, so changing signs of normals does not change the configuration. Cells mean closures of connected components of the complement; their boundary areas are zero. This is the exact case \(n=4\) of the minimum-cell quantity \(H(n)\) defined by Bhowmick, and it does not assert a formula for larger \(n\), the asymptotic conjecture, or the maximal-cell ratio.

## Proof
**1. Orienting the normals and counting cells.** Choose unit normals \(v_1,\ldots,v_4\) of the circles. By the general-position assumption, the \(3\times4\) matrix with columns \(v_i\) has rank three, and its one-dimensional kernel has a generator all of whose coordinates are nonzero. Change the signs of selected \(v_i\) so that
\[
 a_1v_1+a_2v_2+a_3v_3+a_4v_4=0,\qquad a_i>0.
\]
The linear map \(u\mapsto(v_i\cdot u)_{i=1}^{4}\) identifies \(\mathbb R^3\) with the hyperplane \(\{z\in\mathbb R^4:\sum_i a_i z_i=0\}\). This hyperplane meets the interior of each mixed-sign orthant and of no all-positive or all-negative orthant. Therefore the four circles have exactly fourteen nonempty cells, one for each mixed-sign pattern. Eight patterns have one sign opposed to the other three, and produce triangular cells; the remaining six have two positive and two negative signs, producing quadrilaterals. In a one-versus-three pattern, the inequality imposed by the singleton sign follows from the other three via the positive linear dependence.

The origin lies strictly inside the tetrahedron \(T=\operatorname{conv}\{v_1,v_2,v_3,v_4\}\). Its four planar triangular facets, radially projected from the origin to the sphere, form four ordinary geodesically convex spherical triangles \(F_i\), where \(F_i\) is spanned by the three \(v_j\) with \(j\ne i\). Their interiors are disjoint and their union is \(S^2\). In particular,
\[
\sum_{i=1}^4\operatorname{area}(F_i)=4\pi.
\tag{1}
\]

**2. Spherical polarity converts a cell area into a perimeter.** Let \(p_i\) denote the spherical perimeter of \(F_i\), measured using shorter great-circle arcs. The triangle cell with sign positive at \(i\) and negative at the other three indices is
\[
 C_i=\{u\in S^2:v_j\cdot u\le0\ (j\ne i)\}.
\]
This is the spherical polar of \(F_i\) (with the nonpositive sign convention). At the vertex of \(C_i\) where the boundaries corresponding to \(v_j\) and \(v_k\) meet, its interior angle is \(\pi-\arccos(v_j\cdot v_k)\). Girard's spherical excess formula gives
\[
\operatorname{area}(C_i)=2\pi-p_i.
\tag{2}
\]
The antipodal triangular cell has the same area. In particular, \(m(\mathcal A)\le\min_i(2\pi-p_i)\).

**3. Sharp triangle area-perimeter inequality.** A nondegenerate geodesically convex spherical triangle has side lengths \(a,b,c\in(0,\pi)\), perimeter \(2s=a+b+c<2\pi\), and spherical area \(E\in(0,2\pi)\). We prove, including equality, that at any fixed perimeter its area is maximized uniquely by an equilateral spherical triangle.

Set \(x=s-a\), \(y=s-b\), \(z=s-c\), so \(x,y,z>0\) and \(x+y+z=s<\pi\). L'Huilier's identity states
\[
\tan^2(E/4)=\tan(s/2)\tan(x/2)\tan(y/2)\tan(z/2).
\tag{3}
\]
At a fixed sum \(t=x+y<\pi\), the elementary identity
\[
\tan(x/2)\tan(y/2)=
\frac{\cos((x-y)/2)-\cos(t/2)}{\cos((x-y)/2)+\cos(t/2)}
\tag{4}
\]
shows that this product is strictly increased by averaging unequal \(x,y\), since \(\cos(t/2)>0\). The product of the three tangents is continuous on the closed simplex \(x,y,z\ge0\), vanishes on its boundary, and is positive inside. At its maximum all coordinates must be equal, by (4) applied to any unequal pair. Since \(\tan(E/4)\) is strictly increasing for \(0<E<2\pi\), this establishes the sharp triangle inequality and its equality condition without appealing to an unverified general polygonal inequality.

For an equilateral spherical triangle of side length \(\ell\), the spherical cosine law gives its interior angle \(\arccos(\cos\ell/(1+\cos\ell))\), and hence its area
\[
E_{\mathrm{eq}}(\ell)
=3\arccos\!\left(\frac{\cos\ell}{1+\cos\ell}\right)-\pi.
\tag{5}
\]
The function in (5) is strictly increasing on \(0<\ell<2\pi/3\). Put \(\alpha=\arccos(-1/3)\), so \(\alpha<2\pi/3\), and note that \(\cos\alpha/(1+\cos\alpha)=-1/2\), yielding \(E_{\mathrm{eq}}(\alpha)=\pi\). It follows that any spherical triangle with area at least \(\pi\) has perimeter at least \(3\alpha\), with equality if and only if it is equilateral with all sides \(\alpha\).

**4. Sharp bound and equality.** By (1) some \(F_i\) has area at least \(\pi\). The sharp triangle inequality applied to that face gives \(p_i\ge3\alpha\), and (2) therefore implies
\[
 m(\mathcal A)\le2\pi-3\alpha.
\tag{6}
\]
If equality holds in (6), then every triangular cell has area at least \(2\pi-3\alpha\); by (2), every \(p_i\le3\alpha\). Applying the triangle inequality to every \(F_i\) gives \(\operatorname{area}(F_i)\le\pi\), with equality only for an equilateral face having sides \(\alpha\). Since their areas sum to \(4\pi\), all four faces must satisfy equality. Thus every pair of distinct normals has angular separation \(\alpha\), or \(v_i\cdot v_j=-1/3\). This Gram matrix determines the regular tetrahedron up to an orthogonal transformation, proving uniqueness modulo circle orientations and relabeling.

Conversely take the four unit tetrahedral vectors \((1,1,1)/\sqrt3\), \((1,-1,-1)/\sqrt3\), \((-1,1,-1)/\sqrt3\), \((-1,-1,1)/\sqrt3\). Every pair makes angle \(\alpha\). By (2), the eight triangular cells have area \(T_0=2\pi-3\alpha\). The symmetry group permutes the six remaining quadrilaterals transitively, so they have common area
\[
Q_0=\frac{4\pi-8T_0}{6}=4\alpha-2\pi.
\]
Here \(\alpha>3\pi/5>4\pi/7\): the first comparison follows from \(\cos(3\pi/5)=(1-\sqrt5)/4>-1/3\). Consequently \(Q_0-T_0=7\alpha-4\pi>0\), and the smallest cell is indeed triangular with area \(T_0\). This proves attainment and the claimed complete optimizer classification.

## Verification
Run `python3 check_four_circles.py` with the Python 3 standard library. The checker independently reconstructs all spherical sign cells from hemisphere intersection vertices, calculates their areas using spherical solid-angle determinants, validates the complete tetrahedral 8-triangle/6-quadrilateral decomposition, and tests the polar-face identity and the l'Huilier averaging inequality. A deterministic execution passed 541 generic arrangements with 14 cells each and 3,000 pair-smoothing comparisons. The exact equality formula is certified by the analytic proof; finite sampling and numerical tolerance are not substitute proofs of optimality or rigidity.

## Relationship to prior work
Bhowmick (2026, arXiv:2611.15244v1) explicitly defines \(H(n)\) and proves an improved asymptotic upper bound for large \(n\). Its full introduction, the proof of the small-cell theorem and the remaining sections do not state the finite four-circle optimum or its rigidity. Bezdek and Lángi (2022 preprint, 2024 journal) analyze four-circle arrangements in the context of the *minimum spherical inradius* and prove a corresponding inradius theorem, but that statistic is not the smallest **area** and their classification does not imply (6). Published studies of four equal spherical caps at tetrahedral centers determine covering thresholds and multiplicity areas, which can yield the *tetrahedral example's* individual cell measures but not optimality over all four-circle arrangements. The novel claim here is the exact universal maximin area and its uniqueness, not the regular-tetrahedron angular identities or the classical spherical triangle isoperimetric theorem.

## Limitations
This result assumes exactly four distinct great circles with no triple concurrence. Degenerate arrangements, distributions of random arrangements, and larger orders are not classified. The numerical checker only tests finite examples; the infinite assertion comes from (1)–(6). Historical priority remains provisional: exhaustive indexing of all classical spherical tilings and unpublished notes is impossible, and independent mathematical validation has not been performed.

## References
1. K. Bhowmick, *Small cells in arrangements of great circles*, arXiv:2611.15244v1, first posted 2026-11-11, https://arxiv.org/html/2611.15244v1.
2. K. Bezdek and Z. Lángi, *From the separable Tammes problem to extremal distributions of great circles in the unit sphere*, arXiv:2201.11234v3 (2022); *Discrete & Computational Geometry* 72 (2024), 269–309, https://arxiv.org/abs/2201.11234.
3. E. W. Weisstein, *L'Huilier's Theorem*, MathWorld, https://mathworld.wolfram.com/LHuiliersTheorem.html; standard identity is also proved in R. A. Johnson's notes, *Spherical Triangular Area*, https://www.math.ucla.edu/~robjohn/math/spheretrig.pdf.
4. *Exact coverage multiplicities and dual contact exponents of tetrahedral spherical caps*, publicly archived result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-coverage-multiplicities-and-dual-contact-exponents-of-tetr--b1ad9ef47248.
