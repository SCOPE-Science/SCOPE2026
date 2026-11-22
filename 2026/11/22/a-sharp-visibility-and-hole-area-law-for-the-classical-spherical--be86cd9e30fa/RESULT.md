# A sharp visibility and hole-area law for the classical spherical napkin ring

## Finding
Let \(R>a>0\), set \(h=\sqrt{R^2-a^2}\), and let the **solid spherical ring** be
\[
K_{R,a}=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2\le R^2,\;x^2+y^2\ge a^2\}.
\]
For an orthogonal projection onto a plane perpendicular to a viewing axis making acute angle \(\theta\in[0,\pi/2]\) with the bore axis, denote by \(H_{R,a}(\theta)\) the area of the **bounded component of the complement** of the planar projected solid; define the area to be zero if no bounded complementary component exists. Put \(\theta_c=\arctan(a/h)=\arcsin(a/R)\), and, for \(\theta<\theta_c\), put \(\tau=(h/a)\tan\theta\).

**Theorem.** The projected solid has precisely one bounded complementary component for \(0\le\theta<\theta_c\), and none for \(\theta\ge\theta_c\). When present, the hole is *exactly* the intersection of two congruent ellipses with semiaxes \(a\cos\theta,a\) and centers separated by \(2h\sin\theta\) along their short axis. Its area is
\[
H_{R,a}(\theta)=
\begin{cases}
2a^2\cos\theta\left[\arccos\tau-\tau\sqrt{1-\tau^2}\right],&0\le\theta<\theta_c,\\
0,&\theta_c\le\theta\le\pi/2.
\end{cases}
\]
This area decreases strictly from \(\pi a^2\) to zero as \(\theta\) increases to \(\theta_c\). The collapse is nonanalytic, with the sharp law
\[
H_{R,a}(\theta_c-\eta)
=\frac{8\sqrt2}{3}R^2\sqrt{\frac a h}\,\eta^{3/2}+O_{R,a}(\eta^{5/2}),
\qquad\eta\downarrow0.
\]

For a uniformly random unoriented projection axis, \(C=|\cos\theta|\) is uniform on \([0,1]\). The resulting random hole area \(\mathcal H\) has an atom
\[
\Pr(\mathcal H=0)=\frac hR,
\qquad\Pr(\mathcal H>0)=1-\frac hR.
\]
Its remaining distribution is completely specified by the strictly increasing function \(G(c)=H_{R,a}(\arccos c)\) for \(h/R<c\le1\): for \(0<x<\pi a^2\),
\[
\Pr(\mathcal H\le x)=G^{-1}(x).
\]
Writing
\[
B_{R,a}=\frac{8\sqrt2}{3}\frac{R^{7/2}}{a\sqrt h},
\]
the non-atomic portion has the exact small-area onset
\[
\Pr(0<\mathcal H\le x)\sim\left(\frac{x}{B_{R,a}}\right)^{2/3}
\qquad(x\downarrow0).
\]
Finally the pair consisting of the **classical ring volume** \(V=4\pi h^3/3\) and the positive-hole viewing probability \(p=1-h/R\) uniquely reconstructs both generating radii:
\[
h=\left(\frac{3V}{4\pi}\right)^{1/3},\qquad R=\frac{h}{1-p},\qquad a=\sqrt{R^2-h^2}.
\]

## Assumptions and scope
The bore is coaxial with the Euclidean ball and passes completely through it. The remaining material is the **closed three-dimensional solid** outside the open cylindrical bore (boundary conventions do not change shadow area or topology of open holes). Rays are parallel and projected onto the perpendicular two-plane; overlapping rays contribute only once. The viewing axis is isotropic; we identify opposite orientations. The theorems assume fixed \(0<a<R\), with nonuniform limits possible as \(a/R\) approaches either endpoint. The missing region called a *hole* is bounded in the complement of the projected solid, not simply a dark or unilluminated patch in a perspective rendering.

