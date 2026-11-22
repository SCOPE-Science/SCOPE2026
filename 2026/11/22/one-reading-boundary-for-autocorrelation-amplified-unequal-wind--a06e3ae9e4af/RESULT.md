# One-reading boundary for autocorrelation-amplified unequal wind-ramp averages

## Finding

Consider the contrast between two *consecutive, unequal-length* averages of a constant-variance Gaussian wind-power anomaly surrogate. For any integers \(m,n\ge1\), with stationary marginal variance \(\sigma^2>0\) and adjacent-lag correlation \(0\le\rho<1\), its variance \(V_{m,n}(\rho)\) obeys an exact sharp dichotomy:

1. If \(\min\{m,n\}=1\), \(V_{m,n}\) is strictly decreasing on \([0,1)\), so independence is its unique global maximizer.
2. If \(m,n\ge2\), there is a unique \(\rho_{m,n}\in(0,1)\) at which the variance attains its strict global maximum; it increases strictly before that point and decreases strictly afterwards.

The same optimizer and monotonicity govern \(\Pr(|\Delta_{m,n}|>u)\) for **every** fixed \(u>0\). The result includes unequal lengths \(m\ne n\), rather than only the equal-block Allan-variance special case. In particular, comparing two averages of lengths \(2\) and \(10\) yields \(\rho_{2,10}\approx0.638158678162176\); the variance rises from \(0.6\sigma^2\) at independence to approximately \(0.889741973037229\sigma^2\) at that unique optimum, a \(48.29\%\) increase. At threshold \(u=\sigma\), the idealized two-sided exceedance probability rises from approximately \(0.196706\) to \(0.289076\).

## Assumptions and scope

Let \((X_j)_{j\in\mathbb Z}\) be a centered stationary Gaussian process with the fixed covariance law

\[
\operatorname{Cov}(X_i,X_j)=\sigma^2\rho^{|i-j|},\quad \sigma>0,\quad 0\le\rho<1.
\]

For positive integers \(m,n\), define the unbalanced adjacent reporting-window difference

\[
\Delta_{m,n}=\frac1m\sum_{j=1}^{m}X_j-\frac1n\sum_{j=m+1}^{m+n}X_j,
\qquad V_{m,n}(\rho)=\operatorname{Var}(\Delta_{m,n}).
\]

The stationary one-point variance is held fixed as \(\rho\) changes, so the innovation variance in an equivalent AR(1) recursion changes with \(\rho\). The limiting perfectly correlated process at \(\rho=1\) is used only to establish endpoint behavior. The result concerns a Gaussian surrogate for wind-power fluctuations, **not** a fitted or empirically validated physical wind model.

## Proof

Put \(N=m+n\) and let \(w_j=1/m\) for \(1\le j\le m\), and \(w_j=-1/n\) for \(m<j\le N\). These weights sum to zero. Then

\[
\frac{V_{m,n}(\rho)}{\sigma^2}=\frac1m+\frac1n+2\sum_{k=1}^{N-1}c_k\rho^k,
\qquad c_k=\sum_{j=1}^{N-k}w_jw_{j+k}.
\]

By symmetry in \(m,n\), assume \(m\le n\). Counting positive within-block pairs and negative cross-block pairs yields the following **exact disjoint ranges**:

\[
 c_k=\begin{cases}
 (m-k)/m^2+(n-k)/n^2-k/(mn),&1\le k<m,\\
 -k/n^2,&m\le k<n,\\
 -(m+n-k)/(mn),&n\le k<m+n.
 \end{cases}
\]

