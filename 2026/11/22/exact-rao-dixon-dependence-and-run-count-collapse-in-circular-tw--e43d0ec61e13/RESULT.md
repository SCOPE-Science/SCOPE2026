# Exact Rao–Dixon dependence and run-count collapse in circular two-sample spacing tests

## Finding
Let \(m\ge2\) and \(2\le n\le m\). From two labeled circular samples form the \(m\) successive gaps of the first sample and count \(S_j\) second-sample observations in each gap. Define the unhalved Rao discrepancy, the Dixon quadratic statistic, the number of vacant gaps, and the circular number of runs by
\[
R=\sum_{j=1}^{m}|S_j-n/m|,\qquad Q=\sum_{j=1}^{m}S_j^2,\qquad Z=\sum_{j=1}^{m}{\mathbf 1}_{\{S_j=0\}},\qquad C=2\sum_{j=1}^{m}{\mathbf 1}_{\{S_j>0\}}.
\]
**Samplewise collapse:** independently of any sampling distribution, for every tie-free observed configuration with \(2\le n\le m\),
\[
R=\frac{2n}{m}Z=2n-\frac nm C.
\]
Consequently, upper-tail Rao tests and lower-tail circular Wald–Wolfowitz run tests induce exactly the same rejection ordering at every level in this sample-size regime. This is an equivalence of the recorded statistics, not an assertion about the separate power of Dixon's statistic.

Under the common-continuous-distribution two-sample null, their finite covariance and squared correlation are
\[
\operatorname{Cov}(R,Q)=\frac{4n^2(m-1)(n-1)}{m(m+1)(m+n-1)},\qquad
\operatorname{Corr}(R,Q)^2=\frac{(m+2)(m+3)(m+n-2)}{m(m+n)(m+n+1)}.
\]
Both variances are nonzero for the stated parameters and the correlation is positive. It equals one exactly when \(n=2\); for \(3\le n\le m\), it is strictly less than one. Along any sequence with \(m,n\to\infty\) and \(n/m\to\theta\in(0,1]\), the squared correlation tends to \(1/(1+\theta)\). Thus nearly one-to-one dependence when the second sample is relatively sparse contrasts with a nontrivial residual at balance.

For balanced samples \(m=n=s\ge2\), the squared correlation is
\[
\rho_s^2=\frac{(s-1)(s+2)(s+3)}{s^2(2s+1)}.
\]
It decreases strictly from one at \(s=2\) to \(1/2\) as \(s\to\infty\). Hence Dixon's fraction of variance unexplained by optimal *linear* prediction using Rao rises strictly from zero to \(1/2\). At balance \(R=2Z\), with the exact law
\[
\Pr\{R=2z\}=\frac{\binom{s}{z}\binom{s-1}{z}}{\binom{2s-1}{s-1}},\qquad z=0,\ldots,s-1.
\]

## Assumptions and scope
The first sample consists of \(m\) independent points and the second of \(n\) independent points on an oriented circle. Under the null all observations have the same atomless law; values need not be uniform, and no parametric form is needed. By tie-free circular order, exactly \(m\) gaps exist and \(\sum_j S_j=n\). Samplewise identities hold for every configuration with no coincident points, even under alternatives. The laws, variances, covariances and correlations assume the common-distribution null. The Dixon centered-square statistic \(\sum_j(S_j-n/m)^2\) differs from \(Q\) only by the deterministic value \(n^2/m\), so all covariances and correlations are identical. The unhalved \(R\) follows the normalization of the 2021 study; the 2015 chapter uses half this value. Parameters \(n=1\) are excluded from correlation formulas because both relevant statistics are deterministic.

## Proof
**Circular rank representation.** Under the common continuous null, all pooled label sequences are equiprobable. Anchor one of the first-sample labels and read clockwise. Each weak composition \((S_1,\ldots,S_m)\) of \(n\) into \(m\) parts has the same probability \(\binom{m+n-1}{m-1}^{-1}\). This is the uniform/Bose–Einstein composition law, not the independent multinomial occupancy law.

**Deterministic identity.** Put \(a=n/m\le1\). Every positive integer part is at least \(a\); a zero part contributes \(a\) to \(|S_j-a|\). Thus \(R=\sum_{S_j>0}(S_j-a)+aZ=n-a(m-Z)+aZ=2aZ\). The number of nonempty second-sample runs is \(m-Z\) and the alternating circular label string has twice that number of total runs, giving \(C=2(m-Z)\) and the asserted affine equivalence.

