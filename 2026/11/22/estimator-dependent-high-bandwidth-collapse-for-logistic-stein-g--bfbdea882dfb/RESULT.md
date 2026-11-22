# Estimator-dependent high-bandwidth collapse for logistic Stein goodness-of-fit

## Finding

For the Gaussian-frequency-weighted logistic Fourier–Stein goodness-of-fit statistic of Allison, Ebner and Smuts, the large-bandwidth limit depends qualitatively on whether parameters are fitted by moments or maximum likelihood. Under a standard logistic null, for **every** deterministic positive sequence \(a_n\to\infty\),
\[
 a_n^{1/2}T_{n,a_n}^{\mathrm{MO}}\Rightarrow \sqrt\pi\,\frac{\pi^2-9}{27}\chi_1^2,
 \qquad
 a_n^{5/2}T_{n,a_n}^{\mathrm{ML}}\Rightarrow
 \frac{3\sqrt\pi}{4}\left(\frac{7\pi^4}{180}-\frac{(\pi^2-6)^2}{108}\right)\chi_1^2.
\]
The limiting coefficients are, respectively, approximately \(0.0570864322028\) and \(4.85140736494\). The exponents \(1/2\) and \(5/2\) are sharp because both asymptotic variances are strictly positive.

## Assumptions and scope

Let \(X_1,X_2,\ldots\) be independent identically distributed observations with density \(f(x)=1/(4\cosh^2(x/2))\) on \(\mathbb R\). Write \(g(x)=\tanh(x/2)\). For each \(n\), define \(Y_j=(X_j-\widehat\mu_n)/\widehat\sigma_n\). In the method-of-moments (MO) version, \(\widehat\mu_n=\bar X_n\) and \(\widehat\sigma_n=(\sqrt3/\pi)\{n^{-1}\sum_j(X_j-\bar X_n)^2\}^{1/2}\). In the maximum-likelihood (ML) version, use the ordinary joint interior location-scale logistic MLE; it exists almost surely for nonconstant samples for all sufficiently large \(n\). Define
\[
 H_n(t)=\frac1n\sum_{j=1}^n (it-g(Y_j))e^{itY_j},\qquad
 T_{n,a}=n\int_{\mathbb R}|H_n(t)|^2e^{-at^2}\,dt.
\]
The superscripts distinguish the two fitted parameter pairs. The bandwidth \(a_n\) is any deterministic real sequence tending to positive infinity; no relation to sample size is assumed. Only the logistic composite-null law of the raw statistic is asserted.

## Proof

