# Two independent brightness transitions and a quartic rare-view law for circular bicones

## Finding
Let \(K_{r,h}\subset\mathbb R^3\) be the closed, symmetric circular double cone
\[
K_{r,h}=\operatorname{conv}\bigl(\{(x,y,0):x^2+y^2\le r^2\}\cup\{(0,0,\pm h)\}\bigr),\qquad r,h>0.
\]
Set \(k=h/r\). For a uniform unit viewing normal \(U\), put \(Z=|U_3|\) and let \(B\) be the area of the orthogonal projection onto \(U^\perp\). Then \(Z\) is uniform on \([0,1]\). The result is the classification of the two global extremal transitions and the associated rare-view probabilities. Its starting point is the normalized directional profile \(F_k(z)=B/r^2\), which follows from the known single-cone profile by removing the base contribution (see the proof):
\[
\boxed{F_k(z)=\begin{cases}
2\bigl[\sqrt{k^2-(1+k^2)z^2}+z\arctan\bigl(z/\sqrt{k^2-(1+k^2)z^2}\bigr)\bigr],&0\le z<z_0,\\
\pi z,&z_0\le z\le1,
\end{cases}\quad z_0=\frac{k}{\sqrt{1+k^2}}.}\tag{1}
\]
The first formula at \(z=0\) uses its continuous value; both branches agree at \(z_0\). Its extremal directions have **two different sharp transitions**:

- For \(0<k\le1\), the sole least-bright latitude is \(z=0\), and \(m(k):=\min F_k=2k\). For \(k>1\), the least-bright latitude is a unique \(z_*(k)\in(0,z_0)\), characterized explicitly below.
- For \(0<k<\pi/2\), the sole greatest-bright latitude is \(z=1\), and \(M(k):=\max F_k=\pi\). At \(k=\pi/2\), both \(z=0\) and \(z=1\) attain \(M(k)=\pi\); for \(k>\pi/2\), solely \(z=0\) attains \(M(k)=2k\). Thus \(M(k)=\max\{\pi,2k\}\).

For \(k>1\), let \(t_*(k)\) be the unique positive solution to
\[
\boxed{\frac{1+t_*^2}{t_*}\arctan t_*=k^2},\qquad
z_*(k)=\frac{kt_*}{\sqrt{1+(1+k^2)t_*^2}},\qquad m(k)=F_k(z_*).\tag{2}
\]
On \([0,z_*]\), the brightness strictly decreases; on \([z_*,1]\), it strictly increases. For \(k\le1\), it strictly increases on \([0,1]\), apart from the vanishing derivative at the left endpoint. Consequently the **entire law** of \(B/r^2\) is given without further integration by the lengths of the level-set intervals in the uniform variable \(z\). In particular, for \(k>1\), write \(L_k(y)\in[0,z_*]\) and \(R_k(y)\in[z_*,1]\) for the unique inverse branches where their domains permit. Then
\[
\boxed{\Pr(F_k(Z)\le y)=\begin{cases}
0,&y<m,\\
R_k(y)-L_k(y),&m\le y<\min(2k,\pi),\\
R_k(y),&2k\le y<\pi\quad(1<k<\pi/2),\\
1-L_k(y),&\pi\le y<2k\quad(k>\pi/2),\\
1,&y\ge M,
\end{cases}}\tag{3}
\]
with the evident common-endpoint reading for \(k=\pi/2\). For \(k\le1\), the law is the single increasing inverse \(\Pr(F_k(Z)\le y)=F_k^{-1}(y)\) on \([2k,\pi]\).

The rare-orientation powers are **not** the same at the two transitions. At the lower endpoint, as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr(F_k(Z)\le m(k)+\varepsilon)\sim\begin{cases}
\sqrt{\frac{k}{1-k^2}}\,\varepsilon^{1/2},&0<k<1,\\
3^{1/4}\varepsilon^{1/4},&k=1,\\
2\sqrt{\frac{2}{F_k''(z_*)}}\,\varepsilon^{1/2},&k>1.
\end{cases}}\tag{4}
\]
At \(k=1\), conditionally on the lower-tail event, \(Z/(3\varepsilon)^{1/4}\) converges to the uniform distribution on \([0,1]\). More precisely, writing \(k=1+\delta\), the emerging minimizing latitude satisfies \(z_*(k)\sim\sqrt{3\delta}\), with \(F_k(0)-m(k)\sim3\delta^2\) as \(\delta\downarrow0\).

At the upper endpoint,
\[
\boxed{\begin{aligned}
&\Pr(F_k(Z)\ge\pi-\varepsilon)=\varepsilon/\pi &&(0<k<\pi/2;\;\varepsilon>0\text{ sufficiently small}),\\
&\Pr(F_k(Z)\ge\pi-\varepsilon)=\sqrt{\frac{\pi/2}{\pi^2/4-1}}\,\varepsilon^{1/2}+\varepsilon/\pi+O(\varepsilon^{3/2}) &&(k=\pi/2),\\
&\Pr(F_k(Z)\ge2k-\varepsilon)\sim\sqrt{\frac{k}{k^2-1}}\,\varepsilon^{1/2} &&(k>\pi/2).
\end{aligned}}\tag{5}
\]
Thus the two maximizing latitudes tie deterministically at \(k=\pi/2\), but almost all *near-maximal* random views there concentrate in the equatorial latitude, which has a square-root rather than linear tail.

