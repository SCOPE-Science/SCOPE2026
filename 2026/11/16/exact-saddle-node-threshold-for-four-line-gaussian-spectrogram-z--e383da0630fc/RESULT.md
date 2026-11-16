# Exact saddle-node threshold for four-line Gaussian spectrogram zero intensities

## Finding
Let \(\delta>0\), and let \(\xi_{-3},\xi_{-1},\xi_{1},\xi_{3}\) be independent standard circular complex Gaussian variables. Define the stationary random four-harmonic signal
\[
f_\delta(t)=\sum_{j\in\{-3,-1,1,3\}}\xi_j e^{ij\delta t},
\]
and its Gaussian-window short-time Fourier transform by
\[
V_g f(s,\omega)=\int_{\mathbb R}f(t)e^{-(t-s)^2/2}e^{-i\omega t}\,dt,
\qquad g(t)=e^{-t^2/2}.
\]
For each bounded Borel region, count zeros of this complex-valued transform (equivalently, spectrogram zeros), without identifying coincident points across time periods. The expected zero measure has a smooth intensity independent of \(s\):
\[
\boxed{\rho_\delta(\omega)=\frac{\delta^2}{\pi}\,V_{k}(2\delta\omega),\qquad
V_k(u)=\frac{d^2}{du^2}\log(\cosh u+k\cosh 3u),\qquad k=e^{-8\delta^2}.}
\]
Put
\[
\boxed{k_\ast=\frac{2\sqrt3-3}{9},\qquad
\delta_\ast=\sqrt{\frac{-\log k_\ast}{8}}\approx0.608777086658879.}
\]
The complete local-maximum classification is:

* If \(0<\delta\le\delta_\ast\), exactly one local maximum occurs, strictly at \(\omega=0\). At equality there are two additional stationary shoulders, neither maxima nor minima.
* If \(\delta>\delta_\ast\), exactly three strict local maxima occur: at \(\omega=0\) and at a symmetric pair \(\omega=\pm\omega_+(\delta)\). Between these are exactly two strict local minima at \(\omega=\pm\omega_-(\delta)\), with \(0<\omega_-<\omega_+\). There are no other stationary points.

All four noncentral locations in the three-peak regime are given exactly by the two roots \(0<z_-(k)<z_+(k)<1\) of
\[
\begin{aligned}
P_k(z)={}&(27k^3-27k^2+9k-1)z^3+(27k^3+9k^2-15k+3)z^2\\
&+(-135k^3+15k^2+19k-3)z+(81k^3+67k^2-13k+1)
\end{aligned}
\]
through
\[
\boxed{\omega_\pm(\delta)=\frac{\operatorname{arctanh}\sqrt{z_\pm(k)}}{2\delta}.}
\]
At the threshold the two positive stationary points coalesce at
\[
\boxed{z_\ast=\frac1{\sqrt3},\qquad
\omega_\ast=\frac{\operatorname{arctanh}(3^{-1/4})}{2\delta_\ast}\approx0.817890667493796.}
\]
Their approach is a genuine saddle-node square-root law:
\[
\boxed{z_\pm(k)=z_\ast\pm\sqrt{2(k_\ast-k)}+O(k_\ast-k)
\qquad(k\uparrow k_\ast).}
\]
Thus, unlike the symmetry-breaking transition for a three-line spectrum, the central maximum persists strictly on both sides of the four-line threshold and two additional maxima emerge through outer folds. In angular-frequency units, the adjacent spectral-line gap is \(2\delta\), so its critical value is \(2\delta_\ast\approx1.217554173317758\).

## Assumptions and scope
The Gaussian variables have mean zero, unit complex variance and mutually independent circularly symmetric laws; no deterministic signal or broadband noise is added. The four spectral lines have angular frequencies \(-3\delta,-\delta,\delta,3\delta\) and equal input power. The Gaussian window is \(e^{-t^2/2}\), not the \(e^{-\pi t^2}\) convention; the frequency variable is angular frequency. The signal is bounded and smooth for each realization but not in \(L^2(\mathbb R)\). Its Gaussian transform is well-defined for all real \((s,\omega)\). Zeros are isolated and simple almost surely, so expected counting with multiplicity agrees with counting distinct zeros. The classification concerns the **expected zero intensity**, not the peak pattern of an individual realization and not the maxima of spectrogram magnitude.

