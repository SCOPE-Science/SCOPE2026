# Exact finite-null variance and singular small-bandwidth fluctuations of the Cauchy Fourier–Stein statistic

## Finding
Let \(n\ge2\) and \(a>0\). Under the *fully specified* standard Cauchy null, let \(X_1,\ldots,X_n\) be independent with density \(1/[\pi(1+x^2)]\), and define the Fourier–Stein goodness-of-fit statistic
\[
T_{n,a}=\frac1n\int_{\mathbb R}\left|\sum_{j=1}^n\left(it-\frac{2X_j}{1+X_j^2}\right)e^{itX_j}\right|^2e^{-a|t|}\,dt.
\]
The exact expectation is \(\mathbb ET_{n,a}=4/a^3+1/a\). Put
\[
P(a)=a^9+12a^8+64a^7+193a^6+356a^5+366a^4+408a^3+416a^2+288a+96.
\]
For all the above \(n,a\), the **exact finite-sample variance** is
\[
\boxed{\operatorname{Var}(T_{n,a})=\frac{1}{2na^2}+\frac{2(n-1)}n\frac{P(a)}{a^5(a+2)^6}.}
\]
In particular, for \(W_{n,a}=a(T_{n,a}-4/a^3)\),
\[
\operatorname{Var}(W_{n,a})=\frac1{2n}+\frac{2(n-1)}n\frac{P(a)}{a^3(a+2)^6}
\sim\frac{3(n-1)}{na^3}\qquad(a\downarrow0).
\]
Nonetheless, for fixed \(n\), as \(a\downarrow0\), almost surely
\[
W_{n,a}\longrightarrow W_{n,0}:=\frac8n\sum_{j=1}^n\frac{X_j^2}{(1+X_j^2)^2},
\quad\mathbb EW_{n,0}=1,\quad\operatorname{Var}(W_{n,0})=\frac1{2n}.
\]
Thus the small-bandwidth limit **does not hold in mean square**. The exact divergence comes from rare near-collisions of distinct sample observations, not from the bounded pointwise limit itself.

## Assumptions and scope
The null parameters are known and fixed at location zero and scale one. The observations are independent and identically distributed with an absolutely continuous standard Cauchy law; \(n\) is any fixed integer at least two; \(a\) is any positive real. No estimated parameters or Studentization is included. All moments and integrals used at each positive \(a\) are finite. The pointwise limit is taken with the realized sample fixed, and the probability-one distinctness of the sample points matters. The rational formula is valid without taking \(n\) or \(a\) asymptotic.

## Proof
Set \(g(x)=2x/(1+x^2)\), and for real \(t\) put
\[
z_t(x)=g(x)[\cos(tx)-\sin(tx)]+t[\cos(tx)+\sin(tx)].
\]
For \(\eta_t(x)=(it-g(x))e^{itx}\), we have \(z_t=\operatorname{Im}\eta_t-\operatorname{Re}\eta_t\). Since the real part of \(\eta_t\) is even in \(t\), whereas its imaginary part is odd, integration against the even weight \(e^{-a|t|}\) gives the exact identity
\[
T_{n,a}=\frac1n\int_{\mathbb R}\left(\sum_{j=1}^nz_t(X_j)\right)^2e^{-a|t|}\,dt.
\]
This is an identity for every real sample, not a limiting approximation.

The standard Cauchy Fourier transform \(\mathbb E e^{iuX}=e^{-|u|}\) and the elementary rational Fourier transforms yield
\[
\mathbb E[g(X)e^{iuX}]=iu e^{-|u|},\qquad
\mathbb E[g(X)^2e^{iuX}]=\tfrac12(1+|u|-u^2)e^{-|u|}.
\]
For instance the latter follows from \(4x^2/(1+x^2)^3=4[(1+x^2)^{-2}-(1+x^2)^{-3}]\) and the standard transforms of these two rational kernels. Thus \(\mathbb Ez_t(X)=0\) for all \(t\). Multiplying the trigonometric expressions, using the vanishing of odd Cauchy integrals, and simplifying gives the explicit covariance kernel
\[
K(s,t)=\mathbb E[z_s(X)z_t(X)]
=\tfrac12\left(s^2+t^2+|s-t|+1\right)e^{-|s-t|}.
\]
This identity can also be verified by the four Fourier transforms of the products \(\cos(sX)\cos(tX)\), \(\sin(sX)\sin(tX)\), and the corresponding terms weighted by \(g\) and \(g^2\).

Let \(h_a(x,y)=\int z_t(x)z_t(y)e^{-a|t|}\,dt\), so \(T_{n,a}=n^{-1}\sum_{i,j}h_a(X_i,X_j)\). It is a degenerate kernel away from the diagonal:
\[
\mathbb E[h_a(x,X)]=0\quad\text{for every real }x.
\]
Direct integration of the diagonal, using the original complex modulus, gives
\[
h_a(x,x)=\frac4{a^3}+\frac{2g(x)^2}{a}.
\]
Cauchy trigonometric parametrization \(X=\tan U\), \(U\sim\operatorname{Unif}(-\pi/2,\pi/2)\), yields \(g(X)=\sin(2U)\), whence \(\mathbb E g(X)^2=1/2\), \(\mathbb E g(X)^4=3/8\), and \(\operatorname{Var}(g(X)^2)=1/8\). The diagonal therefore has expectation \(4/a^3+1/a\) and variance \(1/(2a^2)\).

