# A sixteen-point reversal in local skyline–comparability dependence

## Finding

For \(n\ge3\), sample independent uniform points \(X_1,\ldots,X_n\) in the unit square. Call a point *Pareto maximal* if no other sample point is at least as large in both coordinates. Define \(I_i=\mathbf1\{X_i\text{ is Pareto maximal}\}\), and define \(J_{ij}=\mathbf1\{X_i,X_j\text{ are coordinatewise comparable}\}\). Write \(H_n=\sum_{k=1}^n1/k\).

The two geometrically different overlaps of these indicators have exact covariances
\[
 s_n:=\operatorname{Cov}(I_1,J_{12})=\frac{(n+3)H_n-4n}{2n(n-1)},\qquad
 t_n:=\operatorname{Cov}(I_1,J_{23})=\frac{3n-(n+2)H_n}{n(n-1)(n-2)}.
\]
The shared-label covariance \(s_n\) is strictly negative for \(3\le n\le15\) and strictly positive for every \(n\ge16\), without equality at any integer. The disjoint-label covariance \(t_n\) stays strictly negative. Yet for the total skyline size \(M=\sum_{i=1}^n I_i\) and comparable-pair count \(C=\sum_{1\le i<j\le n}J_{ij}\),
\[
\operatorname{Cov}(M,C)=-\frac{n-H_n}{2}<0.
\]

A dimension-robust part of this overlap phenomenon holds beyond the plane: for any integer \(d\ge2\), if the points are iid uniform in \((0,1)^d\), then \(\operatorname{Cov}(I_1,J_{23})<0\) whenever \(n\ge3\). The explicit planar formulas and the cutoff \(16\) are not asserted for higher dimensions.

## Assumptions and scope

Comparability means either point is at most the other in every coordinate, including both possible directions. Ties have probability zero. Maximality is simultaneous among all \(n\) sampled points, not only among a designated subset. All statements concern exact finite-sample probabilities. No independence of \(I_i\) and \(J_{jk}\) is presumed merely because their labels are disjoint.

## Proof

**Total covariance in the plane.** Order the observations by their first coordinate. Their second-coordinate ranks form a uniformly random permutation \(\pi\). Let \(R_i\) be the rank of \(\pi(i)\) among the suffix \(\pi(i),\ldots,\pi(n)\), with possible values \(1,\ldots,L_i\) and \(L_i=n-i+1\). The suffix ranks are mutually independent and each uniformly distributed on its stated range (a standard inversion-code bijection). A point is maximal exactly when it is a right-to-left record, so
\[
 M=\sum_i \mathbf1\{R_i=L_i\}.
\]
Each comparable pair corresponds to a noninversion, whence \(C=\binom n2-\sum_i(R_i-1)\). Independence of the suffix ranks gives
\[
 \operatorname{Cov}(M,C)
 =-\sum_{L=1}^n\operatorname{Cov}(\mathbf1\{R=L\},R-1)
 =-\frac12\sum_{L=1}^n\frac{L-1}{L}
 =-\frac{n-H_n}{2}.
\]
Here \(R\) in each summand is uniform on \(\{1,\ldots,L\}\).

**A marked maximal point and an incident comparable pair.** Let \(U=1-X_{11}\) and \(V=1-X_{12}\), the independent coordinate distances of the first point from the upper corner. For the first point to be maximal, all other points must avoid its upper orthant, whose volume is \(UV\). If the pair \((1,2)\) is comparable while point \(1\) is maximal, point \(2\) must be below point \(1\), a region of area \((1-U)(1-V)\). Therefore
\[
 a_n:=\mathbb P(I_1=1,J_{12}=1)
 =\int_0^1\!\int_0^1(1-u)(1-v)(1-uv)^{n-2}\,du\,dv.
\]
Write \(B_m=\int_0^1\!\int_0^1(1-uv)^m\,du\,dv=H_{m+1}/(m+1)\). Direct integration yields \(\int\!\int u(1-uv)^{n-2}\,du\,dv=1/n\), while \(\int\!\int uv(1-uv)^{n-2}\,du\,dv=B_{n-2}-B_{n-1}\). Consequently
\[
 a_n=2\frac{H_{n-1}}{n-1}-\frac{H_n}{n}-\frac2n.
\]
Since \(\mathbb E I_1=H_n/n\) and \(\mathbb E J_{12}=1/2\), subtraction gives the asserted formula for \(s_n\).

**The sharp switch at sixteen.** Put \(F_n=(n+3)H_n-4n\). Its first difference satisfies
\[
 F_{n+1}-F_n=H_n-3+\frac3{n+1},\qquad
 (F_{n+2}-F_{n+1})-(F_{n+1}-F_n)=\frac{n-1}{(n+1)(n+2)}>0.
\]
Thus the sequence is strictly convex for integers \(n\ge2\). Exact endpoint evaluations give \(F_2=-1/2\), \(F_{15}=-5443/20020<0\), and \(F_{16}=168541/720720>0\). Strict convexity keeps every intermediate integer \(2\le n\le15\) below the negative chord, and after the positive increment from \(15\) to \(16\) all later increments are positive. Thus there is precisely one integer sign switch, between \(15\) and \(16\).

