# Three-stage spectral splitting for phase-opposed Gaussian three-tone measurements

## Finding
Fix a frequency separation \(d>0\) and a middle-tone amplitude \(a>0\). Let
\[
f_{d,a}(t)=e^{-idt}-a+e^{idt},\qquad g(t)=(2\pi)^{-1/2}e^{-t^2/2}.
\]
The real-frequency profile of the Gaussian short-time Fourier transform at the phase-opposition time is
\[
I_{d,a}(x)=\left|\int_{\mathbb R}f_{d,a}(t)g(t)e^{-ixt}\,dt\right|^2
=\left[e^{-(x-d)^2/2}-a e^{-x^2/2}+e^{-(x+d)^2/2}\right]^2.
\]
Put \(s=d^2\) and define two sharp curves
\[
A(s)=2e^{-s/2}(1-s),\qquad B(s)=2e^{-s/2}.
\]
For **every** \(s>0\) and \(a>0\), the number of distinct local maxima of \(x\mapsto I_{\sqrt{s},a}(x)\) on the entire real axis is exactly
\[
\boxed{\quad
N(s,a)=\begin{cases}
1,&0<a\le A(s),\\
2,&A(s)<a\le B(s),\\
3,&a>B(s).
\end{cases}\quad}
\]
The first case can occur only for \(0<s<1\). In the first case the sole maximum is at the origin; in the second there are exactly two symmetric off-center maxima; in the third there are exactly three maxima, one central and two symmetric off-center. No additional maxima exist, however small their heights. At \(a=A(s)>0\), the central maximum is quartically flat; at \(a=B(s)\), the origin is instead a fourth-order zero of intensity. In the three-peak regime the two noncentral intensity zeros are exactly
\[
\boxed{\quad x=\pm\frac{1}{\sqrt{s}}\operatorname{arcosh}\!\left(\frac{a e^{s/2}}{2}\right).\quad}
\]
The off-center maxima, when present, occur at \(x=\pm x_*(s,a)\), where \(x_*(s,a)>0\) is the **unique** positive solution of
\[
\boxed{\quad 2e^{-s/2}\left(\cosh(\sqrt{s}\,x)-\frac{\sqrt{s}}x\sinh(\sqrt{s}\,x)\right)=a.\quad}
\]
For each fixed \(0<a<2\), increasing \(s\) gives exactly the sequential phase diagram one peak, two peaks, three peaks, with unique transition values \(s_0(a)\in(0,1)\) and \(s_1(a)=2\log(2/a)>s_0(a)\), determined by \(A(s_0(a))=a\) and \(B(s_1(a))=a\). At the first transition,
\[
x_*(s,a)^2=\frac{3}{s_0(a)}(s-s_0(a))+O_a((s-s_0(a))^2)
\quad(s\downarrow s_0(a)),
\]
and immediately above the second transition the newly appearing central maximum has intensity
\[
I_{\sqrt{s},a}(0)=\frac{a^2}{4}(s-s_1(a))^2+O_a((s-s_1(a))^3).
\]
When \(a\ge2\), the profile has three local maxima for every \(s>0\).

In the equal-amplitude case \(a=1\), the first and second threshold frequency separations are respectively \(d_0=\sqrt{s_0(1)}\approx0.625937683618\) and \(d_1=\sqrt{2\log2}\approx1.177410022515\). Thus a phase-opposed three-tone Gaussian spectrogram displays a rigorously sharp **one-to-two-to-three frequency-peak sequence**, with a distinct symmetry-breaking bifurcation and central-null transition.

## Assumptions and scope
All frequencies \(x\) range over \(\mathbb R\); the frequency separation \(d\) and amplitude \(a\) are strictly positive real numbers. The outer tones have equal unit complex amplitudes and the central tone has opposite phase and magnitude \(a\). The analysis window \(g\) is normalized to have unit integral and frequency standard deviation one. The signal is bounded and tempered, not square-integrable on \(\mathbb R\), but the defining Gaussian short-time Fourier integral is absolutely convergent. We count distinct **strict local intensity maxima**; a quartically flat strict maximum counts once. We do not claim all-time ridge counts, arbitrary coefficient phases, unequal outer amplitudes, noisy signals or detectability above a practical signal-to-noise threshold.

## Proof
**1. Exact Gaussian transform and its derivative.** The Fourier transform of \(g\) is \(e^{-x^2/2}\). Therefore the displayed formula for \(I\) is exact. Put \(c=e^{-s/2}\) and write
\[
F(x)=e^{-x^2/2}\bigl(2c\cosh(\sqrt{s}\,x)-a\bigr),\qquad I(x)=F(x)^2.
\]
The even function \(F\) tends to zero from above at both infinite ends. For \(x>0\), direct differentiation gives
\[
F'(x)=xe^{-x^2/2}\bigl(a-H_s(x)\bigr),
\qquad H_s(x)=2c\left(\cosh(\sqrt{s}\,x)-\frac{\sqrt{s}}x\sinh(\sqrt{s}\,x)\right),
\]
with continuous value \(H_s(0)=2c(1-s)=A(s)\).

**2. Exact count of positive critical points.** Put \(t=sx^2\). Expanding the entire functions gives
\[
\frac{H_s(x)-a}{2c}=
\left(1-s-\frac{a}{2c}\right)
+\sum_{k=1}^\infty\frac{1-s/(2k+1)}{(2k)!}\,t^k.
\]
The nonconstant coefficients change sign at most once, from negative to positive, and are eventually strictly positive. If \(a\le A(s)\), then necessarily \(s<1\); every nonconstant coefficient is strictly positive, whence \(H_s(x)>a\) for all \(x>0\) and \(F'(x)<0\). If \(a>A(s)\), the constant coefficient is strictly negative. Choose the first positive nonconstant coefficient, of index \(m\). After dividing this series by \(t^m\), every term with a negative coefficient and negative power has strictly positive derivative, and every positive-power term with a positive coefficient does also. Thus the quotient is strictly increasing on \((0,\infty)\). It tends to \(-\infty\) at zero and \(+\infty\) at infinity, the latter since \(H_s(x)\) grows exponentially in \(x\). There is exactly one positive root \(x_*\), with \(F'\) positive before it and negative after it. In particular, \(F(x_*)>0\), since \(F(x)\to0^+\) as \(x\to+\infty\).

