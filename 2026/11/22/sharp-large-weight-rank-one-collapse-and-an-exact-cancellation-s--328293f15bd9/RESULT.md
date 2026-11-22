# Sharp large-weight rank-one collapse and an exact cancellation stratum in inverse-Gaussian CDF–Stein testing

## Finding

The maximum-likelihood fitted inverse-Gaussian CDF–Stein goodness-of-fit statistic of Allison, Betsch, Ebner and Visagie [1,2] has a sharp two-regime large-weight law, for both of the paper's exponential weights. The generic regime has polynomial order; its exact cancellation stratum instead has an endpoint-controlled exponential order. For three observations, cancellation occurs **if and only if one observation equals the sample mean**. In a subsequent sample-size limit under the inverse-Gaussian null, the rescaled generic statistic has an explicit one-degree-of-freedom chi-square law.

For every fixed nonconstant positive sample of size \(n\ge2\), let \(y_i=x_i/\overline x\), \(u=n^{-1}\sum_i y_i^{-1}\), \(v=n^{-1}\sum_i y_i^{-2}\), and
\[
\widehat\phi=(u-1)^{-1},\quad
b_i=\frac12\left(\widehat\phi+\frac3{y_i}-\frac{\widehat\phi}{y_i^2}\right),\quad
B=\frac1n\sum_i b_i=\frac12\left(3u+\frac{1-v}{u-1}\right).
\]
Define \(m=\min_i y_i\) and let \(r\) be the number of observations equal to \(m\). The two tests \(T_{n,a}\) and \(\widetilde T_{n,a}\) are defined below. If \(B\ne0\), as \(a\to\infty\) at **fixed sample**, then
\[
T_{n,a}=\frac{2n B^2}{a^3}+O_x(a^{-1}e^{-am}),\qquad
\widetilde T_{n,a}=\frac{n\sqrt\pi B^2}{4a^{3/2}}+O_x(a^{-1}e^{-am^2}).
\]
If \(B=0\), both polynomial leading terms cancel and the sharp replacements are
\[
T_{n,a}\sim \frac{r^2}{na}e^{-am},\qquad
\widetilde T_{n,a}\sim\frac{r^2}{2nam}e^{-am^2}.
\]
For \(n=3\), the exact identity
\[
B=\frac{\prod_{i=1}^3(y_i-1)}{2(u-1)\prod_{i=1}^3y_i}
\]
shows that \(B=0\) exactly when at least one observation equals \(\overline x\), since the nonconstant sample has \(u>1\). For example \((x_1,x_2,x_3)=(1/2,1,3/2)\) has \(m=1/2\), \(r=1\) and
\[
T_{3,a}\sim\frac{e^{-a/2}}{3a},\qquad
\widetilde T_{3,a}\sim\frac{e^{-a/4}}{3a}.
\]
For \(n=2\), setting \((y_1,y_2)=(1-q,1+q)\) with \(0<|q|<1\), one has \(B=q^2/[2(1-q^2)]>0\), so the cancellation stratum is absent.

If \(X_1,X_2,\dots\) are iid \(\operatorname{IG}(\mu,\lambda)\), with fixed positive shape ratio \(\phi=\lambda/\mu\), define \(B_n\) from the first \(n\) observations. Then
\[
\sqrt n\,B_n\ \Rightarrow\ N\!\left(0,\frac{3(\phi+4)}{2\phi^2}\right).
\]
Consequently, taking the high-weight limit **first, for each fixed \(n\)**, and only then letting \(n\to\infty\), gives
\[
\lim_{a\to\infty}a^3T_{n,a}=2n B_n^2\ \Rightarrow_{n\to\infty}\ \frac{3(\phi+4)}{\phi^2}\chi_1^2,
\]
\[
\lim_{a\to\infty}a^{3/2}\widetilde T_{n,a}=\frac{n\sqrt\pi B_n^2}{4}\ \Rightarrow_{n\to\infty}\ \frac{3\sqrt\pi(\phi+4)}{8\phi^2}\chi_1^2.
\]
The first equalities hold almost surely for each \(n\); the subsequent arrows are convergence in distribution.

## Assumptions and scope

