# Affine quantile regression of uniform-sample Gini dispersion and its exact optimal-rank ties

## Finding

Let \(n\ge2\), and let \(X_1,\ldots,X_n\) be independent \(\operatorname{Unif}(0,1)\) observations. Write \(X_{(1)}\le\cdots\le X_{(n)}\) and define the unnormalized sample Gini mean difference
\[
G_n=\binom n2^{-1}\sum_{1\le i<j\le n}|X_i-X_j|.
\]
For each integer \(1\le k\le n\), the **entire conditional least-squares projection onto one empirical quantile**, not only its linear approximation, is
\[
\boxed{\mathbb E[G_n\mid X_{(k)}=x]
=\frac13+\frac{(n+1)(2k-n-1)}{3n(n-1)}
\left(x-\frac{k}{n+1}\right).}
\tag{1}
\]
In particular, the central order statistic for odd \(n\) has constant regression \(\mathbb E[G_n\mid X_{((n+1)/2)}]=1/3\), despite the statistics being constructed from the same data.

The fraction of Gini variance explained by the **optimal unrestricted measurable predictor** based only on \(X_{(k)}\), equivalently the squared Pearson correlation, is exactly
\[
\boxed{R_{n,k}^2=\frac{5k(n+1-k)(2k-n-1)^2}{n(n-1)(n+2)(n+3)}.}
\tag{2}
\]
For every \(n\ge2\), the maximizing ranks occur in exactly two symmetric positions, except at the infinite sequence
\[
 n=9,57,337,\ldots,
\tag{3}
\]
when **exactly four** ranks tie. Precisely, a four-way tie occurs if and only if there are positive integers \(N,j\), with \(N=n+1\), satisfying
\[
N^2-2j^2=2.
\tag{4}
\]
All admissible pairs are generated from \((N,j)=(2,1)\) by \((N,j)\mapsto(3N+4j,2N+3j)\); discard the initial \(n=1\), which is outside the domain. At the first three exceptional sizes, the optimal ranks are respectively \(\{1,2,8,9\}\), \(\{8,9,49,50\}\), and \(\{49,50,288,289\}\).

For every sequence of maximizing ranks, any limiting rank fraction must lie in
\[
\left\{\frac12\left(1-\frac1{\sqrt2}\right),\;
\frac12\left(1+\frac1{\sqrt2}\right)\right\},
\qquad \max_{1\le k\le n}R_{n,k}^2\longrightarrow\frac5{16}.
\tag{5}
\]
By reflection, optimal lower and upper ranks have equal explained variance. Under \(\operatorname{Unif}(a,b)\) with finite \(a<b\), equation (1) transforms affinely and every explained-variance fraction and optimal rank is unchanged.

## Assumptions and scope

The \(n\) observations are independent with one common nondegenerate continuous-uniform distribution, with no estimated parent parameters, censoring, truncation, ties, or normalization of Gini dispersion by the sample mean. The same-sample conditional expectation in (1) is taken with respect to the randomness of all other observations given the specified order statistic. All \(n\ge2\) and all \(1\le k\le n\) are included. Optimality is **among all measurable one-coordinate predictors** for squared-error risk, not among multiquantile summaries, and the stated optimal fraction is the population prediction \(R^2\) under the specified sampling law.

## Proof

Fix \(n,k\), put \(m=k-1\) and \(r=n-k\). Conditional on \(X_{(k)}=x\), the \(m\) unordered observations below \(x\) are iid uniform on \([0,x]\), while the \(r\) unordered observations above \(x\) are iid uniform on \([x,1]\), with the groups independent. For any pair inside the lower group the expected absolute gap is \(x/3\); inside the upper group it is \((1-x)/3\). A lower and an upper observation have mean gap \(1/2\), while gaps to the fixed pivot have means \(x/2\) and \((1-x)/2\). Therefore the exact conditional sum over unordered pairs is
\[
\mathbb E\left[\sum_{i<j}|X_i-X_j|\mid X_{(k)}=x\right]
=\frac{m(m+2)}6x+\frac{r(r+2)}6(1-x)+\frac{mr}{2}.
\tag{6}
\]
Multiplying by \(2/[n(n-1)]\) proves that the conditional expectation is affine, with slope \((n+1)(2k-n-1)/[3n(n-1)]\). Since \(\mathbb E[G_n]=1/3\) and \(\mathbb E[X_{(k)}]=k/(n+1)\), this gives (1) including its intercept. The affine projection is the actual conditional mean, so it is the unique minimum-mean-square-error predictor as a function of this single order statistic, up to almost-sure equality.

For the exact explained fraction, set \(N=n+1\) and introduce all \(N\) uniform order spacings, including boundary spacings. Their joint law is \(\operatorname{Dirichlet}(1,\ldots,1)\), with
\[
\operatorname{Cov}(D_i,D_j)=\frac{N\mathbf1_{i=j}-1}{N^2(N+1)}.
\]
The gap across ordered labels \(j-1,j\) appears in \((j-1)(N-j)\) unordered differences. Thus
\[
G_n=\frac2{n(n-1)}\sum_{j=1}^{N}(j-1)(N-j)D_j.
\]
The elementary sums of gap weights and squared weights are
\[
\sum_{j=1}^{N}(j-1)(N-j)=\frac{n(n^2-1)}6,
\qquad
\sum_{j=1}^{N}(j-1)^2(N-j)^2=\frac{n(n^4-1)}{30}.
\]
Substitution into the displayed Dirichlet covariance matrix gives
\[
\operatorname{Var}(G_n)=\frac{n+3}{45n(n-1)},
\quad
\operatorname{Var}(X_{(k)})=\frac{k(N-k)}{N^2(N+1)}.
\tag{7}
\]
By (1), the regression slope times \(\operatorname{Var}(X_{(k)})\) equals the covariance. The law of total variance gives \(\operatorname{Var}(\mathbb E[G_n\mid X_{(k)}])/\operatorname{Var}(G_n)\), which simplifies using (7) to (2). It is also the squared Pearson correlation because the projection is affine.

