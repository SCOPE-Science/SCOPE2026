# Four-phase coverage of an alternating-radius triangular superlattice

## Finding

Let the unit-nearest-neighbor triangular lattice be
\[
\Lambda=\{(m+n/2,\sqrt3 n/2):m,n\in\mathbb Z\}.
\]
For even \(n\), center a closed disk of radius \(r\ge0\) at that site; for odd \(n\), center one of radius \(s\ge0\). The disks cover \(\mathbb R^2\) if and only if \(s\ge S(r)\), where
\[
S(r)=\begin{cases}
\sqrt{(1/2-r)^2+3/4},&0\le r\le1/2,\\
\sqrt3/2-\sqrt{r^2-1/4},&1/2\le r\le1/\sqrt3,\\
\sqrt{1/4+(\sqrt3/2-r)^2},&1/\sqrt3\le r\le\sqrt3/2,\\
1/2-\sqrt{r^2-3/4},&\sqrt3/2\le r\le1,\\
0,&r\ge1.
\end{cases}
\]
Consequently, every such two-radius covering has formal disk area per fundamental-cell area
\[
\Theta(r,s)=\frac{\pi(r^2+s^2)}{\sqrt3}\ge\frac{2\pi}{3\sqrt3},
\]
with equality if and only if \(r=s=1/\sqrt3\). Four distinct active boundary configurations occur along the critical profile, with switches at \(1/2\), \(1/\sqrt3\), and \(\sqrt3/2\). These statements include zero radii and the boundary-touching cases.

## Assumptions and scope

Disk radii are arbitrary nonnegative real numbers, measured in nearest-neighbor lattice spacing. Coverage means pointwise coverage by a union of **closed** Euclidean disks, allowing overlaps. The area-density \(\Theta\) counts disk areas with multiplicity, not the fractional area of their union. Site locations and the alternating row parity are fixed; the conclusion does not optimize over other periodic center arrangements, row orientations, or arbitrary disk placements.

The two colors are \(\Lambda_0=\mathbb Z\times\sqrt3\mathbb Z\) and \(\Lambda_1=(1/2,\sqrt3/2)+\Lambda_0\). A fundamental rectangular cell has area \(\sqrt3\) and contains one site of each color.

## Proof

Write \(a=1/2\), \(b=\sqrt3/2\), so \(a^2+b^2=1\). By reflection in the coordinate axes and translation by the rectangular periods, every point is congruent to one in \(Q=[0,a]\times[0,b]\), and in this rectangle its nearest even-row and odd-row centers are respectively \(o=(0,0)\) and \(v=(a,b)\). Indeed, each color separately is a translate of the rectangular lattice \(\mathbb Z\times\sqrt3\mathbb Z\); \(Q\) lies in the corresponding Voronoi cells. Thus coverage is equivalent to
\[
Q\subseteq \overline B(o,r)\cup\overline B(v,s).
\]
The even sites alone cover if \(r\ge|v|=1\), giving the last branch.

Suppose \(0<r<1\). A point \(q\in Q\) with \(|q|>r\) can be contracted along the ray from \(o\) to \(q_*=rq/|q|\). Both coordinates decrease, so \(|q_*-v|\ge |q-v|\) because \(v\) dominates all coordinates of \(Q\). Therefore the supremal distance to \(v\) of points not inside the first disk is the maximum of \(|q-v|\) over the arc \(C_r=Q\cap\{q:|q|=r\}\). This maximum controls the required \(s\), including equality by continuity. At \(r=0\), the same conclusion holds with the single point \(q=o\).

On \(C_r\),
\[
|q-v|^2=1+r^2-2(aq_x+bq_y).
\]
Parametrize the arc by \(q=r(\cos t,\sin t)\). The function \(a\cos t+b\sin t\) has a unique interior maximum for \(0<t<\pi/2\), not a minimum. Hence the farthest point from \(v\) on any contiguous arc is one of its two endpoints.

