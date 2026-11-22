# Equilibrium-crossing nonattainment in housekeeping-budget thermodynamic control

## Finding

Consider a scalar control \(\lambda\) moving from \(a\) to \(b\), with \(a<c<b\), and a fixed positive housekeeping budget \(B\). In the leading slow-driving problem, define
\[
\mathcal H[\lambda]=\int_0^T\sigma(\lambda(t))\,dt=B,
\qquad
\mathcal E[\lambda]=\int_0^T\zeta(\lambda(t))\dot\lambda(t)^2\,dt.
\]
Here \(T\in(0,\infty)\) is free, \(\sigma\) is the stationary housekeeping entropy-production rate, and \(\zeta\) is the scalar thermodynamic friction.

**Theorem.** Suppose \(\sigma\in C^2([a,b])\), \(\sigma\geq0\), \(\sigma(c)=0\), \(\sigma(x)>0\) for \(x\ne c\), and \(\zeta\in C([a,b])\) with \(\zeta>0\). Among all finite-duration absolutely continuous controls with these endpoints and budget and with finite energy,
\[
\boxed{\inf\mathcal E=\frac{\mathcal L^2}{B},\qquad
\mathcal L=\int_a^b\sqrt{\zeta(x)\sigma(x)}\,dx>0,}
\]
but **no finite-duration control attains this infimum**. Every sequence approaching it has durations tending to infinity.

For \(\varepsilon>0\), a concrete asymptotically minimizing family is obtained by prescribing the positive speed
\[
\dot\lambda=v_\varepsilon(\lambda)
=\frac{J_\varepsilon}{B}\sqrt{\frac{\sigma(\lambda)+\varepsilon^2}{\zeta(\lambda)}},
\quad J_\varepsilon=\int_a^b\frac{\sigma(x)\sqrt{\zeta(x)}}{\sqrt{\sigma(x)+\varepsilon^2}}\,dx.
\]
If \(\sigma(x)=A(x-c)^2+o((x-c)^2)\) as \(x\to c\), with \(A>0\), then this family has
\[
\boxed{T_\varepsilon\sim\frac{2B}{\mathcal L}\sqrt{\frac{\zeta(c)}{A}}\log(1/\varepsilon),\qquad
\mathcal E[\lambda_\varepsilon]\longrightarrow\mathcal L^2/B.}
\]
The logarithm uses fixed units for \(\varepsilon\); replacing \(\log(1/\varepsilon)\) by \(\log(\varepsilon_0/\varepsilon)\) changes only lower-order terms.

More generally, if an isolated zero has order \(\sigma(x)\sim A|x-c|^p\), \(p>0\), with continuous strictly positive \(\zeta\), then the Cauchy--Schwarz lower bound is attained in finite time if and only if \(p<2\). Thus the quadratic zero is the borderline nonattainment case.

## Assumptions and scope

The optimization above is **exact for the stated leading-order variational functional**, not a claim of exact finite-speed optimality for the original time-dependent Markov master equation. An admissible control has some finite \(T>0\), belongs to \(AC([0,T])\), has specified endpoints, and has finite \(\mathcal E\). The stationary EPR and friction depend on the control only. The unique interior equilibrium control \(c\) has vanishing stationary EPR; both endpoints are dissipative. The budget \(B\) is arbitrary and positive; for physical slow-driving interpretation it should be chosen in the slow-control regime.

The assumptions are realized by a positive-rate, irreducible, three-state Markov ring. Label states \(i=0,1,2\) modulo three and assign forward and backward transition rates
\[
q_{i,i+1}(\lambda)=\exp[(\mathbf1_{\{i=0\}}+\tfrac12)\lambda],\qquad
q_{i,i-1}(\lambda)=\exp[(\mathbf1_{\{i=0\}}-\tfrac12)\lambda].
\]
The diagonal generator entries are minus their row sums. With controls \(\lambda\in[-d,d]\) for any sufficiently small \(d>0\), the steady-state affinity is \(3\lambda\). Hence \(\lambda=0\) is the sole detailed-balance point. In the normalization of the Green--Kubo friction used in the cited housekeeping-budget framework,
\[
\sigma(\lambda)=\lambda^2+O(\lambda^3),\qquad
\zeta(\lambda)=\frac{2}{27}+O(\lambda).
\]
Thus \(c=0\) is a genuine, quadratically vanishing housekeeping rate with a nonzero friction coefficient, not a freely chosen singular toy weight.

