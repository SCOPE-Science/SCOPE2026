# Two rare-bin transitions for a fitted Kolmogorov–Smirnov statistic under increasing logarithmic Pareto binning

## Finding

The logarithmically binned Pareto goodness-of-fit statistic has two distinct information-loss thresholds, even under an exactly specified Pareto sampling law. Let \(q_n=b_n^{-\alpha}\to0\), and let \(D_n\) be the discrete Kolmogorov–Smirnov distance between the empirical law of the logarithmic bin indices and the geometric law fitted by maximum likelihood, with its zero-tail-probability boundary continuation as specified below. With \(Z\sim N(0,1)\) and \(P_t\sim\operatorname{Poisson}(t)\), the following exhaustive regimes hold whenever the indicated limits exist:

1. If \(nq_n^2\to\infty\), then \((\sqrt n/q_n)D_n\Rightarrow |Z|\).
2. If \(nq_n^2\to t\in(0,\infty)\), then \(nD_n\Rightarrow |P_t-t|\).
3. If \(nq_n^2\to0\) but \(nq_n\to\infty\), then \(D_n/q_n^2\xrightarrow{\Pr}1\).
4. If \(nq_n\to t\in[0,\infty)\), then \(n^2D_n\Rightarrow P_t^2\). When \(t=0\), in fact \(\Pr(D_n=0)\to1\).

In the fourth regime, the ordinary finite-exponent MLE fails to exist with probability tending to \(e^{-t}\): the data contain no observations above the first bin. If \(t\in(0,\infty)\), the ideal re-estimating parametric-bootstrap upper-tail probability also has a nonuniform, explicitly discrete limit \(\pi(P_t)\), with \(\pi(m)=\Pr\{\operatorname{Poisson}(m)\ge m\}\) for every nonnegative integer \(m\).

For the concrete design \(b_n=n^\beta\) with fixed \(\alpha,\beta>0\), the first transition is at \(\alpha\beta=1/2\), and the second at \(\alpha\beta=1\). The distributional limits are distinct; in particular, the intermediate deterministic regime is not a Gaussian or Poisson calibration.

## Assumptions and scope

For each integer \(n\ge1\), let \(X_{n,1},\ldots,X_{n,n}\) be independent Pareto observations with a **known fixed** lower endpoint \(x_{\min}>0\) and a **fixed** shape \(\alpha>0\), so that \(\Pr(X_{n,i}\ge x)= (x/x_{\min})^{-\alpha}\) for \(x\ge x_{\min}\). Rows need not be independent. Let \(b_n>1\) be deterministic with \(b_n\to\infty\), and define

\[
K_{n,i}=\left\lfloor\frac{\log(X_{n,i}/x_{\min})}{\log b_n}\right\rfloor,
\qquad q_n=b_n^{-\alpha}.
\]

The bin indices are iid on \(\{0,1,\ldots\}\) with probabilities \(\Pr(K_{n,i}=k)=(1-q_n)q_n^k\). Set \(S_n=\sum_i K_{n,i}\), \(N_{n,j}=\sum_i\mathbf1\{K_{n,i}\ge j\}\), and \(\widehat q_n=S_n/(n+S_n)\). This is the geometric MLE for positive \(S_n\); if \(S_n=0\), set \(\widehat q_n=0\), the natural extended-model boundary fit (equivalent to an infinite fitted Pareto exponent, not a finite estimate).

The **discrete**, fitted-CDF Kolmogorov–Smirnov statistic is

\[
D_n=\sup_{j\ge1}\left|\frac{N_{n,j}}n-\widehat q_n^{\,j}\right|.
\]

This compares CDFs at bin endpoints, with parameter refitting from the *same* observations, as in the fixed-origin logarithmic-binning procedure. It does not use a fitted lower cutoff, added measurement noise, a continuous-null Kolmogorov critical value, or the unknown-parameter test from a different binning model.

For the bootstrap statement, conditionally on the data draw iid geometric indices of size \(n\) with parameter \(\widehat q_n\), refit their geometric parameter with the identical boundary rule, and recompute the statistic \(D_n^*\). Define the **ideal**, non-Monte-Carlo, nonrandomized upper-tail probability \(p_n=\Pr_{\widehat q_n}(D_n^*\ge D_n\mid K_{n,1},\ldots,K_{n,n})\), including ties. This convention is essential at the discrete limit.

## Proof

**1. Exact reduction to two rare bins.** For every \(q\in(0,1)\), the geometric survival probabilities are \(\Pr(K\ge j)=q^j\), and the geometric likelihood is proportional to \((1-q)^nq^{S_n}\), giving the stated fit. The empirical-versus-fitted CDF difference at bin endpoint \(j-1\) is \(\widehat q_n^j-N_{n,j}/n\); hence the expression for \(D_n\).

