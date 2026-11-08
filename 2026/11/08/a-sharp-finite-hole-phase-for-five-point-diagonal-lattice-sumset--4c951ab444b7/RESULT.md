# A sharp finite-hole phase for five-point diagonal lattice sumsets

## Finding
For every integer \(m\ge2\), put
\[
 A_m=\{(0,0),(1,0),(0,1),(m,m),(m+1,m+1)\},\qquad K_m=\operatorname{conv}(A_m).
\]
Let \(H_m(h)=|(hK_m\cap\mathbb Z^2)\setminus hA_m|\), for each integer \(h\ge0\). Then the hole count becomes **exactly constant**, with sharp first constant degree:
\[
\boxed{H_m(h)=\frac{m(m-1)(2m-1)}3\quad\text{for every }h\ge2m-2,}
\]
while \(H_m(2m-3)=m(m-1)(2m-1)/3-1\). The theorem gives all hole locations in every degree, not only their number.

Precisely, every missing lattice point is one of \((u+v,u)\) or \((u,u+v)\), with parameters
\[
1\le r\le m-1,\quad0\le q\le m-r-1,\quad u=(m+1)q+r,\quad v\ge0,
\]
and satisfying
\[
\boxed{q+1\le h-v\le q+2r-1.}
\]
This representation of a hole by \(q,r\) and its absolute coordinate difference \(v\) is unique, except that when \(v=0\), the two displayed orientations describe the same point. In particular, the exact all-degree cardinality is
\[
\boxed{H_m(h)=\sum_{r=1}^{m-1}\sum_{q=0}^{m-r-1}
\left(2\max\{0,\min(h,q+2r-1)-q\}-\mathbf 1_{q+1\le h\le q+2r-1}\right).}
\]
For instance, \(H_3(h)\) takes the values \(0,2,6,9,10,10,\ldots\) at degrees \(h=0,1,2,3,4,5,\ldots\).

## Assumptions and scope
The notation \(hA_m\) means sums of exactly \(h\) (not necessarily distinct) elements of \(A_m\), with \(0A_m=\{(0,0)\}\). The point \((m,m)\) is an interior point of the diagonal segment from \((0,0)\) to \((m+1,m+1)\), not an additional vertex of \(K_m\). Every statement is uniform in integers \(m\ge2\) and \(h\ge0\). The plane lattice is \(\mathbb Z^2\).

## Proof
**1. A shortest-length characterization.** For nonnegative integers \(x,y\), write \(u=\min(x,y)\), \(v=|x-y|\). Any representation by elements of \(A_m\) uses some \(k\) copies of \((m,m)\) and \(\ell\) copies of \((m+1,m+1)\). Let \(t=k+\ell\). The diagonal amount covered is \(z=mt+\ell\le u\), and after it is subtracted, \(x+y-2z\) unit-axis steps are needed. Therefore the fewest generators needed to reach \((x,y)\), allowing the zero generator to pad the length, is
\[
 v+f_m(u),\quad f_m(u)=\min_{t,\ell\ge0,\,0\le\ell\le t,\,mt+\ell\le u}\bigl(2(u-mt-\ell)+t\bigr).
\]
Write \(u=(m+1)q+r\), \(q\ge0\), \(0\le r\le m\). If \(t\le q\), the cost is minimized by \(t=q,\ell=q\), and equals \(q+2r\). A feasible \(t\ge q+1\) exists precisely when \(m(q+1)\le u\), equivalently \(q+r\ge m\); in that case \(t=q+1,\ell=u-m(q+1)\) reaches \(u\) exactly, at cost \(q+1\). No larger \(t\) can improve the latter cost. Since the first cost is smaller for \(r=0\), the resulting exact function is
\[
\boxed{f_m(u)=\begin{cases}q,&r=0,\\q+1,&r\ge1,\ q+r\ge m,\\q+2r,&r\ge1,\ q+r<m.\end{cases}}
\]
Consequently \((x,y)\in hA_m\) if and only if \(v+f_m(u)\le h\).

