# The 120-degree boundary layer for random spherical-latitude triangles

## Finding

Three points are sampled independently and uniformly by arclength on one small circle of the unit two-sphere, with fixed colatitude \(0<\theta<\pi/2\) and \(c=\cos\theta\). Their geodesic triangle is formed by the unique shorter great-circle arcs. Let \(p(c)\) be the probability that every intrinsic angle is strictly below \(2\pi/3\), the unweighted Fermat--Torricelli floating/absorbed angle boundary.

**Theorem.** The function \(p(c)\) is continuous and strictly increasing on \((0,1)\). It has the small-cap (planar) limit \(2/3\) and the sharp equatorial law
\[
\lim_{c\uparrow1}p(c)=\frac23,\qquad
p(c)=\frac4{\pi^2}c^2+o(c^2)\quad(c\downarrow0).
\]

There is an explicit one-dimensional probability formula. Define \(\psi_c(a)=\operatorname{atan2}(\cos a,c\sin a)\), with values in \((-\pi/2,\pi/2)\), and set for \(0<a<\pi/3\)
\[
\beta_c(a)=\frac{2\pi}{3}-\psi_c(a),\qquad
b_c(a)=\arctan\!\left(\frac1{c\tan\beta_c(a)}\right).
\]
At the removable endpoint where \(\beta_c(a)=\pi/2\), take \(b_c(a)=0\). Then
\[
\boxed{p(c)=\frac{12}{\pi^2}\int_0^{\pi/3}
\left[\frac{\pi-a}{2}-\max\{a,b_c(a)\}\right]_+\,da.}
\]
Here \([z]_+=\max(z,0)\). This formula holds for every \(0<c<1\), not merely asymptotically.

More strongly, let \(a_1,a_2,a_3\) be the cyclic successive half-longitude gaps, and let \(J\) be the almost surely unique index of the smallest one (indices modulo three). Define
\[
X_c=\frac{a_J}{c},\qquad Y_c=\frac{a_{J+1}-\pi/2}{c},\qquad
D=\left\{(x,y):x>0,\ -\frac1{\sqrt3}<y<\frac1{\sqrt3}-x\right\}.
\]
Conditioned on the event defining \(p(c)\), the joint law of \((J,X_c,Y_c)\) converges **in total variation** to a uniform \(J\in\{1,2,3\}\) independent of the planar uniform law on \(D\), whose area is \(2/3\) and whose density equals \(3/2\). Thus an extremely rare near-equatorial admissible triangle has a microscopic longitude gap between two points while its third point is almost opposite them, with an explicit joint limiting geometry.

## Assumptions and scope

The sphere has curvature \(+1\); the sampled circle is a parallel, not the boundary of a planar disk or the interior of a spherical cap. Every point is uniform in longitude, which equals normalized arclength on a fixed parallel. For \(0<\theta<\pi/2\), all points lie in an open northern hemisphere, so their pairwise shorter geodesics are unambiguous except on a null set. The polar limit \(c\uparrow1\) is interpreted through limiting triangle angles; the latitude circle itself collapses at the pole. Because reflection across the equator preserves intrinsic angles, the corresponding southern-latitude law depends only on \(|\cos\theta|\). No claim is made about a globally minimizing Steiner network or uniqueness of a geometric median outside the angle criterion.

## Proof

**1. Exact tangent-angle formula.** Write \(s=\sqrt{1-c^2}\) and \(q(t)=(s\cos t,s\sin t,c)\). At a vertex \(q(t)\), form unit tangent vectors toward its neighbors at longitudes \(t-2a\) and \(t+2b\) by orthogonally projecting the two chord vectors into the tangent plane and normalizing. Direct dot products or a great-circle tangent calculation show that the angle between the two shortest geodesic rays is
\[
\angle(q(t-2a),q(t),q(t+2b))=\psi_c(a)+\psi_c(b),
\quad \psi_c(a)=\operatorname{atan2}(\cos a,c\sin a).
\]
This identity is valid for all \(0<a,b<\pi\) with \(a+b<\pi\), including cases where one of the separate \(\psi_c\) terms is negative. The three consecutive positive half-gaps \(a_i\) sum to \(\pi\); consequently the three interior angles are \(\psi_c(a_{i-1})+\psi_c(a_i)\). Their simplex density is the constant \(2/\pi^2\) in two gap coordinates, by the standard uniform-circle order-statistic formula.

**2. Exact integral and monotonicity.** The function \(\psi_c(a)\) is strictly decreasing in \(a\), because
\[
\partial_a\psi_c(a)=-\frac{c}{\cos^2 a+c^2\sin^2 a}<0.
\]
Sort the gaps as \(a\le b\le d\), where \(d=\pi-a-b\). The largest interior angle is \(\psi_c(a)+\psi_c(b)\). The region in sorted coordinates has \(0<a<\pi/3\) and \(a<b<(\pi-a)/2\); there are six orderings. Thus its probability equals \(12/\pi^2\) times the area of the region in which \(\psi_c(a)+\psi_c(b)<2\pi/3\). Solving \(\psi_c(b)<2\pi/3-\psi_c(a)\), whose right side lies between zero and \(\pi/2\), yields \(b>b_c(a)\) and the displayed integral.

