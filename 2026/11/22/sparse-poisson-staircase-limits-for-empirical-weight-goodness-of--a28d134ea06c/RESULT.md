# Sparse-Poisson staircase limits for empirical-weight goodness-of-fit distances

## Finding

Consider the empirical Poisson weight-ratio statistic of Kirui, Bothma, Smuts, Steyn and Visagie [1], and its weighted distance from the constant function one. Under a *true*, shrinking-mean Poisson null, the nine fixed/empirical/fitted weighting schemes split into fundamentally different asymptotic regimes.

**Critical rare-cell law.** Fix an integer \(r\ge2\) and \(c\in(0,\infty)\). Let \(X_{n,1},\ldots,X_{n,n}\) be independent \(\operatorname{Pois}(\lambda_n)\) observations, with \(\lambda_n\to0\) and \(n\lambda_n^r\to c\). Put \(\widehat\lambda_n=n^{-1}\sum_i X_{n,i}\), \(\widehat p_n(k)=n^{-1}\sum_i\mathbf1_{\{X_{n,i}=k\}}\), \(p_\theta(k)=e^{-\theta}\theta^k/k!\), and \(W_n(k)=\widehat p_n(k)/p_{\widehat\lambda_n}(k)\). On the vanishing-probability event \(\widehat\lambda_n=0\), define the distances arbitrarily.

For any deterministic weight \(g:\mathbb N_0\to(0,\infty)\) with \(\sum_{k\ge0}g(k)<\infty\), define for \(1\le p<\infty\)
\[
D_{n,p}(g)^p=\sum_{k\ge0}g(k)|W_n(k)-1|^p,
\]
and \(D_{n,\infty}(g)=\sup_{k\ge0}g(k)|W_n(k)-1|\). If \(Z\sim\operatorname{Pois}(c/r!)\), then jointly for any finite collection of positive summable weights and any finite collection of exponents,
\[
D_{n,p}(g)^p\ \Longrightarrow\ g(r)\left|\frac{r!Z}{c}-1\right|^p+\sum_{k\ge r+1}g(k),\qquad 1\le p<\infty,
\]
\[
D_{n,\infty}(g)\ \Longrightarrow\
\max\left\{g(r)\left|\frac{r!Z}{c}-1\right|,\ \sup_{k\ge r+1}g(k)\right\}.
\]
The *same* \(Z\) drives all these limits. Every fixed-weight limiting distance is bounded strictly away from zero, since \(g(k)>0\) for all \(k\).

By contrast, for either **random weight** \(g_n(k)=\widehat p_n(k)\) or \(g_n(k)=p_{\widehat\lambda_n}(k)\), for every fixed \(1\le p\le\infty\),
\[
D_{n,p}(g_n)\xrightarrow{\mathbb P}0.
\]
Thus, at the same valid Poisson null, all three fixed-Laplace-weight distances have nonzero discrete limits, while the six empirical- or fitted-Poisson-weight counterparts vanish (up to any conventional squaring of the \(L_2\) distance).

**Plateau law.** More generally, if \(\lambda_n\to0\), \(n\lambda_n^r\to\infty\), and \(n\lambda_n^{r+1}\to0\) for fixed \(r\ge1\), then
\[
D_{n,p}(g)^p\xrightarrow{\mathbb P}\sum_{k\ge r+1}g(k),\qquad
D_{n,\infty}(g)\xrightarrow{\mathbb P}\sup_{k\ge r+1}g(k),
\]
for fixed positive summable \(g\), whereas either data-adaptive weighting yields convergence to zero. The critical and plateau laws form a staircase indexed by the highest populated count cell.

**Numerical illustration.** For \(g(k)=e^{-k}\), \(r=2\), and \(n\lambda_n^2\to2\), write \(Z\sim\operatorname{Pois}(1)\). The unrooted weighted \(L_1\) distance satisfies
\[
D_{n,1}(g)\Longrightarrow \frac{e^{-3}}{1-e^{-1}}+e^{-2}|Z-1|.
\]
Its strictly positive minimum is \(0.0787619824612714\ldots\), attained by the limiting variable with probability \(e^{-1}\). Its limit is discrete, not asymptotically normal or convergent to zero.

