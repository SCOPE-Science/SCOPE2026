# A full-null bootstrap failure for moment-fitted Pareto goodness-of-fit tests

## Finding
For each fixed true Pareto shape \(0<\beta<1\), the classical Kolmogorov–Smirnov and Cramér–von Mises empirical-distribution goodness-of-fit tests, when fitted using the sample-mean-based moment estimate and calibrated by refitted parametric bootstrap, reject with probability tending to **one**, despite the true distribution belonging to the composite Pareto null. The mechanism is an exact nonzero population discrepancy, whereas the refitted bootstrap discrepancy vanishes.

Specifically, let \(D_n\) and \(W_n\) be defined below. Almost surely,
\[
D_n\longrightarrow d_\beta=(1-\beta)\beta^{\beta/(1-\beta)}>0,
\qquad
\frac{W_n}{n}\longrightarrow c_\beta=\frac{1}{2\beta+1}-\frac{2}{\beta+2}+\frac13>0.
\]
For example, at \(\beta=1/2\), the limits are \(d_{1/2}=1/4\) and \(c_{1/2}=1/30\). At every fixed significance level \(\alpha\in(0,1)\), either corresponding refitted-bootstrap test has asymptotic rejection probability one.

## Assumptions and scope
The null family consists of \(P_\theta\) with CDF \(F_\theta(x)=1-x^{-\theta}\), \(x\ge1\), for arbitrary \(\theta>0\), with **known lower endpoint one**. The observations \(X_1,\dots,X_n\) are independent and identically distributed from \(P_\beta\) for a fixed \(0<\beta<1\). The estimate is \(\widehat\beta_n=\overline X_n/(\overline X_n-1)\), well-defined and strictly greater than one almost surely. Write \(F_n\) for their empirical CDF. The EDF statistics are
\[
D_n=\sup_{x\ge1}|F_n(x)-F_{\widehat\beta_n}(x)|,
\quad
W_n=n\int_{1}^{\infty}(F_n-F_{\widehat\beta_n})^2\,dF_{\widehat\beta_n}.
\]
Given observations, each parametric bootstrap repetition draws \(n\) independent values from \(P_{\widehat\beta_n}\), recomputes the moment estimate \(\widehat\beta_n^*\) from that bootstrap sample, and recomputes \(D_n^*\) or \(W_n^*\) using that refitted estimate. Conditional quantiles refer to the ideal conditional bootstrap distribution, not a fixed finite Monte Carlo estimate. The claim is not about maximum-likelihood fitting, known-shape tests, the proposed Fourier-statistic itself, unknown lower endpoints, or the boundary case \(\beta=1\).

## Proof
**1. Fitted-data limit.** For every positive integer \(M\), the truncated variables \(\min(X_i,M)\) are bounded. By the strong law of large numbers, \(\liminf_n\overline X_n\ge\mathbb E_\beta\min(X_1,M)\) almost surely. Since \(\mathbb E_\beta X_1=\infty\) for \(0<\beta<1\), monotone convergence as \(M\to\infty\) gives \(\overline X_n\to\infty\) almost surely and \(\widehat\beta_n\to1\). The Glivenko–Cantelli theorem gives \(\lVert F_n-F_\beta\rVert_\infty\to0\). Moreover, for \(\theta\to1\), \(\lVert F_\theta-F_1\rVert_\infty\to0\), for example by continuity on a compact initial interval plus a uniform Pareto-tail bound. Thus \(\lVert F_n-F_{\widehat\beta_n}-(F_\beta-F_1)\rVert_\infty\to0\) almost surely.

**2. Sharp Kolmogorov limit.** For \(x\ge1\), \(F_\beta(x)-F_1(x)=x^{-1}-x^{-\beta}<0\) when \(0<\beta<1\) and \(x>1\). Maximizing \(x^{-\beta}-x^{-1}\) gives the unique maximizer \(x_*=\beta^{-1/(1-\beta)}\); evaluation yields \(d_\beta=(1-\beta)\beta^{\beta/(1-\beta)}\). Uniform convergence proves the stated almost-sure limit for \(D_n\).

**3. Sharp Cramér–von Mises limit.** Let \(g_n=F_n-F_{\widehat\beta_n}\) and \(g=F_\beta-F_1\). Since \(g_n\to g\) uniformly, \(\int g_n^2dF_{\widehat\beta_n}-\int g^2dF_{\widehat\beta_n}\to0\). Weak convergence \(P_{\widehat\beta_n}\Rightarrow P_1\), combined with bounded continuity of \(g^2\), shows \(W_n/n\to\int g^2dF_1\). Substituting \(u=x^{-1}\) yields
\[
\int_1^\infty (x^{-\beta}-x^{-1})^2x^{-2}\,dx
=\int_0^1(u^\beta-u)^2\,du
=\frac1{2\beta+1}-\frac2{\beta+2}+\frac13.
\]
Strict positivity follows since the integrand is positive on \((0,1)\).

