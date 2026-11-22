# Two sharp silhouette-contact laws and local inverse geometry for circular frusta

## Finding

Fix a right circular frustum with larger radius \(R\), smaller radius \(r\), and axial height \(H\), subject to \(R>r>0\) and \(H>0\). Write \(\delta=R-r\), \(L=\sqrt{H^2+\delta^2}\), and let \(\theta\in[0,\pi/2]\) be the acute angle between the frustum axis and the normal of an orthographic projection plane. Denote the projected area and perimeter by \(A(\theta)\) and \(P(\theta)\).

The smaller rim contributes a nonzero arc to the **outer** projected silhouette if and only if
\[
\theta>\theta_c=\arctan(\delta/H).
\]
For \(0\le\theta\le\theta_c\), the entire projected convex body is exactly the projected larger end disk: an ellipse of semiaxes \(R\) and \(R\cos\theta\). In particular \(A(\theta)=\pi R^2\cos\theta\) and \(P(\theta)=4R E(\sin\theta)\), where
\[
E(s)=\int_0^{\pi/2}\sqrt{1-s^2\sin^2 t}\,dt.
\]
For every fixed nondegenerate frustum, both excesses over this hidden-rim baseline have *sharp simultaneous* onset at \(\theta_c\). As \(\eta\downarrow0\),
\[
\begin{aligned}
P(\theta_c+\eta)-4R E(\sin(\theta_c+\eta))
 &= C_P\eta^{3/2}+O_{R,r,H}(\eta^{5/2}),\\
A(\theta_c+\eta)-\pi R^2\cos(\theta_c+\eta)
 &= C_A\eta^{3/2}+O_{R,r,H}(\eta^{5/2}),
\end{aligned}
\]
with the explicit positive coefficients
\[
C_P=\frac{4\sqrt2}{3}L\sqrt{\frac H\delta},\qquad
C_A=\frac{2\sqrt2}{3}(R+r)\frac{L^2}{\sqrt{\delta H}},\qquad
\frac{C_A}{C_P}=\frac{(R+r)L}{2H}.
\]
Thus both angle-dependent quantities are \(C^1\), but not \(C^2\), across this interior silhouette transition. If the projection plane normal is Haar-uniform (with antipodal directions identified), the probability that the smaller rim participates in the outer silhouette is \(H/L\).

**Local reconstruction theorem.** The three statistics \(P(0)\), \(\theta_c\), and \(C_P\) determine all three frustum dimensions uniquely. Explicitly,
\[
R=\frac{P(0)}{2\pi},\quad
L=\frac{3C_P}{4\sqrt2}\sqrt{\tan\theta_c},\quad
H=L\cos\theta_c,\quad r=R-L\sin\theta_c.
\]
Alternatively, the three finite-angle data \(P(0)\), \(\theta_c\), and \(P(\pi/2)\) determine the frustum, using \(P(\pi/2)=2(R+r)+2L\).

## Assumptions and scope

The solid is the convex hull of the Euclidean disks \(B_R\times\{0\}\) and \(B_r\times\{H\}\), where the planar disks are coaxial, centered, and parallel. All projections are orthographic onto planes through the origin; translation does not affect area or perimeter. The projection normal is measured by its acute axial angle, so the formulas are independent of the sign of the normal. No perspective camera, offset rim, oblique-axis frustum, or degenerate \(r=0\), \(r=R\), or \(H=0\) case is included. All expansions fix \(R,r,H\) before taking \(\eta\downarrow0\).

## Proof

**1. Exact projection and contact geometry.** In suitable orthonormal coordinates in the projection plane, the two circular end disks project to ellipses with boundaries
\[
(x,y)=(R\cos\theta\cos t,R\sin t),\qquad
(x,y)=(H\sin\theta+r\cos\theta\cos t,r\sin t).
\]
Orthographic projection commutes with convex hull. For \(\theta<\pi/2\), the invertible affine map \((x,y)\mapsto(x/\cos\theta,y)\) transforms those ellipses into ordinary disks of radii \(R\) and \(r\) with center separation \(D=H\tan\theta\). The small disk is contained in the large one exactly when \(D\le\delta\), which is \(\theta\le\arctan(\delta/H)\). For \(D>\delta\), two nondegenerate common exterior tangent segments and an exposed small-circle arc appear, so the condition is necessary and sufficient, including the equality boundary.

