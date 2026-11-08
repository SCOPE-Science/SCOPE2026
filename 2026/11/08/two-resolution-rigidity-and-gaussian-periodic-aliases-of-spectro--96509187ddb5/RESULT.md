# Two-resolution rigidity and Gaussian-periodic aliases of spectrogram zero intensities

## Finding
Fix two **distinct** numbers \(c_1,c_2>0\). Let \(\mathcal P\) consist of all strictly positive continuous functions \(S:\mathbb R\to(0,\infty)\) for which there are constants \(C_S>0\), \(m_S\geq0\) satisfying \(S(x)\leq C_S(1+|x|)^{m_S}\) for every real \(x\). Set
\[
Z_c^S(R)=\int_{\mathbb R}e^{-c(R-x)^2}S(x)\,dx,\qquad
I_c^S(R)=1+\frac1{2c}\frac{d^2}{dR^2}\log Z_c^S(R).
\]
**Two-resolution classification.** For \(S,T\in\mathcal P\), equality \(I_{c_j}^S=I_{c_j}^T\) on all of \(\mathbb R\) for both \(j=1,2\) holds exactly in the following two cases:

1. There is a constant \(C>0\) with \(T=CS\).
2. There are \(a>0\), \(b\in\mathbb R\), \(h\in\mathbb R\setminus\{0\}\), a continuous positive \(h\)-periodic function \(p\), and \(C>0\) for which
\[
S(x)=e^{-ax^2+bx}p(x),\quad
k_1=\frac{h(a+c_2)}{c_2-c_1},\quad
k_2=\frac{h(a+c_1)}{c_2-c_1},
\]
\[
T(x)=C\exp(2c_1k_1x-c_1k_1^2)S(x-k_1).
\]
In case 2, the same \(T\) can be written with \(c_2,k_2\) instead of \(c_1,k_1\), after changing only its positive overall constant; and \(T\) is **not** proportional to \(S\).

Thus two distinct Gaussian frequency resolutions identify every spectrum in \(\mathcal P\), up to global power scale, **unless** the spectrum is a Gaussian envelope modulated by a positive periodic function. This exceptional family is sharp, infinite-dimensional, and includes nonconstant \(C^\infty\) examples. The assertion is about **two population first intensities**, not about full point-process laws or sample-based estimation.

## Assumptions and scope
The strict positivity and continuity in \(\mathcal P\) permit pointwise logarithms. Only an upper polynomial-growth bound is required; a positive lower bound at infinity is not assumed. The two resolutions \(c_1,c_2\) are fixed and distinct; arbitrary continuous positive periodic functions are allowed, without a prescribed fundamental period.

For the Gaussian STFT window \(g_\sigma(t)=(2\sigma^2)^{1/4}e^{-\pi\sigma^2t^2}\), the squared Fourier-window kernel is a positive constant times \(e^{-c\omega^2}\), where \(c=2\pi/\sigma^2\). The pure stationary circular Gaussian noise first-zero-intensity formula, after the area-preserving time-frequency dilation, equals \(I_c^S\). The standard unit-width formula is given by Escudero, Koliander, and Romero [1, Theorem 1.1, pure-noise specialization]; the dilation only changes \(c\) and the coefficient to \((2c)^{-1}\). No deterministic signal component is included in the present claim.

