# Strict angular perimeter minimization for intersections of congruent ellipses

## Finding

For \(a>b>0\) and \(0\leq\theta\leq\pi/2\), let
\[
E_{a,b}=\bigl\{(x,y)\in\mathbb R^2:\frac{x^2}{a^2}+\frac{y^2}{b^2}\leq1\bigr\},\qquad
K_\theta=E_{a,b}\cap R_\theta E_{a,b}.
\]
Write \(P(\theta)=\operatorname{Per}(K_\theta)\), the ordinary Euclidean boundary length, not the boundary length of the union or the convex hull. For a noncircular ellipse, \(P(\theta)\) is strictly decreasing on \([0,\pi/2]\). In particular, among all orientations of two congruent centered elliptical disks, perpendicular principal axes uniquely minimize their intersection perimeter modulo the ellipse's half-turn and exchange symmetries.

Define \(A=a^2\), \(B=b^2\), and
\[
v(u)=\frac{ab\sqrt{B^2+(A^2-B^2)\sin^2u}}{[B+(A-B)\sin^2u]^{3/2}}.
\]
The complete perimeter profile has the exact one-dimensional representation
\[
\boxed{\quad P(\theta)=4\int_{\theta/2}^{\theta/2+\pi/2}v(u)\,du,\quad0\le\theta\le\pi/2.\quad}
\]
There are distinct sharp endpoint responses:
\[
P(0)-P(\theta)=2(a-b)\theta+O_{a,b}(\theta^2),\qquad\theta\downarrow0,
\]
\[
P(\pi/2-\eta)-P(\pi/2)=C_{a,b}\eta^2+O_{a,b}(\eta^4),\qquad\eta\downarrow0,
\]
with the positive exact coefficient
\[
\boxed{\quad C_{a,b}=\frac{4ab(a^2-b^2)(a^4-a^2b^2+b^4)}{(a^2+b^2)^{5/2}\sqrt{a^4+b^4}}.\quad}
\]
The first endpoint is a linear cusp if orientations are measured by the unsigned smaller angle; the perpendicular optimum has a nondegenerate quadratic gap.

## Assumptions and scope

The ellipse is compact, filled, noncircular and centered at the rotation point. The two copies have exactly the same semiaxes and are related by a planar rotation. The rotation parameter is the smaller angle between their unoriented major axes. The perimeter is the full \(1\)-dimensional Hausdorff measure of the intersection boundary. All formulas are for each fixed pair of positive semiaxes; no uniformity is claimed as \(b/a\to0\). The circular case \(a=b\) has constant intersection perimeter \(2\pi a\) and is excluded from strict statements.

## Proof

**1. The four crossing rays and the active boundary.** At polar angle \(u\), the boundary radius of the unrotated ellipse is
\[
\rho(u)=\frac{ab}{\sqrt{b^2\cos^2u+a^2\sin^2u}}.
\]
The rotated ellipse has radius \(\rho(u-\theta)\). Because \(a>b\), equality \(\rho(u)=\rho(u-\theta)\) for \(0<\theta<\pi/2\) is equivalent to
\[
\sin^2u=\sin^2(u-\theta),\qquad
u=\theta/2+k\pi/2,\quad k\in\mathbb Z.
\]
Between these rays the intersection's polar radius is the smaller of the two. An elementary sign comparison, e.g. at \(u=\pi/2\), shows that the unrotated ellipse contributes the arcs \(u\in(\theta/2,\theta/2+\pi/2)\) and their antipodes. The rotated ellipse contributes the other two congruent arcs. The perimeter is thus four times the length of a single unrotated active arc. The endpoint cases follow by continuity.

