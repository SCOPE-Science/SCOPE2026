# Scientific assessment: sharp zero-intensity tails at infinitely flat spectral edges

## Correctness — PASS

The claim is limited to bounded, nonzero, compactly supported, nonnegative spectral densities of pure circular complex stationary Gaussian noise. The known intensity formula, differentiated without boundary terms, yields the exact identity \(\rho_S(\omega)=4\pi\operatorname{Var}_{\mu_\omega}(X)\). Exponential tilting recovers the essential support endpoints and proves the total-bandwidth law. For algebraic edges, the three requisite tilted moments follow from Gamma integrals; for infinitely flat edges, the unique saddle has position \((\kappa\beta/t)^{1/(\beta+1)}\) and variance width \(\sqrt{u_t/((\beta+1)t)}\). A uniform rescaled-Laplace argument controls the first two centered moments, not merely their mode. The normalization \(t=4\pi|\omega|\) gives the stated sharp constants. Direct numerical integrations from `CHECK.py` passed for three flatness exponents and checked the independent opposite-edge algebraic law. They corroborate but cannot replace the general proof.

## Originality — PASS relative to inspected sources

Escudero–Koliander–Romero [1] derive the pure-noise Gaussian-spectrogram intensity and a separate slow-decay theorem. Their asymptotic theorem assumes a global positive sub-Gaussian lower spectral bound and does not treat compact cutoffs. Feldheim [2] supplies the earlier stationary-Gaussian-analytic-function logarithmic-derivative formula and a Paley–Wiener box spectrum; it therefore already covers the general intensity identity and the specific constant-spectrum interval. Neither inspected result supplies the sharp continuously varying exponent \((\beta+2)/(\beta+1)\), its coefficient, or the integrated tail law for a spectrum vanishing faster than every algebraic order at a band edge. Earlier intensity formulas are acknowledged, not claimed as new. A non-obvious equivalent treatment in wider stationary-analytic-function or Laplace-asymptotic literature remains the main priority risk. The related exact spectral-equivalence classification addresses identical complete intensity profiles, not infinitely flat spectral-edge asymptotic families.

## Value — PASS

The theorem identifies a qualitative change in how zero intensity extends beyond a compact frequency band: ordinary algebraic cutoffs have an inverse-square tail, whereas infinitely flat cutoffs exhibit every exponent strictly between one and two. Its explicit constants make the order and severity of spectral flatness exactly identifiable from an ideal population tail, while the total zero count retains only bandwidth. This is a natural spectral-diagnostics boundary, not an arbitrarily selected finite parameter or a routine numerical increment. It also supplies a mathematically sharp benchmark for separating slowly decaying colored spectra (asymptotically white zero density) from bandlimited spectra (decaying zero density). This concerns first intensities, not stable or finite-sample inference.

## Closest literature and limitations

[1] L. A. Escudero, G. Koliander, J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (2026-09-16), Theorem 1.1 and Section 4. Theorem supplies the base intensity and noncompact slow-decay comparison.

[2] N. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution*, arXiv:1105.3929 (2011), Theorem 1 and Section 3.1. It is prior coverage of the stationary-GAF intensity identity and the Paley–Wiener special case.

The exact leading laws assume convergent positive endpoint prefactors; oscillating cutoffs are excluded. The claim concerns mean zeros per unit time, not point-process correlations, statistical rates, or a new generic intensity identity. Publication priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
