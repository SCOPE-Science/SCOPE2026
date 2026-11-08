# A sharp universal entrainment threshold for periodically driven replicator maps

## Finding

**Theorem (uniform forcing threshold, critical exception, and statistical calibration).** For a constant \(a>0\) and a sequence \(b_n\in(0,1)\), consider the two-strategy multiplicative-weights / replicator recurrence
\[
 x_{n+1}=f_{a,b_n}(x_n):=\frac{x_n}{x_n+(1-x_n)\exp(a(x_n-b_n))},\qquad x_0\in(0,1).
\]

1. **Periodic entrainment, including the endpoint.** If \(0<a\le8\) and \(b_{n+m}=b_n\) for some integer \(m\ge1\), there is exactly one \(m\)-periodic solution \((x_n^*)\) in \((0,1)\). Every interior initial state converges to that solution at each phase: \(x_{km+j}\to x_j^*\) for \(0\le j<m\). Its exact phase average is
\[
 \frac1m\sum_{j=0}^{m-1}x_j^*=\frac1m\sum_{j=0}^{m-1}b_j.
\]
 Convergence is eventually exponential when \(a<8\). For \(a=8\), it remains eventually exponential unless \(b_j=1/2\) for every phase.

2. **Arbitrary bounded forcing.** If \(0<a\le8\) and there exists \(\varepsilon\in(0,1/2)\) with \(\varepsilon\le b_n\le1-\varepsilon\) for all \(n\), any two interior solutions driven by the same input satisfy
\[
 \left|\log\frac{1-x_n}{x_n}-\log\frac{1-\widetilde x_n}{\widetilde x_n}\right|\longrightarrow0.
\]
 For \(a<8\), this synchronization is eventually exponential. In addition, **for every \(a>0\)** under the stated bounded-input condition (without assuming \(a\le8\)), each interior trajectory satisfies
\[
 \frac1N\sum_{n=0}^{N-1}(x_n-b_n)\longrightarrow0.
\]
 Thus input-average calibration can persist even outside the global synchronization regime.

3. **Only nonhyperbolic periodic input and its sharp law.** At \(a=8\), the only periodic input giving a unit-modulus multiplier at its entrained solution is the constant input \(b_n\equiv1/2\). For this exceptional input, if an interior initial condition never iterates exactly to \(x=1/2\), then
\[
 \lim_{n\to\infty}\sqrt n\left|\log\frac{1-x_n}{x_n}\right|=\sqrt3,
 \qquad
 \lim_{n\to\infty}\sqrt n\,|x_n-1/2|=\frac{\sqrt3}{4}.
\]
 Initial conditions that reach \(1/2\) in finitely many steps remain there and have both limits equal to zero.

4. **Sharpness of the forcing-independent threshold.** No number larger than \(8\) can replace \(8\) in item 1 for all periodic inputs: for every \(a>8\), the constant input \(b_n=1/2\) has a repelling interior fixed point and an attracting nontrivial two-cycle (the latter is already known in the autonomous theory).

## Assumptions and scope

The updates are *ordered in time*, with \(b_n\) prescribed independently of the initial state. The constant \(a\) is the normalized learning intensity, and \(b_n\) is the changing target equilibrium of a two-strategy game. No assertion is made for initial values at the boundary \(x_0\in\{0,1\}\), which remain fixed under the algebraic update. In the aperiodic synchronization and calibration statements, \(\varepsilon\) is fixed and independent of \(n\). Here 'eventually exponential' means that for each specified input and initial state there are constants \(C>0\) and \(\rho\in(0,1)\) with phase error at most \(C\rho^n\) for all sufficiently large \(n\); it is not a common convergence rate uniform over all inputs.

Write
\[
 y=\log\frac{1-x}{x},\quad X(y)=\frac{1}{1+e^y},\quad
 g_{a,b}(y)=y+a(X(y)-b)=s_a(y)-ab,
 \quad s_a(y)=y+aX(y).
\]
The logistic change of coordinates is a smooth bijection from \((0,1)\) onto \(\mathbb R\), and it conjugates every update to \(y_{n+1}=g_{a,b_n}(y_n)\).

## Proof

**Step 1: common strict distance decrease at the sharp endpoint.** Differentiation gives
\[
 s_a'(y)=1-\frac a4\operatorname{sech}^2(y/2).
\]
For \(0<a\le8\), one has \(-1\le s_a'(y)<1\) everywhere. Equality \(s_a'(y)=-1\) occurs only when \(a=8\) and \(y=0\). In particular, for distinct finite \(u,v\), integration on the interval between them gives
\[
 |s_a(u)-s_a(v)|<|u-v|.
\]
The affine input term \(-ab\) cancels when two solutions are compared. Hence every one-step driven map is strictly distance-decreasing between distinct logit states; its Lipschitz constant need not be strictly less than one globally on \(\mathbb R\).

