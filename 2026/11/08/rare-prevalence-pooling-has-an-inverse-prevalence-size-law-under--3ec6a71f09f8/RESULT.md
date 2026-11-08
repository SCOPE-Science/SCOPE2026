# Rare-prevalence pooling has an inverse-prevalence size law under beta-binomial clustering

## Finding

For a perfect two-stage Dorfman infection-screening procedure applied to exchangeable beta-binomial infection indicators, the optimal common pool size is eventually proportional to the *inverse* prevalence, rather than to its inverse square root. There is also an exact global finite-size unimodality law throughout a natural low-prevalence region.

Write the pairwise infection correlation as \(\rho\in(0,1)\), and let \(\kappa=\rho^{-1}-1>0\). For prevalence \(p\in(0,1)\) put \(\alpha=\kappa p\) and \(\beta=\kappa(1-p)\). If \(\alpha<1\), define
\[
Q_k=\prod_{j=0}^{k-1}\frac{\beta+j}{\kappa+j},\qquad
H_k=\frac{\alpha k(k+1)Q_k}{\kappa+k}\quad(k\ge1).
\]
Then \(H_k\) is strictly increasing from \(H_1<1\) to infinity. The smallest integer \(K\ge1\) satisfying \(H_K\ge1\) is at least two and is a globally optimal Dorfman pool size among **all** positive integer pool sizes, including individual testing. It is the unique optimum if \(H_K>1\); if \(H_K=1\), the *only* optima are \(K\) and \(K+1\). The minimum test count per person is strictly below one.

