# Exact gamma calibration and a common error exponent for inverse-Weibull lower-record discrimination

## Finding

Consider the inverse-Weibull family
\[
 F_{\beta,\lambda}(x)=\exp(-\lambda x^{-\beta}),\qquad x>0,\quad \beta,\lambda>0.
\]
Fix two candidate shape parameters \(0<\beta_1<\beta_2\), allowing the nuisance parameter \(\lambda\) to be fitted **separately** under the two candidate models. For the first \(m\ge2\) successive strict lower records \(R_1>\cdots>R_m>0\), let \(\Lambda_m\) be the maximum likelihood under \(\beta_2\) divided by that under \(\beta_1\). Write
\[
 q=\frac{\beta_2}{\beta_1}>1,\quad
 c=\frac{\log q}{q-1}<1,\quad d=qc>1,
 \quad I(t)=t-1-\log t.
\]

**Theorem (finite-sample calibration and sharp equal-rate law).** Under a true model with shape \(\beta\in\{\beta_1,\beta_2\}\) and any \(\lambda>0\),
\[
 \log\Lambda_m=m\log q-\frac{\beta_2-\beta_1}{\beta}G_{m-1},
 \qquad G_{m-1}\sim\operatorname{Gamma}(m-1,1).
\]
Here the second Gamma parameter is the *rate*, and the equality is in distribution. Consequently the maximum-profile-likelihood selection rule (choose \(\beta_2\) iff \(\Lambda_m>1\)) has **exact correct-selection probabilities**
\[
 \Pr_{\beta_1}(\text{select }\beta_1)
 =e^{-mc}\sum_{j=0}^{m-2}\frac{(mc)^j}{j!},
 \qquad
 \Pr_{\beta_2}(\text{select }\beta_2)
 =1-e^{-md}\sum_{j=0}^{m-2}\frac{(md)^j}{j!}.
\]
Both are independent of the unknown scale. The respective errors have the **same strictly positive large-deviation exponent** \(J(q)=I(c)=I(d)\), and in fact
\[
 \begin{aligned}
 \Pr_{\beta_1}(\text{select }\beta_2)
 &\sim \frac{e^{-mJ(q)}}{c(1-c)\sqrt{2\pi m}},\\
 \Pr_{\beta_2}(\text{select }\beta_1)
 &\sim \frac{e^{-mJ(q)}}{d(d-1)\sqrt{2\pi m}}.
 \end{aligned}
\]
The equivalence is for fixed \(q>1\) as the number \(m\) of records tends to infinity.

For the inverse exponential versus inverse Rayleigh models \((\beta_1,\beta_2)=(1,2)\), the common error exponent is
\[
 J(2)=\log2-1-\log(\log2)=0.0596601011416\ldots.
\]
For \(m=7\), the two exact correct-selection probabilities are respectively \(0.641905293\ldots\) and \(0.920856168\ldots\); for \(m=11\), they are \(0.761972910\ldots\) and \(0.937830787\ldots\).

## Assumptions and scope

The observation stream is independent and identically distributed from a continuous inverse-Weibull law. The sample consists of the first \(m\ge2\) distinct lower *record values*, not a fixed number of ordinary observations, and is followed until the \(m\)-th record occurs. The true shape is one of the two prespecified positive shapes, while the scale is an arbitrary positive unknown parameter, independently profiled in both candidate models. All formulas refer to this lower-record likelihood; no statement about the corresponding upper-record likelihood is made. The threshold is one, with no likelihood penalties or unequal prior model weights.

## Proof

**1. Exact profile likelihood.** The density is \(f_{\beta,\lambda}(x)=\beta\lambda x^{-\beta-1}e^{-\lambda x^{-\beta}}\). The joint likelihood of successive strict lower records is
\[
 L_{\beta,\lambda}(r_1,\ldots,r_m)
 =f_{\beta,\lambda}(r_m)\prod_{i=1}^{m-1}\frac{f_{\beta,\lambda}(r_i)}{F_{\beta,\lambda}(r_i)}
 =(\beta\lambda)^m\left(\prod_{i=1}^m r_i^{-\beta-1}\right)
 e^{-\lambda r_m^{-\beta}}.
\]
Its log likelihood is strictly concave as a function of \(\log\lambda\) and is maximized uniquely at \(\widehat\lambda_{\beta}=mr_m^\beta\). Substitution gives
\[
 \widehat L_{\beta}=(m\beta)^m e^{-m}r_m^{m\beta}
 \prod_{i=1}^m r_i^{-\beta-1}.
\]
Thus, without any large-sample approximation,
\[
 \boxed{\Lambda_m=q^m\prod_{i=1}^{m-1}
 \left(\frac{r_m}{r_i}\right)^{\beta_2-\beta_1}.}
\]

**2. Gamma pivot.** Under the true \((\beta,\lambda)\), the decreasing records \(R_i\) transform to the increasing records \(Y_i=\lambda R_i^{-\beta}\) of standard exponential observations. The joint density of their first \(m\) upper record values is \(e^{-y_m}\) on \(0<y_1<\cdots<y_m\). Therefore, given \(Y_m=t\), the earlier \(m-1\) values have the distribution of ordered independent \(\operatorname{Uniform}(0,t)\) variables. Since summation ignores ordering,
\[
 \beta\sum_{i=1}^{m-1}\log\frac{R_i}{R_m}
 =\sum_{i=1}^{m-1}\log\frac{Y_m}{Y_i}
 \stackrel{d}{=}\sum_{i=1}^{m-1}(-\log U_i)
 \sim\operatorname{Gamma}(m-1,1).
\]
The conditional distribution does not depend on \(t\), and neither \(\lambda\) nor the record stopping times enter the pivot. Inserting this identity in the boxed likelihood ratio proves its asserted law.