For comparison, the tangency of the projected apices with the projected equatorial ellipse at \(z_0\) has a different power. Direct expansion of the profile gives a \(C^1\) but not \(C^2\) contact, and, as \(z\uparrow z_0\),
\[
\boxed{F_k(z)-\pi z\sim\frac{4\sqrt2}{3}\frac{(1+k^2)^{7/4}}{\sqrt{k}}(z_0-z)^{3/2}.}\tag{6}
\]

## Assumptions and scope
The double cone is the convex hull of a *filled equatorial unit disk* after normalization and two symmetric points of heights \(\pm k\). The height parameter \(h\) is the distance from the equatorial plane to either apex, not the total apex separation. Views are orthographic with Haar-uniform plane normals; opposite normals represent the same projection plane. Every probability above concerns normalized **planar projection area**, not perimeter, width, a planar section, or randomly chosen points in the body. The dimensionless deficit \(\varepsilon\) is area divided by \(r^2\). All assertions hold for fixed \(k>0\); the stated asymptotics are not asserted uniformly in \(k\) near the two thresholds. There are no atoms in the projected-area law.

## Proof
**1. From the single-cone profile to the bicone.** Scale to \(r=1\) and take \(U=(\sqrt{1-z^2},0,z)\). Let \(A_k^{\mathrm{cone}}(z)\) be the normalized brightness of the single cone with one apex at height \(k\) and the equatorial disk as base. Its base contributes \(\pi z/2\) to Cauchy's absolute-normal projection formula. The two halves of the bicone have equal absolute-normal integrals, since their normals are related by central reflection, and the equatorial disk is not a surface face. Thus
\[
F_k(z)=2A_k^{\mathrm{cone}}(z)-\pi z
=\frac12\int_0^{2\pi}\bigl|z+k\sqrt{1-z^2}\cos\phi\bigr|\,d\phi.
\]
The single-cone integral and its evaluation are given in [5]. In the bicone integral the expression has constant sign if \(z\ge c:=k\sqrt{1-z^2}\), giving \(\pi z\). Otherwise integration between the zeros of \(z+c\cos\phi\) gives \(2[S+z\arcsin(z/c)]\), where \(S=\sqrt{c^2-z^2}\) and \(\arcsin(z/c)=\arctan(z/S)\). This proves (1), including the equatorial value \(2k\) and axial value \(\pi\). Geometrically the equatorial disk projects to an ellipse with semiaxes \(z,1\), while the projected apices lie a distance \(c\) from its center along the first axis. The change of branch is therefore the apex–ellipse tangency \(c=z\).