**Finite second moments.** For the uniform-composition law, write \(x_{\underline r}\) and \(x^{\overline r}\) for falling and rising factorials. The factorial moments are
\[
\mathbb E[(S_1)_{\underline r}]=\frac{n_{\underline r}\,r!}{m^{\overline r}},\qquad
\mathbb E[(S_1)_{\underline r}(S_2)_{\underline t}]=\frac{n_{\underline{r+t}}\,r!t!}{m^{\overline{r+t}}}.
\]
Consequently, \(\mathbb EZ=m(m-1)/(m+n-1)\) and
\[
\operatorname{Var}(Z)=\frac{mn(m-1)(n-1)}{(m+n-2)(m+n-1)^2}.
\]
Since \(Q=n+\sum_j (S_j)_{\underline2}\) and
\((x)_{\underline2}^{2}=(x)_{\underline4}+4(x)_{\underline3}+2(x)_{\underline2}\), the displayed factorial moments yield
\[
\operatorname{Var}(Q)=\frac{4n(m-1)(m+n)(n-1)(m+n+1)}{(m+1)^2(m+2)(m+3)}.
\]
Conditioning on \(S_1=0\) leaves a uniform weak composition into \(m-1\) parts and gives
\[
\mathbb E[Q\mid S_1=0]=n+\frac{2n(n-1)}m,\quad
\mathbb EQ=n+\frac{2n(n-1)}{m+1}.
\]
Therefore
\[
\operatorname{Cov}(Z,Q)=m\Pr(S_1=0)\big(\mathbb E[Q\mid S_1=0]-\mathbb EQ\big)
=\frac{2n(m-1)(n-1)}{(m+1)(m+n-1)}.
\]
Substituting \(R=2nZ/m\) into these three identities proves both displayed exact formulas. The squared correlation equals one only if \(n=2\): the difference between its positive denominator and numerator factors as \((n-2)(m^2+mn-2m-6)\), which is positive for \(3\le n\le m\).

**Balanced limit and strict decrease.** Setting \(m=n=s\) gives the rational formula. Its consecutive difference is
\[
\rho_{s+1}^2-\rho_s^2=
-\frac{(s+3)(7s^3-3s^2-13s-6)}{s^2(s+1)^2(2s+1)(2s+3)}<0\qquad(s\ge2).
\]
The cubic is positive at \(s=2\) and strictly increasing thereafter. Taking the leading polynomial coefficients gives \(\lim_{s\to\infty}\rho_s^2=1/2\), and the general fixed-ratio limit follows by the same algebra. Lastly, to realize precisely \(z\) vacant cells at balance, select their positions in \(\binom{s}{z}\) ways and distribute \(s\) units positively into the remaining \(s-z\) cells in \(\binom{s-1}{z}\) ways. Dividing by the total number of weak compositions establishes the law.

## Verification
The included standalone `check.py` enumerates every weak composition for all \(2\le m,n\le7\) using exact rational arithmetic, independently computing the sample means and covariance matrix. It verifies the three second-moment formulas, every samplewise Rao–runs identity for \(n\le m\), the complete vacancy law, the rational squared-correlation formula, and balanced strict decrease through \(s=29\). Replay: `python3 check.py`; observed result: `PASS: 9560 exact-rational assertions`. Enumeration is a cross-check only; the all-parameter proof is the preceding algebra.

## Relationship to prior work
Gatto and Jammalamadaka (2015, Sections 6.2–6.3) introduce the circular spacing-frequency formulation and discuss Dixon, circular runs and half-normalized Rao tests, including a general conditional-geometric representation. Jammalamadaka, Guerrier and Mangalam (2021, Sections 2–4) give exact *univariate* null distributions and critical-value comparisons for the Rao and Dixon tests and their separate marginal Gaussian approximations. Holst and Rao (1980) supply general asymptotic machinery. The full uniform-composition law and individual test definitions are prior results. The present contribution is the explicit shared finite covariance and correlation function, its strict balanced monotonicity, the statistical identification of the Rao/runs redundancy throughout \(n\le m\), and the quantified residual variance in their Dixon comparison. These facts are not established by the named marginal calibration theorems alone.

## Limitations
No claim is made that the individual test statistics, uniform-composition distribution, separate Gaussian limits, or general Dirichlet–multinomial moment tools are new. The exact dependence formula here is restricted to \(2\le n\le m\); outside this range the Rao statistic is no longer simply proportional to vacancy count. The \(1-\rho^2\) quantity concerns optimal *linear* prediction of Dixon from Rao, not conditional independence, incremental hypothesis-testing power, or a critical-value formula for a combined test. Historical priority under alternative terminology may exist.

## References
- S. Rao Jammalamadaka, S. Guerrier and V. Mangalam (2021), “A Two-sample Nonparametric Test for Circular Data– its Exact Distribution and Performance,” *Sankhya B* 83, 140–166, first published 2021-02-13, https://doi.org/10.1007/s13571-020-00244-9.
- R. Gatto and S. Rao Jammalamadaka (2015), “On two-sample tests for circular data based on spacing-frequencies,” in *Geometry Driven Statistics*, Chapter 6, first published 2015-09-03, https://doi.org/10.1002/9781118866641.ch6.
- L. Holst and J. S. Rao (1980), “Asymptotic theory for some families of two-sample nonparametric statistics,” *Sankhya Series A* 42, 19–52, https://www.jstor.org/stable/25050211.