Empty ranges are omitted. If \(m=1\), every coefficient \(c_k\) is strictly negative, so \(V'_{m,n}(\rho)<0\) for \(0\le\rho<1\).

Now let \(m\ge2\). The first coefficient is strictly positive because

\[
 c_1=\frac{m-1}{m^2}+\frac{n-1}{n^2}-\frac1{mn}>0.
\]

The first-range coefficients decrease strictly with \(k\), with difference \(-1/m^2-1/n^2-1/(mn)\). Every coefficient at \(k\ge m\) is negative. Thus the nonzero ordered coefficient sequence \((c_1,2c_2,\ldots,(N-1)c_{N-1})\) has **exactly one** sign change from positive to negative. By Descartes' rule of signs, the derivative polynomial

\[
 \frac{V'_{m,n}(\rho)}{2\sigma^2}=\sum_{k=1}^{N-1}k c_k\rho^{k-1}
\]

has at most one positive real root, counted with multiplicity. It is positive at \(\rho=0\). To establish the other endpoint, define prefix sums \(S_\ell=\sum_{j=1}^{\ell}w_j\) for \(1\le\ell<N\). For every index pair \(i,j\), the integer distance \(|i-j|\) counts how many prefix cuts separate the two indices. Consequently, since \(\sum_jw_j=0\),

\[
\frac{V'_{m,n}(1)}{\sigma^2}=\sum_{i,j=1}^{N}w_iw_j|i-j|
=-2\sum_{\ell=1}^{N-1}S_\ell^2<0.
\]

The inequality is strict because \(S_1=1/m>0\). Thus the derivative has at least one root in \((0,1)\); the one-sign-change rule makes it **the unique simple positive root**. The derivative is strictly positive below and strictly negative above that root, proving the unique strict global maximum. Since \(V_{m,n}(1)=\sigma^2(\sum_jw_j)^2=0\), the boundary introduces no overlooked competing maximizer. A centered Gaussian contrast has tail \(2\Phi(-u/\sqrt{V_{m,n}(\rho)})\) for \(u>0\), strictly increasing in positive variance, giving the tail-probability corollary.

This proof handles every integer \(m,n\ge1\) without limiting enumeration; only \(\rho\in[0,1)\) is considered.

## Verification

The attached standalone `check.py` uses exact rational arithmetic for every \(1\le m,n\le20\) to compare the coefficient formulas with direct pair sums, check the one-sign-change and endpoint derivative identities, and reproduce the numerical \((m,n)=(2,10)\) example. These checks are diagnostics; Descartes' rule and the prefix-cut identity, not finite enumeration, prove the all-length statement. Run `python3 check.py` from a directory containing the extracted script.

## Relationship to prior work

Zhang (2008), Section 2.3 and equation (30), gives the autocorrelation-dependent **equal-width** Allan variance for the AR(1) model. Keim and Percival (2010), Sections 2–3 and Figures 1–3, analyze the **equal-width** Haar wavelet variance and a peak as block *scale* varies at fixed correlation. Both are antecedents, rather than new components of the present claim. Neither inspected result states the all-unequal-length classification when correlation varies at fixed \(m,n\), nor the sharp change at a singleton window.

Kiviluoma et al. (2015 initial online availability; print volume 2016) describe wind-power ramp autocorrelation and variation across dispatch time intervals; Gallego-Castillo et al. (2015) address meteorological causes and forecasting. Those physical studies do not state the two-window variance theorem. Algebraically, the result is a sign-variation consequence of two-step contrast weights, so an equivalent theorem in general signed-filter or total-positivity literature is a residual priority risk. No claim is made to discovery of the Allan variance or of Descartes' rule.

## Limitations

The proof requires nonnegative AR(1) autocorrelation, *fixed marginal variance*, exact stationarity, Gaussian increments and noiseless equal-weight averages inside each window. It does not establish the result for negatively correlated, non-Gaussian, heteroskedastic, nonstationary, seasonally varying, physically bounded or spatially interacting wind-power data. Actual wind farm output is bounded and need not follow this surrogate. The exceedance probability is a single Gaussian contrast probability, not a return period or system-reliability guarantee. The historical novelty judgment remains provisional, particularly for the larger theory of unequal two-step filters and weighted Allan statistics.

## References

1. N. F. Zhang, *Allan variance of time series models for measurement data*, Metrologia **45** (2008), 549–561; publication portal dated 2008-09-22. https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=152041 ; https://doi.org/10.1088/0026-1394/45/5/009
2. M. J. Keim and D. B. Percival, *Assessing Characteristic Scales Using Wavelets*, arXiv:1007.4169v1 (2010-07-23). https://arxiv.org/pdf/1007.4169
3. J. Kiviluoma et al., *Variability in large-scale wind power generation*, Wind Energy **19** (2016), 1649–1665; online first 2015. https://doi.org/10.1002/we.1942
4. M. Gallego-Castillo et al., *Identifying wind power ramp causes from multivariate datasets*, IET Renewable Power Generation **9** (2015), 867–875, first published 2015-11-01. https://doi.org/10.1049/iet-rpg.2014.0457