**Step 2: periodic solution and global phase attraction.** For a prescribed \(m\)-periodic input, define the return map
\[
 G=g_{a,b_{m-1}}\circ\cdots\circ g_{a,b_0}.
\]
As \(y\to+\infty\), every intermediate finite iterate is \(y+O(1)\) and hence
\[
 G(y)-y\longrightarrow-a\sum_{j=0}^{m-1}b_j<0.
\]
Likewise, as \(y\to-\infty\),
\[
 G(y)-y\longrightarrow a\sum_{j=0}^{m-1}(1-b_j)>0.
\]
Continuity gives a fixed point \(y^*\in\mathbb R\). Step 1 implies \(|G(y)-G(z)|<|y-z|\) for \(y\ne z\), so the fixed point is unique. For any other starting value, the distance \(|G^k(y)-y^*|\) strictly decreases. If it had a positive limit, a convergent subsequence in the compact interval centered at \(y^*\), together with continuity and strict distance decrease, would contradict that limit. Thus \(G^k(y)\to y^*\). Continuity of the finite phase maps proves attraction at all intermediate phases. Summing the logit increments over the return orbit yields
\[
 0=y_m^*-y_0^*=a\sum_{j=0}^{m-1}(x_j^*-b_j),
\]
which is the stated exact phase-average law.

**Step 3: rates and exceptional forcing.** The derivative of the return map on the periodic orbit is
\[
 \Lambda=\prod_{j=0}^{m-1}\left(1-\frac a4\operatorname{sech}^2(y_j^*/2)\right).
\]
For \(a<8\), every factor lies strictly within the open unit interval in absolute value. For \(a=8\), absolute value one is possible only if every phase satisfies \(y_j^*=0\), equivalent by the recurrence to every \(b_j=1/2\). Thus \(|\Lambda|<1\) in all the other cases. The classical one-dimensional local contraction estimate for the return map, combined with the already established global convergence, proves eventual exponential attraction at every phase.