For \(0\le r\le a\), the two endpoints are \((r,0)\) and \((0,r)\). Since \(a<b\), the first is farther from \(v\), producing \(\sqrt{(a-r)^2+b^2}\). For \(a\le r\le b\), the endpoints are \((a,\sqrt{r^2-a^2})\) and \((0,r)\), and their distances to \(v\) are respectively \(b-\sqrt{r^2-a^2}\) and \(\sqrt{a^2+(b-r)^2}\). Their difference is strictly decreasing: the derivative of the first is less than \(-1\), and the derivative of the second is greater than \(-1\). Both expressions equal \(1/\sqrt3\) at \(r=1/\sqrt3\), giving the middle two phases.

For \(b\le r\le1\), the endpoints are \((a,\sqrt{r^2-a^2})\) and \((\sqrt{r^2-b^2},b)\). Their respective distances to \(v\) are \(b-\sqrt{r^2-a^2}\) and \(a-\sqrt{r^2-b^2}\). Their difference is strictly increasing on \((b,1)\) and equals zero at \(r=1\); hence the second is larger throughout the open interval, yielding the fourth phase. The formulas meet continuously at every switching point and are necessary as well as sufficient.

For the sharp density, minimize \(F(r)=r^2+S(r)^2\). On \([0,a]\) this is \(1+2r^2-2ar\), whose minimum is \(1-a^2/2=7/8\). On \([a,1/\sqrt3]\), substitute \(t=\sqrt{r^2-a^2}\): \(F=1+2t^2-2bt\), strictly decreasing because \(0\le t\le1/(2\sqrt3)<b/2\). On \([1/\sqrt3,b]\), \(F=1+2r^2-2br\), strictly increasing there. On \([b,1]\), substitute \(t=\sqrt{r^2-b^2}\), again giving \(F=1+2t^2-2at\), bounded below by \(7/8\). For \(r\ge1\), \(r^2+s^2\ge1\). Thus the unique global minimizer has \(r=1/\sqrt3\), \(s=S(r)=1/\sqrt3\), and \(F=2/3\). Multiplying by \(\pi/\sqrt3\) proves the stated bound.

## Verification

The standalone `check.py` reconstructs the two-center distance field on a dense rectangular grid without using the arc-endpoint calculation, checks all four exact junctions, and performs an independent grid search of the density objective. Run with `python check.py` using Python 3.9 or later; no external dependencies. The tests passed. This finite diagnostic is not a substitute for the continuum proof above.

## Relationship to prior work

Neff and Summers (2005) use exactly the alternating-row, two-radius triangular superlattice, with an orthogonal two-site rectangular fundamental cell, to study optical band structures. Their geometric design motivates this calculation; their paper does not derive a disk-union coverage condition, the present four-phase boundary, or its optimal-area law. Sriamorn (2014) develops the distinct problem of multiple lattice coverings by identical triangular shapes, not this heterogeneous disk cover. The classical equal-disk triangular covering is recovered at the unique minimizing equal-radius point, but that fact alone does not give the four-phase unequal-radius boundary or show that unbalancing the radii cannot reduce total disk area within the fixed pattern.

## Limitations

The area density is counted with multiplicity, so it need not equal the covered-area fraction. No claim is made for other geometric patterns or for unrestricted coverings with differently sized disks. The continuum proof is analytic; finite computations are corroborative. Literature coverage was bounded, and priority beyond the primary sources examined remains subject to independent historical review.

## References

1. C. W. Neff and C. J. Summers, *A photonic crystal superlattice based on triangular lattice*, Optics Express 13 (2005), 3166–3173, DOI: 10.1364/OPEX.13.003166; publicly dated 18 April 2005.
2. K. Sriamorn, *Multiple Lattice Packings and Coverings of the Plane with Triangles*, arXiv:1412.5096, first posted 16 December 2014.
3. R. Kershner, *The number of circles covering a set*, American Journal of Mathematics 61 (1939), 665–671, for the classical equal-circle covering context; the historical source was not required to calculate the four-phase boundary.
