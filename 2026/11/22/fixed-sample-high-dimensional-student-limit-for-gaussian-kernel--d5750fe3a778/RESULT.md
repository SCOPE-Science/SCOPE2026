# Fixed-sample high-dimensional Student limit for Gaussian-kernel cross-MMD

## Finding

For a fixed first-half sample size \(s\ge2\) in each group and ambient dimension \(d\to\infty\), the null law of the *published* studentized cross-MMD statistic with a Gaussian radial basis function kernel is not standard normal. Rather, for every bandwidth \(\ell_d>0\) (possibly depending on all observations) satisfying \(\ell_d^2/d\overset{p}{\longrightarrow}c\in(0,\infty)\),

\[
T_d\ \overset{d}{\longrightarrow}\ \sqrt{\frac{s}{s-1}}\,t_{2s-2}.
\]

Consequently, if \(z_{1-\alpha}=\Phi^{-1}(1-\alpha)\), the limiting size of the usual one-sided Gaussian-calibrated test is

\[
p_s(\alpha)=1-F_{t_{2s-2}}\!\left(z_{1-\alpha}\sqrt{\frac{s-1}{s}}\right).
\]

For \(s=2\), the identity \(p_2(\alpha)=\tfrac12[1-z_{1-\alpha}/\sqrt{4+z_{1-\alpha}^2}]\) gives \(p_2(0.05)=0.182400163254645\ldots\). A test with \(s=2\) uses four observations from each distribution, hence eight observations total. Replacing the normal cutoff with \(\sqrt{s/(s-1)}\,F_{t_{2s-2}}^{-1}(1-\alpha)\) gives asymptotic level \(\alpha\) in this dimension-asymptotic regime.

## Assumptions and scope

Fix an integer \(s\ge2\). For each dimension \(d\ge1\), take two independent samples \(X_{1},\ldots,X_{2s}\) and \(Y_{1},\ldots,Y_{2s}\), each of \(d\)-dimensional vectors. All \(4s\) vectors have the same law under the null, with coordinate entries independent and identically distributed as a real variable \(\xi\) satisfying \(\mathbb E\xi=0\), \(\mathbb E\xi^2=\sigma^2\in(0,\infty)\), and \(\mathbb E\xi^4<\infty\). No Gaussian assumption is imposed on \(\xi\).

Use the characteristic Gaussian kernel \(k_d(x,y)=\exp(-\|x-y\|^2/(2\ell_d^2))\), with a *single common* bandwidth parameter \(\ell_d>0\) such that \(\ell_d^2/d\to c>0\) in probability. A deterministic bandwidth is allowed. One can take the **squared bandwidth** \(\ell_d^2\) to be the median of the squared distances over distinct pooled observation pairs, divided by any fixed positive constant, using any positive fallback if that median is zero. There are finitely many pairs and each squared distance divided by \(d\) converges in probability to \(2\sigma^2>0\); the fallback event therefore has probability tending to zero even for discrete coordinates. No independence between bandwidth and observations is needed.

Set

\[
g_d(z)=\frac1s\sum_{j=s+1}^{2s}\{k_d(z,X_j)-k_d(z,Y_j)\},\qquad U_i=g_d(X_i),\quad V_i=g_d(Y_i),\quad 1\le i\le s.
\]

Define \(\bar U=s^{-1}\sum_iU_i\), \(\bar V=s^{-1}\sum_iV_i\) and the *biased, \(s\)-denominator* group variances \(v_U=s^{-1}\sum_i(U_i-\bar U)^2\), \(v_V=s^{-1}\sum_i(V_i-\bar V)^2\). The statistic is

\[
T_d=\frac{\bar U-\bar V}{\sqrt{(v_U+v_V)/s}}.
\]

This is the balanced version of the score and normalization in equations (2)--(4) of Shekhar, Kim and Ramdas. On a zero-denominator event define the statistic arbitrarily, for example zero; this event has probability tending to zero under the stated assumptions.

## Proof

**1. Uniform high-dimensional radial expansion.** Let \(\mathcal Z\) denote the finite collection of observed vectors. For each distinct pair \(a,b\in\mathcal Z\), independence of coordinate entries and their finite fourth moment imply

\[
\|a-b\|^2-2d\sigma^2=O_p(\sqrt d).
\]

