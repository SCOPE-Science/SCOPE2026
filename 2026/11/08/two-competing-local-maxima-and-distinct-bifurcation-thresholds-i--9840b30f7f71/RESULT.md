# Two competing local maxima and distinct bifurcation thresholds in the four-sign quadratic Walsh space

## Finding
Let \(\varepsilon_1,\ldots,\varepsilon_4\) be independent symmetric random signs, and for a real six-tuple \(a=(a_{ij})_{1\le i<j\le4}\) put
\[
F_a=\sum_{1\le i<j\le4}a_{ij}\varepsilon_i\varepsilon_j,\qquad
\mathcal M_p(a)=\frac{\mathbb E|F_a|^p}{(\mathbb E F_a^2)^{p/2}},\quad 2<p<3.
\]
Write \(p_{\mathrm{loc}}\) for the unique root in \((2,3)\) of
\[
3^{p-1}=4p-5,
\]
and \(p_{\mathrm{cross}}\) for the unique root in \((2,3)\) of
\[
3^p+3=2\cdot6^{p/2}.
\]
These roots are distinct and satisfy
\[
2<p_{\mathrm{loc}}=2.3418224547\ldots<\tfrac52<
p_{\mathrm{cross}}=2.7362773220\ldots<3.
\]
There are two explicitly specified, non-equivalent families of unit-variance coefficient vectors: **square configurations** have exactly four nonzero edge coefficients, all of magnitude \(1/2\), supported on a four-cycle with positive product of their signs; **complete configurations** have all six coefficients equal to \(\sigma_i\sigma_j/\sqrt6\) for vertex signs \(\sigma_i\in\{\pm1\}\), with an optional common global sign. Their moments are
\[
\mathcal M_p(\mathrm{square})=2^{p-2},\qquad
\mathcal M_p(\mathrm{complete})=
\frac{3^p+3}{8}\left(\frac23\right)^{p/2}.
\]
Every square configuration is a strict local maximizer of \(\mathcal M_p\) on the unit-variance coefficient sphere for \(2<p<3\). Every complete configuration is a strict local maximizer for \(p_{\mathrm{loc}}<p<3\), and a saddle point for \(2<p<p_{\mathrm{loc}}\). In particular, **two inequivalent strict-local-maximum orbits coexist throughout \((p_{\mathrm{loc}},3)\)**. The square moment is greater when \(2<p<p_{\mathrm{cross}}\), while the complete moment is greater when \(p_{\mathrm{cross}}<p<3\); at \(p_{\mathrm{cross}}\) their values agree although the maximizers have distinct supports. The word “local” is essential: no assertion of global sharp \(L^2\)-to-\(L^p\) constants or completeness of all stationary points is made.

## Assumptions and scope
Coefficients are real and the sign cube carries normalized counting probability. A strict local maximum is relative to the five-sphere \(\sum_{i<j}a_{ij}^2=1\), with the Euclidean topology. The symmetry orbits permit permutation of base signs and independent sign changes. The two root equations and the conclusions apply only to \(2<p<3\). The result compares two specifically constructed local branches, not every critical point of the global optimization.

## Proof
**1. Exact parity-block reduction.** Set \(x=\varepsilon_1\varepsilon_2\), \(y=\varepsilon_1\varepsilon_3\), and \(z=\varepsilon_1\varepsilon_4\). These are three independent symmetric signs and
\[
F_a=a_{12}x+a_{13}y+a_{14}z+a_{23}xy+a_{24}xz+a_{34}yz.
\]
On the four points with \(xyz=+1\), we have \(xy=z\), \(xz=y\), and \(yz=x\); on \(xyz=-1\), these identities acquire minus signs. The orthogonal change of coordinates
\[
u_\pm=\frac{a_{12}\pm a_{34}}{\sqrt2},\quad
v_\pm=\frac{a_{13}\pm a_{24}}{\sqrt2},\quad
w_\pm=\frac{a_{14}\pm a_{23}}{\sqrt2}
\]
satisfies \(\sum a_{ij}^2=\|U_+\|_2^2+\|U_-\|_2^2\). Restricted to the respective parity class, \(F_a\) equals \(\sqrt2(u_\pm x+v_\pm y+w_\pm z)\). Consequently,
\[
\mathbb E|F_a|^p=2^{p/2-1}\left[H_p(U_+)+H_p(U_-)\right],\quad
H_p(u,v,w)=\frac14\bigl(|u+v+w|^p+|u+v-w|^p+|u-v+w|^p+|-u+v+w|^p\bigr).
\tag{1}
\]
Absolute values account for the four global-sign pairs of the three-sign cube. A unit vector concentrated in one parity block corresponds to six coefficients satisfying the three pair equalities with common \(+\) or \(-\) sign. The two specified configurations are among these: square corresponds to \(U_+=(1,1,0)/\sqrt2\), and complete corresponds to \(U_+=(1,1,1)/\sqrt3\), up to the evident finite symmetries.

