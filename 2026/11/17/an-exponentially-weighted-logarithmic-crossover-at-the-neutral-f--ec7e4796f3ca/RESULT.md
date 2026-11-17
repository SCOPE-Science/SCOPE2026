# An exponentially weighted logarithmic crossover at the neutral flip of a sigmoid interval map

## Finding

Consider the EOS interval map \(F_a(x)=x+\frac12-(1+e^{-ax})^{-1}=x-\frac12\tanh(ax/2)\), the symmetric \(b=1/2\) member of the two-parameter interval-map family. Fix any \(x_0\) with \(0<|x_0|\le 1/10\), any real \(\theta\), and an integer experiment horizon \(N\). **Hold the parameter constant throughout that experiment** at \(a_N=8+\theta/N\), and denote its \(N\)-th iterate by \(x_{N,N}=F_{a_N}^{N}(x_0)\). For each fixed \(\theta\), as \(N\to\infty\),
\[
\boxed{\frac{1}{x_{N,N}^{2}}=\frac{64}{3}\,N\Phi(\theta)+\frac{48}{5}e^{-\theta/2}\log N+O_{\theta,x_0}(1)},
\qquad
\Phi(\theta)=\begin{cases}\frac{1-e^{-\theta/2}}{\theta/2},&\theta\ne0,\\1,&\theta=0.\end{cases}
\]
The bound is also uniform for \(\theta\) in any fixed compact real interval and \(|x_0|\) in any fixed compact subset of \((0,1/10]\). In particular the full finite-horizon transition at order \(N^{-1}\) carries not just a leading amplitude profile but a **parameter-dependent logarithmic coefficient**. The critical slice \(\theta=0\) is already covered, after an exact conjugacy, by the earlier fixed-parameter entropic congestion result [2]; the claim of novelty here is the \(\theta\ne0\) crossover, especially the factor \(e^{-\theta/2}\) on its logarithmic correction.

## Assumptions and scope

The initial point is fixed independently of \(N\). Every experiment uses one constant real parameter \(a_N=8+\theta/N\), not a time-varying parameter sequence within a trajectory. The asymptotic holds for each fixed \(\theta\in\mathbb R\) with \(N\) sufficiently large that \(a_N>0\). The upper bound \(1/10\) selects an invariant local neighborhood and is not an optimal basin threshold. The displayed inverse square requires a nonzero initial condition; under these assumptions all iterates remain nonzero. The assertion concerns the \(N\)-step transient, not a fixed-parameter infinite-time attractor, and no uniformity as \(|\theta|\to\infty\) is claimed. The map is odd, so the proof uses \(|x_0|\).

## Proof

