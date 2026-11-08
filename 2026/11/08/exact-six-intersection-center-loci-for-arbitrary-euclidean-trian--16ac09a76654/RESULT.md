# Exact six-intersection-center loci for arbitrary Euclidean triangles

## Finding

Let \(T\) be any nondegenerate Euclidean triangle. For \(p\in\partial T\) define \(H_T(p)\) to be the maximum, over radii \(r>0\), of the number of *distinct* intersection points of \(\partial T\) with the circle of radius \(r\) centered at \(p\). Define \(J_6(T)=\{p\in\partial T:H_T(p)\ge6\}\). This set has an exact description as at most three open intervals, one per side, given below. Consequently the normalized boundary length \(\mathcal H^1(J_6(T))/P(T)\) is given by an explicit finite formula for every triangle.

Fix one *oriented* side \(AB\) of length \(c\), its opposite vertex \(C\), neighboring side lengths \(b=|AC|\) and \(a=|BC|\), and interior angles \(\alpha=\angle BAC\), \(\beta=\angle ABC\). Parameterize \(p\in AB\) by \(x=|AP|\), \(0\le x\le c\). If \(\alpha\ge\pi/2\) or \(\beta\ge\pi/2\), this side has no six-intersection centers. Otherwise set
\[
\ell_{AB}=\max\left\{\frac{c\sin\beta}{1+\sin\beta},\ c-\frac{a}{\cos\beta}\right\},\qquad
u_{AB}=\min\left\{\frac{c}{1+\sin\alpha},\ \frac{b}{\cos\alpha}\right\}.
\]
Then \(0<\ell_{AB}<u_{AB}<c\), and the six-intersection centers in the relative interior of \(AB\) are *precisely* \(\ell_{AB}<x<u_{AB}\). No triangle vertex belongs to \(J_6(T)\). Denoting the positive interval length by \(L_{AB}=u_{AB}-\ell_{AB}\) for eligible sides and \(L_{AB}=0\) for ineligible sides, we have the exact invariant
\[
\boxed{\quad\frac{\mathcal H^1(J_6(T))}{P(T)}=\frac{L_{AB}+L_{BC}+L_{CA}}{a+b+c}.\quad}
\]
In particular, all three sides contain a nonempty six-center interval exactly for acute triangles; only the side joining the two acute-angle vertices does so for a right or obtuse triangle.

For an equilateral triangle, the fraction is \(7-4\sqrt3\), agreeing with the previously established regular-polygon formula. For a \(3\)-\(4\)-\(5\) right triangle, it is \(65/864\). Along the explicit acute degenerating family with vertices \((0,0),(1,0),(1-\varepsilon^2,\varepsilon)\), \(\varepsilon\downarrow0\), the fraction tends to \(1/2\). Thus the equilateral value is not a universal maximum. No universal maximum is asserted here.

## Assumptions and scope

The triangle is a closed, nondegenerate, straight-sided Euclidean triangle. Centers are restricted to its boundary; radii are positive and otherwise unrestricted. Distinct intersection points, including any common-vertex or tangent intersections, count once each. The length of \(J_6\) is one-dimensional Hausdorff measure, and the triangle perimeter is \(P(T)>0\). The formula holds for all angles and real side lengths satisfying the strict triangle inequalities. At every displayed interval endpoint the count is strictly less than six.

## Proof

**A. A six-intersection circle necessarily cuts each open edge twice.** Fix a center \(p\) on the relative interior of \(AB\). A circle has at most two intersections with each supporting line, hence at most six intersections with the three closed sides. If six *distinct* points occur, each side must contribute exactly two distinct points, with none at a vertex (otherwise that point is shared by two sides, reducing the number of distinct points below six). In particular, both non-base edges must contain two interior crossings; conversely two interior crossings on each of the three edges give six distinct points.

**B. Elementary quadratic criterion.** Put \(x=|AP|\). Relative to the line supporting \(AC\), the perpendicular projection of \(p\) is at signed along-edge distance \(x\cos\alpha\) from \(A\), while its perpendicular distance is \(x\sin\alpha\). The corresponding quantities for \(BC\), measured from \(B\), are \((c-x)\cos\beta\) and \((c-x)\sin\beta\). Squared distance from a fixed point to a straight segment is a strictly convex quadratic in its affine parameter. Hence a circle cuts the relative interior of \(AC\) in two points exactly when its radius is strictly above the perpendicular distance, strictly below both endpoint distances, and the perpendicular foot is interior. The same holds for \(BC\). For the base \(AB\), two interior crossings occur exactly when \(0<r<\min(x,c-x)\).

If \(\alpha\ge\pi/2\), projection from an interior \(AB\) center onto line \(AC\) lies at or behind \(A\); distance along segment \(AC\) is monotone and two interior crossings are impossible. The analogous statement holds if \(\beta\ge\pi/2\). Now assume both angles are acute. The foot conditions are
\[
 x\cos\alpha<b,\qquad (c-x)\cos\beta<a.
\]
(The projections from \(A\) and \(B\) are automatically positive.) The radius inequalities on all three sides are feasible exactly when
\[
\max\{x\sin\alpha,(c-x)\sin\beta\}<\min\{x,c-x,|PC|\}.
\]
Under the two strict interior-foot conditions, each perpendicular distance is *strictly smaller* than \(|PC|\), so the \(|PC|\) restriction follows automatically. Because \(\sin\alpha<1\), \(\sin\beta<1\), the same-side constraints \(x\sin\alpha<x\) and \((c-x)\sin\beta<c-x\) are automatic. The remaining cross-constraints reduce to
\[
 x<\frac c{1+\sin\alpha},\qquad x>\frac{c\sin\beta}{1+\sin\beta}.
\]
Together with the two strict foot conditions they are exactly \(\ell_{AB}<x<u_{AB}\), proving necessity and sufficiency.

