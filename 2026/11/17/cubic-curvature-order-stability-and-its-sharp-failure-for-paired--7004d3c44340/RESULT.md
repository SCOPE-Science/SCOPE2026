# Cubic curvature-order stability and its sharp failure for paired-arc reduced bodies

## Finding
Fix any \(m\in(\pi/4,\pi/2)\) and consider the thickness-one planar reduced bodies with paired active arcs and two joining edges described below. In the complete measurable curvature-profile class the unique area maximizer is the previously determined profile \(r_*(m+x)=\tfrac12\mathbf1_{\{|x|>a\}}\), where
\[
 a=\arcsin(2\sin m-\csc m)\in(0,m).
\]
The new result identifies a **sharp stability-topology dichotomy**. If the ordered curvature-radius split is nonnegative, \(0\le r(t)\le\tfrac12\) almost everywhere, put
\[
 N(r)=\int_0^{2m}|r(t)-r_*(t)|\,dt,
 \qquad \mathcal D_m(r)=\operatorname{area}K(m,r_*)-\operatorname{area}K(m,r).
\]
Every admissible nonnegative profile obeys the universal quantitative inequality
\[
 \boxed{\mathcal D_m(r)\ge\frac{N(r)^3}{12\pi^2}.}
\]
The exponent three is best possible for **every fixed** \(m\in(\pi/4,\pi/2)\). There are explicitly constructed feasible nonnegative profiles \(r_\delta\) satisfying
\[
 N(r_\delta)=2\delta+O_m(\delta^2),\qquad
 \mathcal D_m(r_\delta)=\frac{\delta^3}{2}+O_m(\delta^4),\qquad
 \lim_{\delta\downarrow0}\frac{\mathcal D_m(r_\delta)}{N(r_\delta)^3}=\frac1{16}.
\]
The coefficient \(1/(12\pi^2)\) is explicit and universal, **not asserted optimal**.

If instead the full geometrically admissible signed class \(-\tfrac12\le r\le\tfrac12\) is allowed, no positive \(L^1\)-distance stability modulus exists, even at a fixed interior \(m\): there are feasible \(r_j\) and a constant \(c_m>0\) such that \(N(r_j)\to c_m\), yet \(\mathcal D_m(r_j)\to0\). Each corresponding planar body remains convex, reduced, and of thickness one. Thus nonnegativity of the split, meaning an ordering of the two opposite curvature radii, changes the stability topology despite uniqueness of the area maximizer in both classes.

## Assumptions and scope
Let \(u_t=(\cos t,\sin t)\), \(v_t=(-\sin t,\cos t)\), and \(k=\tfrac12\cot^2m\). A bounded measurable \(r:[0,2m]\to[-1/2,1/2]\) is **admissible** if it obeys the vector closing condition
\[
 \int_0^{2m}(r(t)-k)v_t\,dt=0.
\]
Put \(c(t)=\int_0^t r(s)v_s\,ds\), \(a_r(t)=c(t)+\tfrac12u_t\), and \(b_r(t)=c(t)-\tfrac12u_t\). Define \(K(m,r)\) by traversing \(a_r(t)\) and \(b_r(t)\), in increasing parameter order, with joining line segments \([a_r(2m),b_r(0)]\) and \([b_r(2m),a_r(0)]\). The closing condition ensures a convex, thickness-one reduced body: the opposite active curvature radii are \(\tfrac12+r\) and \(\tfrac12-r\), and each joining segment has length \(\cot m>0\). The closure conditions in centered angular coordinates \(x=t-m\) are
\[
 \int_{-m}^m r(m+x)\cos x\,dx=\frac{\cos^2m}{\sin m},
 \quad \int_{-m}^m r(m+x)\sin x\,dx=0.
\]
All claims are within this fixed-angle paired-arc family, not the class of all reduced bodies, and apply to measurable, possibly discontinuous curvature densities.

