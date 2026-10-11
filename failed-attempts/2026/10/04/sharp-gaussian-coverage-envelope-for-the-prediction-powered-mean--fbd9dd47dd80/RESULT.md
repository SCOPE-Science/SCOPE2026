# Sharp Gaussian coverage envelope for the prediction-powered mean interval

## Finding

Let \(N,n\ge2\). Let \(A_1,\ldots,A_N\) be iid Gaussian observations with mean \(\mu_A\) and variance \(\sigma_A^2>0\), and let \(B_1,\ldots,B_n\) be an independent iid Gaussian sample with mean \(\mu_B\) and variance \(\sigma_B^2>0\). Define
\[
\theta=\mu_A+\mu_B,\qquad \widehat\theta=\overline A+\overline B,
\]
and let \(S_A^2,S_B^2\) be the unbiased sample variances. For any fixed critical value \(z>0\), consider
\[
I_z=\widehat\theta\pm z\sqrt{\frac{S_A^2}{N}+\frac{S_B^2}{n}}.
\]
Writing
\[
\nu_A=N-1,\qquad \nu_B=n-1,\qquad \nu=N+n-2,\qquad \nu_*=\min(\nu_A,\nu_B),
\]
the exact finite-sample coverage obeys the sharp envelope
\[
2F_{t_{\nu_*}}(z)-1\le \Pr\{\theta\in I_z\}\le 2F_{t_\nu}(z)-1<2\Phi(z)-1.
\]
The upper endpoint is attained exactly when
\[
\frac{\sigma_A^2}{N(N-1)}=\frac{\sigma_B^2}{n(n-1)}.
\]
The lower endpoint is the sharp infimum over strictly positive variance ratios. It is approached by letting the variance contribution associated with the smaller degrees of freedom dominate; if a zero variance is admitted for the other component, the lower endpoint is attained.

For the mean construction in *Prediction-Powered Inference*, take \(A=f(\widetilde X)\) on the unlabeled sample and \(B=Y-f(X)\) on the labeled sample. Then \(\widehat\theta\) is exactly the paper's prediction-powered mean estimator, and the displayed interval is its normal-critical-value interval because \(\operatorname{Var}(B)=\operatorname{Var}(f(X)-Y)\).

At \(n=10\), \(N=100\), and \(z=1.96\), the sharp floor is
\[
2F_{t_9}(1.96)-1=0.9183555945395834,
\]
the attained upper endpoint is
\[
2F_{t_{108}}(1.96)-1=0.9474279305425579,
\]
while the nominal Gaussian target is
\[
2\Phi(1.96)-1=0.9500042097035590.
\]

## Assumptions and scope

The result is finite-sample and exact under two independent Gaussian samples with positive variances. No asymptotic approximation is used in the proof. The predictor in the prediction-powered interpretation is treated as fixed with respect to both samples, matching the setup in the cited source. The finding concerns the normal-critical-value mean interval, not every prediction-powered interval or every non-Gaussian distribution.

The source's mean notation uses the rectifier \(f(X)-Y\) with a minus sign in the estimator. Writing \(B=Y-f(X)\) changes only the sign convention and leaves the variance term unchanged.

## Proof

Put
\[
V_A=\frac{\sigma_A^2}{N},\qquad V_B=\frac{\sigma_B^2}{n},\qquad V=V_A+V_B,\qquad w=\frac{V_A}{V}.
\]
Gaussian independence gives
\[
Z=\frac{\widehat\theta-\theta}{\sqrt V}\sim N(0,1),
\]
and \(Z\) is independent of the two sample variances. Also
\[
\frac{\nu_A S_A^2}{\sigma_A^2}\sim\chi^2_{\nu_A},\qquad
\frac{\nu_B S_B^2}{\sigma_B^2}\sim\chi^2_{\nu_B},
\]
independently. Hence the random estimated-variance ratio is
\[
Q=\frac{S_A^2/N+S_B^2/n}{V}
=w\frac{\chi^2_{\nu_A}}{\nu_A}+(1-w)\frac{\chi^2_{\nu_B}}{\nu_B},
\]
independent of \(Z\). Conditional on \(Q\), the event \(\theta\in I_z\) is \(|Z|\le z\sqrt Q\), so
\[
\Pr\{\theta\in I_z\}=\mathbb E h_z(Q),\qquad
h_z(q)=2\Phi(z\sqrt q)-1.
\]
A direct differentiation gives
\[
h_z''(q)=-\frac{z\phi(z\sqrt q)}{2q^{3/2}}(1+z^2q)<0
\]
for every \(q>0\). Thus \(h_z\) is strictly concave.

