# Two reach scales and a cubic threshold in four-parameter L-polygons

## Finding
For any four positive real parameters \(a,b,u,v\), form the compact planar polygon
\[
L=([0,a+u]\times[0,b])\cup([0,a]\times[0,b+v]).
\]
This is a simple, connected, six-vertex orthogonal polygon with a unique reentrant corner. Its ordinary reach, conic reach (with the certificate definition of [1]), and polynomial reach (maximum initial interval of degree-at-most-two outer parallel area) are exactly
\[
\operatorname{reach}(L)=0,\qquad
\operatorname{conreach}(L)=\frac{\min\{a,b,u,v\}}{3},\qquad
\operatorname{polreach}(L)=\min\{u,v\}.
\]
Put \(R=\min\{u,v\}\), \(W=a+u\), and \(H=b+v\). Writing \(V_L(t)=\operatorname{area}(L+tB_2)-\operatorname{area}(L)\), for every \(0\le t\le R\),
\[
V_L(t)=2(W+H)t+\left(\frac{5\pi}{4}-1\right)t^2.
\]
For \(t=R+s\) with \(s\downarrow0\), the first departure from this quadratic is **positive and cubic**:
\[
V_L(R+s)-\left[2(W+H)(R+s)+\left(\frac{5\pi}{4}-1\right)(R+s)^2\right]
=\begin{cases}
\dfrac{s^3}{6R}+O(s^4),&u\ne v,\\[3pt]
\dfrac{s^3}{3R}+O(s^4),&u=v.
\end{cases}
\]
Thus the cubic onset coefficient doubles on the equal-arm locus. For \(u=v=1\) and \(a=b=\varepsilon\in(0,1)\), polynomial reach remains \(1\) while conic reach is \(\varepsilon/3\); their ratio tends to infinity as \(\varepsilon\downarrow0\). In particular, there is no universal upper comparison \(\operatorname{polreach}\le C\operatorname{conreach}\) on this class.

## Assumptions and scope
All four lengths are strictly positive. The metric is Euclidean. The radius-\(t\) parallel set is the Minkowski sum with the closed unit disk of radius \(t\); boundary sets have area zero. Ordinary reach is the largest distance on which all nearest-point projections are unique. Polynomial reach is the supremum of \(r\) such that \(V_L\) agrees on \([0,r]\) with a polynomial of degree at most two. Conic reach follows the precise conic-certificate conditions (C1) and (C2) of [1, Definition 4.1], including the enlarged radius \(3r_\sigma\) around a singular apex and the normal-fiber lower bound outside its core. The symbol \(O(s^4)\) is for each fixed positive parameter quadruple, not uniform as any length tends to zero.

## Proof
**1. Exact parallel-area reduction.** Set \(A=[0,W]\times[0,b]\), \(B=[0,a]\times[0,H]\), \(C=A\cap B=[0,a]\times[0,b]\), and let \(A_t,B_t,C_t\) be their Euclidean parallel sets. Since \((A\cup B)_t=A_t\cup B_t\), inclusion–exclusion applies. When \(x\le a\), \(\operatorname{dist}((x,y),A)=\operatorname{dist}((x,y),C)\) whenever \(y>b\), and when \(x>a\) and \(y\le b\), \(\operatorname{dist}((x,y),B)=\operatorname{dist}((x,y),C)\). The same equalities hold in the remaining regions outside the upper-right quadrant. Consequently \((A_t\cap B_t)\setminus C_t\) is entirely contained, up to null sets, in \(\{x>a,y>b\}\).

