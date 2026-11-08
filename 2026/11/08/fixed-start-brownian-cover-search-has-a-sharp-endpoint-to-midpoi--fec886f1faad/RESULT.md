# Fixed-start Brownian cover search has a sharp endpoint-to-midpoint resetting-site transition

## Finding

Consider reflected Brownian diffusion on a closed interval, initially at its midpoint, whose position is instantaneously reset at the times of an independent Poisson process to a fixed, freely chosen site. Resetting does not erase which endpoints have already been visited. For **every positive resetting rate**, the mean time to visit both endpoints is minimized only by an endpoint resetting site, or only by the midpoint, except at one exactly identified critical rate at which all three sites tie. There are no other optimal reset sites.

Precisely, let \(D,L,r>0\), and put
\[
 s=L\sqrt{r/D},\qquad c=\cosh(s/2),\qquad c_\star>1:\;4c_\star^3-6c_\star-3=0.
\]
The cubic has exactly one real root in \((1,\infty)\):
\[
 c_\star=1.423661050931536\ldots,\qquad
 r_\star=\frac{4D}{L^2}\operatorname{arcosh}^2(c_\star)
 =3.173803931003917\ldots\frac{D}{L^2}.
\]
If \(T_z\) is the time at which both endpoints have been visited, with initial position \(L/2\) and resetting point \(z\in[0,L]\), then
\[
 \underset{z\in[0,L]}{\operatorname{argmin}}\ \mathbb E[T_z]
 =\begin{cases}
 \{0,L\},&0<r<r_\star,\\
 \{0,L/2,L\},&r=r_\star,\\
 \{L/2\},&r>r_\star.
 \end{cases}
\]
Thus the optimal site jumps discontinuously from an endpoint to the midpoint as the rate crosses the critical value. This theorem fixes the starting location independently of the resetting site; it is **not** the coincident-start/reset optimization problem.

## Assumptions and scope

Between resetting events, the process is continuous reflected Brownian motion on \([0,L]\) with backward generator \(D\partial_{xx}\) and Neumann reflection at both endpoints. At each event of a Poisson process of rate \(r>0\), the position becomes \(z\), independent of its prior position; the event takes zero time. Visits to \(0\) or \(L\), including visits caused by resetting directly onto an endpoint, are permanently recorded. The first position is \(L/2\), **not** \(z\) unless \(z=L/2\). The completion time \(T_z\) is the first time both endpoints belong to the visited set. The optimizer is over all deterministic \(z\in[0,L]\), with \(D,L,r\) fixed. There is no delay or cost for resetting, no gate at the endpoints, and no extra reset when an endpoint is hit.

## Proof

**1. One-target renewal formula.** For each target set \(A\in\{\{0\},\{L\},\{0,L\}\}\), let \(\tau_A\) be the first hitting time by the diffusion *without* resetting, and let \(\phi_A(x)=\mathbb E_x[e^{-r\tau_A}]\). A first-reset decomposition, valid also for \(z\in A\), gives the mean hitting time in the resetting process started at \(y\):
\[
 F_A(y;z)=\frac{1-\phi_A(y)}{r\phi_A(z)}.
\]
Indeed, the mean length of the first attempt is \((1-\phi_A(y))/r\), its probability of reaching the reset clock first is \(1-\phi_A(y)\), and subsequent attempts begin at \(z\). The resulting geometric renewal identity yields the displayed formula. All denominators are positive.

Put \(k=\sqrt{r/D}\). Solving \(D\phi''=r\phi\) with absorbing boundary conditions at \(A\) and reflecting conditions at whichever endpoint is not in \(A\) yields
\[
 \phi_{\{L\}}(x)=\frac{\cosh(kx)}{\cosh(kL)},\quad
 \phi_{\{0\}}(x)=\frac{\cosh(k(L-x))}{\cosh(kL)},\quad
 \phi_{\{0,L\}}(x)=\frac{\cosh(k(x-L/2))}{\cosh(kL/2)}.
\]

**2. Exact cover mean, with distinct starting and resetting sites.** For each sample path, the time to visit both endpoints is the maximum of their individual first-hitting times, and the time to visit either is their minimum. Thus the elementary pathwise identity \(\max(U,V)=U+V-\min(U,V)\) gives
\[
 \mathbb E[T_z]=F_{\{0\}}(L/2;z)+F_{\{L\}}(L/2;z)-F_{\{0,L\}}(L/2;z).
\]
With \(s=kL\), \(c=\cosh(s/2)\), and \(K=\cosh(s)=2c^2-1\), substitution yields the exact positive mean
\[
 r\mathbb E[T_z]=(K-c)\left(\frac1{\cosh(sz/L)}+\frac1{\cosh(s(1-z/L))}\right)
 -\frac{c-1}{\cosh(s(z/L-1/2))}.
\]
The historical visit record, rather than a restart of the whole search on hitting one endpoint, is essential to this identity.

