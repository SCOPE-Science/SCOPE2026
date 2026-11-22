# A sharp pre-extinction fold and singular conditioning in Simpson energy increments for shrinking circles

## Finding

Consider one Simpson energy-increment step with *exact* starting and midpoint dissipation data on a smooth circle evolving by curve-shortening flow. The scalar constraint has two positive endpoint radii for small steps, one double radius at a sharp fold, and no positive endpoint radius during a nonempty portion of the circle's physical lifetime. The correct small-step branch is strictly over-dissipative and its inverse scalar Jacobian diverges at the fold. Under the analogous exact-data energy-increment constraint, round spheres evolving by mean-curvature flow have no such obstruction: the scalar radius is exactly correct throughout the pre-extinction interval.

Precisely, for dimensionless time \(\xi=h/R_0^2\in(0,1/2)\), define
\[
B(\xi)=1-\frac{\xi}{6}\left(1+\frac4{\sqrt{1-\xi}}\right),\quad
F(\xi)=B(\xi)-2\sqrt{\frac\xi6},\quad
\Delta(\xi)=B(\xi)^2-\frac{2\xi}{3}.
\]
There exists exactly one \(\xi_*\in(0,1/2)\) with \(F(\xi_*)=0\), and
\[
\xi_*=0.4365745125924403897488686\ldots.
\]
For \(0<\xi<\xi_*\) the positive endpoint radii are exactly
\[
y_\pm(\xi)=\frac{B(\xi)\pm\sqrt{\Delta(\xi)}}2,
\qquad y=R_1/R_0.
\]
There is one double positive root \(y_*=\sqrt{\xi_*/6}\) at \(\xi=\xi_*\); there are none for \(\xi_*<\xi<1/2\). Thus the loss occurs before physical extinction, at \(2\xi_*=0.8731490251848807\ldots\) of the circle's initial extinction time.

