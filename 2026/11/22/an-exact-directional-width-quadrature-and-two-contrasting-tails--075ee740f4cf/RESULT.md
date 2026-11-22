# An exact directional-width quadrature and two contrasting tails for the Steinmetz tricylinder

## Finding

Let \(r>0\), and let the orthogonal *tricylinder* be the centrally symmetric compact convex body
\[
K_r=\{x\in\mathbb R^3:x_1^2+x_2^2\le r^2,\;x_1^2+x_3^2\le r^2,\;x_2^2+x_3^2\le r^2\}.
\]
For \(U\) uniform on \(S^2\), let \(W_r=h_{K_r}(U)+h_{K_r}(-U)=2h_{K_r}(U)\) be the one-dimensional orthogonal projection length. If \(a\ge b\ge c\ge0\) are the ordered absolute coordinates of a unit direction \(u\), its **entire support function** is
\[
\boxed{\frac{h_{K_r}(u)}r=
\begin{cases}
\sqrt{1+2bc},&a\ge b+c,\\[2pt]
(a+b+c)/\sqrt2,&a\le b+c.
\end{cases}}
\tag{1}
\]
The two branches agree at equality. In particular \(2r\le W_r\le\sqrt6\,r\).

The complete distribution has the following **one-dimensional, elementary quadrature**. Set \(t=w/(2r)\). For \(\phi\in[0,\pi/4]\), write
\[
s=\cos\phi+\sin\phi,\qquad
\theta_c=\arctan(1/s),\quad
\theta_m=\arctan(1/\cos\phi),
\]
\[
q_c=\sqrt{1+\frac{\sin(2\phi)}{2+\sin(2\phi)}},
\qquad
q_m=\frac{2\cos\phi+\sin\phi}{\sqrt{2(1+\cos^2\phi)}}.
\]
For \(1<t<\sqrt{3/2}\), define \(\Theta(t,\phi)\) by
\[
\boxed{\Theta(t,\phi)=
\begin{cases}
\arcsin\sqrt{\dfrac{t^2-1}{\sin(2\phi)}},&t<q_c,\\[8pt]
\arctan s-\arccos\dfrac{\sqrt2\,t}{\sqrt{1+s^2}},&q_c\le t<q_m,\\[8pt]
\theta_m,&t\ge q_m.
\end{cases}}
\tag{2}
\]
The first case never occurs at \(\phi=0\) for \(t>1\); values on other branch boundaries are taken continuously. Then
\[
\boxed{\Pr(W_r\le2rt)=\frac{12}{\pi}\int_0^{\pi/4}
\bigl[1-\cos\Theta(t,\phi)\bigr]d\phi.}
\tag{3}
\]
The CDF is zero for \(t\le1\) and one for \(t\ge\sqrt{3/2}\).

**Exactly uniform upper interval.** On the nontrivial interval \(4r/\sqrt3\le w\le\sqrt6\,r\), the survival function is *exactly linear*:
\[
\boxed{\Pr(W_r>w)=4\left(1-\frac{w}{\sqrt6\,r}\right).}
\tag{4}
\]
Consequently, conditional on \(W_r\ge4r/\sqrt3\), its distribution is exactly uniform on \([4r/\sqrt3,\sqrt6r]\). This conditioning event has probability \(4(1-2\sqrt2/3)\approx0.2287638337\).

**Logarithmic minimum-width tail.** As \(\varepsilon\downarrow0\), for fixed \(r>0\),
\[
\boxed{\Pr(W_r<2r+\varepsilon)
=\frac{3\varepsilon}{\pi r}\log\frac r\varepsilon+O(\varepsilon/r).}
\tag{5}
\]
Thus its density, where defined near the lower edge, cannot remain bounded there. The logarithm arises from the six intersections of the three great circles of minimum-width directions, whereas the exact linear upper law comes from eight isolated diametral vertices.

## Assumptions and scope

The constituent cylinders are **solid, infinite, equal-radius** right circular cylinders, centered at the origin with mutually perpendicular axes. A width means Euclidean caliper distance along a *line*, not the area of a two-dimensional shadow, nor the width of an individual cylinder. The viewing direction has normalized spherical area law. We use the continuous CDF convention, so equality cases are immaterial. Radius scaling is exact; the numbers in (1)–(5) are universal once widths are divided by \(r\). The theorem concerns this single fixed classical convex body family, not arbitrary finite intersections of quadratic cylinders.

## Proof

