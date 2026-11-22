# A discontinuous calibration threshold for two common-offset Brownian quadrature samples

## Finding
Let \(B\) be standard Brownian motion on \([0,1]\), and let \(Z\sim N(0,\eta)\), independent of \(B\), where \(0\leq\eta<\infty\). To estimate \(J=\int_0^1 B_u\,du\), choose exactly two deterministic times \(0\leq s\leq t\leq1\) and observe \(Y_s=B_s+Z\) and \(Y_t=B_t+Z\). The **same** offset \(Z\) contaminates both measurements; there is no independent per-observation error. The estimator may be any measurable function of the observed pair, and performance is unconditional mean-square error.

Define
\[
\eta_* = \frac{7\sqrt{105}-69}{64}=0.04263524002683107\ldots,
\qquad s_* = \frac{15-\sqrt{105}}{10}=0.4753049234040402\ldots,
\]
and for each \(\eta\geq0\) define
\[
s_+(\eta)=\frac{2-8\eta+\sqrt{(8\eta-2)^2+160\eta}}{10}.
\]
All globally minimum-risk designs, modulo exchange of the two observations, are exactly:

- When \(0\leq\eta<\eta_*\), the unique ordered design is \(s=s_+(\eta)\), \(t=(s+2)/3\).
- When \(\eta=\eta_*\), there are exactly two ordered designs: \((s,t)=(0,2/3)\) and \((s,t)=(s_*,(s_*+2)/3)\).
- When \(\eta>\eta_*\), the unique ordered design is \((s,t)=(0,2/3)\).

Thus the first optimal time jumps discontinuously from \(s_*\) to zero at a **sharp nonzero common-offset variance**. In the high-noise regime the first observation calibrates the common offset, and differencing gives the noiseless value \(B_{2/3}\). The optimal Bayes risk is
\[
R_*(\eta)=\frac13-\max\left\{\frac8{27},\,
\frac{s_+(\eta)^2(1-s_+(\eta)/2)^2}{s_+(\eta)+\eta}
+\frac8{27}(1-s_+(\eta))^3\right\}.
\]
At \(\eta=0\), the design is \((2/5,4/5)\) and the risk is \(1/75\); for every \(\eta\geq\eta_*\), the exact minimum risk is \(1/27\).

## Assumptions and scope
Standard Brownian motion has \(B_0=0\), independent increments, and \(\operatorname{Cov}(B_u,B_v)=\min\{u,v\}\). The time interval and process variance rate are normalized to one. The error \(Z\) is a **single random constant** shared without alteration by the two readings; its variance \(\eta\) is known. The sampling times are chosen nonadaptively from the closed interval, and the target is the *path integral* \(J\), not mean integrated reconstruction error of the state trajectory. The random offset need not be Gaussian for the linear-predictor risk identity, but Gaussianity here ensures that this predictor is the full Bayes conditional expectation. Singular measurements at \(s=0,\eta=0\) are interpreted directly, not through an inverse of a singular covariance matrix.

## Proof
First, stochastic Fubini gives \(J=\int_0^1(1-u)\,dB_u\), so \(\operatorname{Var}(J)=1/3\) and
\[
c(v):=\operatorname{Cov}(J,B_v)=v-v^2/2.
\]
For \(s<t\), transform the two data into \(U=Y_s=B_s+Z\) and \(D=Y_t-Y_s=B_t-B_s\). These are independent centered Gaussian variables with variances \(s+\eta\) and \(t-s\). Their covariances with \(J\) are \(c(s)\) and \(c(t)-c(s)\). Orthogonal Gaussian projection therefore yields captured variance
\[
F_\eta(s,t)=\operatorname{Var}(\mathbb E[J\mid Y_s,Y_t])
=\frac{s^2(1-s/2)^2}{s+\eta}
+(t-s)\left(1-\frac{s+t}{2}\right)^2.
\]
The fraction containing \(s+\eta\) is continuously set to zero when \(s=\eta=0\). At coincident times \(s=t\), the second term is zero; the same expression holds by continuity. The mean-square Bayes risk is \(1/3-F_\eta(s,t)\).

