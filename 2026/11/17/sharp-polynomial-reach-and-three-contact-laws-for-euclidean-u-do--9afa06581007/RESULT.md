# Sharp polynomial reach and three contact laws for Euclidean U-domains

## Finding
For arbitrary positive real numbers \(a,b,g,q\), let \(W=2a+g\), \(H=b+q\), and form the connected orthogonal U-polygon
\[
U=([0,W]\times[0,b])\cup([0,a]\times[0,H])\cup([a+g,W]\times[0,H]).
\]
Write \(V_U(t)=\operatorname{area}(U+tB_2)-\operatorname{area}(U)\), where \(B_2\) is the closed Euclidean unit disk. Put \(m=g/2\) and
\[
P_U(t)=(2W+4H-2b)t+\left(\frac{3\pi}{2}-2\right)t^2.
\]
Then the exact degree-at-most-two polynomial reach is
\[
\boxed{\operatorname{polreach}(U)=\min\{q,g/2\}.}
\]
Indeed \(V_U(t)=P_U(t)\) for every \(0\le t\le\min\{q,m\}\). At \(t=r+s\), where \(r=\min\{q,m\}\) and \(s\downarrow0\), the *first nonzero departure* has three sharp regimes:
\[
\boxed{
V_U(r+s)-P_U(r+s)=
\begin{cases}
\displaystyle \frac{s^3}{3q}+O(s^4),&q<m,\\[4pt]
\displaystyle -\frac43\sqrt{g}\,s^{3/2}+O(s^2),&q=m,\\[4pt]
\displaystyle -2(q-m)s-\frac43\sqrt{g}\,s^{3/2}+O(s^2),&q>m.
\end{cases}}
\]
In the last regime the linear term gives a genuine downward jump \(-2(q-m)\) in the derivative of the parallel-area function at its first contact radius. At the balanced critical depth \(q=m\) the function is differentiable at the threshold but has a nonintegral \(3/2\) onset; in the shallow-notch regime it is twice differentiable with a positive cubic onset. These three possibilities occur for connected eight-vertex polygons, even with fixed side-arm and base thicknesses.

## Assumptions and scope
All \(a,b,g,q\) are strictly positive; the two vertical side arms have equal thickness \(a\), the bottom bar has thickness \(b\), the open channel has width \(g\), and its depth is \(q\). Euclidean distance and two-dimensional Lebesgue area are used throughout. Polynomial reach means the supremum of initial radii on which \(V_U\) is exactly one polynomial of degree at most two, as in Cholaquidis–Cuevas–Moreno and Cholaquidis. The asymptotic remainder constants may depend on the fixed positive lengths. The statement concerns *outer* parallel volume, not inward offset or erosion.

## Proof
**1. Two single-elbow regions and their overlap.** Let
\[
A=[0,W]\times[0,b],\quad B=[0,a]\times[0,H],\quad C=[a+g,W]\times[0,H].
\]
Write \(Q_t=Q+tB_2\) for any compact \(Q\). Since \(U=A\cup B\cup C\), elementary inclusion–exclusion of the two overlapping sets \(A_t\cup B_t\) and \(A_t\cup C_t\) yields, at every \(t\ge0\),
\[
\operatorname{area}(U_t)
=\operatorname{area}((A\cup B)_t)+\operatorname{area}((A\cup C)_t)
-\operatorname{area}(A_t)-\Gamma(t),
\quad
\Gamma(t):=\operatorname{area}((B_t\cap C_t)\setminus A_t).
\]
The identical equality holds for undilated areas with \(\Gamma(0)=0\), since \(B\cap C=\emptyset\). Both \(A\cup B\) and \(A\cup C\) are congruent single-elbow L-domains with notch extension lengths \(p=a+g\) and \(q\).

