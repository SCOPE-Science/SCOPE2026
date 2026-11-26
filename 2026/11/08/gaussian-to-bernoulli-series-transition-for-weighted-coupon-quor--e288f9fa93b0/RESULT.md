# Ranked-weight fluctuation law for homogeneous weighted coupon quorums

## Finding

Let the independent discovery times be \(T_{j,n}\sim\operatorname{Exp}(\lambda/n)\), where \(\lambda>0\). Let positive deterministic weights \(w_{j,n}\) sum to one and let \(\theta\in(0,1)\) be fixed. Set
\[
\tau_n=\inf\{t\ge0:\sum_{j=1}^n w_{j,n}\mathbf 1_{\{T_{j,n}\le t\}}>\theta\},\qquad
Q_n=\lambda\tau_n/n,\quad t_\theta=-\log(1-\theta),\quad s_n=(\textstyle\sum_j w_{j,n}^2)^{1/2}.
\]
Assume \(s_n\to0\). Rank the weights in descending order and assume \(w_{j,n}/s_n\to a_j\) for each fixed \(j\). Then \(\sum_j a_j^2\le1\) and
\[
\frac{Q_n-t_\theta}{s_n}\ \Rightarrow\ -\frac{1}{1-\theta}\left[\sum_{j\ge1}a_j(B_j-\theta)+\sqrt{\theta(1-\theta)(1-\sum_{j\ge1}a_j^2)}\,Z\right].
\]
Here the \(B_j\) are independent Bernoulli\((\theta)\), and \(Z\) is an independent standard Gaussian. The series converges almost surely and in \(L^2\). The limit is Gaussian exactly when every \(a_j=0\). Without profile convergence, every subsequence has a further subsequence satisfying the displayed convergence for some profile.

The distinct claim is the arbitrary ranked-profile law, in particular the regime in which both the series and the Gaussian term are present. For example, with \(w_{1,n}=c/\sqrt n\) and all other weights equal to \((1-c/\sqrt n)/(n-1)\) for sufficiently large \(n\), \(s_n\sim\sqrt{1+c^2}/\sqrt n\), \(a_1=c/\sqrt{1+c^2}\), and \(a_j=0\) for \(j\ge2\). At every fixed \(c>0\) this gives a non-Gaussian limit with an independent Gaussian component of strictly positive variance. A single weight that vanishes in absolute size can therefore remain visible at the fluctuation scale.

## Assumptions and scope

The rates are identical and the clocks independent. The quorum is a fixed strict threshold, and the weights are deterministic, positive and normalized. The condition \(s_n\to0\) is equivalent here to \(\max_jw_{j,n}\to0\) by \((\max_jw_{j,n})^2\le s_n^2\le\max_jw_{j,n}\). No result is asserted for unequal rates, moving thresholds, or persistent macroscopic weights.

## Proof

Write \(U_{j,n}=\lambda T_{j,n}/n\), which are independent unit exponentials. Let \(F(t)=1-e^{-t}\), \(M_n(t)=\sum_jw_{j,n}\mathbf1_{\{U_{j,n}\le t\}}\) and \(b_{j,n}=w_{j,n}/s_n\). The fixed-time fluctuation is
\[
X_n=\frac{M_n(t_\theta)-\theta}{s_n}=\sum_j b_{j,n}(\mathbf1_{\{U_{j,n}\le t_\theta\}}-\theta),\qquad \sum_j b_{j,n}^2=1.
\]
Fatou's lemma gives \(\sum_j a_j^2\le1\). For real \(u\), the logarithm of the characteristic function of \(b(B-\theta)\), with the branch near one, is \(-u^2\theta(1-\theta)b^2/2+O_u(|b|^3)\) as \(b\to0\). Split the product at rank \(k\). Choose \(k\) large enough that the logarithmic expansion applies in the tail for all sufficiently large \(n\). The total tail error is bounded by a constant times \(b_{k+1,n}\sum_{j>k}b_{j,n}^2\); its limit superior tends to zero as \(k\to\infty\). The first \(k\) factors converge individually, and the tail squared mass tends to \(1-\sum_{j\le k}a_j^2\). This proves \(X_n\Rightarrow X\), where \(X\) is the bracketed expression in the finding. The Bernoulli series exists almost surely and in \(L^2\) by convergence of the martingale of its partial sums.

