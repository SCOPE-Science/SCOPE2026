# A two-sided passage-time crossover at the degenerate invasion boundary of an Allee–fear competition flow

## Finding
Consider the dimensionless positive-population competition system of Chen, Chen, Srivastava and Parshad [1],
\[
\dot x=x\left[\frac{(1-x)(x-p)}{1+qy}-ay\right],\qquad
\dot y=by(1-y-cx).
\]
Fix \(0<a<1\), \(b>0\), \(q>0\), set \(p=1-a\), and vary \(c=1+\delta\). Put
\[
\gamma=\frac{1+aq}{a},\qquad Y_{\rm crit}=\gamma^{-1/2},\qquad E=(1,0).
\]
The boundary equilibrium \(E\) is a hyperbolic sink for \(\delta>0\), a saddle for \(\delta<0\), and nonhyperbolic at zero. For all sufficiently small \(\delta>0\), a nearby **positive saddle** has the expansions
\[
\begin{split}
 x_*(\delta)&=1-\gamma^{-1/2}\sqrt\delta-\frac{a(2q-1)}{2(1+aq)}\delta+O(\delta^{3/2}),\\
 y_*(\delta)&=\gamma^{-1/2}\sqrt\delta-\frac{a+2}{2(1+aq)}\delta+O(\delta^{3/2}).
\end{split}
\]
Its two real eigenvalues are \(-a+O(\sqrt\delta)\) and \(2b\delta+O(\delta^{3/2})\).

There exists a sufficiently small fixed \(\eta>0\), depending only on \(a,b,q\), for which the following **complete two-sided critical passage experiment** holds. For \(\varepsilon>0\), initialize
\[
 (x(0),y(0))=(1-Y_0\sqrt\varepsilon,Y_0\sqrt\varepsilon),\qquad Y_0>0,
\]
with \(\varepsilon\) small enough that the initial state is positive. Define \(t_\eta\) to be the first time the positive \(y\)-coordinate equals \(\eta\), or \(+\infty\) if it never does.

If \(c=1-\varepsilon\), every \(Y_0>0\) gives finite passage for sufficiently small \(\varepsilon\), with
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon t_\eta
 =\frac1{2b}\log\left(1+\frac1{\gamma Y_0^2}\right).}
\]
If \(c=1+\varepsilon\) and \(Y_0>Y_{\rm crit}\), passage is again finite, with
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon t_\eta
 =\frac1{2b}\log\left(\frac{\gamma Y_0^2}{\gamma Y_0^2-1}\right).}
\]
If \(c=1+\varepsilon\) and \(0<Y_0<Y_{\rm crit}\), then \(t_\eta=+\infty\) for all sufficiently small \(\varepsilon\), and the trajectory tends to \(E\). No assertion is made for the boundary-layer initial amplitude \(Y_0=Y_{\rm crit}\).

At the exactly degenerate boundary \(c=1\), start instead at \((x(0),y(0))=(1-y_0,y_0)\) and let \(y_0\downarrow0\). The same fixed \(\eta\) satisfies
\[
\boxed{\lim_{y_0\downarrow0} y_0^2 t_\eta=\frac1{2b\gamma}.}
\]
The critical bottleneck therefore has a cubic rather than quadratic local drift, and the sign of the transverse detuning changes its limiting passage profile and the existence of a local extinction basin.

## Assumptions and scope
All statements concern the smooth deterministic two-dimensional ODE, with fixed \(0<a<1\), \(b,q>0\), and the exact algebraic degeneracy \(p=1-a\). The positive quadrant is forward invariant and the model's trajectories are bounded [1]. The passage surface \(y=\eta\) is chosen once, sufficiently near \(E\), then kept fixed as \(\varepsilon\) and \(y_0\) decrease. Statements about the positive saddle and boundary basin are local. The threshold comparison uses fixed \(Y_0\) **strictly** on either side of \(Y_{\rm crit}\), not amplitudes depending on \(\varepsilon\) that approach it. No global basin census is claimed.

