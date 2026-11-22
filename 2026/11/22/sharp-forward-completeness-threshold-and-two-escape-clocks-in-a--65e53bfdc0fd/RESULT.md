# Sharp forward-completeness threshold and two escape clocks in a cubic jerk flow

## Finding
Consider the real polynomial jerk flow
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-x-y-z-\alpha z^2+xy-\beta+\gamma z^3,
\]
with fixed \(\alpha>0\), \(\beta\in\mathbb R\), and \(\gamma\in\mathbb R\). The following is a sharp classification **of forward completeness of the vector field**, not a classification of all individual trajectories.

**Theorem.** All real initial conditions generate solutions for every forward time if and only if \(\gamma<0\). At the complementary parameters there are open sets of finite-time escaping initial conditions, with distinct universal asymptotic clocks:

* For each \(\gamma>0\), each \(K>0\), and each sign \(\sigma\in\{-1,1\}\), there exists \(M>0\) such that every initial state satisfying \(|x(0)|<K\), \(|y(0)|<K\), and \(\sigma z(0)>M\) has a finite maximal forward time \(T\). Its first two coordinates have finite limits \(x_*\) and \(y_*\). As \(\tau=T-t\downarrow0\),
  \[
  z(t)=\frac{\sigma}{\sqrt{2\gamma\tau}}+\frac{\alpha}{3\gamma}+O(\sqrt\tau),\qquad
  y(t)=y_*-\sigma\sqrt{\frac2\gamma}\sqrt\tau-\frac{\alpha}{3\gamma}\tau+O(\tau^{3/2}),
  \]
  and \(x(t)=x_*-y_*\tau+O(\tau^{3/2})\).
* For \(\gamma=0\), each \(K>0\) admits an \(M>0\) such that every initial state with \(|x(0)|<K\), \(|y(0)|<K\), and \(z(0)<-M\) has a finite maximal forward time \(T\). There are finite constants \(x_*\) and \(C\), depending on the initial condition, such that
  \[
  z(t)=-\frac{1}{\alpha\tau}-\frac1{2\alpha}+O\!\bigl(\tau\lvert\log\tau\rvert\bigr),
  \qquad y(t)=\frac1\alpha\log\tau+C+o(1),
  \]
  and \(x(t)=x_*-(\tau/\alpha)\log\tau+O(\tau)\). Thus the velocity diverges logarithmically on the quadratic side but converges on both cubic escape sides.

All asymptotic constants implicit in the \(O\)-terms may depend on the fixed parameters and initial state. The theorem makes no assertion that every solution at \(\gamma\ge0\) escapes; the equilibrium solution exists for all time for every \(\gamma\).

## Assumptions and scope
The phase space is \(\mathbb R^3\). Solutions are unique on their maximal interval by polynomial local Lipschitz continuity. “Forward complete” means every maximal solution exists for all \(t\ge0\). The sign of \(\alpha\) is held strictly positive to make the critical, quadratic-curvature boundary an escape problem. The forcing \(\beta\) is arbitrary and plays no part in the leading escape constants. All conclusions concern the exact continuous-time system, without numerical time-stepping or a compact phase-space restriction.

## Proof
**1. Global forward existence for \(\gamma<0\).** Fix any initial state and any finite horizon \(H>0\). Assume temporarily that a trajectory is defined until a time \(t\le H\) and \(|z(s)|\le R\) for \(0\le s\le t\). Integration of \(\dot y=z\) and \(\dot x=y\) gives
\[
|y(s)|\le |y(0)|+HR,\quad
|x(s)|\le |x(0)|+H|y(0)|+\tfrac12 H^2R.
\]
Hence, with constants depending only on \(H\) and the initial state, the magnitude of \(xy-x-y-\beta\) is bounded by \(C_H(1+R)^2\). At a first outward crossing of \(z=R\), its derivative satisfies
\[
\dot z\le-|\gamma|R^3-\alpha R^2-R+C_H(1+R)^2<0
\]
for all sufficiently large \(R\). At a first outward crossing of \(z=-R\),
\[
\dot z\ge|\gamma|R^3-\alpha R^2+R-C_H(1+R)^2>0.
\]
Both crossings are impossible. Therefore \(z\), and then \(x,y\), remain bounded on every finite horizon \(H\). The standard continuation criterion for locally Lipschitz ODEs gives existence for all forward time. This argument does not claim the existence of a uniform absorbing ball as \(H\to\infty\).

**2. Cubic escapes for \(\gamma>0\).** Fix \(K>0\) and \(\sigma\in\{-1,1\}\), put \(w=\sigma z\), and consider the region \(w\ge M\), \(|x|,|y|\le K+1\). In this region
\[
\dot w=\gamma w^3-\sigma\alpha w^2-w+\sigma(xy-x-y-\beta).
\]
Choosing \(M\) sufficiently large (uniformly over \(|x(0)|,|y(0)|<K\)) ensures \(\dot w\ge(\gamma/2)w^3>0\). While this remains true,
\[
\bigl|y(t)-y(0)\bigr|\le\int_M^\infty\frac{2u}{\gamma u^3}\,du=\frac2{\gamma M},
\quad
0\le t\le\int_M^\infty\frac{2}{\gamma u^3}\,du=\frac1{\gamma M^2}.
\]
Taking \(M\) larger if necessary, these bounds and \(\dot x=y\) prevent \(x,y\) from reaching the edges \(|x|=K+1\) or \(|y|=K+1\). A first-exit bootstrap therefore keeps the entire region invariant until \(w\to\infty\) at some finite \(T\le1/(\gamma M^2)\). The same estimates show \(x(t)\to x_*\) and \(y(t)\to y_*\), both finite.