For the upper bound, write \(Q=\sum_{j=1}^{\nu} c_jR_j\), where the \(R_j\) are iid \(\chi^2_1\), with \(\nu_A\) coefficients equal to \(w/\nu_A\) and \(\nu_B\) coefficients equal to \((1-w)/\nu_B\). The coefficients are nonnegative and sum to one. Replacing any two coefficients by their average reduces the weighted iid sum in convex order: conditional on the remaining variables, Jensen's inequality applied after swapping the two iid coordinates proves the claim. Iterating pairwise averages shows
\[
\frac{\chi^2_\nu}{\nu}\le_{\rm cx} Q,
\]
because the uniform coefficient vector is obtained by averaging. Concavity of \(h_z\) therefore yields
\[
\mathbb E h_z(Q)\le \mathbb E h_z\!\left(\frac{\chi^2_\nu}{\nu}\right)
=2F_{t_\nu}(z)-1.
\]
Equality requires all coefficients to be equal, because \(h_z\) is strictly concave and the chi-square variables are nondegenerate. Thus
\[
\frac{w}{\nu_A}=\frac{1-w}{\nu_B},
\]
which is equivalent to \(\sigma_A^2/[N(N-1)]=\sigma_B^2/[n(n-1)]\). At that balance point, \(Q=\chi^2_\nu/\nu\) exactly.

For the lower bound, let \(X_k=\chi_k^2/k\). The family decreases in convex order with \(k\). Indeed, \(X_{k+1}\) is the average of the \(k+1\) leave-one-out means of \(k\) iid \(\chi^2_1\) variables; Jensen's inequality followed by exchangeability gives \(X_{k+1}\le_{\rm cx}X_k\). Therefore both \(X_{\nu_A}\) and \(X_{\nu_B}\) are below \(X_{\nu_*}\) in convex order. Convex order is preserved by independent sums, and a convex function evaluated at a weighted average of two iid copies has expectation no larger than at either copy. Consequently
\[
Q\le_{\rm cx}X_{\nu_*}.
\]
Concavity now gives
\[
\mathbb E h_z(Q)\ge \mathbb E h_z(X_{\nu_*})=2F_{t_{\nu_*}}(z)-1.
\]
Letting the variance contribution from the component with \(\nu_*\) degrees of freedom tend to one proves sharpness of the lower bound.

Finally, since \(\chi^2_\nu/\nu\) is nonconstant with mean one and \(h_z\) is strictly concave,
\[
2F_{t_\nu}(z)-1=\mathbb E h_z\!\left(\frac{\chi^2_\nu}{\nu}\right)<h_z(1)=2\Phi(z)-1.
\]

## Verification

The algebraic proof above supplies the infinite-family statement. The accompanying `verify.py` independently recomputes the numerical example using a standard continued-fraction evaluation of the regularized incomplete beta function, then checks the balance relation and the three displayed probabilities. It is a numerical replay of the example, not a substitute for the convex-order proof.

## Relationship to prior work

Angelopoulos, Bates, Fannjiang, Jordan, and Zrnic define the prediction-powered mean estimator and the normal-critical-value interval used here in *Prediction-Powered Inference* (arXiv:2301.09633, Section 1.3). Their displayed interval is motivated by the estimator's decomposition into two independent terms and is not presented there with the sharp finite-Gaussian coverage envelope above.

Richter's 2020 paper on chi-square and Student bridge distributions gives the exact Student-bridge representation for the Behrens--Fisher statistic, including the endpoint Student laws and the balanced case where a weighted chi-square denominator collapses to one chi-square law. Those distributional facts cover important ingredients of the present proof and are not claimed as new. The contribution here is the global sharp ordering of the central coverage probability over every positive nuisance variance ratio, with both extremal values and the exact balance surface, specialized to the prediction-powered mean interval.

Classical Welch--Satterthwaite work approximates the weighted variance denominator by a scaled chi-square law. A published published-finding corpus comparison record, *Laplace-transform gaps and metric lower certificates for Satterthwaite Gamma approximation*, proves a transform-order gap between heterogeneous Gamma sums and their moment-matched Gamma approximation. That result does not give the central-coverage convex-order envelope proved here.

A later non-asymptotic study of prediction-powered inference by Mani, Xu, Lipton, and Oberst analyzes finite-sample bias and variance behavior for adaptive prediction-powered estimators. It does not supply this baseline Gaussian coverage extremum.

## Limitations

The exact envelope relies on Gaussianity, independence of the two samples, unbiased sample variances, and a fixed predictor. It does not assert analogous sharp bounds under arbitrary non-Gaussian laws. The lower endpoint is an infimum when both variances are required to be strictly positive. Older Behrens--Fisher literature is extensive; although the closest full-text bridge paper and targeted searches were checked, an equivalent historical statement of this particular global central-coverage extremum remains a residual originality risk.

## References

1. A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, and T. Zrnic, *Prediction-Powered Inference*, Science 382 (2023), 669--674; arXiv:2301.09633. DOI: 10.1126/science.adi6000.
2. W.-D. Richter, *Chi-Square and Student Bridge Distributions and the Behrens--Fisher Statistic*, Stats 3 (2020), 233--257. DOI: 10.3390/stats3030021.
3. B. L. Welch, *The Generalization of Student's Problem when Several Different Population Variances are Involved*, Biometrika 34 (1947), 28--35. DOI: 10.1093/biomet/34.1-2.28.
4. F. E. Satterthwaite, *An Approximate Distribution of Estimates of Variance Components*, Biometrics Bulletin 2 (1946), 110--114. DOI: 10.2307/3002019.
5. A. Mani, A. Xu, Z. C. Lipton, and M. Oberst, *No Free Lunch: Non-Asymptotic Analysis of Prediction-Powered Inference*, arXiv:2505.20178 (2025).