The consistent branch satisfies \(y_+<\sqrt{1-2\xi}\) strictly throughout the interval and
\[
y_+(\xi)=\sqrt{1-2\xi}-\frac7{192}\xi^5+O(\xi^6),\qquad
 y_-(\xi)=\frac\xi6+O(\xi^2).
\]
Writing \(v_*=\sqrt{\xi_*/6}\) and \(G_*=\sqrt{-4v_*F'(\xi_*)}\), one has the sharp root-gap and normalized inverse-Jacobian laws
\[
\begin{aligned}
 y_+-y_-&\sim G_*\sqrt{\xi_*-\xi},\quad G_*=1.4751534132015147\ldots,\\
 \left|\frac{\partial H_\xi}{\partial y}(y_+)\right|^{-1}
 &\sim\frac{v_*}{G_*}(\xi_*-\xi)^{-1/2},\quad
 \frac{v_*}{G_*}=0.1828590146620118\ldots,
\end{aligned}
\]
where \(H_\xi(y)=y-B(\xi)+\xi/(6y)\).

## Assumptions and scope

The circle is perfectly smooth with starting radius \(R_0>0\), normal speed equal to minus its curvature, and exact continuous midpoint radius \(R(h/2)=R_0\sqrt{1-\xi}\). Its perimeter and squared-curvature dissipation are
\[
 W(R)=2\pi R,\qquad D(R)=\int_\Gamma\kappa^2\,ds=2\pi/R.
\]
Only the *scalar* Simpson update
\[
W(R_1)-W(R_0)+\frac h6\{D(R_0)+4D(R(h/2))+D(R_1)\}=0
\]
is imposed, with \(R_1>0\). No spatial polygon, BDF multistep history, predicted endpoint metric, nonlinear geometric evolution equation, or Lagrange-multiplier coupling is asserted to satisfy this idealized scalar closure. The equation is motivated by the endpoint/midpoint weights in Pan–Jiang–Jia's BDF3/BDF4 energy-increment construction [1, Eq. (2.11)]. The exact-data model isolates one aspect of that constraint rather than reproducing the coupled algorithm.

For the sphere comparison, a *round two-dimensional sphere embedded in three dimensions* evolves under mean-curvature flow with \(R'=-2/R\), \(W(R)=4\pi R^2\), and \(D(R)=\int_\Gamma H^2dA=16\pi\).

## Proof

**1. Scalar reduction.** The circle solves \(R'=-1/R\), hence \(R(t)^2=R_0^2-2t\) for \(0\le t<R_0^2/2\). Divide the scalar update by \(2\pi R_0\), write \(y=R_1/R_0\), and obtain
\[
 y-1+\frac\xi6\left(1+\frac4{\sqrt{1-\xi}}+\frac1y\right)=0.
\]
Since \(y>0\), multiplication by \(y\) is reversible and yields
\[
y^2-B(\xi)y+\frac\xi6=0.\tag{1}
\]
Equivalently, \(H_\xi(y)=y+\xi/(6y)-B(\xi)=0\).

**2. Exact positive-root classification.** By the arithmetic–geometric mean inequality, for \(y>0\),
\[
y+\frac\xi{6y}\ge 2\sqrt{\frac\xi6},
\]
with equality only at \(y=\sqrt{\xi/6}\). Consequently positive solutions exist iff \(F(\xi)\ge0\), with two distinct roots iff the inequality is strict. Direct differentiation gives
\[
F'(\xi)=-\frac16\left(1+\frac4{\sqrt{1-\xi}}\right)
-\frac{\xi}{3(1-\xi)^{3/2}}-\frac1{\sqrt{6\xi}}<0.
\]
Also \(F(0+)=1\), while \(F(1/2)= (11-4\sqrt2)/12-1/\sqrt3<0\). The intermediate-value theorem therefore gives exactly one simple \(\xi_*\in(0,1/2)\); solving (1) proves the stated full classification. For a useful rational upper bracket, at \(\xi=9/20\), \(\sqrt{1-\xi}<3/4\), so \(B<21/40<\sqrt{3/10}=2\sqrt{\xi/6}\). Thus \(\xi_*<9/20<6/13\).

**3. Physical branch, strict bias and consistency.** For fixed \(0<\xi<\xi_*\), put \(y_e=\sqrt{1-2\xi}\). The exact energy decrement normalized by \(2\pi R_0\) is \(y_e-1=-\int_0^\xi g(s)\,ds\), with \(g(s)=(1-2s)^{-1/2}\). The Simpson sum used in the constraint at \(y_e\) is \(\xi[g(0)+4g(\xi/2)+g(\xi)]/6\). The classical single-panel Simpson remainder is
\[
 \int_0^\xi g(s)\,ds-\frac\xi6\{g(0)+4g(\xi/2)+g(\xi)\}
 =-\frac{\xi^5}{2880}g^{(4)}(\zeta)<0
\]
for some \(\zeta\in(0,\xi)\), because \(g^{(4)}(s)=105(1-2s)^{-9/2}>0\). Hence \(H_\xi(y_e)>0\). Since \(\xi<\xi_*<6/13\), we have \(y_e^2=1-2\xi>\xi/6\), so \(y_e\) lies on the strictly increasing side of \(H_\xi\). Its larger zero must therefore satisfy \(y_+<y_e\). Expansion of the explicit roots at \(\xi=0\) gives
\[
 y_+=1-\xi-\frac{\xi^2}2-\frac{\xi^3}2-\frac{5\xi^4}8-\frac{175\xi^5}{192}+O(\xi^6),
\]
whereas \(\sqrt{1-2\xi}\) has fifth-order coefficient \(-7/8\). Their difference is \(-7\xi^5/192+O(\xi^6)\), and \(y_-=\xi/6+O(\xi^2)\).

**4. Fold and conditioning.** Put \(v(\xi)=\sqrt{\xi/6}\). Since \(B=F+2v\),
\[
 \Delta=B^2-4v^2=F(F+4v).
\]
At the unique simple zero, \(F'(\xi_*)<0\), so
\[
 \Delta(\xi)=-4v_*F'(\xi_*)(\xi_*-\xi)+O((\xi_*-\xi)^2).
\]
The exact gap \(y_+-y_-=\sqrt\Delta\) gives the stated square-root law. The normalized residual factors as \(H_\xi(y)=(y-y_+)(y-y_-)/y\), and hence \(H_\xi'(y_+)=(y_+-y_-)/y_+\). As \(y_+\to v_*\), the asserted inverse-Jacobian divergence follows. This describes a scalar Newton solve, **not** the full BDF–PFEM Schur complement.

**5. Exact sphere contrast.** For a shrinking round sphere, \(R'=-2/R\), \(W=4\pi R^2\), and \(D=16\pi\) at every nonextinct time. Every endpoint/midpoint Simpson average equals \(16\pi\) exactly. Therefore the scalar equation is \(4\pi(R_1^2-R_0^2)+16\pi h=0\), i.e.
\[
 R_1=\sqrt{R_0^2-4h}>0
 \quad\text{for every }0<h<R_0^2/4,
\]
uniquely on the positive-radius domain, and this is the exact physical flow.

## Verification

A standalone standard-library Python program `checker.py` verifies the quadratic-to-energy residual identity, root counts and strict inequalities for multiple rational and high-precision grid points, the bracketing and Newton fold constants, the fifth-order physical-branch bias, and the sphere identity. Execute `python3 checker.py` from this package. The numerical program supports, but does not replace, the symbolic arguments above; no finite numerical sampling proves the uniqueness or all-step quantifiers.

## Relationship to prior work

Pan, Jiang and Jia [1] formulate the positive-weight energy-increment constraint and prove that *solved* nondegenerate steps are energy decreasing (Proposition 2.4). They explicitly caution that this does **not** imply unconditional solvability, and provide only a necessary positive-energy condition (Eq. (2.15)). Their paper also studies the full BDF–PFEM Jacobian and a shrinking-circle benchmark. The present calculation classifies a distinct *exact-data homothetic scalar closure* completely, including its double-root condition number and sphere contrast; it does not contradict or establish properties of their fully coupled implementation.

The Simpson remainder used here is classical [2]. Its quadrature sign by itself does not supply the positive-root bifurcation or endpoint sensitivity. The circle/sphere comparison concerns different geometric energies and thus different scalar implicit equations; it is not a contradiction with either geometric flow.

## Limitations

Exact midpoint radius and curvature data are deliberately imposed. The analysis excludes errors from polygonal geometry, predicted endpoint metrics, alternating histories, finite elements, the BDF geometry equation, and inexact Newton solves. The fold therefore cannot be promoted to an impossibility result for the original coupled ES-BDF algorithm. The inverse-Jacobian law is a dimensionless scalar sensitivity, not a condition estimate for a full Jacobian. Only positive radii before physical extinction are classified. High precision decimals are approximations to a unique exact implicit root, not independently certified rational intervals. A mathematically equivalent earlier scalar construction may exist outside the inspected sources; independent validation remains outstanding.

## References

[1] Z. Pan, W. Jiang, J. Jia, *Energy-Dissipative, High-Order BDF Schemes for Simulating Geometric Flows via Energy Increments*, arXiv:2611.01593v1 (first public 2026-11-01), Sections 2.3, 4, and 6, https://arxiv.org/abs/2611.01593.

[2] Classical single-interval Simpson quadrature with fourth-derivative remainder; see standard numerical-integration references and the explicit remainder form in [1, Proposition 2.3].
