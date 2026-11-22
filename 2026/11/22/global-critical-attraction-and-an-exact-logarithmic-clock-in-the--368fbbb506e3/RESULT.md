# Global critical attraction and an exact logarithmic clock in the T-system

## Finding

Consider the normalized T-system
\[
\dot x=y-x,\qquad \dot y=mx-xz,\qquad \dot z=-nz+xy,
\]
with \(n>0\) fixed and \(m\ge-1\). The origin attracts **every** real initial condition, with a global forward solution, if and only if \(-1\le m\le0\).

At the nonhyperbolic threshold \(m=0\), define the global strong-stable set \(W^{ss}(0)\) as the set of initial conditions whose orbits converge exponentially to the origin. It is an immersed two-dimensional manifold extending the local strong-stable manifold, tangent at the origin to \(\{y=0\}\). Every orbit starting in \(W^{ss}(0)\) decays exponentially. For every other real initial condition, there is a sign \(\varepsilon\in\{-1,1\}\) and a finite real constant \(K\), depending on that orbit, such that
\[
\frac1{y(t)^2}=\frac2n t+
\left(\frac2n+\frac2{n^2}\right)\log t+K+o(1),\qquad t\to\infty.
\]
In particular, these nonexceptional orbits satisfy
\[
\lim_{t\to\infty}\sqrt t\,x(t)
=\lim_{t\to\infty}\sqrt t\,y(t)
=\varepsilon\sqrt{n/2},\qquad
\lim_{t\to\infty}t z(t)=1/2.
\]
The logarithmic coefficient is strictly positive for every \(n>0\). Thus no generic critical orbit has a purely linear reciprocal-square clock with bounded error.

## Assumptions and scope

Time is the normalized time of the displayed autonomous ordinary differential equation, not the unscaled physical time of a differently normalized T-system. The phase space is all of \(\mathbb R^3\). The global-attraction classification is for \(n>0\) and \(m\ge-1\); the quantitative critical laws are exclusively for \(m=0\), \(n>0\). Initial data are arbitrary real triples. The exceptional set \(W^{ss}(0)\) is defined by exponential decay, not by a guessed algebraic coordinate equation. In the critical law \(y(t)\) is nonzero for all sufficiently large \(t\) outside this exceptional set.

## Proof

**Global existence and the sharp parameter boundary.** For \(-1\le m<0\) put \(V=-m x^2+y^2+z^2\). It is positive definite and proper, and differentiation yields
\[
\dot V=2m x^2-2n z^2\le0.
\]
Every forward orbit remains bounded and exists globally. On the set where \(\dot V=0\), one has \(x=z=0\); invariance requires \(y=0\), because \(\dot x=y\). LaSalle's principle implies convergence to the origin.

For \(m=0\), instead set \(V=y^2+z^2\). Exactly \(\dot V=-2nz^2\), so \(y,z\) are bounded. The variation-of-constants formula
\[
x(t)=e^{-t}x(0)+\int_0^t e^{-(t-s)}y(s)\,ds
\]
bounds \(x\), hence the solution is global. The compact omega-limit set is contained in \(\{z=0\}\). On any entire orbit therein, \(z=0\) forces \(xy=0\). If \(y\ne0\) at any time, continuity forces \(x=0\) locally, contradicting \(\dot x=y\). Therefore \(y=0\) throughout and \(x\) solves \(\dot x=-x\). A bounded complete orbit in this line is necessarily the origin. Thus every critical orbit converges to the origin. Lyapunov stability at the origin also follows from the nonincreasing \(y^2+z^2\) and the displayed bound for \(x\).

For \(m>0\), the two additional equilibria \((\pm\sqrt{mn},\pm\sqrt{mn},m)\) prevent attraction of every initial state by the origin. This proves the stated if-and-only-if parameter boundary.

