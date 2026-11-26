# Sharp symmetry-aligned rectangle capacity of the Reuleaux triangle

## Finding

In a width-one Reuleaux triangle, among rectangles with a pair of sides parallel to a reflection axis, the largest area is
\[
A_*=2u_*\left(\sqrt{1-u_*^2}+\sqrt{1-(u_*+1/2)^2}-\frac{\sqrt3}{2}\right)=0.419716757423\ldots.
\]
Here \(u_*\) is the unique root of \(f(u)+uf'(u)=0\) in \((0,1/2)\), where \(f(u)=\sqrt{1-u^2}+\sqrt{1-(u+1/2)^2}-\sqrt3/2\). With the selected reflection axis vertical, the horizontal and vertical half-sides are \(u_*\) and \(v_*=f(u_*)/2\), and the center is \((0,c_*)\) with \(c_*=1/\sqrt3+v_* - \sqrt{1-u_*^2}\). The extremizer is unique up to threefold rotations and exchange of the names of the two rectangle axes. It is off center and not square.

## Assumptions and scope

Let \(h=1/\sqrt3\) and let \(K\) be the intersection of the unit disks centered at \((0,h)\), \((1/2,-h/2)\), and \((-1/2,-h/2)\). Threefold rotation allows the selected axis to be taken as vertical. Only rectangles with positive side lengths and this alignment are at issue; no unrestricted orientation optimum is asserted.

## Proof

Write the rectangle as \([s-u,s+u]\times[L,H]\) with \(u>0\) and \(H>L\), and put \(U=u+|s|\). The largest horizontal displacement from the upper disk's center is \(U\), and the largest displacement over both lower disk centers is \(U+1/2\). Thus \(U\le 1/2\) is necessary. Put
\[
Q(U)=\sqrt{1-U^2},\qquad P(U)=\sqrt{1-(U+1/2)^2}.
\]
The vertical interval of the rectangle must lie in the intersection of \([h-Q(U),h+Q(U)]\) and \([-h/2-P(U),-h/2+P(U)]\). These exact inequalities are also sufficient: the horizontal displacements of all points are bounded by those used to obtain the intervals, and the maximal displacements are attained at horizontal endpoints, at both heights \(L,H\).

Since \(P\le Q\), the upper endpoint of the intersection is \(-h/2+P(U)\). For the lower endpoint, \(Q-P\) is increasing on \([0,1/2]\), because \((U+1/2)/P>U/Q\) on \((0,1/2)\). Hence \(Q-P\le Q(1/2)-P(1/2)=3h/2\), and the lower endpoint is \(h-Q(U)\). In particular the vertical extent of \(K\) itself, by putting \(U=0\), is \([h-1,h]\). The maximum available rectangle height at a given \(U\) is \(f(U)=Q(U)+P(U)-3h/2\).

The area satisfies \(2u(H-L)\le 2u f(U)\le 2U f(U)\). A rectangle of positive area has \(f(U)>0\), so equality in the second bound requires \(s=0\). For \(0<U<1/2\), the centered horizontal interval and the full available vertical interval attain the bound. Because \(f\) decreases strictly to zero at \(1/2\), the area function \(2Uf(U)\) is positive in this open interval and vanishes at both ends. Both square-root terms are strictly concave and decreasing there, so \((2Uf(U))''=4f'(U)+2Uf''(U)<0\). The unique maximizer is therefore the stated interior root, and attaining the full height fixes \(L,H\) uniquely. The bottom pair of corners contacts the upper disk's arc, and the upper corners contact the farther lower disks.

For explicit separations, the sign of \(f(u)+uf'(u)=Q+P-3h/2-u^2/Q-u(u+1/2)/P\) is positive at \(u=33/100\) and negative at \(34/100\). For example, use \(0.944<Q(0.33)<0.945\), \(0.557<P(0.33)<0.558\), \(0.940<Q(0.34)<0.941\), \(0.542<P(0.34)<0.543\), and \(0.866<3h/2<0.867\), all obtained by squaring. Consequently \(v_*< (0.945+0.558-0.866)/2<0.33<u_*\). Also \(c_*=h/4-(Q(u_*)-P(u_*))/2<0\) since \(h<0.58\) and \(Q(u_*)-P(u_*)>0.944-0.558\). The centroid is the origin by rotation symmetry. Numerical evaluation gives \(u_*\approx0.334833532595\), \(v_*\approx0.313377183410\), and \(c_*\approx-0.051549844935\).

## Verification

The accompanying `checker.py` bisects the strictly monotone area derivative and tests all twelve vertex–disk feasibility inequalities at the resulting optimizer. Bisection corroborates the decimals; strict concavity and the vertical-interval argument establish the exact result and exact contacts.

## Relationship to prior work and limitations

The Reuleaux triangle is the classical least-area constant-width body [1]. General algorithms for axis-aligned rectangles in convex polygons [2,3] use polygonal inputs and do not give the exact formula in this curved body. The result determines a symmetry-restricted capacity; it also supplies a feasible-area lower bound for the unrestricted rectangle problem, not a proof of that unrestricted optimum. No exhaustive priority claim is made.

## References

1. E. M. Harrell, *A direct proof of a theorem of Blaschke and Lebesgue*, arXiv:math/0009137, https://arxiv.org/abs/math/0009137.
2. H. Alt, D. Hsu and J. Snoeyink, *Computing the largest inscribed isothetic rectangle*, CCCG 1995, https://www.academia.edu/48665850/Computing_the_largest_inscribed_isothetic_rectangle.
3. *Largest unit rectangles inscribed in a convex polygon*, Computational Geometry (2024), https://doi.org/10.1016/j.comgeo.2024.102135.
