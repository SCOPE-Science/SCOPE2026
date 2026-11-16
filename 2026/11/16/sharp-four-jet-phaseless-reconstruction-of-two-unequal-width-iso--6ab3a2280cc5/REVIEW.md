# Scientific review

## Correctness — PASS

The normalized Gaussian Fourier formula yields \(I(\xi)=2e^{-s|\xi|^2}(\cosh(q|\xi|^2)+\cos(h\cdot\xi))\) and the exact quadratic/quartic coefficients. Since \(d\ge2\), the positive semidefinite displacement matrix has rank at most one and a nonzero kernel, so its minimum-eigenvalue shift identifies \(s\) without extra assumptions. Restricting the quartic to the kernel extracts \(q^2\). The converse explicitly constructs a strictly positive-variance mixture from every allowed jet. Rational one-dimensional collision and varying \(q\) prove both sharp boundaries. The supplementary checker uses exact rational arithmetic.

## Originality — PASS, provisional against the inspected corpus

The full Kalavasis–Kothari–Li–Zampetakis Fourier-mixture manuscript studies unphased mixture learning and expressly excludes Gaussians from its main algorithm; its appendix is not an intensity-jet inverse theorem. Xia–Xu uses one-dimensional interval indicators rather than varying-scale Gaussians. Fukunaga–Flick and Agostini–Améndola–Ranestad consider moments of the mixture itself, not the even moment tensors of its autocorrelation. Closest database searches for phaseless Gaussian mixture fourth jets returned results about distinct models (intervals, finite discrete intensity samples, Gaussian-window spectrograms). The exact rank-one feasibility criterion, fourth-order threshold in dimension at least two, and rational one-dimensional alias pair were not covered by the source statements actually inspected. The 1983 manuscript and the Xia–Xu full text were not available in the inspected evidence; equivalence risks remain.

## Mathematical value — PASS

Low-frequency intensity jets are natural observables in phaseless inverse scattering and structured deconvolution. For equal-mass two-scale Gaussians, it is not evident a priori that the unobserved Fourier phase and the two individual variances are determined by only a fourth-order jet. The result classifies the entire realizable data region, handles coincident positions without separation, gives a constructive inversion, proves minimal derivative order, and exhibits a sharp ambient-dimensional failure. These form a natural complete finite-jet classification, not a single unmotivated numerical instance. No noise robustness or arbitrary-mixture claim is made.

## Sources and risks

See the references and limitations in `RESULT.md` and the four implication-based comparisons in `AUDIT.json`. Older phaseless Gaussian autocorrelation literature remains a genuine potential source of an equivalent result, so publication priority is not certified. The primary full-text inspection concerned the 2026 Fourier-mixture paper; the Xia–Xu and Fukunaga–Flick sources were abstract-only. No independent audit has taken place.

Self-review: passed. Independent audit: not yet performed.
