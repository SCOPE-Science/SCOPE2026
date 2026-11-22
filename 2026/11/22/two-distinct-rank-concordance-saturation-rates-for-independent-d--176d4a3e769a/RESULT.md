# Two distinct rank-concordance saturation rates for independent drifted random walks

## Finding
Let \(X_i=\sum_{j=1}^{i}\xi_j\) and \(Y_i=\sum_{j=1}^{i}\eta_j\) be two independent random walks. Under the assumptions below, their sample Spearman and Kendall coefficients, \(\rho_n\) and \(\tau_n\), converge to the sign \(\sigma\) of the product of their drifts, but at **different powers** of the sample size. Define \(p_X(k)=\Pr(\sum_{j=1}^{k}\widetilde\xi_j<0)\), and likewise \(p_Y(k)\), where the tildes orient each walk to positive drift. Then almost surely,

\[
\lim_{n\to\infty} n^2(1-\sigma\rho_n)=12\sum_{k=1}^{\infty}k[p_X(k)+p_Y(k)],
\]
\[
\lim_{n\to\infty} n(1-\sigma\tau_n)=4\sum_{k=1}^{\infty}[p_X(k)+p_Y(k)-2p_X(k)p_Y(k)].
\]

Both limits are finite. They are strictly positive whenever at least one of the oriented increment distributions has positive probability of a negative step. Even when the paths are independent, their shared time trend drives the rank coefficients to perfect apparent agreement or disagreement; Spearman's error is quadratic in \(1/n\), Kendall's only linear. The formulas specify the exact leading constants.

## Assumptions and scope
For each walk, increments are iid real variables. The two sequences are independent. Each mean is finite and nonzero. Write \(\epsilon_X=\operatorname{sgn}\mathbb E\xi_1\), \(\epsilon_Y=\operatorname{sgn}\mathbb E\eta_1\), \(\widetilde\xi_j=\epsilon_X\xi_j\), \(\widetilde\eta_j=\epsilon_Y\eta_j\), and \(\sigma=\epsilon_X\epsilon_Y\). Assume that for each oriented walk there is a \(\theta>0\) such that \(\mathbb E e^{-\theta\widetilde\xi_1}<1\), respectively \(\mathbb E e^{-\theta\widetilde\eta_1}<1\). Assume \(\Pr(\sum_{j=1}^k\widetilde\xi_j=0)=\Pr(\sum_{j=1}^k\widetilde\eta_j=0)=0\) for every integer \(k\ge1\); continuous increment distributions suffice. In particular, neither sample contains tied levels almost surely. Observations are the paired cumulative sums at integer times \(i=1,\ldots,n\), not independently sampled levels. \(\rho_n\) is ordinary Spearman rank correlation and \(\tau_n\) ordinary Kendall tau-a without ties. These are almost-sure asymptotics, not fixed-\(n\) distributional identities.

## Proof
**1. Reduce to positive drift.** Changing the sign of one time series reverses every sample rank. It changes both rank coefficients by exactly a minus sign. Hence it suffices to prove the two limits for independent walks with positive oriented drift, after which replace both coefficients by \(\sigma\) times themselves.

**2. Exponentially summable inversions.** Fix one oriented increment sequence and put \(S_k=\sum_{j=1}^k\widetilde\xi_j\) and \(p(k)=\Pr(S_k<0)\). Markov's inequality gives \(p(k)\le q^k\) for \(q=\mathbb E e^{-\theta\widetilde\xi_1}<1\). Thus \(\sum k p(k)<\infty\), and all moments of the total number \(N=\sum_{k\ge1}\mathbf1_{\{S_k<0\}}\) are finite. Indeed, if \(L\) is the last negative partial-sum index, \(\Pr(L\ge m)\le q^m/(1-q)\) and \(N\le L\).

