# Exact zero-count laws and non-self-averaging for two-line Gaussian spectrograms

## Finding
For a stationary circular Gaussian signal consisting of exactly two independent spectral lines, every zero of its Gaussian-window short-time Fourier transform lies on a single randomly positioned horizontal line. Along that line the zeros form a randomly translated lattice. The line frequency has an exact logistic distribution and its temporal offset is uniform and independent. Consequently, counting zeros in a finite frequency band has quadratic time-window variance, despite bounded variance when no frequency restriction is imposed. The complete count distribution, not just its mean and asymptotics, is given below.

## Assumptions and scope
Fix real \(\nu_1<\nu_2\) and \(\Delta=\nu_2-\nu_1>0\), and positive \(\sigma_1,\sigma_2\). Let \(Z_1,Z_2\) be independent standard circular complex Gaussians, meaning their squared moduli are independent mean-one exponentials and their arguments are independent uniform angles, also independent of their moduli. Define
\[
f(t)=\sigma_1Z_1e^{2\pi i\nu_1t}+\sigma_2Z_2e^{2\pi i\nu_2t},\qquad
\varphi(t)=2^{1/4}e^{-\pi t^2}.
\]
The integral \(V_\varphi f(x,\omega)=\int_{\mathbb R}f(t)\overline{\varphi(t-x)}e^{-2\pi i\omega t}\,dt\) is absolutely convergent for every realization. The signal is second-order stationary with spectral measure \(\sigma_1^2\delta_{\nu_1}+\sigma_2^2\delta_{\nu_2}\), which is *purely atomic*, not a power spectral density function. Zeros refer to zeros of the complex-valued STFT, equivalently zeros of its squared modulus, counted without multiplicity.

Set
\[
\mu=\frac{\nu_1+\nu_2}{2}+\frac{\log(\sigma_1/\sigma_2)}{2\pi\Delta},\qquad
p_\Omega(w)=\pi\Delta\operatorname{sech}^2(2\pi\Delta(w-\mu)).
\]
All statements below hold for every choice of these parameters, every finite half-open interval \(I\subset\mathbb R\) of length \(T>0\), and every Borel frequency set \(J\subseteq\mathbb R\).

## Proof
The Gaussian Fourier integral gives, without any stochastic approximation,
\[
V_\varphi f(x,\omega)=2^{1/4}e^{-2\pi i\omega x}\Big[\sigma_1Z_1e^{-\pi(\omega-\nu_1)^2}e^{2\pi i\nu_1x}+\sigma_2Z_2e^{-\pi(\omega-\nu_2)^2}e^{2\pi i\nu_2x}\Big].
\]
Almost surely neither Gaussian coefficient vanishes. Equality of the moduli of the two bracketed summands is equivalent to
\[
\Omega=\mu+\frac{1}{4\pi\Delta}\log\frac{|Z_1|^2}{|Z_2|^2}.
\]
Their phases cancel precisely when \(\Delta x\equiv U\pmod1\), where
\[
U=\frac{1}{2\pi}\arg(-Z_1/Z_2)\pmod1.
\]
Therefore the entire zero set is \(\{((k+U)/\Delta,\Omega):k\in\mathbb Z\}\). The two independent Gaussian arguments make \(U\) uniform and independent of the two squared moduli, and hence independent of \(\Omega\). Since \(|Z_j|^2\) are iid mean-one exponential variables, their logarithmic ratio has CDF \(u\mapsto(1+e^{-u})^{-1}\). This proves that \(\Omega\) has logistic location \(\mu\), scale \(1/(4\pi\Delta)\), and density \(p_\Omega\). At a zero the time and frequency derivatives of the bracketed sum differ by a factor \(i\) and have nonzero magnitude \(2\pi\Delta\) times that of either summand, so every zero is simple as a real two-dimensional zero.