Because the number of pairs is fixed, this bound holds uniformly over all pairs. Put \(q_d=\exp(-d\sigma^2/\ell_d^2)\) and \(b_d=q_d/\ell_d^2\). The bandwidth assumption gives \(q_d\to e^{-\sigma^2/c}>0\) in probability and \(b_d d\to e^{-\sigma^2/c}/c>0\). Taylor's theorem for the exponential, uniformly over the finite observed set, yields

\[
k_d(a,b)=q_d-\frac{b_d}{2}\bigl(\|a\|^2+\|b\|^2-2a^\top b-2d\sigma^2\bigr)+O_p(d^{-1}).
\]

The common bandwidth can be data-dependent: the expansion only uses its positive probability limit and the joint finite-set bound. In particular, the uniform remainder statement means that the maximum absolute error among observed pairs is \(O_p(d^{-1})\).

**2. Cancellation of the shared random offset.** Define the vector difference of second-half means

\[
G_d=\frac1s\sum_{j=s+1}^{2s}(X_j-Y_j)
\]

and the difference of second-half mean squared norms

\[
C_d=\frac1s\sum_{j=s+1}^{2s}(\|X_j\|^2-\|Y_j\|^2).
\]

Subtracting the expansions for the two second-half groups cancels the common kernel constant, the evaluation-vector squared norm, and the \(2d\sigma^2\) term. Uniformly for first-half evaluations \(z\in\{X_1,\ldots,X_s,Y_1,\ldots,Y_s\}\),

\[
g_d(z)=b_d\{z^\top G_d-C_d/2\}+O_p(d^{-1}).
\]

The potentially non-vanishing normalized random quantity \(C_d/(2\sqrt d)\) is the *same* for all first-half observations. It disappears exactly from the numerator \(\bar U-\bar V\) and from the centered variances \(v_U,v_V\). Therefore, with \(W_{Xi,d}=d^{-1/2}X_i^\top G_d\) and \(W_{Yi,d}=d^{-1/2}Y_i^\top G_d\), dividing numerator and denominator by the positive factor \(b_d\sqrt d\) gives

\[
T_d=\frac{\bar W_{X,d}-\bar W_{Y,d}+o_p(1)}{
\sqrt{\{s^{-1}\sum_{i=1}^s(W_{Xi,d}-\bar W_{X,d})^2+s^{-1}\sum_{i=1}^s(W_{Yi,d}-\bar W_{Y,d})^2\}/s+o_p(1)}}.
\]

Here the \(O_p(d^{-1})\) remainder divided by \(b_d\sqrt d\) is \(O_p(d^{-1/2})=o_p(1)\).

**3. Joint Gaussian projection limit.** For each coordinate \(h\), let \(G_{d,h}=s^{-1}\sum_{j>s}(X_{j,h}-Y_{j,h})\). The \(2s\)-component vector of products

\[
(X_{1,h}G_{d,h},\ldots,X_{s,h}G_{d,h},Y_{1,h}G_{d,h},\ldots,Y_{s,h}G_{d,h})
\]

is independent across coordinates \(h\), has mean zero and finite covariance, and its covariance matrix equals \(\tau^2 I_{2s}\) with \(\tau^2=2\sigma^4/s>0\). Indeed, the first-half coordinate entries are independent of the second-half \(G_{d,h}\); cross-products have zero expectation, and each diagonal covariance is \(\sigma^2\mathbb E G_{d,h}^2=2\sigma^4/s\). The multivariate iid central limit theorem gives

\[
(W_{X1,d},\ldots,W_{Xs,d},W_{Y1,d},\ldots,W_{Ys,d})\ \overset{d}{\longrightarrow}\ \tau(Z_1,\ldots,Z_{2s}),
\]

where the \(Z_i\) are independent standard normals. Importantly, the common second-half data do *not* induce a nonzero limiting cross covariance: the joint normal limit has independent coordinates.

**4. Exact Gaussian ratio.** The limiting denominator is positive almost surely for \(s\ge2\). Writing \(\nu=2s-2\), the standard two-sample normal decomposition yields independent \(Z\sim N(0,1)\) and \(Q\sim\chi^2_{\nu}\), with limiting numerator \(\tau\sqrt{2/s}\,Z\) and limiting denominator \(\tau\sqrt Q/s\). Therefore

