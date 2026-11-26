# Square-root arclength cusps and inverse geometry at a Villarceau torus section

## Finding

Let \(R>r>0\), and let \(L(\beta)\) be the total Euclidean arclength of the intersection of the boundary of the standard circular ring torus with a central plane inclined by \(\beta\in[0,\pi/2]\) to its equatorial plane. Put \(a=\sqrt{R^2-r^2}\) and \(\beta_*=\arcsin(r/R)\). Use modulus conventions for the complete elliptic integrals:
\[
K(t)=\int_0^{\pi/2}\frac{du}{\sqrt{1-t^2\sin^2u}},\qquad
E(t)=\int_0^{\pi/2}\sqrt{1-t^2\sin^2u}\,du,\qquad
F(t)=E(t)-(1-t^2)K(t).
\]
At the Villarceau angle, the section consists of two circles of radius \(R\) intersecting at two points, so \(L(\beta_*)=4\pi R\). As \(\epsilon\downarrow0\),
\[
\begin{aligned}
L(\beta_*-\epsilon)&=4\pi R-C_-\sqrt\epsilon+o_{R,r}(\sqrt\epsilon),&
C_-&=\frac{8R}{r}\sqrt{2ra}\,F(r/R),\\
L(\beta_*+\epsilon)&=4\pi R-C_+\sqrt\epsilon+o_{R,r}(\sqrt\epsilon),&
C_+&=\frac{8R}{r}\sqrt{2ra}\,F(a/R).
\end{aligned}
\]
The coefficients are positive, giving a strict local maximum. The larger loss is on the plus side if \(R/r>\sqrt2\) and the minus side if \(R/r<\sqrt2\); the coefficients are equal at \(R/r=\sqrt2\). The ordered pair \((C_-,C_+)\) uniquely determines \((R,r)\). To reconstruct it, determine \(t\in(0,1)\) from the strictly decreasing ratio
\[
\frac{C_+}{C_-}=\frac{F(\sqrt{1-t^2})}{F(t)},
\qquad
R=\frac{C_-}{8\sqrt{2\sqrt{1-t^2}/t}\,F(t)},\qquad r=tR.
\]
The ratio runs from infinity to zero. No claim of global perimeter maximality is made; for instance \(L(0)=4\pi R\) as well.

## Assumptions and scope

The solid torus is \(T_{R,r}=\{(x,y,z):(\sqrt{x^2+y^2}-R)^2+z^2\le r^2\}\), with \(0<r<R\). By rotational symmetry the central plane is parametrized orthonormally by \((x,y,z)=(u,v\cos\beta,v\sin\beta)\). The length is one-dimensional Hausdorff measure of \(\partial T_{R,r}\) in this plane, not solid-section area or projected perimeter. The isolated crossing points have zero length. The little-oh estimates are pointwise for fixed nondegenerate radii.

## Proof

