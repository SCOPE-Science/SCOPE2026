# Sharp affine-invariant Wachspress denominator range for centrally symmetric hexagons

## Finding

For a nondegenerate centrally symmetric convex hexagon \(P\), let \(q_P\) be the Wachspress polynomial denominator (adjoint), normalized with positive sign throughout \(P\). Only positive rescalings are considered, so define the *denominator-range invariant*
\[
\mathcal K(P)=\frac{\max_{z\in P}q_P(z)}{\min_{z\in P}q_P(z)}.
\]
The value does not depend on the overall scaling of \(q_P\) and is invariant under invertible affine transformations. Its complete sharp range is
\[
\boxed{\mathcal K(P)\in[3/2,\infty),\qquad
\mathcal K(P)=3/2\ \Longleftrightarrow\ P\text{ is affine-regular}.}
\]
Every such hexagon admits the affine form
\[
P_{a,b}=\{(x,y): |x|\le1,\ |y|\le1,\ |ax+by|\le1\},
\quad a,b>0,\quad a+b>1,\quad |a-b|<1.
\]
Put \(\alpha=a+b-1\), \(\beta=1+b-a\), \(\gamma=1+a-b\), and sort these three positive parameters as \(0<u\le v\le w\). The exact profile and a quantitative rigidity identity are
\[
\boxed{\mathcal K(P_{a,b})=\frac{(u+v+w)(u+v)}{4uv},\qquad
\mathcal K(P_{a,b})-\frac32=
\frac{(v-u)(2v-u)+(w-v)(u+v)}{4uv}.}
\]
The unique denominator maximum is at the symmetry center. Every denominator minimum is a vertex, and its minimizing opposite vertex pairs are exactly those indexed by the two smallest of \(\alpha,\beta,\gamma\), accounting for ties. This identifies precisely when the minimizing vertex pair changes as the hexagon is sheared.

## Assumptions and scope

A hexagon is called nondegenerate here when it is full-dimensional and has six genuine sides, no consecutive collinear sides. A centrally symmetric hexagon is an intersection of three pairs of parallel supporting half-planes. Translate its center to the origin, choose two independent support functionals as affine coordinates, and choose signs so the third is a positive linear combination of those two. After dividing by the three support numbers, this gives exactly the form \(P_{a,b}\) above. The three pairs of strips are all active precisely when \(a+b>1\) and \(|a-b|<1\); together with \(a,b>0\), these inequalities describe the genuine hexagons.

The Wachspress system has vertex weights
\[
w_j(z)=\det(n_{j-1},n_j)\prod_{k\notin\{j-1,j\}}\ell_k(z),\qquad
q_P(z)=\sum_{j=0}^{5}w_j(z),
\]
where the six nonnegative facet slacks \(\ell_j\) and their outward normals \(n_j\) are cyclically ordered. All determinants are positive in this order. Multiplying any slack by a positive constant multiplies every \(w_j\) by one common positive constant. A nonsingular affine coordinate change likewise rescales the six weights uniformly. Thus the ratio is an intrinsic invariant of these Wachspress coordinates, not a choice of facet normalization. The quadratic adjoint cannot be canceled from every numerator, since its quadratic part has positive rank two while each numerator is a product of linear forms.

## Proof

**1. An exact quadratic denominator.** For the canonical form take the facet slacks in cyclic order
\[
\ell=(1-x,\ 1-ax-by,\ 1-y,\ 1+x,\ 1+ax+by,\ 1+y).
\]
The corresponding outward normals are
\[
 n=((1,0),(a,b),(0,1),(-1,0),(-a,-b),(0,-1)),
\]
whose six adjacent determinants, in the indicated cyclic order, are \(1,b,a,1,b,a\). Form the six quartic Wachspress vertex weights as defined above, and add them. Direct expansion, or pairing opposite vertices before expansion, gives the polynomial identity
\[
\boxed{q(x,y)=2\big[(1+a+b)-a(1+a-b)x^2
 -(1-(a-b)^2)xy-b(1+b-a)y^2\big].}
\]
The quadratic penalty has strictly positive leading principal minors because \(a(1+a-b)>0\) and
\[
4a(1+a-b)b(1+b-a)-(1-(a-b)^2)^2
=(1+a+b)(a+b-1)(1+a-b)(1-a+b)>0.
\]
Therefore \(q\) is strictly concave. Its unique maximum on \(P_{a,b}\) is at \((0,0)\), and equals \(2(1+a+b)\). The sum-of-positive-Wachspress-weights representation gives \(q>0\) throughout the closed polygon.

**2. Every minimum is at a vertex.** Strict concavity ensures that any nonvertex point on a line segment between distinct polygon points has strictly greater \(q\) value than at least one endpoint. Hence a minimum occurs only among the six vertices. Three consecutive vertices (the other three are antipodes) can be chosen as
\[
(1,-1),\quad \left(1,\frac{1-a}{b}\right),\quad
\left(\frac{1-b}{a},1\right).
\]
With \(\alpha=a+b-1\), \(\beta=1+b-a\) and \(\gamma=1+a-b\), substitution into the explicit quadratic yields respectively
\[
\frac{8\beta\gamma}{\beta+\gamma},\qquad
\frac{8\alpha\beta}{\alpha+\beta},\qquad
\frac{8\alpha\gamma}{\alpha+\gamma}.
\]
Each occurs at an opposite pair. These are positive because all three gap parameters are positive, and \(\alpha+\beta+\gamma=1+a+b\).

