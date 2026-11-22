# Strict dispersive contraction for logarithms of exponential sample maxima

## Finding

For each real \(r>0\), consider the distribution on \(\mathbb R\)
\[
F_r(y)=\bigl(1-e^{-e^y}\bigr)^r.
\]
For integer \(r=n\ge1\), a random variable \(Y_n\) with this distribution is \(\log\max(E_1,\ldots,E_n)\), where the \(E_i\) are independent exponential variables of rate one. The positive real parameter also provides a natural continuously exponentiated family.

**Theorem.** For every \(0<r<s<\infty\) and \(0<u<v<1\),
\[
Q_s(v)-Q_s(u)<Q_r(v)-Q_r(u),\qquad
Q_r(u)=\log\bigl[-\log(1-u^{1/r})\bigr].
\]
Thus \(Y_s\) is strictly less dispersed than \(Y_r\). In addition, letting \(\mu_r=\mathbb EY_r\), the centered variables are strictly ordered in convex order:
\[
Y_s-\mu_s\ <_{\mathrm{cx}}\ Y_r-\mu_r.
\]
In particular, \(\mathrm{Var}(Y_s)<\mathrm{Var}(Y_r)\), and every strictly convex loss with finite expectations has smaller expectation under the centered \(Y_s\) law than under the centered \(Y_r\) law. These claims concern the whole distribution rather than only a second-moment sequence.

## Assumptions and scope

All logarithms are natural. The parameter \(r\) is any strictly positive real number. At integer \(r=n\) the generating exponentials are independent, identically distributed, continuous and unit-rate. For an exponential rate \(\lambda>0\), the log maximum is simply shifted by \(-\log\lambda\), so all dispersion and centered convex comparisons remain unchanged. Quantiles are indexed by \(0<u<1\); no endpoint quantile is required. The centered laws have moments of every finite order, because the left tail is exponentially small and the right tail is superexponentially small.

We use \(A\le_{\mathrm{cx}}B\) to mean equal finite means together with \(\mathbb E\phi(A)\le\mathbb E\phi(B)\) for every convex \(\phi\) for which the expectations exist. Strict inequality here means the inequality is strict for all strictly convex \(\phi\) with finite expectations. The *dispersive* assertion is the quantile-spacings inequality above.

## Proof

**1. Exact quantiles.** For real \(r>0\), solving \(F_r(y)=u\) gives
\[
Q_r(u)=\log\bigl[-\log(1-u^{1/r})\bigr],\qquad 0<u<1.
\]
Set \(a=-\log u>0\), \(z=a/r>0\), and \(w=1-e^{-z}=1-u^{1/r}\). Direct differentiation gives
\[
\frac{\partial Q_r(u)}{\partial u}
=\frac{e^{-z}}{r u(1-e^{-z})[-\log(1-e^{-z})]}
=\frac{1}{a u}\,
\frac{g(w)}{g(1-w)},
\qquad g(t)=\frac{-\log(1-t)}{t}.
\]
This normalization has no asymptotic approximation and is valid for every positive \(r\) and all interior quantile levels.

**2. Strict derivative contraction.** For \(0<t<1\),
\[
g(t)=\int_0^1\frac{d\xi}{1-t\xi},\qquad
 g'(t)=\int_0^1\frac{\xi\,d\xi}{(1-t\xi)^2}>0.
\]
Consequently the ratio \(g(w)/g(1-w)\) is *strictly increasing* in \(w\in(0,1)\): its numerator increases while its positive denominator decreases. For fixed \(u\), the quantity \(w_r=1-e^{-a/r}\) is strictly decreasing in \(r\), while \(1/(au)\) is independent of \(r\). Hence
\[
0<Q_s'(u)<Q_r'(u),\qquad 0<r<s,\quad 0<u<1.
\]
Integrating this pointwise strict inequality from \(u\) to \(v\) proves the theorem's strict quantile-spacings inequality. No assumption of log-convexity of the baseline cdf is used.

**3. Centered convex order.** Put \(D(u)=Q_s(u)-Q_r(u)\). Step 2 says that \(D\) is continuous and strictly decreasing. The integrability of the quantiles implies
\[
\int_0^1D(u)\,du=\mu_s-\mu_r.
\]
Therefore \(d(u)=D(u)-(\mu_s-\mu_r)\) is strictly decreasing, integrable and has mean zero on \((0,1)\). For every \(0<t<1\),
\[
\int_0^t d(u)\,du>0.
\]
Indeed, the mean of a strictly decreasing integrable function on any proper left interval is strictly greater than its mean on the whole interval. Thus, at every \(t\in(0,1)\),
\[
\int_0^t\bigl(Q_s(u)-\mu_s\bigr)\,du
>
\int_0^t\bigl(Q_r(u)-\mu_r\bigr)\,du.
\]
The integrated-quantile characterization of convex order (for equal means) gives the asserted strict centered convex order. Strictness against each strictly convex finite-expectation loss follows from the strict integrated-quantile gap and the usual representation of convex functions by positive second-derivative measures. In particular the strictly convex square gives the strict variance inequality.