**The disjoint pair in the plane.** Exchangeability separates the two overlap types:
\[
 \operatorname{Cov}(M,C)=n(n-1)s_n+\frac{n(n-1)(n-2)}2t_n.
\]
Substituting the proven formulas for the total covariance and \(s_n\) gives the displayed formula for \(t_n\). For strict negativity put \(G_n=(n+2)H_n-3n\). Here \(G_3=1/6>0\), and the first difference \(G_{n+1}-G_n=H_n-2+2/(n+1)\) is positive at \(n=3\) and strictly increases thereafter, because its successive difference equals \(n/((n+1)(n+2))>0\). Hence \(G_n>0\) for every \(n\ge3\), and \(t_n<0\).

**Dimension-independent disjoint suppression.** Now let \(d\ge2\). For a fixed point \(x\), put \(v(x)=\prod_{r=1}^d(1-x_r)\) and \(p_d=2^{1-d}=\mathbb P(J_{23}=1)\). The conditional probability that two independent points are comparable and neither dominates \(x\) is
\[
 p_d\left(1-\prod_{r=1}^d(1-x_r^2)\right).
\]
To see this, start with probability \(p_d\), subtract comparable configurations with at least one point in the upper orthant of \(x\), and use inclusion-exclusion; the two-point upper-orthant term cancels. The remaining \(n-3\) points must also avoid that upper orthant. Thus
\[
 \mathbb P(I_1=1,J_{23}=1)
 =p_d\int_{[0,1]^d}(1-v(x))^{n-3}
 \left(1-\prod_r(1-x_r^2)\right)dx.
\]
The product inequality \(\prod_r(1+x_r)>2-\prod_r(1-x_r)=2-v(x)\) holds for interior \(x\) and \(d\ge2\). It follows by induction from \((2-a)(2-b)\ge 2-ab\) for \(0\le a,b\le1\), with strictness when both are interior. Multiplying by \(v(x)>0\) yields
\[
 \prod_r(1-x_r^2)>2v(x)-v(x)^2.
\]
Consequently the last displayed integral is strictly less than
\(p_d\int_{[0,1]^d}(1-v(x))^{n-1}dx=p_d\mathbb E I_1\). This proves \(\operatorname{Cov}(I_1,J_{23})<0\) in every stated dimension.

## Verification

The standalone Python file `pareto_overlap_verifier.py` evaluates exact rational covariance formulas and independently enumerates all coordinate-rank configurations for specified small \((n,d)\). It checks all three overlap quantities, the planar sign cutoff through \(n=100\), and the negative disjoint relation through \(d=8,n=50\). Run with `python3 pareto_overlap_verifier.py`. The completed run yielded 957 exact assertions, with no floating-point tolerance or randomness. Exhaustive finite enumeration corroborates the formulas; the proof above, not the enumeration, establishes them for all integers in scope.

## Relationship to prior work

Bai, Devroye, Hwang and Tsai study the marginal number of maxima of iid points in hypercubes (public paper 2005; an author manuscript is dated 2004). Hwang and Tsai examine multiple multivariate-record counts and their marginal means/variances. These works establish the natural model and extensive existing marginal theory, not the marked skyline–comparability overlap formulas here. The global planar record–inversion relation itself follows from classical inversion codes and is included as a consistency identity, not claimed as a new joint-distribution framework. Jin's later generating-function work concerns Euler–Stirling permutation statistics and reinforces the need to distinguish aggregate record/inversion information from marked-comparability overlap. McDiarmid, Penman and Iliopoulos concern comparable pairs and linear extensions for random interval partial orders, a different sampling model.

## Limitations

The sign-switch location \(16\) is for the planar iid uniform product model. The general-dimensional assertion covers only disjoint-label covariance, not a higher-dimensional cutoff or the sign of total covariance. The global planar formula and several marginal ingredients are elementary consequences of known permutation and record methods; no priority claim is made for those ingredients. Literature overlap was examined against available sources, but an unlocated earlier marked-pair calculation remains a historical-priority risk. No independent audit has been performed.

## References

- Z.-D. Bai, L. Devroye, H.-K. Hwang, T.-H. Tsai, *Maxima in hypercubes*, Random Structures & Algorithms 27 (2005), 290–309, https://doi.org/10.1002/rsa.20053 ; author manuscript https://staff.stat.sinica.edu.tw/chonghi/Papers/Maxima_in_hypercubes.pdf .
- H.-K. Hwang and T.-H. Tsai, *Multivariate records based on dominance*, Electronic Journal of Probability 15 (2010), 1863–1892, https://doi.org/10.1214/EJP.v15-825 .
- E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789 (2022), https://arxiv.org/abs/2210.08789 .
- C. McDiarmid, D. Penman, V. Iliopoulos, *Linear Extensions and Comparable Pairs in Partial Orders*, arXiv:1603.02901 (2016), https://arxiv.org/abs/1603.02901 .