**1. Exact support function.** By scaling take \(r=1\). Sign-change and permutation symmetries allow \(u=(a,b,c)\) with \(a\ge b\ge c\ge0\) and \(a^2+b^2+c^2=1\). If \(a\ge b+c\), set \(Q=\sqrt{a^2+(b+c)^2}\) and
\[
x=\bigl(a/Q,(b+c)/Q,(b+c)/Q\bigr).
\]
Then \(x_1^2+x_2^2=x_1^2+x_3^2=1\), and \(x_2^2+x_3^2\le1\) follows from \(a\ge b+c\). Moreover, \(u\) is a nonnegative linear combination of the two active outward normals \((x_1,x_2,0)\) and \((x_1,0,x_3)\): choose coefficients \(b/x_2\) and \(c/x_3\) when \(b+c>0\), with the axial case obtained by continuity. The supporting-plane criterion for convex intersections therefore proves \(h(u)=u\cdot x=Q=\sqrt{1+2bc}\).

If \(a\le b+c\), the point \(v=(1,1,1)/\sqrt2\) lies on all three cylinder boundaries, and the active outward normals at \(v\) are proportional to \((1,1,0),(1,0,1),(0,1,1)\). The triangle inequalities \(a\le b+c\), \(b\le a+c\), and \(c\le a+b\) (the last two follow from ordering) permit \(u\) to be represented as their nonnegative combination. Therefore \(v\) supports \(u\), and \(h(u)=(a+b+c)/\sqrt2\). This proves (1) without presuming differentiability or an unverified optimization algorithm.

**2. One-quadrature CDF.** In the positive octant sorted chamber, use the spherical coordinates
\[
(a,b,c)=(\cos\theta,\sin\theta\cos\phi,\sin\theta\sin\phi),
\quad0\le\phi\le\pi/4,\quad0\le\theta\le\theta_m(\phi).
\]
The sphere area element is \(\sin\theta\,d\theta\,d\phi\), and this chamber has 48 sign/permutation copies. The axis-to-vertex support transition \(a=b+c\) is exactly \(\theta=\theta_c(\phi)\). From (1), the normalized support is
\[
H(\theta,\phi)=\begin{cases}
\sqrt{1+\sin^2\theta\sin(2\phi)},&\theta\le\theta_c,\\
(\cos\theta+s\sin\theta)/\sqrt2,&\theta\ge\theta_c.
\end{cases}
\]
The first branch is nondecreasing in \(\theta\). The second has derivative \((s\cos\theta-\sin\theta)/\sqrt2\ge0\) throughout \([\theta_c,\theta_m]\), because \(\theta_m\le\arctan s\) for \(0\le\phi\le\pi/4\). (Indeed \(\cos\phi(\cos\phi+\sin\phi)-1=\sin\phi(\cos\phi-\sin\phi)\ge0\).) Inverting the first branch gives the first line of (2). Writing \(\cos\theta+s\sin\theta=\sqrt{1+s^2}\cos(\theta-\arctan s)\) and using \(\theta\le\arctan s\) gives its second line. The third line saturates at the chamber boundary. Hence the sublevel region at fixed \(\phi\) is exactly \(0\le\theta\le\Theta(t,\phi)\). Its spherical area is \(1-\cos\Theta\). Multiplying by \(48/(4\pi)=12/\pi\) proves (3). There are no atoms, since every nonconstant support level is carried by a zero-area set on the sphere.

**3. Sharp upper interval.** In the axis-normal chamber, \(a\ge b+c\), the unit constraint gives
\[
1=a^2+b^2+c^2\ge(b+c)^2+b^2+c^2
=2(b^2+c^2+bc)\ge6bc.
\]
Thus \(h(u)^2=1+2bc\le4/3\). In a triangle-normal chamber the support equals the scalar product with the corresponding signed vertex \((\pm1,\pm1,\pm1)/\sqrt2\), whose norm is \(R_*=\sqrt{3/2}\). For a threshold \(t\ge2/\sqrt3\), no direction outside the triangle-normal chambers can have support above \(t\), and the eight superlevel sets are the eight disjoint spherical caps \(\{u:u\cdot v>t\}\) around signed body-diagonal vertices \(v\). Their angular radius is \(\arccos(t/R_*)\) and a single cap occupies probability \((1-t/R_*)/2\). Summing eight caps gives \(4(1-t/R_*)\), precisely (4). At \(t=2/\sqrt3\) all boundary equalities have area zero, so the formula holds at the endpoint. The maximum \(R_*\) is attained only at the eight diagonal directions.

