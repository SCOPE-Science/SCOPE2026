# Sharp coordinate-crossing dichotomy for unequal-decay negative-feedback planar flows

## Finding

Consider two distinct forward solutions of the same planar feedback system
\[
\dot x=\kappa_1r_1(z)-\gamma_1x,\qquad
\dot z=\kappa_2r_2(x)-\gamma_2z,
\]
where \(\kappa_i,\gamma_i>0\), the response \(r_1\) is strictly decreasing, \(r_2\) is nondecreasing, both are \(C^1\), and \(0\le-r_1'\le M_1\), \(0\le r_2'\le M_2\) on the forward-invariant state domain. Put \(A=\kappa_1M_1>0\), \(B=\kappa_2M_2>0\), \(\Omega=\sqrt{AB}\), and \(\delta=(\gamma_1-\gamma_2)/2\). Equality times are \(t\ge0\) at which the two solutions have equal first coordinates.

If \(|\delta|<\Omega\), any two *consecutive* equality times are separated by at least
\[
T_{\mathrm{min}}=\frac{\pi}{\sqrt{AB-(\gamma_1-\gamma_2)^2/4}}.
\]
For every specified positive \(A,B,\gamma_1,\gamma_2\) in this regime, that bound is attained by bounded, strictly monotone \(C^1\) responses of the stated class and two distinct nonnegative solutions. If \(|\delta|\ge\Omega\), any two distinct solutions have **at most one** equality time: after one first-coordinate crossing they cannot cross again. The conclusion allows the secant slopes to vary arbitrarily with the two trajectories; neither equilibrium linearization nor periodicity is assumed.

## Assumptions and scope

Solutions remain in an interval domain where the stated derivative bounds and strict monotonicity apply. In the gene-regulatory realization the domain can be \([0,\infty)^2\) and responses take values strictly between zero and one. All solutions are classical forward solutions and unique by \(C^1\) regularity. The result is about first-coordinate coincidences of **two** trajectories, not crossings of their individual state coordinate through a specified constant. Strict monotonicity of the inhibitory response is needed to make a coincidence a transverse zero; non-strict inhibition may give identical first outputs for an interval.

## Proof

**Secant reduction.** Let \((x^{(1)},z^{(1)})\) and \((x^{(2)},z^{(2)})\) be distinct solutions and write \(u=x^{(1)}-x^{(2)}\), \(v=z^{(1)}-z^{(2)}\). By the fundamental theorem of calculus their difference satisfies
\[
\dot u=-\gamma_1u-a(t)v,\qquad
\dot v=b(t)u-\gamma_2v,
\]
where \(0\le a(t)\le A\) and \(0\le b(t)\le B\). Whenever \(u(t)=0\), uniqueness gives \(v(t)\ne0\), and strict decrease of \(r_1\) gives \(a(t)>0\). Thus every zero of \(u\) is simple: \(\dot u=-a(t)v\ne0\).

**Angular majorant.** Put \(\bar\gamma=(\gamma_1+\gamma_2)/2\) and
\[
X=\sqrt B\,e^{\bar\gamma t}u,\qquad
Y=\sqrt A\,e^{\bar\gamma t}v.
\]
The transformed system is
\[
\dot X=-\delta X-c(t)Y,\qquad
\dot Y=d(t)X+\delta Y,
\]
with \(0\le c(t)=a(t)\sqrt{B/A}\le\Omega\) and \(0\le d(t)=b(t)\sqrt{A/B}\le\Omega\). The difference vector never vanishes, so its polar angle \(\theta\) has a continuous real lift and satisfies exactly
\[
\dot\theta=d(t)\cos^2\theta+c(t)\sin^2\theta+\delta\sin(2\theta)
\le f(\theta):=\Omega+\delta\sin(2\theta).
\]
At a coincidence \(X=0\), one has \(\dot\theta=c(t)>0\). Hence a following coincidence, if any, requires an upward angular advance of exactly \(\pi\) (a reverse passage through a vertical ray is forbidden by transversality).