Here is a self-contained exact area reduction for either L-domain. For \(L=([0,W]\times[0,b])\cup([0,a]\times[0,H])\), put \(F=[0,a]\times[0,b]\). Outside the upper-right open quadrant based at \((a,b)\), the nearest-point distance to at least one rectangle equals the distance to \(F\). In the translated quadrant \(X,Y\ge0\), the distances to the two rectangles and their intersection are respectively
\[
\sqrt{Y^2+(X-p)_+^2},\quad
\sqrt{X^2+(Y-q)_+^2},\quad
\sqrt{X^2+Y^2},
\quad z_+=\max(z,0).
\]
Consequently, defining
\[
T_{p,q}(t)=\operatorname{area}\big\{(X,Y)\in[0,\infty)^2:
Y^2+(X-p)_+^2\le t^2,\ X^2+(Y-q)_+^2\le t^2\big\},
\]
the intersection of the two rectangle offsets is \(F_t\) plus this quadrant domain minus the common quarter disk of radius \(t\). Applying the ordinary rectangle Steiner formula by inclusion–exclusion gives the all-radius identity
\[
V_L(t)=2(W+H)t+\frac{5\pi}{4}t^2-T_{p,q}(t).
\]
Both inequalities defining \(T_{p,q}(t)\) imply \(0\le X,Y\le t\). Thus \(T_{p,q}(t)=t^2\) whenever \(t\le\min(p,q)\). For \(q<p\) and \(q<t<p\), direct horizontal or vertical integration gives the *exact* deficit
\[
t^2-T_{p,q}(t)=E_q(t),\qquad
E_q(t):=\int_0^{t-q}\left(t-\sqrt{t^2-z^2}\right)dz
=\frac{(t-q)^3}{6q}+O((t-q)^4).
\]
Since both elbows have \(p=a+g\), the rectangle perimeter computation now yields, exactly for every \(t\ge0\),
\[
\boxed{V_U(t)=P_U(t)+2\bigl(t^2-T_{a+g,q}(t)\bigr)-\Gamma(t).}\tag{1}
\]
This separates single-elbow truncation from *new collisions between opposite arms*.

**2. The arm-to-arm contact law.** The Euclidean separation between \(B\) and \(C\) is \(g=2m\), so \(\Gamma(t)=0\) for \(0\le t\le m\). For \(m<t<\min\{q,g\}\), the intersection \(B_t\cap C_t\) in the channel \([a,a+g]\times[0,H]\) is a vertical rectangle of width \(2(t-m)\). Its portion above the base offset \(A_t\) has height \(q-t\). Above \(y=H\), the overlap consists of the *upper half* of the lens formed by radius-\(t\) disks centered at the two channel-mouth corners \((a,H)\) and \((a+g,H)\). This lens has area
\[
\Lambda_m(t)=2\int_0^{\sqrt{t^2-m^2}}\bigl(\sqrt{t^2-z^2}-m\bigr)dz
=t^2\arccos(m/t)-m\sqrt{t^2-m^2}.
\]
Since \(t<q\), the entire top lens is outside \(A_t\). Hence the exact first-contact formula is
\[
\Gamma(t)=2(t-m)(q-t)+\Lambda_m(t),\qquad m<t<\min\{q,g\}.
\tag{2}
\]
For \(t=m+s\), the substitution \(z=\sqrt{s}\,w\) in the integral gives
\[
\Lambda_m(m+s)=\frac43\sqrt{2m}\,s^{3/2}+O(s^{5/2})
=\frac43\sqrt{g}\,s^{3/2}+O(s^{5/2}).
\]
When \(q=m\), the base offset reaches height \(H+(t-q)\) inside the channel, so the part of the top lens with height \(z\le t-q=s\) is already covered. For all sufficiently small \(s>0\), the exact expression instead is
\[
\Gamma(m+s)=2\int_s^{\sqrt{(m+s)^2-m^2}}
\left(\sqrt{(m+s)^2-z^2}-m\right)dz.
\tag{3}
\]
The removed lower strip has area \(O(s^2)\), so \(\Gamma(m+s)=\frac43\sqrt{g}\,s^{3/2}+O(s^2)\).

