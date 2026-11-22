# Sharp maximin cell perimeter for four great circles, with a disphenoid equality region

## Finding

Let \(\mathcal A\) be any four distinct great circles on the unit sphere \(S^2\), no three concurrent, and let \(p(C)\) denote the geodesic boundary perimeter of a cell. Then
\[
\max_{\mathcal A}\min_{C\in\mathcal C(\mathcal A)}p(C)=\pi.
\]
All maximizers, up to orthogonal isometry and relabeling of the *unoriented* circles, have unit normal vectors
\[
\begin{split}
\nu_1&=(a,b,c),&\nu_2&=(a,-b,-c),\\
\nu_3&=(-a,b,-c),&\nu_4&=(-a,-b,c),
\end{split}
\]
where
\[
a,b,c>0,\quad a^2+b^2+c^2=1,\quad bc\le a,\quad ac\le b,\quad ab\le c.
\]
The last three inequalities are both necessary and sufficient. In particular, the maximizer is **not rigid**: a nonempty two-dimensional open region of noncongruent arrangements attains the sharp bound.

More precisely, for all positive \(a,b,c\) with \(a^2+b^2+c^2=1\), this normal family has eight spherical triangular cells, each of perimeter \(\pi\), and six quadrilateral cells in three antipodal pairs, with perimeters
\[
q_a=2\pi-4\arctan\frac{bc}{a},\quad
q_b=2\pi-4\arctan\frac{ac}{b},\quad
q_c=2\pi-4\arctan\frac{ab}{c}.
\]
Consequently its smallest perimeter is exactly \(\min\{\pi,q_a,q_b,q_c\}\). At \(a=b=c=1/\sqrt3\), all six quadrilaterals have perimeter \(4\pi/3\), while the triangular cells have perimeter \(\pi\).

## Assumptions and scope

The sphere has radius one. Every circle is a plane through the origin intersected with \(S^2\); different normals \(\nu\) and \(-\nu\) define the same circle. No three circles are concurrent, equivalently every three of the four normals are linearly independent. Boundary length counts each shortest great-circle edge arc once, with the usual arclength metric. There is no assumption of symmetry or genericity beyond nonconcurrency. The equality inequalities are non-strict, so the boundary of the optimizing parameter region is included.

## Proof

**1. Cell combinatorics and the sharp upper bound.** Fix any unit normal to each circle. The unique linear dependence among the four normals has all four coefficients nonzero: otherwise some three normals would be dependent. Independently reverse signs to obtain normals \(\nu_i\) and positive coefficients \(\lambda_i\) with \(\sum_i\lambda_i\nu_i=0\). Exactly the fourteen mixed sign patterns for the four scalar products \(x\cdot\nu_i\) occur as open cells. Indeed, both constant-sign patterns are forbidden by the dependence. Every mixed pattern is feasible by the Gordan alternative: if it were not, there would be a nonzero nonnegative linear dependence among its signed normals, contradicting uniqueness and the positivity of the original dependence. For a pattern with one sign differing from the other three, its singleton inequality follows from the remaining three, so the cell is a triangle. For a two-and-two pattern all four sides are present: changing any one sign produces an adjacent feasible three-and-one pattern. Thus eight cells are triangles and six are quadrilaterals; every edge separates one triangle from one quadrilateral. The sum of the eight triangular perimeters is therefore the total arclength of the four circles, \(4(2\pi)=8\pi\). Some triangle has perimeter at most \(\pi\). Hence \(\min_C p(C)\le\pi\) universally.

**2. Equality forces an orthogonal disphenoid normal tetrahedron.** Suppose \(\min_C p(C)=\pi\). Since the eight triangular perimeters sum to \(8\pi\), all are \(\pi\). For a convex spherical polygon \(P\) and its polar polygon \(P^\circ\), the spherical-angle relations and Girard's area formula give
\[
\operatorname{area}(P^\circ)=2\pi-p(P).
\]
The triangle with sign pattern having the \(i\)-th sign opposite to the other three has polar equal, up to antipodal reflection, to the spherical triangle spanned by \(\{\nu_j:j\ne i\}\). Thus each of the four triples of normal vectors spans a spherical triangle of area \(\pi\).