There is also a direct variance check: writing a centered random variable as its quantile at a uniform \(U\),
\[
\operatorname{Var}(Y_r)=\frac12\int_0^1\!\int_0^1
\bigl(Q_r(u)-Q_r(v)\bigr)^2\,du\,dv.
\]
Every nonzero quantile difference has strictly smaller absolute value at parameter \(s>r\), so this integral is strictly smaller as well. This establishes the claimed variance conclusion without invoking any unproved asymptotic or approximation.

## Verification

The standalone standard-library file `checker.py` reconstructs the cdf and quantile independently, compares their inverse relation, differentiates the quantile numerically and tests the analytic derivative formula, then verifies strict derivative and quantile-spacings inequalities on a nontrivial finite grid of shape parameters and quantile levels. The checks are finite *diagnostics*, not a proof for all real parameters; that proof is given in Steps 1–3 above. The exact count is printed by the checker.

To reproduce, run `python3 checker.py` in the directory containing the extracted files. No additional package is required.

## Relationship to prior work

The mathematical gap is motivated by stochastic comparisons of extreme order statistics and by the multi-collector coupon problem's logarithmic-exponential maximum law. Das, Kayal and Choudhuri (first available online 18 October 2019) discuss usual, hazard and likelihood-ratio comparisons for exponentiated location-scale extremes; their accessible abstract does not state dispersive or centered convex comparisons. Mesfioui and Trufin (4 December 2021) investigate dispersive comparison between sample maxima, including samples of different sizes. Their Proposition 4.1 requires a log-convex baseline distribution function; the present log-exponential baseline \(F_1(y)=1-e^{-e^y}\) is instead strictly log-concave, since its reversed hazard \(F'_1(y)/F_1(y)=e^y/(e^{e^y}-1)\) is strictly decreasing. Thus their sufficient condition cannot imply this theorem. Their full open-access paper was inspected, including Section 4 and its counterexample for a uniform baseline.

Doumas (first posted 8 February 2022) identified alternating-binomial expressions for an asymptotic variance in independent coupon collection. A March 2026 note identifies that coefficient with \(\operatorname{Var}(Y_n)\), and Giam (2026) separately **proved the decreasing variance coefficient**. Thus decreasing variance for integer \(n\) is **prior work**, not the contribution claimed here. The statement here is the stricter, real-parameter *full quantile contraction and centered convex ordering*, neither of which follows logically from variance monotonicity.

The related 2021 work of Alimohammadi, Esna-Ashari and Cramer concerns dispersive ordering of order statistics from increasing-reversed-hazard-rate distributions. The present baseline has a *decreasing* reversed hazard, so that sufficient condition is inapplicable. Its complete text and that of Giam's note were not accessible for material comparison; potential coverage beyond their stated abstract theorems remains a historical-priority limitation.

## Limitations

This theorem is specific to the cdf family \(F_r(y)=(1-e^{-e^y})^r\). It does not claim a sample-size dispersive order for arbitrary iid laws; indeed, general cdfs can yield incomparable extremes. It does not establish noninteger parameters as actual integer-size samples, nor a finite-coupon completion-time ordering. Stronger literature not identified in the available full texts could predate this observation; an independent literature audit remains outstanding. The deterministic proof is self-contained, while the accompanying finite-grid computations carry no infinite-certification claim.

## References

1. S. Das, S. Kayal and D. Choudhuri, *Ordering results on extremes of exponentiated location-scale models*, first published online 18 October 2019, DOI 10.1017/S0269964819000408. https://doi.org/10.1017/S0269964819000408
2. M. Mesfioui and J. Trufin, *Dispersive order comparisons on extreme order statistics from homogeneous dependent random vectors*, 4 December 2021, DOI 10.1515/demo-2021-0118, especially Proposition 4.1 and Section 4. https://doi.org/10.1515/demo-2021-0118
3. A. V. Doumas, *On the minimum of independent collecting processes via the Stirling numbers of the second kind*, first posted 8 February 2022, arXiv:2202.03713. https://arxiv.org/abs/2202.03713
4. A. V. Doumas, *An inequality involving alternating binomial sums*, 11 March 2026, DOI 10.1016/j.spl.2026.110735; identifies the variance as a log-exponential-maximum variance. https://doi.org/10.1016/j.spl.2026.110735
5. K. K. Giam, *Decreasing nature of a sequence related to the Coupon Collector's problem*, 2026, DOI 10.1016/j.spl.2026.110790; known integer-parameter variance monotonicity. https://doi.org/10.1016/j.spl.2026.110790
6. M. Alimohammadi, M. Esna-Ashari and E. Cramer, *On dispersive and star orderings of random variables and order statistics*, *Statistics & Probability Letters* 170 (2021), DOI 10.1016/j.spl.2020.109014. https://doi.org/10.1016/j.spl.2020.109014
