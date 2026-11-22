# Exponentially invisible smooth alternatives for the Lévy quantile-conditional-mean ratio test

## Finding

For the two-band statistic \(O_n\) of Pączek, Jelito, Pitera and Wyłomańska, with their implemented quantile bands \((0,0.3)\) and \((0.8,0.95)\), there are explicit strictly positive, smooth, non-Lévy densities whose entire statistic distributions are exponentially close in total variation to the Lévy null. This is stronger than mere cancellation of a population contrast: **every rejection rule based only on this statistic has asymptotically the same rejection probability under such an alternative as under the null**.

Specifically, put \(p=2/5\), \(q=7/10\), let \(Q(u)=[\Phi^{-1}(1-u/2)]^{-2}\) be the unit-scale one-sided Lévy quantile, and set
\[
 h(u)=\begin{cases}\sin^4\bigl(\pi(u-p)/(q-p)\bigr),&p<u<q,\\0,&\text{otherwise}.\end{cases}
 \qquad Q_\varepsilon(u)=Q(u)+\varepsilon h(u),\quad0<\varepsilon\le1/10.
\]
For \(U\sim\operatorname{Unif}(0,1)\), let \(P_0\) be the law of \(Q(U)\) and \(P_\varepsilon\) that of \(Q_\varepsilon(U)\). The latter is a distinct, strictly positive \(C^2\)-density law on \((0,\infty)\), agreeing with \(P_0\) on both value tails outside \([Q(p),Q(q)]\). More generally, any nonzero \(C^3\) perturbation of the quantile map supported in \([p,q]\), with its first three derivatives zero at the endpoints and sufficiently small derivative to retain monotonicity, obeys the same total-variation upper bound. Thus the blind class is infinite-dimensional; the sharp coupling exponent below is asserted for the displayed positive sine-power perturbation.

For every integer \(n\ge20\), put \(k=\lfloor3n/10\rfloor\), \(\ell=\lfloor4n/5\rfloor+1\), and
\[
 \eta_n=\Pr\{\operatorname{Bin}(n,2/5)\le k-1\}
 +\Pr\{\operatorname{Bin}(n,7/10)\ge\ell\}.
\]
Then the statistic laws satisfy the **nonasymptotic bound**
\[
 \sup_{B\in\mathcal B(\mathbb R)}
 |\Pr_{P_\varepsilon}\{O_n\in B\}-\Pr_{P_0}\{O_n\in B\}|
 \le \eta_n.
\]
The discrepancy bound has the sharp logarithmic rate
\[
 \lim_{n\to\infty}-\frac1n\log\eta_n
 =D\bigl(3/10\,\|\,2/5\bigr)
 =0.0216008541435465\ldots,
\]
where \(D(s\|t)=s\log(s/t)+(1-s)\log((1-s)/(1-t))\).
Moreover, under the *specified common-uniform quantile coupling*, the probability that the two \(O_n\) values differ has **exactly the same logarithmic rate**. This latter sharpness is a statement about this coupling, not an assertion that the total-variation distance itself has an optimal lower bound.

As a concrete finite-sample consequence, \(\eta_{500}=1.51157135\times10^{-6}\) and \(\eta_{1000}=2.03447303\times10^{-11}\). If a null-calibrated test using only \(O_n\) has rejection probability converging to \(\alpha\) under \(P_0\), its rejection probability under each fixed \(P_\varepsilon\) also converges to \(\alpha\), rather than one.

## Assumptions and scope

The null consists of i.i.d. positive observations from the one-sided Lévy scale family with CDF \(F_c(x)=\operatorname{erfc}(\sqrt{c/(2x)})\) for \(x>0\). The constructed alternative uses scale \(c=1\), which suffices to disprove universal consistency. Quantile functions are continuous and strictly increasing. Only the **fixed-band QCM ratio** is considered, not the paper's different ensemble statistic, location-adjusted statistic or alternative quantile configurations.

