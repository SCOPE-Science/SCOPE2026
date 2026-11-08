# A sharp simplex-projection inball criterion for Cayley sums of boxes

## Finding

Let \(d,m\ge1\), and let \(A=(a_{ij})\in\mathbb R_{\ge0}^{m\times(d+1)}\) have no zero row. Its box-Cayley polytope is
\[
C(A)=\left\{(x,y)\in\mathbb R^m\times\mathbb R^d:
 y_j\ge0,\quad \sum_{j=1}^d y_j\le1,\quad
 0\le x_i\le a_{i0}\left(1-\sum_{j=1}^dy_j\right)+\sum_{j=1}^d a_{ij}y_j\right\}.
\]
Distances and balls are for the standard Euclidean metric on these \(m+d\) coordinates. Define
\[
\rho_d=\frac1{d+\sqrt d},\quad
H_i=\sqrt{1+\sum_{j=1}^d(a_{ij}-a_{i0})^2},\quad
B_i=\sqrt d\,a_{i0}+\sum_{j=1}^d a_{ij}.
\]
Then the following is a necessary and sufficient condition for the Euclidean inradius of \(C(A)\) to equal the projection bound \(\rho_d\):
\[
\boxed{B_i\ge 1+H_i\quad(1\le i\le m).}
\]
If the condition holds, **every** maximum-radius ball center, and no other point, is of the form
\[
\boxed{y=(\rho_d,\ldots,\rho_d),\quad
\rho_d\le x_i\le\rho_d(B_i-H_i)\quad(1\le i\le m).}
\]
Thus the complete incenter locus is a Cartesian product of \(m\) closed intervals, degenerating precisely in coordinates where \(B_i=1+H_i\). Its affine dimension is exactly the number of strict inequalities in the criterion. All \(d+1\) simplex-base hyperplanes contact each maximum ball; the two fiber hyperplanes associated with row \(i\) contact it exactly when the corresponding lower or upper endpoint of that interval is chosen (both when the interval degenerates).

**In particular**, when \(d\ge2\) and every entry of \(A\) is a positive integer, the criterion holds strictly for every row. Hence every such box-Cayley polytope has inradius \(\rho_d\), independently of \(m\) and the entries of \(A\), and its complete incenter locus is a full \(m\)-dimensional rectangular box. Ferroni proves that all such entrywise-positive integral box-Cayley polytopes are smooth; thus this radius and full center-box conclusion hold throughout that natural smooth subfamily.

For Ferroni's sparse family \(A_{\alpha,\beta}=[\alpha\mathbf1_d\mid\beta I_d]\), with \(d\ge2\) and integers \(\alpha,\beta\ge1\), the same sharp radius holds. All center intervals have common length
\[
\boxed{\ell_{d,\alpha,\beta}=\rho_d\left(\alpha\sqrt d+\beta-1-\sqrt{1+(\beta-\alpha)^2+(d-1)\alpha^2}\right).}
\]
The incenter is unique **exactly** at \((\alpha,\beta)=(1,1)\). Otherwise the incenter locus is a full \(d\)-dimensional cube of side \(\ell_{d,\alpha,\beta}>0\). At an interior center of that cube, exactly the \(d+1\) base facets are tangent; at a cube point with \(k\) coordinates at their endpoints, exactly \(d+1+k\) facets are tangent. At \((1,1)\), all \(3d+1\) fiber and base facets contact the unique maximal ball.

## Assumptions and scope

There is no hidden lattice restriction in the general criterion: \(A\) may have arbitrary nonnegative real entries, provided each row is nonzero, so that \(C(A)\) is full dimensional. The all-positive and sparse-family corollaries use integer entries. The Euclidean metric is the particular standard coordinate metric of the displayed Cayley realization, not an affine-invariant metric. The assertions classify **maximum inscribed balls**, not maximum-volume inscribed ellipsoids. Coordinates are normalized so that the projected base simplex has vertices \(0,e_1,\ldots,e_d\).

## Proof

**The Cayley representation.** For \(y\) in the standard simplex \(\Delta_d\), write its barycentric coordinates as \(\lambda_0=1-\sum_{j=1}^dy_j\) and \(\lambda_j=y_j\). The fiber of the Cayley sum of boxes \(D_j=\prod_{i=1}^m[0,a_{ij}]\) over \(y\) is their weighted Minkowski combination \(\sum_j\lambda_j D_j\), equal coordinatewise to \(\prod_i[0,\sum_j\lambda_j a_{ij}]\). This proves the defining halfspace description for all parameters.

**The universal upper bound and its equality case.** Orthogonal projection onto the \(y\)-coordinates sends any radius-\(r\) Euclidean ball in \(C(A)\) to a radius-\(r\) Euclidean ball in \(\Delta_d\). For its center \(y\) to lie at distance at least \(r\) from all simplex facets one must have \(y_j\ge r\) for all \(j\) and \(1-\sum_jy_j\ge\sqrt d\,r\). Adding these inequalities gives \(1\ge(d+\sqrt d)r\), so \(r\le\rho_d\). Equality forces \(y_j=\rho_d\) for every \(j\), and this is the only base-simplex incenter.

