# Two different traversal speeds identify an unknown causal sensor response and a stationary pollutant profile

## Finding

A stationary, integrable one-dimensional atmospheric pollutant-excess profile can be recovered **together with** a nonparametric, causal, normalized sensor response from two complete measurements of the same road at different known constant positive speeds. Neither component needs to be known a priori. A single speed is insufficient even under the same nonvanishing assumptions. The distinguishing feature is that temporal sensor delay becomes a *speed-dilated spatial blur*, which can be eliminated by a telescoping ratio of Fourier transforms.

For \(v_1>v_2>0\), let \(a=v_2/v_1\) and put
\[
R(\xi)=\frac{\widehat y_{v_1}(\xi)}{\widehat y_{v_2}(\xi)}.
\]
The response transform is obtained explicitly by
\[
\boxed{H(\omega)=\lim_{N\to\infty}\prod_{j=0}^{N-1}R\!\left(\frac{a^j\omega}{v_1}\right),}
\]
followed by \(\widehat c(\xi)=\widehat y_{v_1}(\xi)/H(v_1\xi)\). Inverse Fourier uniqueness then determines both unknown densities almost everywhere.

## Assumptions and scope

The coordinate \(x\in\mathbb R\) is distance along a traversed line and \(t\ge0\) is delay in sensor-response time units. The unknown, static *excess* concentration \(c\) is a nonnegative, nonzero function in \(L^1(\mathbb R)\); any constant ambient background is known and removed before applying the theorem. Its Fourier transform \(C(\xi)=\int_{\mathbb R} c(x)e^{-i\xi x}\,dx\) has no real zeros.

The unknown causal, nonnegative response density \(h\in L^1([0,\infty))\) has known unit integral \(\int_0^\infty h(t)\,dt=1\). Its transform \(H(\omega)=\int_0^\infty h(t)e^{-i\omega t}\,dt\) has no real zeros. In particular \(H(0)=1\); without such gain normalization, source and response amplitudes cannot both be identified. No particular decay law or bounded impulse-response support is assumed.

The same \(c\) and \(h\) are used in both complete observations. The two routes have the same direction and spatial origin, travel speeds \(v_1>v_2>0\) are known and constant, and sensor prehistory is initialized so that the noiseless spatial output is exactly
\[
y_v(x)=\int_0^\infty h(t)c(x-vt)\,dt,\qquad x\in\mathbb R.
\]
All real spatial coordinates (including response tails) are available, not merely a finite road segment. Observation noise, finite sampling, speed fluctuation, sensor drift, changing concentrations and unknown baseline are outside this theorem.

## Proof

**1. Fourier factorization and nonvanishing data.** Set \(k_v(s)=v^{-1}h(s/v)\) for \(s\ge0\) and \(k_v(s)=0\) otherwise. The change of variables \(s=vt\) gives \(y_v=c*k_v\). By Fubini--Tonelli, \(y_v\in L^1(\mathbb R)\), and its Fourier transform factors exactly as
\[
Y_v(\xi)=C(\xi)H(v\xi).
\]
Both factors are nonzero for every real frequency by hypothesis. Therefore all measured Fourier ratios used below are defined. The total observation mass is \(Y_v(0)=C(0)>0\), independent of speed.

**2. Dilation identity and exact inverse.** Dividing the two measured transforms gives
\[
R(\xi)=\frac{H(v_1\xi)}{H(v_2\xi)}.
\]
At the geometric frequencies \(a^j\omega/v_1\), this becomes \(R(a^j\omega/v_1)=H(a^j\omega)/H(a^{j+1}\omega)\). Multiplication through \(j=0,\ldots,N-1\) telescopes **exactly**:
\[
\prod_{j=0}^{N-1}R(a^j\omega/v_1)=\frac{H(\omega)}{H(a^N\omega)}.
\]
Because \(0<a<1\), the sequence \(a^N\omega\to0\); continuity of the Fourier transform of an \(L^1\) function and the gain normalization \(H(0)=1\) yield the claimed limit for every real \(\omega\). This is a pointwise *exact-data* identity; no convergence rate is asserted without additional moments. Once \(H\) is known, division by its nonzero values gives \(C(\xi)=Y_{v_1}(\xi)/H(v_1\xi)\). Uniqueness of Fourier transforms of integrable functions determines \(c\) and \(h\) almost everywhere. Any other admissible pair with the same outputs obeys the same product formula and hence has the same transforms, proving uniqueness.

**3. Sharp one-speed obstruction.** Fix any speed \(v>0\). Choose distinct normalized causal exponential response densities \(h_1(t)=e^{-t}\) and \(h_2(t)=2e^{-2t}\), and put \(k_j(s)=v^{-1}h_j(s/v)\) for \(s\ge0\), zero otherwise. Let \(g(x)=\tfrac12 e^{-|x|}\), \(c_1=g*k_2\), and \(c_2=g*k_1\). Both sources are nonnegative and integrable, both responses are normalized causal densities, and every one of their Fourier transforms is nonzero on the real line: \(\widehat g(\xi)=1/(1+\xi^2)\) and \(\widehat h_j(\omega)=r_j/(r_j+i\omega)\), with \(r_1=1\), \(r_2=2\). Also \(c_1\ne c_2\) and \(h_1\ne h_2\). Yet commutativity and associativity of convolution give
\[
c_1*k_1=g*k_2*k_1=g*k_1*k_2=c_2*k_2.
\]
Thus a complete single-speed observation is non-identifying, and two distinct speeds are the least possible number under this model. If the two nominal speeds coincide, the same obstruction applies.