## Assumptions and scope

The triangular-array entries within each row are independent and identically Poisson, with strictly positive \(\lambda_n\). Only fixed count index \(r\) and fixed weighted-distance exponent \(p\) are asserted. No uniformity in \(r\), moving weight sequence other than the two specified probability mass weights, or joint asymptotics over an unbounded collection of exponents is claimed. The fitted parameter is the sample mean, exactly as in [1]. For \(p=\infty\), the weight multiplies the absolute difference before taking the supremum. Fixed \(g\) must be positive and summable. The original exponential family \(g(k)=e^{-ak}\), \(a>0\), satisfies these hypotheses.

For \(\widehat\lambda_n=0\) the original ratio at positive counts is undefined, but the probability of that event equals \(e^{-n\lambda_n}\), which tends to zero under every regime stated here. Its arbitrary completion does not change the conclusions.

## Proof

Write \(N_{n,k}=\sum_i\mathbf1_{\{X_{n,i}=k\}}\) and \(q_{n,k}=p_{\lambda_n}(k)\).

**1. Fitted mean and common-cell ratios.** Under the critical conditions, \(n\lambda_n\to\infty\), since \(r\ge2\) and \(n\lambda_n^r\to c\). Furthermore
\[
\operatorname{Var}\!\left(\frac{\widehat\lambda_n}{\lambda_n}\right)=\frac{1}{n\lambda_n}\longrightarrow0,
\]
so \(\widehat\lambda_n/\lambda_n\to1\) in probability. For every fixed \(0\le k<r\), \(nq_{n,k}\sim n\lambda_n^k/k!\to\infty\). Binomial Chebyshev gives \(N_{n,k}/(nq_{n,k})\to1\) in probability. The fitted-to-true cell probability ratio obeys
\[
\frac{p_{\widehat\lambda_n}(k)}{q_{n,k}}=e^{-(\widehat\lambda_n-\lambda_n)}\left(\frac{\widehat\lambda_n}{\lambda_n}\right)^k\xrightarrow{\mathbb P}1.
\]
Hence \(W_n(k)\to1\) in probability for every \(k<r\), simultaneously over finitely many such cells.

**2. Rare cell and empty higher cells.** The cell \(r\) count is binomial with success probability \(q_{n,r}\sim\lambda_n^r/r!\). Thus \(nq_{n,r}\to c/r!\), while \(nq_{n,r}^2\to0\). Its probability generating function \([1+q_{n,r}(z-1)]^n\) tends to \(\exp[(c/r!)(z-1)]\), proving \(N_{n,r}\Rightarrow Z\sim\operatorname{Pois}(c/r!)\). Moreover
\[
np_{\widehat\lambda_n}(r)
=n e^{-\widehat\lambda_n}\widehat\lambda_n^r/r!
\xrightarrow{\mathbb P}c/r!.
\]
Slutsky's theorem yields \(W_n(r)\Rightarrow r!Z/c\). Finally, the union bound and the Poisson upper-tail series give
\[
\Pr\{\max_iX_{n,i}\ge r+1\}\le n\Pr\{X_{n,1}\ge r+1\}
=O(n\lambda_n^{r+1})\longrightarrow0.
\]
Thus with probability tending to one, \(N_{n,k}=0\), and hence \(W_n(k)=0\), *simultaneously for every* \(k>r\).

**3. Fixed-weight limits.** On the preceding high-probability event the entire infinite tail is exactly \(\sum_{k>r}g(k)\) in the \(p\)-th power of the finite-\(p\) distance, and exactly \(\sup_{k>r}g(k)\) in the weighted supremum. The finitely many lower-cell terms vanish and the cell \(r\) converges to the displayed rare-Poisson coordinate. The continuous mapping and Slutsky theorems prove both limits and their finite joint versions. Positivity of the tail follows from \(g(r+1)>0\).

