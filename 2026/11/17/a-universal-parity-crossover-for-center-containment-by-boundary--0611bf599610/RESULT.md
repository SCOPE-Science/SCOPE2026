# A universal parity crossover for center containment by boundary-sampled regular polygons

## Finding
Let \(m\ge3\) and \(n\ge2\) be integers. Choose \(n\) independent points uniformly by *Euclidean arclength* on the boundary of a centered regular \(m\)-gon \(P_m\). Write \(Q_{m,n}\) for the probability that their convex hull **does not contain** its center; boundary equality has probability zero. For every even \(m\), exactly
\[
Q_{m,n}=n2^{1-n}.
\]
For every odd \(m\), and every fixed \(T<\infty\), uniformly for integers \(n\ge2\) with \(0\le n/m^3\le T\),
\[
\boxed{\frac{Q_{m,n}}{n2^{1-n}}=R\!\left(\frac{n}{m^3}\right)+O_T(m^{-2}),\qquad R(t)=\int_0^1\cosh\!\bigl(\pi^2t\,u(1-u)\bigr)\,du.}
\]
Thus, along any sequence of odd \(m\to\infty\) and \(n/m^3\to t\in[0,\infty)\), the normalized failure probability converges to \(R(t)\). In contrast, the normalized failure probability remains identically one along *all* even polygon orders. The nonconstant crossover is strictly increasing for \(t>0\), with
\[
R(t)=1+\frac{\pi^4}{60}t^2+O(t^4)\quad(t\downarrow0),
\qquad R(t)\sim\frac{\exp(\pi^2 t/4)}{2\sqrt{\pi t}}\quad(t\to\infty).
\]
The scale \(m^3\) is the exact sampling scale at which odd-order boundary asymmetry becomes visible in the center-containment probability.

There is also a conditional angular limit. On the event of failure, almost surely precisely one sampled point begins the open, counterclockwise semicircle containing all other samples. For odd \(m\), let \(J\) be its side index and \(U_m\in[-1,1]\) its polar angular deviation from the outward normal of that side, divided by \(\pi/m\). The side index \(J\) is exactly uniform on the \(m\) sides and independent of \(U_m\) conditional on failure. If \(n/m^3\to t\), then \(U_m\) converges weakly to the density
\[
\boxed{\rho_t(u)=\frac{\exp\{\pi^2 t\,u(1-|u|)\}}{2R(t)},\qquad -1\le u\le1.}
\]
For \(t=0\) this is uniform. For \(t>0\) it preferentially selects the half of each side at which the counterclockwise semicircle contains more of the polygon's perimeter. Conditional on failure, the angular localization law is therefore not symmetric even though the polygon has reflectional symmetry.

## Assumptions and scope
The polygon is regular and nondegenerate; its radius is arbitrary because the event and distribution are scale invariant. Samples are independent with the **continuous uniform arclength** measure, not uniformly chosen polygon vertices or uniform area points. No sample is at a vertex, antipodal to another sample, or on a line through the center with positive probability. The probability \(Q_{m,n}\) refers to missing the center, *not* missing another fixed point and not a Hausdorff-distance event. The crossover is for \(m\to\infty\) over odd orders with bounded \(n/m^3\); its error statement does not claim uniformity when this ratio diverges. The even-order formula holds without asymptotics.

## Proof
**1. Semicircle representation.** Project each boundary point radially onto the unit circle; radial projection preserves its polar angle and whether the origin belongs to the sampled convex hull. A finite set of non-antipodal directions misses the origin exactly when all its directions lie in some open semicircle. In this event there is a unique sample angle \(\Theta\) that is the first point after the unique angular gap exceeding \(\pi\); the other \(n-1\) angles lie in \((\Theta,\Theta+\pi)\) counterclockwise. Let \(f_m(\theta)\) denote the angular density and \(h_m(\theta)=\int_\theta^{\theta+\pi}f_m(s)ds\), with periodic extension. The disjoint-start decomposition gives exactly
\[
Q_{m,n}=n\int_0^{2\pi} f_m(\theta)h_m(\theta)^{n-1}\,d\theta.\tag{1}
\]
This general semicircle integral is used as a known geometric-probability reduction; it is not itself claimed as an original result.