**Underdamped case.** For \(|\delta|<\Omega\), \(f\) is everywhere positive. Set \(F(\theta)=\int_{\theta_0}^{\theta}ds/f(s)\), where \(\theta_0\) is the angular value at one equality time. Since \((F\circ\theta)'\le1\), any next equality at angular value \(\theta_0+\pi\) requires duration at least
\[
\int_{\theta_0}^{\theta_0+\pi}\frac{ds}{\Omega+\delta\sin(2s)}
=\frac\pi{\sqrt{\Omega^2-\delta^2}}.
\]
The integral follows, for example, from the tangent substitution over a full period of the sine function.

**Overdamped case.** For \(|\delta|\ge\Omega\), the scalar comparison field \(f(\theta)\) has an equilibrium between any vertical starting angle \(\theta_0\) and \(\theta_0+\pi\). The solution of \(\dot\phi=f(\phi)\), \(\phi(0)=\theta_0\), cannot pass that equilibrium. The scalar comparison principle and \(\dot\theta\le f(\theta)\) give \(\theta(t)\le\phi(t)\), so the angle cannot reach the next vertical ray. No second coincidence exists.

**Attainment.** Choose arbitrary positive \(A,B,\gamma_i\) with \(|\delta|<\Omega\) and set \(\kappa_i=\gamma_i\). Define \(m_1=A/\gamma_1\), \(m_2=B/\gamma_2\). For sufficiently small \(h>0\), construct a bounded strictly increasing \(C^1\) function \(G_m\) equal to \(1/2+m(s-1/2)\) when \(|s-1/2|\le h\), with exponential tails tending to \(1/2\pm2mh\) and derivative at most \(m\). Explicitly, for \(s_0=1/2\), let
\[
G_m(s)=\begin{cases}
1/2-2mh+mh\exp((s-s_0+h)/h),&s<s_0-h,\\
1/2+m(s-s_0),&|s-s_0|\le h,\\
1/2+2mh-mh\exp(-(s-s_0-h)/h),&s>s_0+h.
\end{cases}
\]
Take \(r_1=1-G_{m_1}\), \(r_2=G_{m_2}\). They take values in \((0,1)\) if \(2h\max(m_1,m_2)<1/2\), attain the stated slope bounds, and have the equilibrium \((1/2,1/2)\). All sufficiently close trajectories stay in their affine core because the constant linearization has eigenvalues \(-\bar\gamma\pm i\sqrt{\Omega^2-\delta^2}\) with \(\bar\gamma>0\). Comparing the equilibrium with a trajectory started at \((1/2,1/2+\varepsilon)\), the first-coordinate difference is exactly
\[
-\varepsilon\,\frac{A}{\sqrt{\Omega^2-\delta^2}}e^{-\bar\gamma t}\sin\bigl(t\sqrt{\Omega^2-\delta^2}\bigr),
\]
whose first positive zero is precisely \(T_{\mathrm{min}}\). This proves the universal constant is sharp within bounded nonlinear response functions, not merely in an unbounded linear model.

## Verification

The standalone `verify.py` checks the constant-coefficient first-coordinate formula in underdamped, critical and overdamped cases; independently quadratures the half-turn angular integral; and integrates randomly modulated admissible angular equations to test the stated comparison. Execution: `python3 verify.py`. Successful output: `PASS: 72108 independent analytic, quadrature and variable-slope angle tests.` These finite tests are not the proof of the universal infinite-time assertions, which follow from the angular comparison argument above.

## Relationship to prior work

Belgacem, *Luenberger observers for two-gene regulatory networks with sigmoidal regulation: explicit observability conditioning, polytopic convergence certificates, and a logistic–Hill comparison* (arXiv:2611.17232v1), studies recovery from a measurement and its instantaneous derivative, along with observers for general unequal degradation rates. Its Theorem 1 does not furnish a derivative-free two-time observation threshold or a first-coordinate crossing classification. The equal-degradation instance of the crossing bound, \(\pi/\sqrt{AB}\), was already available; the present statement gives the genuinely different unequal-degradation transition, including total absence of repeat crossings when \(|\gamma_1-\gamma_2|\ge2\sqrt{AB}\). Classical linear oscillator calculations provide the extremizing example, while the result for all nonlinear monotone responses rests on the secant reduction and pointwise angular majorant. Existing general sampled-observability and Sturm-comparison theory is relevant background; the claim is the *sharp uniform formula and dichotomy for this feedback class*, not invention of those methods.

## Limitations

The common-state measured coordinate is continuous in time but comparisons use only its values at two instants; this does not construct a stable noise-tolerant state estimator. No uniform noise-conditioning bound follows from upper slope constraints alone: flat inhibitory response segments can make inverse recovery arbitrarily ill-conditioned. The equal-sign feedback class is excluded, as are unknown parameters, delays, noisy trajectories and higher-dimensional models. The sharpness construction uses a locally affine \(C^1\) sigmoid; it does not assert exact attainment for each fixed logistic or Hill response.

## References

1. I. Belgacem, *Luenberger observers for two-gene regulatory networks with sigmoidal regulation*, arXiv:2611.17232v1, first publicly posted 12 November 2026, https://arxiv.org/html/2611.17232v1.
2. G. Guo, *Systems with nonequidistant sampling: controllable? observable? stable?*, Asian Journal of Control 7 (2005), 455–461, https://doi.org/10.1111/j.1934-6093.2005.tb00409.x.
3. M. N. Chatzis, K. Maes and G. Lombaert, *Observability of nonlinear discrete-time systems with unmeasured inputs*, Mechanical Systems and Signal Processing 238 (2025), 113142, https://doi.org/10.1016/j.ymssp.2025.113142.