## Proof
**1. Exact area variation and dual certificate.** The known Green-theorem area identity (reproducible directly from the parametrized boundary) is
\[
 \operatorname{area}K(m,r)=\frac m2+\frac{\sin2m}{4}+Q_m(r),\quad
 Q_m(f)=\frac12\int_0^{2m}\!\int_0^{2m} f(t)f(s)\sin|t-s|\,ds\,dt.
\]
The global optimizer \(r_*\) and its first-variation identity, established in the cited full-class maximum theorem, have the following directly checkable form. Define
\[
 H(x)=\int_{-m}^m r_*(m+y)\sin|x-y|\,dy,
 \quad\lambda=\cos a-\cos m.
\]
Integrating over the two exterior constant-density arcs gives
\[
 H(x)-\lambda\cos x= D(x):=
 \begin{cases}0,&|x|\le a,\\
 1-\cos(|x|-a),&a<|x|\le m.
 \end{cases}
\]
For \(f=r-r_*\), the two closing moments are zero. Let \(p(t)=\int_0^t f(s)\sin(t-s)\,ds\). Then \(p''+p=f\) almost everywhere and \(p(0)=p'(0)=p(2m)=p'(2m)=0\). Integration by parts gives
\[
 Q_m(f)=\int_0^{2m}(p^2-p'^2)\,dt\le0,
\]
by Dirichlet Poincaré because \(2m<\pi\). Consequently the exact quadratic area expansion gives
\[
 \mathcal D_m(r)=-\int_{-m}^m D(x)f(m+x)\,dx-Q_m(f)
 \ge\int_{|x|>a}\!\bigl(r_*(m+x)-r(m+x)\bigr)
 [1-\cos(|x|-a)]\,dx.
\]
This uses no finite-dimensional restriction on \(r\).

**2. Positive curvature order produces a cubic \(L^1\) bound.** Assume \(0\le r\le1/2\). Set
\[
 O=\int_{|x|>a}(r_*-r)\,dx,\qquad
 I=\int_{|x|<a}r\,dx.
\]
These are nonnegative and \(N=O+I\). The zero cosine moment gives
\[
 \int_{|x|>a}(r_*-r)\cos x\,dx
 =\int_{|x|<a}r\cos x\,dx.
\]
Since \(\cos x\le\cos a\) on the outer set and \(\cos x\ge\cos a>0\) on the inner set, \(I\le O\), hence \(N\le2O\). Introduce \(y=|x|-a\in[0,m-a]\) and aggregate the outer loss from both sides; the resulting density \(w(y)\) satisfies \(0\le w\le1\) and \(\int w=O\). The elementary bathtub inequality, proved by moving density towards \(y=0\), is
\[
 \int_0^{m-a} y^2w(y)\,dy\ge\int_0^O y^2dy=\frac{O^3}3.
\]
Because \(m-a<\pi/2\), \(1-\cos y\ge2y^2/\pi^2\), whence
\[
 \mathcal D_m(r)\ge\frac{2O^3}{3\pi^2}\ge\frac{N^3}{12\pi^2}.
\]
The bound remains valid at arbitrary finite \(L^1\)-distance; no local-smallness assumption was made.

**3. Exact feasible bands prove optimality of the exponent.** For \(0<\delta<\min\{m-a,a/2\}\), choose \(\eta=\eta_\delta\in(0,a)\) by
\[
 \sin a-\sin(a-\eta)=\sin(a+\delta)-\sin a.
\]
Set \(r_\delta(m+x)=1/2\) on the intervals \(a-\eta<|x|<a\) and \(|x|>a+\delta\), and zero elsewhere. The profile is symmetric, and the displayed sine identity makes both closure moments exact. It lies in \([0,1/2]\). The inverse-function theorem gives \(\eta=\delta+O_m(\delta^2)\) and \(N=\eta+\delta\). Its linear deficit equals \(\delta-\sin\delta\).

The quadratic form of the profile difference is supported on two mirror image pairs of adjacent bands. Each pair has zero cosine moment individually, so its cross interaction with the opposite pair vanishes by \(\sin(t-s)=\sin t\cos s-\cos t\sin s\) for ordered bands. Direct integration on one pair gives
\[
 Q_{\mathrm{one}}=\frac14[\eta+\delta-2\sin\eta-2\sin\delta+\sin(\eta+\delta)].
\]
Thus
\[
 \mathcal D_m(r_\delta)=\delta-\sin\delta-2Q_{\mathrm{one}}
 =\frac{\delta^3}{2}+O_m(\delta^4).
\]
It follows that the limit of \(\mathcal D/N^3\) is \(1/16\). Hence no positive bound of the form \(\mathcal D\ge C_mN^q\) with \(q<3\) can hold, even arbitrarily close to the maximizer.

**4. High-frequency signed profiles defeat \(L^1\)-stability.** Fix an even, nonnegative, nonzero smooth cutoff \(\chi\) supported in \((-a/2,a/2)\), and an even, nonnegative smooth cutoff \(\psi\) supported there with \(\int\psi(x)\cos x\,dx>0\). Define
\[
 c_j=\frac{\int\chi(x)\cos(jx)\cos x\,dx}
 {\int\psi(x)\cos x\,dx},\quad
 f_j(m+x)=\varepsilon[\chi(x)\cos(jx)-c_j\psi(x)],
\]
vanishing outside the central interval. For sufficiently small fixed \(\varepsilon>0\) and all sufficiently large integers \(j\), the signed profiles \(r_j=r_*+f_j\) satisfy \(|r_j|\le1/2\). They have exact zero cosine moment by construction, and zero sine moment by evenness. Riemann–Lebesgue gives \(c_j\to0\) and
\[
 \|f_j\|_{L^1}\longrightarrow \frac{2\varepsilon}{\pi}\int\chi(x)\,dx=:c_m>0.
\]
Their first area variation is identically zero because \(D\equiv0\) on the central support, while the cosine moment vanishes. The smooth integral kernel \(\sin|x-y|\) defines a compact operator on these bounded oscillatory profiles: directly, \(p_j(t)=\int_0^t f_j(s)\sin(t-s)\,ds\to0\) uniformly by integration by parts and \(c_j\to0\). Therefore \(Q_m(f_j)\to0\), and \(\mathcal D_m(r_j)=-Q_m(f_j)\to0\). This proves the claimed failure of positive \(L^1\)-distance stability on the full signed admissible class.

## Verification
Run the standalone `verify.py` using Python 3 and only the standard library. It checks the exact positive moment identity, the cubic inequality, and the band-deficit formula for 1,000 admissible parameter pairs, including the expansion ratio approaching \(1/16\); it reports `VERIFY_OK` and 3,000 passed finite checks. It independently evaluates elementary trigonometric expressions instead of importing any earlier computational artifact. The infinite-profile theorem and the absence of signed \(L^1\)-stability are analytical arguments, not consequences of these finite checks.

## Relationship to prior work
Kominers (arXiv:2606.28612v1, June 26, 2026) introduced the explicit two-arc reduced-body geometry and obtained a counterexample to a conjectured area bound. *Sharp nonparametric area maximum in the paired-arc reduced-body construction* (2026) determines the exact area maximizer over **all** bounded measurable signed curvature profiles and supplies the integral area identity and dual potential. It explicitly does not address shape stability. That maximization, its optimizer, and its area \(0.7945785086\ldots\) are **prior results and are not claimed as new** here.

The new statements are the universal cubic \(L^1\) stability under curvature-radius ordering, the best-possible exponent with a moment-preserving family, and failure of every positive \(L^1\) modulus in the un-ordered (signed) class. The sign condition has geometric meaning: it keeps the same member of each pair of opposite active arcs as the one with greater radius of curvature. No equivalent stability dichotomy was found by searching the relevant published records and general literature. Abstract bathtub-rearrangement and compact-kernel arguments are standard, but their exact application and sharp exponent for this geometric family are not implied by the known uniqueness assertion.

## Limitations
The explicit numerical coefficient \(1/(12\pi^2)\) is not claimed optimal. The exponent three is sharp for each interior fixed angle. The positive stability bound does not extend to all signed profiles; in that larger class uniqueness is compatible with failure of uniform \(L^1\)-stability. No stability across varying angle \(m\) or global classification of all thickness-one reduced convex bodies is asserted. The constructed oscillatory profiles are measurable and their boundaries may have limited smoothness. Historical novelty is assessed against accessible records and could change if unindexed equivalent stability results exist.

## References
1. Scott Duke Kominers, *A reduced planar body with area greater than \(\pi\Delta^2/4\)*, arXiv:2606.28612v1, first public June 26, 2026. https://arxiv.org/html/2606.28612v1.
2. *Sharp nonparametric area maximum in the paired-arc reduced-body construction* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-nonparametric-area-maximum-in-the-paired-arc-reduced-body--df7f77ac86a5.
3. M. Lassak and H. Martini, *Reduced convex bodies in Euclidean space—a survey*, Expositiones Mathematicae 29 (2011), 204–219 (background context).
