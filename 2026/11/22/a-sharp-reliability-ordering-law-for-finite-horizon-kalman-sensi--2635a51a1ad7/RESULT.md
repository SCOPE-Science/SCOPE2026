# A sharp reliability-ordering law for finite-horizon Kalman sensing with packet loss

## Finding

**Theorem (all-horizon sorting and a sharp local frontier).** Consider a scalar Kalman filter with a positive initial predicted covariance, one identically precise measurement offered at each of finitely many observation times, and one use of each of a prescribed set of independent Bernoulli packet-delivery channels. If every intervening forecast has squared state gain \(g_k>0\), process-noise variance \(q_k\ge0\), and satisfies

\[
 g_k+\lambda q_k\ge1,
\]

where \(\lambda>0\) is the common measurement precision, then assigning channels in **nondecreasing delivery probability** minimizes the terminal posterior covariance in **first-order stochastic order** among every nonadaptive permutation. Hence it simultaneously minimizes the expectation of every increasing measurable terminal-covariance loss for which the expectation is defined, including Bayes mean-square error.

This local frontier is sharp for uniform prior-independent reliability sorting: if \(g+\lambda q<1\) and \(q>0\), the optimal order of two channels with distinct success probabilities reverses exactly once as the starting covariance increases, at an explicit positive threshold. If \(q=0\) and \(0<g<1\), the *reverse* reliability ordering is optimal at every covariance. In particular, the sorting theorem cannot be extended to all contractive noisy systems with an arbitrary starting variance.

## Assumptions and scope

Fix an integer \(n\ge2\). At observation time \(j\), a scalar Gaussian state is observed through \(Y_j=X_j+V_j\), where the independent Gaussian measurement noise has variance \(\lambda^{-1}>0\). A single assigned channel \(i\) delivers this observation successfully with probability \(p_i\in[0,1]\), independently across channel identities and of state/process/measurement noise; the filter observes the success/failure acknowledgement. Every channel is used once. Assignments are deterministic permutations chosen before any outcomes are revealed. Conditioned on the acknowledgements, Kalman posterior covariance evolves deterministically. The initial pre-observation covariance is \(x_1>0\); after observation \(j\) and before the next measurement, the prediction is the affine map \(T_j(x)=g_jx+q_j\) for \(g_j>0\) and \(q_j\ge0\). No forecast follows the final observation.

The successful scalar measurement map is \(U(x)=x/(1+\lambda x)\); packet failure leaves \(x\) unchanged. The terminal risk is the covariance after observation \(n\). The stochastic order \(Z\preceq_{\mathrm{st}}Z'\) means \(\mathbb E\phi(Z)\le\mathbb E\phi(Z')\) for every bounded increasing measurable \(\phi\); the same ordering extends to nonnegative increasing losses by monotone convergence. Conditional Gaussianity gives the usual equality between expected terminal covariance and unconditional mean-squared Bayes filtering error.

## Proof

**1. Exact prediction/measurement commutator.** At a single forecast \(T(x)=gx+q\), direct algebra gives

\[
T(U(x))-U(T(x))=
\frac{\lambda\left[q^2+(\lambda q^2+2gq)x+g(\lambda q+g-1)x^2\right]}
{(1+\lambda x)(1+\lambda(gx+q))}.
\tag{1}
\]

For positive \(x,g,\lambda\) and nonnegative \(q\), every coefficient in the numerator is nonnegative if and only if \(g+\lambda q\ge1\) (as a statement of nonnegativity **for every** \(x>0\)). Thus under that condition \(T\circ U\ge U\circ T\) pointwise. When \(q=0\) and \(g<1\), the inequality reverses strictly for every positive \(x\).

**2. Adjacent interchange and stochastic ordering.** Take two consecutive channels with receipt probabilities \(p<r\), and fix the covariance \(x\) before the pair. The distribution of the covariance after the second observation is a four-outcome mixture. When either both packets arrive or neither arrives, the final covariance is independent of the order. If only the first packet arrives it is \(T(U(x))\); if only the second arrives it is \(U(T(x))\). Therefore, for every bounded increasing \(\phi\),

\[
\mathbb E\phi(Z_{p,r})-\mathbb E\phi(Z_{r,p})
=(p-r)\left[\phi(T(U(x)))-\phi(U(T(x)))\right].
\tag{2}
\]

When \(g+\lambda q\ge1\), (1) shows this difference is nonpositive. In particular, \(Z_{p,r}\preceq_{\mathrm{st}}Z_{r,p}\) conditionally on **every** covariance entering the pair. Every later successful/failed measurement and affine forecast is an increasing map, and every later Bernoulli channel is independent; applying a common random suffix preserves the increasing-test-function ordering. An arbitrary prefix merely randomizes the entering covariance and preserves it by conditioning. Every permutation can be bubble-sorted into nondecreasing receipt probabilities through adjacent improvements. This proves the global theorem for all finite \(n\), time-inhomogeneous \(g_j,q_j\), and every increasing terminal risk. Equality cases (identical receipt probabilities or a vanishing commutator) are allowed; no uniqueness claim is needed.