Distinct off-diagonal summands are uncorrelated unless they represent the same unordered pair: conditional centering annihilates all pairs sharing just one observation, and also annihilates their covariance with the diagonal. Consequently, for every \(n\ge2\),
\[
\operatorname{Var}(T_{n,a})=\frac{1}{2na^2}+\frac{2(n-1)}n J(a),\qquad
J(a)=\mathbb E[h_a(X_1,X_2)^2]
=\iint_{\mathbb R^2}K(s,t)^2e^{-a(|s|+|t|)}\,ds\,dt.
\]
Fubini is justified because \(a>0\), \(|g|\le1\), and the squared-integrability bound is dominated by a polynomial in \(|s|+|t|\) times the exponential weight.

For completeness, the double integral is evaluated explicitly by partitioning the frequency plane. On the same-sign quadrants, put \(s=r+u\), \(t=r\) with \(r,u\ge0\); account for the two orderings in each of two quadrants. Their combined contribution is
\[
J_{\rm same}(a)=\int_0^\infty\!\int_0^\infty
(2r^2+2ru+u^2+u+1)^2e^{-2ar-(a+2)u}\,dr\,du.
\]
On the two opposite-sign quadrants, put \(s=r\), \(t=r-u\), with \(0\le r\le u\). Their combined contribution is
\[
J_{\rm opposite}(a)=\frac12\int_0^\infty\!\int_0^u
\big(r^2+(u-r)^2+u+1\big)^2e^{-(a+2)u}\,dr\,du.
\]
Termwise polynomial integration by \(\int_0^\infty u^k e^{-bu}\,du=k!/b^{k+1}\) gives
\[
J_{\rm same}=\frac{a^8+10a^7+46a^6+126a^5+236a^4+260a^3+296a^2+240a+96}{2a^5(a+2)^5},
\]
\[
J_{\rm opposite}=\frac{a^4+12a^3+62a^2+168a+224}{2(a+2)^6}.
\]
Adding these fractions yields \(J(a)=P(a)/[a^5(a+2)^6]\), proving the exact variance. The leading coefficient is \(\lim_{a\downarrow0}a^5J(a)=96/2^6=3/2\), hence the asserted singular variance of \(W_{n,a}\).

Finally, when two realized observations are distinct, the integration-free pair kernel is \(O(a)\) as \(a\downarrow0\), since each off-diagonal term is a rational function with numerator proportional to \(a\) and a strictly positive limiting denominator. The sample has distinct observations almost surely. Hence \(W_{n,a}\) converges almost surely to \(2n^{-1}\sum_jg(X_j)^2\); its stated moments follow from the arcsine representation above. Since \(\operatorname{Var}(W_{n,a})\to\infty\) while \(W_{n,0}\) is bounded, convergence in \(L^2\) is impossible.

## Verification
Run `python3 checker.py` from this package. The pure-standard-library checker independently expands the same-sign and opposite-sign double integrals in exact rational arithmetic, verifies the rational expression at 60 distinct positive rational bandwidth values (more than needed for a degree-nine polynomial identity once the denominator and degree bounds have been established), verifies score moments and checks the finite-sample variance decomposition over sample sizes 2 through 29. Expected output: `PASS: 402 exact rational assertions`. The analytical computation above, not numerical enumeration, proves the statements for all admissible sample sizes and positive real bandwidths.

Independent numerical validation of the original integration-free statistic with standard-Cauchy simulations at \(n=2\), \(a\in\{0.7,1,2\}\) also agreed with the predicted means and variances within Monte Carlo error. Such simulation is supporting evidence, not a proof. For example, at \(n=2,a=1\), exact variance is \(9529/2916\).

## Relationship to prior work
Ebner, Eid and Klar (first publicly available in 2021) introduce the Fourier–Stein Cauchy test, give the integration-free kernel, the fixed-sample small-bandwidth limit and asymptotic null covariance kernels with *estimated* nuisance parameters. They do not state the exact all-\(n\), all-\(a\) variance formula for the **known-parameter** null, nor the sharp divergence of the variance of the centered small-bandwidth statistic. Their pointwise limit and Cauchy score moment identity are used as established inputs, not claimed here as original. The paper's general covariance kernel makes part of this calculation possible, but does not itself establish the finite-sample variance, explicit rational integral or non-\(L^2\) comparison.

Matsui and Takemura (2005), and Gürtler and Henze (2000), study different empirical-characteristic-function Cauchy tests and estimated-parameter asymptotic laws. They do not directly provide the finite-sample Fourier–Stein result above. Residual priority risk remains for a differently named general degeneracy/weighted-integral identity that implies the exact expression or asymptotic constant.

## Limitations
No result is asserted for fitted Cauchy location or scale, or for an alternative weight other than \(e^{-a|t|}\). The variance divergence concerns the centered and scaled **untruncated finite-sample family** as the smoothing parameter approaches zero; it does not say the pointwise endpoint statistic is invalid, nor that all practical significance thresholds are unstable. The exact formula is specific to the fully specified Cauchy null and does not establish power or optimal bandwidth. The proof is mathematical, not independently audited. Earlier mathematical equivalent formulations cannot be excluded with certainty.

## References
1. B. Ebner, L. Eid and B. Klar, *Cauchy or not Cauchy? New goodness-of-fit tests for the Cauchy distribution*, first public preprint 24 June 2021, arXiv:2106.13073, https://arxiv.org/abs/2106.13073 ; *Statistical Papers* (online 22 December 2022), https://doi.org/10.1007/s00362-022-01382-0 .
2. M. Matsui and A. Takemura, *Empirical characteristic function approach to goodness-of-fit tests for the Cauchy distribution with parameters estimated by MLE or EISE*, *Annals of the Institute of Statistical Mathematics* **57** (2005), 183–199, https://www.ism.ac.jp/editsec/aism/57/183.pdf .
3. N. Gürtler and N. Henze, *Goodness-of-fit tests for the Cauchy distribution based on the empirical characteristic function*, *Annals of the Institute of Statistical Mathematics* **52** (2000), 267–286, https://doi.org/10.1023/A:1004113805623 .