## Proof
**1. Exact fast–slow coordinates.** Put \(s=1-x\), \(z=s-y\). Then, with \(\delta=c-1\), the exact equations are
\[
\dot s=(1-s)\left[ay-\frac{s(a-s)}{1+qy}\right],\qquad
\dot y=by\left[z-\delta+\delta(y+z)\right],\qquad \dot z=\dot s-\dot y.
\]
At \((z,y,\delta)=(0,0,0)\) the fast eigenvalue is \(-a\) and the center eigenvalue is zero. Treating \(\delta\) as a fixed parameter with \(\dot\delta=0\), the smooth parameter-dependent center manifold has the graph
\[
 z=h(y,\delta)=\gamma y^2+\frac ba\delta y+O\big((|y|+|\delta|)^3\big).
\]
There is no pure \(\delta\)-only term since \((z,y)=(0,0)\) is an equilibrium for every parameter. To verify the coefficients, the degree-two part of the fast equation is \(\dot z=-az+(1+aq)y^2+b\delta y+O_3\), while the center-manifold invariance derivative is of total degree at least three. Substitution gives the asserted \(h\). The induced scalar center flow is
\[
\dot y=by(\gamma y^2-\delta)+O(y^4+|\delta|y^2+\delta^2 y).
\]
The strong-stable foliation supplies exponentially decaying transverse errors, uniformly for \(|\delta|\) small while the orbit stays in a fixed neighborhood. Consequently initial points on \(z=0\), which differ from the center graph by \(O(y_0^2+|\delta|y_0)\), have the same leading slow-time limit: the fast adjustment takes negligible rescaled time and displaces \(y\) by lower order.

**2. Nearby saddle.** Equilibria with \(y>0\) obey \(y=1-(1+\delta)x\), and the other nullcline is
\[
(1-x)(x-1+a)-ay(1+qy)=0.
\]
This is the quadratic \(A_1x^2+A_2x+A_3=0\) of [1], with \(A_1=1+aq(1+\delta)^2\), \(A_2=-[2aq(1+\delta)+a(1+\delta)+2-a]\), and \(A_3=1+aq\). At \(\delta=0\) it has a double root \(x=1\); its nearby small positive root has the displayed Puiseux expansion (substitution determines the coefficients). Positivity selects \(\delta>0\). Along \(y=1-cx\), the determinant is \(-bxy\,\partial_x f(x,1-cx)\), where \(f=\frac{(1-x)(x-p)}{1+qy}-ay\). The quadratic expansion yields \(\det J=-2ab\delta+O(\delta^{3/2})\), and \(\operatorname{tr}J=-a+O(\sqrt\delta)\). The eigenvalues follow; the sign of the determinant gives a saddle. At \(E\), the Jacobian is triangular with eigenvalues \(-a,-b\delta\).

**3. Rescaled flow and critical amplitudes.** Put \(\delta=\sigma\varepsilon\) for \(\sigma\in\{-1,+1\}\), \(y=\sqrt\varepsilon Y\), and \(\tau=\varepsilon t\). Along the attracting center graph, and equally for the prescribed nearby initial states after their fast layer, solutions converge uniformly on every compact slow-time interval before a possible blow-up to
\[
 \frac{dY}{d\tau}=bY(\gamma Y^2-\sigma),\qquad Y(0)=Y_0.
\]
For \(\sigma=-1\), the positive solution increases to infinity in finite slow time. For \(\sigma=+1\), it decreases to zero when \(Y_0<\gamma^{-1/2}\) and increases to infinity when \(Y_0>\gamma^{-1/2}\). The scalar sign persists for the full flow in a sufficiently small neighborhood by the center-manifold estimate, and the small-amplitude basin on the stable side converges to \(E\).

