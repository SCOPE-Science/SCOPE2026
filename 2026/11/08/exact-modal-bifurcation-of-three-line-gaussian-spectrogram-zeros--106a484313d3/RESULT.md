# Exact modal bifurcation of three-line Gaussian spectrogram zeros

## Finding
Let \(\Delta>0\), \(\nu_j=\nu_0+j\Delta\) for \(j=0,1,2\), and \(a_0,a_1,a_2>0\). Let \(Z_j\) be independent standard circular complex Gaussian variables and set
\[
f(t)=\sum_{j=0}^2 a_jZ_j e^{2\pi i\nu_jt}.
\]
For the Gaussian window \(g(t)=2^{1/4}e^{-\pi t^2}\), let \(\rho(\omega)\) be the expected number of zeros of \(V_g f\) per unit time and per unit frequency. Write
\[
\beta=\frac{a_1^2}{a_0a_2}e^{2\pi\Delta^2},\qquad
\mu=\nu_1+\frac{\log(a_0/a_2)}{4\pi\Delta},\qquad
u=e^{4\pi\Delta(\omega-\mu)}.
\]
Then, for every real \(\omega\),
\[
\boxed{\rho(\omega)=4\pi\Delta^2\frac{u(\beta+4u+\beta u^2)}{(1+\beta u+u^2)^2}.}
\]
The profile is symmetric about \(\mu\), positive, and has total frequency integral \(2\Delta\). It is **strictly unimodal** with its unique maximum at \(\mu\) if \(0<\beta\le4\), with a quartically flat maximum when \(\beta=4\). If \(\beta>4\), it is **strictly bimodal**, with precisely two equal global maxima at
\[
\boxed{\omega_\pm=\mu+\frac{\log u_\pm}{4\pi\Delta},\quad u_\pm=\frac{\beta^2-8\pm\sqrt{(\beta^2-16)(\beta^2-4)}}{2\beta}.}
\]
Here \(u_-u_+=1\), and \(\mu\) is the unique local minimum. The maximal value is exactly
\[
\boxed{\rho_{\max}=\begin{cases}8\pi\Delta^2/(\beta+2),&0<\beta\le4,\\ \pi\Delta^2\beta^2/(\beta^2-4),&\beta>4.\end{cases}}
\]
In particular, when all three input powers are equal, the transition occurs at \(\Delta=\sqrt{\log4/(2\pi)}\). The result classifies *expected* zero intensity, not the number of visible modes in each random realization.

