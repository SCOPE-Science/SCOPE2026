# Rank-dependent covariance and an independent median shell for sliding order statistics

## Finding

For integers \(k\ge3\) and \(1\le j\le k\), take independent identically distributed observations \((X_i)_{i\in\mathbb Z}\) with an atomless common real distribution. Let \(R_i^{(j)}\) be the \(j\)-th smallest observation in the window \(X_i,\ldots,X_{i+k-1}\), and let \(I_i^{(j)}=\mathbf1\{R_i^{(j)}\ne R_{i+1}^{(j)}\}\) indicate a change when that window advances. Put \(z=j(k+1-j)\) and \(A=k(k+1)-2z\). Then

\[
\mathbb P(I_i^{(j)}=0)=\frac{A}{k(k+1)},\qquad
\operatorname{Cov}(I_i^{(j)},I_{i+1}^{(j)})
=-\frac{4zA}{k^2(k-1)(k+1)^2(k+2)}<0.
\]

Writing \(F_{j,k+1-j}\) for the cumulative distribution function of \(\operatorname{Beta}(j,k+1-j)\), and \(U\) for an independent uniform variable on \([0,1]\), the opposite end of the dependence range satisfies

\[
\operatorname{Cov}(I_i^{(j)},I_{i+k}^{(j)})
=\frac{(k+1-2j)^2}{k^2}
\operatorname{Var}\big(F_{j,k+1-j}(U)\big).
\]

Thus the lag-\(k\) covariance is strictly positive except at the unique central rank, which exists exactly when \(k\) is odd. For odd \(k\) and \(j=(k+1)/2\), the two change indicators at separation \(k\) are **independent**, not merely uncorrelated. They are independent at every separation \(d\ge k+1\), irrespective of rank.

For fixed \(k\), the ranks attaining the strongest negative adjacent covariance are exactly the integers \(j\in\{1,\ldots,k\}\) minimizing

\[
\left|\left(j-\frac{k+1}{2}\right)^2-\frac{k+1}{4}\right|.
\]

Their displacement from the median is of order \(\sqrt{k}/2\); the maximal adjacent dependence generally occurs at **off-center** ranks. The scientifically new scope is the interior-rank change process \(2\le j\le k-1\), its rank optimization, and the full-window median-independence boundary; the extremal ranks are included only to state the full classification and to compare with earlier maxima results.

## Assumptions and scope

Observations are iid and atomless. Equal numerical ranks therefore coincide exactly when the same original observation is selected, almost surely. A common monotone transformation does not change any indicator. The window width and rank are fixed; all displayed identities are finite-sample, requiring only the \(k+2\) or \(2k+1\) relevant observations. No circular boundary convention is required.

## Proof

Apply the probability-integral transformation, replacing observations by iid \(\operatorname{Unif}(0,1)\) ranks without changing order. Write \(S_i=1-I_i^{(j)}\).

First condition on the middle window \(X_1,\ldots,X_k\) and denote its \(j\)-th order statistic by \(V\). Its distribution is \(\operatorname{Beta}(j,k+1-j)\). An adjacent window retains \(V\) as its selected observation precisely when the element discarded from the middle window has rank below \(j\) and the fresh endpoint is below \(V\), or when the discarded element has rank above \(j\) and the fresh endpoint is above \(V\). Discarding the element at rank \(j\) makes retention impossible. Hence, conditional on the middle window, the two retention events \(S_0,S_1\) are independent because the two fresh endpoints \(X_0,X_{k+1}\) are independent. The ranks of the two discarded positions \(X_k,X_1\) are distinct, uniformly distributed ordered ranks, independently of \(V\). Therefore

\[
\begin{aligned}
\mathbb E(S_0S_1)=\frac{1}{k(k-1)}\big(&
(j-1)(j-2)\mathbb E V^2\\
&+(k-j)(k-j-1)\mathbb E(1-V)^2\\
&+2(j-1)(k-j)\mathbb E[V(1-V)]\big).
\end{aligned}
\]

The beta moments \(\mathbb E V^2=j(j+1)/[(k+1)(k+2)]\), \(\mathbb E(1-V)^2=(k+1-j)(k+2-j)/[(k+1)(k+2)]\), and \(\mathbb E[V(1-V)]=j(k+1-j)/[(k+1)(k+2)]\) reduce this expression to

\[
\mathbb E(S_0S_1)=\frac{A(A-2)}{k(k-1)(k+1)(k+2)}.
\]

The one-event version gives \(\mathbb ES_0=A/[k(k+1)]\). Subtracting its square yields the displayed lag-one covariance. Since \(\operatorname{Cov}(1-S_0,1-S_1)=\operatorname{Cov}(S_0,S_1)\), the same formula applies to changes.