**3. From amplitude to intensity.** In the first regime \(F(0)=B(s)-a>0\), and \(F\) decreases strictly from its central maximum toward zero. Thus \(F^2\) has one strict maximum. In the second regime there is one positive maximum \(F(x_*)>0\), and \(F(0)=B(s)-a\ge0\), so the origin is an intensity minimum and exactly two symmetric intensity maxima occur at \(\pm x_*\). In the third regime \(F(0)<0\), while \(F(x_*)>0\); strict monotonicity on \((0,x_*)\) gives one and only one zero there. Solving \(2c\cosh(\sqrt{s}x)=a\) gives the stated zero locations. Because \(I'=2FF'\), the origin is a strict maximum of \(I\) and the two positive-amplitude side peaks remain strict maxima, with the two zeros as intervening minima. This proves the exhaustive global classification, including the boundaries. At \(a=A(s)\), coefficient positivity starts with the quadratic term in \(H_s\); hence \(F'\) has leading negative cubic term and the sole central peak is quartically flat. At \(a=B(s)\), \(F(0)=0\) and \(F''(0)=2cs>0\), so \(I\) has a fourth-order zero.

**4. Two thresholds and their sharp onsets.** The function \(A(s)\) strictly decreases from \(2\) to \(0\) on \((0,1)\), and \(B(s)\) decreases from \(2\) to zero on \((0,\infty)\); moreover \(A(s)<B(s)\). Thus for \(0<a<2\) the two transition values exist uniquely in the stated order. Near \(s_0\),
\[
a-H_s(0)=e^{-s_0/2}(3-s_0)(s-s_0)+O_a((s-s_0)^2),
\]
while
\[
H_s(x)-H_s(0)=e^{-s/2}s(1-s/3)x^2+O_s(x^4).
\]
The analytic implicit-function theorem in \(x^2\), with nonzero quadratic coefficient at \(s_0\in(0,1)\), yields \(x_*^2=3(s-s_0)/s_0+O_a((s-s_0)^2)\). At \(s_1\), \(2e^{-s_1/2}=a\), and Taylor expansion of \((2e^{-s/2}-a)^2\) yields the displayed quadratic onset of the central intensity peak. Finally, \(a\ge2>B(s)\) for all \(s>0\), proving the last case.

## Verification
The included independent-from-formula numerical/symbolic script `CHECK.py` reproduces the Gaussian integral normalization, derivative identity, analytic series coefficients, finite modal classifications across representative parameter regimes, uniqueness and sign of positive critical points, and the two critical asymptotic laws. It passes **212** assertions in the recorded execution. These checks are diagnostic finite tests; the all-parameter result follows from the sign-pattern argument above. Run `python CHECK.py` with the libraries listed in `requirements.txt`.

## Relationship to prior work
Chand, Nolen and Wu [1] developed sharp Gaussian-window STFT spectral-interference analysis for a **two-tone** model. Their source is the motivation for asking what happens for three coherent, equally spaced tones with the middle tone opposed. The present theorem distinguishes two separate, parameter-dependent phenomena: off-center maxima bifurcate, then a formerly cancelled central component becomes a third local intensity peak. General two-tone resolution calculations do not imply either two-parameter curve for the signed three-tone spectrum. Miramont and coauthors [2] consider three-tone interference in the context of **spectrogram zeros and denoising**, not an exhaustive global count of local intensity maxima for a phase-opposed three-tone model. A published three-line Gaussian model [3] classifies maxima of **expected random-zero intensity**, not maxima of this deterministic spectrogram. Another published note [4] studies a **two-chirped-tone** local tricritical transition; it neither has the same signal nor supplies the present global modal classification. The standard Gaussian Fourier transform and elementary power-series sign arguments are acknowledged tools, not claims of novelty.

## Limitations
The classification concerns one **fixed phase-opposition time slice**. No all-time or multidimensional Morse classification is established. The side maxima can have arbitrarily small amplitudes and may be undetectable under noise. The source [1] has an available abstract but its complete long-form manuscript was not accessible for direct comparison; a hidden general multi-tone appendix or older signed-Gaussian-mixture theorem remains a concrete priority risk. The theorem is self-contained and makes no priority claim beyond the material examined. Independent publication-priority and mathematical audits have not been performed.

## References
1. S. Chand, J. Nolen and H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910v1, first posted 2026-01-15, https://arxiv.org/abs/2601.10910; *Applied and Computational Harmonic Analysis* 85 (2026), DOI:10.1016/j.acha.2026.101889.
2. J. M. Miramont, F. Auger, M. A. Colominas, N. Laurent and S. Meignen, *Unsupervised classification of the spectrogram zeros*, arXiv:2210.05459 (2022), https://arxiv.org/abs/2210.05459.
3. *Exact modal bifurcation of three-line Gaussian spectrogram zeros*, public research result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-modal-bifurcation-of-three-line-gaussian-spectrogram-zeros--106a484313d3.
4. *A tricritical frequency-ridge transition for two coherently chirped tones*, public research result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-tricritical-frequency-ridge-transition-for-two-coherently-chir--1e23e76ae647.