**C. Every eligible interval is nonempty.** By the sine rule, \(a:b=\sin\alpha:\sin\beta\). Choose \(x_0=cb/(a+b)\), the location where the internal angle bisector from \(C\) meets \(AB\). The two cross-constraints hold strictly since \(b\sin\alpha<a\) and \(a\sin\beta<b\) follow from \(\sin\alpha,\sin\beta<1\) and the sine rule. The foot conditions also hold because \(c\cos\alpha<a+b\) and \(c\cos\beta<a+b\), consequences of \(c<a+b\). Thus \(\ell_{AB}<x_0<u_{AB}\). The positive projection and strict base-interior conditions give \(0<\ell_{AB}<u_{AB}<c\).

**D. Vertices and perimeter fraction.** At a triangle vertex, either adjacent side is a ray beginning at the center, so each contributes at most one nonzero-radius intersection; the remaining side contributes at most two. Thus at most four distinct intersections are possible, never six. The three eligible open edge intervals are disjoint. Add their lengths and divide by \(a+b+c\) to obtain the stated fraction. Every triangle has either three acute angles or precisely one nonacute angle; this proves the phase classification.

**E. Calibrations and a nonregular boundary phenomenon.** In the equilateral case \(a=b=c\), \(\alpha=\beta=\pi/3\) on each side, so the open interval length divided by the side length is \(1/(1+\sqrt3/2)-(\sqrt3/2)/(1+\sqrt3/2)=7-4\sqrt3\). In the right \(3\)-\(4\)-\(5\) triangle only the hypotenuse side is eligible; on the orientation from the vertex adjacent to the side of length three, its bounds are \(15/8\) and \(25/9\), giving interval length \(65/72\) and perimeter fraction \(65/864\).

For \(A=(0,0)\), \(B=(1,0)\), \(C=(1-\varepsilon^2,\varepsilon)\) with sufficiently small positive \(\varepsilon\), direct scalar products show all angles acute (in particular, at \(C\) the two incident vectors have dot product \(\varepsilon^4>0\)). Substitution into the preceding bounds shows that the six-center interval lengths on \(AB\) and \(AC\) each tend to \(1/2\), while the third side has length \(\varepsilon\sqrt{1+\varepsilon^2}\) tending to zero. The perimeter tends to \(2\). The fraction therefore tends to \(1/2\).

## Verification

The standalone `verify.py` uses exact elementary formulas for side bounds and independent circle-segment quadratic roots. It checks the equilateral identity and the right \(3\)-\(4\)-\(5\) value, then tests more than five thousand nonsingular boundary centers across 270 reproducibly sampled triangles, including acute and obtuse cases. For each center it computes the maximum intersection count by sampling all radius intervals separated by every vertex distance and every admissible perpendicular-foot distance; it also tests the critical radii themselves. The script reports `VERIFY_OK` when all comparisons agree. Those tests are not an exhaustive proof; Sections A–E supply the full proof for all nondegenerate triangles.

## Relationship to prior work

Bárány and Roldán-Pensado [1] introduced the center locus \(J(K,n)\) and the length fraction \(|J(K,n)|/|\partial K|\) in their study of Erdős's circle-intersection problem. Their full online paper proves qualitative bounds and constructions, including a sufficient double-segment crossing criterion, but does not give the necessary-and-sufficient edge intervals for \(J(T,6)\) for a general triangle. A later exact regular-polygon result [2] supplies the equilateral special case \(7-4\sqrt3\), which is not claimed as new here; its symmetry-based proof and all regular-polygon formula do not imply the nonregular three-interval formula or the obtuse/right side classification. A separate result [3] classifies the *minimum over boundary centers* \(N(T)=\min_p H_T(p)\); that extremal minimum does not determine \(J(T,6)\) or its perimeter fraction. The distinct contribution is the complete nonregular triangle locus and exact fraction, including its angle-driven phase split.

## Limitations

The classification concerns triangles; it does not determine the six-center fraction for arbitrary polygons or smooth curves. No universal upper bound for that fraction over all triangles is claimed. At exact interval thresholds six distinct intersections are impossible, and the strict endpoints matter. The reported numerical checks are supplementary. Although the comparisons inspect highly relevant published full text and recoverable research records, an unindexed equivalent formula could exist; independent historical priority review has not occurred.

## References

[1] I. Bárány and E. Roldán-Pensado, “A Question from a Famous Paper of Erdős,” *Discrete & Computational Geometry* **50** (2013), 253–261, DOI 10.1007/s00454-013-9507-z, first publicly dated May 8, 2013. Full online journal article, Introduction and Sections 2–4.

[2] “Exact boundary-circle intersection spectrum of regular polygons,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-boundary-circle-intersection-spectrum-of-regular-polygons--bc2a75909fbe/RESULT.md . Full theorem and proof inspected; includes the equilateral-triangle special case.

[3] “A polygon-complexity bound for the Erdős circle-intersection invariant,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-polygon-complexity-bound-for-the-erd-s-circle-intersection-inv--ab61f433b81d . Comparison restricted to the reported best-center triangle classification; full text not inspected.