**2. Complete critical-point and extremal classification.** Put \(S=\sqrt{k^2-(1+k^2)z^2}\), \(t=z/S\). Direct differentiation of the nontrivial branch yields
\[
F_k'(z)=2\left[\arctan t-\frac{k^2t}{1+t^2}\right]
=\frac{2t}{1+t^2}\left[H(t)-k^2\right],\quad H(t)=\frac{1+t^2}t\arctan t.\tag{7}
\]
The parameter \(t\) increases strictly from zero to infinity on \(0<z<z_0\), because \(t'(z)=k^2/S^3>0\). Furthermore
\[
H'(t)=\frac{t+(t^2-1)\arctan t}{t^2}>0.\tag{8}
\]
For \(t\ge1\), positivity is immediate; for \(0<t<1\), use \(\arctan t<t\), giving a strictly positive lower bound \(t^3\) in the numerator. Because \(H(0+)=1\) and \(H(\infty)=\infty\), (7) proves strict monotonicity for \(k\le1\), and precisely one interior minimum and the inverse-branch structure (2)–(3) for \(k>1\). The derivative on the elliptical-only branch is \(\pi>0\), and at the contact \(z=z_0\) the first derivative matches: \(F_k'(z_0-)=\pi\). Therefore the maximum must be one of \(F_k(0)=2k\) and \(F_k(1)=\pi\). Comparison gives exactly the global equality classes and the two sharp transition heights.

**3. Lower-tail asymptotics and the quartic contact.** Expansion of (1) at \(z=0\) gives for fixed \(k\)
\[
F_k(z)=2k+\frac{1-k^2}{k}z^2+O_k(z^4),\qquad
F_1(z)=2+\frac{z^4}{3}+\frac{2z^6}{5}+O(z^8).\tag{9}
\]
For \(k<1\), these and monotonicity give the first line in (4). At \(k=1\), solving \(F_1(z)=2+\varepsilon\) yields \(z=(3\varepsilon)^{1/4}(1+o(1))\), and because \(Z\) is uniform, the event is exactly an interval from zero to that root; this proves the second line and the conditional uniform limit. For \(k>1\), the positive second derivative at the unique interior minimum is
\[
F_k''(z_*)=\frac{2k^2}{S_*^3}
\frac{(1+t_*^2)-k^2(1-t_*^2)}{(1+t_*^2)^2}>0,\tag{10}
\]
where positivity follows equivalently from \(H'(t_*)>0\) and (7). The sublevel interval has length \(2\sqrt{2\varepsilon/F_k''(z_*)}(1+o(1))\), proving the last line of (4). Finally \(H(t)=1+2t^2/3+O(t^4)\) gives \(t_*^2\sim3(k-1)\), hence \(z_*\sim\sqrt{3(k-1)}\). Inserting the expansion (9), with its coefficient at \(k=1\), yields \(F_k(0)-F_k(z_*)\sim3(k-1)^2\).

**4. Upper tails and the competing-contact critical point.** If \(k<\pi/2\), the unique maximum at \(z=1\) has an entire neighborhood on which \(F_k(z)=\pi z\); there the superlevel event has exact length \(\varepsilon/\pi\). If \(k>\pi/2\), the sole maximizer is \(z=0\), and expansion (9) with negative quadratic coefficient implies the square-root coefficient in (5). At equality \(k=\pi/2\), both boundary neighborhoods contribute disjoint intervals: the equatorial one of length \(\sqrt{k/(k^2-1)}\,\varepsilon^{1/2}+O(\varepsilon^{3/2})\), and the axial one of length exactly \(\varepsilon/\pi\). There are no additional near-maximal directions by strict monotonicity on the branches. Their sum proves the middle formula of (5).

**5. The tangential-contact singularity.** For \(z<z_0\), the area excess over the ellipse is exactly \(2[S-z\arctan(S/z)]\). Writing \(w=S/z\), \(w-\arctan w=w^3/3+O(w^5)\). As \(z\uparrow z_0\), \(S^2=(1+k^2)(z_0^2-z^2)\sim2(1+k^2)z_0(z_0-z)\); substitution yields (6). Its positive coefficient proves the shadow-area profile has a continuous first derivative but a divergent one-sided second derivative at the ellipse/apex tangency.

**6. Mean-shadow consistency check.** The lateral area of the double cone is \(2\pi r\sqrt{r^2+h^2}\). Cauchy's average projected-area formula therefore gives \(\mathbb E[B]/r^2=\pi\sqrt{1+k^2}/2\). Integrating (1) against the uniform \(z\)-law yields the same value; this independently cross-checks the normalization.

## Verification
`check_bicone.py` uses independent convex-hull areas of finely sampled generating disks and the two apices; quadrature against Cauchy's mean-area formula; parameter-wide grid checks of both extrema; finite-difference checks of the analytic derivative; and asymptotic checks at the quartic critical point and near the emerging minimum latitude. The script prints its number of successful deterministic checks and can be run as `python3 check_bicone.py` after installing NumPy and SciPy. Finite polygonal approximations and numerical quadrature are **diagnostics only**, not proofs of (1)–(6). The infinite-family conclusions follow from the exact directional projection formula, monotonicity and local expansions proved above.

## Relationship to prior work
Vickers and Brown (2001) studied projected-area and perimeter distributions for convex particles, including conical particles [1]. The publication abstract does not resolve its exact overlap with the bicone results here. Finch studied cone and cylinder intrinsic volumes and mean widths [2], and the average projected-area formula gives the normalization check in §6 [3]. The known single-cone profile [5] gives (1) by reflection and subtraction of the base term. Neither (1), its tangency expansion (6), nor the inverse-CDF construction as a general procedure is claimed as an independent contribution. The single-cone global maximum switches instead at \(k=2.6414025\ldots\) [5]; the base term changes the optimization. The symmetric bicone's *projected perimeter* has a different obliquity transition at \(k=0.6627434\ldots\) [4], not an area transition. The contribution here is the bicone's global area-minimum bifurcation at \(1\), the separate global area-maximum switch at \(\pi/2\), and the resulting critical viewing laws: the quartic minimum and the unequal equatorial and axial contributions at the tied maximum.

## Limitations
The bicone must have congruent coaxial halves with a filled circular equator. The results do not cover unequal apices, skewed cones, opaque base-face variants, perspective viewing, or joint limits in which the aspect \(k\) approaches a critical value as the brightness deficit shrinks. The exact full CDF uses inverses of explicitly monotonic elementary functions, rather than a globally elementary closed-form inverse. The scientific novelty comparison is based on available full texts and related mathematical records and is not an independent historical-priority certificate.

## References
1. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proc. R. Soc. Lond. A **457** (2001), 283–306, DOI: 10.1098/rspa.2000.0667.
2. S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1 (first publicly posted 24 December 2012), https://arxiv.org/abs/1212.5946.
3. Z. Slepian, *The Average Projected Area Theorem — Generalization to Higher Dimensions*, arXiv:1109.0595 (2011), https://arxiv.org/abs/1109.0595.
4. *Sharp oblique orientation transition for the minimum shadow perimeter of a circular bicone*, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sharp-oblique-orientation-transition-for-the-minimum-shadow-peri--0f13e384bdf1.
5. *A sharp global brightness-direction switch for right circular cones*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-sharp-global-brightness-direction-switch-for-right-circular-co--19c34891a8b8.
