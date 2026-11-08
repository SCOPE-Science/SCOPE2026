# Singular reactivity rounding of the Péclet restart transition

## Finding

For one-dimensional drift–diffusion toward an imperfect reactive point, the optimal Poisson resetting rate has three sharply different limits as the point reactivity tends to infinity. Put \(b=vL/(2D)\) and \(a=kL/(2D)\), with \(D,L,v,k>0\). If \(r_*(a,b)\) minimizes the mean killing time among strictly positive resetting rates, then

\[
\frac{L^2}{D}r_*(a,b)\sim
\begin{cases}
 y_b(2b+y_b),&0<b<1,\\
 2(3/a)^{1/3},&b=1,\\
 2b^2\sqrt{2/[a(b-1)]},&b>1.
\end{cases}
\]

Here \(y_b>0\) is the unique positive solution of
\[
y(2b+y)e^y=(2b+2y)(e^y-1).
\]
In the first case the displayed \(\sim\) means convergence to the stated positive constant; in the other cases it means the ratio tends to one. Thus finite target reactivity rounds the perfect-absorber zero-reset region into a positive optimal rate, with an inverse-square-root law in the drift-dominated region and an inverse-cube-root law at its boundary.

More sharply, fix any real \(\lambda\) and let \(b=1+\lambda a^{-1/3}>0\). There is a unique positive \(Y(\lambda)\) solving
\[
\frac23Y(\lambda)^3+\lambda Y(\lambda)^2=2.
\]
In this critical window,
\[
\lim_{a\to\infty}a^{1/3}\frac{L^2}{D}r_*(a,1+\lambda a^{-1/3})=2Y(\lambda).
\]
Convergence is uniform for \(\lambda\) in every fixed compact interval. In particular, the crossover produces both sharp powers from one cubic scaling function; it is not a claim about the rate for finite negative or positive \(\lambda\) outside the stated window.

## Assumptions and scope

Let \(X_t\) satisfy \(dX_t=-v\,dt+\sqrt{2D}\,dW_t\) on the whole real line, with initial position \(L>0\). An imperfect target at zero kills a trajectory according to the Feynman–Kac weight \(\exp[-k\int_0^t\delta_0(X_s)\,ds]\). The coefficient \(k>0\) has units of distance divided by time. Independently, a rate-\(r>0\) homogeneous Poisson clock restores the position to \(L\), refreshing Brownian increments but not changing \(D,v,k\). A killing event terminates the process. The physical target is on the full line: crossing zero need not cause absorption when \(k<\infty\).

The reset rate \(r_*(a,b)\) is optimized for the **unconditional mean killing time**, not for the exponential survival-tail rate or a deadline success probability. All limits are at fixed \(D,L\), with \(v=2Db/L\) and \(k=2Da/L\) varied as indicated. The fixed-\(b\) regimes hold for each specified \(b\) and do not assert uniformity at \(b=1\); the critical-window result supplies that missing interpolation. The statement does not address drift away from the target, several targets, state-dependent resetting or non-Poisson clocks.

## Proof

**1. Exact dimensionless objective.** Write \(q(s)=\sqrt{v^2+4Ds}\). The free drifted resolvent at target and the target diagonal are respectively
\[
G_s(0\mid L)=q(s)^{-1}\exp\!\left(\frac{vL-q(s)L}{2D}\right),\qquad G_s(0\mid0)=q(s)^{-1}.
\]
For an absorbing point of finite strength \(k\), the rank-one resolvent identity makes the reset-free killing-time Laplace transform
\[
f(s)=\frac{kG_s(0\mid L)}{1+kG_s(0\mid0)}
=\frac{k}{k+q(s)}\exp\!\left(\frac{vL-q(s)L}{2D}\right).
\]
In particular \(f(0)=k/(k+v)<1\): without resetting, trajectories can escape the reactive point after imperfect contact. Independent exponential restarting gives the standard renewal identity
\[
\mathbb E T_r=\frac{1-f(r)}{rf(r)}.
\]
Set \(a=kL/(2D)\), \(b=vL/(2D)\), and \(y=\sqrt{b^2+rL^2/D}-b\). Then \(rL^2/D=y(2b+y)\), and direct substitution yields
\[
\tau_{a,b}(y):=\frac{D}{L^2}\mathbb ET_r
=\frac{g_{a,b}(y)}{y(2b+y)},\qquad
 g_{a,b}(y)=e^y\left(1+\frac{b+y}{a}\right)-1.
\]
Thus optimizing \(r>0\) is equivalent to optimizing \(y>0\).