All samples are positive, finite and nonconstant; \(n\) is an integer at least \(2\). These hypotheses make the finite-sample maximum-likelihood estimate \(\widehat\phi\) positive and finite, because \(n^{-1}\sum_i y_i=1\) and strict harmonic–arithmetic mean inequality gives \(u>1\). No moment hypotheses are required for the fixed-sample asymptotics.

For \(t>0\), the paper's empirical CDF–Stein discrepancy and two corresponding tests are
\[
G_n(t)=\frac1n\sum_{i=1}^n b_i\min\{y_i,t\}-\frac1n\sum_{i=1}^n\mathbf1_{\{y_i\le t\}},
\]
\[
T_{n,a}=n\int_0^\infty G_n(t)^2e^{-at}\,dt,\qquad
\widetilde T_{n,a}=n\int_0^\infty G_n(t)^2e^{-at^2}\,dt,
\quad a>0.
\]
Only the fitted maximum-likelihood version is analyzed; moment-fitted versions use a different \(\widehat\phi\). The null theorem assumes the density \(f(x)=\sqrt{\lambda/(2\pi x^3)}\exp[-\lambda(x-\mu)^2/(2\mu^2x)]\), \(x>0\). These are sequential, not uniform or simultaneous-in-\(n,a\), assertions.

## Proof

**1. Endpoint identity and sharp regimes.** For \(0<t<m\), all empirical indicators vanish and all minima equal \(t\), hence the exact (not asymptotic) identity \(G_n(t)=Bt\). On each interval cut out by the finitely many observations \(y_i\), the discrepancy is affine with bounded coefficients, and after the largest observation it is constant, so \(G_n\) is globally bounded. It follows that
\[
T_{n,a}=nB^2\int_0^\infty t^2e^{-at}dt+O_x(e^{-am}/a),
\]
\[
\widetilde T_{n,a}=nB^2\int_0^\infty t^2e^{-at^2}dt+O_x(e^{-am^2}/a).
\]
(The subtracted polynomial tails above \(m\) satisfy the stated bounds.) The elementary full-line integrals are \(2a^{-3}\) and \(\sqrt\pi/(4a^{3/2})\). If \(B=0\), the discrepancy vanishes identically on \((0,m)\). At \(m\), the empirical CDF jumps by \(r/n\), whereas the min-function term is continuous, whence \(G_n(m+)=-r/n\). On a right neighborhood of \(m\), \(G_n(t)^2=(r/n)^2+O_x(t-m)\). One-sided endpoint Laplace asymptotics thus give respectively \(r^2e^{-am}/(na)\) and \(r^2e^{-am^2}/(2nam)\). Later intervals are exponentially smaller.

**2. Exactly classified three-sample cancellation.** For \(n=3\), \(y_1+y_2+y_3=3\). Put \(u=(\sum_i y_i^{-1})/3\), \(v=(\sum_i y_i^{-2})/3\). Expanding elementary symmetric polynomials with the sum constraint gives
\[
3u^2-3u+1-v=\frac{(y_1-1)(y_2-1)(y_3-1)}{y_1y_2y_3}.
\]
Since \(B=(3u^2-3u+1-v)/[2(u-1)]\), its zero set is exactly the stated sample-mean configuration. Direct substitution for \(n=2\) establishes the stated strictly positive expression.