**2. Exact area.** For \(\theta_c<\theta<\pi/2\), put
\[
D=H\tan\theta,\quad \ell=\sqrt{D^2-\delta^2},\quad
\gamma=\arccos(\delta/D).
\]
The hull of the two transformed disks consists of the major arc of the larger disk, the minor arc of the smaller disk, and two common tangent segments. Direct application of the oriented area formula \(\tfrac12\oint(x\,dy-y\,dx)\) to those four pieces yields
\[
\operatorname{area}(\operatorname{conv}(B_R\cup(D e_1+B_r)))
=\pi R^2+(R+r)(\ell-\delta\gamma).
\]
Scaling back by determinant \(\cos\theta\) gives the **complete** area profile
\[
A(\theta)=\cos\theta\left[\pi R^2+(R+r)(\ell-\delta\gamma)\right]
\quad(\theta_c<\theta<\pi/2).
\]
It joins continuously to the baseline for \(\theta\le\theta_c\). At \(\theta=\pi/2\), the projected body is a trapezoid, giving \(A(\pi/2)=H(R+r)\), also the above formula's limit.

**3. Exact perimeter.** Put \(s=\sin\theta\), and for projected unit normal angle \(t\) define \(q_\theta(t)=\sqrt{1-s^2\cos^2t}\). The two projected ellipses have support functions \(Rq_\theta(t)\) and \(Hs\cos t+rq_\theta(t)\), respectively. Thus their hull has support
\[
h_\theta(t)=Rq_\theta(t)+[Hs\cos t-\delta q_\theta(t)]_+.
\]
Cauchy's planar perimeter formula is \(P=\int_0^{2\pi}h(t)\,dt\). The first term gives \(4R E(s)\). In the contact regime, the second term is positive exactly for \(|t|<\beta\) modulo \(2\pi\), where
\[
\beta=\arccos\left(\frac{\delta}{sL}\right).
\]
Consequently the **complete** perimeter profile is
\[
P(\theta)=4R E(s)+2\int_0^\beta
\left(Hs\cos t-\delta\sqrt{1-s^2\cos^2t}\right)dt
\quad(\theta_c<\theta<\pi/2).
\]
The correction is zero below the threshold. At \(\theta=\pi/2\), direct use of the integral or the trapezoid gives \(P(\pi/2)=2(R+r)+2L\). This support argument also accounts for the common tangent segments; no additional perimeter terms are missing.

**4. Sharp contact asymptotics.** Write \(\eta=\theta-\theta_c>0\). Because \(s_c=\delta/L\) and \(\cos\theta_c=H/L\), the integrand \(g(\theta,t)=Hs\cos t-\delta q_\theta(t)\) satisfies
\[
g(\theta_c+\eta,t)=L\eta-\frac{\delta L}{2H}t^2
+O_{R,r,H}(\eta^2+\eta t^2+t^4)
\]
near \((\eta,t)=(0,0)\). Its zero occurs at \(\beta=\sqrt{2H/\delta}\,\eta^{1/2}(1+O(\eta))\). Integrating the leading parabolic cap from \(-\beta\) to \(\beta\) gives
\[
\int_{-\beta}^{\beta}g\,dt
=\frac{4\sqrt2}{3}L\sqrt{H/\delta}\,\eta^{3/2}
+O(\eta^{5/2}),
\]
which is the stated \(C_P\). For area, \(D-\delta=(L^2/H)\eta+O(\eta^2)\), while elementary differentiation (or a Taylor expansion with \(\ell=\sqrt{D^2-\delta^2}\)) gives
\[
\ell-\delta\arccos(\delta/D)
=\frac{2\sqrt2}{3\sqrt\delta}(D-\delta)^{3/2}
+O_\delta((D-\delta)^{5/2}).
\]
Multiplying by \((R+r)\cos\theta\) produces the stated \(C_A\). Both coefficients are strictly positive, so the one-sided second derivatives of the excesses diverge positively as \(\eta^{-1/2}\); the full profiles are \(C^1\) but not \(C^2\) at the transition.