**4. Logarithmic lower interval.** Equation (1) gives \(H\ge1\) and minimum exactly on the three coordinate great circles. To capture the leading logarithm, choose any sufficiently small fixed \(\eta>0\) and, about each of the six signed coordinate axes, use spherical tangent coordinates \((y,z)\) with \(|y|,|z|\le\eta\). There the dominant absolute coordinate exceeds the sum of the other two, so (1) is exact and
\[
H^2=1+2|yz|,\qquad d\sigma=\frac{dy\,dz}{\sqrt{1-y^2-z^2}}.
\]
Put \(s_\delta=((1+\delta)^2-1)/2=\delta+O(\delta^2)\). On one axial coordinate chart the event \(H<1+\delta\) is \(|yz|<s_\delta\). Its unweighted area is exactly, when \(s_\delta<\eta^2\),
\[
\int_{[-\eta,\eta]^2}{\bf1}_{|yz|<s_\delta}\,dy\,dz
=4s_\delta\bigl[1+\log(\eta^2/s_\delta)\bigr].
\]
The spherical Jacobian differs from one by \(O(y^2+z^2)\), whose integrated contribution on this product sublevel set is \(O(s_\delta)\). Away from the six axis charts, the minimum-width great circles are smooth, and the support grows at a uniformly positive one-sided linear rate transverse to them, as seen directly from the two branches in (1). Their remaining \(1+\delta\) sublevel neighborhoods therefore have area \(O(\delta)\). The six disjoint charts consequently contribute
\[
\Pr(H<1+\delta)=\frac{6\cdot4}{4\pi}\delta\log(1/\delta)+O(\delta)
=\frac6\pi\delta\log(1/\delta)+O(\delta).
\]
Substituting \(\delta=\varepsilon/(2r)\) proves (5). The error constant depends only on the fixed scale \(r\), and no finite sample is used to infer the logarithmic asymptotic.

## Verification

The standalone file `check_tricylinder_width.py` runs with Python 3, NumPy and SciPy. Execute `python check_tricylinder_width.py` in the extracted artifact directory. In a recorded replay it returned `TRICYLINDER_WIDTH_CHECKS_OK 251`. It compares the piecewise support value against independent constrained numerical optimization on 180 generated sphere directions; cross-checks the one-quadrature distribution against 262,144 scrambled Sobol sphere directions; verifies exact upper-tail values at nine thresholds; tests support bounds at 50 further points; and prints the progressively convergent logarithmic-tail ratios. The computations are diagnostic, not an exhaustive proof; the global assertions follow from the analytic arguments above.

## Relationship to prior work

Angell and Moore (1987) present the three-cylinder solid, its symmetries, orthographic views and exact bulk volume, not a random-direction support/width law. Their entire seven-page paper was materially inspected. The geometric section-area studies “Exact twelve-sector sections and cubic directional anisotropy of the Steinmetz tricylinder” (2026) and “Exact central-section area and six/eight-arc law of the orthogonal tricylinder” (2026) concern **central planar sections**, not support planes or one-dimensional width, so neither implies (1)–(5). Finch (first circulated October 4, 2011) derives width moments of the tetrahedron and cube, not these three-cylinder formulas. A published exact cube-width distribution does have its own constant upper density, but uses the linear cube support function and has a different lower tail; the exact tricylinder quadrature and six-axis logarithmic coefficient do not follow by a substitution. Earlier width work for the *bicylinder* treats the intersection of two perpendicular cylinders, which has a different support and tail coefficient. General spherical-cap arguments explain the linear upper portion after the new tricylinder support function has been established, not the global piecewise support law or the logarithmic lower tail.

## Limitations

The one-quadrature law is exact but not presented as an everywhere elementary antiderivative. The lower-tail remainder is only \(O(\varepsilon/r)\) at fixed radius. No claim is made for unequal radii, nonorthogonal axes, planar shadow *area*, or all higher-dimensional multi-cylinder intersections. The earliest relevant articles on intersection geometry describe volume and views, and a comprehensive historical-priority guarantee is not claimed: the 1974 paper and some historical texts were not materially available in full. An independent mathematical audit has not been performed.

## References

1. I. O. Angell and M. Moore, “Symmetrical Intersections of Cylinders,” *Acta Crystallographica A* **43** (1987), 244–250, DOI `10.1107/S0108767387099501`; full primary article inspected at `https://math.pro/db/attachment.php?aid=7715` (URL may require repository-specific access parameters).
2. Steven R. Finch, “Width Distributions for Convex Regular Polyhedra,” arXiv:1110.0671v1, first public 2011-10-04; HTML full text `https://arxiv.org/html/1110.0671v2`.
3. Moreton Moore, “Symmetrical Intersections of Right Circular Cylinders,” *Mathematical Gazette* **58** (1974), 181–185, DOI `10.2307/3615957`; accessible abstract only, material comparison limited.
4. “Exact twelve-sector sections and cubic directional anisotropy of the Steinmetz tricylinder,” published mathematical record, `https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-twelve-sector-sections-and-cubic-directional-anisotropy-of--428486a75562` (full result read).
5. “Exact central-section area and six/eight-arc law of the orthogonal tricylinder,” published mathematical record, `https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-central-section-area-and-six-eight-arc-law-of-the-orthogon--3c351c7fe62f` (full result read).
6. “Exact directional width law of the cube and its first spherical-cap transition,” published mathematical record, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2` (full result read).