For independent unit vectors \(u,v,w\), the area \(\Omega\in(0,2\pi)\) of their shorter spherical-convex triangle satisfies the exact solid-angle identity
\[
\Omega=2\operatorname{atan2}\!\left(|\det(u,v,w)|,\;1+u\cdot v+v\cdot w+w\cdot u\right).
\]
It follows that \(\Omega=\pi\) precisely when the second argument of \(\operatorname{atan2}\) is zero. Write \(g_{ij}=\nu_i\cdot\nu_j\). Applying this to the four triples gives
\[
\begin{aligned}
1+g_{12}+g_{13}+g_{23}&=0,&1+g_{12}+g_{14}+g_{24}&=0,\\
1+g_{13}+g_{14}+g_{34}&=0,&1+g_{23}+g_{24}+g_{34}&=0.
\end{aligned}
\]
Solving yields \(g_{12}=g_{34}\), \(g_{13}=g_{24}\), \(g_{14}=g_{23}\) and \(g_{12}+g_{13}+g_{14}=-1\). Define
\[
a=\sqrt{\frac{1+g_{12}}2},\qquad b=\sqrt{\frac{1+g_{13}}2},\qquad c=\sqrt{\frac{1+g_{14}}2}.
\]
Because the circles are distinct, \(a,b,c>0\); the sum identity implies \(a^2+b^2+c^2=1\). The Gram matrix of the four normals equals the Gram matrix of the four displayed sign vectors. Since the vectors span \(\mathbb R^3\), the two configurations are related by an orthogonal transformation. Thus every equality arrangement has the stated disphenoid form. Conversely that form has equal opposite Gram entries with the required sum, so each of its eight triangular perimeters is exactly \(\pi\).

**3. The six quadrilateral perimeters.** Consider the cell with signs \((+,+,-,-)\). Its polar is the spherical convex quadrilateral with vertices \(\nu_1,\nu_2,-\nu_3,-\nu_4\), which are exactly the radial projections of the four corners \((a,\pm b,\pm c)\) of a rectangle in the plane with first coordinate \(a>0\). In the chart \((1,s,t)/\sqrt{1+s^2+t^2}\), the spherical area element is \((1+s^2+t^2)^{-3/2}\,ds\,dt\). Integrating over \([-b/a,b/a]\times[-c/a,c/a]\) gives
\[
\operatorname{area}(P^\circ)=4\arctan\frac{bc}{a},
\]
using \(a^2+b^2+c^2=1\). The polar perimeter identity therefore gives \(q_a=2\pi-4\arctan(bc/a)\). The two other pair partitions give \(q_b\) and \(q_c\); antipodal cells have equal perimeter. Consequently all cells have perimeter at least \(\pi\) exactly when \(bc\le a\), \(ac\le b\), and \(ab\le c\). This proves both sufficiency and necessity, and the exact full-family profile.

**4. Attainment and non-rigidity.** At \(a=b=c=1/\sqrt3\), the three inequalities are strict and \(q_a=q_b=q_c=4\pi/3\). Strict inequalities persist on a neighborhood in the positive sphere octant, giving an open two-dimensional family of maximizers. Distinct unordered triples \(\{a,b,c\}\) in that neighborhood have different normal Gram data, hence need not be congruent. The maximum is attained, so the displayed supremum is a maximum.

## Verification

Run the accompanying standard-library program with `python3 check_perimeter.py`. It reconstructs cells independently by intersecting signed great-circle hemispheres, orders their vertices on the sphere and sums their geodesic edge lengths. In a deterministic sample of 500 normalized disphenoid configurations it checks the eight triangular perimeters, six quadrilateral perimeters, exact three-formula profile and optimizer inequalities. In 400 additional nonsymmetric generic configurations it verifies the fourteen-cell census, the triangular perimeter sum and the universal upper bound. All 900 tests passed. These floating-point tests are corroborative; the infinite statements and exact equality classification follow from the analytic proof above.

## Relationship to prior work

Bhowmick (2026) studies the **area** of cells in arbitrary great-circle arrangements and uses total perimeter and side-count identities to bound the smallest area for large numbers of circles; it does not state this sharp four-circle maximin **perimeter** result or its non-rigid complete equality region. Bezdek and Lángi (2022, journal 2024) analyze **inradius** and **circumradius** extrema of four-circle arrangements, including their eight-triangle/six-quadrilateral cell census, but their resulting extremal configurations and objectives differ. The incidence combinatorics and spherical polar identities are standard and are used as inputs, not claimed as new. Van Oosterom and Strackee's solid-angle formula supplies a convenient exact characterization of the equal-perimeter condition. The contribution claimed here is the sharp perimeter problem together with its exhaustive two-parameter equality classification and exact quadrilateral profile.

## Limitations

The theorem assumes nonconcurrency of every three circles; degenerate arrangements are not classified. It concerns geodesic perimeter, not spherical area, cell inradius, circumradius or Euclidean chord perimeter. It does not assert the sharp value for other numbers of circles. The historical novelty assessment is based on the inspected and searched sources, and is not a guarantee against unindexed older work. Independent proof audit has not been performed.

## References

1. K. Bhowmick, *Small cells in arrangements of great circles*, arXiv:2611.15244v1, publicly posted 2026-11-11. https://arxiv.org/html/2611.15244v1
2. K. Bezdek and Z. Lángi, *From the separable Tammes problem to extremal distributions of great circles in the unit sphere*, arXiv:2201.11234 (2022); *Discrete & Computational Geometry* 72 (2024), 269–309. https://arxiv.org/abs/2201.11234
3. A. van Oosterom and J. Strackee, *The solid angle of a plane triangle*, *IEEE Transactions on Biomedical Engineering* 30 (1983), 125–126. https://doi.org/10.1109/TBME.1983.325207