Fix \(s\in[0,1)\) and put \(d=t-s\in[0,1-s]\). The only \(d\)-dependent term is \(d(1-s-d/2)^2\), whose derivative is
\[
\left(1-s-\frac d2\right)\left(1-s-\frac{3d}{2}\right).
\]
It increases strictly to \(d=2(1-s)/3\) and then decreases strictly. Consequently the unique maximizing second time is \(t=(s+2)/3\), and the reduced objective is
\[
h_\eta(s)=\frac{s^2(1-s/2)^2}{s+\eta}+\frac8{27}(1-s)^3,
\quad 0\leq s\leq1.
\]
The endpoint \(s=1\) is dominated by the design at \(s=0\). For \(s>0\), direct differentiation factors as
\[
h'_\eta(s)=-\frac{\bigl[s^2+(2+4\eta)s-4\eta\bigr]
\bigl[5s^2+(8\eta-2)s-8\eta\bigr]}{36(s+\eta)^2}.
\]
When \(\eta>0\), each bracket has exactly one root in \((0,1)\), respectively \(r_1\) and \(r_2=s_+(\eta)\). At the first root, the second bracket equals \(3r_1(r_1-2)<0\), hence \(r_1<r_2\). The derivative has signs negative, positive, negative on the successive intervals. Thus the global maximum occurs **only** at \(s=0\) or at \(s=r_2\). For \(\eta=0\), \(h'_0(s)=-(s+2)(5s-2)/36\) for \(s>0\), so the sole maximum is \(s=2/5=r_2\).

The comparison with the boundary design is governed by an exact factorization, valid for \(s>0\):
\[
h_\eta(s)-\frac8{27}
=\frac{s}{108(s+\eta)}
\left[s(12-12s-5s^2)-32\eta(s^2-3s+3)\right].
\]
Since \(s^2-3s+3>0\), an interior point strictly beats calibration exactly when \(\eta<H(s)\), where
\[
H(s)=\frac{s(12-12s-5s^2)}{32(s^2-3s+3)},\qquad
H'(s)=-\frac{(s^2-3s-6)(5s^2-15s+6)}{32(s^2-3s+3)^2}.
\]
On \([0,1]\) the first factor in the numerator of \(H'\) is negative, so \(H\) strictly increases until its unique stationary point \(s_*=(15-\sqrt{105})/10\), then strictly decreases. Its unique maximum is \(H(s_*)=(7\sqrt{105}-69)/64=\eta_*\). Therefore an interior point beats the calibration design if and only if \(\eta<\eta_*\). At equality the only interior tying point is \(s=s_*\); differentiation then identifies it with \(s_+(\eta_*)\). The candidate maxima and the strict inequalities above yield the complete classification, including uniqueness and the two-way tie. The risk expressions follow by subtracting the captured variance from \(1/3\).

## Verification
The standalone file `verify.py` checks the Gaussian conditioning formula two independent ways (direct covariance-matrix inversion and independent-increment decomposition), symbolically factors both optimization derivatives and the exact risk comparison, verifies the algebraic critical variance, and compares 7,000 off-optimal random designs against the claimed global optimum. It passed using `numpy` and `sympy`. The maximum numerical discrepancy in the covariance identity was \(3.06\times10^{-16}\); no randomly tested design exceeded the proved optimum. These finite checks support but do not replace the all-parameter proof above. Run with `python verify.py` after installing `requirements.txt`.

## Relationship to prior work
Aksenov, Amblard, Michel, and Jutten's 2017 study of optimal measurement times for Brownian Kalman filtering uses **time-aggregated state-estimation uncertainty**, rather than the single Brownian path-integral target and perfectly shared random offset analyzed here. Their 2019 continuation treats one and two measurement times in the Kalman setting. Attia and Constantinescu's 2020/2022 correlated-noise Bayesian experimental-design framework supplies general goal-oriented covariance design and numerical PDE-based sensor placement, but not this closed-form, rank-one common-calibration error phase transition. Earlier noiseless Wiener quadrature theory already gives the \((2/5,4/5)\) endpoint case and is not asserted as new. The new assertion is the full sharp positive-noise classification and discontinuous calibration-versus-interior transition.

## Limitations
This theorem does not cover independent per-reading error, imperfectly correlated errors, sensor costs, unknown Brownian variance rate, general kernels, sequential choice of observation times, or more than two measurements. Perfectly shared error permits exact cancellation by differencing and explains the noise-insensitive boundary risk. The publication-priority comparison is based on the accessible primary texts and search results listed below; a full-text copy of the 2019 two-measure continuation was not obtained, leaving a residual possibility of historical overlap. The result has not received independent mathematical review.

## References
- A. Aksenov, P.-O. Amblard, O. Michel, C. Jutten, *Optimal Measurement Times for Observing a Brownian Motion over a Finite Period Using a Kalman Filter* (2017), HAL hal-01479301, submitted 2017-02-28, DOI: 10.1007/978-3-319-53547-0_48. https://hal.science/hal-01479301
- A. Aksenov, P.-O. Amblard, O. Michel, C. Jutten, *Optimal Measurement Times for a Small Number of Measures of a Brownian Motion over a Finite Period* (first preprint 2019-02-16), arXiv:1902.06126. https://arxiv.org/abs/1902.06126
- A. Attia, E. Constantinescu, *Optimal Experimental Design for Inverse Problems in the Presence of Observation Correlations* (first preprint 2020-07-28), arXiv:2007.14476, SIAM Journal on Scientific Computing 44 (2022), A2808–A2842. https://arxiv.org/abs/2007.14476
