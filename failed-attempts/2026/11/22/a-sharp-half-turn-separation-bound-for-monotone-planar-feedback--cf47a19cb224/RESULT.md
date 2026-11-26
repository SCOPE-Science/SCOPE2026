# A sharp half-turn separation bound for monotone planar feedback trajectories

## Finding

Let \(\kappa_1,\kappa_2,\gamma>0\) and let \(r_1,r_2\in C^1(\mathbb R)\) be bounded, strictly decreasing and strictly increasing, respectively, with
\[
0\le -r_1'(z)\le M_1,\qquad 0\le r_2'(x)\le M_2,
\]
where \(M_1,M_2\in(0,\infty)\). Set \(A=\kappa_1M_1\), \(B=\kappa_2M_2\), and \(T_*=\pi/\sqrt{AB}\). Consider the autonomous system
\[
\dot x=\kappa_1r_1(z)-\gamma x,\qquad
\dot z=\kappa_2r_2(x)-\gamma z.
\]
For any two distinct solutions and any two consecutive times \(t_0<t_1\) at which their first coordinates agree, one has
\[
\boxed{t_1-t_0\ge T_*.}
\]
More precisely, if \(x(t_0)=\widetilde x(t_0)\) and \(z(t_0)>\widetilde z(t_0)\), then \(x(t)<\widetilde x(t)\) for every \(t_0<t<t_0+T_*\). Reversing the initial second-coordinate inequality reverses this conclusion. The bound is sharp even among the logistic feedback functions below: distinct logistic trajectories have first-coordinate return times tending to \(T_*\).

An exact endpoint phenomenon also occurs within bounded, strictly monotone \(C^1\) feedback: there are feedback functions with \(A=B=1\) for which a one-parameter family of distinct trajectories has the same first-coordinate observations at **every** integer multiple of \(T_*=\pi\), despite the trajectories being distinct between observation times. Thus a sample at zero and at any \(0<h<T_*\) distinguishes every pair of initial states, whereas equality at the sharp endpoint can destroy even infinite regularly spaced observations.

## Assumptions and scope

The statement concerns two-dimensional autonomous negative-feedback differential equations with a common degradation rate \(\gamma\), finite global slope bounds, strictly monotone regulations, and classical forward solutions. Bounded regulations make the vector field globally Lipschitz and ensure all solutions exist for all positive time. For biological concentrations one may additionally assume \(r_i(\mathbb R)\subset(0,1)\), as in the explicit examples; the nonnegative quadrant is then forward invariant. Strict monotonicity is essential to give a definite sign immediately after equality of the measured coordinate. The slope constants can be any valid upper bounds; optimality concerns taking their actual suprema.

## Proof

**Half-turn comparison.** Translate time so \(t_0=0\). For distinct solutions write \(u=x-\widetilde x\), \(v=z-\widetilde z\). The secant-slope identity, including continuous interpretation when one difference vanishes, gives
\[
\dot u=-\gamma u-a(t)v,\qquad
\dot v=b(t)u-\gamma v,
\]
with \(0\le a(t)\le A\), \(0\le b(t)\le B\). If \(v\ne0\), strict monotonicity of \(r_1\) implies \(a(t)>0\). Uniqueness guarantees \((u,v)\ne(0,0)\) at every time for distinct solutions.

Introduce positive-rescaled variables \(U=\sqrt B\,e^{\gamma t}u\), \(V=\sqrt A\,e^{\gamma t}v\), which satisfy
\[
\dot U=-a(t)\sqrt{B/A}\,V,\qquad
\dot V=b(t)\sqrt{A/B}\,U.
\]
For any continuous lifting \(\theta(t)\) of the polar angle of \((U,V)\),
\[
\dot\theta(t)=
\frac{b(t)\sqrt{A/B}\,U^2+a(t)\sqrt{B/A}\,V^2}{U^2+V^2},
\qquad 0\le\dot\theta(t)\le\sqrt{AB}.
\]
If \(u(0)=0\) and \(v(0)>0\), initially \(\theta(0)=\pi/2\) and \(\dot U(0)=-a(0)\sqrt{B/A}V(0)<0\). Thus \(U<0\) immediately. It cannot return to zero before the angle advances from \(\pi/2\) to \(3\pi/2\), which requires at least \(\pi/\sqrt{AB}\) time. This proves the sign assertion and the gap between all consecutive zeros by time translation. The case \(v(0)<0\) is symmetric.

**Sharpness within the logistic family.** Take \(\kappa_1=\kappa_2=1\), \(\gamma=1/10\),
\[
f(s)=(1+e^{-(s-5)})^{-1},\qquad r_1(s)=1-f(s),\quad r_2(s)=f(s).
\]
Here \(A=B=1/4\), so \(T_*=4\pi\), and \((x,z)=(5,5)\) is an equilibrium. The Jacobian there is
\[
J=\begin{pmatrix}-1/10&-1/4\\1/4&-1/10\end{pmatrix}.
\]
Consider solutions starting from \((5,5+\varepsilon)\) and \((5,5-\varepsilon)\). Smooth dependence on initial conditions gives, uniformly with one time derivative on bounded intervals,
\[
\frac{x_{+}(t)-x_{-}(t)}{2\varepsilon}
\longrightarrow -e^{-t/10}\sin(t/4)
\quad\text{as }\varepsilon\downarrow0.
\]
The limiting first-coordinate difference has a simple zero at \(4\pi\) and changes sign there. The intermediate value theorem and uniform convergence give a zero \(T_\varepsilon\to4\pi\). The half-turn bound excludes any earlier positive zero below \(4\pi\), establishing the optimality of the constant within a smooth, bounded sigmoid family.

