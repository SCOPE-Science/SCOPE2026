# Gaussian-to-Bernoulli-series transition for weighted coupon quorum times

## Finding

Consider independent first-discovery times \(T_{j,n}\sim\operatorname{Exp}(\lambda/n)\), \(1\le j\le n\), with \(\lambda>0\). For positive deterministic weights \(w_{j,n}\) summing to one and a fixed quorum \(\theta\in(0,1)\), let
\[
\tau_n=\inf\Big\{t\ge0:\sum_{j=1}^{n}w_{j,n}\mathbf1_{\{T_{j,n}\le t\}}>\theta\Big\}.
\]
Define \(s_n=(\sum_jw_{j,n}^2)^{1/2}\), \(t_\theta=-\log(1-\theta)\), and the dimensionless completion time \(Q_n=\lambda\tau_n/n\). Assume \(s_n\to0\). Rearrange the weights in descending order, and suppose for every fixed \(j\ge1\) that \(w_{j,n}/s_n\to a_j\). Then \(\sum_ja_j^2\le1\), and
\[
\boxed{\frac{Q_n-t_\theta}{s_n}\ \Rightarrow\ -\frac{1}{1-\theta}\left[\sum_{j=1}^{\infty}a_j(B_j-\theta)+\sqrt{\theta(1-\theta)\left(1-\sum_{j=1}^{\infty}a_j^2\right)}\,Z\right].}
\]
Here \(B_j\) are independent \(\operatorname{Bernoulli}(\theta)\), \(Z\sim\mathcal N(0,1)\) is independent, and the series converges in \(L^2\) and almost surely. The limiting distribution is Gaussian if and only if every \(a_j=0\); otherwise it is non-Gaussian. Without the coordinate-convergence assumption, every sequence admits a subsequence for which the displayed conclusion holds after taking a further subsequence, though the resulting profile may depend on that subsequence.

**Zipf specialization.** Let \(w_{j,n}=j^{-\rho}/H_{n,\rho}\), where \(H_{n,u}=\sum_{j=1}^n j^{-u}\), with \(0\le\rho\le1\). Here \(s_n=\sqrt{H_{n,2\rho}}/H_{n,\rho}\to0\). The normalized quorum time is Gaussian for \(0\le\rho\le1/2\):
\[
\frac{Q_n-t_\theta}{s_n}\Rightarrow\mathcal N\!\left(0,\frac{\theta}{1-\theta}\right).
\]
For \(1/2<\rho\le1\), it has instead the non-Gaussian limit
\[
\frac{Q_n-t_\theta}{s_n}\Rightarrow
-\frac{1}{(1-\theta)\sqrt{\zeta(2\rho)}}
\sum_{j=1}^{\infty}j^{-\rho}(B_j-\theta).
\]
The natural fluctuation scales are, respectively,
\[
s_n\sim
\begin{cases}
\dfrac{1-\rho}{\sqrt{1-2\rho}}n^{-1/2},&0\le\rho<1/2,\\[3pt]
\dfrac{\sqrt{\log n}}{2\sqrt n},&\rho=1/2,\\[3pt]
(1-\rho)\sqrt{\zeta(2\rho)}\,n^{\rho-1},&1/2<\rho<1,\\[3pt]
\dfrac{\sqrt{\zeta(2)}}{\log n},&\rho=1.
\end{cases}
\]
For the non-Gaussian limit at \(\theta=1/2\), the standardized fourth cumulant is \(-2\zeta(4\rho)/\zeta(2\rho)^2\). At \(\rho=1\), this equals exactly \(-4/5\), despite the same leading variance as in the Gaussian cases.

## Assumptions and scope

All weights are deterministic, positive and normalized; all discovery clocks are independent and have the identical continuous-time rate \(\lambda/n\). The strict threshold is fixed strictly between zero and one. The first theorem assumes \(s_n\to0\) (which is equivalent here to \(\max_jw_{j,n}\to0\)) and convergence of the ranked \(\ell^2\)-normalized weights. Nothing is claimed for nonhomogeneous clocks, for persistent macroscopic weights, for moving thresholds, or for higher-order corrections.

## Proof

1. **Fixed-time weighted-sum limit.** Let \(U_{j,n}=\lambda T_{j,n}/n\); these are independent unit exponentials. Write \(F(t)=1-e^{-t}\), \(M_n(t)=\sum_jw_{j,n}\mathbf1_{\{U_{j,n}\le t\}}\), and \(b_{j,n}=w_{j,n}/s_n\). At \(t_\theta\), the variables \(B_{j,n}=\mathbf1_{\{U_{j,n}\le t_\theta\}}\) are independent Bernoulli variables of parameter \(\theta\), so
   \[
   X_n:=\frac{M_n(t_\theta)-\theta}{s_n}=\sum_jb_{j,n}(B_{j,n}-\theta),\qquad\sum_jb_{j,n}^2=1.
   \]
   The ranked coefficients have limits \(a_j\), and Fatou's lemma gives \(\sum_ja_j^2\le1\). For fixed real \(u\), the characteristic function of the centered Bernoulli variable satisfies
   \[
   \log\mathbb E e^{iu b(B-\theta)}=-\tfrac12\theta(1-\theta)u^2b^2+O_u(|b|^3)
   \]
   uniformly for sufficiently small \(|b|\). For every fixed \(k\), split off the first \(k\) coefficients. The remaining cubic error is bounded by a constant times \(\max_{j>k}b_{j,n}\sum_{j>k}b_{j,n}^2\), hence its limit superior is bounded by a constant times \(a_{k+1}\), which tends to zero as \(k\to\infty\). Passing first \(n\to\infty\), then \(k\to\infty\), the characteristic functions converge to those of
   \[
   X=\sum_ja_j(B_j-\theta)+\sqrt{\theta(1-\theta)(1-\sum_ja_j^2)}Z.
   \]
   Independence and \(\ell^2\)-summability give existence of the infinite series; thus \(X_n\Rightarrow X\).

