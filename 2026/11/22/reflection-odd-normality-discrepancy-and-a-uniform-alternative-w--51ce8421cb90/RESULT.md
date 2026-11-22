# Reflection-odd normality discrepancy and a uniform alternative with vanishingly small limiting power

## Finding

Consider the scalar zero-bias normality statistic defined in Kattumannil's normality-test preprint, with the null family \(N(0,\sigma^2)\). Its empirical contrast is identically a *reflection-odd squared-order-statistic contrast*. Consequently its population target vanishes under **every** zero-centered symmetric distribution of finite, positive variance, not only under Gaussian laws. Under a nondegenerate centered symmetric law with finite fourth moment the statistic remains on the null \(n^{-1/2}\) scale and has a centered Gaussian limit, so a conventional two-sided Gaussian-null-calibrated test cannot be consistent against that fixed alternative.

For the particular nonnormal alternative \(F=\operatorname{Unif}(-\sqrt3,\sqrt3)\), the limiting variance of \(\sqrt n\widehat\Delta_n\) is exactly \(1/7\), compared with the standard-Gaussian null variance
\[
\nu_0=\frac14\int_{-\infty}^{\infty}\left[2x\phi(x)+(x^2-1)(2\Phi(x)-1)\right]^2\phi(x)\,dx
=0.4423311143775626914\ldots.
\]
Here \(\phi\) and \(\Phi\) are the standard-normal density and distribution function. Thus the two-sided test that rejects when \(\sqrt n|\widehat\Delta_n|>z_{0.975}\sqrt{\nu_0}\) (or uses asymptotically equivalent exact-normal Monte Carlo cutoffs) has limiting rejection probability
\[
2\Phi\left(-z_{0.975}\sqrt{7\nu_0}\right)
=0.0005630364701048416\ldots,
\]
although its nominal level is \(0.05\). This is an *alternative power*, not the null size.

## Assumptions and scope

Fix \(n\ge2\), and let \(X_1,\ldots,X_n\) be independent, identically distributed real observations. Write \(S_n^2=(n-1)^{-1}\sum_i(X_i-\overline X)^2\); define the statistic when \(S_n^2>0\) by
\[
\widehat\Delta_n=\frac{1}{2S_n^2\binom n2}\sum_{i<j}\{\min(X_i,X_j)^2-X_iX_j\}-\frac12.
\]
This is the uncentered-input, unspecified-positive-variance but *specified-zero-mean* normality statistic of [1, Eq. (4)--(5)], not a claim about a separate recentered or empirical-likelihood procedure. For the general population identity assume \(0<\sigma^2=\operatorname{Var}(X)<\infty\). For the central limit theorem assume \(\mathbb E|X|^4<\infty\), \(\mathbb EX=0\), and central symmetry \(X\overset d=-X\). The explicit uniform and normal cases are continuous and satisfy all these hypotheses.

Set \(g(x,y)=(x+y)|x-y|\), \(g_F(x)=\mathbb E[g(x,Y)]\), where \(Y\) is an independent copy of \(X\), and \(\nu_F=\operatorname{Var}(g_F(X))/(4\sigma^4)\). The claimed normal limit permits the degenerate case \(\nu_F=0\); the explicit uniform case has \(\nu_F>0\).

## Proof

**1. Exact identity and parity.** For all real \(x,y\),
\[
\min(x,y)^2-xy=\tfrac12\big[(x-y)^2-(x+y)|x-y|\big].
\]
The elementary identity \(\sum_{i<j}(X_i-X_j)^2=n(n-1)S_n^2\) therefore gives
\[
\widehat\Delta_n=-\frac{1}{4S_n^2\binom n2}\sum_{i<j}g(X_i,X_j)
=-\frac{1}{2n(n-1)S_n^2}\sum_{j=1}^n(2j-n-1)X_{(j)}^2.
\]
The last equality follows by sorting and using \(g(X_{(i)},X_{(j)})=X_{(j)}^2-X_{(i)}^2\) for \(i<j\). The denominator is unchanged by global sign reversal and \(g(-x,-y)=-g(x,y)\), so
\[
\widehat\Delta_n(-X_1,\ldots,-X_n)=-\widehat\Delta_n(X_1,\ldots,X_n)
\]
for every nonconstant data vector. In particular its finite-sample law under any symmetric parent distribution is symmetric about zero, regardless of normality.

**2. Population blindness.** With independent copies \(X,Y\), the published population target is
\[
\Delta(F)=\frac{\mathbb E[\min(X,Y)^2-XY]}{2\sigma^2}-\frac12
=-\frac{\mathbb E[(X+Y)|X-Y|]}{4\sigma^2}.
\]
The second equality uses \(\mathbb E(X-Y)^2=2\sigma^2\). Under \((X,Y)\overset d=(-X,-Y)\), the numerator is its own negative and hence zero. This covers all zero-centered symmetric laws with finite positive variance, including many nonnormal distributions.