For the **exact integer optimizer**, set \(t=|2k-N|\). As \(k\) ranges over the allowed ranks, \(t\) ranges through integers of the parity of \(N\), from \(0\) or \(1\) up to \(N-2\), and every positive \(t\) corresponds to exactly two symmetric ranks. Apart from the positive rank-independent denominator of (2), maximizing \(R_{n,k}^2\) is equivalent to maximizing
\[
k(N-k)t^2=\frac{N^2t^2-t^4}{4}
=\frac{N^4}{16}-\frac{(t^2-N^2/2)^2}{4}.
\tag{8}
\]
Thus choose available \(t\) whose square is closest to \(N^2/2\). There is either one optimal \(t\), yielding two ranks, or precisely two consecutive admissible values \(t,t+2\), yielding four ranks. Equality of the two scores occurs precisely when \(t^2+(t+2)^2=N^2\), equivalent to (4) with \(j=t+1\). For \(n\ge2\), any such solution has \(N\) even, \(j\) odd, and \(1\le t\le N-4\). The positive integral solutions to \(N^2-2j^2=2\) are exactly the powers of the fundamental norm-one unit \(3+2\sqrt2\) applied to \(2+\sqrt2\), equivalently the displayed recurrence; this follows from the standard descent using multiplication by \(3-2\sqrt2\), taking any positive solution to a smaller nonnegative one and terminating at \((2,1)\). This establishes (3) and the complete finite classification.

Finally, write \(u=k/N\). The exact numerator in (2) normalized by its fourth-order scale converges uniformly to \(u(1-u)(2u-1)^2\) on \([0,1]\); the denominator normalizes to one, so
\[
R_{n,k}^2\longrightarrow 5u(1-u)(2u-1)^2
\]
along rank fractions \(k/N\to u\). Writing \(z=2u-1\) reduces this to \(5z^2(1-z^2)/4\), with exactly two maximizers \(z=\pm1/\sqrt2\), maximum \(5/16\). Compactness and the exact finite maximization give (5).

## Verification

The standard-library checker `verify.py` performs independent exact-rational calculations of all order-statistic covariances from their Dirichlet covariance matrix, of Gini variance, and of the complete conditional regression via direct class-by-class pair counting, for every \(2\le n\le60\) and all \(1\le k\le n\). It also enumerates every rank score for \(2\le n\le600\), compares the maximizing set to the nearest-square characterization, independently detects Pell-tie sizes, and checks the first three exceptional optimal rank sets. Run `python3 verify.py` in the directory containing that file. The checker passes 12,775 exact assertions. These finite checks are supplementary; equations (6)–(8) and Pell descent establish the universally quantified statements.

## Relationship to prior work

Gerstenberger and Vogel [1] study the Gini mean difference as a robust scale estimator. Čiginas and Pumputis [2] examine its dependence on variance-type dispersion and finite-population estimation. Neither inspected full text gives the conditional projection of the same-sample Gini statistic on one observed order statistic. Hosking [3] introduces linear order-statistic scale summaries; a formula may be indirectly accessible from that general framework, but a complete full-text comparison was unavailable.

The published **uniform sample-variance/order-statistic** covariance result [4] has a closely related and, in fact, proportional rank-wise mixed covariance profile and **the same limiting optimal rank fractions**. Those rank fractions and their limiting correlation magnitude are therefore **not claimed novel in themselves**. Crucially, the conditional variance regression in [4] is quadratic in the observed quantile, whereas the Gini conditional projection (1) is **exactly affine for every rank**, so the present optimum is also optimum over *all nonlinear one-quantile predictors*. The exact Pell-indexed four-way finite-rank ties and their full classification are not given in [4]. Another published result [5] optimizes Pearson correlation of a Gini statistic with an order statistic for an *exponential* rather than uniform parent; its first-order optimal rank is different, and it does not imply the present uniform conditional projection.

## Limitations

No independent mathematical audit or comprehensive historical priority certification has been performed. Older L-statistic and order-statistic literature, especially the full text of [3], might contain an equivalent affine projection or a more general conditional result, although no such statement was identified in inspected sources. The finite-rank Pell classification follows from an elementary optimization once (2) is known, so its significance is as an exact boundary of a motivated prediction problem, not as a standalone number-theoretic advance. The result does not establish optimality of a single quantile among multiple coordinates, validity for nonuniform parents, or statistical adaptivity to unknown distributional parameters. Conditional mean independence at the central rank is not full independence.

## References

[1] C. Gerstenberger and D. Vogel, *On the efficiency of Gini's mean difference*, arXiv:1405.5027, first submitted 20 May 2014. https://arxiv.org/abs/1405.5027

[2] A. Čiginas and D. Pumputis, *Gini's mean difference and variance as measures of finite populations scales*, arXiv:1406.2275, first submitted 9 June 2014. https://arxiv.org/abs/1406.2275

[3] J. R. M. Hosking, *L-Moments: Analysis and Estimation of Distributions Using Linear Combinations of Order Statistics*, *JRSS B* **52** (1990), 105–124. https://doi.org/10.1111/j.2517-6161.1990.tb01775.x

[4] *Exact order-statistic coupling profile with sample variance under a uniform law*. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-order-statistic-coupling-profile-with-sample-variance-unde--59495db55ed7

[5] *An asymptotically optimal exponential-sample quantile for Gini mean-difference correlation*. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-an-asymptotically-optimal-exponential-sample-quantile-for-gini-m--d004c7551177
