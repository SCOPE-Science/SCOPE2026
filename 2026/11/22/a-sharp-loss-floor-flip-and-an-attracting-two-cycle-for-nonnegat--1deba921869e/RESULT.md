# A sharp loss-floor flip and an attracting two-cycle for nonnegative Gauss--Newton descent

## Finding

The deterministic nonnegative Gauss--Newton (NGN) update, using a fixed base step \(\sigma>0\) and the actual positive objective value rather than its minimum-subtracted value, has a sharp and explicit stability bifurcation even for a scalar strongly convex quadratic. Let
\[
f(x)=c+\frac{\lambda x^2}{2},\qquad c>0,\quad\lambda>0,
\]
and set \(\alpha=\lambda\sigma\). Apply the NGN rule
\[
T(x)=x-\gamma(x)\lambda x,\qquad
\gamma(x)=\frac{\sigma}{1+\sigma\lambda^2x^2/(\lambda x^2+2c)}.
\]

**Sharp classification.** For every \(0<\alpha\le2\), every real starting point converges to the unique minimizer \(0\). When \(0<\alpha<2\), the local linear factor is \(|1-\alpha|\) (at \(\alpha=1\), convergence is locally cubic). At the critical value \(\alpha=2\), every non-terminating orbit satisfies the exact critical asymptotic
\[
\lim_{n\to\infty} n x_n^2=\frac{c}{4\lambda},\qquad
\lim_{n\to\infty}n\bigl(f(x_n)-c\bigr)=\frac{c}{8}.
\]
An orbit that reaches zero at a finite iteration stays there; the displayed positive limits are only for orbits that never reach zero.

For every \(\alpha>2\), the minimizer is locally repelling, and the map has a **unique antipodal nonzero period-two orbit** \(\{-r,r\}\), where
\[
r^2=\frac{2c}{\lambda}\frac{\alpha-2}{\alpha+2}.
\]
This two-cycle is locally attracting, with exact one-step derivative and two-step multiplier
\[
T'(r)=T'(-r)=1-\frac8{\alpha^2},\qquad
\mu_2=\left(1-\frac8{\alpha^2}\right)^2<1.
\]
The effective NGN step at either cycle point is \(\gamma(r)=2/\lambda\), regardless of the larger base parameter. Its perpetual excess loss is exactly
\[
f(r)-\min f=c\frac{\alpha-2}{\alpha+2}\xrightarrow[\alpha\to\infty]{}c.
\]
Consequently, **all-start convergence to the minimizer holds exactly when \(0<\lambda\sigma\le2\)**, despite bounded nonconvergent trajectories for every larger normalized base step. This does not assert that every initial state at a supercritical step converges to the two-cycle, nor that it is the only non-antipodal cycle.

## Assumptions and scope

This is the deterministic, single-component, constant-parameter NGN update of Schaipp--Gower--Taylor [1] and Orvieto--Xiao [2]. The state is scalar and real; \(\sigma,\lambda,c\) are strictly positive; the loss is evaluated with its true strictly positive minimum \(c\), not after subtracting \(c\). No noise, clipping, momentum, projection, preconditioning or line search occurs. Local attraction of the two-cycle means an open neighborhood of either cycle point has iterates converging to that orbit (with the appropriate phase), not that there is a global basin classification. The original NGN scheme is not translation-invariant in the objective value.

## Proof