**3. Exact profile and stability.** The harmonic-pair function \(H(r,s)=rs/(r+s)\) is strictly increasing in both positive variables. Thus for the three gap parameters ordered as \(0<u\le v\le w\), the smallest vertex value is exactly \(8uv/(u+v)\). Dividing the center value \(2(u+v+w)\) by that minimum yields
\[
\mathcal K(P)=\frac{(u+v+w)(u+v)}{4uv}.
\]
An exact rearrangement gives
\[
4uv\big(\mathcal K(P)-3/2\big)
=(v-u)(2v-u)+(w-v)(u+v).
\]
Both terms on the right are nonnegative, and they vanish simultaneously exactly when \(u=v=w\). This equality makes \(\alpha=\beta=\gamma\), equivalently \(a=b=1\), whose six vertices form an affine-regular hexagon. This proves the sharp minimum and uniqueness up to affine equivalence. Since the harmonic-pair function is strictly increasing, ties among candidate minimum pairs occur exactly when multiple choices of the two smallest gaps are possible; no other polygon points can minimize.

**4. No finite maximum.** Along the admissible one-parameter family \(a=b=t\) with \(1/2<t\le1\), we have \(\alpha=2t-1\) and \(\beta=\gamma=1\). At \(t=1\), the ratio is \(3/2\); as \(t\downarrow1/2\), the ratio diverges to infinity. Continuity and the intermediate-value theorem give the full range \([3/2,\infty)\). The degenerate endpoint itself is excluded from the theorem.

## Verification

The standalone `verify.py` uses only Python's standard library and exact rational polynomial arithmetic. For 210 admissible rational parameter pairs on a two-parameter grid, it constructs all six Wachspress weights independently from facet slacks and normal determinants; verifies the quadratic identity, affine precision, every listed vertex value, the sharp ratio and the exact nonnegative deficit. It also checks the unique equality parameter within that grid. The analytic argument above, not those finite tests, proves the arbitrary-hexagon assertion. Run `python verify.py` in the directory containing the extracted file.

## Relationship to prior work

Baumbach and Winter (2026) investigate rational generalized barycentric coordinates, their Wachspress numerators and the degrees of adjoint denominators, motivating a study of how the denominator varies inside a polygon; their article does not state this shape-extremal pointwise ratio. Baumbach, Freyer, Weigert and Winter (2025) classify adjoint degree drops for symmetric polygons; the degree classification does not determine the magnitude of the polynomial on the polygon.

The closest indexed regular-polygon finding gives an exact factorization and denominator range for **regular polygons**, including the regular six-gon. It therefore implies the equality example \(\mathcal K=3/2\), which is acknowledged as prior work, but cannot imply the inequality and equality rigidity for **all** centrally symmetric hexagons by specializing to regular polygons. A separate all-polygon finding establishes minimum denominator degree and uniqueness at that degree, not any extrema of its values. The new content is the full affine-normalized two-parameter profile, its sharp global lower bound, quantitative deficit and minimizer transitions. CGAL's public documentation presents the polynomial Wachspress formulation and warns that near-boundary evaluation can be unstable; the present mathematical ratio is **not** claimed to be a general floating-point interpolation condition number. Searches found no prior theorem implying the joint statement, but do not constitute proof of publication priority.

## Limitations

The theorem concerns the *Wachspress polynomial denominator* and its max/min variation, **not** the behavior of arbitrary generalized barycentric systems, interpolation errors, all evaluation algorithms, or the true numerical condition number of a finite-element stiffness matrix. It does not extend the sharp inequality to nonsymmetric hexagons or polygons with more sides. Existing regular-hexagon formulas already give the equality-case value, so the contribution is the all-shapes bound and rigidity. Historical equivalents outside accessible and indexed sources cannot be excluded. No independent mathematical audit has been performed.

## References

1. T. Baumbach and M. Winter, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1 (first public 2026-11-01), https://arxiv.org/html/2611.02110v1.
2. T. Baumbach, A. Freyer, J. Weigert and M. Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes*, arXiv:2508.04275v1 (first public 2025-08-06), https://arxiv.org/html/2508.04275v1.
3. *Exact radial Wachspress adjoints, pole circles, and sharp conditioning for every regular polygon*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-radial-wachspress-adjoints-pole-circles-and-sharp-conditio--3cbb9ad8cd9b.
4. *Wachspress denominators have minimum degree on every convex polygon*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-wachspress-denominators-have-minimum-degree-on-every-convex-poly--7b4aad67706d.
5. CGAL, *2D Generalized Barycentric Coordinates: User Manual*, https://doc.cgal.org/6.1.1/Barycentric_coordinates_2/index.html.
6. A. Gillette, A. Rand, and C. Bajaj, *Error Estimates for Generalized Barycentric Interpolation* (2012), https://pmc.ncbi.nlm.nih.gov/articles/PMC3549276/.