\[
T_d\ \overset{d}{\longrightarrow}\ \frac{\sqrt{2s}\,Z}{\sqrt Q}=\sqrt{\frac{s}{s-1}}\,t_{2s-2}.
\]

Continuity of this limiting distribution yields the rejection-probability expression. The \(s=2\) elementary formula follows from the explicit survival function of \(t_2\). This completes the proof.

## Verification

The accompanying `check.py` independently implements the original \(1/s\)-variance statistic, compares its Gaussian-kernel finite-dimensional Monte Carlo sizes to the derived Student limit, checks the Gaussian linear-witness control (which is exactly scaled-Student under the null at every finite dimension), and evaluates critical-value formulas. `check-output.json` contains one deterministic seeded replay. Those are numerical implementation checks, not a substitute for any limit argument. For reproducibility, use a Python environment with NumPy and SciPy and execute `python check.py`.

## Relationship to prior work

Shekhar, Kim and Ramdas introduced this exact studentized split statistic and prove a *standard-normal limit as sample sizes grow*, including settings in which dimension and bandwidth vary with sample size (2022 conference paper, Section 2.1, Theorems 4 and 5; expanded preprint, Theorem 15 and Appendix B). Their conditions entail diverging sample sizes; the present fixed-size, dimension-only limit does not follow from that Gaussian theorem. Their paper uses the same biased group variances, which are essential to the exact scaling factor above. The result concerns their own characteristic Gaussian RBF kernel, not a substituted linear kernel.

Zhu and Shao study fixed-sample high-dimensional MMD and energy-distance permutation tests. Their Gaussian kernel on normalized squared distances has \(\ell_d^2=d\gamma^2\) in the notation here. Their distance expansion and joint centered-pair framework (Assumption 2) are antecedents to the high-dimensional linearization; their Theorem 3.1 and Proposition 3.1 concern an unsplit, unstudentized statistic and its permutation distribution. The distinct result here is the limit for the published split score and its within-group studentizer, including a shared observation-dependent bandwidth under the stated conditions. Gao and Shao investigate a different, non-split, studentized MMD U-statistic with growing sample sizes. Kübler and collaborators study independently trained witness tests and state an asymptotic normal law as test-set size increases. Classical two-sample Student theory supplies the final ratio computation once the joint projection limit and its connection to the centered split scores have been established.

## Limitations

The sample size is fixed while dimension diverges; no uniform approximation rate, general joint \(s,d\to\infty\) theorem, or power theorem is claimed. The coordinates must be independent, identically distributed, centered, nondegenerate and have a finite fourth moment. Only Gaussian RBF kernels with a single bandwidth in the specified \(d\)-scale are treated. Other bandwidth regimes, dependence between coordinates, and non-null distributions require separate investigation. The finite-dimensional Gaussian-kernel distribution is not asserted to be Student; only its dimension-asymptotic limit is. Earlier or less accessible work on studentized kernel witnesses may contain overlapping ideas, so historical priority is not certified by this result.

## References

1. S. Shekhar, I. Kim and A. Ramdas, *A permutation-free kernel two-sample test*, NeurIPS 2022. https://proceedings.nips.cc/paper_files/paper/2022/file/731b952bdc833485eb72f458cdd5c489-Paper-Conference.pdf . First public preprint 2022-11-27: https://arxiv.org/abs/2211.14908 ; expanded text https://arxiv.org/pdf/2211.14908 .
2. H. Gao and X. Shao, *Two Sample Testing in High Dimension via Maximum Mean Discrepancy*, Journal of Machine Learning Research 24 (2023), 1--33. https://arxiv.org/abs/2109.14913 .
3. J. M. Kübler, W. Jitkrittum, B. Schölkopf and K. Muandet, *A Witness Two-Sample Test*, AISTATS 2022, PMLR 151:1403--1419. https://proceedings.mlr.press/v151/kubler22a.html .
4. Classical multivariate central limit theorem and classical normal-sample decomposition into independent sample means and sums of squares.
5. C. Zhu and X. Shao, *Interpoint Distance Based Two Sample Tests in High Dimension*, Bernoulli **27** (2021), 1189–1211. https://arxiv.org/abs/1902.07279 .