**1. Exact rational reduction.** Put \(y=\lambda x^2/(2c)\ge0\). Direct algebra gives
\[
\frac{T(x)}x=t_\alpha(y):=\frac{y+1-\alpha}{1+(1+\alpha)y},\quad x\ne0;
\qquad
 y_{n+1}=y_n\,t_\alpha(y_n)^2.
\]
The formula extends continuously to \(x=0\). The denominator is always strictly positive, and \(t_\alpha\) strictly increases with \(y\), because \(t_\alpha'(y)=\alpha^2/[1+(1+\alpha)y]^2>0\). Its endpoint values are \(1-\alpha\) and \(1/(1+\alpha)\).

**2. Exact global subcritical and critical behavior.** The inequalities
\[
1-t_\alpha(y)=\frac{\alpha(1+y)}{1+(1+\alpha)y}>0,
\qquad
1+t_\alpha(y)=\frac{2-\alpha+(2+\alpha)y}{1+(1+\alpha)y}
\]
show \(|t_\alpha(y)|<1\) for every \(y>0\) when \(0<\alpha\le2\). Therefore \(|x_n|\) decreases, and any positive limiting magnitude would contradict strict contraction at that limiting magnitude; hence \(x_n\to0\) globally. Linearization at zero gives \(T'(0)=1-\alpha\); when \(\alpha=1\), \(t_1(y)=y/(1+2y)\), hence the order-three local update.

At \(\alpha=2\), if the orbit ever has \(y_n=1\), its next value is zero. Otherwise, \(y_n\downarrow0\) and the exact reciprocal identity is
\[
\frac1{y_{n+1}}-\frac1{y_n}=\frac{8(1+y_n)}{(1-y_n)^2}\longrightarrow8.
\]
Cesàro averaging the reciprocal increments yields \(1/(n y_n)\to8\), hence \(ny_n\to1/8\). Substituting \(x_n^2=(2c/\lambda)y_n\) and \(f(x_n)-c=c y_n\) gives the stated sharp limits. They do not apply to exactly terminating orbits.

**3. Exact supercritical branch and stability.** An antipodal two-cycle requires \(T(r)=-r\) for \(r>0\), equivalently \(t_\alpha(y)=-1\). The unique solution is \(y_*=(\alpha-2)/(\alpha+2)\), which is positive if and only if \(\alpha>2\); this establishes uniqueness among antipodal cycles and the radius formula. Ordinary fixed points with \(r>0\) cannot occur since \(t_\alpha(y)<1\) for all \(y\ge0\). The derivative of the state map is
\[
T'(x)=t_\alpha(y)+2y\frac{\alpha^2}{[1+(1+\alpha)y]^2}.
\]
At \(y=y_*\), \(t_\alpha=-1\) and \(1+(1+\alpha)y_*=\alpha^2/(\alpha+2)\), giving \(T'(\pm r)=1-8/\alpha^2\). For \(\alpha>2\), this lies strictly between \(-1\) and \(1\), so the two-cycle is locally attracting by contraction of the second iterate. Meanwhile \(T'(0)=1-\alpha<-1\) makes the minimizer repelling. Inserting \(y_*\) into the effective stepsize gives \(\lambda\gamma(r)=2\); the loss formula follows from \(f(x)-c=cy\). Because a genuine nonoptimal two-cycle exists for each \(\alpha>2\), global all-start convergence is impossible. At \(\alpha=3\), \(\lambda=c=1\), the cycle is exactly \(\pm\sqrt{2/5}\), its two-step multiplier is \(1/81\), and its excess loss is \(1/5\).

## Verification

Run `python check_ngn.py` with Python 3 and its standard library. The self-contained test executes 84 exact-rational checks for the map's antipodal branch, derivatives, critical reciprocal identity, stable multipliers and numerical-parameter witnesses; it outputs `EXACT_RATIONAL_CHECKS_PASS 84`. The universal claims are proved by the algebra and monotonicity above, not by the finite test cases. The exact algebraic identities can also be verified manually with rational-function arithmetic.

## Relationship to prior work

Schaipp, Gower and Taylor [1], first public February 10, 2026, give the NGN square-root model, its exact update, and a per-step stability index that grows more slowly than SGD's as the base step increases. Their index comparison does **not** imply convergence of actual iterates for arbitrarily large fixed steps and does not provide this positive-floor bifurcation, critical asymptotic, or attracting cycle.

Orvieto and Xiao [2], first public July 5, 2024, introduced NGN and studied positive-minimum scalar quadratics experimentally (their Figure 2); the cited observation is **nondivergence**, not a proof that every iterate converges to the minimizer. Their general analyses do not state the exact attracting antipodal cycle and sharp transition derived here. A related published quadratic-spectrum result [3] gives exact one-step objective envelopes for *zero-minimum* positive-definite quadratics and explicitly excludes positive objective floors and trajectories. Another published study [4] compares one-step model indices on zero-floor convex radial losses, not multi-step dynamics with a positive floor. Thus the present assertion is neither the original NGN algorithm nor an extension by renaming: its new object is the sharp large-step optimization-versus-boundedness bifurcation caused by an objective offset.

## Limitations

The proof does not classify all possible non-antipodal periodic orbits or global attraction basins for \(\alpha>2\), and does not study stochastic noise, higher dimensions, finite precision or nonquadratic losses. The existence of an attracting cycle is enough to refute all-start convergence; it does not imply divergence to infinity. Even at a fixed positive loss floor, exact terminal points can arise from exceptional initial conditions. This is a mathematical priority assessment based on the sources inspected; a more obscure equivalent analysis could exist. Independent validation has not been performed.

## References

1. F. Schaipp, R. M. Gower and A. Taylor, *Step-Size Stability in Stochastic Optimization: A Theoretical Perspective*, arXiv:2602.09842v1, first publicly released 2026-02-10, Sections 1 and 4.3 and Appendix A. https://arxiv.org/abs/2602.09842
2. A. Orvieto and L. Xiao, *An Adaptive Stochastic Gradient Method with Non-negative Gauss-Newton Stepsizes*, arXiv:2407.04358v1, first publicly released 2024-07-05, Sections 2 and 4. https://arxiv.org/html/2407.04358v1
3. *Two sharp regularization transitions for nonnegative Gauss--Newton steps on SPD quadratics*, published research record, November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-sharp-regularization-transitions-for-nonnegative-gauss-newto--737f754c4cc5
4. *Square-root curvature orders proximal and Gauss--Newton stability on radial losses*, published research record, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-square-root-curvature-orders-proximal-and-gauss-newton-stability--da4742ebe857