**Exact radius-saturation test.** The fiber lower inequality \(x_i\ge0\) has unit Euclidean normal and therefore requires \(x_i\ge r\) for the radius-\(r\) ball. The upper inequality can be written
\[
x_i+\sum_{j=1}^d(a_{i0}-a_{ij})y_j\le a_{i0}.
\]
Its Euclidean normal length is exactly \(H_i\), so radius-\(r\) ball containment is equivalent to
\[
a_{i0}\left(1-\sum_jy_j\right)+\sum_ja_{ij}y_j-x_i\ge H_ir.
\]
At radius \(r=\rho_d\) the unique permitted projected center is \(y_j=\rho_d\); here \(1-\sum_jy_j=\sqrt d\,\rho_d\). Hence the last two inequalities reduce to
\[
\rho_d\le x_i\le\rho_d(B_i-H_i).
\]
They have a simultaneous solution if and only if \(B_i\ge1+H_i\) for every \(i\). They also describe all possible centers. A Euclidean ball is contained in an intersection of halfspaces precisely when its center has the stated normalized slack to each halfspace; this proves both necessity and sufficiency, including the contact characterization.

**Strict saturation for all-positive integral matrices.** If every \(a_{ij}\ge1\), then every fiber contains the unit cube \([0,1]^m\). Accordingly \(C(A)\supset\Delta_d\times[0,1]^m\). For \(d\ge2\) one has \(\rho_d<1/2\), and, for any \(x_i\in[\rho_d,1-\rho_d]\), the radius-\(\rho_d\) ball with center \((x,\rho_d\mathbf1_d)\) lies in this product and hence in \(C(A)\). Thus each exact incenter interval contains the strictly nondegenerate interval \([\rho_d,1-\rho_d]\); in particular \(B_i>1+H_i\). The upper bound proves optimality.

**Sharp sparse-family transition.** For \(A_{\alpha,\beta}\) each row has \(a_{i0}=\alpha\), \(a_{ii}=\beta\) and other \(a_{ij}=0\). It follows that \(B_i=\alpha\sqrt d+\beta\) and \(H_i=\sqrt{1+(\beta-\alpha)^2+(d-1)\alpha^2}\). Both \(B_i-1\) and \(H_i\) are positive. The identity
\[
(B_i-1)^2-H_i^2
=2\bigl(\alpha\sqrt d\,(\beta-1)+\beta(\alpha-1)\bigr)
\]
is nonnegative for integers \(\alpha,\beta\ge1\), and is zero if and only if \(\alpha=\beta=1\). Therefore every row saturates the inradius criterion, and its interval degenerates exactly at that parameter pair. Since the rows have identical \(B_i,H_i\), the Cartesian product is a point there and a full cube otherwise. The base facets and fiber faces are genuine facets in this family (each \(\alpha>0\)), so the indicated contact counts follow from which interval endpoints are chosen.

## Verification

A standalone numerical-optimization verifier is supplied as `verify_cayley.py`. It executes 1,120 independently assembled linear programs (one for each randomly generated small nonnegative matrix) and checks that the optimal radius equals \(\rho_d\) exactly in the predicted saturation cases, within numerical tolerance. It separately checks the sparse-family radical formula and the unique-degeneracy criterion for every \(1\le d\le31\) and \(1\le\alpha,\beta\le11\). The executed script reported `PASS: 1120 independent LPs, 19865 assertions; sparse parameter formula checked through d=31.` The radial halfspace proof above, not finite computations or numerical solver tolerances, establishes the unrestricted theorem.

## Relationship to prior work

Ferroni, *Unimodality shenanigans in Ehrhart theory* (arXiv:2609.10513; first submitted September 9, 2026), defines the same Cayley sums of coordinate boxes, proves the fiber representation, studies their regular unimodular flag triangulations and smoothness, and constructs nonunimodal Ehrhart numerators. These established statements are used as motivation and are not presented as new. The present result concerns the **Euclidean Chebyshev radius, the sharp saturation criterion, and all optimal centers and facet contacts**; these are not statements of Ferroni's manuscript. The older Haase–Paffenholz–Piechnik–Santos theory supplies triangulation results for Nakajima or chimney polytopes, not this metric classification. Standard convex optimization gives general inball linear programs, but the exact criterion and closed-form center family in these box-Cayley coordinates require the geometric reduction above. Comparable incenter-cube phenomena in other polytope families do not imply this criterion for general \(A\).

## Limitations

For general matrices failing at least one inequality \(B_i\ge1+H_i\), the theorem proves that the inradius is **strictly below** \(\rho_d\) but does not calculate its value or describe its centers. No assertion is made about John ellipsoids or Santaló points, nor about optimality of the insphere under affine changes of coordinates. There is no independent audit of this proposed original result. Historical coverage by currently inaccessible or unindexed literature remains possible.

## References

1. Luis Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513, first posted 2026-09-09; the inspected version is v2 (2026-10-29), especially Section 2, Proposition 2.1 and the matrices \(A_{\alpha,\beta}\).
2. Christian Haase, Andreas Paffenholz, Lindsay C. Piechnik, and Francisco Santos, *Existence of unimodular triangulations—positive results*, arXiv:1405.1687; Memoirs of the AMS 270 (2021), no. 1321. Its role here is background on chimney and Nakajima polytopes.
