# Sharp sparse-Bernoulli size trichotomy for studentized cross-HSIC

## Finding

The linear-kernel, sample-split studentized cross-HSIC independence test has a sharp, and potentially severe, sparse-marginal null-calibration transition. The sample consists of \(2n\) independent pairs \((X_i,Y_i)\), where the two coordinates are independent \(\operatorname{Bernoulli}(p_n)\) variables. Assume throughout that \(n\ge3\), \(p_n\to0\), and \(np_n\to\infty\). Let \(T_n\) be the one-sided studentized cross-HSIC statistic defined precisely below. Its rejection rule is \(T_n>z_{1-\alpha}\), the standard-normal upper quantile.

**Theorem (sparse null-size trichotomy).**

1. If \(np_n^2\to0\), then \(T_n/\sqrt{np_n/2}\to1\) in probability. Hence, for every fixed significance target \(\alpha\in(0,1)\), the null rejection probability converges to **one**, despite exact independence.
2. If \(np_n^2\to\theta\in(0,\infty)\) with \(\theta\notin\mathbb N\), then \(T_n\) converges in distribution on the extended real line to \(\mathcal T_\theta\), defined using independent \(K_1,K_2\sim\operatorname{Poisson}(\theta)\) by
   \[
   \mathcal T_\theta=\begin{cases}
   +\infty,&K_1=0,\ K_2<\theta,\\
   -\infty,&K_1=0,\ K_2>\theta,\\
   \operatorname{sgn}(K_2-\theta)(K_1-\theta)/\sqrt{K_1},&K_1\ge1.
   \end{cases}
   \]
   The two infinite atoms have probabilities \(e^{-\theta}\Pr(K_2<\theta)\) and \(e^{-\theta}\Pr(K_2>\theta)\), respectively. For \(\theta=1/2\) and a nominal upper-tail level \(\alpha=0.05\), the exact limiting false-rejection probability is
   \[
   e^{-1}+(1-e^{-1/2})\left[1-e^{-1/2}\sum_{j=0}^{3}\frac{(1/2)^j}{j!}\right]
   =0.3685686509430986\ldots.
   \]
3. If \(np_n^2\to\infty\), the published uniform Gaussian theorem applies: \(T_n\Rightarrow N(0,1)\) and the same test has asymptotic null rejection probability \(\alpha\).

The new claim is the complete sparse trichotomy and the exact studentized Poisson/extended-real law, particularly the 100% false-rejection regime and the critical 5% size calculation. The fixed-null and moment-controlled Gaussian theorem is prior work, as is the original observation that the *sign* of the critical statistic has a Poisson-product limit.

## Assumptions and scope

