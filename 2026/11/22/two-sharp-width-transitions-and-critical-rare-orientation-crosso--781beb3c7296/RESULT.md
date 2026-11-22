# Two sharp width transitions and critical rare-orientation crossovers for right square pyramids

## Finding

Let \(P_h=\operatorname{conv}(\{(\pm1,\pm1,0)\}\cup\{(0,0,h)\})\subset\mathbb R^3\), with \(h>0\), and let \(W_h\) be its Euclidean caliper width in a Haar-uniform unoriented line direction. For \(t\in[0,1]\) and \(\phi\in[0,\pi/2]\) put \(c(\phi)=\cos\phi+\sin\phi\). Then \(t\) and \(\phi\) are independent and uniform in the indicated intervals, and
\[
W_h(t,\phi)=\max\{2c(\phi)\sqrt{1-t^2},\;c(\phi)\sqrt{1-t^2}+ht\}.
\tag{1}
\]
Its complete distribution is the one-dimensional quadrature
\[
\Pr(W_h\le w)=\int_0^1 G\!\left(\min\!\left\{\frac{w}{2\sqrt{1-t^2}},\frac{w-ht}{\sqrt{1-t^2}}\right\}\right)dt,
\tag{2}
\]
where \(G(q)=0\) for \(q\le1\), \(G(q)=\frac4\pi(\arcsin(q/\sqrt2)-\pi/4)\) for \(1<q<\sqrt2\), and \(G(q)=1\) for \(q\ge\sqrt2\); at \(t=1\) interpret the integrand by its limiting value. Its exact support endpoints are
\[
m(h)=\min\left\{h,\frac{2h}{\sqrt{1+h^2}}\right\},\qquad
M(h)=\max\{2\sqrt2,\sqrt{h^2+2}\}.
\tag{3}
\]
The least-width direction changes at \(h=\sqrt3\), while the greatest-width direction changes at \(h=\sqrt6\). At strict heights, as \(\varepsilon\downarrow0\),
\[
\Pr\{W_h\le m(h)+\varepsilon\}=C_-(h)\varepsilon^2+o(\varepsilon^2),\qquad
C_-(h)=\begin{cases}\pi^{-1},&0<h<\sqrt3,\\(1+h^2)^{5/2}/[2\pi h^2(h^2-1)],&h>\sqrt3;\end{cases}
\tag{4}
\]
and, for all sufficiently small \(\varepsilon>0\), the upper law is **exact**:
\[
\Pr\{W_h\ge M(h)-\varepsilon\}=C_+(h)\varepsilon,\qquad
C_+(h)=\begin{cases}1/\sqrt2,&h<\sqrt6,\\4/\sqrt{h^2+2},&h>\sqrt6.\end{cases}
\tag{5}
\]
At the critical heights, \(C_-(\sqrt3)=11/(3\pi)\) and \(C_+(\sqrt6)=3/\sqrt2\). The conditional proportions of the two minimizing contact families at \(h=\sqrt3\) are \(3/11\) axial and \(8/11\) oblique, and those of the two maximizing contact families at \(h=\sqrt6\) are \(1/3\) equatorial and \(2/3\) oblique.

Both transitions have exact moving-height boundary layers: for every fixed real \(\lambda\), using \([x]_+=\max(x,0)\),
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr\bigl\{W_{\sqrt3+\lambda\varepsilon}\le m(\sqrt3+\lambda\varepsilon)+\varepsilon\bigr\}
=\frac{[1-3\lambda_+/4]_+^2}{\pi}+\frac{8[1-3(-\lambda)_+/4]_+^2}{3\pi},
\tag{6}
\]
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr\bigl\{W_{\sqrt6+\lambda\varepsilon}\ge M(\sqrt6+\lambda\varepsilon)-\varepsilon\bigr\}
=\frac{[1-(\sqrt3/2)\lambda_+]_+}{\sqrt2}
+\sqrt2[1-(\sqrt3/2)(-\lambda)_+]_+.
\tag{7}
\]
The known general minimum-width formula for convex pyramids already implies the endpoint \(m(h)\) in (3). The new claims here are the complete random directional law (2), the **two-sided sharp probability laws and mode splits**, and the critical moving-height crossovers (6)–(7), not a new general minimum-width principle.

## Assumptions and scope

This is a solid right square pyramid with base side length \(2\), no restriction on \(h>0\), and projection onto unoriented lines, not orthogonal plane-shadow areas or section distributions. Haar measure means uniform surface-area measure on \(S^2\), with \(u\) and \(-u\) identified. The conditional contact modes are disjoint neighborhoods of the finitely many extremal unoriented directions; their limits refer to those neighborhoods as the width tolerance tends to zero. Equations (4)–(5) are for fixed heights; equations (6)–(7) specify fixed-parameter joint scalings.