**2. Exact side-sector geometry.** Put \(\alpha=\pi/m\), choose a side whose outward normal has polar angle zero, and write \(x=\theta\in[-\alpha,\alpha]\) on that side. Its apothem is \(a\), and polar radius and arclength obey \(r=a\sec x\) and \(ds=a\sec^2x\,dx\). Since total perimeter is \(2ma\tan\alpha\),
\[
f_m(x)=\frac{\sec^2 x}{2m\tan\alpha},\quad |x|\le\alpha,
\]
extended with period \(2\alpha\). For even \(m\), central symmetry forces \(h_m\equiv1/2\), hence (1) gives the asserted exact identity. For odd \(m\), adding \(\pi=m\alpha\) changes the local sector coordinate by \(\alpha\) modulo \(2\alpha\). Using \(h_m'(x)=f_m(x+\pi)-f_m(x)\) and the reflection-axis value \(h_m(0)=1/2\), set \(C_m=(2m\tan\alpha)^{-1}\) and obtain the two *exact* expressions
\[
h_m(x)=\begin{cases}
\frac12+C_m[\tan(x+\alpha)-\tan x-\tan\alpha],&-\alpha\le x\le0,\\
\frac12+C_m[\tan(x-\alpha)-\tan x+\tan\alpha],&0\le x\le\alpha.
\end{cases}\tag{2}
\]
Because all \(m\) sides have equal length, (1) is equivalent to
\[
\frac{Q_{m,n}}{n2^{1-n}}=\int_{-1}^{1}w_m(u)[2h_m(\alpha u)]^{n-1}\,du,\quad
w_m(u)=\frac{\alpha\sec^2(\alpha u)}{2\tan\alpha}.\tag{3}
\]
The density \(w_m\) integrates to one on \([-1,1]\).

**3. Uniform two-parameter expansion.** Define \(g(u)=u(1-|u|)\) on \([-1,1]\), an odd function. Taylor's formula for \(\tan\) on a fixed neighborhood of zero, with a uniform remainder for \(|u|\le1\), applied to (2) gives
\[
2h_m(\alpha u)=1+\frac{\pi^2}{m^3}g(u)+O(m^{-5}),\qquad
w_m(u)=\frac12+O(m^{-2}),\tag{4}
\]
uniformly on \([-1,1]\) as odd \(m\to\infty\). For \(n/m^3\le T\), logarithmic expansion gives uniformly in \(u\)
\[
(n-1)\log[2h_m(\alpha u)]
=\frac{n}{m^3}\pi^2g(u)+O_T(m^{-2}).\tag{5}
\]
Indeed, the \(m^{-5}\) error multiplied by \(n=O_T(m^3)\) is \(O_T(m^{-2})\); the squared logarithmic term contributes only \(O_T(m^{-3})\), and replacement of \(n-1\) by \(n\) costs \(O(m^{-3})\). The exponent stays uniformly bounded, so exponentiating (5) and integrating against (4) in (3) yields
\[
\frac{Q_{m,n}}{n2^{1-n}}
=\frac12\int_{-1}^{1}e^{\pi^2(n/m^3)g(u)}du+O_T(m^{-2}).
\]
Oddness of \(g\) turns the integral into \(R(n/m^3)\). This proves the crossover, including the case \(t=0\).

**4. Shape of the crossover.** Differentiation under the finite integral gives \(R'(t)=\pi^2\int_0^1u(1-u)\sinh(\pi^2tu(1-u))du>0\) for \(t>0\). Expanding the hyperbolic cosine and using \(\int_0^1u^2(1-u)^2du=1/30\) gives the quadratic small-\(t\) coefficient. As \(t\to\infty\), the positive exponential in \(\cosh\) is dominated by the unique nondegenerate maximum of \(u(1-u)=1/4-(u-1/2)^2\), so elementary Gaussian Laplace integration yields \(R(t)\sim e^{\pi^2t/4}/(2\sqrt{\pi t})\).

**5. Conditional limit.** The unique starting point in step 1, conditional on failure, has density proportional to \(f_m(\theta)h_m(\theta)^{n-1}\). Periodicity makes its side index exactly uniform and independent of the normalized within-side coordinate. Formula (3) shows that the latter has conditional density \(w_m(u)[2h_m(\alpha u)]^{n-1}/[Q_{m,n}/(n2^{1-n})]\). Uniform convergence in (4)–(5) and positivity of \(R(t)\) give convergence in total variation to \(\rho_t\), which is stronger than the claimed weak convergence.

## Verification
Execute `python regular_polygon_crossover_checker.py` and `python regular_polygon_mc_checker.py` after installing `numpy` and `scipy` from `requirements.txt`. The first program checks the exact side-sector probability integral against the crossover function over multiple odd polygon orders, sampling scales, and the exact Taylor-coefficient identity. The second samples points *directly and uniformly on polygon sides*, computes their sorted angular gaps without using (1), and compares center-exclusion frequencies with analytic integrals for three through seven sides. Both provide finite corroboration; the uniform all-order proof is steps 1–5 above, not an extrapolation from the checks.

## Relationship to prior work
Wendel's 1962 theorem gives the centrally symmetric case of origin exclusion, and thus the even-order formula. The 1982 paper of Jewell and Romano gives general coverage/convex-hull probability methods, so the general exact semicircle reduction (1) is not represented as new. A published record entitled *Exact directional perimeter Winternitz law for regular polygons* derives the exact central-line boundary split for odd regular polygons and the \(m^{-3}\) angular imbalance. Its geometric angular-mass calculation overlaps equation (2) and motivates the relevant scaling; neither the fixed-sample coverage integral nor the *uniform joint \(n/m^3\) limit*, the explicit crossover \(R\), its \(O_T(m^{-2})\) error, or the failure-conditioned angular tilt are claimed in that work. The current claim is solely this two-scale random-sampling transition. Published studies of random boundary polytopes chiefly concern expected face counts and missed volume, not fixed-center inclusion.

## Limitations
The theorem is restricted to **regular** polygons, boundary arclength sampling, and a fixed center. It does not cover arbitrary odd polygons, nonuniform sampling, or a simultaneous limit with unbounded \(n/m^3\). The 1982 coverage paper was available as an abstract but its complete text was inaccessible in this inspection; it is a residual historical-priority risk and no whole-document exclusion is asserted. The cited directional-split result supplies a strong related exact geometric calculation, so originality concerns the distinct two-parameter probability and conditional limit, not those geometric preliminaries. Independent mathematical validation and exhaustive historical-priority verification remain outstanding.

## References
1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–112; public issue date 1962-06-01; DOI: 10.7146/math.scand.a-10655. Full original proof inspected at https://journals.msp.org/mscand/article/download/2688/2687/2719 .
2. N. P. Jewell and J. P. Romano, *Coverage problems and random convex hulls*, Journal of Applied Probability 19 (1982), 546–561; DOI: 10.2307/3213513. Abstract inspected; full text not accessible.
3. *Exact directional perimeter Winternitz law for regular polygons*, published mathematical research record `8f89b976a416` (2026), full `RESULT.md` consulted. This establishes the directional boundary-mass formula, not the stochastic crossover.
4. M. Reitzner, C. Schütt and E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, Discrete & Computational Geometry 69 (2023), 453–504; DOI: 10.1007/s00454-022-00460-2; introduction and stated theorems consulted.
