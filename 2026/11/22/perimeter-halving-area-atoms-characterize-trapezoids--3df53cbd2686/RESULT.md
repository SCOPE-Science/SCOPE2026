# Perimeter-halving area atoms characterize trapezoids

## Finding

Let \(K\subset\mathbb R^2\) be a nondegenerate strictly convex-vertex Euclidean polygon: its vertices are in counterclockwise order, every interior angle is strictly between zero and \(\pi\), and no adjacent edges are collinear. Let \(P\) be its perimeter and \(V\) its area. Select a boundary point \(p(s)\) uniformly by Euclidean arclength \(s\in[0,P)\), and pair it with \(q(s)=p(s+P/2)\), where arclength is periodic. The chord \([p(s),q(s)]\) cuts the polygon into two portions. Define \(Z_K\in(0,1/2]\) as the smaller portion's area divided by \(V\).

**Atomicity and density theorem.** The law of \(Z_K\) is the sum of finitely many point masses and an absolutely continuous distribution; it has no singular-continuous component. The continuous density is a finite sum of branches obtained from quadratic polynomials by inversion, hence of inverse-square-root form away from a finite set of branch endpoints. An atom occurs **if and only if** a positive-length interval of perimeter-halving chords pairs the interiors of two parallel polygon edges. Distinct such intervals can contribute to the same atom, in which case their masses add.

**Complete quadrilateral classification.** If \(K=Q\) is any nondegenerate convex quadrilateral, then the distribution has an atom if and only if \(Q\) is a trapezoid (here including parallelograms). More precisely:

- If no two opposite sides are parallel, \(Z_Q\) has no atoms.
- If exactly one pair of opposite sides is parallel, let their lengths be \(a,b>0\), the two other side lengths be \(c,d>0\), and \(P=a+b+c+d\). There is **exactly one atom**, with probability and location
  \[
  \boxed{\Pr(Z_Q=z_*)=\frac{2\min(a,b)}P,\qquad
  z_*=\frac12-\frac{|c-d|}{2(a+b)}.}
  \]
  The atom lies at \(1/2\) precisely for an isosceles trapezoid.
- If both pairs of opposite sides are parallel, \(Q\) is a parallelogram and \(Z_Q=1/2\) almost surely.

In particular, the positive jump of the distribution function detects the existence of parallel sides without observing directions. For a genuine trapezoid, its jump \(w\), together with the perimeter, recovers its shorter parallel side as \(Pw/2\); the atom location recovers the dimensionless leg-length asymmetry \(|c-d|/(a+b)=1-2z_*\).

## Assumptions and scope

The random point is uniform in **boundary arclength**, and its second endpoint is deterministically half the perimeter away, not sampled independently. The segment is always the straight Euclidean chord. A ``genuine trapezoid'' means exactly one pair of parallel opposite edges, with both bases positive; the parallelogram is a separate limiting case. The area fraction is the **smaller** of the two portions, so its law is independent of which arclength direction labels the cap. Edges of a convex polygon have length strictly less than half the perimeter, since an edge is shorter than the complementary boundary chain. Vertex coincidences occur on a finite arclength set of probability zero.

For clarity, the phrase inverse-square-root density means a finite sum of terms proportional to \(1/\sqrt{\alpha+\beta z}\) restricted to appropriate open intervals, with \(\beta\ne0\); terms are interpreted only where their denominator is positive. Their integrable endpoint divergences do not create atoms.

## Proof