**4. Data-adaptive weights.** For each \(k<r\), both \(\widehat p_n(k)\le1\) and \(p_{\widehat\lambda_n}(k)\le1\), while \(|W_n(k)-1|\to0\). At \(k=r\), \(W_n(r)=O_{\mathbb P}(1)\), \(\widehat p_n(r)=O_{\mathbb P}(1/n)\), and \(p_{\widehat\lambda_n}(r)=O_{\mathbb P}(1/n)\). Beyond \(r\), the empirical weight is identically zero on the high-probability event, whereas the fitted-Poisson weight of the unseen tail is \(\Pr_{\widehat\lambda_n}\{X\ge r+1\}=o_{\mathbb P}(1)\). This handles the finite-\(p\) sums. For the supremum, use \(\sup\le\sum\) on the fitted tail, and the same bounded finite-cell factors elsewhere. All adaptive distances tend to zero.

**5. Plateaus.** If \(n\lambda_n^r\to\infty\) and \(n\lambda_n^{r+1}\to0\), then \(n\lambda_n\to\infty\), all ratios \(W_n(k)\to1\) for \(k\le r\) by the argument in step 1, and all larger cells are absent with probability tending to one by step 2. The same finite-sum and exact-tail decomposition gives the deterministic plateau, while the adaptive-weight tail vanishes. This also establishes the \(r=1\) plateau case.

## Verification

The standalone `verify.py` uses only Python's standard library. It checks exact geometric-tail identities; binomial rare-cell probabilities against their Poisson limits; and directly computed finite-histogram \(L_1\), \(L_2\), and \(L_\infty\) scores against their limiting formulas for two critical count indices, three exponential weights, and both adaptive weight schemes. The packaged checker passed 367 assertions. No simulation, numerical check, or finite enumeration is used as a substitute for the general proof above.

## Relationship to prior work

Kirui et al. [1] define the empirical-weight ratio, all three weights (fitted Poisson pmf, empirical pmf, exponential), and \(L_1\), \(L_2\), \(L_\infty\) scores, reporting finite-sample simulation results for fixed Poisson means. Kirui's earlier thesis [2] provides the same construction and finite-sample comparisons. Neither source's relevant development and conclusions state the critical \(n\lambda_n^r\) Poisson staircase, its shared rare-cell limit, or the separation of fixed versus adaptive weights. This result uses the existing statistic rather than claiming its invention.

The standard binomial-to-Poisson rare-event limit is an ingredient, not claimed as new. The distinct new statement is the joint asymptotic behavior of the complete infinite-support weight-ratio distances and the six-versus-three weighting contrast, including exact nonzero unseen-cell tails. Earlier Stein–Chen count goodness-of-fit asymptotics [3] concern a different class of scalar characterization statistics and do not imply these empirical histogram-ratio limits.

## Limitations

This is an exact asymptotic null description under shrinking means, not a demonstration of erroneous finite-sample bootstrap size. Parametric bootstrap behavior at discontinuity points of the discrete limits, local-alternative power, and uniformly growing count levels are not proved. The original tests remain well-defined and usable for positive sample means; this theorem does not disprove fixed-mean consistency or the authors' finite-mean simulation conclusions. The historical literature comparison cannot exclude every earlier derivation of a similar occupancy regime.

## References

[1] Kirui, W., Bothma, E., Smuts, M., Steyn, A., Visagie, I. J. H. *On new tests for the Poisson distribution based on empirical weight functions*. arXiv:2402.12866v1 (publicly posted 2024-02-20); *South African Statistical Journal* 59 (2025), 21–36, doi:10.37920/sasj.2025.59.1.2. https://arxiv.org/abs/2402.12866

[2] Kirui, W. C. *On a new class of tests for the Poisson distribution based on empirical weight functions*. MSc dissertation, North-West University (graduation May 2023). https://repository.nwu.ac.za/bitstreams/6bc2adcb-3dbb-4312-b440-4d92cc48d5f6/download

[3] Aleksandrov, B., Weiß, C. H., Jentsch, C. *Goodness-of-fit tests for Poisson count time series based on the Stein–Chen identity*. *Statistica Neerlandica* 76 (2022), 35–64, doi:10.1111/stan.12252. https://doi.org/10.1111/stan.12252