## Proof

**Support and probability coordinates.** For \(u=(u_x,u_y,u_z)\), set \(a=|u_x|+|u_y|\) and \(t=|u_z|\). The four base vertices have projections between \(-a\) and \(+a\), while the apex projects to \(hu_z\). Thus, without loss of orientation, \(W_h(u)=a+\max(a,ht)\). Write \(a=c(\phi)\sqrt{1-t^2}\), where \(\phi\in[0,\pi/2]\) is the folded azimuth. In spherical area measure \(t\) and \(\phi\) are independent uniforms, the latter with density \(2/\pi\). Both inequalities \(2cs\le w\) and \(cs+ht\le w\) must hold, with \(s=\sqrt{1-t^2}\). The exact CDF of \(c=\cos\phi+\sin\phi\) is \(G\), since \(c=\sqrt2\cos(\phi-\pi/4)\). This proves (1)–(2), including normalization and boundary conventions.

**Global extrema and direction sets.** For each fixed \(t\), expression (1) increases strictly with \(c\), whose range is \([1,\sqrt2]\). Therefore global minima occur at \(c=1\) and maxima at \(c=\sqrt2\). At \(c=1\), the first branch \(2\sqrt{1-t^2}\) decreases with \(t\), while \(\sqrt{1-t^2}+ht\) is concave on \([0,1]\). Their maximum attains its minimum either at \(t=1\), giving \(h\), or at their unique intersection \(t_0=(1+h^2)^{-1/2}\), giving \(2h/\sqrt{1+h^2}\). The minimum changes branch exactly when \(h^2=3\). At \(c=\sqrt2\), each branch is bounded above by its own global maximum: \(2\sqrt2\) for the equatorial branch and \(\sqrt{h^2+2}\) for the oblique linear-functional branch. Both bounds are attained: at \(t=0\), and at \(t=h/\sqrt{h^2+2}\), respectively, in the regimes where that branch dominates. The maximum changes exactly when \(h^2=6\). Equality directions are the two axial poles or eight oblique signed axis–height directions for the minimum, and four equatorial diagonal directions or eight oblique signed diagonal–height directions for the maximum; at the respective transition both separated families occur. These counts are on \(S^2\), so antipodal identification halves both numerator and denominator in the probability calculation.

**Least-width endpoint.** If \(h<\sqrt3\), only the two axial poles minimize. In local tangent coordinates \(x=u_x\), \(y=u_y\), the leading width excess is \(|x|+|y|\), whose planar sublevel set has area \(2\varepsilon^2\). Dividing twice this by \(4\pi\) gives \(\varepsilon^2/\pi\).

If \(h>\sqrt3\), the eight oblique minima are nonsmooth intersections of two support branches. Work in folded coordinates \(\phi\ge0\) near an angular endpoint and \(t=t_0+\varepsilon\delta\). With \(s_0=h/\sqrt{1+h^2}\) and \(\phi=\varepsilon v\) (\(v\ge0\)), uniform Taylor expansions give
\[
\frac{W_h-m(h)}{\varepsilon}\longrightarrow
\max\left\{2s_0v-\frac2h\delta,\;s_0v+\left(h-\frac1h\right)\delta\right\}.
\tag{8}
\]
The unit sublevel of this maximum is an elementary triangle in \((v,\delta)\) with area
\[
A_h=\frac{(1+h^2)^{5/2}}{8h^2(h^2-1)}.
\]
The folded density \(2/\pi\) and two angular endpoints yield \(4A_h\varepsilon^2/\pi\), proving (4). Uniform localization follows from compactness and the strict gap away from the finitely many minimizing directions. At equality \(h=\sqrt3\), the pole and ridge neighborhoods are separated, and their coefficients sum to \(1/\pi+8/(3\pi)=11/(3\pi)\). Normalizing the contributions proves the claimed contact-mode proportions.

**Greatest-width endpoint.** For \(h<\sqrt6\), the maxima come from the four equatorial diagonals; within a sufficiently small neighborhood the active branch equals the dot product of a fixed base-vertex difference vector of length \(2\sqrt2\). For \(h>\sqrt6\), the maxima come from eight oblique diagonal–apex signed directions; each is locally the dot product of a fixed apex–base-vertex difference vector of length \(\sqrt{h^2+2}\). The probability of a uniform spherical direction lying in a cap \(u\cdot v\ge\|v\|-\varepsilon\), with \(\|v\|=M\), is exactly \(\varepsilon/(2M)\) for \(0<\varepsilon<2M\). The indicated caps are disjoint and do not meet any competing larger support branch when \(\varepsilon\) is sufficiently small. Multiplying by the four or eight maximizing directed vectors yields (5). At \(h=\sqrt6\), the two disjoint classes contribute \(1/\sqrt2\) and \(\sqrt2\), proving the total and the split.