**3. Limiting statistic.** Under the stated fourth-moment hypothesis, \(g(X,Y)\) is square integrable because \(|g(X,Y)|\le(|X|+|Y|)^2\). The order-two Hoeffding projection for \(U_{g,n}=\binom n2^{-1}\sum_{i<j}g(X_i,X_j)\), whose expectation is zero, yields
\[
\sqrt n U_{g,n}=\frac{2}{\sqrt n}\sum_{i=1}^n g_F(X_i)+o_{\Pr}(1).
\]
As \(S_n^2\to\sigma^2\) in probability, the ordinary central limit theorem and Slutsky's theorem give
\[
\sqrt n\widehat\Delta_n\ \Longrightarrow\ N(0,\nu_F),\qquad
\nu_F=\frac{\mathbb E[g_F(X)^2]}{4\sigma^4}.
\]
When \(\nu_F=0\), convergence is to the point mass at zero. Thus for every fixed symmetric law with finite fourth moment, a correctly Gaussian-null-calibrated two-sided test with a strictly positive asymptotic cutoff has limiting rejection probability less than one.

**4. Uniform and normal calculations.** Scaling every observation by a positive constant leaves \(\widehat\Delta_n\) unchanged. Work with \(X\sim\operatorname{Unif}(-1,1)\). Directly splitting the \(Y\)-integral at \(x\) gives
\[
g_F(x)=\frac12\int_{-1}^1(x+y)|x-y|\,dy=\frac{2x^3}{3}\quad(-1\le x\le1).
\]
As \(\sigma^2=1/3\) and \(\mathbb E X^6=1/7\), this yields \(\nu_F=1/7\). Under the standard Gaussian null, the folded-normal identities
\[
\mathbb E|x-Y|=2\phi(x)+x(2\Phi(x)-1),\quad
\mathbb E[(x-Y)|x-Y|]=(x^2+1)(2\Phi(x)-1)+2x\phi(x)
\]
show that
\[
g_0(x)=2x\phi(x)+(x^2-1)(2\Phi(x)-1).
\]
The integral in the finding is exactly \(\operatorname{Var}(g_0(X))/4\) for \(X\sim N(0,1)\), positive and finite. Its numerical value and resulting Gaussian-tail probability follow from high-precision one-dimensional quadrature, not from an unproved closed form. Because the null limit is continuous, exact-null two-sided quantiles normalized by \(\sqrt n\) converge to the same Gaussian cutoff. The uniform alternative limit therefore has the displayed rejection probability.

## Verification

The standalone `CHECK.py` uses rational arithmetic to check the exact order-statistic identity, sign reversal and scale behavior across all nonconstant short integer vectors from specified finite alphabets. It checks the uniform projection and variance identities with exact fractions, independently integrates the normal conditional projection, and recomputes the null variance and limiting rejection probability using high-precision quadrature. A local execution completed 18,443 assertions and gave \(\nu_0=0.44233111437756269142232991582315\ldots\) and rejection probability \(0.000563036470104841576242212393706\ldots\). The proof above, not the finite checker or quadrature, establishes the infinite-sample claims.

## Relationship to prior work

The scalar signed statistic and its claimed general alternative-discrimination motivation appear in Kattumannil [1], whose first public preprint was submitted January 22, 2020. The exact odd representation, symmetric nonnormal blind class, and calculated uniform alternative limit are not stated in the inspected version [1, Sec. 2]. The earlier Betsch--Ebner tests [2] use *squared* \(L^2\) distances of zero-bias transforms and are different statistics: their omnibus conclusions do not transfer to the signed scalar integral. General U-statistic limit theory supplies the projection method, not the kernel-specific parity or variance comparison. No claim is made that an underlying algebraic identity is independent of classical U-statistic or order-statistic theory.

## Limitations

This concerns the stated signed scalar statistic for testing zero-mean Gaussian laws; it does not invalidate the original pointwise Stein characterization or the nonnegative squared-distance procedures. The explicit numeric power uses a standard-normal-null, two-sided asymptotic calibration. A separately recentered sample, an empirical-likelihood construction, or a different rejection rule requires its own limiting-variance analysis. Numerical quadrature is used for the Gaussian constant; no explicit elementary closed form is claimed. Historical-priority uncertainty remains, especially for older signed-dispersion and L-statistic literature. No independent external mathematical audit has occurred.

## References

[1] S. K. Kattumannil, *A new goodness of fit test for normal distribution based on Stein's characterization*, arXiv:2001.07932, first submitted 2020-01-22; revised version 4 (2023-11-13), Sec. 2, Eqs. (4)--(5). https://arxiv.org/html/2001.07932v4

[2] S. Betsch and B. Ebner, *Testing normality via a distributional fixed point property in the Stein characterization*, arXiv:1803.07069 (2018), later TEST 29 (2020), 105--138. https://arxiv.org/abs/1803.07069

[3] Standard order-two U-statistic projection central limit theorem; see A. J. Lee, *U-Statistics: Theory and Practice* (1990), cited in [1].