**Permanent endpoint aliasing with bounded regulation.** Fix \(d=e=1/10\) and define the bounded, strictly increasing \(C^1\) function
\[
s(w)=\begin{cases}
w,&|w|\le d,\\
\operatorname{sgn}(w)\bigl[d+e(1-\exp(-( |w|-d)/e))\bigr],&|w|>d.
\end{cases}
\]
Its derivative is positive everywhere, equals \(1\) for \(|w|\le d\), and never exceeds \(1\). Put \(\kappa_1=\kappa_2=1\), \(\gamma=1/10\), \(r_1(q)=1/2-s(q-5)\), and \(r_2(q)=1/2+s(q-5)\). Both regulations lie strictly between \(0.3\) and \(0.7\); they satisfy the assumptions with \(A=B=1\) and \(T_*=\pi\).

For every \(|\xi|<1/10\), the solution from \((5,5+\xi)\) is exactly
\[
x(t)=5-\xi e^{-t/10}\sin t,\qquad
z(t)=5+\xi e^{-t/10}\cos t.
\]
Indeed its displacement in either coordinate stays below \(|\xi|<d\), so it stays in the central affine strip where the differential equation has constant cross-couplings \(-1,+1\). At every \(k\in\mathbb Z_{\ge0}\), \(x(k\pi)=5\), independently of \(\xi\). This proves that the half-turn boundary can coincide with exact loss of all information in a regular sampled first-coordinate record, even though all these trajectories converge to the same equilibrium and are pairwise distinct at every finite time.

## Verification

The accompanying `CHECK.py` uses only the Python standard library. It verifies the analytic central-strip identities across four initial amplitudes and ten sampling indices and numerically stress-tests the smooth logistic example for four perturbation sizes and four precritical times. Numerically computed return times for \(\varepsilon=0.2,0.05,0.01,0.002\) approach \(4\pi\), with approximate values \(12.577984,12.567098,12.566400,12.566372\). These tests illustrate the statement; the all-time and all-initial-data conclusions follow from the polar-angle proof, not from finite simulations.

Reproduce by running `python CHECK.py` in the folder containing this document and the checker. It reports a final `PASS` only after completing the indicated tests.

## Relationship to prior work

Belgacem (2026) analyzes the two-gene negative-feedback model, proving continuous-time reconstruction from \((x,\dot x)\) and observer convergence using regulation slope bounds. The sampled first-coordinate separation bound, its optimality within logistic regulation, and the endpoint construction above are not stated in the inspected model analysis. Classical sampled-observability theory, including Ammar--Vivalda (2004) and Ammar--Massaoud--Vivalda (2016), addresses preservation of observability in broader settings. The result here concerns a structural *sharp* half-turn lower bound for the first zero of a two-trajectory difference, with a nonlinear bounded-feedback realization of a complete sample alias. It is not a claim that half-period aliasing for a linear harmonic oscillator is novel. Full-text comparisons for those two older sampled-observability studies were not available, so exact historical priority remains qualified.

## Limitations

The common-decay hypothesis is necessary for this precise angular-speed proof; no threshold is asserted for unequal degradation rates. Finite global slope bounds are required: unshifted Hill responses with exponent below one can have unbounded slope at the basal boundary. For some fixed nonlinear response functions the actual first-return gap can exceed the universal bound. A locally singular delay-observation map need not imply exact global noninjectivity, so the proof establishes actual noninjectivity at the endpoint only for the explicitly constructed plateau family. Numerical examples are not exhaustive certificates and no independent mathematical review has been performed.

## References

1. I. Belgacem, *Luenberger observers for two-gene regulatory networks with sigmoidal regulation: explicit observability conditioning, polytopic convergence certificates, and a logistic--Hill comparison*, arXiv:2611.17232v1, first posted 2026-11-12. https://arxiv.org/html/2611.17232v1
2. S. Ammar and J.-C. Vivalda, *On the preservation of observability under sampling*, Systems & Control Letters 52 (2004), 7--15. https://doi.org/10.1016/j.sysconle.2003.08.008
3. S. Ammar, M. Massaoud, and J.-C. Vivalda, *Observability Under Sampling for Nonlinear Systems*, Asian Journal of Control 18 (2016), 1269--1278. https://doi.org/10.1002/asjc.1284
4. S. Ammar, J.-C. Vivalda, and B. Zitouni, *Strong Differential Observability for Sampled-Time Systems*, SIAM J. Control Optim. 58 (2020), 3814--3841. https://doi.org/10.1137/19M1302867