**Center reduction in the critical case.** The linearization at the origin for \(m=0\) has eigenvalues \(0,-1,-n\). Its center eigendirection is \((1,1,0)\) and its stable plane is \(\{y=0\}\). A local smooth one-dimensional center manifold may be parametrized by \(s=y\) as \(x=h(s),z=k(s)\). The symmetry \((x,y,z)\mapsto(-x,-y,z)\) and the invariance equations
\[
h'(s)(-h(s)k(s))=s-h(s),\qquad
k'(s)(-h(s)k(s))=-nk(s)+s h(s)
\]
fix the Taylor coefficients, whether or not the global choice of center manifold is unique:
\[
\begin{aligned}
h(s)&=s+\frac{s^3}{n}+\frac{5n+2}{n^3}s^5+O(s^7),\\
k(s)&=\frac{s^2}{n}+\frac{n+2}{n^3}s^4+O(s^6).
\end{aligned}
\]
In particular the reduced scalar field is
\[
\dot s=-h(s)k(s)
=-\frac{s^3}{n}-\left(\frac2{n^2}+\frac2{n^3}\right)s^5+O(s^7).
\]
The cubic term is strictly dissipative, so every sufficiently small nonzero center trajectory retains its sign and tends to zero. For such a trajectory put \(w=s^{-2}\). Then
\[
\dot w=\frac2n+\frac{4(n+1)}{n^3}\frac1w+O(w^{-2}).
\]
Initially \(w(t)\sim 2t/n\). Integration first gives \(w(t)=2t/n+O(\log t)\). Substituting this estimate back, the derivative of
\[
w(t)-\frac2n t-\left(\frac2n+\frac2{n^2}\right)\log t
\]
is \(O(\log t/t^2)\), hence integrable on a late-time half-line. The displayed expression therefore tends to a finite real constant. This proves both the claimed inverse-square clock and the leading center-coordinate asymptotics.

**From the center manifold to every initial condition.** Standard smooth center-manifold exponential tracking in the stable directions applies because both remaining eigenvalues have strictly negative real parts for every fixed \(n>0\). Every sufficiently late segment of any orbit approaching the origin is exponentially shadowed by some center-manifold orbit. The center shadow is identically zero exactly for points in the local strong-stable manifold, which extends by backwards flow to the global exponential-decay set \(W^{ss}(0)\). For every point outside it, the shadow has a constant nonzero sign. The exponential tracking error is negligible after applying the reciprocal-square transformation to a center amplitude of order \(t^{-1/2}\). Thus the center clock, with possibly a different finite constant, holds for the original coordinate \(y(t)\). Finally \(h(s)=s+O(s^3)\), \(k(s)=s^2/n+O(s^4)\) give the stated asymptotic limits of \(x(t)\) and \(z(t)\).

## Verification

The standalone `checker.py` computes the invariance-equation Taylor coefficients over an exact rational-function field in \(n\), verifies both Lyapunov derivatives, checks the reduced quintic field, and checks the resulting logarithmic coefficient. It also evaluates exact rational residual coefficients for positive rational parameters. Run `python checker.py` with SymPy available. Independently, numerical integrations for \(n\in\{1/2,1,2,3\}\) to normalized time \(20000\) show convergence of the predicted renormalized reciprocal-square offset. Those integrations are diagnostics only; the proof above establishes the all-time statement.

## Relationship to prior work

Constantinescu, *On the Bifurcations of a 3D Symmetric Dynamical System* (2023), Proposition 2 and Section 3.1, establishes the center-stable dimensions and pitchfork at \(m=0\) and studies a different singular limit \(n=0\). It does not state the global \(m\le0\) attraction classification or the physical-time inverse-square and logarithmic laws. Munteanu, *Jacobi Stability for T-System* (2024), studies KCC Jacobi stability and equilibrium spectra rather than trajectory-resolved critical relaxation. Van Gorder and Choudhury (2011) study Hopf bifurcations of nonzero equilibria; their early stability section lists the origin's linear spectrum but not the nonlinear critical clock. These existing results establish motivation and some prerequisites, not the displayed nonlinear asymptotic expansion.

## Limitations

The result does not determine an explicit global equation for \(W^{ss}(0)\), nor does it classify dynamics for \(m>0\) beyond showing failure of global attraction to the origin. The constant \(K\) is orbit dependent and is not expressed in closed form. The asymptotic error \(o(1)\) is for each fixed \(n>0\), not uniform as \(n\downarrow0\).

## References

1. D. Constantinescu, *On the Bifurcations of a 3D Symmetric Dynamical System*, Symmetry **15** (2023), 923, published 15 April 2023, https://doi.org/10.3390/sym15040923.
2. F. Munteanu, *Jacobi Stability for T-System*, Symmetry **16** (2024), 84, published 9 January 2024, https://doi.org/10.3390/sym16010084.
3. R. A. Van Gorder and S. R. Choudhury, *Analytical Hopf Bifurcation and Stability Analysis of T System*, Communications in Theoretical Physics **55** (2011), 609–616, https://doi.org/10.1088/0253-6102/55/4/17.
4. J. Carr, *Center manifold*, Scholarpedia **1** (2006), 1826, https://doi.org/10.4249/scholarpedia.1826.
