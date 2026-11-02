# Exact maximum-relative-diameter bisection of every rectangle
## Finding
Let \(R\subset\mathbb R^2\) be a rectangle with side lengths \(L\ge H>0\). For a bisection \(P\) into connected pieces \(R_1,R_2\), set
\[
d_M(P)=\max\{D(R_1),D(R_2)\},
\]
where \(D\) denotes Euclidean diameter. Then
\[
\min_P d_M(P)=\sqrt{H^2+\frac{L^2}{4}}.
\]
A midpoint segment parallel to the sides of length \(H\) is minimizing. Among all straight-line bisections through the center, that line is the unique minimizer when \(L>H\). For a square, the two side-parallel midpoint lines are exactly the minimizing center-passing straight lines.

## Assumptions and scope
The rectangle is nondegenerate and no equal-area assumption is imposed on an arbitrary admissible bisection. The reduction from arbitrary bisections to center-passing straight-line bisections uses Proposition 3.1 of Cañete and Segura Gomis, which states that every minimizing bisection of a centrally symmetric planar convex body has a center-passing straight-line bisection with the same maximum relative diameter. The older equal-area fencing formulation already contained the analogous central-line reduction.

Write
\[
R=[-A,A]\times[-B,B],\qquad A=\frac L2,\quad B=\frac H2,
\]
so \(A\ge B>0\).

## Proof
It is enough to minimize over straight lines through the center.

First suppose such a line meets the two horizontal sides at \((t,B)\) and \((-t,-B)\), where by reflection symmetry we may take \(t\ge0\). One of the two halves contains the right-hand corners \((A,B)\) and \((A,-B)\). In that half, the points \((-t,-B)\) and \((A,B)\) both occur on its boundary, so its diameter is at least
\[
\sqrt{(A+t)^2+(2B)^2}\ge \sqrt{A^2+4B^2}.
\]
Equality in this lower bound is possible only for \(t=0\).

Now suppose the center-passing line meets the two vertical sides at \((A,s)\) and \((-A,-s)\), with \(s\ge0\). One of the halves contains the two top corners. It therefore contains a pair at distance at least
\[
\sqrt{(2A)^2+(B+s)^2}\ge \sqrt{4A^2+B^2}.
\]
Since \(A\ge B\),
\[
4A^2+B^2\ge A^2+4B^2,
\]
with equality exactly when \(A=B\). Thus every center-passing straight-line bisection has maximum relative diameter at least \(\sqrt{A^2+4B^2}\).

The vertical midpoint cut \(x=0\) produces two rectangles of side lengths \(A\) and \(2B\), each of diameter
\[
\sqrt{A^2+4B^2}=\sqrt{H^2+\frac{L^2}{4}},
\]
so the lower bound is attained. If \(A>B\), equality in the two cases forces \(t=0\), giving uniqueness among center-passing straight lines. If \(A=B\), the horizontal midpoint cut also attains the same value, and the preceding strictness conditions show that these two axis-parallel midpoint lines are the only center-passing straight-line minimizers.

## Verification
The proof was checked independently in the two exhaustive incidence classes for a line through the center of a rectangle: intersection with the horizontal pair of sides or with the vertical pair. The equality conditions were tracked in each class. The reduction theorem was checked in the full text of Cañete--Segura Gomis, arXiv:1803.00321, Proposition 3.1. The earlier 2004 fencing source was also inspected in full text at the conference-proceedings version; its Theorem 2 gives the corresponding central-line reduction for equal-area bisections.

For the square \(L=H\), the value becomes \(\sqrt5\,L/2\), agreeing with the independently recorded regular-quadrilateral special case of the regular-even-polygon formula. That special case is a consistency check and is not the source of the non-square rectangle argument.

## Relationship to prior work
Miori, Peri, and Segura Gomis introduced the relative-diameter fencing problem and proved a center-passing-line reduction for centrally symmetric planar convex sets in the equal-area setting. Cañete, Miori, and Segura Gomis later emphasized that the precise optimal straight line was not known in the general centrally symmetric framework. Cañete and Segura Gomis subsequently extended the center-line reduction to arbitrary bisections and developed general necessary and sufficient criteria, but their full text contains no rectangle, square, or parallelogram specialization.

A database comparison found a result for every regular even polygon; it implies the square endpoint of the present formula but no non-square rectangle. Other nearby records concern different functionals on rectangles or higher-dimensional cubes. Thus the new content is the complete aspect-ratio family of rectangles and the exact center-line equality classification, not the already covered square boundary case.

## Limitations
This result does not classify all curved minimizing bisections. Diameter minimization can admit nonunique curved perturbations, and only the center-passing straight-line minimizers are classified here. No assertion is made for general parallelograms or noncentrally symmetric quadrilaterals.

## References
1. C. Miori, C. Peri, S. Segura Gomis, *On fencing problems*, 20th European Workshop on Computational Geometry, Seville, 25--26 March 2004; journal version: J. Math. Anal. Appl. 300 (2004), 464--476, DOI 10.1016/j.jmaa.2004.06.050.
2. A. Cañete, C. Miori, S. Segura Gomis, *Trisections of a 3-rotationally symmetric planar convex body minimizing the maximum relative diameter*, J. Math. Anal. Appl. 418 (2014), 1030--1046, DOI 10.1016/j.jmaa.2014.04.041.
3. A. Cañete, S. Segura Gomis, *Bisections of centrally symmetric planar convex bodies minimizing the maximum relative diameter*, arXiv:1803.00321, first version 1 March 2018.