**3. Reduction to one variable and absence of interior optima.** Set
\[
 u=\cosh(s(z/L-1/2)),\qquad 1\le u\le c.
\]
The pair of symmetric reciprocal hyperbolic cosines satisfies
\[
 \frac1{\cosh(s z/L)}+\frac1{\cosh(s(1-z/L))}
 =\frac{2cu}{u^2+c^2-1}.
\]
Consequently minimizing the mean is equivalent to minimizing
\[
 H_c(u)=\frac{2c(2c^2-1-c)u}{u^2+c^2-1}-\frac{c-1}{u},\qquad u\in[1,c].
\]
Writing \(t=u^2\), direct differentiation gives
\[
 H_c'(u)=\frac{(c-1)N_c(u^2)}{u^2(u^2+c^2-1)^2},
\]
where
\[
 N_c(t)=-(4c^2+2c-1)t^2+2(c^2-1)(2c^2+c+1)t+(c^2-1)^2.
\]
For every \(c>1\), the coefficient of \(t^2\) is negative, the coefficient of \(t\) and constant are positive, and the two real roots of \(N_c\) have opposite signs. Thus \(H_c'\) is positive below its unique positive turning root and negative above it. On \([1,c]\), \(H_c\) is either monotone or increases and then decreases. In particular, **every global minimum is attained at \(u=1\) or \(u=c\)**, and if those two values tie, no strict interior point is also a minimizer.

The case \(u=1\) is exactly \(z=L/2\); the case \(u=c\) consists exactly of \(z=0\) and \(z=L\). Their difference factors as
\[
 H_c(c)-H_c(1)
 =\frac{(c-1)^2(4c^3-6c-3)}{c(2c^2-1)}.
\]
The function \(4c^3-6c-3\) is strictly increasing for \(c>1\), takes value \(-5\) at \(c=1\), and diverges to \(+\infty\). It has exactly one root \(c_\star>1\). Since \(c=\cosh(L\sqrt{r/D}/2)\) is strictly increasing in \(r>0\), the endpoint comparison proves all three regimes and the exact critical rate. This completes the proof.

## Verification

`verify_location_transition.py` independently checks the derivative identity and endpoint factorization with exact symbolic algebra, 54 high-precision hyperbolic reductions, the cubic root and change of optimizer, and five independent reflected-lattice diffusion calculations (grid sizes 64 and 128) with endpoint-visit history and reset jumps. All checks passed. The finite-grid calculations are confirmations only; the global and all-rate conclusions are established analytically by the one-sign-change derivative argument and cubic factorization.

For a quick dimensionless reproducibility example with \(D=L=1\), at \(s=1\) the endpoint reset has mean \(0.5715107277\ldots\) versus \(0.6092401277\ldots\) for midpoint reset; at \(s=2\), the respective means are \(0.6142537645\ldots\) and \(0.5832833393\ldots\). These values use the same initial position \(L/2\) in both comparisons.

## Relationship to prior work

Ghosh and Sabhapandit (2026) compute the interval cover-time distribution and optimize the **resetting frequency** with the initial and resetting positions both fixed at the midpoint. Linn and Lawley (2024; revised 2025), Section 4.1, give exact mean cover times for arbitrary asymmetric distances to endpoints when the search starts **at the resetting point**; their results do not classify the optimizer over a separate resetting site for a fixed midpoint start. The exact equal-start/equal-reset location transition has also been established separately, with a *different* critical value. None of those cases is the model solved here.

Calvert and Evans (2021) study searches for multiple targets on the real line, incorporating an **extra immediate reset after the first target is found**, unlike the reflected trajectory with persistent visit history considered here. Their target-geometry optimization does not supply the cubic boundary-to-midpoint reset-site transition in the present model. General one-target renewal formulas are used as known tools, not claimed as new. No claim of independent publication-priority certification is made.

## Limitations

The theorem concerns only **mean** completion time for one Brownian particle, a fixed midpoint start, deterministic resetting point, Poisson resets, and perfect reflection. It does not optimize the reset rate jointly, assert finite-time stochastic dominance, or determine median/quantile or exponential-tail-optimal reset locations. More general multi-target reset-site optimization literature may contain unindexed equivalent results; no search alone establishes uniqueness of a contribution.

## References

1. A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting* (2026), arXiv:2605.31207, https://arxiv.org/abs/2605.31207. First publicly posted 2026-05-29.
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting* (2024, revised 2025), arXiv:2406.12154, https://arxiv.org/abs/2406.12154, especially Section 4.1.
3. G. R. Calvert and M. R. Evans, *Searching for clusters of targets under stochastic resetting* (2021), arXiv:2111.02335, https://arxiv.org/abs/2111.02335, especially Sections 2–3.
4. P. C. Bressloff, *Search processes with stochastic resetting and multiple targets*, Physical Review E 102, 022115 (2020), https://doi.org/10.1103/PhysRevE.102.022115.