**Step 4: arbitrary bounded-input synchronization and calibration.** Choose \(B>0\) so large that \(X(y)<\varepsilon/2\) for \(y>B\) and \(X(y)>1-\varepsilon/2\) for \(y<-B\). Then
\[
 y_{n+1}-y_n\le-a\varepsilon/2\quad(y_n>B),\qquad
 y_{n+1}-y_n\ge a\varepsilon/2\quad(y_n<-B),
\]
and \(|y_{n+1}-y_n|\le a\). Therefore every orbit eventually enters and remains in the common compact interval \([-B-a,B+a]\). For two such orbits, their logit separation decreases strictly by Step 1. If its limit were some \(d>0\), compactness would give a uniform contraction factor strictly below one on pairs separated by at least \(d/2\), a contradiction. Consequently the separation tends to zero. When \(a<8\), the maximum of \(|s_a'|\) on this compact interval is strictly below one, yielding eventual exponential synchronization. Finally, telescoping gives for every \(a>0\)
\[
 \frac1N\sum_{n=0}^{N-1}(x_n-b_n)=\frac{y_N-y_0}{aN}.
\]
Boundedness of \(y_N\) proves calibration, without any synchronization hypothesis.

**Step 5: the unique critical law.** When \(a=8\) and \(b_n\equiv1/2\), the conjugated map is odd and satisfies
\[
 g(y)=y-4\tanh(y/2)=-y+\frac{y^3}{6}-\frac{y^5}{60}+O(y^7).
\]
Step 2 already proves every orbit tends to zero. Excluding initial points whose trajectory hits zero, the absolute values \(r_n=|y_n|\) are positive and, for all sufficiently large \(n\), satisfy
\[
 r_{n+1}=r_n-\frac{r_n^3}{6}+O(r_n^5),\qquad
 \frac1{r_{n+1}^2}-\frac1{r_n^2}=\frac13+O(r_n^2).
\]
Because \(r_n\to0\), Cesàro averaging the last identity yields \(r_n^{-2}/n\to1/3\), proving \(\sqrt n\,r_n\to\sqrt3\). The Taylor expansion \(X(y)=1/2-y/4+O(y^3)\) supplies the second limit. If zero is hit, all subsequent iterates vanish and the limits are zero. The exceptional set is countable: each iterate of the nonconstant analytic map \(g\) has a discrete (and hence countable) set of zeros.

**Step 6: threshold sharpness.** For the admissible constant signal \(b_n=1/2\), the fixed point \(y=0\) has derivative \(1-a/4\). When \(a>8\), its magnitude exceeds one. In a neighborhood of zero the map is expanding in distance from zero; any orbit converging to zero must therefore hit it in finite time. Since an iterate of this nonconstant real-analytic map has only a countable zero set, some interior trajectories do not converge to zero. Consequently, a universal forcing-independent global entrainment theorem beyond \(8\) is false. The existence and attraction of the corresponding symmetric two-cycle are previously established in Chotibut–Falniowski–Misiurewicz–Piliouras, Theorem 3.9; they are cited as a known sharpness example, not claimed as new here. This completes the proof.

## Verification

The standalone program `verify.py` uses symbolic algebra for the exact conjugacy, derivative, and critical Taylor coefficients; high-precision numerical return-map solutions for four nonconstant periodic inputs; 24 independent initializations for convergence; three critical-relaxation trajectories; four known supercritical symmetric cycles; and three bounded aperiodic inputs for synchronization. Execute with `python verify.py` in an environment with `sympy` and `mpmath`. Its printed `VERIFY_OK` output is a diagnostic of those computations, not a proof for all inputs, all periods, or arbitrarily long times. For the diagnostic example \(a=8\), \(b_0=1/4\), \(b_1=3/4\), the computed unique phase states are approximately \(0.9406126803877602\) and \(0.0593873196122398\), with return multiplier \(0.3059376113997673\). All infinite-quantifier assertions follow from the analytic proof above, not from finite sampling.

## Relationship to prior work

Kryzhevich and Zhang (2026, Sections 4–6) develop stationary-parameter replicator maps and invariant orbit means, and explicitly use the logit conjugacy \(g_{a,b}\). Chotibut, Falniowski, Misiurewicz and Piliouras (2018 preprint, Theorems 3.4 and 3.9) prove the autonomous mean-value law, the symmetric \(a=8\) fixed-point convergence threshold, and the supercritical attracting two-cycle. These autonomous results are **not** presented as original here. The new assessed statement concerns *arbitrary periodic target sequences*, the sharp input-independent global threshold including endpoint, the uniqueness of the nonhyperbolic forcing, input-driven synchronization, and the explicit critical relaxation coefficient.

Falniowski and Mertikopoulos (2024) examine distinct autonomous replicator and exponential-weights discretizations, and Vlatakis-Gkaragkounis et al. (2023 preprint; 2026 revision) study genuinely nonautonomous *adaptive learning rates* for fixed congestion-game parameters, principally in the large-rate chaotic regime. Neither treatment gives the present prescribed time-varying equilibrium-target theorem. General contraction and entrainment principles motivate the proof; classical strict contraction accounts for the subcritical portion, but does not alone give the attained nonuniform endpoint and its sharp power-law exception. Literature priority has been assessed against these sources and relevant research records, not exhaustively certified.

## Limitations

The global synchronization theorem concerns the scalar two-strategy family with a **fixed** \(a\) and exogenously prescribed \(b_n\). It does not cover coupled multiagent networks, adaptive step sizes, discontinuous state feedback, or arbitrary unconstrained target sequences approaching \(0\) or \(1\). At \(a=8\), arbitrary aperiodic bounded forcing is only proved to synchronize, without a uniform exponential rate; exponential attraction is proved for periodic nonexceptional forcing. The critical law excludes finite preimages of the equilibrium. The universality and novelty assertions are relative to the explicitly inspected literature; no independent external scientific audit has been performed.

## References

1. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1, publicly submitted 2026-03-21, https://arxiv.org/abs/2603.20685.
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1, publicly submitted 2018-07-18, https://arxiv.org/abs/1807.06831.
3. F. Falniowski and P. Mertikopoulos, *On the discrete-time origins of the replicator dynamics: From convergence to instability and chaos*, arXiv:2402.09824v1, publicly submitted 2024-02-15, https://arxiv.org/abs/2402.09824.
4. E.-V. Vlatakis-Gkaragkounis, K. Metaxas, L. Flokas and G. Piliouras, *Chaos persists in large-scale multi-agent learning despite adaptive learning rates*, arXiv:2306.01032 (first submitted 2023-06-01; revision 2026-10-17), https://arxiv.org/abs/2306.01032.
