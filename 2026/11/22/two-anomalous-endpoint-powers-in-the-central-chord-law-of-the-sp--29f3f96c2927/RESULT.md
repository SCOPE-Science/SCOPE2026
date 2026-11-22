# Two anomalous endpoint powers in the central-chord law of the sphericon

## Finding

Let \(K_a\subset\mathbb R^3\) be the standard radius-\(a\) sphericon, constructed by cutting the right circular double cone of base radius and half-height \(a\) along an axial plane, rotating one half through a right angle about the normal to the cut, and rejoining. Through its centroid \(0\), choose an unoriented line with Haar-uniform direction \(U\in S^2\). Let \(L\) be the total length of its intersection with \(K_a\), and \(T=L/a\).

Then \(\sqrt2\le T\le2\), both endpoints are attained, and the complete distribution is determined by
\[
T=f(|U_1|)+f(|U_2|),\qquad f(t)=\frac1{t+\sqrt{1-t^2}}\quad(0\le t\le1).
\]
In particular, writing \(D_+=\{(x,y):x,y\ge0,\ x^2+y^2<1\}\),
\[
\Pr(T\le t)=\frac2\pi\int\!\!\int_{D_+}
\frac{\mathbf1\{f(x)+f(y)\le t\}}{\sqrt{1-x^2-y^2}}\,dx\,dy.
\]
The two extreme tails have **different anomalous powers**, with sharp coefficients:
\[
\boxed{\displaystyle
\Pr(T<\sqrt2+\varepsilon)=
\frac{2^{7/8}\Gamma(1/4)\Gamma(3/2)}{\pi\Gamma(7/4)}
\varepsilon^{3/4}+o(\varepsilon^{3/4})}
\qquad(\varepsilon\downarrow0),
\]
\[
\boxed{\displaystyle
\Pr(T>2-\varepsilon)=\frac7{3\pi}\varepsilon^2+o(\varepsilon^2).}
\]
There are precisely four minimizing oriented directions, \((\pm1/\sqrt2,\pm1/\sqrt2,0)\), and six maximizing oriented directions, the coordinate axes. Given a lower-tail event, each of four minimizing charts has asymptotic mass \(1/4\); its angular displacement divided by \(\sqrt\varepsilon\), and its vertical coordinate divided by \(\varepsilon^{1/4}\), are asymptotically uniform on
\[
\mathcal D_-:=\{(u,v):u^2+v^4/4<\sqrt2\}.
\]
Given an upper-tail event, the two vertical-axis charts have combined asymptotic mass \(3/7\), and the four horizontal-axis charts combined mass \(4/7\). Each vertical chart, scaled transversely by \(\varepsilon\), is uniform on \(\{|u|+|v|<1\}\); each horizontal chart is uniform on \(\{\sqrt{u^2+v^2}+|u|<1\}\). All these conditional convergences hold in total variation.

## Assumptions and scope

The sphericon is **the solid**, not just its developable boundary. Coordinates may be chosen so its upper and lower halves are
\[
K_a^+=\{(x,y,z):z\ge0,\ |x|+\sqrt{y^2+z^2}\le a\},
\qquad
K_a^-=\{(x,y,z):z\le0,\ |y|+\sqrt{x^2+z^2}\le a\}.
\]
Both meet along the same planar diamond \(z=0,\ |x|+|y|\le a\). Their union is the claimed solid. The sampling law is **Haar-uniform lines through the centroid**; it is not the Euclidean-motion-invariant law on all translated affine lines, nor uniform pairs of surface points. Equality at endpoints has probability zero. Coordinate-axis directions are counted as oriented points on the sphere for the marked limit; the central line itself is unoriented.

## Proof

**1. Exact radial formula and support.** For \(U=(u_1,u_2,u_3)\), the length of the positive ray inside whichever half has the same sign of \(u_3\) is \(a/(|u_1|+\sqrt{u_2^2+u_3^2})\); the opposite ray lies in the other half and contributes \(a/(|u_2|+\sqrt{u_1^2+u_3^2})\). Since \(\|U\|=1\), their sum is the displayed formula. The same formula is valid at \(u_3=0\) by continuity and by the common diamond. For \(0\le t\le1\),
\[
1\le t+\sqrt{1-t^2}\le\sqrt2.
\]
The left equality occurs only at \(t=0,1\), and the right equality only at \(t=1/\sqrt2\). Hence \(1/\sqrt2\le f(t)\le1\), with the specified minimizers and maximizers after imposing \(u_1^2+u_2^2\le1\). The image is the full interval by connectedness and continuity. The first-quadrant projection \((|U_1|,|U_2|)\) has density \(2/[\pi\sqrt{1-x^2-y^2}]\), yielding the exact CDF integral.

