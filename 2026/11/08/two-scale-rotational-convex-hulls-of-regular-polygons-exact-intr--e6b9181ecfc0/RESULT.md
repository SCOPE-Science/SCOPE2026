# Two-scale rotational convex hulls of regular polygons: exact intrinsic volumes and a sharp contact threshold

## Finding
For every integer \(n\ge3\), put \(b=\pi/n\), \(c=\cos b\), and \(s=\sin b\). Let \(Q_n\) be the regular polygon with circumradius one and vertices at arguments \(2\pi j/n\). For \(0<r\le1\) and relative rotation \(0\le\theta\le b\), consider
\[
K_n(r,\theta)=\operatorname{conv}\bigl(Q_n\cup rR_\theta Q_n\bigr).
\]
The restriction on the rotation loses no configurations up to Euclidean congruence. Write \(T=\cos(b-\theta)\) and \(g_r(u)=\sqrt{1+r^2-2r\cos u}\). Its *exact* Euclidean area and perimeter are
\[
\boxed{\begin{aligned}
\operatorname{area}K_n(r,\theta)&=ns\max\{c,rT\},\\
\operatorname{per}K_n(r,\theta)&=\begin{cases}
2ns,&rT\le c,\\
n\bigl(g_r(\theta)+g_r(2b-\theta)\bigr),&rT>c.
\end{cases}
\end{aligned}}
\]
When \(rT\le c\), the inner polygon lies inside the outer and the hull has precisely the outer \(n\) extreme vertices; at equality, its inner vertices meet supporting edges. When \(rT>c\), the hull has all \(2n\) input vertices as extreme points in alternating cyclic order.

If \(r\le c\), both intrinsic volumes are constant under rotation. If \(r>c\), define the *exact contact threshold*
\[
\theta_* = b-\arccos(c/r).
\]
Then both volumes remain at the outer-polygon values on \(0\le\theta\le\theta_*\) and are *strictly increasing* on \(\theta_*<\theta<b\). Their sole maximizing relative angle in \([0,b]\) is \(\theta=b\), with
\[
\boxed{\operatorname{area}_{\max}=ns\max\{c,r\},\qquad
\operatorname{per}_{\max}=\begin{cases}2ns,&r\le c,\\
2n\sqrt{s^2+(r-c)^2},&r>c.\end{cases}}
\]
The two intrinsic volumes turn on at different orders as the inner-to-outer radius crosses \(c\): as \(r\downarrow c\) from above,
\[
\operatorname{area}_{\max}-nsc=ns(r-c),\qquad
\operatorname{per}_{\max}-2ns=\frac{n}{s}(r-c)^2+O_n((r-c)^4).
\]
For each fixed \(c<r<1\), the area increase just after \(\theta_*\) is first-order in \(\theta-\theta_*\), whereas the perimeter increase is strictly second-order. Thus the onset of new extreme vertices is a differentiable-perimeter transition but not a differentiable-area transition.

## Assumptions and scope
The two polygons have identical numbers \(n\) of sides, identical centers, and positive circumradii in ratio \(r\in(0,1]\); all quantities use the ordinary Euclidean metric, with larger radius normalized to one. The operator \(R_\theta\) is planar counterclockwise rotation and \(\operatorname{per}\) denotes the Euclidean boundary length. The formulas hold at all boundary cases, including coincident vertices at \(r=1,\theta=0\), and line-contact configurations at \(r\cos(b-\theta)=\cos b\). A general larger circumradius \(R\) multiplies perimeters by \(R\) and areas by \(R^2\). Statements of strict increase apply to the indicated open ranges, with endpoint maxima included by continuity.

## Proof
**1. Cyclic chamber and contact.** The outer vertices are \(A_j=(\cos(2jb),\sin(2jb))\), while the inner vertices are \(B_j=r(\cos(2jb+\theta),\sin(2jb+\theta))\), with indices modulo \(n\). Because the two polygons have dihedral symmetry, interchanging \(\theta\) and \(2b-\theta\) gives congruent hulls. Hence \(0\le\theta\le b\) suffices.

The outer edge \(A_0A_1\) has outward unit normal at angle \(b\) and supporting value \(c\). The inner vertex \(B_0\) has scalar product \(r\cos(b-\theta)=rT\) with this normal. For \(0\le\theta\le b\), this is the maximal inner-vertex projection on the normal, and the same statement holds at every cyclically rotated edge. Thus the inner polygon is contained in the outer polygon **if and only if** \(rT\le c\). In the strict reverse inequality each \(B_j\) is exposed beyond the outer edge \(A_jA_{j+1}\). Each \(A_j\) remains extreme because its radius is one, no inner point has radius above one, and, except at the coincident degeneracy, no other point has its radial argument. Consequently the hull has exactly the alternating cyclic vertex order \(A_0,B_0,A_1,B_1,\ldots\) when \(rT>c\). On equality the inner vertices lie on outer edges, not as additional extreme vertices.

**2. Intrinsic volumes.** In the contained regime the hull is \(Q_n\), with area \(\frac n2\sin 2b=nsc\) and perimeter \(2ns\). In the alternating regime the shoelace formula gives
\[
\operatorname{area}K_n=\frac n2r\bigl[\sin\theta+\sin(2b-\theta)\bigr]
=nrs\cos(b-\theta)=nrsT.
\]
The two edge lengths in each repeated sector are \(|A_0-B_0|=g_r(\theta)\) and \(|B_0-A_1|=g_r(2b-\theta)\), yielding the claimed perimeter. The formulas agree continuously at the threshold because a point on an outer edge divides that edge into two collinear subsegments.