Write \(q=q_n\), \(A=N_{n,1}\), \(B=N_{n,2}\), and \(S=S_n\). For one geometric index, \(\mathbb EK=q/(1-q)\) and \(\operatorname{Var}(K)=q/(1-q)^2\). Thus \(S/n=q/(1-q)+O_{\Pr}(\sqrt{q/n})\). If \(nq\to\infty\), it follows that \(\widehat q/q\xrightarrow{\Pr}1\) and \(\widehat q-q=O_{\Pr}(\sqrt{q/n})\).

For \(f(v)=v/(1+v)\), the exact identity

\[
f(v)-f(w)=\frac{v-w}{(1+v)(1+w)}\]

shows, with \(w=q/(1-q)\), that

\[
\widehat q-q=(1-q)^2\left(\frac Sn-\frac q{1-q}\right)+O_{\Pr}(q/n).
\]

Now \(S-A=\sum_{j\ge2}N_{n,j}=B+\sum_{j\ge3}N_{n,j}\). The centered remainder \(\sum_{j\ge3}(N_{n,j}-nq^j)\) is a sum over \(n\) independent variables \((K-2)_+\), whose second moment is \(q^3(1+q)/(1-q)^2=O(q^3)\). Also \(q(S-\mathbb ES)=O_{\Pr}(\sqrt{nq^3})\). Combining these observations gives

\[
A-n\widehat q=-(B-nq^2)+O_{\Pr}(\sqrt{nq^3}+q),
\]

and, by \(\widehat q^2-q^2=(\widehat q-q)(\widehat q+q)\),

\[
B-n\widehat q^2=(B-nq^2)+O_{\Pr}(\sqrt{nq^3}+q).
\]

For all later bins, condition on \(M=N_{n,3}\). Then \(M\sim\operatorname{Bin}(n,q^3)\), and the conditional excess counts above bin three are iid geometric. The empirical-distribution maximal inequality, followed by \(\mathbb E\sqrt M\le\sqrt{nq^3}\), yields

\[
\sup_{j\ge3}|N_{n,j}/n-q^j|=O_{\Pr}(\sqrt{q^3/n}).
\]

Moreover, for \(r=\max(q,\widehat q)<1/2\), \(\sup_{j\ge3}|q^j-\widehat q^j|\le3r^2|q-\widehat q|/(1-r)=O_{\Pr}(q^{5/2}/\sqrt n)\). Consequently, whenever \(q\to0\) and \(nq\to\infty\),

\[
\boxed{\quad
D_n=\left|\frac{B}{n}-q^2\right|
+O_{\Pr}\left(\sqrt{\frac{q^3}{n}}+\frac qn\right).
\quad}
\]

The statement is an error bound for the *difference of nonnegative quantities*; it does not assert that the signed difference is positive.

**2. Gaussian and Poisson transition at the second occupied bin.** The random variable \(B\) is \(\operatorname{Bin}(n,q^2)\). If \(nq^2\to\infty\), the Bernoulli triangular-array central limit theorem gives \((B-nq^2)/(\sqrt n\,q)\Rightarrow Z\). The remainder above, divided by \(q/\sqrt n\), tends to zero because \(q\to0\). This proves regime 1. If \(nq^2\to t\in(0,\infty)\), the binomial-to-Poisson limit yields \(B\Rightarrow P_t\), and the remainder multiplied by \(n\) vanishes because \(nq^3\to0\). This proves regime 2. If \(nq^2\to0\) and \(nq\to\infty\), then \(B=0\) with probability tending to one; the remainder divided by \(q^2\) is \(O_{\Pr}(1/\sqrt{nq}+1/(nq))=o_{\Pr}(1)\). This proves regime 3.

**3. The first-bin rare window, including the boundary fit.** If \(nq\to t\in[0,\infty)\), then \(\Pr(B>0)\le nq^2\to0\). On \(B=0\), all indices are zero or one, so \(S=A\), \(\widehat q=A/(n+A)\), and direct comparison of the first two bin endpoints gives the *exact finite-sample identity*

\[
\boxed{\quad D_n=\frac{A^2}{n(n+A)}\quad\text{whenever }B=0.\quad}
\]

Indeed the first discrepancy is \(A^2/[n(n+A)]\), while every later discrepancy is at most \(\widehat q^2=A^2/(n+A)^2\). Since \(A\sim\operatorname{Bin}(n,q)\Rightarrow P_t\), we obtain \(n^2D_n\Rightarrow P_t^2\). If \(t=0\), \(\Pr(A=0)=(1-q)^n\to1\), so \(D_n=0\) with probability tending to one. The finite-exponent likelihood estimate does not exist precisely when \(S=0\), whose probability is \((1-q)^n\to e^{-t}\).

