# Quantization shifts the unique optimal site for a cubic Brownian path integral

## Finding

Let \(W\) be standard Brownian motion on \([0,1]\) and let the signed cubic path functional be
\[
C=\int_0^1 W_t^3\,dt.
\]
A sensing device may sample \(W_x\) at one predetermined \(x\in[0,1]\), and the estimator minimizes mean squared error among all measurable decoders of the chosen observation. Consider two fixed observation models: the single zero-threshold sign bit \(S_x=\operatorname{sgn}(W_x)\) and the entire real value \(W_x\). The sign-bit class does not permit changing the threshold, using magnitude bits or applying an arbitrary binary encoder.

For \(x>0\) the optimal sign-bit decoder and its minimum Bayes risk are exactly
\[
\mathbb E[C\mid S_x]=m(x)S_x,\qquad
m(x)=\sqrt{\frac2\pi}\,\frac{\sqrt{x}(x^2-4x+6)}4,
\]
\[
R_{\mathrm{sgn}}(x)=\frac95-\frac{x(x^2-4x+6)^2}{8\pi}.
\]
At \(x=0\), the observation is deterministic and the Bayes risk is \(9/5\). The unique global optimum of the one-bit sign design is
\[
\boxed{x_{\mathrm{sgn}}=\frac{6-\sqrt6}{5}=0.71010205144336438036\ldots.}
\]
Its explained mean-square variance and fraction of the prior variance are respectively
\[
G_{\mathrm{sgn}}^*=\frac{24(138+7\sqrt6)}{3125\pi}
=0.379274049807351133\ldots,
\qquad
\frac{G_{\mathrm{sgn}}^*}{\operatorname{Var}(C)}
=\frac{8(138+7\sqrt6)}{1875\pi}=0.210707805448528407\ldots.
\]

For a full-value observation the optimal decoder is a cubic polynomial,
\[
\mathbb E[C\mid W_x]
=\left(1-\frac{3x}{4}\right)W_x^3
+\frac{7x^2-12x+6}{4}W_x,
\]
and the resulting explained variance equals
\[
G_{\mathrm{full}}(x)=\frac{x(29x^4-72x^3+36x^2+18)}8.
\]
It has a **different unique global optimal site**, \(x_{\mathrm{full}}\), which is the unique zero in \((0,1)\) of
\[
\boxed{145x^4-288x^3+108x^2+18=0.}
\]
More precisely,
\[
\frac34<x_{\mathrm{full}}<\frac45,
\qquad x_{\mathrm{full}}=0.7886095813305781\ldots,
\qquad\frac{G_{\mathrm{full}}(x_{\mathrm{full}})}{\operatorname{Var}(C)}
=0.892283961314875640\ldots.
\]
The two sites satisfy the **strict quantization displacement**
\[
\boxed{x_{\mathrm{sgn}}<x_{\mathrm{full}}},
\]
with a numerical difference of \(0.0785075298872137\ldots\) of the time horizon. Thus sign quantization changes not only the available information but the location where the information should be gathered.

## Assumptions and scope

Brownian motion is centered, has independent increments, \(W_0=0\), and \(\mathbb E[W_sW_t]=\min(s,t)\). All integrals are ordinary time (Lebesgue) integrals of almost surely continuous sample paths. Their moments are finite by Gaussian moment formulas. The horizon is normalized to one. A single observation time is deterministic and selected before seeing the path. The estimator is any square-integrable measurable function of that observation; the best estimator is its conditional expectation. Squared error is averaged over the Brownian law. At \(x=0\), define the sign datum as the deterministic zero bit. For \(x>0\), zero occurs with probability zero, so either convention for \(\operatorname{sgn}(0)\) is immaterial.

The two hardware models are compared at the same one-site sampling budget but different information precision. The sign result is **not** optimality over all one-bit encoders, nonzero thresholds, random times, or adaptive queries.

## Proof