Given a positive sample \(x_1,\ldots,x_n\), write \(x_{(1)}\le\cdots\le x_{(n)}\), \(k=\lfloor0.3n\rfloor\), \(\ell=\lfloor0.8n\rfloor+1\), \(j=\lfloor0.95n\rfloor\), and
\[
 A_n=\frac1k\sum_{i=1}^k x_{(i)},\quad
 B_n=\frac1{j-\ell+1}\sum_{i=\ell}^{j}x_{(i)}.
\]
Writing \(m_1=\mu_{P_0}(0,0.3)>0\), \(m_2=\mu_{P_0}(0.8,0.95)>0\), the source's statistic is
\[
 O_n=\sqrt n\left(\frac{A_n/m_1}{B_n/m_2}-1\right).
\]
No fitted parameters from unused order statistics enter \(O_n\). The two bands have nonempty denominators for \(n\ge20\).

## Proof

**1. The alternative is a legitimate smooth nonnull law.** The unit Lévy density is
\[
 f_0(x)=\frac{x^{-3/2}}{\sqrt{2\pi}}e^{-1/(2x)},\quad x>0.
\]
Differentiating its log shows the global maximum occurs at \(x=1/3\), with
\[
 f_{\max}=\frac{3^{3/2}e^{-3/2}}{\sqrt{2\pi}}<0.463.
\]
Thus \(Q'(u)=1/f_0(Q(u))\ge1/f_{\max}>2.1619\). Direct maximization of \(4\sin^3\theta\cos\theta\) gives
\[
 \sup_{u\in(0,1)}|h'(u)|=\frac{3\sqrt3\pi}{4(q-p)}<13.604.
\]
Therefore \(Q_\varepsilon'(u)>2.1619-(1/10)13.604>0.8015\) everywhere. The bump and its first three derivatives vanish at \(p,q\), so \(Q_\varepsilon\) is \(C^3\), increasing from zero to infinity. Its inverse is \(C^3\) and has strictly positive \(C^2\) density \(f_\varepsilon(y)=1/Q_\varepsilon'(Q_\varepsilon^{-1}(y))\). The law agrees with \(P_0\) outside the value interval \([Q(p),Q(q)]\), but \(Q_\varepsilon((p+q)/2)=Q((p+q)/2)+\varepsilon\), so it is not Lévy: a Lévy scale change would alter all positive quantiles, including those below \(p\).

**2. Pathwise equality on a high-probability rank event.** Take i.i.d. \(U_1,\ldots,U_n\sim\operatorname{Unif}(0,1)\). Couple the two samples as \(X_i=Q(U_i)\) and \(Y_i=Q_\varepsilon(U_i)\). Both quantile maps are strictly increasing; hence they preserve the same rank permutation. Let \(N_p=\sum_i1_{\{U_i\le p\}}\) and \(N_q=\sum_i1_{\{U_i\le q\}}\). On
\[
 E_n=\{N_p\ge k\}\cap\{N_q<\ell\},
\]
all observations used in the first QCM have ranks with \(U_{(i)}\le p\), and all used in the second QCM have \(U_{(i)}>q\). Since \(Q_\varepsilon=Q\) there, both QCMs, and therefore both \(O_n\) values, agree *exactly*. The coupling inequality and the union bound yield the stated binomial upper bound for the total-variation distance, for every Borel rejection region and every \(n\ge20\).

**3. The exact exponential rate.** The binomial large-deviation limits, with the floor changes contributing only \(o(n)\), are
\[
 -\frac1n\log\Pr(N_p<k)\to D(0.3\|0.4),\qquad
 -\frac1n\log\Pr(N_q\ge\ell)\to D(0.8\|0.7).
\]
The first rate is strictly smaller: \(0.0216008541435465\ldots<0.0257320924779853\ldots\), proving the rate for \(\eta_n\). For sharpness of the coupling disagreement, consider
\[
 H_n=\{N_p=k-1,\quad k\le N_q<\ell\}.
\]
On \(H_n\), at least one transformed point from \((p,q)\) belongs to the lower QCM, strictly increasing its value, whereas the upper QCM is unchanged. Thus \(O_n(Y)>O_n(X)\). Conditional on \(N_p=k-1\), the count \(N_q-(k-1)\) has law \(\operatorname{Bin}(n-k+1,1/2)\). Its mean is asymptotic to \(0.35n\), whereas the upper permitted value \(\ell-k\) is asymptotic to \(0.5n\). Therefore \(\Pr(H_n\mid N_p=k-1)\to1\). By Stirling's formula,
\[
 -\frac1n\log\Pr(N_p=k-1)\to D(0.3\|0.4).
\]
Sandwiching the coupling disagreement probability between \(\Pr(H_n)\) and \(\eta_n\) proves the claimed sharp coupling exponent.

**4. This is failure of detection, not equality of the populations.** At \(x_0=Q(0.55)\), the reference CDF equals \(0.55\). Because \(Q_\varepsilon(0.55)>x_0\), the alternative CDF satisfies \(F_\varepsilon(x_0)=0.55-\delta_\varepsilon\) with \(\delta_\varepsilon>0\). A one-point empirical-CDF test with threshold \(0.55-\delta_\varepsilon/2\) has each of its two errors at most \(\exp(-n\delta_\varepsilon^2/2)\) by Hoeffding's inequality. Thus the full i.i.d. samples are consistently distinguishable even as the specified \(O_n\) statistic remains asymptotically blind.

## Verification

Run `python3 checker.py` with Python 3 standard library. The checker independently evaluates the analytic derivative margin, exact binomial-tail bounds, Chernoff inequalities, separated rank-band coupling on generated samples, lower-excursion strict inequality, and separation of the alternative's CDF at \(Q(0.55)\). It passed 24,271 deterministic/numerical assertions. The numerical calculations verify concrete values and formulas, not the infinite-\(n\) statements; those follow from the proof above.

For \(\varepsilon=0.1\), the numerical CDF separation at \(x_0=Q(0.55)\) is \(0.007214711952\ldots\). The exact binomial-tail bound is \(0.0236625265\ldots\) at \(n=100\), \(1.51157135\times10^{-6}\) at \(n=500\), and \(2.03447303\times10^{-11}\) at \(n=1000\). The displayed probabilities are rounded, not used as premises in the argument.

## Relationship to prior work

Pączek, Jelito, Pitera and Wyłomańska (arXiv:2311.15359, first publicly available November 26, 2023; Journal of Applied Statistics 2024) introduce this exact two-band statistic, its fixed-scale-free normalization, null asymptotic normality, and empirical power comparisons. Their analysis motivates separated bands for tail discrimination; it does not derive the smooth central-deformation class, exponential *statistic-law* coupling, or the sharp coupling mismatch exponent established here. Their separate ensemble statistic uses full-sample estimators and is **not** implicated by this theorem.

The same authors' earlier quantile-conditional-variance work (arXiv:2212.13502) concerns stability-index estimation, not this Lévy two-QCM testing functional. The large-deviation and coupling tools employed here are classical; novelty is claimed only for the assembled, statistic-specific, quantitative impossibility and sharp rate, **not** for Hoeffding or Chernoff bounds themselves. Searches of relevant literature and mathematical-result records yielded no directly covering statement. An older general theory of rank-band insensitivity could potentially subsume parts of the argument; this is a historical-priority limitation.

## Limitations

The bound and blind-alternative conclusion apply to the published fixed two-band \(O_n\) statistic, its measurable functions and tests using **only** that statistic. They do not apply automatically to the paper's \(T_n\) ensemble, \(V_n\), or tests that also use central observations or other fitted summaries. The asymptotic rejection result assumes the null rejection probabilities actually converge to their calibrated limit. The exact exponent is established for the explicit common-uniform *coupling disagreement*, not as a lower bound on distributional total variation. The construction gives a fixed, detectable alternative; it does not describe minimax separation rates or any practical large-sample optimality of other tests.

## References

1. K. Pączek, D. Jelito, M. Pitera, A. Wyłomańska, *Goodness-of-fit tests for the one-sided Lévy distribution based on quantile conditional moments*, arXiv:2311.15359v1, 26 November 2023, https://arxiv.org/abs/2311.15359; Journal of Applied Statistics 51 (2024), 3154–3177, DOI:10.1080/02664763.2024.2340592, https://pmc.ncbi.nlm.nih.gov/articles/PMC11536646/.
2. K. Pączek, D. Jelito, M. Pitera, A. Wyłomańska, *Estimation of stability index for symmetric α-stable distribution using quantile conditional variance ratios*, arXiv:2212.13502v1, 27 December 2022, https://arxiv.org/abs/2212.13502.
3. H. Chernoff, *A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations*, Annals of Mathematical Statistics 23 (1952), 493–507, https://doi.org/10.1214/aoms/1177729330. Standard binomial relative-entropy tail bounds and Stirling's formula are used in their elementary forms.
4. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, Journal of the American Statistical Association 58 (1963), 13–30, https://doi.org/10.1080/01621459.1963.10500830.
