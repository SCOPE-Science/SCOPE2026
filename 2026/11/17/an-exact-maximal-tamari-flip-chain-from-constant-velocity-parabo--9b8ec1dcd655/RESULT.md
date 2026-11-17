# An exact maximal Tamari flip chain from constant-velocity parabolic sites

## Finding

For any integer \(n\ge4\), choose distinct increasing real numbers \(a_1<\cdots<a_n\) with distinct sums over distinct four-element subsets. At real time \(t\), let the moving planar sites be
\[
Q_i(t)=(a_i,a_i^2+2ta_i),\qquad i=1,\ldots,n.
\]
Their ordinary Euclidean Delaunay triangulation changes **exactly** \(\binom{n-2}{2}\) times, one flip for each pair of nonoverlapping adjacent index pairs \((i,i+1)\) and \((j,j+1)\), where \(i+1<j\). The full event schedule is
\[
t_{ij}=-\tfrac14(a_i+a_{i+1}+a_j+a_{j+1}),
\]
and each flip replaces diagonal \((i+1,j+1)\) by diagonal \((i,j)\) as \(t\) increases. All events have different times. Initially the triangulation is the fan with apex \(n\); finally it is the fan with apex \(1\). Up to the conventional choice of order orientation, this is a saturated, maximum-length chain of the Tamari lattice.

## Assumptions and scope

All distances, empty-circle tests and triangulations are Euclidean. Every \(a_i\) is real and the parameters are strictly ordered. The four-subset-sum genericity is essential to isolate events; it is satisfiable for every \(n\), e.g. take \(a_i=3^{i-1}\). At the isolated event instants the empty circumcircle has four sites on its boundary, so the Delaunay triangulation itself is not unique; the statement concerns its unique triangulations in the neighboring open time intervals. All sites remain in strictly convex position, and each has a constant, vertical velocity \((0,2a_i)\).

The moving set differs by the common translation \((t,t^2)\) from the sites \((a_i+t,(a_i+t)^2)\) on the standard parabola; translation preserves Euclidean empty circles and triangulations. The indexed polygon is therefore a convex \(n\)-gon throughout.

## Proof

**1. The exact cocircularity equation.** Write \(u_i=a_i+t\), so the translated sites are \((u_i,u_i^2)\). A Euclidean circle has an equation \(x^2+y^2+Ax+By+C=0\). Restricted to the parabola, the left side is the monic quartic
\[
F(u)=u^4+(1+B)u^2+Au+C,
\]
whose cubic coefficient is identically zero. Given four distinct parameters \(u_r\) with \(r\in I\), a circle through all four exists precisely when the cubic coefficient of \(\prod_{r\in I}(u-u_r)\) vanishes, i.e. when \(\sum_{r\in I}u_r=0\). The remaining coefficients then uniquely determine a circle. Therefore the event for four indices \(r_1<r_2<r_3<r_4\) happens precisely at
\[
t_I=-\frac14\sum_{r\in I}a_r.
\]
All \(\binom n4\) cocircularity times are distinct by assumption.

**2. Which events are Delaunay events?** At the cocircular time for a quartet with ordered abscissas \(u_1<u_2<u_3<u_4\), the circle polynomial is exactly
\[
F(u)=(u-u_1)(u-u_2)(u-u_3)(u-u_4).
\]
The point \((u,u^2)\) is strictly inside this disk precisely when \(F(u)<0\), or equivalently when \(u\in(u_1,u_2)\cup(u_3,u_4)\). Thus the cocircular disk contains no other site if and only if the first two and last two members are consecutive in the full index order. Precisely the eligible quartets are
\[
I=\{i,i+1,j,j+1\},\qquad 1\le i<i+1<j<j+1\le n.
\]
Each forms a convex quadrilateral with an empty circumdisk; conversely, all other four-site cocircularities have a fifth site inside their circle and cannot change the Delaunay triangulation.

**3. Direction and occurrence of every flip.** For any ordered parameters \(u_1<u_2<u_3<u_4\), the circle through the first three has restriction
\[
F_{123}(u)=(u-u_1)(u-u_2)(u-u_3)(u+u_1+u_2+u_3).
\]
At \(u_4\), the first three factors are positive, so the fourth site lies inside this circle exactly when \(u_1+u_2+u_3+u_4<0\). Therefore, near an eligible cocircularity, the local Delaunay diagonal is \((2,4)\) just before the event and \((1,3)\) just afterward. Because the critical disk is empty and all other four-site sums are nonzero at that time, this event produces exactly one edge flip and no other simultaneous change. The generic Delaunay triangulation is locally constant between such events. Consequently, all and only the eligible pairs flip, with diagonal \((i+1,j+1)\) replaced by \((i,j)\).