## Proof

**1. Universal bound.** For any admissible control, Cauchy--Schwarz and the one-dimensional path-variation inequality give
\[
\mathcal E B\geq
\left(\int_0^T|\dot\lambda(t)|\sqrt{\zeta(\lambda(t))\sigma(\lambda(t))}\,dt\right)^2
\geq\mathcal L^2.
\]
The second inequality follows by applying the chain rule to an antiderivative of \(\sqrt{\zeta\sigma}\); it permits backtracking but does not incorrectly identify a signed integral with total variation.

**2. No finite-time equality.** Equality would require a monotone trajectory and, away from the zero of \(\sigma\), the almost-everywhere speed equation
\[
\dot\lambda=\kappa\sqrt{\sigma(\lambda)/\zeta(\lambda)},\qquad \kappa=\mathcal L/B>0.
\]
Since \(\sigma\) is nonnegative and \(C^2\), its derivative vanishes at the interior minimum \(c\), and Taylor's theorem gives \(\sigma(x)\leq C|x-c|^2\) near \(c\). Because \(\zeta\) stays bounded below, the absolute value of the right side is at most \(C'|\lambda-c|\). A finite-time solution reaching \(c\) cannot leave it by Gronwall's inequality. Every continuous path from \(a\) to \(b\) must reach and then leave \(c\), so equality is impossible. A plateau at \(c\) does not bypass this obstruction.

**3. Approaching the sharp infimum.** Define
\[
K_\varepsilon=\int_a^b\sqrt{\zeta(x)}\sqrt{\sigma(x)+\varepsilon^2}\,dx.
\]
The positive speed in the Finding defines a finite-duration monotone trajectory. The substitution \(dt=dx/v_\varepsilon(x)\) yields exactly
\[
\mathcal H=B,\qquad
\mathcal E=J_\varepsilon K_\varepsilon/B,\qquad
T_\varepsilon=\frac{B}{J_\varepsilon}\int_a^b\frac{\sqrt{\zeta(x)}}{\sqrt{\sigma(x)+\varepsilon^2}}\,dx.
\]
Dominated convergence gives \(J_\varepsilon\to\mathcal L\) and \(K_\varepsilon\to\mathcal L\), hence the claimed infimum. If \(\sigma\sim A(x-c)^2\), a fixed small neighborhood of \(c\) contributes \(2\sqrt{\zeta(c)/A}\log(1/\varepsilon)+o(\log(1/\varepsilon))\) to the last integral. The region away from \(c\) contributes a bounded amount. This proves the displayed time law.

**4. Divergence for every minimizing sequence.** Suppose a minimizing sequence had bounded durations. Since \(B\leq T\max\sigma\), durations are bounded away from zero. Pass to a subsequence with \(T_n\to T_*\in(0,\infty)\) and rescale controls to the unit interval. Bounded \(\mathcal E\), uniform positivity of \(\zeta\), and bounded durations give a uniform \(H^1\) bound. One-dimensional compactness yields uniform convergence and weak \(H^1\) convergence. The budget and endpoints pass to the limit, while the energy is lower semicontinuous. The limit would attain the lower bound, contradicting step 2. Therefore all near-minimizing duration sequences diverge.

**5. Threshold in the vanishing exponent.** The equality equation away from the zero produces the formal physical travel time
\[
T_{\mathrm{eq}}=\frac{B}{\mathcal L}\int_a^b\sqrt{\frac{\zeta(x)}{\sigma(x)}}\,dx.
\]
The local integral is finite exactly when \(\int_0^\eta x^{-p/2}\,dx\) is finite, namely \(p<2\). For \(p<2\), its inverse cumulative-time map yields an admissible finite-time equality trajectory (and one may also pause at the zero). For \(p\geq2\), nonattainment follows as above directly from the divergent travel-time integral; the regularized construction still approaches the infimum.