**3. Stationary rank displacements.** Extend the two iid increment sequences independently to all integer indices. Let
\[
U_i^X=\sum_{k\ge1}\mathbf1_{\{X_{i+k}<X_i\}}-\sum_{k\ge1}\mathbf1_{\{X_{i-k}>X_i\}},
\]
and similarly \(U_i^Y\), interpreting differences using the two-sided extension. Both infinite sums terminate almost surely by Step 2. The future and past counts in \(U_i^X\) are independent and each distributed as \(N_X\); consequently \(\mathbb E U_i^X=0\) and \(\operatorname{Var}(U_i^X)=2\operatorname{Var}(N_X)\). The two walks are independent, so
\[
\mathbb E(U_i^X-U_i^Y)^2=2\operatorname{Var}(N_X)+2\operatorname{Var}(N_Y).
\]
The stationary process \((U_i^X,U_i^Y)_{i\in\mathbb Z}\) is an ergodic function of a two-sided iid shift. Thus its average squared difference converges almost surely to this expectation.

If \(R_{i,n}^X\) denotes the rank of \(X_i\) among \(X_1,\ldots,X_n\), a direct count gives
\[
R_{i,n}^X-i=\sum_{j=i+1}^{n}\mathbf1_{\{X_j<X_i\}}-\sum_{j=1}^{i-1}\mathbf1_{\{X_j>X_i\}}.
\]
This is a windowed version of \(U_i^X\). For any integer \(m\), uniformly for interior positions \(m<i\le n-m\), its difference from \(U_i^X\) is bounded by the number of past and future inversions at lag greater than \(m\). These tails form a stationary integrable-square process with expectation of its square tending to zero as \(m\to\infty\) (Step 2 and Cauchy–Schwarz). The ergodic theorem bounds the interior average squared error by its arbitrarily small mean. For the \(2m\) boundary positions, every squared rank displacement is bounded by an all-lag inversion count with finite fourth moment; stationarity and Borel–Cantelli show these finitely many boundary contributions divided by \(n\) vanish almost surely. Therefore
\[
\frac1n\sum_{i=1}^n(R_{i,n}^X-R_{i,n}^Y)^2 \longrightarrow 2\operatorname{Var}(N_X)+2\operatorname{Var}(N_Y)\quad\text{a.s.}
\]
The exact no-tie Spearman identity \(1-\rho_n=6\sum_i(R_{i,n}^X-R_{i,n}^Y)^2/[n(n^2-1)]\) implies the first limit once the variance is evaluated.

**4. Spitzer's occupation identity.** The classical Sparre Andersen–Spitzer cyclic permutation identity for an iid random walk with no zero partial sums gives the generating function for the total number of negative partial sums:
\[
\mathbb E z^N=\exp\left\{\sum_{k\ge1}\frac{p(k)}{k}(z^k-1)\right\},\qquad 0\le z\le1.
\]
Differentiation of the log generating function at \(z=1\), justified by \(\sum k p(k)<\infty\), yields \(\operatorname{Var}(N)=\sum_{k\ge1}k p(k)\). To make the identity and its normalization checkable, its finite-time form is
\[
\sum_{n\ge0}t^n\mathbb E z^{N_n}=\exp\left\{\sum_{k\ge1}\frac{t^k}{k}[(1-p(k))+p(k)z^k]\right\},\quad N_n=\sum_{k=1}^n\mathbf1_{\{S_k<0\}}.
\]
For fixed \(|t|<1\) this is the classical cycle decomposition; letting \(t\uparrow1\) after multiplication by \(1-t\), with \(N_n\uparrow N\) and geometric tails, gives the infinite-horizon identity. Substitution into Step 3 proves the Spearman constant.

