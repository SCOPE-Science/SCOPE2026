# Universal optimality of uniform observation precision in scalar Kalman filtering

## Finding

**Theorem (asymptotic lower bound and strict periodic optimizer).** Consider a scalar Gaussian state model with fixed real state multiplier \(a\), strictly positive process-noise variance \(q\), and identity observations whose nonnegative finite precision \(u_n\) may vary with time, with precision zero interpreted as no observation. Write \(s=a^2\). Given any positive initial posterior variance, the exact filtering posterior covariances obey
\[
P_n=\frac{sP_{n-1}+q}{1+u_n(sP_{n-1}+q)},\qquad n\ge1.
\]
For every deterministic precision schedule \(u_n\ge0\) satisfying
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N u_n=b>0,
\]
its time-average posterior error has the sharp bound
\[
\liminf_{N\to\infty}\frac1N\sum_{n=1}^N P_n\ \ge\ p_b
:=\frac{2q}{bq+1-s+\sqrt{(bq+1-s)^2+4bsq}}.
\]
The constant schedule \(u_n=b\) attains equality as a limit, including when \(s\ge1\). For every positive integer period \(m\), among all nonnegative \(m\)-periodic precision schedules of mean \(b\), the **unique** minimizer of the average variance over the attracting periodic covariance orbit is the constant schedule. Equality holds precisely when all the \(m\) allocated precisions equal \(b\).

## Assumptions and scope

The state and observation model is \(X_n=aX_{n-1}+W_n\) and \(Y_n=X_n+V_n\) when observed. The centered Gaussian process noises \(W_n\) are mutually independent with variance \(q>0\). Observation noise at step \(n\) is independent and Gaussian with variance \(1/u_n\) when \(u_n>0\). Setting \(u_n=0\) means no measurement, rather than a Gaussian with infinite variance. Initial state uncertainty is Gaussian with finite posterior variance \(P_0>0\), independent of future noises. Time and resource units are fixed; the cost is **linear in observation precision** \(u_n\), not the number of activated readings, mutual information, or communication bits. State coefficient \(a\) can be negative, zero, stable or unstable. For the nonperiodic conclusion the average precision need only converge to a strictly positive finite constant; no bound on the individual precisions and no stationarity assumption is imposed. Uniqueness is asserted for fixed-period minimizers, not for arbitrary nonperiodic schedules asymptotically equivalent to constant allocation.

## Proof

**1. Scalar precision balance.** Define
\[
g(p)=\frac1p-\frac1{sp+q}\qquad (p>0).
\]
Direct inversion of the Kalman update gives
\[
u_n=\frac1{P_n}-\frac1{sP_{n-1}+q}.
\]
Consequently every trajectory satisfies the exact telescoping identity
\[
\sum_{n=k+1}^N u_n
=\sum_{n=k+1}^N g(P_n)
+\frac1{sP_N+q}-\frac1{sP_k+q},
\]
for all integers \(N>k\ge0\). Since \(q>0\), the end correction has absolute value no greater than \(1/q\), uniformly in the schedule and horizon. In particular, the long-run averages of allocated precision and of \(g(P_n)\) coincide whenever either exists.