**6. Three-state Markov realization.** At \(\lambda=0\), the generator has diagonal \(-2\) and all off-diagonal entries \(1\), with stationary row distribution \(\pi(0)=(1/3,1/3,1/3)\). Differentiating \(\pi Q=0\) at zero gives
\[
\pi'(0)=(-2/9,1/9,1/9).
\]
Every clockwise steady edge current has derivative \(1/3\) at zero. Since the clockwise product of rates divided by the counterclockwise product is \(e^{3\lambda}\), stationary entropy production is \(3\lambda J(\lambda)=\lambda^2+O(\lambda^3)\). The score is \(\partial_\lambda\log\pi|_0=(-2/3,1/3,1/3)\), which is a mean-zero eigenvector with relaxation eigenvalue \(-3\). Its stationary variance is \(2/9\), so its Green--Kubo time integral, the friction at equilibrium, is \((2/9)/3=2/27\). Analyticity and positivity around zero establish the remaining hypotheses on some \([-d,d]\).

## Verification

The accompanying `check.py` uses exact rational arithmetic to check the perturbed stationary equation, three identical clockwise current derivatives, score eigenvector and friction \(2/27\). It also tests the explicitly solvable representative \(\sigma(x)=x^2\), \(\zeta(x)=1\) on \([-1,1]\), at budget \(B=2\), for which
\[
J_\varepsilon=\sqrt{1+\varepsilon^2}-\varepsilon^2\operatorname{arsinh}(1/\varepsilon),\quad
K_\varepsilon=\sqrt{1+\varepsilon^2}+\varepsilon^2\operatorname{arsinh}(1/\varepsilon).
\]
In that example \(B\mathcal E-1=\varepsilon^2-\varepsilon^4\operatorname{arsinh}(1/\varepsilon)^2>0\), and \(T_\varepsilon\sim2B\log(1/\varepsilon)\). Run `python3 check.py` with the standard Python library. The infinite-dimensional quantifier over all admissible protocols is proved analytically above, not inferred from tests.

## Relationship to prior work

Sugie, Loutchko and Kobayashi (2026, arXiv:2611.14891v1), equations (5)--(11), introduce housekeeping-budget thermodynamic geometry and the length bound, explicitly requiring the steady EPR to remain positive for the entropic-time change of variables. Their equilibrium discussion treats protocols that remain at equilibrium, where the only feasible leading-order budget is zero. The present result concerns the distinct, physically natural situation of **positive-budget driving across one isolated detailed-balance point**: the sharp bound remains valid as an infimum, but its finite-time equality assertion cannot extend across the zero. The complete vanishing-exponent threshold and explicit three-state realization clarify this singular boundary. Kamp and Proesmans (2025 preprint, 2026 publication) study fixed-duration optimization of a different total-EP functional; their diverging-parameter protocols do not imply the nonattainment result for the fixed-housekeeping-budget excess functional.

## Limitations

This theorem concerns only the leading, slow-driving thermodynamic functional, not an exact finite-time master-equation optimum. It assumes a one-dimensional control path, strictly positive continuous friction, fixed positive budget and a zero of the stationary EPR inside the required control interval. It makes no general claim for multidimensional controls that can route around the equilibrium locus, for nonsmooth controls with instantaneous jumps, or for exact higher-order slow-driving corrections. The logarithmic coefficient requires a nondegenerate quadratic zero; higher-order zeros have other divergence rates. No independent scientific verification is asserted.

## References

1. K. Sugie, D. Loutchko and T. J. Kobayashi, *Optimal Driving between Nonequilibrium Steady States under a Dissipation Budget*, arXiv:2611.14891v1 (first public 2026-11-11), https://arxiv.org/html/2611.14891v1.
2. D. Kamp and K. Proesmans, *Thermodynamic control of non-equilibrium systems*, arXiv:2506.14416v1 (first public 2025-06-17), https://arxiv.org/html/2506.14416v1; *Physical Review E* **113**, 014140 (2026).
3. D. Mandal and C. Jarzynski, *Analysis of slow transitions between nonequilibrium steady states*, *Journal of Statistical Mechanics* 063204 (2016), cited in [1] for the slow-driving excess-EP framework.
