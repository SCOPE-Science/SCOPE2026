# Exact four-cycle basins and physical-measure selection for right-isosceles farthest projections

## Finding
Let \(X\) be the union of the three **complete** supporting lines of the right-isosceles triangle with vertices \((0,0)\), \((1,0)\), \((0,1)\). Apply Everett's farthest-orthogonal-projection map \(T:X\to X\), with equal-distance ties fixed. Put
\[
s=\sqrt2-1,\quad
I_0=(s^2,s),\quad
I_1=(2s^2-1,2s-1),\quad
I_2=(4s^2-3,4s-3),\quad B=I_0\cup I_1\cup I_2.
\]
For a point \((t,0)\) or \((0,t)\), its forward orbit approaches the **unique primitive period-four orbit** if and only if \(t\in B\). For a point \((u,1-u)\), it approaches that orbit if and only if \(\min\{u,1-u\}\in B\). The four-cycle is
\[
(1/3,0)\longmapsto(2/3,1/3)\longmapsto(0,1/3)
\longmapsto(1/3,2/3)\longmapsto(1/3,0).
\]
The exact Euclidean arclength of its full basin in \(X\) is
\[
\boxed{\mathcal H^1(\mathcal B_4)=14(2-\sqrt2).}
\]
Its basin occupies the exact proportion
\[
\boxed{\frac{\mathcal H^1(\mathcal B_4\cap\partial Q)}{\mathcal H^1(\partial Q)}=6-4\sqrt2}
\]
of the triangle perimeter \(\partial Q\), where \(Q\) is the closed unit triangle.

The only other recurrent points are five fixed points: \((1/2,1/2)\), \((s,0)\), \((0,s)\), \((-1-\sqrt2,0)\), and \((0,-1-\sqrt2)\). Every point outside \(\mathcal B_4\) reaches one of these fixed points after finitely many steps. The invariant Borel probability measures are exactly the convex combinations of the uniform measure on the four-cycle and the five fixed-point Dirac measures. Relative to \(\mathcal H^1\) on \(X\), precisely two are physical: the uniform four-cycle measure and the point mass at \((1/2,1/2)\). The latter has an infinite-arclength basin; the other four fixed points have null basins. All conclusions scale by a factor \(a>0\) in the spatial distances when the legs of the triangle have length \(a\); the perimeter fraction is unchanged.

## Assumptions and scope
Parameterize the lines by \(L_x(t)=(t,0)\), \(L_y(t)=(0,t)\), and \(L_h(u)=(u,1-u)\), with all parameters real. If a point lies on one of these lines, calculate its perpendicular projections onto the other two lines; move to the farther projection, unless the two distances are equal, in which case the point is fixed. At pairwise intersections the rule gives the same point regardless of which incident line is used, so the map is well-defined. All basin statements use the ordinary forward-iteration limit; convergence to a period-four orbit means convergence in the four-phase sense, equivalently convergence in distance to its finite orbit. The arclength measure is the one-dimensional Hausdorff measure in the plane; intersections of lines have zero measure. A physical measure means an invariant probability whose empirical-measure basin has positive \(\mathcal H^1\)-measure.

## Proof
**Step 1: Direct geometry.** For \((t,0)\), the distances to \(L_y\) and \(L_h\) are \(|t|\) and \(|1-t|/\sqrt2\), respectively. The equality equation \(t^2=(1-t)^2/2\) has exactly the roots \(t=s\) and \(t=-1-\sqrt2\). Thus the four axis points at these parameters are fixed. If \(t\notin[-1-\sqrt2,s]\), the farther projection is the origin, which maps to the fixed point \((1/2,1/2)\). If \(-1-\sqrt2<t<s\) and \(t\ne0\), the first image is \(L_h((1+t)/2)\). A point \(L_h(u)\) projects to \(L_x(u)\) when \(u<1/2\), to \(L_y(1-u)\) when \(u>1/2\), and remains fixed at \(u=1/2\). Therefore the second image of an axis point \(t\ne0\) is on an axis with coordinate
\[
R(t)=\frac{1-|t|}{2},
\]
on the same axis if \(t<0\), on the opposite axis if \(t>0\). The point \(t=0\) maps directly to \((1/2,1/2)\). Reflection in the diagonal gives the same rule on \(L_y\). The only fixed point of \(L_h\) is its midpoint, since \(|u|=|1-u|\) only for \(u=1/2\).

**Step 2: Complete basin partition.** Every axis coordinate \(t\) in \((-1-\sqrt2,s)\) reaches a positive axis coordinate after at most two applications of \(R\), except when the orbit hits zero and then reaches the midpoint. For positive \(0<t<s\), the next return \(R(t)=(1-t)/2\) lies in the same interval \((0,s)\) exactly when \(s^2<t<s\). Indeed, \((1-s^2)/2=s\), and \(R\) maps \(I_0\) into \(I_0\). When \(t\in(0,s^2)\), the next coordinate exceeds \(s\) and hence reaches the origin and the midpoint; at \(t=s^2\) it hits the fixed tie \(s\). For \(-1<t<0\), \(R(t)=(1+t)/2\), so the condition \(R(t)\in I_0\) is exactly \(t\in I_1\). For \(-1-\sqrt2<t<-1\), its first return lies in \((-1,0)\), and the condition that the second return lies in \(I_0\) is exactly \(t\in I_2\). Here \(I_2\subset(-1-\sqrt2,-1)\). All remaining open intervals map to the midpoint; the finitely many boundary points of \(I_0,I_1,I_2\) either reach a fixed tie or the midpoint. This establishes the necessary and sufficient axis-basin statement and excludes further recurrent points.