**2. The convex-decreasing domain.** Differentiation yields
\[
g'(p)=-\frac1{p^2}+\frac{s}{(sp+q)^2},\qquad
 g''(p)=\frac2{p^3}-\frac{2s^2}{(sp+q)^3}.
\]
If \(s\ge1\), then \(sp+q>\sqrt{s}\,p\) and \(sp+q>s^{2/3}p\), so \(g'<0\) and \(g''>0\) on \((0,\infty)\). For \(s=0\), these inequalities are immediate from \(g(p)=1/p-1/q\). If \(0<s<1\), both strict inequalities hold at every \(0<p\le q/(1-s)\), since \(sp+q\ge p>\sqrt{s}\,p\) and \(sp+q\ge p>s^{2/3}p\). By continuity they hold on a slightly larger interval \((0,B)\), for some \(B>q/(1-s)\). Every posterior trajectory satisfies
\[
0<P_n\le s^nP_0+q\frac{1-s^n}{1-s},
\]
and hence lies in \((0,B)\) for all sufficiently large \(n\). Thus every trajectory eventually enters an interval on which \(g\) is strictly decreasing and strictly convex. This also includes the case \(s=0\).

**3. Arbitrary Cesàro precision schedules.** Choose the tail index \(k\) from Step 2. Jensen's inequality on the tail, and Step 1, give
\[
g\!\left(\frac1{N-k}\sum_{n=k+1}^NP_n\right)
\le \frac1{N-k}\sum_{n=k+1}^Ng(P_n)
=\frac1{N-k}\sum_{n=k+1}^Nu_n+O((N-k)^{-1})=b+o(1).
\]
Here the same estimate holds with \(k=0\) for \(s\ge1\). On the relevant monotonicity interval, \(g\) decreases continuously from \(+\infty\) down through every positive value \(b\), and \(g(p_b)=b\). Therefore, for any \(\varepsilon>0\), eventually the displayed tail average cannot be less than \(p_b-\varepsilon\). The finitely many omitted positive covariances do not lower the full Cesàro liminf. This proves the universal lower bound.

**4. Sharp constant allocation.** With \(u_n=b\), the update \(F_b(p)=(sp+q)/(1+b(sp+q))\) is increasing, maps positive arguments into a bounded positive interval, and has a unique positive fixed point. Inversion at a fixed point gives \(g(p)=b\), or equivalently
\[
bs p^2+(bq+1-s)p-q=0.
\]
Its positive solution is \(p_b\) above, including the \(s=0\) boundary by continuity. The iteration converges monotonically toward this fixed point from either side, establishing attainment of the limit average.

**5. Existence and strict uniqueness for periodic allocations.** Fix \(m\ge1\) and a nonnegative period \((u_1,\ldots,u_m)\) with sum \(mb>0\). Each map \(F_u(p)=(sp+q)/(1+u(sp+q))\) is continuous, nondecreasing and concave on \([0,\infty)\). Their one-period composition \(F=F_{u_m}\circ\cdots\circ F_{u_1}\) retains these properties, satisfies \(F(0)>0\), and is bounded above because at least one \(u_i\) is positive. For every \(0<x<y\), strict positivity of \(F(0)\) and concavity imply \(F(x)/x>F(y)/y\). Thus \(F(p)=p\) has exactly one positive solution, and iterating the increasing map converges to it from any initial positive point. There is therefore a unique attracting covariance cycle \((P_1,\ldots,P_m)\). On this cycle \(\max_iP_i\le q/(1-s)\) when \(s<1\), by choosing an index of maximal variance and comparing it with its predecessor. Step 2 gives strict convexity and monotonicity of \(g\) over its entire range. The exact cyclic telescoping identity and Jensen yield
\[
b=\frac1m\sum_{i=1}^m g(P_i)
\ge g\!\left(\frac1m\sum_{i=1}^m P_i\right),
\]
so the mean posterior variance is at least \(p_b\). Since \(g\) is **strictly** convex, equality forces \(P_1=\cdots=P_m=p_b\); inversion of the step updates then forces \(u_i=g(p_b)=b\) for all \(i\). Conversely, the constant precision schedule achieves equality. This completes the proof.

## Verification

`check.py` runs without third-party packages under Python 3. It checks exact rational rearrangements of \(g\), derivative signs on the claimed domains, the telescoping identity, the period-two example, and numerical time-periodic Riccati solutions across stable, marginal and unstable multipliers, including periods with skipped observations. The recorded run produced 7,609 passing assertions. These finite checks are diagnostics, **not** a substitute for Steps 1–5 of the proof.

For a concrete example, take \(s=2\), \(q=1\), and alternating precisions \((u_1,u_2)=(0,1)\). The attracting posterior variances are exactly \(1+\sqrt3\) and \(\sqrt3/2\), giving mean \(\frac12+\frac{3\sqrt3}{4}\approx1.799038106\), whereas constant precision \(b=1/2\) gives \(p_b=(1+\sqrt{17})/4\approx1.280776406\). The intermittent design thus raises long-run posterior mean-square error by approximately 40.46% under the **same mean precision cost**.

To reproduce, run `python3 check.py`. Numerical tolerances are in the script; proof covers the full infinite parameter ranges, not just tested samples.

## Relationship to prior work

Das and Bhattacharya (2021) optimize sensing precision under a specified Kalman filtering error bound, including a periodic steady-state lifted formulation. Their published Theorem 2 is based on a potentially conservative covariance upper bound, as their Remark 5 explicitly notes. It does **not** state the time-average posterior minimization and equality classification under a fixed average precision budget derived here. Aspeel, Legay, Jungers and Macq (2021) optimize the placement of a finite number of fixed-noise measurements for mean *prediction* error on finite horizons, and examine a number-versus-noise tradeoff; discrete measurement counts and prediction error differ from continuous precision allocation and posterior error. Shakeri, Pattipati and Kleinman (1995) consider a general finite-horizon resource allocation with inverse-accuracy costs, but the accessible abstract does not determine this infinite-horizon exact uniform-optimality theorem. Earlier infinite-horizon sensor scheduling results typically select among discrete sensors and derive structural/approximation properties rather than a continuous-precision equality case.

The Kalman update, scalar information identity, convexity, and Jensen inequality are standard methods; the claim is the complete optimality theorem for this explicitly defined precision budget and error criterion, not discovery of these ingredients.

## Limitations

The result does not establish optimal allocation for finite horizons, time-varying state coefficients, nonlinear or vector-valued systems, observation *count* constraints, prediction-error instead of posterior-error objectives, logarithmic or nonlinear sensor costs, or stochastic resource policies correlated with observations. Periodic equality is uniquely characterized; asymptotic equality for nonperiodic perturbations is not. A possible unlocated equivalent statement in earlier measurement scheduling/control literature remains a priority for independent bibliographic validation.

## References

1. N. Das and R. Bhattacharya, *Optimal Sensor Precision for Multi-Rate Sensing for Bounded Estimation Error*, public manuscript uploaded May 29, 2021, DOI 10.13140/RG.2.2.22073.08806; arXiv:2106.06906 (June 2021). https://www.researchgate.net/publication/351955056_Optimal_Sensor_Precision_for_Multi-Rate_Sensing_for_Bounded_Estimation_Error
2. A. Aspeel, A. Legay, R. M. Jungers and B. Macq, *Optimal measurement budget allocation for Kalman prediction over a finite time horizon by genetic algorithms*, EURASIP Journal on Advances in Signal Processing 2021, article 39, published July 16, 2021. https://doi.org/10.1186/s13634-021-00732-8
3. M. Shakeri, K. R. Pattipati and D. L. Kleinman, *Optimal measurement scheduling for state estimation*, IEEE Transactions on Aerospace and Electronic Systems 31 (1995), 716–729. https://doi.org/10.1109/7.381919
4. *On the Optimal Solutions of the Infinite-Horizon Linear Sensor Scheduling Problem*, IEEE Transactions on Automatic Control 59 (2014), 2825–2830. https://doi.org/10.1109/TAC.2014.2314222
5. V. Zinage, T. Tanaka and V. Ugrinovskii, *Optimal Sensor Gain Control for Minimum-Information Estimation of Continuous-Time Gauss-Markov Processes*, arXiv:2109.13854 (2021). https://arxiv.org/abs/2109.13854
