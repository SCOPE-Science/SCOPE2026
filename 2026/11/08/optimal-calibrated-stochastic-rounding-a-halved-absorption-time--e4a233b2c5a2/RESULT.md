# Optimal calibrated stochastic rounding: a halved absorption-time logarithm and a Gaussian transition

## Finding

For each integer \(M\ge2\), apply exact gradient descent to \(f(x)=x^2/2\) with stepsize \(1/M\) at integer states \(k\in\{0,1,\ldots,M\}\), followed by stochastic rounding of \((1-1/M)k\) to its neighboring integers. Write \(b_k\) for a nonnegative, state-dependent increment of the probability of rounding *down*, so the downward probability is \(p_k=k/M+b_k\). For a fixed total transition total-variation budget \(0<B<(M-1)/2\), namely \(\sum_{k=1}^M b_k\le B\) and \(0\le b_k\le1-k/M\), the unique policy minimizing expected time to reach zero from \(M\) is

\[
p_k^*=\max\{k/M,c\},\qquad b_k^*=(c-k/M)_+,
\]
where \(c\in(1/M,1)\) is uniquely determined by \(\sum_{k=1}^M(c-k/M)_+=B\). If \(K=\#\{k:k/M<c\}\), it has the finite, exactly computable form

\[
c=\frac{B+K(K+1)/(2M)}{K},\quad
K/M\le c\le(K+1)/M,\quad
\mathbb E[T_M^*]=\frac Kc+M(H_M-H_K).
\]
At a tie \(c=(K+1)/M\), the same policy is obtained by either neighboring active-set indexing. Here \(H_0=0\), and \(H_j=\sum_{i=1}^j1/i\).

For every fixed \(B>0\), as integers \(M\to\infty\) through values satisfying \(B<(M-1)/2\),

\[
c=\sqrt{2B/M}\,(1+o(1)),\qquad K=\sqrt{2BM}\,(1+o(1)),
\]
\[
\mathbb E[T_M^*]=M\!\left(\tfrac12\log M+1-\tfrac12\log(2B)+o(1)\right),
\qquad\operatorname{Var}(T_M^*)\sim\sqrt{2/B}\,M^{3/2},
\]
\[
\frac{T_M^*-\mathbb E T_M^*}{M^{3/4}}
\ \Longrightarrow\ \mathcal N\!\left(0,\sqrt{2/B}\right).
\]
The variance parameter in \(\mathcal N(0,v)\) is \(v\), not the standard deviation. The **unbiased** scheme has \(p_k=k/M\) and \(\mathbb E T_M=M H_M\sim M\log M\); it is exactly the classical coupon-collector completion time, whose order-\(M\) Gumbel fluctuation law is known prior work. A fixed total calibration budget therefore halves the leading logarithmic expected runtime and changes the centered fluctuation scale from order \(M\) to order \(M^{3/4}\) with a Gaussian limit.

## Assumptions and scope

The state space is precisely the nonnegative integer set \(\{0,\ldots,M\}\); the initial state is \(X_0=M\); state zero is absorbing. All rounding choices at successive steps are conditionally independent given current states. At \(k>0\), the real proposal is \((1-1/M)k=k-k/M\), which lies in \([k-1,k)\). Unbiased stochastic rounding chooses \(k-1\) with probability \(k/M\). The chosen policy instead chooses \(k-1\) with probability \(p_k=k/M+b_k\) and otherwise remains at \(k\). The signed bias is always directed toward the minimizer. The total-variation distance between the two binary transition distributions at state \(k\) is exactly \(b_k\); \(B\) is an **aggregate statewise calibration budget**, not a per-iteration error tolerance or an average visited-state cost. The upper bound on \(B\) excludes the trivial policy that always rounds down. The asymptotics keep \(B\) fixed independently of \(M\).

## Proof

**Exact waiting-time decomposition.** Each positive state \(k\) can only hold or move to \(k-1\); hence the time spent at \(k\) before leaving is \(G_k\sim\operatorname{Geom}(p_k)\), on \(\{1,2,\ldots\}\). Separate sequences of independent rounding coins give independent \(G_1,\ldots,G_M\), so \(T_M=\sum_{k=1}^M G_k\). Therefore, for every admissible allocation,
\[
\mathbb E T_M=\sum_{k=1}^M\frac1{p_k},\qquad
\operatorname{Var}(T_M)=\sum_{k=1}^M\frac{1-p_k}{p_k^2}.
\]
In particular, the unbiased expected time is \(M H_M\); its waiting-time decomposition matches the classical coupon collector with \(k\) unseen types remaining.

**Finite-dimensional optimality, including boundaries.** Write \(a_k=k/M\). Since \(p_M=1\) is fixed, the objective \(F(b)=\sum_k(a_k+b_k)^{-1}\) is strictly convex in the free coordinates \(b_1,\ldots,b_{M-1}\) over \(0\le b_k\le1-a_k\). Its derivatives are strictly negative, so an optimizer for \(0<B<(M-1)/2\) spends the full budget. At an interior free coordinate, the Lagrange multiplier condition \(-1/p_k^2+\lambda=0\) forces \(p_k=c=\lambda^{-1/2}\). At the lower bound \(b_k=0\), the KKT inequality forces \(a_k\ge c\). All \(a_k<c\) become active, and none reaches the upper bound, because \(c<1\). This constructs the displayed water-filling policy, which is feasible and unique by strict convexity. The continuous strictly increasing budget function \(g(c)=\sum_k(c-a_k)_+\) grows from zero at \(c=1/M\) to \((M-1)/2\) at \(c=1\). Thus each admissible \(B\) determines one \(c\). Writing \(K=\#\{a_k<c\}\), the budget identity gives the finite formula for \(c\), and summing its \(K\) equal hazards and remaining baseline hazards gives the exact mean.

**Fixed-budget asymptotics.** The threshold condition gives \(K=Mc+O(1)\). The budget identity rewrites as
\[
B=Kc-\frac{K(K+1)}{2M}=\frac{K^2}{2M}+O(K/M),
\]
so \(K\sim\sqrt{2BM}\) and \(c\sim\sqrt{2B/M}\). Consequently \(K/c=M+o(M)\) and \(H_M-H_K=\log(M/K)+o(1)\), proving the mean expansion. For the variance, the \(K\) equal-hazard states contribute
\[
K\frac{1-c}{c^2}\sim \frac{M^{3/2}}{\sqrt{2B}},
\]
while the remainder contributes
\[
\sum_{k=K+1}^M\frac{1-k/M}{(k/M)^2}
=M^2\sum_{k=K+1}^M\frac1{k^2}-M\sum_{k=K+1}^M\frac1k
\sim\frac{M^{3/2}}{\sqrt{2B}}.
\]
The sum proves the variance coefficient. The upper tail term \(M(H_M-H_K)\) is lower order than \(M^{3/2}\).

**Gaussian fluctuations.** Center the independent waiting times \(G_k-1/p_k\). A geometric variable with success probability \(p\in(0,1]\) satisfies \(\mathbb E|G-\mathbb E G|^3\le C p^{-3}\) with a universal finite \(C\); e.g. bound the absolute centered third moment by a fixed multiple of \(\mathbb E G^3+(\mathbb EG)^3\), and use the exact geometric third moment. For the water-filled hazards,
\[
\sum_{k=1}^M p_k^{-3}=Kc^{-3}+M^3\sum_{k=K+1}^M k^{-3}=O_B(M^2).
\]
The variance is asymptotic to a strictly positive constant times \(M^{3/2}\), hence its three-halves power has order \(M^{9/4}\). The Lyapunov ratio tends to zero as \(O_B(M^{-1/4})\); the Lyapunov central limit theorem and the variance asymptotic prove the stated distributional limit. No independent-normality or finite-test extrapolation is assumed.

## Verification

The accompanying standalone file `verify.py` uses only standard Python fractions and elementary arithmetic. It independently checks the first-step Markov moment recurrence against the sum of geometric waiting times; exact active-set solutions, feasibility and budgets for several finite \(M\); exhaustive small rational-grid competitor comparisons; the unbiased coupon-collector CDF through exact inclusion-exclusion; and comparisons against the derived asymptotic coefficients. Its captured execution output is `check_output.txt`. All **422 assertions passed**. This checks numerical and algebraic instances; the infinite optimality and limit laws are established by the proof above, not by enumeration.

For example, with \(M=100\) and \(B=1/2\), the exact optimum has \(K=10\), \(c=21/200\), and \(\mathbb E T_{100}^*\approx321.0790216052\). Distributing the same total budget uniformly over the \(99\) free states gives \(\mathbb E T_{100}\approx457.4024198869\); the unbiased mean is \(100H_{100}\approx518.737751764\). These computations are exact rational sums before final decimal display.

## Relationship to prior work

Stochastic neighboring-grid rounding, its signed bias toward descent, and convergence bounds under floating- and fixed-point arithmetic are developed in Xia, Massei, Hochstenbach and Koren (2022), and Xia, Hochstenbach and Massei (2023). This result uses those familiar rounding principles but optimizes a **state-dependent collection of signed-bias probabilities under one aggregate total-variation budget**, with an exact hitting-time objective and a fixed-budget Gaussian limit. Their investigated convergence bounds do not supply this allocation or the limiting law. The unbiased baseline is the classical coupon-collector process; its exact harmonic mean and Gumbel limit are not novel claims. The Lagrange-multiplier water-filling *technique* is classical; the contribution is the optimal rounding calibration and its nontrivial scaling/fluctuation transition, not invention of KKT theory.

## Limitations

This is a deliberately finite-grid, scalar, noiseless quadratic with monotone nonnegative iterates. The budget is an aggregate of **possible statewise** total-variation deviations, not the expected cumulative perturbation along a trajectory, a bound on coordinatewise floating-point relative error, or a guarantee for a general implementation of low-precision arithmetic. It does not give a convergence theorem for arbitrary multidimensional objectives. Mathematically equivalent results in specialist optimal controlled pure-death chains, coupon-collector acceleration or quantized control literature remain a precedence risk. Finite checks and an unsuccessful search are not a proof of priority. The Gaussian central limit theorem is for each fixed positive \(B\); no uniform-in-\(B\) limit is asserted.

## References

- L. Xia, S. Massei, M. E. Hochstenbach, and B. Koren. *On the influence of stochastic roundoff errors and their bias on the convergence of the gradient descent method with low-precision floating-point computation*. arXiv:2202.12276, publicly posted 2022-02-24. https://arxiv.org/abs/2202.12276
- L. Xia, M. E. Hochstenbach, and S. Massei. *On the Convergence of the Gradient Descent Method with Stochastic Fixed-point Rounding Errors under the Polyak–Łojasiewicz Inequality*. arXiv:2301.09511, publicly posted 2023-01-23. https://arxiv.org/abs/2301.09511
- Classical coupon collector completion-time law and Lyapunov central limit theorem are used as standard probability facts; the latter is applied to a different, calibrated waiting-time triangular array.
