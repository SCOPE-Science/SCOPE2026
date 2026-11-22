# Saturation shifts optimal one-bit quadrature to the first-arrival timescale

## Finding

An event-count trajectory has a natural integral—the total event-time exposure or cumulative count area—yet a sensor that reports only whether *any* event has occurred behaves very differently from an exact count sensor. The following theorem gives the exact Bayes-optimal observation time, estimator, and mean-square risk for both an unconditioned Poisson path and a path conditioned on its total event count.

**Theorem (one-bit count-path quadrature).** On the unit horizon, let \(J=\int_0^1 N(s)\,\mathrm ds\). Exactly one nonadaptive observation at a deterministic time \(t\in[0,1]\) reports \(Y_t=\mathbf1_{\{N(t)\ge1\}}\). The sensor has no false positives or missed detections, but *saturates* at one event. Under squared error, use the conditional-mean estimator.

**(A) Poisson model.** If \(N\) is homogeneous Poisson of known rate \(\lambda>0\), the explained variance and residual risk, for \(0<t<1\), are
\[
 I_\lambda(t)=\frac{\lambda^2(t-t^2/2)^2}{e^{\lambda t}-1},\qquad R_\lambda(t)=\frac\lambda3-I_\lambda(t).
\]
There is a unique globally optimal \(t_\lambda\in(0,1)\), characterized by
\[
 \frac{\lambda t_\lambda}{1-e^{-\lambda t_\lambda}}=\frac{2(1-t_\lambda)}{1-t_\lambda/2}.
\]
It is strictly decreasing in \(\lambda\), with \(t_\lambda\to2/3\) as \(\lambda\downarrow0\). As \(\lambda\to\infty\),
\[
 \lambda t_\lambda\to c_*,\qquad
 \frac{I_\lambda(t_\lambda)}{\operatorname{Var}(J)}\sim\frac{3c_*(2-c_*)}{\lambda}.
\]

**(B) Fixed-count model.** For integer \(m\ge1\), let exactly \(m\) event times be independent uniform points of \([0,1]\), so \(N(1)=m\). The explained variance and residual risk are
\[
 I_m(t)=\frac{m^2t^2(1-t)^m}{4[1-(1-t)^m]},\qquad R_m(t)=\frac m{12}-I_m(t),\qquad 0<t<1.
\]
The unique globally optimal \(t_m\in(0,1)\) is determined by
\[
 2\sum_{k=1}^{m}(1-t_m)^k=m.
\]
It satisfies \(t_1=1/2\), is strictly decreasing with \(m\), and obeys
\[
 mt_m\to c_*,\qquad
 \frac{I_m(t_m)}{\operatorname{Var}(J)}\sim\frac{3c_*(2-c_*)}{m}.
\]
In both models the same strictly positive constant \(c_*\) is the unique root in \((1,2)\) of
\[
 2(1-e^{-c_*})=c_*,\qquad c_*=1.59362426004004\ldots,
 \quad 3c_*(2-c_*)=1.94283071367574\ldots.
\]

**Exact-count comparator.** If \(N(t)\), rather than its saturated bit, is observed, the Poisson-model optimal time is \(2/3\), and the maximum explained fraction is \(8/9\), independent of \(\lambda\). Under fixed count \(m\), exact counting is optimal at \(1/2\) and explains \(3/4\) of the variance. In contrast, the optimal single bit explains a fraction tending to zero at inverse expected-count order in either model. The classical exact-count placement in the Poisson model is prior work, not a new claim.

## Assumptions and scope

All events occur on \([0,1]\). The Poisson rate \(\lambda\) and, separately, the fixed total count \(m\) are known to the estimator. There is a *single deterministic observation time*, no sensor cost depending on time, no randomized observation time, and only the bit \(Y_t\), not the count or event timestamps, is retained. Observations are exact except for count saturation. The goal is to predict the *random realization* of the path integral, not to infer an unknown event rate. Squared-error Bayes optimality ranges over **all measurable estimators of this one bit**, not just linear estimators. The two models are distinct probability laws; the fixed-count model is the conditional law of the Poisson model given \(N(1)=m\).

## Proof