## Proof
**1. Gaussian convolution and variance.** For any \(c>0\) and \(S\in\mathcal P\), the integral \(Z_c^S\) is everywhere positive and smooth. Under the probability density proportional to \(e^{-c(R-x)^2}S(x)\), write \(m_c(R)\) and \(v_c(R)\) for the mean and variance of \(x\). Direct differentiation under the integral gives
\[
(\log Z_c^S)'(R)=2c(m_c(R)-R),\qquad
m_c'(R)=2c\,v_c(R).
\]
Consequently \(I_c^S=m_c'=2c\,v_c>0\). This checks the normalization independently of the zero-counting representation.

**2. Exact one-resolution gauge.** Suppose \(I_c^T=I_c^S\). Integrating the equality of logarithmic second derivatives twice gives real constants \(A,B\) with \(Z_c^T(R)=e^{AR+B}Z_c^S(R)\) for every \(R\). Let \(k=A/(2c)\). Define the entire bilateral Laplace transform
\[
F_c^S(z)=\int_{\mathbb R}e^{zx-cx^2}S(x)\,dx.
\]
Since \(Z_c^S(R)=e^{-cR^2}F_c^S(2cR)\), the relation becomes \(F_c^T(z)=e^{kz+B}F_c^S(z)\), first for real \(z\) and hence everywhere by analyticity. At purely imaginary \(z\), uniqueness of Fourier transforms of finite measures therefore yields
\[
T(x)=e^B e^{2ckx-ck^2}S(x-k)\qquad(x\in\mathbb R).
\]
Conversely, any such transformation whose right-hand side belongs to \(\mathcal P\) gives \(Z_c^T(R)=e^{2ckR+B}Z_c^S(R)\), so the two \(I_c\) profiles coincide. The full Fourier uniqueness, not any finite moment matching, is used here.

**3. Compatibility at two resolutions.** Apply Step 2 to each of \(c_1,c_2\), obtaining real \(k_1,k_2\) and positive constants \(C_1,C_2\). If \(k_1=k_2=k\), strict positivity of \(S\) forces \(e^{2(c_1-c_2)kx}\) to be constant in \(x\), hence \(k=0\); therefore \(T\) is proportional to \(S\).

Otherwise let \(h=k_1-k_2\ne0\) and \(F(x)=\log S(x)\). Comparing the two gauge identities and putting \(y=x-k_1\) gives a **global** finite-difference equation
\[
F(y+h)-F(y)=2(c_1k_1-c_2k_2)y+D
\]
for some real \(D\). Every continuous solution has the form
\[
F(y)=\alpha y^2+by+\log p(y),\qquad
\alpha=\frac{c_1k_1-c_2k_2}{h},
\]
where \(p\) is strictly positive, continuous and \(h\)-periodic. Indeed choose \(b\) so the quadratic-affine part has exactly the displayed finite difference, and exponentiate the remaining periodic function.

Because \(p\) has positive finite minimum and maximum on a period, the polynomial upper-growth assumption on \(S\) rules out \(\alpha>0\). When \(\alpha=0\), it also forces \(b=0\), so \(S=p\) is positive periodic. Polynomial growth of \(T=C_1e^{2c_1k_1x-c_1k_1^2}p(x-k_1)\) then forces \(k_1=0\); the relation \(\alpha h=c_1k_1-c_2k_2\) yields \(k_2=0\), contradicting \(h\ne0\). Hence \(\alpha=-a<0\).

Substituting \(\alpha=-a\) gives \((a+c_1)k_1=(a+c_2)k_2\). Together with \(k_1-k_2=h\), these equations have the unique solution
\[
k_1=\frac{h(a+c_2)}{c_2-c_1},\qquad
k_2=\frac{h(a+c_1)}{c_2-c_1}.
\]
This proves the necessary exceptional form.

**4. Sufficiency and genuine ambiguity.** Conversely, take arbitrary \(a>0\), real \(b\), nonzero \(h\), and positive continuous \(h\)-periodic \(p\), and define \(S,k_1,k_2,T\) as in the theorem. Both \(S\) and \(T\) have Gaussian decay times a bounded positive factor, hence belong to \(\mathcal P\). Since \(k_1-k_2=h\), periodicity gives \(p(x-k_1)=p(x-k_2)\), and \((a+c_1)k_1=(a+c_2)k_2\) makes the two transformed Gaussian envelopes' linear coefficients identical. Thus there is \(C_2>0\) such that
\[
T(x)=C_2e^{2c_2k_2x-c_2k_2^2}S(x-k_2).
\]
The converse in Step 2 gives equality of both intensity profiles. Finally, \(T/S\) is an exponential of a **nonzero** linear term, namely \(2(a+c_1)k_1x\), times a bounded positive periodic ratio; since \(k_1\ne0\), it cannot be constant. This finishes the classification.

## Verification
The accompanying `CHECK.py` independently computes the zero-intensity profile as \(2c\) times a Gaussian-tilted variance, with deterministic Simpson integration. It checks exact compatibility identities, equality at both intended resolutions for a nonconstant smooth periodic factor, a generic third-resolution failure, and the Gaussian closed form \(I_c=c/(a+c)\). Successful finite-precision checks support but do not replace the proof above. Run with `python CHECK.py` using Python's standard library.

## Relationship to prior work
Escudero, Koliander, and Romero [1] derive the fixed-Gaussian-window first-intensity formula and explicitly recognize a two-constant exponential-affine ambiguity **for the smoothed PSD** [1, Remark 5.1]. The one-resolution unsmoothed spectral orbit is also known in subsequent work. The claim here is distinct: it gives an **if and only if classification for the intersection of two different Gaussian-width ambiguity orbits**, identifies the sharp infinite-dimensional Gaussian-periodic exception, and proves generic two-resolution identification up to power. Feldheim [2] derives stationary Gaussian analytic-function zero intensities from spectral measures but does not state the two-resolution inverse classification. The exact one-resolution orbit alone does not imply injectivity from a pair of resolutions without the finite-difference and polynomial-growth analysis.

## Limitations
The result assumes strict positivity and continuity of both spectra and global, noiseless knowledge of population first intensities at two widths. It does not address spectral densities with zeros, distributional spectral measures, finite frequency observation bands, measurement error, inverse stability, or higher-order zero correlations. The periodic ambiguity class includes Gaussians (constant \(p\)). Equivalent earlier descriptions under heat-kernel or exponential-family terminology remain an originality risk.

## References
[1] L. A. Escudero, G. Koliander, J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689, first submitted 2026-09-16, especially Theorem 1.1 and Remark 5.1. https://arxiv.org/abs/2609.18689

[2] N. D. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution*, arXiv:1105.3929 (2011), Theorem 1, Theorem 2, and examples. https://arxiv.org/html/1105.3929v3