**2. The bounding polygon.** Its vertices are \((0,0),(1,0),(m+1,m+1),(0,1)\). For \(x\ge y\), the only nonautomatic upper supporting inequality is
\[
 (m+1)x-my\le(m+1)h,
\]
which becomes \(u+(m+1)v\le(m+1)h\). The other inequality is symmetric. Thus for all \(x,y\ge0\),
\[
\boxed{(x,y)\in hK_m\iff v+\lceil u/(m+1)\rceil\le h.}
\]
The lattice difference between polygon inclusion and sumset membership occurs precisely where \(\lceil u/(m+1)\rceil\le h-v<f_m(u)\). The only case with a strict difference is \(r\ge1\), \(q+r<m\), where \(\lceil u/(m+1)\rceil=q+1\) and \(f_m(u)=q+2r\). This proves the displayed complete hole-location description and its unique parameters.

**3. All-degree count and exact saturation.** For fixed admissible \(r,q\), the possible integers \(n=h-v\) lie in \([q+1,q+2r-1]\cap[0,h]\). Their number is \(\max\{0,\min(h,q+2r-1)-q\}\). Each \(n<h\) permits two orientations and \(n=h\) only one, proving the all-degree counting formula.

The largest upper endpoint \(q+2r-1\) in the admissible parameter domain is \(2m-3\), attained uniquely at \((r,q)=(m-1,0)\). Hence when \(h\ge2m-2\), every interval is fully available and each of its \(2r-1\) integers yields two orientations. Therefore
\[
 H_m(h)=2\sum_{r=1}^{m-1}(m-r)(2r-1)
 =\frac{m(m-1)(2m-1)}3.
\]
At \(h=2m-3\), the sole lost orientation is the central point with \(v=0\) in the unique extremal interval; the count is exactly one less. Therefore \(2m-2\) is the first degree after which the hole count remains constant. All statements include \(m=2\) and \(h=0\).

## Verification
Run `python verify.py` in the same directory. The checker generates \(hA_m\) by repeated ordinary set addition, constructs \(hK_m\cap\mathbb Z^2\) independently via integer inequalities, and compares every missing lattice point with the location formula; it also checks minimum lengths and the sharp threshold. It tested all \(2\le m\le8\), \(0\le h\le16\): 119 parameter-degree pairs and 64,855 independently enumerated polygon lattice points. The captured output is `verification_output.txt`. These finite checks corroborate, rather than prove, the all-parameter claims.

## Relationship to prior work
Nathanson's 2023 survey identifies the exact structure of holes in dilated lattice sumsets as a general problem. Curran and Goldmakher (2020/2021), in their theorem on \(d+2\)-element sumsets, determine an exact cardinality formula for **four** planar generators; it does not directly apply to the **five** generators here. Granville, Shakan and Walker (2023) prove general effective eventual polynomial growth and structure, but their bounds do not specify the present finite-hole invariant or its sharp \(2m-2\) onset. Levy and Nathanson (2015) prove saturation when all lattice points of the polygon are available as generators; here three of the polygon's many lattice points are generally absent from the five-point generating set. For comparison, the same polygon with the intermediate generator \((m,m)\) omitted has \(2m^2h+O_m(1)\) missing lattice points in degree \(h\), by Curran–Goldmakher's four-generator cardinality theorem and Pick's lattice count. The insertion therefore changes the leading hole-growth order from linear to constant. This four-generator asymptotic is a consequence of published results, not an independent novelty claim. The contribution asserted is the explicit five-generator boundary-hole location classification and its sharp eventual **constant** count; general sumset structure, elementary coin optimization, and lattice polygon inequalities are not claimed new.

## Limitations
This proves a complete classification only for the stated symmetric diagonal five-point family. It does not settle arbitrary five-point configurations or general Khovanskii boundary-hole questions. Searches of published literature and a semantic research index cannot rule out an unindexed equivalent special-case formula. No external independent audit has been carried out.

## References
1. M. B. Nathanson, *Extremal problems and the combinatorics of sumsets*, arXiv:2310.18277, first submitted 2023-10-27, Section 7 and Problem 13. https://arxiv.org/abs/2310.18277
2. M. J. Curran and L. Goldmakher, *Khovanskii's theorem and effective results on sumset structure*, arXiv:2009.02140, first submitted 2020-09-04, especially Theorem 1.2 and Section 6. https://arxiv.org/abs/2009.02140
3. A. Granville, G. Shakan, and A. Walker, *Effective results on the size and structure of sumsets*, Combinatorica 43 (2023), especially Theorems 1.1 and 1.3. https://doi.org/10.1007/s00493-023-00055-2
4. K. Levy and M. B. Nathanson, *Pick's theorem and sums of lattice points*, arXiv:1511.02747 (2015). https://arxiv.org/abs/1511.02747
