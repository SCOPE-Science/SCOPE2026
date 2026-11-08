# Three distinct weak-reset risk responses for simultaneous Brownian searchers

## Finding
For simultaneous Poisson resetting of an ensemble of independent Brownian target searchers, the first-passage mean, variance and squared coefficient of variation can respond in three *different* ways at weak reset rate. For \(N=7,8,9\), an infinitesimal positive rate increases the mean but decreases both absolute variance and squared relative dispersion. For \(N=10,11\), it increases mean and variance but decreases squared relative dispersion. For \(N=12\), all three increase. These are strict one-sided derivative statements at zero rate and hence hold for every sufficiently small positive rate; no assertion about all larger populations or globally optimal rates is made.

## Assumptions and scope
Let \(N\in\{7,8,9,10,11,12\}\). Independent one-dimensional particles, initially at \(x_0>0\), follow \(dX_i=\sqrt{2D}\,dB_i\) with \(D>0\), are absorbed at the target \(0\), and stop the search at the first absorption. At times of one independent rate-\(r\) Poisson clock, all surviving walkers are reset *simultaneously* to \(x_0\). Put \(t_0=x_0^2/(4D)\), \(q=rt_0\), and \(T_q\) equal to the first-hit time divided by \(t_0\). Write \(M(q)=\mathbb E[T_q]\), \(V(q)=\operatorname{Var}(T_q)\) and \(C(q)=V(q)/M(q)^2\). Derivatives below are right derivatives at \(q=0\). This corresponds to the simultaneous (protocol B), not the independently reset (protocol A), ensemble.

Define three baseline raw moments for the no-reset minimum search time:
\[
m_k=2k\int_0^\infty u^{-2k-1}\operatorname{erf}(u)^N\,du,\qquad k=1,2,3.
\]
They are finite for \(N>6\). Define
\[
A_N=m_1^2-\tfrac12m_2,\quad B_N=-\tfrac23m_3+3m_1m_2-2m_1^3,\quad G_N=m_2^2-\tfrac23m_1m_3.
\]
Then \(M'(0)=A_N\), \(V'(0)=B_N\), and \(C'(0)=G_N/m_1^3\). Their strict sign triple \((A_N,B_N,G_N)\) is \((+,-,-)\) at \(N=7,8,9\), \((+,+,-)\) at \(N=10,11\), and \((+,+,+)\) at \(N=12\).

## Proof
The reflection principle gives the individual no-hit probability \(\operatorname{erf}(x_0/\sqrt{4Dt})\). Independence makes the no-reset minimum-time survival \(S_N(t)=\operatorname{erf}(t^{-1/2})^N\) in units \(t_0\). Therefore \(m_k=k\int_0^\infty t^{k-1}S_N(t)\,dt\); the substitution \(u=t^{-1/2}\) gives the displayed integral. As \(t\to\infty\), \(S_N(t)=O(t^{-N/2})\), establishing the first three moment assumptions for \(N>6\).

Set \(F(q)=\int_0^\infty e^{-qt}S_N(t)\,dt\). The event that a search completes before the next common reset regenerates all walkers, and the standard renewal identity for the Laplace transform of reset survival is
\[
\widehat S_q(s)=\frac{F(q+s)}{1-qF(q+s)}.
\]
Consequently
\[
M(q)=\frac{F(q)}{1-qF(q)},\qquad V(q)=\frac{-2F'(q)-F(q)^2}{(1-qF(q))^2},\qquad C(q)=-\frac{2F'(q)}{F(q)^2}-1.
\]
The third no-reset moment permits differentiating at \(q=0\) because \(F(0)=m_1\), \(F'(0)=-m_2/2\) and \(F''(0)=m_3/3\). Elementary differentiation gives the three derivative identities.

For the strict signs, the included reproducible `check.py` computes conservative enclosures of all eighteen integrals. On \([0,4]\), partition into 40,000 equal cells, enclosing the error function by a 110-term alternating Taylor approximation with absolute allowance \(10^{-40}\). Because \(\operatorname{erf}\) is monotone and \(u^{-2k-1}>0\), use the left and right endpoint error-function bounds against the exact integration weights \(u_{i}^{-2k}-u_{i+1}^{-2k}\) for every cell away from zero. The first cell has a nonnegative contribution bounded above by \(2k(2/\sqrt\pi+10^{-40})^N h^{N-2k}/(N-2k)\). On \([4,\infty)\), the bound \(0<\operatorname{erfc}(4)<2\times10^{-8}\) gives bounds \((1-2N\times10^{-8})4^{-2k}\) and \(4^{-2k}\) on the tail integral. Interval arithmetic then bounds \(A_N,B_N,G_N\) by the formulas in the checker, and every resulting interval has the claimed strict sign. This establishes all sign claims without approximating an infinite integral solely by a finite numerical sample.

## Verification
Run `python check.py` using Python 3's standard library in the folder containing `check.py`; it regenerates `enclosures.json` and asserts every strict sign. The recorded enclosure outputs bound the response coefficients as follows, with each pair denoting the verified lower and upper enclosure (rounded outward for display):

| \(N\) | \(A_N\) | \(B_N\) | \(G_N\) |
|---|---|---|---|
| 7 | [0.08486, 0.08586] | [-2.97373, -2.89450] | [-2.89446, -2.82069] |
| 8 | [0.13170, 0.13236] | [-0.54316, -0.53584] | [-0.57111, -0.56561] |
| 9 | [0.14287, 0.14335] | [-0.09345, -0.08982] | [-0.15912, -0.15687] |
| 10 | [0.14239, 0.14278] | [0.03120, 0.03354] | [-0.04241, -0.04117] |
| 11 | [0.13789, 0.13821] | [0.06980, 0.07148] | [-0.00199, -0.00119] |
| 12 | [0.13213, 0.13240] | [0.08029, 0.08159] | [0.01328, 0.01384] |

The JSON artifact records the unrounded interval endpoints. The checker evaluates a proved finite quadrature enclosure, rather than claiming finite experiments prove all parameters.

## Relationship to prior work
Biroli, Majumdar and Schehr (2023) develop precisely the same simultaneous-reset target-search process and determine its *mean*-optimality transition at \(N_c\approx6.3555864\) (protocol B). Their mean calculation does not assert these variance and relative-dispersion thresholds. Reuveni (2015/2016) supplies universal first-passage restart fluctuation identities and the coefficient-of-variation condition at mean-optimal rate, but those general formulas alone do not determine the particular population-dependent sign table. Linn and Lawley (2023) investigate high-frequency resetting limits of moments, not these zero-rate signs. The contribution here is the *jointly certified*, model-specific three-way local risk classification, not a new renewal theorem.

## Limitations
The sign classifications are proved only for the six displayed integer populations and sufficiently small positive resetting rate. They do not establish monotonicity for all rates, a universal asymptotic in population, or the exact transition at a noninteger \(N\). Other moment inequalities or further prior literature may yield equivalent statements; publication priority is not independently established. The mathematical result depends on the simultaneous-reset protocol and instantaneous, cost-free resetting.

## References
- M. Biroli, S. N. Majumdar, G. Schehr, *Critical number of walkers for diffusive search processes with resetting* (first public 2023-03-31), https://arxiv.org/abs/2303.18012.
- S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal* (first public 2015), https://arxiv.org/abs/1512.01600.
- S. Linn and S. D. Lawley, *First passage times under frequent stochastic resetting* (first public 2023), https://arxiv.org/abs/2302.05409.