**1. A differential identity for every polygon.** Write \(r(s)\) for the boundary parametrization and \(H=P/2\). Put \([x,y]=x_1y_2-x_2y_1\). The oriented cap area \(B(s)\), enclosed by the counterclockwise arc \(r([s,s+H])\) and the straight chord back to its starting point, is nonnegative by convexity. Green's formula gives
\[
 2B(s)=\int_s^{s+H}[r(t),r'(t)]\,dt+[r(s+H),r(s)].
\]
On any open interval where both endpoints remain in the interiors of two fixed edges, let \(u=r'(s)\) and \(v=r'(s+H)\) be their constant unit tangents. Then differentiation yields
\[
 2B'(s)=[q(s)-p(s),u+v],\qquad
 \boxed{B''(s)=-[u,v].}
\]
There are only finitely many endpoint-edge regimes, since transitions occur exactly when \(s\) or \(s+H\) is a vertex. Thus \(B(s)\) is continuous and piecewise quadratic. The normalized smaller-cap function is \(Z(s)=\min\{B(s),V-B(s)\}/V\).

**2. Classifying constant regimes and the law.** Two unit edge tangents of a strictly convex-vertex polygon are either linearly independent or, if parallel, oppositely directed. Indeed, as edges are traversed counterclockwise, their tangent angles rotate strictly through one full turn without repeating a direction. If \(u\) and \(v\) are not parallel, \([u,v]\ne0\), so \(B\) is a nonconstant quadratic. If \(v=-u\), then \(B'=0\) identically, so \(B\) is constant on that regime. The converse is immediate from \(B''=-[u,v]\). Because no edge has length at least \(P/2\), the paired endpoints never remain in the same edge throughout a positive interval.

A nonconstant polynomial of degree at most two can take any one value on only finitely many points, and the monotone pieces of its pushforward of arclength measure have the standard change-of-variables density
\[
 f_B(b)=\frac1P\sum_{s:B(s)=b,\;B'(s)\ne0}\frac1{|B'(s)|}.
\]
On each quadratic regime, solving \(B(s)=b\) expresses \(|B'(s)|\) as the square root of an affine expression in \(b\). Passing to \(Z(s)=\min(B,V-B)/V\) merely combines the two level sets \(B=Vz\) and \(B=V(1-z)\) and introduces the factor \(V\). All omitted transition and critical points form a finite null set. Constant regimes contribute atoms proportional to their arclengths; therefore the law has exactly the stated finite atomic and inverse-square-root absolutely continuous parts and no singular-continuous component.

**3. Quadrilaterals without parallel edges.** If a quadrilateral has no parallel opposite sides, all paired edge tangents on open regimes are nonparallel, so every regime is nonconstant. The preceding result gives no atoms. Two distinct edges of a convex quadrilateral can be parallel only if they are opposite.

**4. Exact plateau for a genuine trapezoid.** Name the parallel bases so that \(b>a>0\), and put the counterclockwise vertices at
\[
 (0,0),\quad (b,0),\quad (\xi+a,h),\quad (\xi,h),\qquad h>0.
\]
Their other side lengths, in that order, are
\[
 c=\sqrt{(\xi+a-b)^2+h^2},\qquad
 d=\sqrt{\xi^2+h^2}.
\]
Set \(P=a+b+c+d\) and \(C=(a+b+c-d)/2\). Because the vectors defining \(c\) and \(d\) differ by a nonzero horizontal vector of length \(b-a\), the reverse triangle inequality is strict:
\[
 |c-d|<b-a.
\]
Consequently \(0<C-a<C<b\). For **every** starting point \(p(t)=(t,0)\) with \(C-a<t<C\), the point half the perimeter away is on the upper base and equals
\[
 q(t)=(\xi+C-t,h).
\]
The relevant cap is the quadrilateral with successive vertices \(p(t),(b,0),(\xi+a,h),q(t)\), whose height is \(h\) and whose two parallel base lengths are \(b-t\) and \(a-C+t\). Hence its area, independent of \(t\), is
\[
 B(t)=\frac h2\{(b-t)+(a-C+t)\}
 =\frac h2(a+b-C)=\frac h4(a+b-c+d).
\]
The full trapezoid has area \(V=h(a+b)/2\). The smaller fraction is therefore
\[
 z_*=\min\!\left(\frac12-\frac{c-d}{2(a+b)},
                         \frac12+\frac{c-d}{2(a+b)}\right)
 =\frac12-\frac{|c-d|}{2(a+b)}.
\]
The lower-base starting interval has length exactly \(a\); translation of its arclength parameters by \(P/2\) gives a second disjoint interval, also of length \(a\), on the upper base. Their smaller cap fractions agree. No other edge pair is parallel in a genuine trapezoid, so no other constant regime exists and the **one** atom has mass \(2a/P\). This is exactly \(2\min(a,b)/P\), since \(b>a\). The location equals \(1/2\) if and only if \(c=d\), as claimed.

**5. Parallelograms.** When both pairs of opposite sides are parallel, translation by half the perimeter maps every boundary point to its image under central reflection through the parallelogram's center. Each chord therefore passes through that center and divides area equally by the central symmetry. Thus \(Z=1/2\) almost surely. These cases exhaust convex quadrilaterals. The inverse formulas follow by rearranging the exact atom mass and location. \(\square\)

## Verification

The attached standalone `verify.py` needs only standard Python and checks two independent levels. First, exact rational shoelace calculations independently reconstruct the constant cap area on 101 arclength samples in each of three integer-geometry trapezoids, including a parallelogram; exact interval lengths and atom locations/masses are also checked. Second, on four explicit convex polygons with four to six vertices, it directly evaluates arc-and-chord cap areas by polygon shoelace geometry and compares numerical second differences with the independently computed tangent determinant. It passes `VERIFY_OK 948 exact_and_geometric_assertions` in the supplied environment. These finite checks are regression tests; the continuous classifications and all-quadrilateral formula follow from the proof above, not enumeration.

For a concrete instance, the trapezoid with vertices \((0,0),(7,0),(4,4),(0,4)\) has base lengths \(7,4\), leg lengths \(5,4\), perimeter \(20\), and area \(22\). Its smaller-cut-area law has exactly one atom, at \(5/11\) with mass \(2/5\).

## Relationship to prior work

Harned's *Perimeter Bisectors, Cusps, and Kites* (2021, full PDF examined), particularly Definition 2.5 and Theorem 3.1, explicitly detects paired parallel polygon edges and proves that their contribution to the **envelope of bisecting lines** collapses to a point. That geometric observation is closely related and is **not** claimed as new. Its theorems do not give the area-fraction probability measure, the quadratic-area derivative, or the one-atom mass and location formula. The present work starts from that known edge-parallel phenomenon and studies a different geometric invariant: the distribution of the area on either side of a boundary-random perimeter-halving chord.

Amadtohed et al. (2022; complete open full text examined) classify envelopes for **arbitrary fixed perimeter split ratios of triangles**, not the area distribution of equal-perimeter cuts in quadrilaterals. Grüne et al. (2007; full PDF inspected) study **chords that halve area**, a different family, and optimize lengths. Earlier public mathematical computations of halving-chord **length moments for parallelograms** and geometric dilation of isosceles trapezoids similarly do not supply this area distribution or converse atom characterization. These comparisons concern implication of precise statements, not just matching words.

Berele and Catoiu's 2022 *Bisecting envelopes of convex polygons* is a close priority risk because it classifies perimeter-bisecting envelopes, particularly quadrilateral cases. Its abstract and bibliographic material were checked, but its full article could not be obtained through open or institutional routes. The absence of an explicit area-law statement in those accessible portions is **not** evidence that the full paper cannot imply the result. Earlier unindexed results on area bisection or probabilistic chord laws may also exist; independent literature verification has not occurred.

## Limitations

The polygonal density claim requires strict convexity at every listed vertex (no redundant collinear edges); it does not cover arbitrary nonconvex polygons or smooth-boundary bodies. The exact one-atom formula is for convex quadrilaterals, not all polygons with multiple parallel edge pairs. The atom alone does not reconstruct the entire trapezoid up to congruence; it detects a pair of parallel sides and recovers only the specified base and leg-asymmetry quantities. No quantitative robustness under measurement noise is proved. The incomplete access to the highly relevant 2022 envelope article is a real residual priority uncertainty, not a claim of uniqueness or independent verification.

## References

1. M. Harned, *Perimeter Bisectors, Cusps, and Kites*, International Journal of Geometry 10 (2021), no. 4, 85–106, https://ijgeometry.com/wp-content/uploads/2021/09/6.-85-106.pdf, especially Definition 2.5, Theorem 3.1, and the trapezoid figures.
2. N. Amadtohed, T. Chaidee, P. Racha-in, and T. Theerakarn, *Dividing the Perimeter of a Triangle into Unequal Proportions*, International Journal of Mathematics and Mathematical Sciences (2022), Article 2751666, first publicly released 2022-06-09, https://doi.org/10.1155/2022/2751666.
3. A. Grüne, R. Klein, C. Miori, and S. Segura Gomis, *Chords halving the area of a planar convex set*, Mathematical Inequalities & Applications 10 (2007), 205–216, https://tizian.cs.uni-bonn.de/publications/gkms-chapc-05.pdf.
4. A. Berele and S. Catoiu, *Bisecting envelopes of convex polygons*, Advances in Applied Mathematics 137 (2022), 102342, https://doi.org/10.1016/j.aam.2022.102342 (abstract/metadata inspected; full text inaccessible).