**Moving-height boundary layers.** The separated pole/ridge minimizing families have competing values \(h\) and \(r(h)=2h/\sqrt{1+h^2}\), with \(h-r(h)=(3/4)(h-\sqrt3)+O((h-\sqrt3)^2)\). A family whose local minimum exceeds the global one by \(d\varepsilon+o(\varepsilon)\) contributes the same quadratic sublevel area with available tolerance \([1-d]_+\varepsilon\). Its local coefficient changes by \(o(1)\) as the height changes by \(O(\varepsilon)\). At \(h=\sqrt3\) the coefficients are \(1/\pi\) and \(8/(3\pi)\); inserting the positive gaps on the appropriate sides proves (6), uniformly for each fixed \(\lambda\).

Likewise the competing greatest-width values are \(2\sqrt2\) and \(\sqrt{h^2+2}\), whose difference to first order is \((\sqrt3/2)(h-\sqrt6)\). A family below the global maximum by \(d\varepsilon\) supplies an exact cap law with tolerance \([1-d]_+\varepsilon\), and the coefficients at equality are \(1/\sqrt2\) and \(\sqrt2\). This proves (7). At fixed \(\lambda\), all other directions remain uniformly suboptimal and cannot affect either limit.

## Verification

Run `python3 verify.py` with the standard Python library. The supplied checker compares the two-branch support identity against direct extrema over all five vertices for 20,000 deterministic sample directions, checks extremal witnesses through all phases, verifies the local triangular-area coefficient, compares the exact angular-CDF kernel with finite angular counting, and checks the two critical mixture identities. It prints `PASS: 20032 supplemental deterministic assertions` on success. Independently, adaptive numerical integration of equation (2) at heights below, at and above \(\sqrt3\) showed the lower-tail ratios approaching the analytic coefficients. These finite computations support the formulas but are not substitutes for the global proof or historical-priority verification.

## Relationship to prior work

Finch (2011) studies random directional widths and their moments for the regular tetrahedron and cube, establishing the classical distributional context, but not the varying-height square pyramid. Kim, Yaskin and Zvavitch (2015) study distribution functions of central-section and hyperplane-projection **areas**, rather than this one-dimensional caliper observable.

The published result *Exact minimum-width formula for convex pyramids and a partial-plank consequence* proves a general support-function minimum-width formula for all convex pyramids. It already implies equation (3)'s minimum value in the square-base specialization; the minimum *value alone* is not claimed as an original result. It does not classify the complete random width law or the critical endpoint probability crossovers in (2), (4)–(7).

The published *A three-threshold random-width law for every proper right circular frustum* provides a complete law for **circular** end disks; the square-base geometry has an independent azimuth and two distinct, noncircular endpoint transition laws. A published exact random-width law for the cube likewise concerns a different five-versus-eight-vertex body. Exact projected planar-shadow area and silhouette probabilities for right square pyramids do not imply their line-width distribution: they are different observables under the same directional measure. These differences were checked at the level of hypotheses, random observables and implication, not title matching alone.

## Limitations

Historical originality is provisional, not independently certified. Although directly relevant prior full text and indexed statements were compared, an older unindexed computation could cover some formulas. The claim is restricted to the centered right square pyramid, Haar-uniform **line** directions, fixed-height endpoint asymptotics and fixed-parameter critical double scalings; it does not assert uniformity for diverging moving-height parameters or an elementary closed form for the entire CDF beyond the exact one-dimensional integral. The arbitrary-base general minimum-width theorem is prior art.

## References

1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, publicly posted 4 October 2011. https://arxiv.org/abs/1110.0671
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, publicly posted 22 December 2015. https://arxiv.org/abs/1512.07289
3. *Exact minimum-width formula for convex pyramids and a partial-plank consequence*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-minimum-width-formula-for-convex-pyramids-and-a-partial-pl--5011fb3c7815
4. *A three-threshold random-width law for every proper right circular frustum*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-three-threshold-random-width-law-for-every-proper-right-circul--d2f25b7ec7c9
5. *Exact directional width law of the cube and its first spherical-cap transition*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2