**5. Discordant pairs and Kendall's law.** At positions \(i<j\) separated by \(k=j-i\), discordance occurs if exactly one of the two independently distributed increments sums is negative. Its probability equals \(\delta_k=p_X(k)(1-p_Y(k))+p_Y(k)(1-p_X(k))\). With \(D_n\) the number of discordant index pairs, write \(D_n=\sum_{k=1}^{n-1}\sum_{i=1}^{n-k}I_{i,k}\). At each fixed \(k\), \(I_{i,k}\) is an ergodic stationary finite-window function, so \(n^{-1}\sum_{i=1}^{n-k}I_{i,k}\to\delta_k\) almost surely. For all \(k>m\), \(I_{i,k}\) is bounded by the union of a negative increment sum in one of the two walks. The stationary sum of such long-lag indicators over \(k>m\) has finite expectation bounded by \(\sum_{k>m}[p_X(k)+p_Y(k)]\), which goes to zero. Another application of the ergodic theorem then proves \(D_n/n\to\sum_{k\ge1}\delta_k\) almost surely. The exact identity \(1-\tau_n=4D_n/[n(n-1)]\) proves the second limit.

**6. Gaussian example.** If both oriented increments are Gaussian with common positive mean \(\mu\) and standard deviation \(s>0\), set \(a=\mu/s\); then \(p_X(k)=p_Y(k)=\Phi(-a\sqrt{k})\). Hence the constants simplify to \(24\sum k\Phi(-a\sqrt{k})\) and \(8\sum\Phi(-a\sqrt{k})[1-\Phi(-a\sqrt{k})]\). Their exponential tails make them directly computable.

## Verification
The independent standalone Python checker `checker.py` recomputes the exact cyclic-permutation generating-function recursion by enumerating all step sequences through length nine for the nonlattice two-point law with increments \(\sqrt2\) and \(-1\) at respective probabilities \(2/3\) and \(1/3\). Negative-sum comparisons use integer arithmetic (no floating-point tie tests). It also verifies exact Spearman and Kendall algebra against enumerated rank permutations. Numerical Gaussian constants are computed from convergent normal-tail series. Checks are finite corroboration, not proof of the almost-sure limits; the proof above rests on geometric tail bounds, the iid ergodic theorem, and the cited classical occupation identity.

## Relationship to prior work
Piancastelli and Barreto-Souza (arXiv:2502.05102, first posted 2025-02-07) investigate stochastic dynamics of rankings based on a stationary Mallows/GARCH model, rather than the ranks induced *across time* by cumulative-sum trajectories. Ryan, Haslbeck and Waldorp (online 2025-01-15) discuss random walks with drift as stochastic trends and the danger of mishandled nonstationarity, but do not quantify rank-concordance saturation. Xie and Zhu (arXiv:2611.20572, publicly posted 2026-11-16) prove Brownian-functional limits for **centered** independent walks; their mean-zero assumptions exclude the exponentially transient inversions exploited here. Classical Sparre Andersen–Spitzer fluctuation identities are used as established inputs, not claimed as new. The contribution is the pair of exact and distinct almost-sure rates for independent **nonzero-drift** walks, including the one-sided-walk constants.

## Limitations
No conclusion is asserted for zero drift, long-tailed increments without the stated negative exponential moment, dependent walk pairs, or ties. The result does not furnish a finite-sample sampling distribution or inferential calibration. The constants can be very large when drift is weak, so the asymptotic regime may require large sample sizes. An older equivalent statement not indexed by the literature searches cannot be entirely excluded; an independent mathematical and historical audit has not been performed.

## References
1. Piancastelli, L. S. C., and Barreto-Souza, W., *Time Series Analysis of Rankings: A GARCH-Type Approach*, arXiv:2502.05102 (2025), https://arxiv.org/abs/2502.05102 .
2. Ryan, O., Haslbeck, J. M. B., and Waldorp, L. J., *Non-Stationarity in Time-Series Analysis: Modeling Stochastic and Deterministic Trends*, Multivariate Behavioral Research (online 2025-01-15), https://doi.org/10.1080/00273171.2024.2436413 .
3. Xie, Z., and Zhu, L., *Nonsense rank correlations between independent random walks*, arXiv:2611.20572 (2026-11-16), https://arxiv.org/abs/2611.20572 .
4. Spitzer, F., *A combinatorial lemma and its application to probability theory*, Transactions of the American Mathematical Society 82 (1956), 323–339, https://doi.org/10.1090/S0002-9947-1956-0079851-X .