For fixed real \(h\), take \(t_n=t_\theta+s_n h\), positive for all large \(n\). The increment \(D_n=M_n(t_n)-M_n(t_\theta)\) has expectation \((1-\theta)s_n h+O_h(s_n^2)\). Its variance is bounded by \(s_n^2 |F(t_n)-F(t_\theta)|=O_h(s_n^3)\), using independence for both signs of \(h\). Thus \(D_n/s_n\to(1-\theta)h\) in probability. The exact events \(\{Q_n\le t_n\}=\{M_n(t_n)>\theta\}\) give convergence of distribution functions at every continuity point of \(-X/(1-\theta)\); a discontinuous limit does not require evaluating the strict event at its atoms.

If \(\theta\ne1/2\), the third cumulant of \(X\) is \(\theta(1-\theta)(1-2\theta)\sum_j a_j^3\), nonzero when some \(a_j>0\). If \(\theta=1/2\), its fourth cumulant is \(-\sum_j a_j^4/8\). These cumulants are obtained by passing from the independent partial sums, whose uniform sub-Gaussian bounds follow from the square-summable ranges. If all \(a_j=0\), \(X\) is Gaussian. Finally, the padded ranked arrays lie in \([0,1]^{\mathbb N}\); a diagonal subsequence gives coordinate convergence along a further subsequence of any subsequence, to which the proof applies.

## Earlier Zipf result and relation to this theorem

For \(w_{j,n}=j^{-\rho}/H_{n,\rho}\), where \(H_{n,u}=\sum_{j=1}^n j^{-u}\), we have \(s_n=\sqrt{H_{n,2\rho}}/H_{n,\rho}\). The homogeneous-clock Zipf transition for \(0\le\rho<1\) was already stated in [1], including the critical scale at \(\rho=1/2\); it is not a new result here. In the ranked-profile formulation the limit is Gaussian of variance \(\theta/(1-\theta)\) for \(0\le\rho\le1/2\) because every normalized coefficient vanishes. For \(1/2<\rho\le1\), \(a_j=j^{-\rho}/\sqrt{\zeta(2\rho)}\), so the Gaussian component vanishes. In particular, at the harmonic endpoint \(\rho=1\), the same theorem gives \(s_n\sim \sqrt{\zeta(2)}/\log n\); at \(\theta=1/2\) the limit's standardized fourth cumulant is \(-2\zeta(4)/\zeta(2)^2=-4/5\). The endpoint is an application of the general law, not a separate originality claim.

Müller and Šebek [2] study this quorum model, including first-order and concentration results and different, aligned choices of rates and weights. Withers and Nadarajah [3] study higher-order approximations for weighted empirical functionals under regularity conditions. The general probability tools used in the proof are classical; no new general triangular-array or quantile theorem beyond this quorum result is claimed.

## Reproducibility and limitations

The accompanying `CHECK.py` from the source package checks finite rational discovery-mass, strict-crossing, cumulant and normalization identities. It is diagnostic only. The limiting assertions rely on the analytic proof above. No stopping-time moment convergence or stronger mode of convergence is asserted. The full text of Allouche and Gobet [4] was not available for comparison, and equivalent or stronger prior weighted-quantile results remain a possibility.

## References

1. *Gaussian-to-Bernoulli-series transition in Zipf-weighted quorum times*, Resultary record, 2026-10-12, https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-gaussian-to-bernoulli-series-transition-in-zipf-weighted-quorum--05cca1011618.
2. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1.
3. C. S. Withers and S. Nadarajah, *The distribution and quantiles of functionals of weighted empirical distributions when observations have different distributions*, arXiv:1002.4338.
4. M. Allouche and E. Gobet, *Wilks confidence regions for empirical weighted quantiles*, DOI:10.1016/j.spl.2026.110795.