**1. Prior variance.** Odd centered Gaussian moments yield \(\mathbb E C=0\). For \(0\le s\le t\le1\), Wick's pairing rule gives
\[
\mathbb E[W_s^3 W_t^3]=9s^2t+6s^3.
\]
Fubini and symmetry therefore give the exact finite variance
\[
\operatorname{Var}(C)=2\int_0^1\int_0^t(9s^2t+6s^3)\,ds\,dt=\frac95.
\]

**2. One full observation.** Fix \(0<x\le1\), put \(X=W_x\), and write \(c(t,x)=\min(t,x)\). Gaussian regression decomposes
\(W_t=c(t,x)X/x+Z_t\), where \(Z_t\) is independent of \(X\) with variance \(t-c(t,x)^2/x\). Thus
\[
\mathbb E[W_t^3\mid X]
=\frac{c(t,x)^3}{x^3}X^3
+3\frac{c(t,x)}x\left(t-\frac{c(t,x)^2}x\right)X.
\]
Integrating the two coefficients separately on \([0,x]\) and \([x,1]\) gives
\[
A(x)=\int_0^1\frac{c(t,x)^3}{x^3}\,dt=1-\frac{3x}4,
\]
\[
B(x)=3\int_0^1\frac{c(t,x)}x\left(t-\frac{c(t,x)^2}x\right)\,dt
=\frac{7x^2-12x+6}4.
\]
Hence the conditional-mean decoder is \(A(x)X^3+B(x)X\). Since \(X\sim N(0,x)\), its variance is
\[
15A(x)^2x^3+6A(x)B(x)x^2+B(x)^2x
=\frac{x(29x^4-72x^3+36x^2+18)}8.
\]
By the orthogonality of conditional expectation, the squared Bayes risk is exactly \(9/5-G_{\mathrm{full}}(x)\).

**3. Sign observation.** For \(x>0\), \(S_x=\operatorname{sgn}(X)\) is equally likely to be \(+1\) or \(-1\), and the joint law of \((C,S_x)\) changes sign under \(W\mapsto-W\). Consequently \(\mathbb E[C\mid S_x]=\mathbb E[CS_x]S_x\). Standard Gaussian absolute moments give
\[
\mathbb E[X S_x]=\sqrt{2x/\pi},\qquad
\mathbb E[X^3S_x]=2x\sqrt{2x/\pi}.
\]
Using the full-observation conditional mean just derived,
\[
\mathbb E[CS_x]
=\sqrt{2x/\pi}\,[2xA(x)+B(x)]
=\sqrt{\frac2\pi}\,\frac{\sqrt{x}(x^2-4x+6)}4=m(x).
\]
Because \(S_x^2=1\), the variance explained by the sign bit is \(m(x)^2\), proving the displayed risk formula. This is a complete optimization over **all sign-based decoders**, not just linear estimators, because the datum has only two outcomes.

**4. Unique sign-optimal site.** The factor \(x^2-4x+6\) is strictly positive for \(0\le x\le1\), so maximizing \(m(x)^2\) is equivalent to maximizing \(m(x)\). For \(x>0\),
\[
m'(x)=\sqrt{\frac2\pi}\,\frac{5x^2-12x+6}{8\sqrt{x}}.
\]
The two zeros of the numerator are \((6\pm\sqrt6)/5\); exactly one lies in \((0,1)\). The numerator is positive before that zero and negative afterward, while \(m(0)=0\). Hence the stated \(x_{\mathrm{sgn}}\) uniquely maximizes the information gain globally. Exact substitution gives the asserted radical expression for \(G_{\mathrm{sgn}}^*\).