**4. Exact low-order moment recovery.** If \(c\) and \(h\) have finite second moments after normalization, divide each measured profile by the common mass \(M=\int c>0\). As probability densities these outputs have the law of \(X+vU\), for independent \(X\) with density \(c/M\) and \(U\) with density \(h\). Let \(\mu_j\) and \(s_j^2\) denote the mean and variance of normalized \(y_{v_j}\). Then
\[
\begin{aligned}
\mathbb E[U]&=\frac{\mu_1-\mu_2}{v_1-v_2},
&\mathbb E[X]&=\frac{v_1\mu_2-v_2\mu_1}{v_1-v_2},\\
\operatorname{Var}(U)&=\frac{s_1^2-s_2^2}{v_1^2-v_2^2},
&\operatorname{Var}(X)&=\frac{v_1^2s_2^2-v_2^2s_1^2}{v_1^2-v_2^2}.
\end{aligned}
\]
These formulas are exact and do not require numerically inverting the full Fourier product. For any existing cumulant of order \(m\ge1\), the analogous subtraction divides by \(v_1^m-v_2^m\).

## Verification

The standalone `verify.py` reproduces the Fourier-factorization and finite telescoping identity for a Laplace-shaped nonnegative spatial source and a normalized mixture of two causal exponential response densities. It tests reconstruction for multiple randomly generated distinct speed pairs, response-rate pairs and frequencies, verifies the finite-moment identities, and checks the one-speed alias by explicit convolution-factor commutativity. Run with `python3 verify.py` (Python standard library only). The script is supplementary finite numerical evidence; the analytical proof above establishes the full functional claim. Its output reports 12,800 successful comparisons with a fixed random seed.

## Relationship to prior work

Russell and colleagues' original 2024 mobile air-quality study documented the practical importance of response time, moving-source variability and calibration against higher-grade instruments; it did not construct a nonparametric two-speed blind inverse. Its March 2024 preprint preceded the May 2024 journal publication. In the present theorem the *speed* changes the mathematical width of a static field's spatial response kernel, which is a controlled hypothesis; this does not contradict the field study's conclusion that a direct speed-performance trend was not evident in its observational data.

Mulleti, Lee and Eldar (2020) studied multichannel blind deconvolution and proved finite-dimensional, sparse or finite-impulse-response identification results under coprimeness and sampling assumptions. The general Fourier ratio principle and generic multichannel perspective are prior art. Their examined hypotheses are not fulfilled by arbitrary, nonparametric, infinite-support causal response densities, and their conclusions do not supply this continuous-scale telescoping reconstruction or the present one-speed ambiguity within the same normalized positive class. Carasso (2001) developed direct blind deconvolution for a restricted class of symmetric stable blurs; that is not the arbitrary causal sensor-response setting considered here. Classical Fourier injectivity, convolution factorization and moment additivity are used, not claimed as discoveries.

## Limitations

This is an exact, infinite-spatial-coverage, noise-free uniqueness result, not a stability theorem. Small or noisy Fourier amplitudes can make the quotients and deconvolution severely ill-conditioned, even when theoretically nonzero. Zero-valued transfer functions, unknown sensor gain, unknown baseline, a changing ambient field, unknown speed/origin, finite windows and transient sensor initialization may break the stated reconstruction assumptions. The one-speed counterexample is an impossibility result for the specified class, not a claim about finite-dimensional calibrated sensors. No experimental or field-performance guarantee is asserted. Literature priority is conditional on the inspected sources, and independent scientific audit has not yet been performed.

## References

- H. S. Russell, L. B. Frederickson, M. O. B. Sørensen, J. A. Schmidt, O. Hertel and M. S. Johnson, *Hyperlocal Air Pollution in London Part 1: Validating Low-Cost Sensors for Mobile Measurements from Vehicles*, ChemRxiv preprint, publicly indexed March 5, 2024. DOI: https://doi.org/10.26434/chemrxiv-2024-pjxtj.
- H. S. Russell et al., *Hyperlocal Air Pollution in London: Validating Low-Cost Sensors for Mobile Measurements from Vehicles*, **ACS ES&T Air** 1 (2024), 438--450, published online May 3, 2024. DOI: https://doi.org/10.1021/acsestair.3c00043.
- S. Mulleti, K. Lee and Y. C. Eldar, *Identifiability Conditions for Compressive Multichannel Blind Deconvolution*, **IEEE Transactions on Signal Processing** 68 (2020), 4627--4642, preprint https://arxiv.org/abs/2001.00613, DOI: https://doi.org/10.1109/TSP.2020.3011804.
- A. S. Carasso, *Direct Blind Deconvolution*, **SIAM Journal on Applied Mathematics** 61 (2001), 1980--2007, DOI: https://doi.org/10.1137/S0036139999362592.