1. **A binary regression identity.** For a square-integrable \(J\) and a Bernoulli bit \(Y\) of success probability strictly between zero and one, \(\mathbb E[J\mid Y]\) is affine in \(Y\). Its reduction of mean-square risk is exactly
\[
 \operatorname{Var}(\mathbb E[J\mid Y])=\frac{\operatorname{Cov}(J,Y)^2}{\operatorname{Var}(Y)}.
\]
The law of total variance gives \(R=\operatorname{Var}(J)-I\). At \(t=0\), the bit is constant in both models and the explained variance is zero. At \(t=1\) it is constant only under fixed total count: in the unconditioned Poisson model it still indicates whether any arrival occurred, and the formula for \(I_\lambda(1)\) remains strictly positive. The fixed-count information tends to zero as \(t\uparrow1\).

2. **Poisson covariance and estimator.** Write the arrivals as \(U_i\) and use \(J=\sum_{U_i\le1}(1-U_i)\). Campbell's covariance formula gives \(\mathbb E J=\lambda/2\) and \(\operatorname{Var}(J)=\lambda/3\). The no-arrival probability is \(q=e^{-\lambda t}\), and conditioning on \(N(t)=0\) leaves an independent future Poisson process, yielding
\[
 \mathbb E[J\mid Y_t=0]=\frac\lambda2(1-t)^2,\qquad
 \operatorname{Cov}(J,Y_t)=\lambda(t-t^2/2)q.
\]
Since \(\operatorname{Var}(Y_t)=q(1-q)\), the claimed \(I_\lambda\) follows. The other conditional mean is
\[
 \mathbb E[J\mid Y_t=1]=\frac\lambda2+\frac{\lambda(t-t^2/2)q}{1-q}.
\]
Differentiating \(\log I_\lambda\) shows that stationarity is precisely the equation in (A). Define \(g(x)=x/(1-e^{-x})\) and \(h(t)=2(1-t)/(1-t/2)\). On positive arguments, \(g\) is strictly increasing because \(1-(1+x)e^{-x}>0\), whereas \(h\) is strictly decreasing on \([0,1]\). Their boundary values satisfy \(g(0+)=1<h(0)=2\) and \(g(\lambda)>h(1)=0\). Hence their intersection is unique and its derivative changes from positive to negative at this unique crossing, so it is the unique global maximum even though the Poisson endpoint \(t=1\) retains some information. Increasing \(\lambda\) increases \(g(\lambda t)\) at each fixed \(t\), so the intersection time strictly decreases. Since \(g(\lambda t_\lambda)=h(t_\lambda)\le2\), \(\lambda t_\lambda\le c_*\); the resulting \(t_\lambda\to0\) as \(\lambda\to\infty\), and passing to the equation gives \(\lambda t_\lambda\to c_*\). As \(\lambda\downarrow0\), \(g(\lambda t)\to1\) uniformly, so \(h(t_\lambda)\to1\) and \(t_\lambda\to2/3\).

3. **Fixed-count covariance and estimator.** With \(U_1,\ldots,U_m\) independent uniform, \(J=\sum_{i=1}^m(1-U_i)\) has mean \(m/2\) and variance \(m/12\). Set \(q=(1-t)^m=\Pr(Y_t=0)\). Conditioning every \(U_i>t\) gives
\[
 \mathbb E[J\mid Y_t=0]=\frac{m(1-t)}2,
 \quad \operatorname{Cov}(J,Y_t)=\frac{mtq}{2},
 \quad \mathbb E[J\mid Y_t=1]=\frac m2+\frac{mtq}{2(1-q)}.
\]
The binary regression identity yields \(I_m\). Differentiating \(\log I_m\) gives \(2/t-m/[(1-t)(1-(1-t)^m)]\). Thus an interior stationary point obeys \(2(1-t)(1-(1-t)^m)=mt\), equivalent to \(2\sum_{k=1}^m(1-t)^k=m\). The sum is strictly decreasing from \(m\) to zero as \(t\) grows from zero to one, giving exactly one critical point and global maximizer. At fixed \(t>0\), the average \(m^{-1}\sum_{k=1}^m(1-t)^k\) strictly decreases as \(m\) grows; therefore the root \(t_m\) is strictly decreasing.