For \(0<a\le b<\pi/2\), both cosines are positive, so \(\partial_c\psi_c(a)<0\) and \(\partial_c\psi_c(b)<0\). Hence the event increases with \(c\). Strictness follows because the maximal-angle level \(2\pi/3\) is attained on a nonempty smooth interior arc for each \(c\in(0,1)\), with negative derivative in \(c\); a small open set switches status between any two distinct values of \(c\). As \(c\uparrow1\), \(\psi_c(a)\to\pi/2-a\); the condition reduces to the Euclidean cyclic-triangle bound on the maximum angle. Each of three circular gaps above \(4\pi/3\) has probability \(1/9\), and they are disjoint; the complement has probability \(2/3\).

**3. Equatorial localization.** At \(c\downarrow0\), the ordered event requires its middle half-gap \(b\) to approach \(\pi/2\) and its smallest half-gap \(a\) to approach zero. Indeed \(a\le\pi/3\) implies \(\psi_c(a)=\pi/2+O(c)\) uniformly in this range, while \(\psi_c(a)+\psi_c(b)<2\pi/3\) implies \(\psi_c(b)<\pi/6+O(c)\). With \(b<\pi/2\) and the exact identity \(\cot b=c\tan\psi_c(b)\), it follows that \(b\ge\pi/2-O(c)\). Since the largest gap \(d\ge b\) and \(a+b+d=\pi\), we obtain \(a=O(c)\), \(b-\pi/2=O(c)\), and \(d-\pi/2=O(c)\). Thus the entire rare event lies in the union of three mutually disjoint compactly bounded scaled neighborhoods, indexed by the location of the uniquely tiny half-gap.

**4. Blow-up and total variation.** In the neighborhood indexed by \(J\), set \(a_J=cx\), \(a_{J+1}=\pi/2+cy\), \(a_{J+2}=\pi/2-c(x+y)\). For any fixed \(x>0\) and real \(y\),
\[
\psi_c(cx)\longrightarrow\frac\pi2,\quad
\psi_c(\pi/2+cy)\longrightarrow-\arctan y,\quad
\psi_c(\pi/2-c(x+y))\longrightarrow\arctan(x+y).
\]
The two angles adjoining the tiny gap are below \(2\pi/3\) precisely in the limiting open triangle \(D\), because their inequalities become \(y>-1/\sqrt3\) and \(x+y<1/\sqrt3\). The third angle is the difference of the two arctangents; on \(D\) it is between zero and \(\pi/3\), so the third condition adds no restriction. The boundary has Lebesgue area zero. The localization above bounds all scaled feasible coordinates uniformly; convergence of their indicators and dominated convergence therefore give \(L^1\) convergence of the unnormalized marked densities. In each chart their density is \((2/\pi^2)c^2\) and \(\operatorname{area}(D)=\frac12(2/\sqrt3)^2=2/3\). Summing the three charts yields
\[
p(c)=3\frac2{\pi^2}c^2\frac23+o(c^2)=\frac4{\pi^2}c^2+o(c^2).
\]
Dividing the convergent marked densities by this mass proves the claimed total-variation limit, with joint density \(1/2\) on each copy of \(D\), equivalent to an independent uniform index and a planar uniform point in \(D\).

## Verification

The standalone `checker.py` independently reconstructs spherical angles from three-dimensional tangent-vector dot products and compares them to the half-gap expression for several nondegenerate triples and four values of \(c\). A Simpson integral independently tests the one-dimensional formula at \(c\in\{0.2,0.5,0.8,1\}\) and the small-\(c\) coefficient along \(c=0.1,0.05,0.02,0.01\). The checker prints `SPHERICAL_LATITUDE_120_LAW_CHECKS_OK` on success. These finite checks corroborate the formulas but neither constitute the infinite-domain proof nor an independent mathematical audit. Reproduce using `python checker.py`; no nonstandard dependencies are required.

## Relationship to prior work

Zachos (2014) discusses deterministic weighted spherical Fermat--Torricelli minimizers and gives the floating/absorbed unit-tangent conditions. For equal weights, the associated local angle boundary is \(2\pi/3\), but the cited work does not develop the random fixed-latitude angular distribution, equatorial rare-event probability, or marked conditional law. Finch and Jones (2010) investigate spherical triangles with vertices uniform over the **entire sphere**, primarily their area and perimeter. The published paper *A sharp latitude threshold and exact acute-triangle law on spherical small circles* treats the same small-circle sampling object but requires all three intrinsic angles to be **below \(\pi/2\)**, yielding a forbidden latitude belt and a distinct quadratic onset near \(\cos^2\theta=1/3\). This is not a statement about the \(2\pi/3\) boundary or the equatorial limit \(\cos\theta\downarrow0\). Its primary result and proof have been inspected and compared, not merely matched by title. The present result gives a separate threshold-specific integral and an additional conditional geometric limit.

## Limitations

The result applies only to exactly three independent uniform-longitude points on a fixed non-equatorial latitude, not arbitrary sampling densities or points drawn from a spherical cap. The finite-\(c\) probability is expressed by a convergent one-dimensional integral, not a claimed elementary closed form. The theorem classifies the \(120^\circ\) angle event and does not assert an otherwise unproved equivalence to every global Steiner-network optimization decision on a sphere. Historical priority cannot be established by database search alone, and no independent mathematical validation has been performed.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, originally posted 2010-09-27. https://arxiv.org/abs/1009.5329
2. A. N. Zachos, *An analytical solution of the weighted Fermat–Torricelli problem on the unit sphere*, arXiv:1408.6495, originally posted 2014-08-27. https://arxiv.org/abs/1408.6495
3. *A sharp latitude threshold and exact acute-triangle law on spherical small circles*, published mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-latitude-threshold-and-exact-acute-triangle-law-on-spher--711f5d6843db
