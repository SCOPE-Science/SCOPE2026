# Exact ambiguity orbits and tail rigidity for Gaussian-spectrogram zero intensities

## Finding

Consider stationary, circularly symmetric complex Gaussian noise with a nonzero power spectral density (PSD) \(S:\mathbb R\to[0,\infty)\), measurable and bounded almost everywhere by \(C(1+|x|)^m\) for some \(C,m<\infty\). Its Gaussian-window short-time Fourier transform (STFT) uses the normalized window \(\varphi(t)=2^{1/4}e^{-\pi t^2}\). Define
\[
P_S(\omega)=\int_{\mathbb R}e^{-2\pi(\omega-x)^2}S(x)\,dx,
\qquad
\rho_S(\omega)=1+\frac{1}{4\pi}\frac{d^2}{d\omega^2}\log P_S(\omega).
\]
Here \(\rho_S\) is the expected number of STFT zeros per unit area at frequency \(\omega\), independent of time, in the pure-noise model. Its identification with the spectrogram-zero intensity is the established colored-noise formula [1, Theorem 1.1 and equation (4.1)].

**Exact intensity-fiber theorem.** For any two such PSDs \(S,T\), the equality \(\rho_T(\omega)=\rho_S(\omega)\) for every \(\omega\in\mathbb R\) holds if and only if there are constants \(a\in\mathbb R\), \(C_0>0\) such that, almost everywhere,
\[
\boxed{T(x)=C_0\exp\!\left(ax-\frac{a^2}{8\pi}\right)
S\!\left(x-\frac{a}{4\pi}\right).}
\tag{1}
\]
The right-hand side must of course itself be an admissible polynomially bounded PSD. In this normalization \(P_T(\omega)=C_0 e^{a\omega}P_S(\omega)\) exactly.

**Two-sided-tail rigidity.** If, in addition, \(S(x)\ge c(1+|x|)^{-M}\) for almost every sufficiently large positive and negative \(x\), for some \(c>0,M\ge0\), and \(T\) remains polynomially bounded, then equality of zero intensities forces \(a=0\), hence \(T=C_0S\) almost everywhere. Thus a polynomially lower-bounded spectrum is identifiable up to its unavoidable overall power scale from its entire expected Gaussian-STFT zero-density profile, with no externally supplied logarithmic-slope normalization.

The two-sided tail hypothesis has real content. For \(S=\mathbf1_{[-1,1]}\), every real \(a\) gives another admissible PSD via (1). If \(|a|>8\pi\), the supports of \(S\) and \(T\) are disjoint, and the distance between them can be arbitrarily large, yet their expected spectrogram-zero density profiles agree *at every frequency*. These are different stationary noise spectra, not different descriptions of the same spectrum.

**Homogeneity rigidity.** Among all nonzero polynomially bounded PSDs in this theorem, \(\rho_S\) is constant if and only if \(S\) is almost everywhere either a positive constant or a Gaussian \(C_1e^{-b(x-\mu)^2}\) with \(C_1,b>0\), \(\mu\in\mathbb R\). The respective constant intensities are
\[
\boxed{\rho_S\equiv1\quad\text{and}\quad
\rho_S\equiv\frac{2\pi}{2\pi+b}.}
\tag{2}
\]
In particular, no admissible PSD has identically constant intensity larger than \(1\) or equal to \(0\). The forward centered-Gaussian example was already known [1, Proposition 1.3]; the converse is part of this classification.

## Assumptions and scope

The model is *pure stationary colored Gaussian noise*, with no deterministic signal added; the Gaussian analysis window and Fourier-frequency normalization are fixed as above. All PSD equalities are almost-everywhere equalities of functions. The PSD need not be smooth, integrable or bounded away from zero. It is required to be nonnegative, nonzero on a set of positive Lebesgue measure and polynomially bounded. Gaussian smoothing makes \(P_S\) positive and real analytic. The conclusions concern equality of *first intensities of zeros*, not equality of all joint zero-process laws and not deterministic signal recovery.

## Proof

**1. Reduction to an affine logarithmic gauge.** Since \(P_S,P_T>0\), equality of the displayed zero-intensity functions is equivalent to \((\log P_T-\log P_S)''\equiv0\). Two integrations give \(P_T(\omega)=C_0e^{a\omega}P_S(\omega)\) with \(a\in\mathbb R,C_0>0\). The converse of this reduction is immediate.