**2. A single positive optimal root.** Define
\[
N_{a,b}(y)=y(2b+y)g'_{a,b}(y)-(2b+2y)g_{a,b}(y).
\]
The sign of \(\tau'_{a,b}(y)\) is the sign of \(N_{a,b}(y)\). In the absolutely convergent Taylor series \(g_{a,b}(y)=\sum_{n\ge0}c_ny^n\),
\[
c_0=\frac ba,\qquad c_n=\frac{1+(b+n)/a}{n!}\quad(n\ge1).
\]
Writing \(C_n=2b(n-1)c_n+(n-3)c_{n-1}\) for \(n\ge2\) gives
\[
\frac{N_{a,b}(y)}{y^2}
=-\frac{2bc_0}{y^2}-\frac{2c_0}{y}+C_2
+\sum_{n\ge3}C_ny^{n-2}.
\]
Every \(C_n>0\) for \(n\ge3\). Hence \(N_{a,b}(y)/y^2\) is strictly increasing on \((0,\infty)\), tends to \(-\infty\) at zero and \(+\infty\) at infinity. It has exactly one positive zero \(y_*(a,b)\). At this zero the derivative crosses from negative to positive, so it is the unique nondegenerate global minimum; independently, \(\tau\) diverges at both ends because \(c_0=b/a>0\) and the numerator grows exponentially. This uniqueness fact is an auxiliary baseline, not the novel assertion of the theorem.

**3. Singular stationarity expansion.** From the coefficients above,
\[
\begin{aligned}
N_{a,b}(y)={}&-\frac{2b^2}{a}-\frac{2b}{a}y
+\left(b-1+\frac{b^2+b-1}{a}\right)y^2\\
&+\left(\frac{2b}{3}+\frac{2b(b+3)}{3a}\right)y^3
+O((1+a^{-1})y^4),
\end{aligned}
\]
locally uniformly in \(b\) on compact subsets of \((0,\infty)\). The coefficient formula bounds all remaining terms and justifies the stated remainder.

For \(0<b<1\), setting \(a^{-1}=0\) gives \(N_{\infty,b}(y)/y^2\) increasing from \(b-1<0\) to infinity, so it has a unique positive zero \(y_b\). Local uniform convergence and strict monotonicity trap \(y_*(a,b)\) between any two nearby points surrounding \(y_b\), giving \(y_*(a,b)\to y_b\) and the positive limiting rate.

For fixed \(b>1\), the limiting function \(N_{\infty,b}(y)/y^2\) is positive for all \(y>0\); hence \(y_*(a,b)\to0\). Substitute \(y=t a^{-1/2}\) in the expansion. Multiplying \(N\) by \(a\) gives uniformly on compact positive \(t\)-intervals
\[
a N_{a,b}(ta^{-1/2})\longrightarrow -2b^2+(b-1)t^2.
\]
The limiting expression has a unique positive zero \(t=b\sqrt{2/(b-1)}\). Monotonic-root bracketing proves \(y_*(a,b)\sim b\sqrt{2/[a(b-1)]}\).

At \(b=1\), the quadratic term loses its order-one coefficient. Now substitute \(y=t a^{-1/3}\). The same expansion gives
\[
aN_{a,1}(ta^{-1/3})\longrightarrow -2+\frac23t^3,
\]
whose positive zero is \(t=3^{1/3}\). Again, the unique-root property and bracketing yield \(y_*(a,1)\sim(3/a)^{1/3}\).

**4. Full critical crossover.** Let \(b_a=1+\lambda a^{-1/3}\) and \(y=ta^{-1/3}\). For every compact set of \(\lambda\)'s and compact positive \(t\)-interval,
\[
aN_{a,b_a}(ta^{-1/3})
=-2+\lambda t^2+\frac23t^3+o(1)
\]
uniformly. The cubic is initially negative and crosses zero exactly once on \((0,\infty)\): if \(\lambda<0\), its derivative \(2t(t+\lambda)\) is initially negative and thereafter positive, whereas if \(\lambda\ge0\) it is strictly increasing. Comparing the stationarity sign at \(t=Y(\lambda)\pm\varepsilon\), and using continuity and the unique finite-\(a\) optimum, proves \(a^{1/3}y_*(a,b_a)\to Y(\lambda)\). Positive roots of the cubic depend continuously on \(\lambda\), with compact-range positive upper and lower bounds; the same sign-bracketing is therefore uniform for \(\lambda\) in compact sets. Finally \(r_*L^2/D=y_*(2b_a+y_*)\) establishes the stated rate crossover and every fixed-parameter formula.

## Verification

A standard-library numerical diagnostic is included as `verify.py`. Running `python3 verify.py` checks the exact stationary numerator against its convergent coefficient series, signs and sampled monotonicity of the stationary equation, sampled global-minimum comparisons, the three fixed-\(b\) regimes, and the critical-window cubic normalization. The verifier reports 1,591 passing bounded checks. The mathematical statements for all admissible parameters and the asymptotic limits follow from the proof above, not from sampling.

## Relationship to prior work

Mazzolo (2026, arXiv:2609.22527v1) established the drifted delta-killing resolvent and reset survival formula used in Step 1; its Appendix A treats driftless optimal resetting and then weak-drift perturbations. The novelty asserted here is **only** the singular near-perfect-reactivity phase diagram and its critical crossover, not the objective, stationary-point equation or finite-reactivity existence/uniqueness.

Ray, Mondal and Reuveni (2019, arXiv:1811.08239) established the perfect-absorber Péclet transition at \(b=1\). That exact limiting transition is prior work. The new question is how finite reactivity regularizes its zero-rate side, and the uniform cubic crossover between the inverse-square-root and inverse-cube-root regimes. Whitehouse, Evans and Majumdar (2013, arXiv:1301.2489) solved imperfect absorption with resetting without drift. Das and Giuggioli (2022, arXiv:2209.08330) gave a broad discrete-time biased-walk/partially absorbing defect renewal formula and an unbiased diffusive continuum example. Their general formulas are acknowledged, but the specific joint drift–reactivity optimizer asymptotics and crossover are not stated in the inspected results. A general formula permitting a later calculation is not claimed as a new underlying mechanism.

## Limitations

The proof assumes precisely one delta sink on the full line, complete instantaneous resets to the initial point, and strictly constant coefficients. The zero-reset boundary of the perfectly absorbing limit is **not** included as a finite-\(a\) optimizer. The strong drift limit \(b\to\infty\) is not simultaneous with the reactivity limit here. The universal critical-window formula is proved for bounded \(\lambda\), not for arbitrary \(\lambda\) growing with \(a\). The result concerns the minimizing *mean* rather than the survival exponent. Publication priority could be affected by a broader, unidentified singular-perturbation theorem applicable to the same renewal objective; mathematical proof does not settle that historical question.

## References

- A. Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes*, arXiv:2609.22527v1 (first posted 2026-09-18), https://arxiv.org/abs/2609.22527.
- S. Ray, D. Mondal and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239, https://arxiv.org/abs/1811.08239.
- J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489, https://arxiv.org/abs/1301.2489.
- D. Das and L. Giuggioli, *Discrete space-time resetting model: Application to first-passage and transmission statistics*, arXiv:2209.08330, https://arxiv.org/abs/2209.08330.