**Exact arclength quadrature.** In plane polar coordinates \((u,v)=(\rho\cos\varphi,\rho\sin\varphi)\), let \(s=\sin\beta\), \(q(\varphi)=\sqrt{1-s^2\sin^2\varphi}\), and \(w(\varphi)=\sqrt{r^2-R^2s^2\sin^2\varphi}\) on \(D_\beta=\{\varphi\in[0,2\pi):|R s\sin\varphi|\le r\}\). The equation on each admissible ray is \(\rho^2-2Rq\rho+a^2=0\). The two radii \(\rho_\pm=Rq\pm w\) are positive since \((Rq)^2-w^2=a^2>0\). Thus
\[
 L(\beta)=\sum_{\sigma\in\{+,-\}}\int_{D_\beta}
 \sqrt{\rho_\sigma^2+(\rho_\sigma')^2}\,d\varphi,\quad
 q'=-\frac{s^2\sin\varphi\cos\varphi}{q},\quad
 w'=-\frac{R^2s^2\sin\varphi\cos\varphi}{w}.
 \tag{1}
\]
For \(Rs\le r\) all rays are admissible; when \(Rs>r\) the angular intervals have integrable endpoint singularities where \(w=0\). The equatorial section consists of concentric circles of radii \(R\pm r\). At \(\beta=\pi/2\) the section is two circles of radius \(r\), giving \(L(\pi/2)=4\pi r\).

**An exact local hyperbola.** Squaring the equation \(u^2+v^2+a^2=2R\sqrt{u^2+v^2\cos^2\beta}\) introduces no extra real points because its left side is strictly positive. The result is
\[
Q_\beta(u,v)=(u^2+v^2-a^2)^2-4r^2u^2+4kv^2=0,
\qquad k=R^2\sin^2\beta-r^2. \tag{2}
\]
At \(k=0\) this is the product of \((u-r)^2+v^2-R^2\) and \((u+r)^2+v^2-R^2\), proving the asserted critical circles. Their nodes are \((0,\pm a)\), both transverse. Around either node set
\[
 U=\sqrt{r^2+k}\,u,\qquad V=\frac{u^2+v^2-a^2}{2}+k.
\]
These are smooth local coordinates for small \(k\); the inverse on each patch uses the fixed sign of \(v\). Substitution gives the exact identity
\[
 Q_\beta/4=V^2-U^2+a^2k-k^2. \tag{3}
\]
The plane metric in the chart is smooth in \((U,V,k)\); at \((U,V,k)=(0,0,0)\) it is \(r^{-2}dU^2+a^{-2}dV^2\). Write \(\eta=\sqrt{|a^2k-k^2|}\). For \(k>0\) the longitudinal coordinate is \(U\), and for \(k<0\) it is \(V\); the transverse coordinate is the other one. In each quadrant use the positive longitudinal distance \(x\). The smoothed model has transverse coordinate of magnitude \(\sqrt{x^2-\eta^2}\) for \(x\ge\eta\), compared with magnitude \(x\) for the critical ray. In longitudinal/transverse order the constant metric has weights \((p,q)=(1/r,1/a)\) for \(k>0\) and \((1/a,1/r)\) for \(k<0\).

**Constant-metric length defect.** Use a small square \(|U|,|V|\le\delta\) in each chart and put \(m=\sqrt{p^2+q^2}\). The change of length of one half-branch relative to its critical ray, in the constant metric, is
\[
\int_\eta^\delta\left(\sqrt{p^2+q^2x^2/(x^2-\eta^2)}-m\right)dx-m\eta
  =\eta J(p,q)+O_{R,r,\delta}(\eta^2),
\quad
J(p,q)=\int_1^\infty\left(\sqrt{p^2+q^2z^2/(z^2-1)}-m\right)dz-m. \tag{4}
\]
Here rescaling by \(\eta\) gives an integrable singularity at 1 and a tail of order \(z^{-2}\). The lost ray segment is included in \(-m\eta\). Substituting \(z=\sqrt{1+y^2}\) gives \(J(p,q)/m=I(\lambda)-1\), with
\[
 I(\lambda)=\int_0^\infty\frac{\sqrt{y^2+\lambda^2}-y}{\sqrt{1+y^2}}\,dy,
 \qquad \lambda=q/m.
\]
For \(0<\lambda<1\), differentiation under the integral and the substitution \(y=\lambda\tan u\) give \(I'(\lambda)=\lambda K(\sqrt{1-\lambda^2})\). Since \(I(0)=0\) by continuity, \(F'(t)=tK(t)\), and \(F(1)=1\) by continuous extension, \(I(\lambda)=1-F(\sqrt{1-\lambda^2})\). Consequently
\[
 J(p,q)=-mF(p/m). \tag{5}
\]

**Transfer to the plane metric.** Let \(g_k(z)\) be the smooth metric on a fixed chart square and write \(z\) in longitudinal/transverse order, using fixed coordinate sign changes for each quadrant. Replacing \(g_k\) by \(g_0\) costs \(O_{R,r,\delta}(|k|)\) in length because the graph in each quadrant has bounded Euclidean arclength and the metric changes uniformly by \(O_{R,r,\delta}(|k|)\). To compare the remaining metric corrections for the two curves, let \(B(z,w)=\|w\|_{g_0(z)}-\|w\|_{g_0(0)}\). Smoothness and uniform positive definiteness bound \(|\partial_z B|\le C|w|\), \(|\partial_w B|\le C|z|\) for \(w\ne0\), and \(|B(z,w)|\le C|z||w|\). The second bound follows by differentiating the two norms in \(w\), subtracting at \(z=0\), and using homogeneity of the gradients on nonzero velocities.

For \(x\in(\eta,\delta]\), write the two graph positions as \(z_\eta(x)=(x,\sqrt{x^2-\eta^2})\) and \(z_0(x)=(x,x)\), and put \(w_\eta=z_\eta'\), \(w_0=z_0'\). Their position difference is at most \(\eta^2/x\). Their derivative difference is \(x/\sqrt{x^2-\eta^2}-1\); multiplied by \(|z_0(x)|\), it is at most \(C\eta^2/\sqrt{x^2-\eta^2}\). Therefore
\[
 |B(z_\eta,w_\eta)-B(z_0,w_0)|
 \le C\eta^2\left(\frac1x+\frac1{\sqrt{x^2-\eta^2}}\right).
\]
The right side integrates to \(O_{R,r,\delta}(\eta^2(1+\log(\delta/\eta)))\), and the correction on the missing critical segment \([0,\eta]\) is \(O_{R,r,\delta}(\eta^2)\). Hence metric variation changes the length defect by \(o_{R,r}(\eta)\). The complement of the two squares is a smooth deformation of regular arcs. For either sign of \(k\), each endpoint on a chart square has one coordinate equal in magnitude to \(\delta\) and the other equal in magnitude to \(\sqrt{\delta^2-\eta^2}\); in the physical plane it varies smoothly up to \(k=0\) on that side. Regularity of the arc and transversality to the corresponding cutting side at \(k=0\) give an \(O_{R,r,\delta}(|k|)\) change of complementary length.

There are four half-branches per node and two nodes. Thus the leading total change is \(-8m\eta F(p/m)\). Since \(m=R/(ra)\) and \(\eta=a\sqrt{|k|}(1+O_{R,r}(|k|))\), this yields
\[
\begin{aligned}
 L(\beta)-4\pi R&=-\frac{8R}{r}\sqrt{k}\,F(a/R)+o_{R,r}(\sqrt k), && k\downarrow0,\\
 L(\beta)-4\pi R&=-\frac{8R}{r}\sqrt{-k}\,F(r/R)+o_{R,r}(\sqrt{-k}), && k\uparrow0.
\end{aligned}\tag{6}
\]
Finally \(k=2ra(\beta-\beta_*)+O_{R,r}((\beta-\beta_*)^2)\), which gives the two angular coefficients.

**Sign and reconstruction.** Since \(F(0)=0\), \(F(1)=1\), and \(F'(t)=tK(t)>0\) on \((0,1)\), both losses are positive. For \(t=r/R\), \(F(\sqrt{1-t^2})\) decreases from 1 to 0 while \(F(t)\) increases from 0 to 1. The ratio is strictly decreasing with the stated range, and equals one exactly when \(t=1/\sqrt2\). Substituting \(a=R\sqrt{1-t^2}\) into \(C_-\) gives the scale reconstruction.

## Verification

The supplied `checks/torus_section_checker.py` uses NumPy and SciPy. It evaluates (1) and separately computes chord sums for the same radial parametrization. It compares the cusp coefficients with numerical approach ratios for five aspect ratios, checks endpoints, and samples the inverse ordering. Run `python checks/torus_section_checker.py` from the package root. The recorded check count is 174. These are finite diagnostics, not the proof of the asymptotic or monotonicity. The exact coordinates and metric estimate above justify the limiting length defect without assuming a numerical result.

## Relationship to prior work

The two Villarceau circles and their tangent-plane geometry are classical [1–3]. The exact claim here concerns loss of total boundary arclength as the plane tilts through that angle, including the different one-sided coefficient values and inversion from the ordered pair. A related Villarceau result [4] instead studies the solid-section **area**; its logarithmic singularity does not give the boundary-length coefficients. The sphere–cylinder nodal transition [5] is a close analogue involving square-root length cusps and inverse geometry. Its use of a nodal smoothing mechanism is not a distinct contribution here; the torus has its own two-node normalization, angle conversion, and torus-specific reconstruction. These comparisons do not establish historical priority or exclude a broader equivalent evaluation elsewhere.

## Limitations

The asymptotic is local in angle and for fixed nondegenerate ring-torus radii. No result is claimed for noncentral sections, horn or spindle tori, general surfaces of revolution, or inversion from noisy estimates. The analytic and numerical checks concern correctness, not comprehensive literature coverage.

## References

1. A. Hirsch, *Extension of the “Villarceau-Section” to Surfaces of Revolution with a Generating Conic*, Journal for Geometry and Graphics **6** (2002). https://www.heldermann-verlag.de/jgg/jgg06/jgg0610.pdf
2. M. García Monera and J. Monterde, *Building a Torus with Villarceau Sections*, Journal for Geometry and Graphics **15** (2011), 93–99. https://www.heldermann-verlag.de/jgg/jgg15/j15h1mone.pdf
3. L. Moroni, *The toric section: intersection of a torus with a plane* (2017). https://www.lucamoroni.it/toric-sections/
4. *Logarithmic area cusp and Haar topology law at the Villarceau transition*. https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a
5. *Two-sided square-root length cusps and inverse geometry at the grazing sphere–cylinder transition*. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-two-sided-square-root-length-cusps-and-inverse-geometry-at-the-g--b35556e4cf39