**4. Number, endpoints and lattice chain.** Choosing \(i\in\{1,\ldots,n-3\}\) and \(j\in\{i+2,\ldots,n-1\}\) gives
\[
\sum_{i=1}^{n-3}(n-i-2)=\binom{n-2}{2}
\]
events. For sufficiently negative time, every quartet has negative parameter sum. The fan at vertex \(n\) has every interior edge locally Delaunay, since for each consecutive pair of its triangles the admissible diagonal is the ordered four-vertex diagonal \((2,4)\). Hence this fan is globally Delaunay by the standard local-to-global Delaunay criterion. For sufficiently positive time, all sums are positive, and the same argument gives the fan at vertex \(1\), using the ordered diagonal \((1,3)\).

Each flip is the same consistently directed Tamari cover, with orientation possibly reversed from the chosen literature convention. The two endpoint fans are the lattice extremal triangulations. The classical maximal chain-length theorem for triangulations of a convex \(n\)-gon gives \(\binom{n-2}{2}\), so the constructed chain has maximum possible length. The length theorem itself is previously known and is not claimed here as new.

## Verification

The standalone Python program `check_kinetic.py` uses only the standard library and exact rational arithmetic. With \(a_i=3^{i-1}\), it separately constructs the empty circumcircles for **every** triple in configurations of \(n=4,5,6,7,8\) sites, checks all other sites for strict disk exclusion, and extracts all interior Delaunay edges at a time between every pair of successive predicted critical instants. It verifies the exact expected flip deletions and insertions, initial/final fans, and counts \(1,3,6,10,15\). Its output ends with `PARABOLIC_KINETIC_DELAUNAY_CHECKS_OK`. These finite exact checks corroborate, but do not replace, the all-\(n\) algebraic argument.

An explicit event generator can enumerate every admissible pair and sort the exact time values in \(O(n^2\log n)\) comparisons, after which each event specifies the diagonal update. This running-time statement concerns the event description, not an implementation of a generic kinetic Delaunay data structure.

## Relationship to prior work

The circle test, Delaunay parabolic lifting, and local edge-flip rules are classical; see Musin (2003). Rambau and Reiner (2011) discuss the parabola-based Tamari lattice, including its oriented flips; the connection of Tamari order with triangulations is not new here. Nelson's exposition of the Fishel–Nelson maximal chain-length result already gives the extremal count. Vomáčka and Kolingerová (2008) and Rubin (2013) study kinetic Delaunay changes for general moving point sets, including the fact that quadratic-scale behavior is not itself a new discovery. None of these inspected source materials states the complete linear-velocity parabolic construction with its exact active-event pairs, four-sum schedule, and maximal-chain realization. The contribution is this combined explicit trajectory; no priority beyond the inspected sources is asserted.

## Limitations

A genericity condition on all four-subset sums excludes simultaneous events; the proof makes no classification of non-generic simultaneous events. No lower or upper bound for arbitrary kinetic Delaunay motion is claimed. The construction does not assert that every maximum-length Tamari chain is realizable. No higher-dimensional or perturbation-robustness result is established. The search and primary-text comparisons cannot exclude an older specialized equivalent construction; independent mathematical and historical review has not been performed.

## References

- O. R. Musin, *Construction of the Voronoi Diagram and Secondary Polytope*, arXiv:math/0312052v1 (first public version December 2, 2003), https://arxiv.org/abs/math/0312052.
- O. R. Musin, *Properties of the Delaunay Triangulation*, arXiv:math/0312050v1 (December 2, 2003), https://arxiv.org/abs/math/0312050.
- J. Rambau and V. Reiner, *A Survey of the Higher Stasheff–Tamari Orders* (October 18, 2011 draft), https://epub.uni-bayreuth.de/id/eprint/257/1/rambau_reiner.pdf.
- T. Vomáčka and I. Kolingerová, *Computation of Topologic Events in Kinetic Delaunay Triangulation Using Sturm Sequences of Polynomials* (2008), https://ep.liu.se/ecp/034/014/ecp083414.pdf.
- N. Rubin, *On Topological Changes in the Delaunay Triangulation of Moving Points*, arXiv:1304.3671v1 (April 12, 2013), https://arxiv.org/abs/1304.3671.
- S. Fishel and L. Nelson, *Chains of Maximum Length in the Tamari Lattice*, Proc. Amer. Math. Soc. (2014), DOI: 10.1090/S0002-9939-2014-12069-7; full chapter text available in L. Nelson's dissertation (2016), https://files01.core.ac.uk/download/pdf/79586822.pdf.