**3. Strict simultaneous maximization.** The threshold condition is monotone in \(\theta\), since \(T=\cos(b-\theta)\) increases strictly on \([0,b)\), from \(c\) to one. Therefore if \(r\le c\), no active interval exists. If \(r>c\), the stated \(\theta_*\) uniquely solves \(rT=c\) (and is zero at \(r=1\)). Area differentiation on the active interval gives \(nrs\sin(b-\theta)>0\) for \(\theta<b\).

For perimeter, set \(u=\cos\theta\), \(v=\cos(2b-\theta)\), and keep \(T=\cos(b-\theta)\). The elementary identities \(u+v=2cT\) and \(uv=T^2+c^2-1\) give the exact factorization
\[
\begin{split}
&\sin^2\theta\,g_r(2b-\theta)^2
-\sin^2(2b-\theta)\,g_r(\theta)^2\\
&\quad=2\bigl(\cos\theta-\cos(2b-\theta)\bigr)
(rT-c)(T-rc).
\end{split}
\]
Throughout the nonempty active interval below \(b\), every factor on the right is strictly positive: \(rT>c\), \(T\ge c\ge rc\), and \(\cos\theta>\cos(2b-\theta)\). The denominators \(g_r(\theta),g_r(2b-\theta)\) are positive in that interval. Consequently
\[
\frac{d}{d\theta}\operatorname{per}K_n
=nr\left(\frac{\sin\theta}{g_r(\theta)}-
\frac{\sin(2b-\theta)}{g_r(2b-\theta)}\right)>0.
\]
This establishes strict simultaneous maximization and the exact maximizing values on substituting \(\theta=b\).

**4. Different onset orders.** At the maximizing angle the area excess is exactly \(ns(r-c)\) for \(r>c\). The perimeter excess is \(2n(\sqrt{s^2+(r-c)^2}-s)\), whose Taylor expansion is \(n(r-c)^2/s+O_n((r-c)^4)\). Finally, for fixed \(c<r<1\), the threshold angle lies strictly between zero and \(b\). As \(\theta\downarrow\theta_*\) from above, \(rT-c\) has a positive first derivative \(r\sin(b-\theta_*)\), proving linear area onset. The perimeter-derivative factorization above has a simple zero at \(\theta_*\) and all its other factors and denominators are strictly positive there, proving a positive right second derivative and strictly quadratic perimeter onset.

## Verification
`VERIFY.py` independently constructs all \(2n\) input points and uses the convex-hull algorithm in SciPy to compute planar hull area and perimeter, without reusing the analytic edge ordering. Test cases include every integer \(3\le n\le39\), radius ratios below, at, and above the threshold \(\cos(\pi/n)\), including \(r=1\), and 41 orientations per radius. The reported execution verified 10,619 configurations (4,436 alternating and 6,183 contained), with zero discrepancies larger than \(2\times10^{-7}\) in area or perimeter. These finite numerical comparisons are supporting checks, not a substitute for the proof for all integers and real parameters.

## Relationship to prior work
Horváth and Lángi (arXiv:2012.08955, published 2022) introduce and analyze convex-hull functions of translated bodies and translated homothetic copies. Their definitions vary a **translation vector**, whereas this result fixes a common center and varies **relative rotation** and **scale**; their formulas do not give the threshold or joint area–perimeter profile here. Their earlier study (arXiv:1302.6164, 2013) treats convex-hull volume inequalities for congruent copies under translation or reflection, and notes a distinct problem for two regular simplices with the same centroid in higher dimension. Neither the two-scale planar rotational profile nor the perimeter transition follows from the inspected statements.

The previously available result *Universal radial coverage by concentric regular-polygon unions* (2026) proves coverage and area dominance for a **nonconvex union of congruent polygons**. A union is not a convex hull, and its radial coverage does not imply the two-scale convex-hull perimeter or its threshold. *Exact translative convex-hull profile of every regular polygon* (2026) concerns **translates** and has a different optimization variable. The elementary formulas for regular-polygon area and chord length are classical; novelty is claimed only for the complete combined two-parameter hull phase diagram and its unequal onset orders. Literature comparison is necessarily limited to sources actually inspected; an earlier exact result under a different name remains possible.

## Limitations
No claim is made for polygons with different numbers of sides, distinct centers, arbitrary affine transformations, random rotations, nonconcentric homothets, or three-dimensional analogues. The asymptotic \(O_n\) holds at fixed \(n\), and the near-angle quadratic onset requires \(\cos(\pi/n)<r<1\). At \(r=1\) two vertices coincide at zero rotation and the onset behavior there differs. The primary literature inspection establishes non-coverage by the named published statements but cannot certify absolute historical novelty. No independent mathematical audit has been performed.

## References
1. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, arXiv:2012.08955v1, first public 2020-12-16, and *Geometriae Dedicata* 216 (2022), article 20, DOI:10.1007/s10711-022-00673-y. https://arxiv.org/abs/2012.08955
2. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164v1 (2013), *Monatshefte für Mathematik* 174 (2014), 219–229. https://arxiv.org/html/1302.6164v3
3. *Universal radial coverage by concentric regular-polygon unions*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-radial-coverage-by-concentric-regular-polygon-unions--4705952c9b28
4. *Exact translative convex-hull profile of every regular polygon*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0