For every fixed \(\kappa>0\), as \(p\downarrow0\), every optimal size \(K_p\) obeys
\[
\boxed{\kappa p K_p\longrightarrow1},\qquad
\boxed{\min_k C_k=\kappa p\left[\log\frac1{\kappa p}+1-\psi(\kappa)\right]+o(p)},
\]
where \(\psi=\Gamma'/\Gamma\) is the digamma function. Thus \(K_p\sim1/(\kappa p)\), and the optimum tests per person are of order \(p\log(1/p)\). In contrast, for independent infections the classical optimum is \(\sim2\sqrt p\) tests per person at pool size \(\sim p^{-1/2}\).

## Assumptions and scope

Fix \(p\in(0,1)\) and \(\rho\in(0,1)\). Draw a latent prevalence \(U\sim\operatorname{Beta}(\alpha,\beta)\) with \(\alpha=\kappa p\), \(\beta=\kappa(1-p)\), and \(\kappa=\rho^{-1}-1\). Conditional on \(U\), specimens within a pool are independent Bernoulli\((U)\). This gives marginal prevalence \(p\) and intracluster correlation \(\rho\). One pool of size \(k\ge2\) is tested once, and all \(k\) specimens are individually retested precisely when the pool is positive. All tests are noiseless; there is no dilution, no maximum pool capacity, and no testing-time constraint. A singleton is directly tested once, without a redundant retest.

The normalized expected test use is \(C_1=1\), whereas for \(k\ge2\), \(C_k=1/k+1-Q_k\) with \(Q_k=\Pr(\text{all }k\text{ specimens negative})\). Fixed \(\rho\) is essential in the rare-prevalence asymptotic; changing \(\rho\) together with \(p\) is not included. A single latent prevalence may govern arbitrarily large exchangeable pools; finite clusters impose separate size constraints.

## Proof

**Exact negative-pool probability.** Conditional independence gives \(Q_k=\mathbb E[(1-U)^k]\). Evaluating the beta integral yields
\[
Q_k=\frac{B(\alpha,\beta+k)}{B(\alpha,\beta)}
=\frac{\Gamma(\kappa)\Gamma(\beta+k)}{\Gamma(\beta)\Gamma(\kappa+k)}
=\prod_{j=0}^{k-1}\frac{\beta+j}{\kappa+j}.
\]
Consequently \(Q_{k+1}=Q_k(\beta+k)/(\kappa+k)\). For \(k\ge2\), or algebraically extending the pooled cost to \(k=1\), the first difference is
\[
\left(\frac1{k+1}+1-Q_{k+1}\right)-\left(\frac1k+1-Q_k\right)
=\frac{H_k-1}{k(k+1)}.
\]
The special singleton cost is \(C_1=1\), while the formal extension at one is \(1+p\); thus the first difference identity is used only from \(k\ge2\).

**One exact crossing.** Direct cancellation gives
\[
\frac{H_{k+1}}{H_k}=
\frac{(k+2)(\kappa+k-\alpha)}{k(\kappa+k+1)}.
\]
The numerator minus denominator equals \(k(1-\alpha)+2(\kappa-\alpha)>0\) whenever \(0<\alpha<1\). Moreover
\[
H_1=\frac{2\alpha(\kappa-\alpha)}{\kappa(\kappa+1)}
\le\frac{\kappa}{2(\kappa+1)}<1.
\]
The standard gamma ratio, which also follows by summing \(\log(1-\alpha/(\kappa+j))\), gives
\[
Q_k\sim\frac{\Gamma(\kappa)}{\Gamma(\kappa-\alpha)}k^{-\alpha},\qquad
H_k\sim\frac{\alpha\Gamma(\kappa)}{\Gamma(\kappa-\alpha)}k^{1-\alpha}\longrightarrow\infty.
\]
Hence a first crossing \(K\ge2\) exists. From the difference formula the pooled costs strictly decrease before \(K\), then strictly increase after \(K\), with exactly one possible adjacent tie when \(H_K=1\). Finally \(C_k-1=1/k-Q_k<0\) for all sufficiently large \(k\), since \(\alpha<1\). Thus this pooled minimum also strictly beats the distinct singleton cost \(1\).

**Rare-prevalence location.** Now fix \(\kappa>0\) and let \(\alpha=\kappa p\downarrow0\). For \(k=\lfloor t/\alpha\rfloor\) with any fixed \(t>0\), uniformly for \(t\) in compact subsets of \((0,\infty)\),
\[
\log Q_k=\sum_{j=0}^{k-1}\log\left(1-\frac{\alpha}{\kappa+j}\right)
=-\alpha[\psi(\kappa+k)-\psi(\kappa)]+O(\alpha^2)
=-\alpha[\log k-\psi(\kappa)]+o(\alpha).
\]
Here the quadratic remainder is \(O(\alpha^2\sum_{j\ge0}(\kappa+j)^{-2})\), and \(\psi(\kappa+k)=\log k+o(1)\). Therefore \(Q_k\to1\) and \(H_k\to t\). Strict monotonicity brackets the first crossing between \(\lfloor t_-/\alpha\rfloor\) and \(\lceil t_+/\alpha\rceil\) for any \(0<t_-<1<t_+\); consequently \(\alpha K_p\to1\), including either member of a tied pair.

**Rare-prevalence cost.** At \(k=K_p\sim\alpha^{-1}\), the preceding expansion gives \(\log Q_k=-\alpha[\log(1/\alpha)-\psi(\kappa)]+o(\alpha)\), and \((\log Q_k)^2=O(\alpha^2\log^2(1/\alpha))=o(\alpha)\). Thus \(1-Q_k=\alpha[\log(1/\alpha)-\psi(\kappa)]+o(\alpha)\). Because \(1/K_p=\alpha+o(\alpha)\), the claimed cost follows. A tied optimum has exactly the same cost.

For comparison, under independent Bernoulli\((p)\) status the corresponding pooled cost is \(1/k+1-(1-p)^k\). The leading terms for \(k\sim t/\sqrt p\) are \(\sqrt p(t+t^{-1})\), uniquely minimized at \(t=1\). A candidate \(k=\lceil p^{-1/2}\rceil\) has cost \(2\sqrt p+o(\sqrt p)\). Conversely, any near-minimizer must satisfy \(1/k=O(\sqrt p)\) and \(1-(1-p)^k=O(\sqrt p)\), whence \(k=\Theta(p^{-1/2})\). The compact rescaled minimum therefore is \(2\sqrt p\), as claimed.

## Verification

The standalone `CHECK.py` evaluates the beta-binomial zero-pool probability by two independent exact-rational representations, reconstructs the finite difference of normalized Dorfman test use and verifies the strict increase of \(H_k\) across a parameter grid. It also checks numerical approach of the optimizer and minimum cost to their proved rare-prevalence limits at three fixed correlation levels. Running `python CHECK.py` requires only the Python standard library. Finite checks are diagnostics; they do not establish the all-parameter or asymptotic statements proved above.

## Relationship to prior work

Lendle, Hudgens and Qaqish (first exact-day online publication September 27, 2011; a technical report is also catalogued by the month October 2010) introduce beta-binomial clustered group testing and derive the negative-pool probability and two-stage expected test use. These ingredients are **not claimed as new**. Basso and colleagues (online 2021) compare beta-binomial and independent optimized pooling and show that correlated-model optimal pool sizes are no smaller under perfect tests; their published capped-size numerical studies do not give the unrestricted integer one-crossing criterion or its fixed-correlation rare-prevalence scale. Landolfi and Lall (preprint 2023) present a more general finite-population exchangeable-partition optimization, but their finite-population characterization does not state this beta-binomial infinite-size asymptotic. The contribution here is the exact discrete unimodality and the inverse-prevalence/logarithmic-cost asymptotic, not the model, Dorfman protocol, or generic exchangeable partition formula.

## Limitations

The extrapolation to arbitrarily large exchangeable pools assumes an unlimited cluster size and no dilution or assay capacity ceiling. These assumptions can fail in real laboratory screening. For finite clusters, the optimum is truncated by the cluster limit, and neither the inverse-prevalence scale nor its test savings need be achievable. The analysis does not optimize multistage protocols, costs of delayed classification, error probabilities, or uncertain prevalence. No independent review or historical-priority certification is asserted; an equivalent asymptotic calculation in other pooled-testing literature remains possible. Publication metadata for the 2010 precursor identify a month but not a precise public day; the exact-day source date used in metadata is September 27, 2011.

## References

1. Lendle, Hudgens and Qaqish, *Group Testing for Case Identification with Correlated Responses*, Biometrics 68 (2012), first online September 27, 2011, https://doi.org/10.1111/j.1541-0420.2011.01674.x; earlier month-only working-paper record https://biostats.bepress.com/uncbiostat/art16/.
2. Basso, Salinas, Sauré, Thraves and Yankovic, *The effect of correlation and false negatives in pool testing strategies for COVID-19*, Health Care Management Science 25 (2022), first online August 28, 2021, https://doi.org/10.1007/s10729-021-09578-w.
3. Landolfi and Lall, *Optimal Dorfman Group Testing for Symmetric Distributions*, arXiv:2308.11050 (2023), https://arxiv.org/abs/2308.11050.
4. Dorfman, *The Detection of Defective Members of Large Populations*, Annals of Mathematical Statistics 14 (1943), https://doi.org/10.1214/aoms/1177731363.