Translate by the reentrant vertex \(q=(a,b)\) and put \(X=x-a>0\), \(Y=y-b>0\). The relevant distances become
\[
d_A^2=Y^2+(X-u)_+^2,\quad d_B^2=X^2+(Y-v)_+^2,\quad d_C^2=X^2+Y^2,
\]
where \(z_+=\max\{z,0\}\). Define the area
\[
T_{u,v}(t)=\operatorname{area}\{(X,Y)\in[0,\infty)^2:Y^2+(X-u)_+^2\le t^2,\ X^2+(Y-v)_+^2\le t^2\}.
\]
The part of this quadrant lying in \(C_t\) is a quarter disk of area \(\pi t^2/4\). Hence
\[
\operatorname{area}(A_t\cap B_t)=\operatorname{area}(C_t)+T_{u,v}(t)-\pi t^2/4.
\]
Apply the rectangle Steiner formula \(\operatorname{area}(Q_t)=\operatorname{area}(Q)+\operatorname{Per}(Q)t+\pi t^2\) to each of \(A,B,C\). Their signed perimeter sum is \(2(W+H)\), giving the **all-radius identity**
\[
\boxed{V_L(t)=2(W+H)t+\frac{5\pi}{4}t^2-T_{u,v}(t).}\tag{1}
\]
This shows in particular that changing the two overlap widths \(a,b\) affects the parallel area only through the linear perimeter term; all nonlinear interactions depend solely on the arm extensions \(u,v\).

**2. Exact maximal quadratic interval.** By both distance inequalities defining \(T_{u,v}(t)\), \(0\le X,Y\le t\). If \(0\le t\le R:=\min\{u,v\}\), both positive-part terms vanish, so the feasible region is exactly \([0,t]^2\) and \(T_{u,v}(t)=t^2\). Formula (1) yields the claimed quadratic on \([0,R]\).

Suppose \(u<v\), and choose \(u<t<v\). The vertical-arm inequality then only restricts \(X\le t\), and the horizontal-arm inequality restricts \(Y\le\sqrt{t^2-(X-u)_+^2}\). Thus
\[
T_{u,v}(t)=ut+\int_0^{t-u}\sqrt{t^2-z^2}\,dz,
\]
and
\[
t^2-T_{u,v}(t)=\int_0^{t-u}\bigl(t-\sqrt{t^2-z^2}\bigr)dz
=\frac{(t-u)^3}{6u}+O((t-u)^4)>0.
\]
The case \(v<u\) follows by exchanging the two axes.

For \(u=v=R\) and \(R<t\) sufficiently close to \(R\), symmetry gives the crossing point \(X=Y=R+\eta\) with \(\eta=(\sqrt{2t^2-R^2}-R)/2\). Vertical integration, split at that crossing, gives the exact expression
\[
T_{R,R}(t)=R(2t-R-\eta)+\int_0^\eta\sqrt{t^2-z^2}\,dz
+\int_{R+\eta}^{t}\sqrt{t^2-z^2}\,dz.
\]
For \(t=R+s\), \(\eta=s-s^2/(2R)+O(s^3)\). The first integral equals \(t\eta-\eta^3/(6t)+O(s^5)\). The second is \(s^3/(3R)+O(s^4)\), as seen by substituting \(z=t-h\), using \(t-(R+\eta)=s^2/(2R)+O(s^3)\), and integrating \(\sqrt{2th-h^2}\). Substitution yields
\[
T_{R,R}(R+s)=(R+s)^2-\frac{s^3}{3R}+O(s^4).
\]
In both cases \(t^2-T_{u,v}(t)\) is strictly positive just above \(R\), so no polynomial of degree at most two can agree with \(V_L\) on a longer initial interval: it would agree with the already determined quadratic on \((0,R)\), and hence be identical to it everywhere. This proves \(\operatorname{polreach}(L)=R\) and the stated cubic coefficients.

**3. Exact conic reach.** Let \(m=\min\{a,b,u,v\}\), \(\rho=m/3\), and \(q=(a,b)\). Choose the one-point singular set \(\{q\}\), core radius \(r_q=\rho\), and the translated three-quarter-plane cone \(q+\{(X,Y):X\le0\text{ or }Y\le0\}\). The polygon agrees *exactly* with that cone inside \(\overline B(q,3\rho)=\overline B(q,m)\), verifying (C1); the separation condition is vacuous.

For (C2), the only finite small proximal normal fibers are the perpendicular outward fibers of the two notch walls. For a point at distance \(d\) along either wall from \(q\), the fiber length is at least \(\min\{d,u,v\}\) (before reaching the opposite arm there is no competing closer foot). Thus wall feet outside \(B(q,\rho)\) have lengths at least \(\rho\). Every other straight open side has a globally supporting outward normal and an infinite fiber. At the three globally extreme convex vertices, all exterior fan directions are globally supporting and also have infinite fibers. At the two convex corners terminating the notch walls, a competing foot on the opposite arm lies at a horizontal or vertical separation at least \(u\) or \(v\), respectively, for the entire outward fan ray, implying fiber length at least \(\min\{u,v\}\ge\rho\). Hence (C2) holds and \(\operatorname{conreach}(L)\ge m/3\).