On \(I_0\), two returns to axis coordinates are a four-step return to the **same** axis. There the four-step iterate is
\[
T^4(t)=R^2(t)=\frac{1+t}{4},
\]
where the displayed formula records the axis coordinate. It is a strict contraction with unique fixed coordinate \(t=1/3\), and the next three images are the four-cycle displayed above. Since the four locations are distinct and the map alternates between two axes and the hypotenuse, its least period is four. Every point in \(I_1\) or \(I_2\) reaches \(I_0\) after one or two axis returns. On \(L_h\), the first image has axis coordinate \(\min\{u,1-u\}\) except at its fixed midpoint, giving the claimed six open intervals. This completes the global orbit classification.

**Step 3: Lengths.** The interval lengths are
\[
|I_0|=s-s^2=3\sqrt2-4=:d,\quad |I_1|=2d,\quad |I_2|=4d.
\]
Each axis contributes \(7d\) arclength. For every interval in \(B\), two disjoint inverse coordinate intervals on \(L_h\) contribute \(2\sqrt2\) times that interval's parameter length. Thus
\[
\mathcal H^1(\mathcal B_4)=2(1+\sqrt2)\,7d=14(2-\sqrt2).
\]
Only \(I_0\) and its reflected copy meet the relevant positive unit segments of the triangle boundary, so \(\mathcal H^1(\mathcal B_4\cap\partial Q)=2(1+\sqrt2)d=2(2-\sqrt2)\). Since the perimeter is \(2+\sqrt2\), the fraction equals \(6-4\sqrt2\).

**Step 4: Invariant statistics.** All forward orbits either reach a fixed point or converge to the period-four orbit. Hence the recurrent points are precisely the five fixed points and the four period-four points: any other point is either transient before becoming fixed, or lies on a strict contracting branch and is nonrecurrent. Poincaré recurrence forces every invariant Borel probability to be supported on these nine points; invariance makes the four-cycle masses equal. The fixed tie points have zero-arclength basins because their preimages are finite unions of single points under the noncollapsed branches, while the only constant branch maps to the origin and then to the midpoint. The four-cycle has positive finite-arclength basin, and the midpoint has an infinite-arclength basin containing all sufficiently distant axis tails. It follows that exactly the two stated ergodic measures are physical; a nontrivial convex mixture cannot be the time-empirical limit of any individual orbit. Similarity of triangles supplies the scaling assertion.

## Verification
The self-contained script `verify_triangle.py` checks the algebraic interval and measure identities exactly using SymPy, builds the projections from the three line equations independently, confirms the four-cycle and all fixed tie points, and runs 7,200 seeded direct trajectory tests over the three complete lines. The script completed successfully with the message `PASS`. The continuum and uniqueness conclusions follow from the proof above; these finite trajectory tests are not an exhaustive argument.

## Relationship to prior work
Samuel Everett's *A Piecewise Contractive Map on Triangles* (first verified public online release 2021-01-07, DOI 10.1080/1726037X.2020.1847765; arXiv:2408.16019) introduced this projection map, proved qualitative convergence toward fixed points or periodic orbits, and studied isosceles-triangle bifurcations. Those contributions are prior work. The result here is the complete right-isosceles **support-line** basin partition, exact arclength and perimeter probability, and full invariant/physical-measure census; it is not an assertion that the original map or the existence of periodic orbits is new. Wang and Zhang's arXiv:1605.01794 concerns a different iterated system on the moduli space of triangles. A related later result classifying primitive three-cycles in Everett's general triangle map does not imply the period-four basin measure calculated here.

## Limitations
The exact formula applies to the right-isosceles similarity class and to the specified farthest-projection tie convention; it does not classify arbitrary triangle angles, other selection rules, or perturbations. Equivalence with unindexed prior results has not been excluded. The physical-measure claim uses Euclidean one-dimensional arclength on the union of lines, not planar Lebesgue measure. No independent mathematical audit is claimed.

## References
1. S. Everett, *A Piecewise Contractive Map on Triangles*, Journal of Dynamical Systems and Geometric Theories 18 (2020 issue), 183–192, first published online 2021-01-07. DOI: https://doi.org/10.1080/1726037X.2020.1847765 ; open manuscript: https://arxiv.org/abs/2408.16019 .
2. J. Wang and Y. Zhang, *A Geometric Iterated Function System on Triangles*, arXiv:1605.01794 (2016), https://arxiv.org/abs/1605.01794 .
