# Exact convex-position profile for two pairs of concentric-circle points

## Finding
Fix two concentric Euclidean circles of radii \(1\) and \(r\), with \(0<r<1\). Choose \(A,B\) independently with normalized arclength measure on the outer circle, and \(C,D\) independently with normalized arclength measure on the inner circle; all four choices are independent. Let \(Q(r)\) be the probability that all four are vertices of their Euclidean convex hull (equivalently, that the hull is a strict quadrilateral). Define \(a_r(x)=\arcsin(r\sin x)\) for \(0\le x\le\pi/2\). Then the **complete finite-radius probability profile** is
\[
\boxed{Q(r)=\frac12+\frac8{\pi^3}\int_0^{\pi/2}x a_r(x)\,dx
                  +\frac4{\pi^3}\int_0^{\pi/2}a_r(x)^2\,dx.}
\]
There is also an exact transfer identity to a different natural random-chord experiment. Let \(p(R)\) be the probability that a chord joining two independent uniform points of the unit circle meets a chord joining two independent uniform points of the concentric circle of radius \(R\ge1\). Then
\[
\boxed{Q(r)=\frac12+p(1/r)+\frac1{\pi^2}\operatorname{Li}_2(r^2).}
\]
Here \(\operatorname{Li}_2(z)=\sum_{n=1}^\infty z^n/n^2\) is the classical dilogarithm. The previously published exact \(p(R)\) and its sharp singular expansion are explicitly credited; the new contribution is the separate convex-hull event, its exact reduction and dilogarithmic correction, strict convexity, and complete two-radius profile.

It extends continuously to \(Q(0)=1/2\) and \(Q(1)=1\), is strictly increasing and strictly convex on \([0,1)\), and has the sharp two endpoint expansions
\[
Q(r)=\frac12+\frac8{\pi^3}r+\frac1{\pi^2}r^2
       +\frac{28}{27\pi^3}r^3+O(r^4) \quad(r\downarrow0),
\]
\[
1-Q(1-\delta)=\frac4{\pi^2}\delta\log(1/\delta)+O(\delta)
 \quad(\delta\downarrow0).
\]
The zero-radius limit alone was previously known for a more general two-radius mixture; the claim here is the exact full-radius profile, its strict convexity, and its sharp near-coincident-radius cusp.

## Assumptions and scope
All angles are independent and uniform on \([0,2\pi)\), with their respective point radii fixed rather than randomized. Both circles share their center. The geometric hull is ordinary Euclidean convex hull; the terms convex position and four vertices agree almost surely when \(0<r<1\), since any collinearity has probability zero. The limit \(r=0\) is a one-sided limit of positive-radius laws, not a model with two identical deterministic center points. The value \(r=1\) is the equal-circle endpoint. No statement is made for a nonconcentric pair or a different sampling law.

## Proof
**1. Reduction to the trapping probability.** Both outer samples \(A,B\) lie on the strictly convex outer circle and are extreme points almost surely. Therefore failure of four-point convex position means precisely that \(C\) is inside triangle \(ABD\), or \(D\) is inside triangle \(ABC\). These alternatives are mutually exclusive. By symmetry, if \(H(r)=\Pr(C\in\operatorname{int}\operatorname{conv}\{A,B,D\})\), then
\[Q(r)=1-2H(r).\]
By rotation set \(C=(r,0)\). Every ray from \(C\) meets the unit circle once. If \(\theta\) is the polar bearing of that ray and \(t\) the usual outer-circle polar angle at the origin, elementary right-triangle geometry gives the strictly increasing map
\[t=\theta-\arcsin(r\sin\theta),\qquad
 p_r(\theta)=\frac{1}{2\pi}\left(1-\frac{r\cos\theta}{\sqrt{1-r^2\sin^2\theta}}\right).\]
Thus the bearings of \(A,B\) from \(C\) are independent with density \(p_r\), while the bearing of \(D\) from \(C\) is uniform on the *inward semicircle* \((\pi/2,3\pi/2)\). The last statement follows from \(r(e^{i\phi}-1)=2ri e^{i\phi/2}\sin(\phi/2)\) for uniformly distributed \(0<\phi<2\pi\).

**2. Exact half-circle containment identity.** For three independent, nonatomic random angular directions \(\Theta_1,\Theta_2,\Theta_3\), their positive convex cone is all of \(\mathbb R^2\) precisely when they do not fit into any closed semicircle. In the complementary event, outside a null set there is a *unique* direction among the three such that the clockwise-forward semicircle starting at it contains the other two. This partitions the failure event into three disjoint anchor events, without requiring the angular densities to be identical.