For any bounded measurable rectangle, averaging the uniform phase produces \(\Delta\) zeros per unit time conditional on \(\Omega\in J\); averaging the logistic frequency gives the first intensity
\[
\rho_1(x,w)=\Delta p_\Omega(w)=\pi\Delta^2\operatorname{sech}^2(2\pi\Delta(w-\mu)).
\]
For \(I=[a,a+T)\), the translated lattice has either \(n=\lfloor\Delta T\rfloor\) or \(n+1\) points inside \(I\). By uniform translation the second event has probability \(u=\Delta T-n\). Its count thus has the distribution \(n+B\) for \(B\sim\operatorname{Bernoulli}(u)\). Independently, the whole lattice is retained by the frequency restriction exactly when \(H=\mathbf1_{\{\Omega\in J\}}=1\), with \(H\sim\operatorname{Bernoulli}(p)\). Independence yields \(N\stackrel d=H(n+B)\). Conditional variance and total variance now give
\[
\mathbb EN=p\Delta T,\qquad
\operatorname{Var}N=p\,u(1-u)+p(1-p)(\Delta T)^2.
\]
For \(J=\mathbb R\), \(p=1\) and \(u(1-u)\le1/4\). For every proper spectral event with \(0<p<1\), the quadratic coefficient is positive. Finally, \(|(n+B)-\Delta T|\le1\) for all \(T\), so dividing by \(T\) proves \(N/T\to\Delta H\) almost surely as \(T\to\infty\), taking the windows with a fixed left endpoint. Since \(H\) is nonconstant when \(0<p<1\), the time-average is not self-averaging.

## Verification
The standalone `CHECK.py` uses standard Python only. It computes zeros directly from the two Gaussian STFT summands for several explicit nonzero coefficient pairs and confirms the exact temporal spacing and cancellation; compares the logistic CDF and density formulas against elementary exponential-ratio calculations; derives the first intensity independently from the analytic second derivative of the smoothed atomic spectral measure; and exhaustively enumerates uniform phase bins to test the Bernoulli lattice-count law and its moment formulas. These tests check normalization and implementation; the exact results for all parameters and all \(T\) follow from the proof, not finite tests.

The smoothed atomic spectral measure is
\[
S_\varphi(w)=\sigma_1^2e^{-2\pi(w-\nu_1)^2}+\sigma_2^2e^{-2\pi(w-\nu_2)^2}.
\]
Direct differentiation yields \(1+\frac1{4\pi}(\log S_\varphi)''(w)=\pi\Delta^2\operatorname{sech}^2(2\pi\Delta(w-\mu))\). This is an algebraic consistency identity, not an application of a colored-noise theorem that assumes an ordinary PSD function.

## Relationship to prior work
Escudero, Koliander, and Romero (2026), *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689, Theorem 1.1, derive the first intensity for stationary Gaussian noise with a nonzero PSD *function* of polynomial growth, and Section 5 considers estimating smoothed spectra from empirical zero counts. Their stated model does not include a purely atomic two-line spectral measure, and their first-intensity formula alone does not imply the present exact count distribution, random almost-sure time average, or quadratic band-limited variance. The formal algebraic matching of first intensities above is noted explicitly.

Feldheim, Haimi, Koliander, and Romero (2024), arXiv:2406.20003, study fluctuation and hyperuniformity of zeros of twisted-stationary Gaussian Weyl–Heisenberg functions; their full planar invariance hypotheses and planar-window results differ from this two-line partial-stationarity boundary. Bellourak, Meignen, Polisano, and Nahon (2026), arXiv:2610.13531, study white noise with Hermite windows, a different spectral and window regime. The elementary fact that a two-term exponential has periodically placed zeros is not itself new; the claim here is its precise stochastic spectral law and its opposite full-band versus frequency-filtered fluctuation regimes.

## Limitations
The input is a stationary but **nonergodic** two-line Gaussian process; the variance phenomenon is a boundary counterexample, not a prediction for an absolutely continuous or mixing colored-noise PSD. The zero set consists of a random lattice on one random horizontal line rather than a diffuse planar process. The result gives no quantitative noise-perturbation stability for a broadband component and no claims about three or more spectral lines. While targeted prior-work comparisons found no identical exact fluctuation law, an equivalent formulation in elementary random exponential-polynomial literature may exist; independent publication-priority review is pending.

## References
1. L. A. Escudero, G. Koliander, J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (first posted 2026-09-16), https://arxiv.org/abs/2609.18689 .
2. N. Feldheim, A. Haimi, G. Koliander, J. L. Romero, *Hyperuniformity and non-hyperuniformity of zeros of Gaussian Weyl-Heisenberg Functions*, arXiv:2406.20003 (first posted 2024-06-28), https://arxiv.org/abs/2406.20003 .
3. C. Bellourak, S. Meignen, K. Polisano, M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531 (first posted 2026-10-09), https://arxiv.org/abs/2610.13531 .