**1. Exact score cancellation and Taylor coefficients.** Let \(K(t,y)=(it-g(y))e^{ity}\). Its Taylor expansion at frequency zero is
\[
 K(t,y)=-g(y)+it[1-yg(y)]+t^2h(y)+O(t^3(1+|y|^3)),
 \qquad h(y)=\tfrac12y^2g(y)-y,
\]
where the remainder bound holds for all real \(t\) in \([-1,1]\), with a polynomial in \(|y|\) large enough to bound derivatives of order three. The logistic likelihood score equations are exactly
\[
 \overline{g(Y)}=0,\qquad \overline{Yg(Y)}=1.
\]
Thus ML gives \(H_n(0)=H_n'(0)=0\) and \(H_n''(0)/2=\overline{h(Y)}\); for MO, \(H_n(0)=-\overline{g(Y)}\). These are identities for each admissible sample, not asymptotic approximations.

**2. Uniform-in-bandwidth remainder.** Set \(Z_n(t)=\sqrt n H_n(t)\). Standard root-\(n\) expansions of both location-scale estimators give \(\sqrt n(|\widehat\mu_n|+|\widehat\sigma_n-1|)=O_{\mathbb P}(1)\). The population Stein identity \(\mathbb E K(t,X)=0\) holds for every real \(t\), and hence all frequency derivatives of this expectation vanish. For \(k\le4\), the independent centered processes \(n^{-1/2}\sum K^{(k)}(t,X_j)\) have bounded expected squared \(L^2([-1,1])\) norms. Applying the one-dimensional Sobolev inequality to derivatives of consecutive orders yields \(\sup_{|t|\le1}|n^{-1/2}\sum K^{(k)}(t,X_j)|=O_{\mathbb P}(1)\), for \(k\le3\). The residual-estimation perturbation has the same property, because \(|\partial_y K^{(k)}(t,y)|\le C_k(1+|y|^{k+2})\) for \(|t|\le1\), and the fitted parameter errors are root-\(n\) bounded. Consequently, uniformly for \(|t|\le1\),
\[
 Z_n^{\mathrm{MO}}(t)=-\sqrt n\,\overline{g(Y^{\mathrm{MO}})}+tO_{\mathbb P}(1),\qquad
 Z_n^{\mathrm{ML}}(t)=t^2\sqrt n\,\overline{h(Y^{\mathrm{ML}})}+t^3O_{\mathbb P}(1).
\]
Here \(t^kO_{\mathbb P}(1)\) denotes a single random bound uniform for the stated frequency interval. On the complement \(|t|>1\), decompose \(Z_n(t)\) into its centered independent raw-observation process and its fitted-residual perturbation. The first has \(\mathbb E|n^{-1/2}\sum K(t,X_j)|^2\le (1+|t|)^2\); by the global derivative bound \(|\partial_y K(t,y)|\le C(1+t^2)\), the second is bounded by \(O_{\mathbb P}(1)(1+t^2)\). Therefore the Gaussian-weighted tail, multiplied by either \(a_n^{1/2}\) or \(a_n^{5/2}\), tends to zero in probability for every diverging \(a_n\), with **no hidden factor \(n\)**. With \(u=\sqrt{a_n}t\), dominated stochastic Taylor control now gives
\[
 a_n^{1/2}T_{n,a_n}^{\mathrm{MO}}=\sqrt\pi\,n\overline{g(Y^{\mathrm{MO}})}^2+o_{\mathbb P}(1),
 \quad
 a_n^{5/2}T_{n,a_n}^{\mathrm{ML}}=\frac{3\sqrt\pi}{4}n\overline{h(Y^{\mathrm{ML}})}^2+o_{\mathbb P}(1),
\]
using \(\int_\mathbb R e^{-u^2}du=\sqrt\pi\) and \(\int_\mathbb R u^4e^{-u^2}du=3\sqrt\pi/4\).

**3. Influence functions and exact constants.** The logistic Stein identity gives \(\mathbb E q'(X)=\mathbb E[q(X)g(X)]\) for admissible smooth \(q\). The centered location influence function is \(X\) for MO and \(3g(X)\) for ML. Since \(g\) and \(h\) are odd, their first-order scale-estimation corrections vanish by symmetry; furthermore \(\mathbb Eg'(X)=1/3\) and \(\mathbb Eh'(X)=(\pi^2-6)/18\). Thus
\[
 \sqrt n\,\overline{g(Y^{\mathrm{MO}})}=\frac1{\sqrt n}\sum_j\left(g(X_j)-\frac{X_j}3\right)+o_{\mathbb P}(1),
\]
\[
 \sqrt n\,\overline{h(Y^{\mathrm{ML}})}=\frac1{\sqrt n}\sum_j\left(h(X_j)-\frac{\pi^2-6}6g(X_j)\right)+o_{\mathbb P}(1).
\]
The logistic moment-generating function is \(M(s)=\pi s/\sin(\pi s)\) for \(|s|<1\), and directly integrating with \(u=(1+e^{-X})^{-1}\) gives \(\mathbb E[e^{sX}g(X)^2]=(1+2s^2)M(s)/3\). Consequently \(\mathbb E g^2=1/3\), \(\mathbb E[Xg]=1\), \(\mathbb E[X^2]=\pi^2/3\), \(\mathbb E[hg]=(\pi^2-6)/18\), and \(\mathbb E h^2=7\pi^4/180\). The two centered influence variances are exactly
\[
 V_{\mathrm{MO}}=\frac{\pi^2-9}{27}>0,
\qquad
 V_{\mathrm{ML}}=\frac{7\pi^4}{180}-\frac{(\pi^2-6)^2}{108}>0.
\]
The scalar central limit theorem and continuous mapping applied to the expansions in step 2 complete the proof.

## Verification

The standalone Python/SciPy checker at `checks/check_logistic.py` numerically verifies the stated exact moment identities against independent quadrature, positivity and values of both limiting constants, the maximum-likelihood score constraints, and the finite-sample Gaussian-weight frequency integral against its leading asymptotic expression at three large bandwidths. Fifteen assertions passed in the packaged test. The mathematical proof is analytic; finite numerical checks are not used as proof of a triangular-array limit.

## Relationship to prior work

Allison, Ebner and Smuts (arXiv:2108.07036, posted 16 August 2021; later Statistica Neerlandica, DOI 10.1111/stan.12292) introduced this precise Fourier–Stein statistic and established its null limit for a **fixed positive** frequency weight, including ML and moment influence-function representations. The present claim treats arbitrary **diverging** Gaussian precision and quantifies a non-equivalent estimator-dependent cancellation. Ebner, Eid and Klar's Cauchy Stein statistic (DOI 10.1007/s00362-022-01382-0) studies another law and an exponential-absolute-frequency weighting; its limiting statements do not supply the logistic Gaussian-frequency rate or constants. Other large-bandwidth goodness-of-fit results for exponential and inverse-Gaussian models concern different Stein kernels, weights or boundaries. The present statement is not asserted to be historically unique without independent priority review.

## Limitations

Only the null law of the stated Gaussian-weighted logistic statistic is established. The result does not assert failure of a bootstrap-calibrated test, an alternative-distribution power law, a minimax rate, or a uniform approximation over arbitrary data-dependent tuning-parameter choices. The ML statement presumes the usual nondegenerate interior MLE. Neither theorem requires a relation between deterministic bandwidth and sample size. Historical priority remains a risk despite direct comparison of the primary preprint and related published work.

## References

1. J. S. Allison, B. Ebner and M. Smuts, *Logistic or not logistic?*, arXiv:2108.07036v1 (16 August 2021); *Statistica Neerlandica*, DOI:10.1111/stan.12292 (2023). https://arxiv.org/html/2108.07036v1
2. B. Ebner, L. Eid and B. Klar, *Cauchy or not Cauchy? New goodness-of-fit tests for the Cauchy distribution*, *Statistical Papers* (2022 online), DOI:10.1007/s00362-022-01382-0. https://link.springer.com/article/10.1007/s00362-022-01382-0