**2. Lower-end quartic degeneracy.** Parameterize the unit sphere with azimuth \(\theta\) and signed vertical coordinate \(z\):
\[
U=(\sqrt{1-z^2}\cos\theta,\sqrt{1-z^2}\sin\theta,z),
\qquad d\Pr=\frac{d\theta\,dz}{4\pi}.
\]
At each minimizing chart \(\theta=\pi/4+k\pi/2\), write \(\phi=\theta-(\pi/4+k\pi/2)\). Since \(f'(1/\sqrt2)=0\) and \(f''(1/\sqrt2)=\sqrt2\), Taylor expansion gives, uniformly as \((\phi,z)\to(0,0)\),
\[
T-\sqrt2=\frac1{\sqrt2}\left(\phi^2+\frac{z^4}{4}\right)
+o(\phi^2+z^4).
\]
The mixed leading term cancels between the two radial summands. Compactness and strictness of the four minima confine a sufficiently short-chord event to four fixed disjoint charts. Local coercivity then bounds the rescaled coordinates \(\phi/\sqrt\varepsilon\) and \(z/\varepsilon^{1/4}\). By the change of variables and dominated convergence, the probability divided by \(\varepsilon^{3/4}\) tends to four times the area of \(\mathcal D_-\) divided by \(4\pi\). Direct integration gives
\[
|\mathcal D_-|=4\,2^{7/8}\int_0^1\sqrt{1-t^4}\,dt
=2^{7/8}\frac{\Gamma(1/4)\Gamma(3/2)}{\Gamma(7/4)}.
\]
This proves the lower coefficient. The same indicator convergence in rescaled coordinates, with finite positive limiting area and bounded supports, yields total-variation convergence of conditional marked densities.

**3. Upper-end linear cones.** Near either vertical pole, use \(u_1=x,\ u_2=y\) as a local chart. Here
\[
2-T=|x|+|y|+o(\sqrt{x^2+y^2}).
\]
The limiting rescaled sublevel set is the diamond \(\mathcal D_z=\{|x|+|y|<1\}\) of area \(2\). Near \((1,0,0)\), with transverse coordinates \((y,z)\) and \(u_1=\sqrt{1-y^2-z^2}\), one instead has
\[
2-T=\sqrt{y^2+z^2}+|y|+o(\sqrt{y^2+z^2}),
\]
and the limit set \(\mathcal D_x=\{\sqrt{y^2+z^2}+|y|<1\}\) has area
\[
|\mathcal D_x|=\frac12\int_0^{2\pi}\frac{d\theta}{(1+|\cos\theta|)^2}=\frac43.
\]
There are four equivalent horizontal-pole charts. Each spherical local area density tends to \(1/(4\pi)\); the regions shrink linearly in two coordinates. Therefore
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr(T>2-\varepsilon)
=\frac{2\cdot2+4\cdot(4/3)}{4\pi}=\frac7{3\pi}.
\]
The vertical contribution is \(4/(28/3)=3/7\), and the horizontal contribution is \((16/3)/(28/3)=4/7\). The same rescaling/indicator argument proves the claimed conditional uniform limits in total variation.

## Verification

Run `python3 checks/verify_sphericon.py` from the unpacked finding directory. Its standard-library diagnostics reconstruct the two half-bicone rays, test the global support bounds, check lower quartic and upper linear local expansions, and numerically integrate both limiting tangent-region areas. It reports \(2.040949835686054\) and \(0.742723067762178\) for the two constants. An additional deterministic Sobol-direction experiment with \(2^{21}\) directions gave ratios of observed to leading predicted probabilities at \(\varepsilon=0.01\) of approximately \(1.055\) (lower) and \(1.034\) (upper); these finite-threshold ratios are not claimed to be error bounds or proofs.

## Relationship to prior work

The 1999 constructions of Stewart and Phillips describe the sphericon and its surface geometry, not the center-passing Haar-chord law above. MathWorld records its area, volume, centroid and inertia. Results about the extreme central chords of centrally symmetric **polytopes**, and about invariant *affine-line* chords in ellipsoids, concern different assumptions and do not imply the lower quartic degeneracy or the six-direction upper constant here. The distinction between central lines and affine-line sampling is essential.

## Limitations

The law is for the standard right-angle, equal-height-radius sphericon and center-passing lines only. It does not give the random translated-line chord law, an explicit elementary closed form for the entire CDF beyond the displayed integral, or uniform error bounds for endpoint asymptotics. It is an analytical result with corroborative finite numerical checks, not independent certification. Relevant full-text historical literature includes a 1999 magazine article whose publisher landing page was accessible but whose article body was not retrieved; absence of a chord statement there is not asserted solely from the landing page. Historical-priority risk remains.

## References

1. I. Stewart, “Cone with a Twist,” *Scientific American* **281** (1999), 116–117; published 1999-10-01. https://doi.org/10.1038/scientificamerican1099-116
2. T. Phillips, “The Differential Geometry of the Sphericon,” American Mathematical Society online column (1999), sections 1–7. https://www.math.stonybrook.edu/~tony/whatsnew/column/sphericon-1099/sphericon1.html
3. E. W. Weisstein, “Sphericon,” *MathWorld*, https://mathworld.wolfram.com/Sphericon.html
4. R. Kaufman, “The Sphericon,” *The N-Icon Study* (initial release 2007-09-06). https://www.interocitors.com/polyhedra/n_icons/Sphericon/index.html
5. American Mathematical Society, *MSC2020* classification, 52A22: random convex sets and integral geometry. https://mathscinet.ams.org/msc/msc2020.html?t=52A21