**4. Fixed-height first passage.** For any large fixed \(K>Y_0\) that lies above the separatrix, the first hitting time of \(y=K\sqrt\varepsilon\) converges after multiplication by \(\varepsilon\) to the corresponding hitting time of \(Y=K\) in the limiting scalar equation. Choose \(\eta\) sufficiently small. The center expansion and fast-fiber control give, uniformly in sufficiently small \(\varepsilon\), a positive cubic lower bound \(\dot y\ge (b\gamma/2)y^3\) once \(y\in[K\sqrt\varepsilon,\eta]\) and \(K\) is large, apart from an exponentially small initial layer already passed. Thus the remaining scaled time is bounded by a constant times \(K^{-2}\), independently of \(\varepsilon\). Sending first \(\varepsilon\to0\), then \(K\to\infty\), proves the limits by the exact integrals
\[
\begin{aligned}
 \int_{Y_0}^{\infty}\frac{dY}{bY(\gamma Y^2+1)}&=\frac1{2b}\log\left(1+\frac1{\gamma Y_0^2}\right),\\
 \int_{Y_0}^{\infty}\frac{dY}{bY(\gamma Y^2-1)}&=\frac1{2b}\log\left(\frac{\gamma Y_0^2}{\gamma Y_0^2-1}\right),\quad Y_0>\gamma^{-1/2}.
\end{aligned}
\]
For \(\delta=0\), the identical comparison and \(\dot y=b\gamma y^3(1+O(y))\) on the center graph give \(t_\eta=(2b\gamma y_0^2)^{-1}(1+o(1))\). The initial fast layer contributes \(o(y_0^{-2})\).

## Verification
The accompanying standalone `verify.py` (Python 3 and SymPy) checks the center-graph coefficients to quadratic order, the cubic reduced-flow coefficient, the exact equilibrium quadratic, the two Puiseux coefficients, the Jacobian eigenvalue leading terms, and the critical sign of \(\gamma\). Run `python verify.py`. The checker returns `VERIFY_OK`. Finite trajectory calculations at three positive parameter combinations independently corroborate the limiting constants, but no finite run proves an infinite-time or singular-limit statement; those depend on the analytical estimates above.

## Relationship to prior work
Chen et al. [1], Theorems 3.1, 4.1 and 5.1, provide the equilibrium quadratic, classify the nonhyperbolic saddle when \(c=1,p=1-a\), and show the ordinary transcritical case only for \(p\ne1-a\). Those qualitative facts are prior work, not new claims. The present contribution is the **quantified two-sided \(\sqrt{|c-1|}\) invasion threshold and exact, fixed-section passage laws of the nonlinear two-species flow** at the excluded degenerate case, including the saddle's small positive eigenvalue. Corral [2] supplies general finite-time scaling for scalar pitchfork and other bifurcation normal forms; the scalar normal-form mechanism and its universal exponent are therefore explicitly credited. That one-dimensional theory does not by itself compute this model's parameter-dependent center coefficient, identify which positive two-species initial states pass a fixed ecological threshold, or prove the full two-dimensional fast-fiber-to-fixed-section limit. An indexed 2026 result [3] considers a **different** rational fear-modified competition system, establishes a cubic boundary normal form and a separate coexistence fold, and does not imply these Allee-model passage formulas. Generic saddle-node–transcritical normal-form theory is also precedent; novelty is restricted to the stated concrete full-system threshold and constants.

## Limitations
Only local initial states, local saddle structure and near-boundary passage are established. The theorem does not classify arbitrary positive initial states or the equality-layer \(Y_0=\gamma^{-1/2}\), nor does it concern spatial diffusion, environmental noise or parameter drift. The law is for a fixed small \(\eta\), and does not claim threshold independence of unscaled finite-time corrections. Some asymptotic exponents follow from known generic normal-form scaling; publication priority for the full application is not independently certified. Independent audit has not been performed.

## References
[1] S. Chen, F. Chen, V. Srivastava, R. D. Parshad, *Dynamical Analysis of a Lotka-Volterra Competition Model with both Allee and Fear Effect*, arXiv:2303.04919 (first public 2023-03-08), https://arxiv.org/html/2303.04919v1 .

[2] A. Corral, *Universal finite-time scaling in the transcritical, saddle-node, and pitchfork discrete and continuous bifurcations*, arXiv:2405.19947 (first public 2024-05-30), https://arxiv.org/abs/2405.19947 .

[3] *Exact fear-induced coexistence wedge and cubic boundary bottleneck*, published-finding corpus indexed result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fear-induced-coexistence-wedge-and-cubic-boundary-bottlene--8245e3bf11a0 (different fear-competition equations).