For each \(n\), the pairs \((X_i,Y_i)\), \(1\le i\le2n\), are iid, with \(X_i\) independent of \(Y_i\) and both \(\operatorname{Bernoulli}(p_n)\). There are \(n\) pairs in each of the two independent halves, and scalar linear kernels \(k(x,x')=xx'\), \(\ell(y,y')=yy'\) are used.

In half \(r\in\{1,2\}\), let \(A_r\) count observed \(X=1\), \(B_r\) count \(Y=1\), and \(C_r\) count simultaneous ones. For the ordered-pair kernel \(h_{ij}=\frac12(X_i-X_j)(Y_i-Y_j)\), the sample covariance estimator in half \(r\) is
\[
f_r=\frac{1}{n(n-1)}\sum_{i\ne j\text{ in half }r}h_{ij}
=\frac{nC_r-A_rB_r}{n(n-1)}.
\]
In the first half put
\[
g_i=\frac{1}{n-1}\sum_{j\ne i}h_{ij},\qquad
Q_n=\sum_{i=1}^{n}(g_i-f_1)^2.
\]
The exact published jackknife normalizer is
\[
s_n^2=\frac{4(n-1)}{(n-2)^2}f_2^2 Q_n,
\qquad T_n=\frac{\sqrt n\,f_1f_2}{s_n}.
\]
For the exceptional event \(s_n=0\), define \(T_n=0\) and do not reject. Under each regime in the theorem, this event has probability tending to zero, so this convention does not alter any limit. The result is specifically about this Gaussian-calibrated, nonrandomized statistic, not a permutation-calibrated HSIC test, not general nonlinear kernels, and not a claim of invalidity under the hypotheses of the source's Gaussian theorems.

## Proof

**Exact count reduction.** In the first half, write \(A=A_1\), \(B=B_1\), and \(C=C_1\). Direct expansion gives
\[
g_i=\frac{nX_iY_i+C-BX_i-AY_i}{2(n-1)},\qquad
f_1=\frac{nC-AB}{n(n-1)}.
\]
Hence \(Q_n\) is fully determined by the four cell counts. Their values and corresponding \(g_i\) are:

| Cell \((X_i,Y_i)\) | Count | Value of \(g_i\) |
|---|---:|---|
| \((0,0)\) | \(n-A-B+C\) | \(C/[2(n-1)]\) |
| \((1,0)\) | \(A-C\) | \((C-B)/[2(n-1)]\) |
| \((0,1)\) | \(B-C\) | \((C-A)/[2(n-1)]\) |
| \((1,1)\) | \(C\) | \((n+C-A-B)/[2(n-1)]\) |

In particular, when \(C=0\), exact simplification yields
\[
Q_n=\frac{AB}{(n-1)^2}\left(\frac{A+B}{4}-\frac{AB}{n}\right),
\quad
f_1=-\frac{AB}{n(n-1)}.
\]
On \(f_2\ne0\) and \(Q_n>0\), the factor \(|f_2|\) cancels:
\[
T_n=\operatorname{sgn}(f_2)\,
\frac{\sqrt n\,f_1}{\sqrt{4(n-1)Q_n/(n-2)^2}}.
\]

**Sparse regime.** Under \(np_n\to\infty\), binomial concentration gives \(A_r/(np_n)\to1\) and \(B_r/(np_n)\to1\) in probability. If \(np_n^2\to0\), the union bound yields \(\Pr(C_1=C_2=0)\ge1-2np_n^2\to1\). On this event, both \(f_1\) and \(f_2\) are negative with probability tending to one. The preceding exact formula gives
\[
f_1=-p_n^2(1+o_{\Pr}(1)),\quad
Q_n=\tfrac12np_n^3(1+o_{\Pr}(1)),\quad
\frac{4(n-1)Q_n}{(n-2)^2}=2p_n^3(1+o_{\Pr}(1)).
\]
It follows that \(T_n=\sqrt{np_n/2}(1+o_{\Pr}(1))\). The assumption \(np_n\to\infty\) completes the first assertion. For example, \(p_n=n^{-3/4}\) satisfies all its hypotheses.

**Critical Poisson regime.** If \(np_n^2\to\theta>0\), each overlap count \(C_r\sim\operatorname{Bin}(n,p_n^2)\) tends to an independent \(\operatorname{Poisson}(\theta)\) variable. Moreover,
\[
 n f_r=C_r-\frac{A_rB_r}{n-1}=C_r-\theta+o_{\Pr}(1).
\]
If \(C_1=k\ge1\) is fixed, the \(k\) joint-one observations have \(g_i=1/2+o_{\Pr}(1)\), while the remaining terms contribute only \(o_{\Pr}(1)\) to the quadratic sum. Consequently \(Q_n=k/4+o_{\Pr}(1)\), and
\[
\frac{\sqrt n\,f_1}{\sqrt{4(n-1)Q_n/(n-2)^2}}
=\frac{k-\theta}{\sqrt{k}}+o_{\Pr}(1).
\]
If \(C_1=0\), the exact zero-cell identity instead gives the diverging ratio \(-\sqrt{np_n/2}(1+o_{\Pr}(1))\). Because \(\theta\) is not an integer, the sign of \(f_2\) converges conditionally on \(C_2\) to \(\operatorname{sgn}(C_2-\theta)\), and the limiting signs cannot be ambiguous. Joint convergence for the independent halves, followed by truncation to finitely many Poisson counts and then removal of the truncation, proves convergence on the extended real line to the stated \(\mathcal T_\theta\).

At \(\theta=1/2\), the first-half critical values for \(k\ge1\) are \((k-1/2)/\sqrt{k}\), strictly increasing in \(k\). They first exceed \(z_{0.95}=1.6448536269\ldots\) at \(k=4\). For \(k=0\), rejection occurs precisely when the other Poisson count is zero, giving \(e^{-1}\). For \(k\ge4\), rejection occurs precisely when the second-half count is positive. Multiplication of the independent Poisson probabilities gives the displayed exact false-rejection limit. No limiting atom lies on \(z_{0.95}\).

**Gaussian regime.** For Bernoulli coordinates, the centered-product fourth-moment ratio in the published uniform Gaussian theorem is asymptotic to \(1/(np_n^2)\). It vanishes when \(np_n^2\to\infty\), so Theorem 4(b) of the source implies the third assertion. This is cited prior work rather than a new central limit proof.

## Verification

`verify_sparse_cross_hsic.py` reconstructs the test from all ordered pairs and independently from four contingency-cell counts, comparing exact rational results for every binary sample of sizes \(3\) through \(6\). It checks the zero-overlap identity, the critical finite-count asymptotics, and the explicit Poisson-tail probability. It also computes exact finite-\(n\) rejection probabilities from the multinomial cell probabilities and includes reproducible independent simulation checks. It passed **6,638 assertions** in the delivered environment. The deterministic exact finite-null rejection probabilities at \(n=20,40,60\) and \(\theta=1/2\) are approximately \(0.0303133228\), \(0.0810921939\), and \(0.1744353052\); their slow approach to the asymptotic limit is consistent with the \(n^{1/4}\) growth at the zero-overlap configurations. The proof, not finite simulations or these finite checks, establishes the asymptotic theorem.

Run using `python verify_sparse_cross_hsic.py` with the standard library and NumPy for the optional seeded simulation checks. Exact identities and deterministic mathematical assertions do not require NumPy.

## Relationship to prior work

Shekhar, Kim and Ramdas define exactly this studentized cross-HSIC statistic and prove Gaussian limits under fixed-null and uniform-moment hypotheses. Their **Example 1** already uses the same sparse Bernoulli scaling \(np_n^2\to\theta\notin\mathbb N\) and derives the limiting *sign probability* through a product of two centered Poisson variables; that prior sign fact is not claimed new. Its appendix does not compute the full studentized magnitude or either infinite atom. The present calculation uses the exact finite-sample jackknife variance to identify the complete extended-real distribution, derive an exact upper-tail rejection probability, and establish the separate subcritical convergence to 100% false rejections. The source's Corollary 5 is explicitly conditional on a moment requirement not satisfied in the subcritical or critical regimes, so there is no contradiction.

Kim and Ramdas develop the general cross-U-statistic methodology, rather than the present specific sparse-Bernoulli xHSIC rejection-size phase diagram. Classical Poisson approximation supplies the overlap-count limit but neither the jackknife-collapse factor nor the stated exact false-rejection probability. Permutation-calibrated HSIC is a different inference procedure and is not implicated by the phenomenon.

## Limitations

The statement is restricted to identical sparse Bernoulli marginals, independent coordinates, linear kernels, equal halves, and the specified Gaussian calibration. The boundary \(np_n\to\infty\) excludes ultra-sparse degenerate margins. The critical theorem excludes integer \(\theta\), where fluctuations of the fitted-marginal product can determine the sign on the equality event. The type-I limit at general critical \(\theta\) can have atoms at a chosen quantile; the exact numerical upper-tail result is stated only at \(\theta=1/2\), where the boundary is non-atomic. None of the assertions concerns a permutation test, a finite-sample uniform level guarantee, an alternative hypothesis, or a generic nonlinear-kernel cross-HSIC. The self-review is not an independent mathematical audit; historical priority remains subject to further literature verification.

## References

1. S. Shekhar, I. Kim, and A. Ramdas, *A Permutation-Free Kernel Independence Test*. First publicly posted 18 December 2022, arXiv:2212.09108; Journal of Machine Learning Research **24** (2023), paper 369, pp. 1–68. https://arxiv.org/abs/2212.09108 ; https://jmlr.org/papers/volume24/23-0248/23-0248.pdf . Especially the definition in Section 3, Corollary 5, Example 1, Theorem 7, and Appendix B.3.
2. I. Kim and A. Ramdas, *Dimension-agnostic inference using cross U-statistics*. First preprint 10 November 2020, arXiv:2011.05068; Bernoulli **30** (2024), pp. 683–711. https://arxiv.org/abs/2011.05068 . General methodological background.
3. D. Rindt et al., *Consistency of permutation tests of independence using distance covariance, HSIC and dHSIC*. Stat **10** (2021), e364. https://doi.org/10.1002/sta4.364 . Different, permutation-calibrated methodology.