**2. Recovering the unsmoothed spectrum.** Define positive finite measures
\[
\mu_S(dx)=e^{-2\pi x^2}S(x)\,dx,
\qquad
\mu_T(dx)=e^{-2\pi x^2}T(x)\,dx,
\]
with bilateral Laplace transforms \(F_S(z)=\int e^{zx}\,\mu_S(dx)\), and similarly for \(T\). Polynomial growth times a Gaussian implies that these functions are entire, by dominated convergence on each compact subset of \(\mathbb C\). Completing the square gives
\[
P_S(\omega)=e^{-2\pi\omega^2}F_S(4\pi\omega).
\]
It follows from the affine logarithmic gauge that for every real \(z\),
\[
F_T(z)=C_0 e^{(a/(4\pi))z}F_S(z).
\]
The identity theorem extends this equality to complex \(z\). At purely imaginary \(z\) it says that the Fourier transform of \(\mu_T\) equals that of \(C_0\) times the translate of \(\mu_S\) through \(d=a/(4\pi)\). Uniqueness of Fourier transforms of finite Borel measures yields \(\mu_T=C_0(\tau_d)_\#\mu_S\). Substitution into the positive densities gives
\[
T(x)e^{-2\pi x^2}
=C_0S(x-d)e^{-2\pi(x-d)^2},
\]
which is precisely (1), because \(4\pi d=a\) and \(2\pi d^2=a^2/(8\pi)\). Conversely direct Gaussian completion of squares establishes \(P_T=C_0e^{a\omega}P_S\) whenever (1) defines an admissible \(T\). This proves both directions, including normalization.

**3. Polynomial-tail rigidity and sharp failure.** Suppose \(S(x)\ge c(1+|x|)^{-M}\) for almost every \(|x|\ge R\). If \(a>0\), equation (1) makes \(T(x)\) grow at least as an exponential times an inverse polynomial as \(x\to+\infty\), contradicting polynomial upper growth. If \(a<0\), use \(x\to-\infty\). Thus \(a=0\). Conversely, for the compactly supported band \(S=\mathbf1_{[-1,1]}\), the right-hand side of (1) is a strictly positive exponential weight on the interval \([d-1,d+1]\) and zero outside, hence is admissible for every real \(a\). Those intervals are disjoint from \([-1,1]\) whenever \(|d|>2\), or \(|a|>8\pi\).

**4. Homogeneous-intensity converse.** One more differentiation identity gives a useful positive probabilistic representation. Let \(X_\omega\) have the probability density proportional to \(S(x)e^{-2\pi(x-\omega)^2}\). Differentiating the Gaussian convolution twice shows
\[
\rho_S(\omega)=4\pi\operatorname{Var}(X_\omega)>0.
\tag{3}
\]
Strict positivity holds because the measure has an absolutely continuous nonzero density, not a point mass. If \(\rho_S(\omega)\equiv r\), then integration yields \(\log P_S(\omega)=2\pi(r-1)\omega^2+A\omega+B\) for real \(A,B\). Consequently the Laplace transform of \(\mu_S\) has the form
\[
F_S(z)=e^B\exp\!\left(\frac{A}{4\pi}z+\frac{r}{8\pi}z^2\right).
\]
By uniqueness of moment-generating functions, \(\mu_S\), normalized to mass \(e^B\), is Gaussian with mean \(A/(4\pi)\) and variance \(r/(4\pi)\). Undoing the factor \(e^{-2\pi x^2}\) shows that \(S(x)\) is proportional to
\[
\exp\!\left(-\frac{2\pi(1-r)}r x^2+\frac{A}{r}x\right).
\]
Polynomial upper growth forbids \(r>1\), and for \(r=1\) forces \(A=0\) and constant \(S\). For \(0<r<1\) this is a positive Gaussian of precision \(b=2\pi(1-r)/r\), with arbitrary center. The forward computation follows by convolving Gaussians, recovering (2). The case \(r=0\) was already excluded by (3).

## Verification

The standalone Python 3 script `CHECK.py` independently evaluates Gaussian convolutions by numerical quadrature for Gaussian, rational-tail and compact-band PSDs and their transforms (1), tests the predicted exponential ratio across multiple frequencies and deformation parameters, checks Gaussian constant-intensity values, and compares (3) against finite-difference logarithmic derivatives for a rational-tail PSD. It terminates with `ALL_COLORED_NOISE_FIBER_CHECKS_PASSED` on success. These checks are finite numerical corroboration; the unrestricted classification follows from the analytic measure-transform proof above.

## Relationship to prior work

Escudero, Koliander and Romero [1] proved the colored-noise first-intensity identity used here, and their Remark 5.1 correctly observes the two-constant affine ambiguity at the *smoothed PSD* level. They also computed the forward centered-Gaussian homogeneous-intensity example. This result does not claim those formulas as new: it identifies the exact corresponding ambiguity orbit of the *unsmoothed, admissible* PSD, proves its collapse under a two-sided polynomial lower tail, constructs disjoint-band counterexamples, and establishes the converse classification for homogeneous intensity. The white-noise Bargmann-zero methods of Escudero, Feldheim, Koliander and Romero [2] concern a different stochastic input class; earlier zero-intensity work of Haimi, Koliander and Romero [3] concerns Weyl-Heisenberg-invariant fields and general windows rather than this colored-PSD inverse fiber.

## Limitations

The conclusion concerns population first-intensity functions known on the *entire continuous* frequency line; it does not provide a stable finite-sample PSD estimator. Gaussian deconvolution is ill-conditioned, and first-intensity equality does not imply equality of the full point-process law. The positive multiplicative PSD scale cannot be inferred from zeros. For spectra with sufficiently rapid decay, the affine orbit may remain nontrivial; the polynomial-tail hypothesis is only a sufficient identifiability condition, not a necessary characterization of all singleton orbits. Historical specialty literature under exponential-family or heat-kernel identifiability terminology remains an originality risk. No independent mathematical audit has been performed.

## References

[1] L. A. Escudero, G. Koliander and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689, first publicly posted 2026-09-16. In particular Theorem 1.1, equation (4.1), Proposition 1.3 and Remark 5.1. https://arxiv.org/abs/2609.18689

[2] L. A. Escudero, N. Feldheim, G. Koliander and J. L. Romero, *Efficient Computation of the Zeros of the Bargmann Transform Under Additive White Noise*, first published 2022-09-27, *Foundations of Computational Mathematics* 24 (2024), 279–312. https://pmc.ncbi.nlm.nih.gov/articles/PMC10879403/

[3] A. Haimi, G. Koliander and J. L. Romero, *Zeros of Gaussian Weyl-Heisenberg Functions and Hyperuniformity of Charge*, arXiv:2012.12298 (2020), *Journal of Statistical Physics* 187 (2022). https://arxiv.org/abs/2012.12298