## Proof
**Step 1: exact membership of a projected ray.** Rotational invariance allows a unit viewing vector \(u=(s,0,c)\), where \(s=\sin\theta\ge0\) and \(c=\cos\theta\ge0\). Use screen coordinates \((p,y)\) and the orthonormal frame \((c,0,-s),(0,1,0)\). A point on the associated ray is
\[
(x,y,z)=(cp+st,y,-sp+ct),\qquad t\in\mathbb R.
\]
The segment within the sphere is \(|t|\le Q=\sqrt{R^2-p^2-y^2}\), whenever \(p^2+y^2\le R^2\). If \(|y|\ge a\), this segment necessarily intersects the ring. For \(|y|<a\), let \(A=\sqrt{a^2-y^2}\). The maximum over that segment of \(|x|\) is exactly \(c|p|+sQ\). Hence **a screen point belongs to the shadow if and only if**
\[
p^2+y^2\le R^2,\quad
\left(|y|\ge a\ \text{or}\ c|p|+s\sqrt{R^2-p^2-y^2}\ge\sqrt{a^2-y^2}\right).
\]
This exact ray criterion, not any opaque-surface approximation, controls all the conclusions.

**Step 2: topology of missing rays.** Fix \(|y|<a\) and set \(q_y=\sqrt{R^2-y^2}\). The function \(f(p)=cp+s\sqrt{q_y^2-p^2}\), defined for \(0\le p\le q_y\), is concave (strictly for \(s>0\)) and has maximum \(q_y>A\). Therefore its superlevel set \(f(p)\ge A\) is a nonempty interval of the half-screen; all missing points in that half-screen not adjacent to \(p=0\) are connected through the outside of the spherical projection disk to the unbounded exterior. The possible bounded missing component consists precisely of points with \(f(|p|)<A\) and \(p\) near zero.

For \(s>0\), squaring the boundary equation \(f(p)=A\) yields the two algebraic candidates
\[
p_{\pm}=c\sqrt{a^2-y^2}\pm s h,
\qquad h=\sqrt{R^2-a^2}.
\]
The smaller candidate \(p_-\) is a genuine crossing when positive; the larger one can be extraneous after squaring and is not used for the hole boundary. These expressions also arise by projecting the sphere–bore intersection rim at heights \(\pm h\). An inner, missing interval exists precisely if \(p_{-}>0\), equivalently \(|y|<a\sqrt{1-\tau^2}\), where \(\tau=sh/(ca)\). It follows that a hole exists precisely when \(sh<ca\), equivalently \(\theta<\arctan(a/h)\). Its full shape is
\[
\mathcal O_{\theta}=\{(p,y):(|p|+sh)^2/c^2+y^2<a^2\}.
\]
This is the intersection of the interiors of the two ellipses
\[
(p-sh)^2/c^2+y^2<a^2,\qquad(p+sh)^2/c^2+y^2<a^2.
\]
The region is bounded, connected, and separated from the unbounded complement by the nonempty projected annular material. Conversely, horizontal sections of the shadow are either one interval or two intervals with this central gap, so no other bounded complementary components exist. At the threshold the region contracts to one screen point; that point lies on the projected solid, hence there is no open hole. The formula extends directly to \(s=0\), where the hole is the radius-\(a\) disk. For \(c=0\), the same ray criterion gives no open bounded hole.

**Step 3: area and monotonicity.** Integrate the central halfwidth \(p_{-}(y)=c\sqrt{a^2-y^2}-sh\) over its positive domain. With \(y_*=a\sqrt{1-\tau^2}\),
\[
H=4\int_0^{y_*}\left(c\sqrt{a^2-y^2}-sh\right)dy
=2ca^2\bigl[\arccos\tau-\tau\sqrt{1-\tau^2}\bigr].
\]
For any fixed \(|y|<a\), as \(c\) increases in \((h/R,1]\), the halfwidth \(c\sqrt{a^2-y^2}-h\sqrt{1-c^2}\) increases strictly wherever positive. Thus hole regions are strictly nested as \(c\) increases; their areas increase strictly from zero to \(\pi a^2\), proving invertibility of \(G\).