Write
\[a(\theta)=\arcsin(r\sin\theta),\quad
F(\theta)=\int_{\theta}^{\theta+\pi}p_r(u)\,du=\frac12+\frac{a(\theta)}{\pi},\]
and let \(q(\theta)=\pi^{-1}\mathbf1_{(\pi/2,3\pi/2)}(\theta)\) (periodically extended) and \(T(\theta)=\int_{\theta}^{\theta+\pi}q(u)\,du\). By the unique-anchor partition,
\[
H(r)=1-2\int_0^{2\pi}p_r(\theta)F(\theta)T(\theta)\,d\theta
        -\int_0^{2\pi}q(\theta)F(\theta)^2\,d\theta.
\]
Here the first two terms count the two possible outer-ray anchors, and the last the inner-ray anchor.

**3. Evaluate the two integrals.** Put \(x=\theta-\pi\), so \(-\pi\le x<\pi\), and define \(a(x)=\arcsin(r\sin x)\). In these variables,
\[p_r(\pi+x)=\frac{1+a'(x)}{2\pi},\quad F(\pi+x)=\frac12-\frac{a(x)}\pi,\quad T(\pi+x)=\frac12+t(x),\]
where \(t\) is odd and for \(0\le x\le\pi\) equals
\[
t(x)=\begin{cases}-x/\pi,&0\le x\le\pi/2,\\x/\pi-1,&\pi/2\le x\le\pi.\end{cases}
\]
The integral of every odd term vanishes. Since \(a(x)=a(\pi-x)\) for \(0<x<\pi\), integration by parts gives
\[\int_{-\pi}^{\pi}a(x)a'(x)t(x)\,dx=0,\qquad
\int_{-\pi}^{\pi}a(x)t(x)\,dx=-\frac4\pi\int_0^{\pi/2}x a(x)\,dx.\]
Consequently,
\[
\int p_rFT=\frac14+\frac2{\pi^3}\int_0^{\pi/2}xa(x)\,dx,
\quad
\int qF^2=\frac14+\frac2{\pi^3}\int_0^{\pi/2}a(x)^2\,dx.
\]
Substituting into the anchor identity and then \(Q=1-2H\) proves the exact claimed formula. It also proves that there are no omitted geometric cases.

**3a. Exact connection to nested-circle chord crossings.** The independently published nested-circle chord-intersection formula for \(R\ge1\) is
\[p(R)=\frac1\pi\int_{-1}^{1}\frac{\frac12-\frac2{\pi^2}(\arcsin u)^2}{\sqrt{R^2-u^2}}\,du.\]
Put \(u=\sin t\), \(R=1/r\). Integration by parts, using the vanishing of the numerator at both endpoints and \(d\arcsin(r\sin t)=r\cos t\,dt/\sqrt{1-r^2\sin^2t}\), gives
\[p(1/r)=\frac8{\pi^3}\int_0^{\pi/2} t\arcsin(r\sin t)\,dt.\]
Further, the elementary power-series identity
\[\arcsin^2 z=\frac12\sum_{n=1}^{\infty}\frac{(2z)^{2n}}{n^2\binom{2n}{n}}\]
and \(\int_0^{\pi/2}\sin^{2n}t\,dt=\frac\pi2\binom{2n}{n}/4^n\) show, by nonnegative termwise integration for \(0\le r\le1\), that
\[\int_0^{\pi/2}\arcsin^2(r\sin t)\,dt=\frac\pi4\operatorname{Li}_2(r^2).\]
This proves the stated transfer identity. In particular the published chord-intersection cusp accounts for exactly half of the present convex-position cusp; the dilogarithm supplies the other half.

**4. Monotonicity, convexity and the small-radius expansion.** For \(0<x<\pi/2\) and \(0\le r<1\),
\[\partial_r a_r=\frac{\sin x}{\sqrt{1-r^2\sin^2x}}>0,\qquad
\partial_r^2a_r=\frac{r\sin^3x}{(1-r^2\sin^2x)^{3/2}}\ge0.\]
Therefore
\[Q'(r)=\frac8{\pi^3}\int_0^{\pi/2}(x+a_r)\partial_r a_r\,dx>0,\]
\[Q''(r)=\frac8{\pi^3}\int_0^{\pi/2}\big[(\partial_r a_r)^2+(x+a_r)\partial_r^2a_r\big]dx>0.\]
Dominated differentiation applies locally on \([0,1)\). The Taylor expansion \(a_r(x)=r\sin x+(r^3/6)\sin^3x+O(r^5)\), uniformly in \(x\), together with
\[\int_0^{\pi/2}x\sin x\,dx=1,\quad
\int_0^{\pi/2}\sin^2x\,dx=\pi/4,\quad
\int_0^{\pi/2}x\sin^3x\,dx=7/9\]
gives the stated expansion. At \(r=1\), \(a_1(x)=x\); both integrals in the exact formula equal \(\pi^3/24\), so \(Q(1)=1\).

**5. The logarithmic contact cusp.** Let \(r\uparrow1\) and \(\delta=1-r\). Uniformly near \(x=\pi/2\),
\[0\le\pi-x-a_r(x)\le C\big((\pi/2-x)+\sqrt{\delta+(\pi/2-x)^2}\big).\]
After multiplying by \(\partial_r a_r\) and integrating, this contributes only \(O(1)\) to \(Q'(r)\) compared with replacing \(x+a_r(x)\) by \(\pi\). In fact,
\[\int_0^{\pi/2}\partial_r a_r(x)\,dx
 =\frac1r\operatorname{arsinh}\frac{r}{\sqrt{1-r^2}}
 =\frac12\log\frac1{1-r}+O(1).\]
Thus
\[Q'(r)=\frac4{\pi^2}\log\frac1{1-r}+O(1),\]
and integration from \(1-\delta\) to \(1\) yields
\[1-Q(1-\delta)=\frac4{\pi^2}\delta\log(1/\delta)+O(\delta).\]
The full profile and endpoint behavior are thereby proved.

## Verification
The standalone `mixed_circle_check.py` evaluates the one-dimensional formula with adaptive quadrature and independently samples the four actual Euclidean points. Barycentric orientation tests detect whether either inner point lies in the triangle formed by the other three, with no use of the formula. Five radius values, endpoints, small-radius expansion and near-contact coefficient are tested. Monte Carlo numbers are evidence of implementation consistency only; every infinite and sharp statement above follows analytically. Run `python mixed_circle_check.py` with NumPy and SciPy.

## Relationship to prior work
The 2014 arXiv paper *Probability that n random points in a disk are in convex position* (Marckert, arXiv:1402.3512, primary MSC 52A22) gives the complete iid area-uniform disk model using recursively defined integrals, not two prescribed boundary radii. The 2015 paper *Around Sylvester's question in the plane* (Marckert, arXiv:1511.03658) studies iid area-uniform samples in convex domains and extremal shapes, again not the present stratified two-circle law. Both full HTML papers were inspected.

A separate earlier mixed-two-radius study gave the zero-radius limit of the convex-position probability for a binomial mixture of two circles, including the special \(2+2\) conditional limit \(Q(0)=1/2\). That limit is credited here and does not determine \(Q(r)\) for positive radius, its curvature or its sharp \(r\uparrow1\) asymptotics. A published nested-circle chord-crossing law gives the first integral of the new formula after a change of variables; its full result was inspected, and the exact transfer identity above exhibits the additional dilogarithmic contribution. A published thin-homothetic-shell result gives a logarithmic convexity defect for *area-uniform sampling from a continuous annular shell*, not for two samples on each of two distinct circles; its full result and distinct coefficient were compared. Classical Wendel-type half-circle ideas underlie the proof but do not imply the evaluated mixed-radius profile without the new bearing calculation. These comparisons establish separation from the inspected results, not a definitive priority certificate.

## Limitations
The formula concerns exactly two samples on each of two concentric circles. The original logarithmic cusp result is not asserted for other sampling laws or noncircular curves. A global numerical error bound for a chosen quadrature implementation is not proved. Historical priority remains subject to older and nonindexed geometric-probability literature; no independent mathematical audit has been performed.

## References
- J.-F. Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512, first public 2014-02-14; https://arxiv.org/html/1402.3512v1.
- J.-F. Marckert, *Around Sylvester's question in the plane*, arXiv:1511.03658, first public 2015-11-11; https://arxiv.org/html/1511.03658v1.
- J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111; https://doi.org/10.7146/math.scand.a-10655.
- *Logarithmic Sylvester defect for thin homothetic shells of smooth convex bodies*, publicly available comparison: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-logarithmic-sylvester-defect-for-thin-homothetic-shells-of-smoot--e7cc702edec5.
- *A logarithmic collision cusp and complete monotonicity for nested-circle random chords*, published comparison: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-logarithmic-collision-cusp-and-complete-monotonicity-for-neste--21cbc7a7c0ae.
