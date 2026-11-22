# Sharp symmetry-aligned rectangle capacity of the Reuleaux triangle

## Finding
For the width-one Reuleaux triangle, the largest area of a rectangle whose edges are aligned with either direction of any of its three reflection axes is precisely
\[
A_*=2u_*\left(\sqrt{1-u_*^2}+\sqrt{1-(u_*+1/2)^2}-\frac{\sqrt3}2\right)=0.419716757423\ldots.
\]
Here \(u_*\in(0,1/2)\) is the unique root of \(f(u)+uf'(u)=0\), where \(f(u)=\sqrt{1-u^2}+\sqrt{1-(u+1/2)^2}-\sqrt3/2\). The extremizer is unique up to the threefold rotations and the conventional exchange of its two axis labels. Its horizontal and vertical half-sides are \(u_*\) and \(v_*=f(u_*)/2\); its center is at signed symmetry-axis height \(c_*=1/\sqrt3+v_*-\sqrt{1-u_*^2}\). Its center is off the triangle's centroid and its two side lengths are unequal.

## Assumptions and scope
Let \(h=1/\sqrt3\) and let \(K\subset\mathbb R^2\) be the intersection of the three closed unit disks centered at \((0,h)\) and \((\pm1/2,-h/2)\). A rectangle is eligible only if one pair of its sides is parallel to a reflection axis of \(K\); orientation is not otherwise variable. Width is one. Nondegenerate means strictly positive side lengths. Threefold rotational invariance reduces to horizontal/vertical rectangles with the selected axis vertical.

## Proof
For a horizontal/vertical rectangle with center \((s,c)\) and half-sides \(u,v>0\), convexity of \(K\) implies all four vertices must belong to \(K\). Reflecting across the vertical symmetry line and averaging the reflected centers keeps \(u,v\) fixed and yields a feasible rectangle with \(s=0\). Consequently the optimum can be attained with center \((0,c)\); moreover the farthest horizontal corner distances in both pairs of unit disks grow strictly with \(|s|\), so any optimal rectangle must have \(s=0\).

The triangle has vertical extent \([-h/2,h]\). At the bottom rectangle corners, the upper unit disk gives precisely \(u^2+(h-c+v)^2\le1\). At the upper corners, the two lower disks give precisely \((u+1/2)^2+(c+v+h/2)^2\le1\). The remaining corner-disk constraints are weaker because of the vertical extent. Therefore feasibility is equivalent to
\[
0<u\le\frac12,\quad v>0,\quad h+v-\sqrt{1-u^2}\le c\le\sqrt{1-(u+1/2)^2}-v-\frac h2.
\]
It follows that \(2v\le f(u)\), with equality possible at exactly one \(c\). The maximal area for any chosen \(u\) is thus \(4uv=2uf(u)\). At \(u=0\) and \(u=1/2\) this product is zero and it is positive in between. Both square-root terms in \(f\) are strictly concave and strictly decreasing on \((0,1/2)\). Thus
\[
\frac{d^2}{du^2}(2uf(u))=4f'(u)+2uf''(u)<0,
\]
so there is a unique maximizer \(u_*\) in the open interval. Differentiation gives the displayed root equation; strict concavity proves existence, uniqueness and global optimality **within the permitted rectangle orientations**. At equality, both opposite pairs of rectangle corners contact the relevant circular arcs. Evaluating the uniquely defined root gives \(u_*\approx0.334833528635\), \(v_*\approx0.313377187116\), \(c_*\approx-0.051549842637\). In particular the solution is neither centered nor square.

## Verification
The standalone checker `checker.py` solves the strictly monotone derivative equation by bisection, checks all twelve vertex-disk squared-distance inequalities and checks the analytical relation between optimality and contact equalities at the computed root. Its numerical checks corroborate but do not replace the strict-concavity proof.

## Relationship to prior work
The Reuleaux triangle is the classical least-area constant-width body (Harrell, 2000, arXiv:math/0009137). Alt, Hsu and Snoeyink (1995) study axis-aligned inscribed rectangles in convex polygons, and later algorithms study general polygonal hosts, but the stated exact off-center, unequal-side rectangle in the **curved Reuleaux body** is not given by those inspected accounts. The orientation restriction is essential. The formula supplies a constructive lower bound for the unrestricted maximum, not its exact value.

## Limitations
No global statement is made for rectangles of arbitrary orientation, and no optimality among all Reuleaux-triangle rectangles is inferred. The explicit decimal values are approximations to the uniquely specified algebraic-analytic root. Historical novelty is based on the inspected literature and recorded semantic comparisons, not a comprehensive priority certificate.

## References
1. E. M. Harrell, *A direct proof of a theorem of Blaschke and Lebesgue*, arXiv:math/0009137, first posted 2000-09-14, https://arxiv.org/abs/math/0009137.
2. H. Alt, D. Hsu and J. Snoeyink, *Computing the largest inscribed isothetic rectangle*, CCCG 1995, https://www.academia.edu/48665850/Computing_the_largest_inscribed_isothetic_rectangle.
3. *Largest unit rectangles inscribed in a convex polygon*, Computational Geometry (2024), https://doi.org/10.1016/j.comgeo.2024.102135.
