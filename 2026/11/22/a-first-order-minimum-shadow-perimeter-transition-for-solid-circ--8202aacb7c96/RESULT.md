# A first-order minimum-shadow-perimeter transition for solid circular cones

## Finding
Let \(C_{R,H}\) be the Euclidean solid right circular cone obtained as the convex hull of the radius-\(R\) disk in \(z=0\) and the apex \((0,0,H)\), with \(R,H>0\). Write \(\Pi_{R,H}(u)\) for the Euclidean perimeter of its *orthogonal planar projection* normal to \(u\in S^2\), and put \(h=H/R\) and \(c=|u\cdot e_3|\in[0,1]\). A side-on view has \(c=0\), an axial view \(c=1\).

**Theorem.** There exists exactly one threshold \(h_*\) with
\[
1<h_*<\sqrt{(\pi-1)^2-1}
\]
such that:

1. If \(0<h<h_*\), the side-on directions \(c=0\) are the **only** global perimeter-minimizing viewing latitudes.
2. If \(h=h_*\), side-on directions tie with at least one genuinely oblique latitude \(c\in(0,1)\); no axial view minimizes.
3. If \(h>h_*\), all global minimizing viewing latitudes lie strictly inside \(c\in(0,1)\), and the side-on latitude is not globally optimal.
4. Nevertheless, for **every fixed** \(h>0\), the side-on latitude is a *strict local minimum*, with the singular positive stability law
\[
\frac{\Pi_{R,H}(c)-\Pi_{R,H}(0)}R
=c^2\log\frac1c+O_h(c^2),\qquad c\downarrow0.
\]
Consequently the switch at \(h_*\) is discontinuous in viewing latitude: its competing oblique minimizers are bounded away from the side-on latitude.

Here \(\Pi_{R,H}(c)\) is independent of the azimuth of \(u\) by rotational symmetry. The threshold is given *exactly* as follows. For each \(c\in(0,1]\), there is a **unique** positive solution \(h_c\) of
\[
\Pi_{1,h_c}(c)=2+2\sqrt{1+h_c^2},
\]
and
\[
\boxed{h_*=\min_{0<c\le1}h_c.}
\]
The minimum is attained at an interior \(c\in(0,1)\). The one-dimensional perimeter formula below makes this characterization effective without requiring a uniqueness theorem for the competing oblique latitude. An ordinary floating-point solution of the tie and stationarity equations gives the *noncertified numerical indication* \(h_*\approx1.6014993045\) and \(c\approx0.7957267671\); the rigorously proved result is the exact minimax characterization and stated strict bounds, not the decimal enclosure.

## Assumptions and scope
The cone is solid (the filled convex hull), not a double cone, unbounded cone, conical lateral surface alone, or truncated cone. Perimeters refer to two-dimensional boundaries of orthogonal shadows, not projected *areas*, random intrinsic chords, or section lengths. Every \(R,H>0\) is covered. A viewing normal and its negative identify the same plane. All logarithms are natural and all angles radians.

Define for \(0\le\varphi\le\pi/2\) and \(0\le m\le1\) the elliptic integral
\[
E(\varphi\mid m)=\int_0^\varphi\sqrt{1-m\sin^2 t}\,dt,
\quad E(m)=E(\pi/2\mid m).
\]
For \(c\in[0,1]\), set \(s=\sqrt{1-c^2}\), \(m=1-c^2\). Then the exact normalized perimeter is
\[
\boxed{\frac{\Pi_{R,H}(c)}R=\begin{cases}
4E(m),&hs\le c,\\
2E(m)+2E(\alpha\mid m)+\displaystyle\frac{2h\sqrt{h^2s^2-c^2}}{\sqrt{1+h^2}},&hs>c,
\end{cases}}
\]
with \(\alpha=\arctan(1/\sqrt{h^2s^2-c^2})\). This includes its continuous endpoint limits
\[
\frac{\Pi_{R,H}(0)}R=2+2\sqrt{1+h^2},\qquad
\frac{\Pi_{R,H}(1)}R=2\pi.
\]