## Proof
**1. Exact analytic reduction.** Gaussian integration gives
\[
V_g f_\delta(s,\omega)=\sqrt{2\pi}\,e^{-\omega^2/2-i\omega s} F_\delta(\omega+is),
\qquad
F_\delta(z)=\sum_{j\in\{-3,-1,1,3\}}\xi_j e^{-j^2\delta^2/2+j\delta z}.
\]
The prefactor never vanishes. The random entire function \(F_\delta\) has diagonal covariance
\[
K_\delta(z,z)=\mathbb E|F_\delta(z)|^2
=2e^{-\delta^2}[\cosh(2\delta\operatorname{Re}z)
+e^{-8\delta^2}\cosh(6\delta\operatorname{Re}z)].
\]
Every pointwise value is a nondegenerate circular Gaussian. Its derivative is not almost surely proportional to the value: the weighted slopes \(j\delta\) are distinct, and all coefficient variances are positive. Standard analytic-Gaussian zero regularity (or the locally bounded Gaussian-density argument) shows that multiple zeros are almost surely absent. For the intensity, the identity \(\mathbb E\log|F(z)|=\frac12\log K(z,z)+c\), valid for nondegenerate circular Gaussian values, together with \(\Delta\log|F|=2\pi\sum\delta_{\mathrm{zeros}}\) in distributions, yields
\[
\rho_\delta(\omega)=\frac{1}{4\pi}\Delta\log K_\delta(z,z)
=\frac{\delta^2}{\pi}V_k(2\delta\omega).
\]
This expected intensity is a nonnegative analytic function independent of time. Moreover \(\int_{\mathbb R}\rho_\delta(\omega)\,d\omega=3\delta/\pi\) because the logarithmic derivative of the hyperbolic sum tends to \(\pm3\) at the two ends. Equivalently, the analytic exponential polynomial has three roots per time period \(\pi/\delta\), almost surely.

**2. Positive rational form and its derivative.** Set \(t=\tanh u\in(-1,1)\), \(z=t^2\). The identity \(\cosh3u=4\cosh^3u-3\cosh u\) gives
\[
\cosh u+k\cosh3u
=\frac{1+k+(3k-1)t^2}{(1-t^2)^{3/2}}.
\]
Twice differentiating its logarithm and using \(dt/du=1-t^2\) gives the exact positive expression
\[
V_k(u)=\frac{(1-t^2)[(3k-1)^2(1-t^2)^2+16k]}
{[1+k+(3k-1)t^2]^2}>0.
\]
The denominator is strictly positive for \(0\le z<1\), since it equals \((1+k)(1-z)+4kz\). A further exact differentiation gives
\[
\frac{dV_k}{du}=-\frac{2t(1-t^2)P_k(t^2)}{[1+k+(3k-1)t^2]^3}.
\]
Thus every noncentral stationary frequency corresponds bijectively to a root of \(P_k\) in \((0,1)\). At \(u=0\),
\[
V_k''(0)=-\frac{2(81k^2-14k+1)}{(1+k)^2}<0,
\]
so the central stationary point is always a strict maximum: the quadratic numerator has discriminant \(-128\) and positive leading coefficient.

**3. Exhaustive algebraic root count.** The following identities hold exactly:
\[
\begin{gathered}
P_k(0)=(1+k)(81k^2-14k+1)>0,\quad P_k(1)=64k^2>0,\\
\operatorname{disc}_z(P_k)=-16384k^3(3k-1)^6(27k^2+18k-1).
\end{gathered}
\]
For \(0<k<k_\ast\) the cubic has three distinct real roots. At \(k=1/32\), direct exact evaluation gives \(P_{1/32}(3/4)=-41739/2097152<0\), so precisely two roots lie in \((0,1)\). Their number cannot change anywhere on the connected interval \((0,k_\ast)\), since there are neither multiple roots nor roots at either endpoint. Hence every such \(k\) has exactly two interior roots, where the sign of \(P_k\) goes from positive to negative to positive. For \(k>k_\ast\) and \(k\ne1/3\), the discriminant is negative, so the cubic has only one real simple root; the positive endpoint values rule out an interior root. At \(k=1/3\), the Bernstein-basis expression below has all coefficients positive, excluding interior roots:
\[
P_k(z)=b_0(1-z)^3+3b_1z(1-z)^2+3b_2z^2(1-z)+b_3z^3,
\]
\[
b_0=(1+k)(81k^2-14k+1),\quad
b_1=\tfrac{4k}{3}(27k^2+54k-5),\quad
b_2=\tfrac{16k}{3}(15k-1),\quad b_3=64k^2.
\]
At \(k=k_\ast\), the exact factorization is
\[
P_{k_\ast}(z)=\left(-16+\frac{80\sqrt3}{9}\right)
\left(z-\frac1{\sqrt3}\right)^2
\left(z-2-\frac1{\sqrt3}\right),
\]
which is nonnegative for \(z\in[0,1]\), with a unique interior double root at \(z_\ast=1/\sqrt3\). Since \(dV_k/du\) does not change sign across this double root, it creates a stationary shoulder, not a new extremum. The derivative signs now prove the claimed one-peak or three-peak classification for both signs of \(\omega\), including the transition.