**1. Exact sign reduction and an invariant neighborhood.** Put \(T_a(w)=\frac12\tanh(aw/2)-w\) for \(w>0\). At \(a=8\), \(T_8\) is positive and increasing on \([0,1/10]\), with \(T_8(1/10)<1/10\), since \(T_8'(w)=2\operatorname{sech}^2(4w)-1>0\) there. Positivity, monotonicity and strict containment at the right endpoint persist for all \(a\) sufficiently close to eight. Therefore, for all sufficiently large \(N\), \(w_{k,N}:=|F_{a_N}^{k}(x_0)|\) obeys the positive recurrence \(w_{k+1,N}=T_{a_N}(w_{k,N})\) within \((0,1/10]\), and the signs of the original iterates alternate.

**2. Uniform exact inverse-square expansion.** The analytic Taylor series, uniformly for \(a\) near eight, is
\[
T_a(w)=s_aw-d_aw^3+e_aw^5+O(w^7),\quad
s_a=\frac a4-1,\quad d_a=\frac{a^3}{48},\quad e_a=\frac{a^5}{480}.
\]
With \(v_{k,N}=w_{k,N}^{-2}\ge100\), direct inversion gives a uniform recurrence
\[
v_{k+1,N}=q_N v_{k,N}+A_N+\frac{B_N}{v_{k,N}}+O(v_{k,N}^{-2}),
\]
where
\[
q_N=s_{a_N}^{-2},\qquad A_N=\frac{2d_{a_N}}{s_{a_N}^{3}},\qquad
B_N=\frac{3d_{a_N}^2}{s_{a_N}^{4}}-\frac{2e_{a_N}}{s_{a_N}^{3}}.
\]
In particular
\[
q_N=1-\frac{\theta}{2N}+O(N^{-2}),\quad
A_N=\frac{64}{3}+O(N^{-1}),\quad
B_N=\frac{1024}{5}+O(N^{-1}).
\]
The remainder estimate holds uniformly for all iterates in the displayed invariant interval. To bound the additive drift rigorously rather than assuming small remainder, consider \(H_a(w)=T_a(w)^{-2}-s_a^{-2}w^{-2}\). It extends continuously and positively to \(w=0\), with \(H_a(0)=2d_a/s_a^3\); its positivity at positive \(w\) follows from \(0<T_a(w)<s_aw\), the strict inequality \(\tanh t<t\). Compactness gives \(0<c\le H_a(w)\le C\) uniformly for \(a\) near eight and \(0\le w\le1/10\). Thus
\[
q_Nv_{k,N}+c\le v_{k+1,N}\le q_Nv_{k,N}+C.
\]
Discrete geometric-sum comparison (using \(q_N=1+O(N^{-1})\)) implies \(c_\theta(k+1)\le v_{k,N}\le C_{\theta,x_0}(k+1)\) for \(0\le k\le N\).

**3. Uniform first-order control.** Iterate the inverse-square recurrence and use \(v_{k,N}\asymp(k+1)\), uniformly through the horizon. Since the \(O(v^{-1})\) contribution sums to \(O(\log(k+1))\), while \(q_N^{k}=1+O(k/N)\), one obtains
\[
v_{k,N}=\frac{64}{3}k+O_{\theta,x_0}\!\left(1+\log(k+1)+\frac{k^2}{N}\right)
\quad(0\le k\le N).
\]
Write \(A=64/3\). Comparing reciprocals with \(1/[A(k+1)]\) now gives
\[
\sum_{k=0}^{N-1}\frac{1}{v_{k,N}}=\frac1A\log N+O(1),
\]
because the difference is bounded by a constant multiple of \((1+\log(k+1))/(k+1)^2+N^{-1}\), which has bounded total sum.

**4. Weighted borderline harmonic sum.** The exact iterated recurrence reads
\[
v_{N,N}=q_N^N v_{0,N}+A_N\sum_{k=0}^{N-1}q_N^{N-1-k}
+B_N\sum_{k=0}^{N-1}\frac{q_N^{N-1-k}}{v_{k,N}}+O\!\left(\sum_{k=0}^{N-1}\frac{q_N^{N-1-k}}{v_{k,N}^{2}}\right).
\]
The final error is \(O(1)\), and the initial term is \(O(1)\). The geometric sum satisfies
\[
A_N\sum_{k=0}^{N-1}q_N^{N-1-k}
=\frac{64}{3}N\int_0^1e^{-\theta(1-t)/2}\,dt+O(1)
=\frac{64}{3}N\Phi(\theta)+O(1).
\]
For \(0\le k<N\), \(q_N^{N-1-k}=e^{-\theta/2}+O_{\theta}((k+1)/N)\). Inserting this into the weighted reciprocal sum, using \(v_{k,N}\asymp k+1\), proves
\[
\sum_{k=0}^{N-1}\frac{q_N^{N-1-k}}{v_{k,N}}
=\frac{e^{-\theta/2}}{A}\log N+O(1).
\]
Since \((1024/5)/(64/3)=48/5\), combining the terms gives the claimed two-order formula. Every estimate above is uniform for compact ranges of \(\theta\) and positive initial amplitudes bounded away from zero.

## Verification

The accompanying `check_crossover.py` independently expands \(T_a\) to fifth order in exact SymPy rational arithmetic and checks the rational constants \(64/3\), \(1024/5\), and \(48/5\). It then computes finite iterations for both signs of the critical detuning, and compares the residual after subtraction of **both** the leading and logarithmic terms across increasing horizons and several initial amplitudes. Tests are finite illustrations, whereas the inverse-square recurrence and summability arguments above establish the all-\(N\) result.

## Relationship to prior work

Bielawski–Chotibut–Falniowski–Misiurewicz–Piliouras [1] introduced and studied the full EOS family, including period-rotation behavior at large steepness. A prior publicly indexed theorem [2] treats the same map after the exact logit conjugacy \(u=8x\) **at the fixed critical parameter** \(a=8\), and already gives \(x_{2m}^{-2}=\frac{128}{3}m+\frac{48}{5}\log m+O(1)\). Neither that critical slice, its leading \(n^{-1/2}\) relaxation, nor the existence and stability of its attracting two-cycle is newly claimed here. A separate quantitative quadratic-flip theorem [3] and the state-scaling theory [4] address finite-horizon leading crossover profiles; they do not imply the explicit EOS-specific logarithmic coefficient as stated. The present claim concerns **the fixed-per-experiment near-critical detuning** \(a_N=8+\theta/N\), which produces both an explicit full crossover \(\Phi(\theta)\) and the exponentially reweighted logarithmic correction. Similarity to the universal cubic normal form is openly acknowledged.

## Limitations

The result is local in initial amplitude and concerns one sigmoid family, not an arbitrary smooth flip map. The theorem does not classify behavior for larger initial conditions or fixed noncritical \(a\) after infinitely many iterations. The leading crossover is a natural consequence of parabolic normal-form scaling and should not be treated as a new universal mechanism. The novelty assessment centers on the explicit model-specific **second-order, parameter-dependent logarithmic coefficient**, which is not present in the inspected primary results. Unindexed equivalent asymptotic statements remain a genuine literature risk. No independent mathematical audit has been performed.

## References

1. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, first publicly posted 2024-11-03. https://arxiv.org/abs/2411.01495
2. *Global neutral-flip attraction and signed critical relaxation in an entropic congestion map*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-global-neutral-flip-attraction-and-signed-critical-relaxation-in--54b59b4edf7d
3. *Exact finite-time susceptibility crossover at a quadratic flip threshold*, published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-finite-time-susceptibility-crossover-at-a-quadratic-flip-t--acec857a2ec3
4. D. A. Martin, Q.-Y. Tang and D. R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, arXiv:2505.24673v1, first posted 2025-05-30. https://arxiv.org/abs/2505.24673
