# Uniformity as the unique perfect first-order Gini–variance alignment

## Finding
Let \(X_1,X_2,\ldots\) be independent with a common **non-atomic**, nondegenerate probability law \(F\) on \(\mathbb R\), with finite fourth moment. For \(n\ge2\), define the sample Gini mean difference and unbiased sample variance by
\[
G_n=\binom n2^{-1}\sum_{i<j}|X_i-X_j|,
\qquad S_n^2=\binom n2^{-1}\sum_{i<j}\frac{(X_i-X_j)^2}{2}.
\]
Then the limiting Pearson correlation \(\rho(F)=\lim_{n\to\infty}\operatorname{Corr}(G_n,S_n^2)\) exists, and
\[
\boxed{\rho(F)=1\ \Longleftrightarrow\ F\text{ is uniform on a nondegenerate finite interval}.}
\]
Indeed, \(|\rho(F)|=1\) is possible only in this uniform case. This characterizes precisely when these distinct dispersion estimators have the same first-order random fluctuation after deterministic rescaling.

In the uniform case on an interval of length \(\ell>0\), their **exact finite-sample** correlation and the variance of the difference of their natural normalizations are
\[
\boxed{\operatorname{Corr}(G_n,S_n^2)=\frac{\sqrt2(n+2)}{\sqrt{(n+3)(2n+3)}}},\qquad
\boxed{\operatorname{Var}\left(\frac{G_n}{\ell}-\frac{2S_n^2}{\ell^2}\right)=\frac1{90n(n-1)}}.
\]
For normalized observations \(U_i=(X_i-a)/\ell\) and empirical CDF \(F_n\), let the classical Watson uniformity statistic be
\[
W_n^2=n\int_0^1\left[F_n(t)-t-\int_0^1(F_n(s)-s)\,ds\right]^2dt.
\]
For **every deterministic sample** in the interval, not merely in distribution,
\[
\boxed{(n-1)\left(\frac{G_n}{\ell}-\frac{2S_n^2}{\ell^2}-\frac16\right)=\frac16-2W_n^2.}
\]
Consequently, for independent standard-normal variables \(Z_{k,1},Z_{k,2}\),
\[
n\left(\frac{G_n}{\ell}-\frac{2S_n^2}{\ell^2}-\frac16\right)
\ \xrightarrow{d}\ \frac16-\frac1{2\pi^2}\sum_{k=1}^{\infty}\frac{Z_{k,1}^2+Z_{k,2}^2}{k^2}.
\]
The series converges almost surely and in \(L^2\). The limit is centered, non-Gaussian, and has variance \(1/90\).

## Assumptions and scope
Non-atomic means no point masses; a density or connected support is **not** assumed in the characterization. Nondegeneracy and a finite fourth moment guarantee that the relevant second moments and nonzero first-order projection variances exist. The exact formulas and Watson identity use a known fixed interval \([a,a+\ell]\), with \(\ell>0\), and the usual unbiased sample variance, not the root-mean-square sample deviation. For a general nonuniform law, the limit of the Pearson correlation need not equal one and the uniform Watson calibration does not apply.

## Proof
**1. First-order characterization.** Put \(A(x)=\mathbb E|x-X|\) and \(B(x)=\mathbb E(x-X)^2=(x-\mu)^2+\sigma^2\), where \(X\sim F\). The order-two Hoeffding decomposition gives
\[
\rho(F)=\operatorname{Corr}(A(X),B(X)).
\]
Both projection variances are positive for an atomless nondegenerate law: the functions are continuous, and vanishing projection variance would make one of the functions constant on the perfect support of \(F\), which contradicts its derivative and the nonconstant CDF.

Suppose \(|\rho(F)|=1\). Equality in Cauchy–Schwarz yields \(A(X)=cB(X)+d\) almost surely for constants \(c\ne0,d\). By continuity this holds at every point in the support \(S\) of \(F\). Since \(F\) is atomless, its support has no isolated points. Therefore the differentiable function \(A-cB-d\), which vanishes on \(S\), has zero derivative throughout \(S\). Using
\[
A'(x)=2F(x)-1,\qquad B'(x)=2(x-\mu),
\]
we find
\[
F(x)=\frac12+c(x-\mu)\qquad(x\in S).
\]
Monotonicity and nondegeneracy force \(c>0\). This affine identity rules out unbounded support. If a bounded complementary interval \((u,v)\) separated two portions of \(S\), then \(u,v\in S\), and \(F(u)=F(v)\), contradicting \(c>0\) and \(u<v\). Thus \(S=[a,b]\) is an interval and the CDF is affine on it. Normalization gives \(F(x)=(x-a)/(b-a)\): the law is uniform. Conversely, uniformity makes \(A\) and \(B\) affine transforms, hence \(\rho=1\). This also excludes \(\rho=-1\).