**2. Square: strict negative Hessian.** On the unit sphere in the plus block introduce local coordinates
\[
U(t,s)=\frac{(1+t,1-t,s)}{\sqrt{2+2t^2+s^2}}.
\]
Then the exactly evaluated four-point moment is
\[
H_p(U(t,s))=\frac{|2+s|^p+|2-s|^p+|2t+s|^p+|2t-s|^p}{4(2+2t^2+s^2)^{p/2}}.
\]
Since \(p>2\), the last two numerator terms are \(o(t^2+s^2)\) near the origin and the first two are twice differentiable. Taylor expansion gives
\[
H_p(U(t,s))=2^{p/2-1}
\left[1-\frac p2t^2+\frac{p(p-3)}8s^2+o(t^2+s^2)\right].\tag{2}
\]
Both Hessian directions are strictly negative for \(2<p<3\); hence the square profile is a strict local maximum within its three-dimensional parity block.

**3. Complete: the local bifurcation.** Near \(U_0=(1,1,1)/\sqrt3\), use the tangent-direction curve
\[
U(t)=\frac{(1+t,1-t,1)}{\sqrt{3+2t^2}}.
\]
For sufficiently small \(t\), (1) gives
\[
H_p(U(t))=\frac{3^p+1+|1+2t|^p+|1-2t|^p}{4(3+2t^2)^{p/2}}
=\frac{3^p+3}{4\,3^{p/2}}
\left[1+\frac{p(4p-5-3^{p-1})}{3^p+3}t^2+O(t^4)\right].\tag{3}
\]
The Hessian of \(H_p\) on the tangent plane \(u+v+w=0\) is a scalar multiple of the identity: the full \(S_3\) permutation symmetry fixes \(U_0\), and an invariant symmetric quadratic form on this two-dimensional irreducible permutation representation must be scalar. Thus (3) determines its sign in *every* tangent direction. Put \(g(p)=3^{p-1}-(4p-5)\). We have \(g(2)=0\), \(g'(2)=3\log3-4<0\), \(g''(p)>0\), and \(g(3)=2>0\). Strict convexity gives exactly one additional root in \((2,3)\), called \(p_{\mathrm{loc}}\). For \(p>p_{\mathrm{loc}}\) the tangent Hessian is negative definite and for \(2<p<p_{\mathrm{loc}}\) it is positive definite.

**4. The inactive parity block makes the maxima strict in all six coordinates.** Let \(U\) be a unit-vector strict local maximum of \(H_p\) in one parity block, and consider nearby unit six-vectors \((\sqrt{1-r^2}\,V,rW)\), where \(r\ge0\), \(\|V\|_2=\|W\|_2=1\). By (1), the value becomes
\[
2^{p/2-1}\left[(1-r^2)^{p/2}H_p(V)+r^pH_p(W)\right].
\]
The sphere is compact, so \(H_p(W)\) is uniformly bounded. Because \(p>2\), the negative \(-\tfrac p2r^2H_p(U)\) term strictly dominates the positive \(O(r^p)\) term when \(r\ne0\) is small. For \(r=0\), strictness follows from the three-coordinate Hessian. Hence both negative-definite profiles are strict local maxima on the complete six-dimensional coefficient sphere. When \(2<p<p_{\mathrm{loc}}\), the complete profile has a positive tangent curvature from (3), while the inactive-block perturbation has negative curvature, so it is a saddle point.

**5. Distinct crossing and its uniqueness.** Formula (1) at the square yields \(H_p=2^{p/2-1}\), and at the complete profile gives \(H_p=(3^p+3)/(4\,3^{p/2})\). Multiplication by \(2^{p/2-1}\) gives the two moments asserted. Their equality is equivalent to \(3^p+3=2\cdot6^{p/2}\). Set \(t=p/2-1\), so the equality is
\[
h(t)=3(3/2)^t+6^{-t}-4=0.
\]
Here \(h(0)=0\), \(h'(0)=3\log(3/2)-\log6<0\), \(h''(t)>0\), and \(h(t)\to+\infty\). It has exactly one root \(t>0\). The root belongs to \((1/4,1/2)\): at \(t=1/4\), the rational comparisons \((3/2)^{1/4}<111/100\) and \(6^{-1/4}<2/3\) imply \(h(1/4)<3(111/100)+2/3-4<0\), while \(h(1/2)=3\sqrt{3/2}+1/\sqrt6-4>0\). Thus \(5/2<p_{\mathrm{cross}}<3\), and the sign of \(h\) determines the stated strict moment comparisons. Finally \(g(5/2)=3\sqrt3-5>0\), so \(p_{\mathrm{loc}}<5/2<p_{\mathrm{cross}}\), proving the coexistence and distinct thresholds.

## Verification
The companion `verify.py` uses the Python standard library. It enumerates all sixteen base-sign inputs for the two explicit coefficient arrays, checks their exact second/fourth/sixth moments and the eight-point parity-block identity at several rational arrays, and computes numerical approximations to each analytically unique root and the local-Hessian signs. The script's finite evaluations are corroboration only; equations (1)–(3) and the convexity/root arguments prove the conclusions for all real \(2<p<3\).

## Relationship to prior work
Mordhorst's 2016 preprint addresses the **dimension-free** optimal Khintchine constants for \(2<p<3\) via distribution functions; the explicit finite three-sign stationary Hessian and its two competing local branches do not follow from the dimension-free numerical bounds. Komorowski's 1988 result gives sharp fixed-coefficient-count constants for \(p\ge3\), outside the open interval here. Related published finite quadratic Walsh results determine sharp **fourth moments** for five or more base signs, or certain graph-supported spaces, not the real-exponent local bifurcations for the four-sign complete quadratic space. No claim of global optimization in the interval \((2,3)\) is made; the two explicit local branches could coexist with additional, higher local or global maxima.

## Limitations
No global sharp norm or exhaustive classification of stationary vectors is asserted. The degenerate endpoints \(p=2\), \(p=p_{\mathrm{loc}}\), and \(p=3\) are excluded from strictness conclusions; at \(p=p_{\mathrm{cross}}\) both local maxima remain strict and have equal value. This is for real quadratic Walsh coefficients on exactly four independent signs; complex coefficients and larger sign counts are not covered. Closely related finite-dimensional Khintchine local-extremum literature may exist under alternate terminology, and an independent mathematical audit has not been performed.

## References
1. O. Mordhorst, “The optimal constants in Khintchine's inequality for the case \(2<p<3\),” arXiv:1601.07850v1, first posted 2016-01-28, Sections 1–3; https://arxiv.org/abs/1601.07850.
2. R. Komorowski, “On the best possible constants in the Khintchine inequality for \(p\ge3\),” *Bulletin of the London Mathematical Society* 20 (1988), 73–75, DOI:10.1112/blms/20.1.73.
3. M. Kauers, R. O'Donnell, L.-Y. Tan and Y. Zhou, “Hypercontractive inequalities via SOS, and the Frankl–Rödl graph,” arXiv:1212.5324v1 (2012), https://arxiv.org/abs/1212.5324.
4. “Sharp fourth moments and Euclidean distance of the five-sign quadratic Walsh chaos,” published 2026-10-11, theorem for five signs.
5. “Sharp fourth moments and Euclidean distortion of complete quadratic Walsh chaoses,” published 2026-10-11, theorem for six or more signs.