For lag \(k\), the variables determining \(S_0\) and \(S_k\) have only \(X_k\) in common. Conditional on \(X_k=x\), they are independent, and by time reversal the conditional probability of either retention event is the same function \(h(x)\). Let \(Z_1<\cdots<Z_{k-1}\) be the order statistics of the remaining shared \(k-1\) observations, with boundary conventions \(Z_0=0\) and \(Z_k=1\). For an independent incoming uniform endpoint, the conditional retention probability is

\[
 h(x)=\mathbb E\big[Z_{j-1}\mathbf1\{x<Z_{j-1}\}+(1-Z_j)\mathbf1\{x>Z_j\}\big].
\]

The beta order-statistic densities give

\[
 h'(x)=\frac{k+1-2j}{k}\,f_{j,k+1-j}(x),\qquad h(0)=\frac{j-1}{k},
\]

so \(h(x)=(j-1)/k+[(k+1-2j)/k]F_{j,k+1-j}(x)\). The conditional covariance is zero; the law of total covariance now gives \(\operatorname{Cov}(S_0,S_k)=\operatorname{Var}(h(X_k))\), proving the second formula. The beta cumulative distribution is strictly increasing on the unit interval, so its evaluation at a uniform point has positive variance. This establishes the sign classification. At the central rank the coefficient of that CDF vanishes: \(h(x)\) is constant, and conditional independence implies unconditional Bernoulli independence. For lags at least \(k+1\), the two indicator windows use disjoint observations, proving independence.

Finally, the absolute lag-one covariance is a positive \(k\)-dependent factor times \(z[k(k+1)-2z]\). Completing the square shows its maximum precisely when \(z\) is as close as possible to \(k(k+1)/4\). Since \(z=(k+1)^2/4-(j-(k+1)/2)^2\), this is exactly the stated discrete rank classification.

## Verification

The standalone standard-library-only script `verify.py` recomputes both covariance formulas with exact rational arithmetic. It enumerates all relative-order permutations for lag one at widths \(2\le k\le6\) and for lag \(k\) at widths \(2\le k\le4\), all admissible ranks. It also checks the beta-polynomial integrals, strict-sign and median-null tests, and all discrete optimizers at widths up to \(21\). A successful execution produces `PASS: 1286 exact identities, inequalities, and exhaustive checks`. These finite computations corroborate but do not substitute for the proof for arbitrary width.

## Relationship to prior work

Suomela (2014) formulates the sliding median and establishes algorithmic equivalence with sorting, not random-input update dependence. Restrepo and Bovik (1987) derive joint distributions of **two** order statistics from overlapping samples and calculate analog output correlations; those two-output distributions do not alone determine the covariance between the **two change events** studied here, each comparing adjacent order statistics. Gallagher and Wise (1981) address deterministic invariance under median filtering. Bovik (1987) analyzes equal-output streaks of running medians and thus overlaps with **central-median adjacent-equality** calculations; no originality is claimed for such a marginal or streak-length fact without further qualification. A prior exact covariance law for running maxima covers the extremal rank \(j=k\), including the corresponding special case of our formulas. The rank-dependent interior family, the off-center extremizer rule and the exceptional lag-\(k\) independent median shell are the contribution assessed here.

## Limitations

Covariances for intermediate lags \(2\le d\le k-1\) are not classified here. Independence at lag \(k\) is a pairwise statement, not joint independence of the whole stationary change process. General continuous non-atomic marginals are allowed, but ties or serial dependence invalidate the calculation. Historical priority remains qualified because the complete text of Bovik's 1987 streaking paper could not be obtained; its abstract specifically concerns streak lengths. The 1987 pair-overlap results are also substantial prior theory; more general multivariate identities could subsume parts of this theorem. No independent mathematical audit has been performed.

## References

- J. Suomela, *Median Filtering is Equivalent to Sorting*, initial arXiv submission 2014-06-06, https://arxiv.org/abs/1406.1717.
- A. C. Bovik and A. Restrepo, *Spectral properties of moving L-estimates of independent data*, Journal of the Franklin Institute 324 (1987), 125–137, https://doi.org/10.1016/0016-0032(87)90378-4.
- A. C. Bovik, *Streaking in median filtered images*, IEEE Transactions on Acoustics, Speech, and Signal Processing 35 (1987), 493–503, https://doi.org/10.1109/TASSP.1987.1165153.
- N. C. Gallagher and G. L. Wise, *A theoretical analysis of the properties of median filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing 29 (1981), 1136–1141, https://doi.org/10.1109/TASSP.1981.1163708.
- *A negative-to-positive dependence transition in sliding-window maxima*, public mathematical finding (2026), exact extremal-rank covariance benchmark; original source is credited rather than republished.