**Step 4: critical profile and probability.** As \(\tau\uparrow1\), elementary Taylor expansion gives
\[
\arccos\tau-\tau\sqrt{1-\tau^2}
=\frac{4\sqrt2}{3}(1-\tau)^{3/2}+O((1-\tau)^{5/2}).
\]
At the closing angle, \(\cos\theta_c=h/R\), and
\[
1-\tau=\frac{R^2}{ah}(\theta_c-\theta)+O_{R,a}((\theta_c-\theta)^2).
\]
Substitution proves the coefficient and remainder for \(H\). In terms of \(c\) approaching \(c_0=h/R\) from above, the corresponding expansion is
\[
G(c)=B_{R,a}(c-c_0)^{3/2}+O_{R,a}((c-c_0)^{5/2}),
\quad B_{R,a}=\frac{8\sqrt2}{3}\frac{R^{7/2}}{a\sqrt h}.
\]
The isotropic measure of an unoriented viewing direction makes \(c\) exactly uniform on \([0,1]\). Thus the probability of a hole is the interval length \(1-c_0\), the full CDF is the inverse of the monotone \(G\), and inversion of the last expansion gives the \(2/3\)-order continuous onset. The reconstruction statement follows from \(V=4\pi h^3/3\) and \(p=1-h/R\); its algebra has a unique solution with \(0<a<R\).

## Verification
The standalone program `verify_napkin.py` uses a separate one-dimensional integral for the hole area, checks the closed expression across several nondegenerate radii and angles, samples exact ray-intersection membership to verify that proposed hole points are absent from the shadow, checks critical power-law coefficients, and independently integrates the isotropic threshold indicator. It executed successfully with **6,824 numerical diagnostic assertions**. These floating-point checks are complementary to, not substitutes for, the all-parameter proof above.

## Relationship to prior work
The spherical ring (or napkin ring) has a classical height-only volume law, including the treatment of the sphere-with-bore geometry in Keith Devlin's *Volume of a napkin ring* (April 2008; the accessible document gives only a month, not an exact posting day) and the *Spherical Ring* MathWorld entry. Neither gives a moving-direction planar shadow-hole geometry or its probability law. A day-specific public demonstration of the classical construction is recorded on 2012-02-16 in the linked Mathematics Stack Exchange discussion.

Zachary Slepian's first-posted 2011-09-03 paper on mean projected area explicitly treats **convex** solids and the average area, not topological holes of this nonconvex drilled ball. The published *Two visibility transitions and a critical hole-area tail for torus shadows* concerns the Euclidean tubular neighborhood of a circle. Its \(3/2\)-order hole-area collapse involves erosion of a projected ellipse, and it does **not** cover the different sphere-minus-cylinder body or imply its explicit intersection-of-ellipses shape, viewing probability, and inverse-volume corollary. Related descriptive-geometry sources discuss projected penetration curves of cylinders and cones, but not the present stochastic shadow-hole statistic.

## Limitations
The law is specific to a **centered circular cylindrical bore through a Euclidean ball**, exact orthographic shadows, and isotropic viewing. Off-axis holes, oblique or noncircular bores, finite-distance cameras, partial transparency, and volume-weighted rather than orientation-uniform sampling are not covered. The critical remainder is for each fixed pair of positive radii; no uniform assertion is made as \(a/R\) approaches zero or one. Numerical checks are not an independent mathematical audit; historical priority cannot be guaranteed from available searches.

## References
- Keith Devlin, *Volume of a napkin ring*, April 2008 (month-only evidence), https://profkeithdevlin.org/wp-content/uploads/2023/09/napkinring.pdf.
- Eric W. Weisstein, *Spherical Ring*, MathWorld, https://mathworld.wolfram.com/SphericalRing.html.
- Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*, arXiv:1109.0595, first public v1 on 2011-09-03, https://arxiv.org/abs/1109.0595.
- A. Nicolas, *Given a solid sphere of radius R, remove a cylinder whose central axis goes through the center of the sphere*, Mathematics Stack Exchange, original answer 2012-02-16, https://math.stackexchange.com/questions/109908.
- *Two visibility transitions and a critical hole-area tail for torus shadows*, published research record, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-visibility-transitions-and-a-critical-hole-area-tail-for-tor--128776cbdf5e.
- T. M. Apostol and M. A. Mnatsakanian, *Unwrapping Curves from Cylinders and Cones*, American Mathematical Monthly 114 (2007), 388–416, https://doi.org/10.1080/00029890.2007.11920429.