## Proof
**1. Exact support-function reduction.** Rescale by \(R\) and write \(h=H/R\). For a projection normal with axial cosine \(c\) and sine \(s=\sqrt{1-c^2}\), the base disk projects to a planar ellipse with semiaxes \(1,c\), while the apex projects to a point at signed distance \(hs\) from the ellipse center along its short-axis line. Thus the projected convex body is the convex hull of this ellipse and the point. In suitable planar coordinates its support function at angle \(t\) is
\[
g_{c,h}(t)=\max\left\{\sqrt{\cos^2t+c^2\sin^2t},\ hs\sin t\right\}.
\]
By Cauchy's perimeter formula, \(\Pi_{1,h}(c)=\int_0^{2\pi}g_{c,h}(t)\,dt\). If \(hs\le c\), the apex belongs to the ellipse and integration gives \(4E(m)\). If \(hs>c\), put \(z=\sqrt{h^2s^2-c^2}\); the apex term dominates precisely for \(t\in(\alpha,\pi-\alpha)\), with \(\alpha=\arctan(1/z)\). Integrating the remaining ellipse arcs and the apex interval gives the formula above. At \(c=0\), the hull becomes a triangle with base length \(2\) and equal sides \(\sqrt{1+h^2}\), proving the side-on value. At \(c=1\), its shadow is a unit disk.

**2. Monotone competition as height changes.** Fix \(c>0\), and set \(D_c(h)=\Pi_{1,h}(c)-\Pi_{1,h}(0)\). In the inactive regime \(hs\le c\), the first term is independent of \(h\). In the active regime, differentiating the support integral in \(h\) gives, because the switching terms agree at the moving boundary,
\[
\frac{\partial \Pi_{1,h}(c)}{\partial h}
=\frac{2\sqrt{h^2-(1+h^2)c^2}}{\sqrt{1+h^2}}.
\]
In both regimes the derivative is **strictly less** than that of the side-on perimeter, namely \(2h/\sqrt{1+h^2}\), for every \(h>0\), \(c>0\). Hence \(D_c\) is continuous and strictly decreasing in \(h>0\). At \(h=0\), its continuous limiting value is \(4E(1-c^2)-4>0\). On the other hand, using \(\max(a,b)\le a+b_+\) in the support formula gives \(\Pi_{1,h}(c)\le4E(1-c^2)+2hs\), and therefore \(D_c(h)\to-\infty\) as \(h\to\infty\) for each fixed \(c>0\). Consequently each \(D_c\) has exactly one zero \(h_c>0\).

**3. Short cones favor side views globally.** For \(0<c<1\) put
\[
J(c)=\int_0^{\pi/2}\frac{\sin^2t}{\sqrt{\cos^2t+c^2\sin^2t}}\,dt
\ge\frac\pi4.
\]
If \(hs\le c\), differentiation of the ellipse formula gives \(\partial_c\Pi_{1,h}=4cJ(c)>0\). Otherwise differentiating at the crossing gives
\[
\frac{\partial_c\Pi_{1,h}(c)}{2c}
=J(c)+J_0(c)-B_h(c),
\]
where \(J_0(c)=\int_0^\alpha\frac{\sin^2t}{\sqrt{\cos^2t+c^2\sin^2t}}\,dt\ge0\) and
\[
B_h(c)=\frac{h\sqrt{h^2-(1+h^2)c^2}}{(1-c^2)\sqrt{1+h^2}}.
\]
For \(0<h\le1\), the square of \(B_h(c)\), apart from the positive constant \(h^2/(1+h^2)\), is \((h^2-(1+h^2)x)/(1-x)^2\) with \(x=c^2\). Its derivative has numerator \(h^2-1-(1+h^2)x\le0\), so \(B_h(c)\le h^2/\sqrt{1+h^2}\le1/\sqrt2<\pi/4\). Thus \(\Pi_{1,h}(c)\) is strictly increasing in \(c\) throughout \([0,1]\) for \(0<h\le1\). In particular \(h_c>1\) for all \(c>0\).

**4. Side-on singular local stability.** For fixed \(h>0\), the active formula applies at all sufficiently small positive \(c\). Its first term is \(2E(1-c^2)\); the remaining incomplete-elliptic and elementary terms are real analytic functions of \(c^2\) near zero, since \(\alpha\to\arctan(1/h)<\pi/2\). The classical complete-elliptic endpoint expansion
\[
E(1-c^2)=1+\frac{c^2}{2}\left(\log\frac4c-\frac12\right)
+O(c^4\log(1/c))
\]
therefore yields \(\Pi_{1,h}(c)-\Pi_{1,h}(0)=c^2\log(1/c)+O_h(c^2)\). This proves strict local side-on minimality at every positive height. The error estimate is uniform for \(h\) in compact subintervals of \((0,\infty)\).