2. **Local inversion of the strictly crossed threshold.** For each fixed real \(h\), put \(t_n=t_\theta+s_nh\), which is nonnegative for large \(n\). The increment \(D_n=M_n(t_n)-M_n(t_\theta)\) has mean \(F(t_n)-F(t_\theta)=(1-\theta)s_nh+O_h(s_n^2)\). Whether \(h\) is positive or negative, independence yields
   \[
   \operatorname{Var}(D_n)\le\sum_jw_{j,n}^2|F(t_n)-F(t_\theta)|=O_h(s_n^3).
   \]
   Hence \(D_n/s_n\to(1-\theta)h\) in probability. Since \(M_n\) is nondecreasing and right-continuous,
   \[
   \{Q_n\le t_n\}=\{M_n(t_n)>\theta\}.
   \]
   Therefore at every continuity point \(h\) of the law of \(-X/(1-\theta)\), the distribution functions converge to \(\Pr\{-X/(1-\theta)\le h\}\). This proves the asserted weak limit, including cases where the limit itself has atoms.

3. **Gaussian rigidity.** For \(\theta\ne1/2\), the third cumulant of \(X\) equals \(\theta(1-\theta)(1-2\theta)\sum_ja_j^3\). It is nonzero whenever some \(a_j>0\). For \(\theta=1/2\), the fourth cumulant is \(-\tfrac18\sum_ja_j^4<0\) in that case. Consequently \(X\), and hence its nonzero linear transform, cannot be Gaussian unless every \(a_j\) vanishes. Conversely if all vanish, the displayed formula is Gaussian. All relevant cumulants exist because the independent centered Bernoulli series is sub-Gaussian under \(\ell^2\)-summability. For arbitrary ranked arrays, compactness of \([0,1]^\mathbb N\) by a diagonal subsequence and step 1 give the stated subsequential assertion.

4. **Power-law phase transition.** With Zipf weights, \(b_{j,n}=j^{-\rho}/\sqrt{H_{n,2\rho}}\). If \(2\rho\le1\), every fixed normalized coefficient tends to zero; the Gaussian component has full variance. If \(2\rho>1\), the coefficients converge to \(a_j=j^{-\rho}/\sqrt{\zeta(2\rho)}\) and have squared sum one, leaving no Gaussian component. Standard power-sum asymptotics give the four scales shown above. At \(\theta=1/2\), the cumulant identity and \(\zeta(2)=\pi^2/6\), \(\zeta(4)=\pi^4/90\) yield the stated excess kurtosis of \(-4/5\) at \(\rho=1\).

## Verification

The standalone `CHECK.py` uses exact rational arithmetic to compare two independent finite-state descriptions of the discovery-mass distribution, validate the strict-crossing CDF identity, verify the first four centered moments and cumulants, and check the finite Zipf variance normalization. Executing `python CHECK.py` yielded `PASS 1019 exact rational checks`. These are finite diagnostic checks; the analytic characteristic-function and inverse-process arguments establish the limiting theorem. Reproduce with Python 3, standard library only.

## Relationship to prior work

Müller and Šebek, *Weighted-threshold Coupon Collection* (arXiv:2607.08551v1, July 9, 2026), introduced the same quorum model and established homogeneous-clock first-order universality under diffuse weights, together with concentration and separate aligned-Zipf results. The present fluctuation theorem keeps clocks homogeneous and characterizes a transition hidden beneath that first-order universality. Earlier weighted-empirical-distribution and weighted-quantile work, including Withers and Nadarajah (2010), develops Gaussian or Edgeworth expansions under regularity conditions; that is not the Bernoulli-series regime. General triangular-array probability tools underlie the proof, so its novelty is claimed only as the explicit quorum-time law and associated Zipf fluctuation boundary, not as a new general probability-limit principle.

## Limitations

The available portion of the motivating manuscript includes its abstract, introduction, model and early concentration results; later full-text sections could not be re-opened during comparison. Thus full-manuscript priority remains a material historical risk. The 2026 weighted-quantile article by Allouche and Gobet and the 1999 weighted partial-sums article by Csörgő, Norvaiša and Szyszkowicz were accessible only to abstract-level inspection; broader literature might implicitly cover aspects of the limit through existing general theorems. The proof is not an independent mathematical audit. No conclusion is offered about total-variation convergence, moment convergence of the stopping-time normalization, or nonhomogeneous weights and rates beyond the specified model.

## References

- S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1 (first submitted 2026-07-09), https://arxiv.org/abs/2607.08551 .
- C. S. Withers and S. Nadarajah, *The distribution and quantiles of functionals of weighted empirical distributions when observations have different distributions*, arXiv:1002.4338 (2010), https://arxiv.org/abs/1002.4338 .
- M. Allouche and E. Gobet, *Wilks confidence regions for empirical weighted quantiles*, Statistics & Probability Letters (2026), DOI:10.1016/j.spl.2026.110795 .
- M. Csörgő, R. Norvaiša and B. Szyszkowicz, *Convergence of weighted partial sums when the limiting distribution is not necessarily Radon*, Stochastic Processes and their Applications 81 (1999), 81–101, DOI:10.1016/S0304-4149(98)00100-8 .
- *Approaching the coupon collector’s problem with group drawings via Stein’s method*, Journal of Applied Probability 60 (2023), 1352–1366, DOI:10.1017/jpr.2023.6 .