**5. Viewing probability and inverse geometry.** If the plane normal is uniformly distributed over unoriented directions, \(\lvert\cos\theta\rvert\) is uniform on \([0,1]\). Therefore \(\Pr(\theta>\theta_c)=\cos\theta_c=H/L\). The formula for \(P(0)\) identifies \(R\); \(\theta_c\) gives \(\delta/L=\sin\theta_c\) and \(H/L=\cos\theta_c\); \(C_P\) then uniquely determines the positive scale \(L\), yielding the explicit inverse in the finding. Replacing \(C_P\) with the side-on perimeter yields \(L=(P(\pi/2)-4R)/(2(1-\sin\theta_c))\). Positivity and \(r>0\) ensure uniqueness within the stated class.

## Verification

The included standard-library program `checks/frustum_checker.py` numerically evaluates the perimeter support integral, computes the independent convex hull of finely discretized projected rim polygons, compares both geometric quantities at multiple tilt angles and six nondegenerate frusta, verifies both sharp coefficients with shrinking offsets, and checks the two exact inversions. To reproduce from the folder containing this file, run `python3 checks/frustum_checker.py`. It records finite diagnostics only; the preceding analytic proof establishes the continuum claim.

## Relationship to prior work

The classical planar support/perimeter formula and common tangent geometry underlie the derivation. A March 31, 2011 mathematical discussion of the orthographic silhouette of a truncated cone explicitly observes that the outline is the larger projected ellipse when the smaller one is contained, and otherwise consists of elliptical arcs and two common tangents. This **already covers the qualitative silhouette classification**, which is not claimed as new here. Vickers and Brown (2001) develop projected area/perimeter statistics of cylinders, ellipsoids, right circular cones and tetrahedra, including a cone-specific ellipse-plus-point area calculation, but not this two-positive-radii frustum law. The distinct contribution asserted here is the pair of sharp nonanalytic coefficients and their exact local inverse-geometric consequences, together with the globally valid explicit area and perimeter profiles in a common normalization. The broader literature may contain equivalent special formulas; definitive priority needs independent historical review.

## Limitations

The local exponents and remainders hold only with fixed strictly positive radii difference and height, not uniformly as \(r\uparrow R\), \(r\downarrow0\), or \(H\downarrow0\). Inverse formulas concern noiseless, angle-labeled measurements, not error stability or statistical estimators. The exact area profile has no elliptic integral, while the general perimeter remains a one-dimensional elliptic-type quadrature. No claim about global angle extrema is made. The finite checker provides tests, not proof or independent certification. Historical priority beyond the inspected sources remains open.

## References

1. R. Israel, answer to “Cylinder silhouette,” Mathematics Stack Exchange, March 31, 2011, https://math.stackexchange.com/questions/30154/cylinder-silhouette/30169 .
2. G. T. Vickers and D. J. Brown, “The distribution of projected area and perimeter of convex, solid particles,” *Proceedings of the Royal Society A* **457** (2001), 283–306, https://doi.org/10.1098/rspa.2000.0667 .
3. R. Alexander, I. D. Berg, and R. L. Foote, “Integral-Geometric Formulas for Perimeter in S², H², and Hilbert Planes,” *Rocky Mountain Journal of Mathematics* **35** (2005), 1825–1857, https://arxiv.org/abs/math/0503313 .
4. E. W. Weisstein, “Conical Frustum,” MathWorld, https://mathworld.wolfram.com/ConicalFrustum.html (standard solid geometry only).
5. E. W. Weisstein, “Cauchy’s Perimeter Formula,” MathWorld, https://mathworld.wolfram.com/CauchysPerimeterFormula.html (classical planar perimeter identity).