**4. Exact fold scale.** At \((z,k)=(z_\ast,k_\ast)\), direct differentiation shows
\[
\partial_kP_k(z)=\partial_z^2P_k(z)
=64-\frac{320\sqrt3}{9}>0.
\]
Taylor expansion of the root equation, with \(z-z_\ast=O(\sqrt{k_\ast-k})\), gives
\[
0=\partial_kP(k-k_\ast)+\tfrac12\partial_z^2P(z-z_\ast)^2
+O(|k-k_\ast|^{3/2}),
\]
whence the displayed square-root law follows. Since \(k=e^{-8\delta^2}\) is strictly decreasing, the three-maximum regime is precisely \(\delta>\delta_\ast\).

## Verification
The included `CHECK.py` uses exact SymPy algebra to independently recompute the hyperbolic-to-rational reduction, cubic derivative, discriminant, Bernstein coefficients, endpoint positivity formulas, critical factorization and fold coefficient. It supplements these by numerical stationary-point and positivity checks across the parameter transition. Run `python CHECK.py` after installing `requirements.txt`; successful execution prints `FOUR_LINE_INTENSITY_CHECKS_PASSED 317`. The proof above, not finite sampling, establishes the all-parameter claims.

## Relationship to prior work
Escudero, Koliander and Romero (2026) derive a general expected Gaussian-STFT zero-intensity formula for stationary colored noise with a **function-valued** power spectral density, and investigate slowly varying, Gaussian and rational spectral densities. That source supplies a natural analytic motivation and a related logarithmic-covariance method, but its stated hypotheses do not include a four-atomic spectral measure and the inspected main results and examples do not contain the exact four-line modal phase diagram. Standard Edelman–Kostlan/Gaussian-analytic-function identities already give the intensity from a covariance; this identity is not claimed as new. A publicly accessible three-line Gaussian-spectrogram calculation establishes a different symmetry-breaking transition, in which the central maximum becomes a minimum. The four-line theorem instead gives a persistent central maximum and an **outer saddle-node pair**, with exact radical threshold and fold coefficient. It is not a restatement of the three-line formulas or deterministic tone-interference zero-count results.

## Limitations
The claim is limited to four equally spaced **random independent equal-power** spectral lines and a Gaussian window, with the above angular-frequency normalization. The theorem does not classify arbitrary four-line weights/spacings, individual-realization spectrogram peaks, joint zero correlations, or additional broadband noise. The special-case intensity follows from familiar Gaussian analytic-function theory; the claimed addition is its nontrivial complete modality classification. A possible older equivalent calculation under exponential-family variance, random-polynomial roots or spectral peak terminology remains an originality risk. Independent mathematical and publication-priority review has not been performed.

## References
1. L. A. Escudero, G. Koliander and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (first posted 2026-09-16), especially Sections 1.2, 2.2, 3 and 5, https://arxiv.org/abs/2609.18689.
2. M. Sodin, *Zeros of Gaussian Analytic Functions*, arXiv:math/0007030 (2000), https://arxiv.org/abs/math/0007030.
3. *Exact modal bifurcation of three-line Gaussian spectrogram zeros*, publicly accessible research record, 2026-11-08, examined in full in the available scientific statement. This treats three equally spaced Gaussian spectral lines, not four.