**4. Conditional bootstrap collapse, despite triangular infinite-mean behavior.** Consider any original-sample path on which \(\theta_n=\widehat\beta_n\to1\). Given this path, the bootstrap observations are iid \(P_{\theta_n}\). For any fixed finite \(K>0\), choose a finite truncation level \(L>1\) such that \(\mathbb E_1\min(X,L)>2K\), possible since \(\mathbb E_1\min(X,L)=1+\log L\). By continuity in \(\theta\), \(\mathbb E_{\theta_n}\min(X,L)>3K/2\) eventually. Hoeffding's inequality for bounded bootstrap truncations implies
\[
\Pr^*\{\overline X_n^*\le K\}\le\exp[-nK^2/(2L^2)]\longrightarrow0.
\]
Hence \(\overline X_n^*\to\infty\) and \(\widehat\beta_n^*=\overline X_n^*/(\overline X_n^*-1)\to1\), both in conditional probability. By the distribution-free Dvoretzky–Kiefer–Wolfowitz inequality, \(\lVert F_n^*-F_{\theta_n}\rVert_\infty\to0\) in conditional probability. Therefore
\[
D_n^*\le\lVert F_n^*-F_{\theta_n}\rVert_\infty +\lVert F_{\theta_n}-F_1\rVert_\infty+\lVert F_{\widehat\beta_n^*}-F_1\rVert_\infty\ \xrightarrow{\Pr^*}\ 0.
\]
Furthermore, \(0\le W_n^*/n\le(D_n^*)^2\to0\) in conditional probability. For each fixed \(\alpha\in(0,1)\), the conditional \((1-\alpha)\)-quantiles \(q_{D,n}^*(1-\alpha)\to0\) and \(q_{W,n}^*(1-\alpha)/n\to0\), almost surely along those original-sample paths. The nonzero almost-sure observed limits from Steps 2–3 force eventual rejection for each test along almost every true-null path; bounded convergence yields unconditional rejection probability tending to one.

## Verification
The accompanying `pareto_checker.py` uses exact arithmetic for special-case constants and independently simulates the fitted and refitted-bootstrap Kolmogorov statistics. It passed 23 analytical and simulation assertions. These finite checks corroborate but do not replace the probability-theoretic proof, whose infinite-sample claims rest on the strong law, Glivenko–Cantelli, DKW, and bounded concentration for triangular bootstrap samples.

## Relationship to prior work
Ndwandwe, Allison, Santana and Visagie (2022), Sections 3.2 and 4.2, already note the finite-mean assumption for adjusted moment estimators and report size distortion for the shape-one null, with a finite-sample explanation. Their work does **not** provide the shape-\((0,1)\) exact Kolmogorov/Cramér–von Mises discrepancy limits, conditional-bootstrap collapse, or asymptotic rejection-probability-one theorem stated here. Ndwandwe, Allison, Smuts and Visagie (2023), Section 4.1, explicitly use the sample-mean-based fitted shape in bootstrap calibration and compare against classical EDF tests. The result here applies solely to the stated EDF comparators with the stated resampling convention; it makes no claim about the parameter-free Fourier tests themselves. The truncation proof and DKW inequality are classical tools, not asserted as novel.

## Limitations
The theorem concerns ideal conditional bootstrap quantiles for a fixed \(0<\beta<1\); it does not quantify finite bootstrap-repetition error, local approaches to \(\beta=1\), or the behavior of every statistic in the cited papers. Existing prior warnings at \(\beta=1\) and general infinite-mean arguments limit historical-priority claims. An independently conducted audit has not been performed.

## References
1. L. Ndwandwe, J. S. Allison, M. Smuts and I. J. H. Visagie, *On a new class of tests for the Pareto distribution using Fourier methods*, first public arXiv version dated 2023-01-23, https://arxiv.org/abs/2301.09385 ; published DOI https://doi.org/10.1002/sta4.566. Sections 1–4, particularly Section 4.1 and its comparator definitions.
2. L. Ndwandwe, J. S. Allison, L. Santana and I. J. H. Visagie, *Testing for the Pareto type I distribution: A comparative study*, arXiv version dated 2022-11-18, https://arxiv.org/abs/2211.10088. Sections 2, 3 and 4 and numerical tables.
3. A. Dvoretzky, J. Kiefer and J. Wolfowitz, *Asymptotic minimax character of the sample distribution function and of the classical multinomial estimator*, Ann. Math. Stat. 27 (1956). Standard empirical-CDF concentration reference.