## Assumptions and scope
The Gaussian variables are independent, centered, unit-variance, and circular. The signal is stationary but has a three-atomic spectral measure; it is a smooth tempered random function, not generally square-integrable over the real line. The window STFT is defined by \(V_g f(x,\omega)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\omega t}\,dt\). Its zeros mean complex zeros of the transform, equivalently zeros of its squared modulus. Expected counts are finite in bounded rectangles. A density \(\rho\) is defined by \(\mathbb E\#\{(x,\omega):V_gf=0,(x,\omega)\in I\times J\}=|I|\int_J\rho(\omega)\,d\omega\) for bounded intervals \(I,J\), and extends to Borel sets by standard measure arguments.

## Proof
**1. Exact Gaussian STFT reduction.** Completing the square in the Gaussian Fourier integral gives
\[
V_gf(x,\omega)=2^{1/4}e^{-\pi(\omega-\nu_0)^2}e^{2\pi i(\nu_0-\omega)x}(A+Bz+Cz^2),
\]
where \(z=e^{2\pi\Delta(\omega-\nu_0)+2\pi i\Delta x}\), \(A=a_0Z_0\), \(B=a_1e^{-\pi\Delta^2}Z_1\), and \(C=a_2e^{-4\pi\Delta^2}Z_2\). The nonzero prefactor has no zeros. Almost surely the quadratic has two distinct nonzero roots: \(A,C\ne0\) and the discriminant is nonzero, since its vanishing is a proper complex-algebraic condition on absolutely continuous Gaussian coefficients. Each root corresponds to a time-periodic horizontal row of zeros with spacing \(1/\Delta\) in time.

**2. Expected radial root count.** Put \(v_0=a_0^2\), \(v_1=a_1^2e^{-2\pi\Delta^2}\), and \(v_2=a_2^2e^{-8\pi\Delta^2}\). The random quadratic has covariance \(K(z,z)=v_0+v_1|z|^2+v_2|z|^4\). The elementary Gaussian logarithmic-potential identity \(\mathbb E\log|P(z)|=\tfrac12\log K(z,z)+c\), coupled with Jensen's formula, gives for every \(R>0\)
\[
\mathbb E\#\{|z_j|\le R\}=\frac{R^2(v_1+2v_2R^2)}{v_0+v_1R^2+v_2R^4}.
\]
One may equivalently obtain this from the standard Gaussian-analytic-function zero-intensity identity; the present proof also follows directly by rotational differentiation of Jensen's formula. Nonzero multiple roots have probability zero, and finite Gaussian logarithmic moments permit averaging. Define \(u=R^2\sqrt{v_2/v_0}\) and \(\beta=v_1/\sqrt{v_0v_2}\). Then the expected cumulative root count is \(F(u)=u(\beta+2u)/(1+\beta u+u^2)\). Under the root-to-STFT correspondence \(R=e^{2\pi\Delta(\omega-\nu_0)}\), one obtains precisely \(u=e^{4\pi\Delta(\omega-\mu)}\) and \(\mu=\nu_1+\log(a_0/a_2)/(4\pi\Delta)\).

**3. Intensity and total count.** The joint coefficient law is invariant under \((A,B,C)\mapsto(A,e^{i\theta}B,e^{2i\theta}C)\); therefore its expected root measure is angularly uniform. Each complex root gives one STFT zero in each time interval of length \(1/\Delta\). Thus \(\rho(\omega)=\Delta\,dF(u(\omega))/d\omega\). Differentiation gives the displayed rational formula. Since \(F(\infty)=2\) and \(F(0)=0\), the total integral is \(2\Delta\). The identity \(\rho(\mu+s)=\rho(\mu-s)\) follows by substituting \(u\mapsto 1/u\).

**4. All critical points and the sharp transition.** Set \(h_\beta(u)=u(\beta+4u+\beta u^2)/(1+\beta u+u^2)^2\). Direct exact differentiation factors as
\[
h_\beta'(u)=-\frac{(u-1)(u+1)\left[\beta(u^2+1)+(8-\beta^2)u\right]}{(1+\beta u+u^2)^3}.
\]
For \(0<\beta<4\), the bracket is strictly positive on \((0,\infty)\): its discriminant equals \((\beta^2-16)(\beta^2-4)\), and in the possible positive-discriminant regime \(\beta<2\) all coefficients of the bracket are positive; for \(2\le\beta<4\), the discriminant is nonpositive. At \(\beta=4\), the bracket is \(4(u-1)^2\); thus the derivative vanishes to order three and the maximum is quartically flat. For \(\beta>4\), the bracket has two distinct positive reciprocal roots \(u_\pm\) in the displayed formula. Its sign alternates positive/negative/positive; combined with the factor \(-(u-1)\), this gives two strict local maxima at \(u_\pm\), a strict local minimum at \(u=1\), and no other extrema. Since \(h_\beta\to0\) at both ends, both maxima are global; their heights agree by reciprocal symmetry. Finally,
\[
h_\beta(u)-\frac{\beta^2}{4(\beta^2-4)}=-\frac{[\beta(u^2+1)+(8-\beta^2)u]^2}{4(\beta^2-4)(1+\beta u+u^2)^2}
\]
for \(\beta>4\), hence the maximum height is \(\pi\Delta^2\beta^2/(\beta^2-4)\). For \(\beta\le4\), evaluate at \(u=1\). This proves the classification and boundary behavior. Equal amplitudes give \(\beta=e^{2\pi\Delta^2}\), establishing the stated transition in line spacing.

## Verification
Executing `python CHECK.py` returned `THREE_LINE_MODALITY_CHECKS_PASSED 93`. It checks the rational differentiation, symbolic factorizations and peak-height identity, total mass and local curvature, representative regimes on both sides of the threshold, and two direct Gaussian STFT evaluations. These checks corroborate the exact algebra; the all-parameter theorem is proved analytically above. The checker uses Python with SymPy.

## Relationship to prior work
Escudero, Koliander and Romero [1] give expected spectrogram-zero intensities for stationary Gaussian colored noise with a **function-valued** power spectral density, as well as slowly varying and regular spectral examples. Their theorem is not directly applicable to the three-atomic power spectrum used here and does not state a three-line mode-splitting phase diagram. The Gaussian-analytic-function logarithmic-potential identity [2,3] yields a general radial-intensity formula for independent Gaussian coefficients; it is an openly acknowledged starting point rather than a new contribution. The claim here is the complete global modality classification for a natural three-tone STFT family, with its exact transition parameter, bifurcating peak locations, and heights. Existing two-line calculations have a single logistic-shaped peak and cannot exhibit this transition.

## Limitations
This is a three-line, equally spaced, independent circular Gaussian model and an expected intensity statement. It does not cover arbitrary frequency spacings, four or more lines, additive broadband noise, or fluctuations/ergodicity of zero counts. Because the threshold follows by a finite algebraic optimization of a classical logarithmic-potential formula, equivalent statements may appear under random-polynomial or spectrogram terminology not indexed in the sources checked. The result is not an independent validation of practical statistical procedures.

## References
1. L. A. Escudero, G. Koliander and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689v1, posted 2026-09-16, sections 1.2 and 3–4, https://arxiv.org/abs/2609.18689.
2. M. Sodin, *Zeros of Gaussian Analytic Functions*, arXiv:math/0007030, 2000, https://arxiv.org/abs/math/0007030.
3. O. Kiro, *Fluctuations for zeros of Gaussian Taylor series*, Journal of the London Mathematical Society 2021, appendix on the Edelman–Kostlan expectation formula, https://doi.org/10.1112/jlms.12457.