**4. Bootstrap limit at the first-bin window.** Fix an integer \(m\ge0\). Conditional on an observed sample with \(A=m\) and \(B=0\), the bootstrap parameter is \(m/(n+m)\). The probability of any bootstrap observation in the second or a higher bin is at most \(n(m/(n+m))^2\to0\). The bootstrap number \(A^*\) of nonzero indices therefore converges to \(\operatorname{Poisson}(m)\). On the overwhelmingly likely event that both samples contain only indices zero and one, their distances are \(g_n(A)=A^2/[n(n+A)]\) and \(g_n(A^*)\). The map \(g_n\) is strictly increasing on nonnegative integers, so the upper-tail event is exactly \(\{A^*\ge m\}\). It follows that the conditional ideal bootstrap probability tends to \(\pi(m)=\Pr\{\operatorname{Poisson}(m)\ge m\}\), including \(\pi(0)=1\). Since \(A\Rightarrow P_t\) and \(\Pr(B>0)\to0\), conditioning on finitely many \(m\) and then controlling the Poisson tail proves \(p_n\Rightarrow\pi(P_t)\).

## Verification

`check_ks.py` is a self-contained Python 3 standard-library checker. It exhaustively checks the finite-sample discrete-CDF identity for \(n\le4\) and indices in \(\{0,\ldots,4\}\), the special-event formula for \(n\le6\) and indices in \(\{0,1,2\}\), basic geometric tail identities, and independent seeded numerical diagnostics in the critical and first-bin windows. Its simulations are corroboration only; every infinite-sample limit is proved above without reliance on sampling output.

To run: `python3 check_ks.py`. The exact check and numerical diagnostics should print `Checker PASS`. Calculations make no claim about noisy observations or a lower cutoff estimated from the data.

## Relationship to prior work

Lin and Newberry (arXiv:2301.05690, first publicly posted 13 January 2023) introduce logarithmic binning for robust Pareto inference and explicitly specify a discrete geometric likelihood, an estimated-parameter Kolmogorov–Smirnov statistic and a parametric bootstrap. They describe the tradeoff between information and robustness with the binning ratio, but do not formulate the increasing-bin-ratio triangular-array null limits established here. Their journal exposition, *Seeing through noise in power laws* (2023), discusses increasing the bin ratio with sample size and empirical thresholds for useful bin counts, but does not give this pair of exact fluctuation thresholds or the boundary-bootstrap law.

Virkar and Clauset (arXiv:1208.3524, first posted 2012) develop power-law inference for binned empirical data and quantify Fisher-information loss and KS calibration with fitted parameters. Their treatment includes estimation of a lower tail cutoff and mostly fixed binning schemes; it does not directly imply the stated triangular-array distributions. Newberry and Savage (2019) provide the self-similar discrete logarithmic power-law model and its MLE, but not the present fitted-KS transition theorem. Classical binomial normal/Poisson limits and conditional empirical-process bounds are explicitly used in the proof; the new content is their joint, parameter-refitted KS consequence across all rare-bin scales.

## Limitations

The null model is exact Pareto with known threshold and deterministic common bin ratio; deviations from Pareto, measurement errors, fitted thresholds, dependence, and data-dependent selection of the bin ratio are outside scope. The zero-tail fit is an **extended** likelihood fit; if the finite Pareto exponent is required, the procedure is undefined on all-zero binned samples. The ideal bootstrap convention includes ties and re-estimates the parameter; randomized or finite-replicate \(p\)-values have different behavior. Convergence in distribution of \(n^2D_n\) does not assert convergence of its moments: exceptionally rare second-bin observations can produce large scaled values. The proof does not establish higher-order rates, finite-sample test size, or power under alternatives.

## References

1. Q. Lin and M. Newberry, *Tunable robustness in power-law inference*, arXiv:2301.05690v1 (13 January 2023), https://arxiv.org/abs/2301.05690.
2. M. Newberry and Q. Lin, *Seeing through noise in power laws*, Journal of the Royal Society Interface 20 (2023), article 20230310, https://pmc.ncbi.nlm.nih.gov/articles/PMC10465205/.
3. Y. Virkar and A. Clauset, *Power-law distributions in binned empirical data*, arXiv:1208.3524 (2012), Annals of Applied Statistics 8 (2014), 89–119, https://arxiv.org/abs/1208.3524.
4. M. G. Newberry and V. M. Savage, *Self-Similar Processes Follow a Power Law in Discrete Logarithmic Space*, Physical Review Letters 122 (2019), 158303, https://doi.org/10.1103/PhysRevLett.122.158303.
5. E. Kulinskaya, *Coefficients of the asymptotic distribution of the Kolmogorov–Smirnov statistic when parameters are estimated*, Journal of Nonparametric Statistics 5 (1995), 43–60, https://doi.org/10.1080/10485259508832633.