4. **Common high-density law and information barrier.** Let \(x_m=mt_m\). For fixed positive \(x\),
\[
 \frac1m\sum_{k=1}^m(1-x/m)^k\longrightarrow\int_0^1 e^{-xs}\,\mathrm ds=\frac{1-e^{-x}}x.
\]
Strict monotonicity and bracketing about the unique positive solution of \(2(1-e^{-x})/x=1\) imply \(x_m\to c_*\). This solution is unique in \((1,2)\) because \(g(x)=x/(1-e^{-x})\) strictly increases from one to infinity. Substituting the convergent optimizing scales into the exact information formulas yields
\[
 I_\lambda(t_\lambda)\to\frac{c_*^2}{e^{c_*}-1},\quad
 I_m(t_m)\to\frac{c_*^2}{4(e^{c_*}-1)}.
\]
The root identity gives \(c_*^2/(e^{c_*}-1)=c_*(2-c_*)\). Division by \(\lambda/3\) and \(m/12\) proves the universal normalized coefficient.

5. **Exact-count contrast.** In the Poisson model, \(\operatorname{Cov}(J,N(t))=\lambda(t-t^2/2)\) and \(\operatorname{Var}(N(t))=\lambda t\). Conditional on \(N(t)\), the expected integral is affine in the count, so the explained variance equals \(\lambda t(1-t/2)^2\), with unique maximum \(8\lambda/27\) at \(t=2/3\). This reproduces the previously established exact-count theorem. In the fixed-count model, \(N(t)\sim\operatorname{Bin}(m,t)\), and conditioning on the count yields explained variance \(mt(1-t)/4\), uniquely maximized as \(m/16\) at \(t=1/2\). Dividing by the respective prior variances completes the comparison.

## Verification

The standalone pure-Python `verify.py` recomputes all scalar information functions from the stated formulas, independently brackets the optimizer equations, checks more than seven thousand supplementary grid comparisons, verifies limiting constants, and draws Poisson and fixed-count arrival paths using separate random simulations to compare empirical covariance-based explained variance against theory. It passes 7,219 checks with a fixed reproducible seed. The continuum optimality and asymptotic statements follow from the preceding analytic proof, not from these finite experiments.

## Relationship to prior work

Cressie (1978), following Samaniego (1976), completely solves optimal placement for the integral of an independent-increment process when its **full value** is observed; the one-count Poisson reference \(t=2/3\) is covered by that result. The present theorem changes the statistical experiment from \(N(t)\) to the saturated bit \(\mathbf1_{\{N(t)>0\}}\), for which the conditional predictor and design criterion are different. The finite-rate transition, fixed-total-count classification, and common inverse-density fraction are the claim, not the earlier count-sampling result. Dokter and collaborators (2017) study event-time observations and missed events; Yoder and collaborators (2017) compare partial-interval event recording with count estimates. Neither inspected accessible material gives the single-bit count-path-integral optimal-design equations. A related binary detection design studied elsewhere also produces the scalar maximizer \(c_*\); the calculus constant itself is **not claimed to be novel**. The distinction is its appearance, with matching normalized information-loss coefficient, in two different stochastic quadrature ensembles.

## Limitations

The Poisson rate or total event count is known; there is no rate learning, false detection, independent dropout, repeated querying, adaptive timing or nonuniform intensity. The result uses one deterministic binary reading and squared-error loss for a single path integral. It does not characterize optimal policies with richer communication or continuous observation. Historical literature coverage is necessarily incomplete: older studies of stochastic-process integration and interval-censored event recording may contain equivalent formulations, so publication priority has not been independently established. The supplied numerical verifier is corroborative, not a proof of analytic statements.

## References

1. Dokter, A. M. et al. (2017). *Analyzing time-ordered event data with missed observations*. Ecology and Evolution 7, 7362–7369. First public online date 2017-08-09. https://doi.org/10.1002/ece3.3281 .
2. Cressie, N. (1978). *Estimation of the integral of a stochastic process*. Bulletin of the Australian Mathematical Society 18, 83–93. https://doi.org/10.1017/S0004972700007838 .
3. Samaniego, F. J. (1976). *The optimal sampling design for estimating the integral of a process with stationary independent increments*. IEEE Transactions on Information Theory 22, 375–376. https://doi.org/10.1109/TIT.1976.1055551 .
4. Yoder, P. J., Ledford, J. R., Harbison, A. L., and Tapp, J. T. (2017). *Partial-Interval Estimation of Count: Uncorrected and Poisson-Corrected Error Levels*. First public online date 2017-12-19. https://doi.org/10.1177/1053815117748407 .