**2. Exact finite moments.** Scale to \([0,1]\) and write \(Q_n=2S_n^2\). For independent uniforms \(U,V\), the density of \(|U-V|\) is \(2(1-t)\), so \(\mathbb E|U-V|^r=2/((r+1)(r+2))\) for each nonnegative integer \(r\). The two conditional kernels are
\[
\mathbb E(|U-V|\mid U=x)=x^2-x+\tfrac12,\qquad
\mathbb E((U-V)^2\mid U=x)=x^2-x+\tfrac13.
\]
Their centered projections coincide and have variance \(1/180\). For a common pair, the kernel variances are \(1/18\) and \(7/180\), and their covariance is \(2/45\). Distinct pairs sharing exactly one index contribute \(1/180\); disjoint pairs contribute zero. Enumerating these overlaps gives
\[
\operatorname{Var}(G_n)=\frac{n+3}{45n(n-1)},\quad
\operatorname{Var}(Q_n)=\frac{2n+3}{90n(n-1)},\quad
\operatorname{Cov}(G_n,Q_n)=\frac{n+2}{45n(n-1)}.
\]
The stated correlation and contrast variance follow, with the correct powers of \(\ell\) restored by scaling.

**3. Watson identity.** Let \(B_2(t)=t^2-t+1/6\) for \(0\le t\le1\). The Fourier expansion \(B_2(t)=\pi^{-2}\sum_{k\ge1}\cos(2\pi kt)/k^2\), together with Parseval's identity for the centered empirical bridge, yields the exact relation
\[
W_n^2=\frac1{2n}\sum_{i,j=1}^{n}B_2(|U_i-U_j|).
\]
Since \(B_2(0)=1/6\) and \(|u-v|-(u-v)^2-1/6=-B_2(|u-v|)\), separation into diagonal and off-diagonal terms gives the asserted sample-wise identity.

**4. Non-Gaussian second-order limit.** For fixed frequencies, the multivariate CLT applied to \(\sqrt n( n^{-1}\sum_j\cos(2\pi kU_j),n^{-1}\sum_j\sin(2\pi kU_j))\) gives independent centered normal components of variance \(1/2\). Parseval represents \(W_n^2\) as \(n/(2\pi^2)\sum_{k\ge1}k^{-2}|n^{-1}\sum_j e^{2\pi ikU_j}|^2\). The expected tail beyond frequency \(K\) is bounded by \((2\pi^2)^{-1}\sum_{k>K}k^{-2}\), uniformly in \(n\), allowing convergence of the infinite series. The Watson identity then gives the displayed limit. Its variance is \(\pi^{-4}\sum_{k\ge1}k^{-4}=1/90\).

## Verification
Run \(\texttt{python3 checker.py}\) with Python 3. This standard-library checker verifies the rational kernel moments, the exact covariance identities for \(2\le n\le120\), the Watson identity for a large deterministic family of rational samples with repeated endpoints, and Fourier partial sums. It passed 56,331 assertions when checked. These computations verify finite algebra and instances; they do not replace the support-characterization proof or the infinite-series limit argument.

## Relationship to prior work
Hoeffding's order-two \(U\)-statistics theory provides the general first-projection framework; the Gini mean difference and sample variance are standard examples. Gerstenberger and Vogel (2014, arXiv:1405.5027v1, Sections 2–3) compute general influence functions and observe equal asymptotic efficiencies for the uniform law, but do not give the non-atomic **if-and-only-if** classification or the paired finite-sample Watson identity established here. Čiginas and Pumputis (2014, arXiv:1406.2275, Sections 1 and 3) examine the two estimators under finite-population sampling without replacement, rather than the stated iid characterization. Fortiana and Grané (2003) directly connect the empirical Gini mean difference with a standardized maximum correlation and the sample variance under uniformity; their test uses the Gini statistic rather than the Gini-minus-variance Watson contrast. The Watson uniformity statistic and its limiting distribution are classical, **not claimed as new**: the exact identity specifies which contrast of two scale estimators it equals. Related finite-sample Gini/variance covariance calculations under exponential sampling and Gini–Greenwood correlations for spacings concern different sampling laws or objects. The additional statement is the uniqueness of uniformity in the first-order alignment together with its exact second-order contrast interpretation.

## Limitations
Historical priority for the uniqueness formulation has not been independently certified. Some older Gini/Watson literature was accessible only through abstracts or bibliographic records; a differently named distribution-characterization theorem may exist. This does not characterize distributions with atoms, and no quantitative stability bound for near-perfect correlation is established. The known-interval normalization is essential to the exact Watson representation; substituting data-dependent endpoints would require a different null law.

## References
- Gerstenberger, C., and Vogel, D. *On the efficiency of Gini's mean difference*. arXiv:1405.5027v1, first posted 2014-05-20. https://arxiv.org/html/1405.5027v1
- Čiginas, A., and Pumputis, D. *Gini's mean difference and variance as measures of finite populations scales*. arXiv:1406.2275, first posted 2014-06-09. https://arxiv.org/abs/1406.2275
- Fortiana, J., and Grané, A. *Goodness-of-fit tests based on maximum correlations and their orthogonal decompositions*. Journal of the Royal Statistical Society: Series B 65 (2003), 115–126. https://halweb.uc3m.es/esp/Personal/personas/agrane/ficheros_articulos/JRSSB2003.pdf
- Tung, D. D., and Jammalamadaka, S. R. *On the Gini Mean Difference Test for Circular Data*. Published online 2013-04-25. https://doi.org/10.1080/03610926.2011.601947
- Watson, G. S. *Goodness-of-fit tests on a circle*. Biometrika 48 (1961), 109–114. Classical uniformity statistic; bibliographic reference, not a novelty claim.
- Hoeffding, W. *A class of statistics with asymptotically normal distribution*. Annals of Mathematical Statistics 19 (1948), 293–325.