With \(x,y\) convergent, the curvature equation has the refined form
\[
\dot w=\gamma w^3-\sigma\alpha w^2-w+O(1).
\]
As \(w\) is strictly increasing, we may use it as the independent variable. Integrating \(dt/dw\) from \(w\) to infinity yields
\[
\tau=\frac{1}{2\gamma w^2}+\frac{\sigma\alpha}{3\gamma^2w^3}+O(w^{-4}).
\]
Elementary inversion gives \(w=(2\gamma\tau)^{-1/2}+\sigma\alpha/(3\gamma)+O(\sqrt\tau)\), and hence the asserted expansion for \(z=\sigma w\). Integrating \(\dot y=z\) and then \(\dot x=y\) up to \(T\) proves the remaining expansions.

**3. Critical quadratic escape at \(\gamma=0\).** Put \(w=-z\). Then
\[
\dot w=\alpha w^2-w+x+(1-x)y+\beta,\qquad
\dot y=-w,\qquad \dot x=y.
\]
Fix \(K>0\) and choose \(M\) so large that \(\alpha w^2/2\le\dot w\le3\alpha w^2/2\) whenever
\[
w\ge M,\qquad |x|\le K+1,\qquad
|y|\le K+\frac2\alpha\log\frac wM.
\]
Such an \(M\) exists, because the nonquadratic terms are at most \(O_K(w+\log(w/M)+1)\) uniformly in this region, and these are \(o(w^2)\). In the region, the change of independent variable to \(w\) gives
\[
\left|\frac{dy}{dw}\right|\le\frac2{\alpha w},\qquad
\left|\frac{dx}{dw}\right|\le\frac{2}{\alpha w^2}
 \left(K+\frac2\alpha\log\frac wM\right).
\]
The first estimate propagates the claimed logarithmic bound on \(y\), and integration of the second over \([M,\infty)\) is at most \((2/\alpha M)(K+2/\alpha)\). Making this smaller than one closes the bootstrap on \(x\). Therefore \(w\uparrow\infty\) in a finite time \(T\le2/(\alpha M)\), while \(x\) converges to a finite limit and \(y=O(\log w)\).

The stronger identity
\[
\dot w=\alpha w^2-w+O(\log w)
\]
now implies
\[
\tau=\int_w^\infty\frac{du}{\alpha u^2-u+O(\log u)}
=\frac1{\alpha w}+\frac1{2\alpha^2w^2}
  +O\!\left(\frac{\log w}{w^3}\right).
\]
Inverting gives \(w=1/(\alpha\tau)+1/(2\alpha)+O(\tau\lvert\log\tau\rvert)\). Moreover,
\[
\frac{dy}{dw}=-\frac{w}{\dot w}=-\frac1{\alpha w}+O(w^{-2}),
\]
so \(y+(1/\alpha)\log w\) tends to a finite constant. Substituting \(w\sim1/(\alpha\tau)\) proves the stated logarithmic velocity and integrating \(\dot x=y\) proves the position expansion.

Parts 1–3 establish the completeness classification and all claimed asymptotics.

## Verification
The standalone `verify.py` checks the exact reciprocal-curvature expansions and formal inverse-series constants with symbolic algebra. It also integrates the equations after changing the independent variable from time to the growing curvature, as a finite diagnostic on both cubic tails and the critical quadratic tail. The checks returned `VERIFY_OK`. Such finite diagnostics are not substitutes for the continuation argument, invariant-region bootstrap, or asymptotic integration proved above.

## Relationship to prior work
Vaidyanathan et al. (2023) introduce this cubic jerk system, identify its equilibrium, and numerically scan its attractors as the parameters—including the cubic coefficient across zero—vary. The inspected source's modeling and bifurcation sections do not provide a global forward-completeness criterion, open finite-time escape regions, or the two distinct escape clocks proved here. Its numerical attractor results concern other initial data and are not contradicted by the existence of remote finite-time escapes.

The quadratic predecessor of Vijayakumar et al. (2021) already displays *unbounded* numerical trajectories at zero cubic feedback. That observation is not new here; the additional critical-side statements are finite **time** of escape and sharp pole, logarithmic velocity, and constant corrections. A published calculation entitled “Explicit Hopf criticality surface for a cubic jerk flow” treats a local bifurcation at zero forcing for the very same ODE; the local first Lyapunov coefficient neither implies nor excludes the global completeness boundary in the cubic coefficient.

## Limitations
This theorem does not classify the basins of bounded attractors or all solutions at \(\gamma\ge0\), nor establish ultimate boundedness at \(\gamma<0\). It treats the real polynomial ODE, and no conclusions about physical circuit voltage limits or numerical integrator stability follow. Hidden equivalent results in poorly indexed literature cannot be ruled out solely by the recorded comparisons; an independent mathematical audit is not claimed.

## References
1. S. Vaidyanathan, A. T. Azar, I. A. Hameed, K. Benkouider, E. Tlelo-Cuautle, B. Ovilla-Martinez, C.-H. Lien and A. Sambas, “Bifurcation Analysis, Synchronization and FPGA Implementation of a New 3-D Jerk System with a Stable Equilibrium,” *Mathematics* **11** (2023), 2623. https://doi.org/10.3390/math11122623. First public publication June 8, 2023.
2. M. D. Vijayakumar, A. Karthikeyan, J. Zivcak, O. Krejcar and H. Namazi, “Dynamical Behavior of a New Chaotic System with One Stable Equilibrium,” *Mathematics* **9** (2021), 3217. https://doi.org/10.3390/math9243217.
3. “Explicit Hopf criticality surface for a cubic jerk flow” (published mathematical note, 2026), a local analysis of the same ODE's equilibrium transition.
