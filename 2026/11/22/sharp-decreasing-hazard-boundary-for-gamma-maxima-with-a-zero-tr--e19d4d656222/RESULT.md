# Sharp decreasing-hazard boundary for gamma maxima with a zero-truncated Poisson sample size

## Finding

Let a positive random sample size have the zero-truncated Poisson distribution with intensity \(\lambda>0\). Conditional on that size, draw independent gamma lifetimes of common shape \(\alpha>0\) and rate \(\beta>0\), and take their maximum \(Z\). The following statements classify its global hazard monotonicity.

1. If \(\alpha\ge1\), the hazard of \(Z\) is strictly increasing for every \(\lambda,\beta>0\).
2. If \(0<\alpha<1\), the exact positive and finite threshold \(\lambda_c(\alpha)\) defined below satisfies: the hazard is strictly decreasing on \((0,\infty)\) **if and only if** \(0<\lambda\le\lambda_c(\alpha)\). Above the threshold it decreases near both endpoints but increases on a nonempty intermediate interval; consequently there is an interior local minimum followed by an interior local maximum. No uniqueness of these turning points is asserted.
3. The boundary depends only on \(\alpha\); the gamma rate \(\beta\) changes the time scale, not the monotonicity classification.

For \(t>0\), put
\[
 f_\alpha(t)=\frac{t^{\alpha-1}e^{-t}}{\Gamma(\alpha)},\quad Q_\alpha(t)=\frac{\Gamma(\alpha,t)}{\Gamma(\alpha)},\quad m_\alpha(t)=\frac{Q_\alpha(t)}{f_\alpha(t)}.
\]
Let \(V(u)=u/(1-e^{-u})\) for \(u>0\). Since \(V:(0,\infty)\to(1,\infty)\) is strictly increasing, its inverse is defined on \((1,\infty)\). For \(0<\alpha<1\), define
\[
 \boxed{\lambda_c(\alpha)=\min_{t>0}\frac{V^{-1}(1+m_\alpha'(t))}{Q_\alpha(t)}.}
\]
This is an exact one-dimensional variational description, rather than an elementary closed-form constant. The minimum is attained and is strictly between zero and infinity.

## Assumptions and scope

Write \(N\sim\operatorname{Poisson}(\lambda)\mid\{N\ge1\}\), independent of all lifetimes, and \(Y_i\sim\operatorname{Gamma}(\alpha,\beta)\) independently with density \(\beta^\alpha y^{\alpha-1}e^{-\beta y}/\Gamma(\alpha)\), for \(y>0\). Let \(Z=\max_{1\le i\le N}Y_i\). All statements quantify over **every** finite strictly positive \(\lambda,\alpha,\beta\), with the partition at \(\alpha=1\). An increasing hazard means strict increase on the full open positive half-line; decreasing likewise. Values at the nonincluded boundaries \(\lambda=0\) and \(t=0\) are limiting calculations only.

## Proof

**1. Distribution and logarithmic derivative.** Let \(t=\beta z\). Conditioning on \(N\) and summing its zero-truncated Poisson generating function gives the survival function and hazard
\[
 S_Z(z)=\frac{1-e^{-\lambda Q_\alpha(t)}}{1-e^{-\lambda}},\qquad
 h_Z(z)=\frac{\lambda\beta f_\alpha(t)}{e^{\lambda Q_\alpha(t)}-1}.
\]
Here \(Q_\alpha'=-f_\alpha\) and \(f_\alpha'/f_\alpha=(\alpha-1)/t-1\). Define \(m=m_\alpha\) and \(V(u)=u/(1-e^{-u})\). Direct differentiation yields
\[
 m'(t)=-1+m(t)\left(1-\frac{\alpha-1}{t}\right),
\]
\[
 \frac{d}{dt}\log h_Z(t/\beta)
 =\frac{f_\alpha(t)}{Q_\alpha(t)}
 \left[V(\lambda Q_\alpha(t))-(1+m_\alpha'(t))\right]. \tag{1}
\]
The positive prefactor fixes the exact sign of the derivative. The function \(V\) increases strictly because its derivative has numerator \(1-(1+u)e^{-u}>0\), and \(V(0+)=1\), \(V(\infty)=\infty\).

**2. Integral Mills-ratio representation and the increasing case.** Changing variables \(s=t+y\) in the upper gamma integral gives
\[
 m_\alpha(t)=\int_0^\infty e^{-y}\left(1+\frac yt\right)^{\alpha-1}\,dy. \tag{2}
\]
For \(\alpha>1\), its integrand is strictly decreasing in \(t\) for every \(y>0\), so \(m_\alpha'(t)<0\). For \(\alpha=1\), \(m_1(t)=1\), hence \(m_1'=0\). In both cases \(V(\lambda Q)>1\ge1+m'\), making (1) strictly positive for every \(t>0\).

**3. Strict positivity and threshold in the decreasing case.** When \(0<\alpha<1\), write \(a=1-\alpha>0\). Differentiating (2) under the integral gives
\[
 m_\alpha'(t)=\int_0^\infty e^{-y}\left(1+\frac yt\right)^{-a}\frac{ay}{t(t+y)}\,dy>0. \tag{3}
\]
Thus \(u_\alpha(t)=V^{-1}(1+m_\alpha'(t))\) is well-defined, positive and continuous. Put \(\Lambda_\alpha(t)=u_\alpha(t)/Q_\alpha(t)\). Since \(V\) increases strictly, (1) implies the *pointwise equivalence*
\[
 h_Z'(z)\begin{cases}<0,&\lambda<\Lambda_\alpha(\beta z),\\=0,&\lambda=\Lambda_\alpha(\beta z),\\>0,&\lambda>\Lambda_\alpha(\beta z).\end{cases} \tag{4}
\]
Continuity and the endpoint limits established next show that \(\Lambda_\alpha\) reaches a finite positive global minimum.

**4. Endpoint control.** As \(t\downarrow0\), elementary gamma-density and survival asymptotics give
\[
 m_\alpha(t)\sim\Gamma(\alpha)t^{1-\alpha},\quad
 m_\alpha'(t)\sim(1-\alpha)\Gamma(\alpha)t^{-\alpha},\quad Q_\alpha(t)\to1.
\]
Because \(V^{-1}(1+w)\sim w\) as \(w\to\infty\),
\[
 \Lambda_\alpha(t)\sim(1-\alpha)\Gamma(\alpha)t^{-\alpha}\to\infty. \tag{5}
\]
As \(t\to\infty\), expanding (2) with integrable exponential moments and differentiating its integral gives
\[
 m_\alpha(t)=1-\frac{1-\alpha}{t}+O(t^{-2}),\quad
 m_\alpha'(t)=\frac{1-\alpha}{t^2}+O(t^{-3}),\quad
 Q_\alpha(t)\sim\frac{t^{\alpha-1}e^{-t}}{\Gamma(\alpha)}.
\]
Since \(V^{-1}(1+w)\sim2w\) as \(w\downarrow0\),
\[
 \Lambda_\alpha(t)\sim2(1-\alpha)\Gamma(\alpha)e^t t^{-\alpha-1}\to\infty. \tag{6}
\]
Consequently \(\lambda_c(\alpha)=\min_{t>0}\Lambda_\alpha(t)\) is achieved at some finite positive \(t\), and \(0<\lambda_c(\alpha)<\infty\).

**5. Exact phase classification.** For \(\lambda<\lambda_c\), (4) gives \(h_Z'<0\) everywhere. For \(\lambda=\lambda_c\), it gives \(h_Z'\le0\) everywhere; the hazard is real analytic on \((0,\infty)\) and has strictly negative derivative near both endpoints by (5)–(6), so it cannot be constant on an interval. Hence it remains **strictly decreasing**. For \(\lambda>\lambda_c\), at any minimizer of \(\Lambda_\alpha\) the derivative is strictly positive; (5)–(6) ensure strict negativity near zero and infinity. By continuity it has an interior local minimum followed by a local maximum. The dependence on \(\beta\) is only through \(t=\beta z\). This proves all claims.

## Verification

The standalone `CHECK.py` evaluates the two independent derivative expressions in (1) numerically using arbitrary-precision gamma and differentiation routines. It also checks the strict signs for examples on both sides of the transition and estimates the minimization at \(\alpha=1/2\). A reproducible numerical estimate is \(\lambda_c(1/2)\approx1.6554326886\); this decimal is illustrative and is not a computer-assisted certificate of the global minimum. The infinite-domain claim and the boundary cases are proved analytically above; finite grid checks are not substituted for this proof.

## Relationship to prior work

Niyomdecha and Srisuradetchai (2023) introduced this maximum-compounded distribution and its exact hazard in their Section 3.2. Their analysis gave selected shape descriptions and a derivative criterion, but not the present necessary-and-sufficient, rate-invariant global decreasing-hazard phase boundary. The 2024 Bayesian paper by Srisuradetchai and Niyomdecha retains the same distribution and studies parameter inference, not this boundary. Earlier zero-truncated-Poisson lifetime-class work by Alkarni and Oraby (2012) uses the **minimum** of the lifetimes, so its general formulas do not imply a hazard classification for the maximum. The separately published minimum-compounded gamma model is likewise a different random variable. General classical gamma-hazard and Glaser criteria remain prior mathematical tools and are not claimed as novel.

## Limitations

The threshold is specified by an attained scalar minimum, not by an elementary formula; neither uniqueness of its minimizing age nor the exact number of turning points above it is claimed. The result does not supply confidence intervals or statistical estimation algorithms. Searches and full-text inspection of closely related open-access primary literature found no covering theorem, but absolute historical priority is not guaranteed, particularly for the vast general literature on compounded lifetime distributions. Numerical values are illustrative. Independent verification by another researcher has not been performed.

## References

1. A. Niyomdecha and P. Srisuradetchai, *Complementary Gamma Zero-Truncated Poisson Distribution and Its Application*, Mathematics 11(11), 2584 (5 June 2023). https://doi.org/10.3390/math11112584
2. P. Srisuradetchai and A. Niyomdecha, *Bayesian Inference for the Gamma Zero-Truncated Poisson Distribution with an Application to Real Data*, Symmetry 16(4), 417 (2 April 2024). https://doi.org/10.3390/sym16040417
3. S. Alkarni and A. Oraby, *A Compound Class of Poisson and Lifetime Distributions*, Journal of Statistics Applications & Probability 1(1), 45–51 (2012). https://doi.org/10.12785/jsap/010106
4. A. Niyomdecha, P. Srisuradetchai and B. Tulyanitikul, *Gamma Zero-Truncated Poisson Distribution with the Minimum Compounded Function*, Thailand Statistician (2023). https://ph02.tci-thaijo.org/index.php/thaistat/article/view/251065