**5. Unique full-observation site and strict displacement.** Differentiation yields
\[
G_{\mathrm{full}}'(x)=\frac{g(x)}8,
\quad g(x)=145x^4-288x^3+108x^2+18,
\quad g'(x)=4x(145x^2-216x+54).
\]
The quadratic factor of \(g'\) is positive at zero, negative at one and has its second real zero above one. Hence \(g\) increases to one interior maximum and then decreases on the remainder of \([0,1]\). Since \(g(0)=18>0\) and \(g(1)=-17<0\), \(g\) has exactly one zero in \((0,1)\), where \(G_{\mathrm{full}}\) changes from increasing to decreasing. The rational signs \(g(3/4)=801/256>0\), \(g(4/5)=-118/125<0\) isolate the unique optimum. Finally
\[
g(x_{\mathrm{sgn}})=\frac{1566-576\sqrt6}{25}>0,
\]
so the full-observation maximum necessarily lies **strictly later** than the sign optimum. This proves the global inequality and both claimed unique optima without an unverified numerical root count.

## Verification

The standalone `verify.py` uses SymPy and mpmath. It checks the Wick covariance integral, both Gaussian-regression coefficient integrals, both explained-variance polynomials, radical and quartic stationarity identities, interval brackets and ten independent high-precision numerical quadrature comparisons (sign/full gain for five times). The output `EXACT_QUADRATURE_CHECKS_OK 27` was obtained from the supplied program. The quartic's **unique** interior root and the global optima do not depend on numerical root finding; they follow from the derivative-sign arguments above. The numerical decimals are illustrative evaluations of exact expressions.

## Relationship to prior work

Foster, Lyons and Oberhauser (2019, arXiv:1904.06998v1) develop Brownian polynomial approximations preserving path integrals and conditional estimates for the integrated **quadratic** process. Their Introduction and Theorems 1–3, together with the discussion of nonlinear stochastic Taylor functionals, motivate low-information approximation, but they do not derive the single-location cubic-path sign/full sampling design or the two explicit optimal sites above.

Fesl, Koller and Utschick (2022, arXiv:2212.04470v1) analyze conditional-mean estimation and one-bit quantization of Gaussian channel coefficients, including the univariate one-bit conditional estimator. Their Section IV and accompanying theorem statements deal with Gaussian **channel targets** rather than the non-Gaussian integrated cubic functional. The Gaussian sign-moment mechanism is classical and is not claimed as new. Guo and Kostina (2019, arXiv:1909.01317v1) optimize *causal, rate-constrained* Wiener trajectory reconstruction; their adaptive event-triggered sampling and time-averaged tracking loss are distinct from one predetermined site for an integrated cubic functional.

Related published results on the odd cubic Gaussian Hermite plane concern extremal sixth-to-second moment ratios of static Gaussian polynomials, rather than the Brownian path-time sampling dependence; another treats finite-sample Gaussian cubic regression control variates, rather than conditional-mean point sensing. Published Brownian-bridge two-node kernel quadrature minimizes a different linear-functional expected error. None implies the pair of exact site optimizations here. The originality comparison acknowledges the standard conditional-expectation projection principle, Gaussian regression, Wick identities, normal absolute moments and derivative tests as prior tools. A broad search cannot exclude previously unindexed equivalent special-case computations.

## Limitations

The theorem fixes a *single* zero-threshold sign bit versus one perfect point reading. Allowing general one-bit encodings, nonzero thresholds, observation noise, adaptive query times or multiple observations can change the optimum. It concerns Brownian motion starting at zero, the unit horizon and the integrated signed third power; Brownian bridges, other power functionals, and stochastic differential equations driven by Brownian motion need separate analysis. The result is an exact benchmark for a low-information path functional, not a proof of improved convergence order for a numerical SDE solver. The work has not had independent mathematical or historical-priority review.

## References

1. J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998v1 (first public 2019-04-15), https://arxiv.org/abs/1904.06998.
2. N. Guo and V. Kostina, *Optimal Causal Rate-Constrained Sampling of the Wiener Process*, arXiv:1909.01317v1 (first public 2019-09-03), https://arxiv.org/abs/1909.01317.
3. B. Fesl, M. Koller and W. Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, arXiv:2212.04470v1 (first public 2022-12-08), https://arxiv.org/abs/2212.04470.
4. *Sharp sixth moments in the odd cubic Gaussian Hermite plane*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-sixth-moments-in-the-odd-cubic-gaussian-hermite-plane--55f0d0a5beeb.
5. *Four samples reverse the oracle comparison for Gaussian cubic regression control variates*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-samples-reverse-the-oracle-comparison-for-gaussian-cubic-re--df33c46c5ea3.
6. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4.