**5. Existence, sharpness, and discontinuity of the unique switch.** The map \(c\mapsto h_c\) is continuous for \(c\in(0,1]\), since \(D_c(h)\) is jointly continuous and has one strict height crossing. The uniform positive local-side estimate from step 4 implies \(h_c\to\infty\) as \(c\downarrow0\). At \(c=1\), the equality \(2\pi=2+2\sqrt{1+h^2}\) gives \(h_1=\sqrt{(\pi-1)^2-1}\). At this particular height, taking \(c<1\) sufficiently near one yields \(hs\le c\) and hence \(\Pi_{1,h}(c)=4E(1-c^2)<2\pi=\Pi_{1,h}(0)\). Therefore \(h_c<h_1\) for some \(c<1\). Thus \(h_*=\min_{c>0}h_c\) is attained in the open interval \((0,1)\) and satisfies \(1<h_*<h_1\).

For \(h<h_*\), every \(D_c(h)>0\); at \(h=h_*\), an interior latitude has \(D_c(h_*)=0\) and none is negative; for \(h>h_*\), evaluating at a minimizing latitude for \(h_*\) gives a strictly negative \(D_c(h)\) by step 2. Axial views are never globally optimal for positive \(h\), because for \(c<1\) sufficiently near one the apex is inactive and \(4E(1-c^2)<2\pi=\Pi_{1,h}(1)\). All post-transition global minima are therefore oblique. Finally, the compact-height-uniform local-side estimate ensures every competing minimizing latitude near \(h_*\) stays a fixed positive distance from \(c=0\). Hence the switch is first order and the theorem follows.

## Verification
The accompanying standalone `check_cone_shadow.py` checks the elliptic perimeter against independent planar convex-hull geometry for 180 random views of actual three-dimensional rim vertices and the apex; verifies analytic derivatives against finite differences; and checks short-cone monotonicity, local-side stability, monotonic height competition, and a floating-point stationary/tie candidate. It passed **738 diagnostic assertions** with NumPy and SciPy. Reproduce by running `python check_cone_shadow.py` from the package directory. These finite checks are corroborative; the all-parameter statements follow from the above inequalities and compactness argument. The quoted decimal values are illustrative and not interval-certified.

## Relationship to prior work
Vickers and Brown (2001), *The distribution of projected area and perimeter of convex, solid particles*, analyze a right circular cone's **projected area** (including a stationary-point transition) and give the convex-hull-of-ellipse-and-apex description. Their relevant cone section and Appendix A were inspected: these results do not provide the directional perimeter minimizer or its first-order height switch. Finch (arXiv:1212.5946, first posted December 24, 2012) treats **three-dimensional surface area and mean width** of cones; these are not the minimum perimeter of one planar shadow. The previously published circular-**bicone** shadow-perimeter theorem (published-finding corpus record `0f13e384bdf1`) has a different generating body, a continuous square-root optimal-angle bifurcation and a different threshold, and it does not imply the single-apex cone theorem. A separate right-cone result on **shadow area** (published-finding corpus record `19c34891a8b8`) concerns the maximum brightness, not the projected-boundary perimeter. Historical priority remains a best-knowledge assessment rather than a proof of uniqueness.

## Limitations
The proof classifies the global **side-on/oblique competition**, not the number or uniqueness of all oblique local/global minimizers at every height. The exact threshold is defined by a one-variable family of strict-crossing equations, not an elementary constant. Its decimal estimate is not rigorously enclosed. No assertion is made for oblique cones, bicones, noncircular bases, perspective silhouettes, or projection **area**. Prior literature beyond the inspected sources may yet contain an equivalent theorem.

## References
- G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proceedings of the Royal Society A 457 (2001), 283–306, DOI: 10.1098/rspa.2000.0667; https://doi.org/10.1098/rspa.2000.0667. Published 2001; exact first-public day not established.
- S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1, first publicly posted 2012-12-24; https://arxiv.org/abs/1212.5946. Related intrinsic-volume calculations.
- *Sharp oblique orientation transition for the minimum shadow perimeter of a circular bicone*, published published-finding corpus record `0f13e384bdf1`, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-oblique-orientation-transition-for-the-minimum-shadow-peri--0f13e384bdf1.
- *A sharp global brightness-direction switch for right circular cones*, published published-finding corpus record `19c34891a8b8`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-global-brightness-direction-switch-for-right-circular-co--19c34891a8b8.
- Cauchy's planar support-function perimeter identity (classical).