**3. Null limit with fitted scale and shape.** By scale invariance take \(\mu=1\), so \(X\sim\operatorname{IG}(1,\phi)\). Let \(A_n=\overline X\), \(U_n=\overline{X^{-1}}\), \(V_n=\overline{X^{-2}}\). Then the actual fitted normalized moments are \(u=A_nU_n\), \(v=A_n^2V_n\), not simply \(U_n,V_n\). The population vector is
\[
(A,U,V)=\left(1,1+\phi^{-1},1+3\phi^{-1}+3\phi^{-2}\right),
\]
which yields \(B=0\). Differentiating
\[
F(A,U,V)=\tfrac12\left(3AU+\frac{1-A^2V}{AU-1}\right)
\]
at this vector gives the centered influence function
\[
\psi_\phi(X)=\frac{\phi+3}{2}(X-1)
+\frac{3\phi+6}{2}\left(X^{-1}-1-\phi^{-1}\right)
-\frac\phi2\left(X^{-2}-1-3\phi^{-1}-3\phi^{-2}\right).
\]
It has expectation zero. The inverse-Gaussian moments are \(\mathbb E X^2=1+\phi^{-1}\), \(\mathbb E X^{-3}=1+6\phi^{-1}+15\phi^{-2}+15\phi^{-3}\), and \(\mathbb E X^{-4}=1+10\phi^{-1}+45\phi^{-2}+105\phi^{-3}+105\phi^{-4}\), together with the displayed lower inverse moments and \(\mathbb E X=1\). Expanding the covariance matrix gives exactly
\[
\operatorname{Var}(\psi_\phi(X))=\frac{3(\phi+4)}{2\phi^2}>0.
\]
All needed fourth inverse moments exist. The multivariate iid central limit theorem and delta method prove the normal limit. The continuous mapping theorem applied to the fixed-\(n\) high-weight identities completes the sequential chi-square laws.

## Verification

The standalone script `check.py` uses exact SymPy identities to verify the three-observation factorization, the two-observation coefficient, and the full null influence variance; it then directly quadratures the original piecewise-empirical tests at high weight for both a generic and an exact-cancellation sample, for both specified weights. It reports 13 passed assertions. This is reproducibility support; it is not a substitute for the general analytical endpoint and central-limit proofs. Run from a Python environment with SymPy and mpmath installed using `python check.py`.

## Relationship to prior work

Allison, Betsch, Ebner and Visagie [1,2] introduce these CDF–Stein statistics, the two weight functions, both estimation methods, computational formulas, and fixed-weight asymptotics/bootstrap calibration. The 2019 arXiv posting provides the earliest verified public date, October 30, 2019; the 2022 paper is a later version, not a new dating anchor. The findings above instead provide exact fixed-sample large-weight regimes, an explicit three-observation zero stratum, and the associated sequential null law.

**Important methodological precedent:** Henze and Klar [3], Theorem 3.1, prove a large-weight Abelian \(a^3\) collapse of a *different*, empirical-Laplace-transform inverse-Gaussian goodness-of-fit statistic onto its own squared empirical-moment contrast. Thus polynomial high-weight collapse and its Abelian method are not claimed to be new in general. Their contrast involves a second positive moment and a first inverse moment, whereas the current CDF–Stein contrast uses first and second inverse moments with different maximum-likelihood normalization. The theorem of [3] does not give the exact zero-stratum for the 2019 CDF–Stein statistic, either of its sharp exceptional endpoint laws, or its explicit sequential one-degree-of-freedom coefficient. Analogous high-weight collapse is also known for other testing procedures and is not claimed as a new general principle.

## Limitations

The exceptional exact-cancellation data set has probability zero under a continuous sampling law; the relevance is a finite-data structural boundary and numerical conditioning, not an asserted positive-probability exceptional null event. The asymptotic variable \(a\) tends to infinity with a fixed sample, *then* \(n\to\infty\). No theorem is asserted for simultaneous \(a=a_n\), for local or fixed alternatives, for bootstrap power or size, for data-chosen weights, or for moment estimators. Generic high-weight Abelian reduction is classical. Literature searches cannot exclude all historical priority; an independent audit has not been carried out.

## References

[1] J. S. Allison, S. Betsch, B. Ebner and I. J. H. Visagie, *New weighted \(L^2\)-type tests for the inverse Gaussian distribution*, arXiv:1910.14119, version 1 publicly dated 2019-10-30. https://arxiv.org/abs/1910.14119

[2] J. S. Allison, S. Betsch, B. Ebner and I. J. H. Visagie, *On Testing the Adequacy of the Inverse Gaussian Distribution*, Mathematics 10(3), 350 (2022), DOI:10.3390/math10030350. https://www.mdpi.com/2227-7390/10/3/350

[3] N. Henze and B. Klar, *Goodness-of-fit tests for the inverse Gaussian distribution based on the empirical Laplace transform*, Theorem 3.1, published 2002. https://wwwalt.math.kit.edu/stoch/~klar/seite/veroeffentlichungen/media/invgauss.pdf