**2. Exact radial arc speed.** Differentiation gives
\[
\sqrt{\rho(u)^2+\rho'(u)^2}
=ab\frac{\sqrt{B^2+(A^2-B^2)\sin^2u}}{[B+(A-B)\sin^2u]^{3/2}}=v(u).
\]
Consequently \(P(\theta)=4\int_{\theta/2}^{\theta/2+\pi/2}v(u)\,du\) and the fundamental theorem of calculus gives, for interior angles,
\[
P'(\theta)=2\bigl(v(\pi/2+\theta/2)-v(\theta/2)\bigr).
\]

**3. A strictly positive polynomial certificate.** Let \(t=\sin^2(\theta/2)\), so \(0<t<1/2\). Define \(D(t)=B+(A-B)t\) and \(N(t)=B^2+(A^2-B^2)t\). Then
\[
v(\theta/2)^2=AB\frac{N(t)}{D(t)^3},\qquad
v(\pi/2+\theta/2)^2=AB\frac{N(1-t)}{D(1-t)^3}.
\]
Direct polynomial expansion and factorization gives the exact identity
\[
N(t)D(1-t)^3-N(1-t)D(t)^3
=(A-B)(1-2t)\Big[A^2B^2+t(1-t)(A-B)^2(A^2+3AB+B^2)\Big].
\]
Every factor is strictly positive when \(A>B>0\) and \(0<t<1/2\). Therefore \(v(\theta/2)>v(\pi/2+\theta/2)\), hence \(P'(\theta)<0\) throughout the open interval. Continuity at both ends completes strict monotonicity on the closed interval.

**4. Boundary sharpness.** We have \(v(0)=a\) and \(v(\pi/2)=b\). Thus \(P'(0+)=2(b-a)\), yielding the linear expansion. For the perpendicular endpoint use \(v(\pi/2+u)=v(\pi/2-u)\) to obtain \(P'(\pi/2)=0\). Direct differentiation of the displayed rational square-root expression gives
\[
P''(\pi/2)=\frac{8ab(A-B)(A^2-AB+B^2)}{(A+B)^{5/2}\sqrt{A^2+B^2}}>0.
\]
Taylor's theorem gives half this value as \(C_{a,b}\). Because swapping a relative rotation \(\pi/2+\eta\) for \(\pi/2-\eta\) does not change the intersection up to a global rigid motion, \(P\) has a smooth even continuation near \(\pi/2\). Its odd derivatives therefore vanish there, and the remainder improves to \(O_{a,b}(\eta^4)\). All steps use smooth positive denominators for fixed \(a>b>0\).

## Verification

The companion program `verify_ellipse_overlap.py` evaluates the exact integral, and independently computes the perimeter by selecting the smaller of the two polar radii across each crossing interval. It also checks strict monotonicity, the negative interior derivative, endpoint coefficients, and the circular boundary case for several aspect ratios, including a highly eccentric ellipse. Running `python verify_ellipse_overlap.py` with NumPy and SciPy available produced `ELLIPSE_OVERLAP_CHECKS_OK 629`. Numerical tests are diagnostics, not the proof; the factorization in Step 3 and analytic differentiation in Step 4 establish the continuum statement.

## Relationship to prior work

Hughes and Chraibi, *Calculating ellipse overlap areas* (first posted June 19, 2011, arXiv:1106.3787v1), derive algorithms for overlap **area** and ellipse segment and sector areas; their full preprint was inspected, including its general ellipse-ellipse overlap treatment and appendices. It supplies the historical source object but not the varying-angle **perimeter** inequality or its sharp endpoint coefficients. A published result on the Mahler product of perpendicular congruent ellipse intersections varies ellipticity at one fixed angle, so neither its invariant nor domain implies the angular perimeter profile here. A published equal-area centered ellipse convex-hull area identity concerns the opposite set operation and a different functional, again not the displayed claim. Details and remaining access limitations are documented in `AUDIT.json` and `REVIEW.md`.

## Limitations

No extension is proved for unequal semiaxis pairs, displaced centers, nonelliptical convex ovals, or arbitrary unions and convex hulls. We do not assert that the formula alone is a completely new identity in all historical geometry literature, or that the self-review is independent validation. The factorization establishes the stated perimeter result, while absolute historical priority remains subject to specialist verification. Independent audit has not been performed.

## References

- G. B. Hughes and M. Chraibi, *Calculating ellipse overlap areas*, arXiv:1106.3787v1, June 19, 2011, https://arxiv.org/html/1106.3787v1 (full text inspected).
- *Exact Mahler-product profile for intersections of perpendicular ellipses*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-mahler-product-profile-for-intersections-of-perpendicular--24e4e421284e (published record summary compared; complete text not accessible).
- *An affine-invariant exact convex-hull area law for equal-area ellipses*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-affine-invariant-exact-convex-hull-area-law-for-equal-area-el--ff4feeef7ef8 (published record summary compared; complete text not accessible).