**3. Exact classification probabilities.** The rule \(\Lambda_m>1\) is equivalent under true shape \(\beta\) to \(G_{m-1}<m\beta\log q/(\beta_2-\beta_1)\). The threshold is \(mc\) for \(\beta=\beta_1\), and \(md\) for \(\beta=\beta_2\). Since for integer \(k\ge1\),
\[
 \Pr\{\operatorname{Gamma}(k,1)\ge x\}=e^{-x}\sum_{j=0}^{k-1}\frac{x^j}{j!},
\]
the two stated finite-sample expressions follow. Equalities at the threshold have probability zero.

**4. Matching sharp error rates.** Elementary logarithm inequalities yield \(0<c<1<d\). For fixed \(0<a<1\), the Gamma/Poisson identity and Stirling's formula give
\[
 \Pr\{G_{m-1}\le ma\}
 =\Pr\{\operatorname{Poisson}(ma)\ge m-1\}
 \sim\frac{e^{-mI(a)}}{a(1-a)\sqrt{2\pi m}}.
\]
Indeed the first included Poisson mass has the stated exponential rate and prefactor \(1/[a\sqrt{2\pi m}]\), and its succeeding mass ratios converge to \(a\). For fixed \(a>1\), the reverse Poisson lower tail similarly gives
\[
 \Pr\{G_{m-1}\ge ma\}
 =\Pr\{\operatorname{Poisson}(ma)\le m-2\}
 \sim\frac{e^{-mI(a)}}{a(a-1)\sqrt{2\pi m}}.
\]
Here the last included Poisson mass has prefactor \(1/[a^2\sqrt{2\pi m}]\), and the preceding mass ratios converge to \(1/a\). Finally,
\[
 I(d)-I(c)=(q-1)c-\log q=0.
\]
This proves the equal exponential rate and both distinct prefactors. No asymptotic statements are inferred from finite simulations.

## Verification

Run `python verify.py` in the same directory. The standalone checker performs exact rational profile-likelihood identities across multiple record lengths and shape pairs, seeded exponential-record tests of the exact pivot, finite Gamma-calibration comparisons, and the common-rate identity. It reports 450,965 supporting assertions and the displayed \(m=7\) and \(m=11\) probabilities. The probabilistic and asymptotic theorems are proved above; computational checks are diagnostic, not infinite proofs.

## Relationship to prior work

Tripathi, Singh and Singh (2022), *Model Discrimination Based on Record Values*, introduced the inverse-Rayleigh/inverted-exponential lower-record profile-likelihood comparison, supplied model-specific scale MLEs, and estimated correct-selection probabilities using Monte Carlo (their Table III). Their printed simplification in Equation (20), \(4r_m\prod_{i<m}r_i^{-1}\), agrees with the algebraically correct profiled ratio only when \(m=2\); the ratio implied by Equations (7), (8), (12), (14), and (19) is \(2^m r_m^{m-1}\prod_{i<m}r_i^{-1}\). The original simulated Table III is numerically close to the exact Gamma probabilities for \(m=7,\ldots,11\); no inference is made about which expression was implemented by its authors.

Al-Duais (2021) analyzes scale estimation from inverse-Weibull lower records, not the two-model calibration. Classical results on record processes and exponential spacings supply the underlying Poisson-arrival representation. The present theorem connects that representation with the *particular separately profiled model discrimination likelihood*, yielding parameter-free exact operating characteristics and a common sharp large-deviation exponent for **every** fixed pair of inverse-Weibull shapes. It does not claim that the constituent record-process facts are new.

## Limitations

The result concerns only independent observations, the first \(m\) lower records, two fixed shapes, and a freely fitted scale under each model. Upper-record decisions in the source paper are not calibrated here. The integer Gamma shape and common error-rate limit do not imply an optimality assertion across all tests, all priors, or all censoring regimes. The exact date of first public release of the journal issue is not established to a day; a dated public full-text upload on 18 February 2022 establishes an eligible public source date. Original simulation code was not examined. Exhaustive historical-priority review and independent mathematical audit have not been performed.

## References

1. A. Tripathi, U. Singh, S. K. Singh, *Model Discrimination Based on Record Values*, Journal of Scientific Research 66(1) (2022), 411–418. DOI: [10.37398/JSR.2022.660144](https://doi.org/10.37398/JSR.2022.660144). [Open article PDF](https://www.bhu.ac.in/research_pub/jsr/Volumes/JSR_66_01_2022/44.pdf). [Public full-text upload](https://www.researchgate.net/publication/358702209_Model_Discrimination_Based_on_Record_Values).
2. F. S. Al-Duais, *Bayesian Analysis of Record Statistic from the Inverse Weibull Distribution under Balanced Loss Function*, Mathematical Problems in Engineering (2021), 6648462. [DOI: 10.1155/2021/6648462](https://doi.org/10.1155/2021/6648462).
3. R. W. Shorrock, *On record values and record times*, Journal of Applied Probability 9 (1972), 316–326. [DOI: 10.2307/3212801](https://doi.org/10.2307/3212801).