**3. Exact sharp crossover.** If \(q>0\) and \(g+\lambda q<1\), put \(b=\lambda q^2+2gq>0\) and \(c=g(1-g-\lambda q)>0\). The commutator numerator in (1) is \(q^2+bx-cx^2\), which has exactly one positive zero,

\[
 x_* = \frac{b+\sqrt{b^2+4cq^2}}{2c}.
\]

It is positive below \(x_*\) and negative above. By (2), when \(0<p<r<1\), low-reliability first is strictly better below this threshold and strictly worse above it for the expected terminal covariance. Consequently there is no covariance-independent reliability order outside the frontier, even for two time slots. With \(q=0\), (1) has the strict sign of \(g-1\), establishing the reverse-order assertion for contractive noiseless forecasts (and any number of such forecasts, by the same interchange proof).

An exact rational example takes \(\lambda=1\), \(g=1/2\), \(q=1/10\), and probabilities \(p=1/4\), \(r=3/4\). Writing \(D(x)=\mathbb E[P_{\mathrm{terminal}}\mid(p,r)]-\mathbb E[P_{\mathrm{terminal}}\mid(r,p)]\), direct substitution yields \(D(1/4)=-2/245<0\) and \(D(2)=19/420>0\). By contrast, if \(q\ge1/2\) with the same \(g,\lambda\), the less reliable channel always belongs first.

## Verification

Run `python3 verify.py` with Python 3.9 or newer; no external packages are needed. This exact-rational verifier checks identity (1) on a rational parameter grid, both counterexample signs, and *all* permutations and finite-support distribution functions for example time-inhomogeneous models through five observations. The observed replay result is `PASS: 14884 exact-rational identities, schedule comparisons, and finite CDF inequalities`. These finite checks independently test the algebra and examples; the arbitrarily long-horizon stochastic-order statement is established by the proof in Steps 1–2, not by enumeration.

## Relationship to prior work

Wu, Ding, Cheng and Shi's 2018 paper develops monotone state/holding-time scheduling for **multiple independent dynamic processes**, with a stationary average-cost Markov decision formulation. It does not identify the exact interchange of **heterogeneous packet reliabilities on one scalar process**, or a stochastic-order optimum across all fixed permutations. Marelli, Sui, Rohr and Fu (2018) treat the **stability** of randomly intermittent Kalman filtering with random measurement equations rather than the finite-horizon arrangement of success probabilities. Singh, Kamath and Kumar (2019) prioritize time-stamped packets using a constant-gain estimator and value-of-information indices; their observation-quality/age problem does not entail the exact Bayesian variance commutator (1).

Leong, Dey and Quevedo's earlier event-triggered packet-drop framework proves **covariance-dependent sensor-switching thresholds** for transmission decisions, a different policy class and cost. Related published two-use scalar Kalman work optimizes **measurement precision order with reliable delivery**, and work on uniform observation precision concerns **infinite-horizon precision budgets**; neither statement directly implies the present all-horizon stochastic dominance for sorting success probabilities. These distinctions do not certify historical novelty: an unlocated equivalent rearrangement theorem in the broad stochastic-filtering literature is still possible.

## Limitations

The theorem assumes a scalar known linear-Gaussian model, identical measurement precisions, independent identity-specific Bernoulli receipts, a known positive starting covariance, nonadaptive permutation of exactly one use per channel, and known prediction parameters. It does not optimize feedback-dependent or adaptive scheduling, unequal observation precisions, correlated packet failures, vector Riccati systems, time-average errors, or actual channel communication costs. The sharpness is for *uniform covariance-independent sorting*, not the absence of a more complicated state-dependent optimal ordering in the contractive-noisy regime. No external mathematical audit or definitive historical-priority determination has been performed.

## References

1. S. Wu, K. Ding, P. Cheng and L. Shi, “Optimal Scheduling of Multiple Sensors over Lossy and Bandwidth Limited Channels,” first public 2018-04-16, https://arxiv.org/abs/1804.05618.
2. D. Marelli, T. Sui, E. Rohr and M. Fu, “Stability of Kalman Filtering with a Random Measurement Equation: Application to Sensor Scheduling with Intermittent Observations,” first public 2018-06-21, https://arxiv.org/abs/1806.08098.
3. R. Singh, G. K. Kamath and P. R. Kumar, “Optimal Information Updating based on Value of Information,” first public 2019-08-03, https://arxiv.org/abs/1908.01119.
4. A. S. Leong, S. Dey and D. E. Quevedo, “Sensor Scheduling in Variance Based Event Triggered Estimation with Packet Drops,” first public 2015-11-16, https://arxiv.org/abs/1511.04792.