Conversely take any conic certificate of radius \(\rho'>0\). The two perpendicular notch walls have normal fibers of length tending to zero as their feet approach \(q\). Therefore \(q\) must belong to the closure of at least one singular core \(B(\sigma,r_\sigma)\), or (C2) fails. It lies strictly inside the enlarged conic ball \(B(\sigma,3r_\sigma)\). Two noncollinear straight boundary segments through \(q\) in a locally conical set force the cone apex \(\sigma\) to equal \(q\): otherwise rays from \(\sigma\) through a whole segment would sweep an open planar patch of the boundary, impossible for a closed cone. The cone is then uniquely the local three-quarter-plane wedge. Its agreement with the polygon inside \(\overline B(q,3r_q)\) forces \(3r_q\le m\): beyond the first of the four edge distances \(a,b,u,v\), one of the rays of the wedge continues into a region absent from the polygon. Since every admissible certificate requires \(\rho'\le r_q\), \(\rho'\le m/3\). This proves the reverse bound and therefore equality.

**4. Ordinary reach and separation.** For sufficiently small \(s>0\), the point \((a+s,b+s)\) has distinct nearest points \((a+s,b)\) and \((a,b+s)\) of the polygon, both at distance \(s\). Thus its ordinary reach is zero. Taking \(u=v=1\) and \(a=b=\varepsilon\in(0,1)\) gives \(\operatorname{polreach}/\operatorname{conreach}=3/\varepsilon\to\infty\), proving the absence of any universal reverse comparison.

## Verification
The supplied `verify.py` computes the quadrant intersection independently by one-dimensional numerical quadrature, compares the two explicit first-contact formulas, checks the predicted cubic coefficients at several scales, and checks the exact rational expressions for the reach parameters. Run `python verify.py` with Python 3 (standard library only). These finite numerical/rational checks corroborate, but do not prove, the all-real-parameter statements; the complete argument is above.

## Relationship to prior work
Cholaquidis [1, Example 4.5 and Proposition 6.3, including Appendix B.5] proved the reach values \(0,1/3,1\) and the first cubic departure for the *single normalized L-shape* \(a=b=u=v=1\). Theorem 8.2 of [1] proves **some** initial quadratic interval for a broader wedge-like class, not the four-parameter maximal endpoints or the exact conic-certificate maximum here. The present result gives the full parameter-dependent reach pair, exact cubic equality/inequality transition, and the absence of any universal reverse bound. The definition of polynomial reach and motivation from statistical estimation are due to [2]. The global all-radius planar polynomiality result of [3] is distinct from local polynomial reach and does not imply the formulas.

## Limitations
The theorem is specifically for Euclidean planar outer parallel area and the stated *orthogonal connected* L-polygons. It makes no assertion about other norms, higher-dimensional bodies, disjoint sets or general polygonal conic certificates. The cubic remainder constants depend on the fixed positive parameters. Priority over every possible earlier equivalent statement has not been independently established; in particular, the general formulas are elementary enough that an unindexed geometric account cannot be excluded. No external mathematical audit has been performed.

## References
[1] Alejandro Cholaquidis, *Conic reach and polynomial parallel volume in the plane*, arXiv:2607.24487v1, first posted 2026-07-27. https://arxiv.org/abs/2607.24487 (Definition 4.1, Example 4.5, Theorem 8.2, Proposition 6.3 and Appendix B.5).

[2] Alejandro Cholaquidis, Antonio Cuevas and Leonardo Moreno, *On the notion of polynomial reach: a statistical application*, arXiv:2307.00373, first posted 2023-07-01. https://arxiv.org/abs/2307.00373.

[3] Matthias Heveling, Daniel Hug and Günter Last, *Does polynomial parallel volume imply convexity?*, Mathematische Annalen 328 (2004), 469–479, DOI: 10.1007/s00208-003-0497-7.