**3. Three threshold regimes.** If \(q<m\), then for \(t\) just above \(q\) one still has \(t<m\), hence \(\Gamma=0\), and \(q<t<a+g\) as \(a+g>g>2q\). Equation (1) therefore gives \(V_U(t)-P_U(t)=2E_q(t)=\frac{(t-q)^3}{3q}+O((t-q)^4)>0\). If \(q>m\), then for \(t\) just above \(m\), the single-elbow terms still vanish (\(t<q<a+g\) is not needed; simply \(t<\min(q,a+g)\)), and (2) yields
\[
V_U(m+s)-P_U(m+s)
=-2(q-m)s-\frac43\sqrt{g}\,s^{3/2}+O(s^2)<0.
\]
Finally if \(q=m\), the elbow terms are \(O(s^3)\), whereas (3) gives the negative \(s^{3/2}\) term. In every case the deficit is identically zero below the claimed reach and strictly nonzero immediately above it. Any other quadratic agreeing on a larger initial interval would agree with \(P_U\) on an open interval and therefore coincide identically, a contradiction. The reach and all three onset expansions follow. The one-sided derivative and differentiability assertions follow directly from these expansions and the exact analytic formulas on either side.

## Verification
The accompanying `verify.py` uses an independent rectangular-distance point-grid integral for the three-piece union, against the analytical first-contact formulas, at six positive parameter sets on both sides of the transition. It also compares the leading asymptotic coefficients in each regime. Execute using `python verify.py` (Python 3, standard library only). The observed checks are finite numerical corroboration, not substitutes for the geometric set decomposition and asymptotic proof. The parameter ranges, exact formulas and their domain restrictions are in the code.

## Relationship to prior work
Cholaquidis, *Conic reach and polynomial parallel volume in the plane* (2026), establishes a general local quadratic tube formula for planar wedge-like sets, and gives the exact polynomial reach of a *single normalized L-shape* (Example 4.5, Proposition 6.3 and Appendix B.5). Neither that general positivity theorem nor its single-elbow computation gives the collision of two separate reentrant corners, the width-versus-depth critical line, or the three different onset exponents here. Cholaquidis–Cuevas–Moreno (2023) introduce and statistically estimate polynomial reach, with examples including separated squares and a frame; they do not classify this connected U family. Single-elbow L-domain calculations can support the first term in (1), but alone do not account for the arm-to-arm lens \(\Gamma\). In particular, the noninteger onset at the balanced critical line requires the additional overlap geometry, not merely a rescaling of the L-shape.

## Limitations
This is an exact statement for Euclidean planar, *symmetric-thickness* U-polygons with positive base and arm thicknesses. Unequal left and right arm widths, rounded corners, more than one channel, other norms and higher dimensions are not covered. The remainder constants are for fixed geometry and are not uniform at the regime boundary. The proof does not assert that the entire outer parallel area is polynomial beyond its first threshold or that every older unindexed geometric calculation has been excluded. No independent mathematical review has occurred.

## References
1. Alejandro Cholaquidis, *Conic reach and polynomial parallel volume in the plane*, arXiv:2607.24487, first posted 2026-07-27. https://arxiv.org/abs/2607.24487 (Theorem 6.1, Example 4.5, Proposition 6.3, Appendix B.5, Section 8).
2. Alejandro Cholaquidis, Antonio Cuevas, Leonardo Moreno, *On the notion of polynomial reach: a statistical application*, arXiv:2307.00373, first posted 2023-07-01. https://arxiv.org/abs/2307.00373 (definitions, Section 5 examples).
3. Matthias Heveling, Daniel Hug, Günter Last, *Does polynomial parallel volume imply convexity?*, Mathematische Annalen 328 (2004), 469–479, DOI 10.1007/s00208-003-0497-7 (global, rather than local, polynomial parallel volume).
