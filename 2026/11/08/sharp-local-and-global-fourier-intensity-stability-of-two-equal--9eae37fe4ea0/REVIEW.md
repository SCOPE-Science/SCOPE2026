# Scientific review

## Correctness — PASS

The global formula follows by Plancherel and by direct evaluation of the self-correlation of one triangular tent, with careful separation of positive and negative lags for all positive gaps. Its strict-increase and plateau ranges are proved by derivatives, and the sharp noise indistinguishability criterion uses the Hilbert-space midpoint argument. Differentiability of the piecewise-linear covariogram in \(L^2\), the two derivative functions, all Gram entries (including the positive cross term), and the eigenvalues are reconstructed explicitly. The standalone checker reports 616 independent deterministic assertions including numerical Fourier quadrature, direct piecewise integration, and finite differences; finite checks do not replace the proof.

## Originality — PASS relative to inspected sources

The closest source is Xia–Xu, arXiv:2606.19855 (2026), whose Theorems 1.2–1.3 concern uniqueness and nonsharp conditional small-error reconstruction for general one- or two-interval indicators. Its Remark 1.5 exhibits large-gap instability without an exact noise radius. Our particular complete global cubic distance, critical noise threshold, and local width–gap Gram spectrum are stronger *quantitative exact invariants*, not consequences of that paper's stated small-error bounds. Grohs–Koppensteiner–Rathmair, arXiv:1901.07911, is a broad survey with no calculation of the same profile. Classical tent-convolution identities themselves are not new. The principal residual risk is equivalent explicit formulae in the older covariogram or experimental Fourier optics literature. Publication-priority certification has not been independently carried out.

## Mathematical value — PASS

The result resolves both local conditioning and the global noise-resolution limit for the canonical two-piece equal-width phase-retrieval geometry. Most notably, it identifies the precise deterministic noise threshold where otherwise distinguishable gap configurations may be arbitrarily far apart, while the local differential remains nondegenerate. The sharp exact modulus gives a usable inverse noise tolerance rather than a nonsharp asymptotic bound. This is a natural full two-parameter stability profile, not an arbitrary finite numerical slice.

## Limits and closest literature

The complete continuous squared-Fourier-intensity norm, positive gaps, and equal widths are essential. No claim is made about reconstruction algorithms, discrete data, unequal widths, or statistical optimality. Direct numerical tests are not proofs for infinitely many widths and gaps. The newest relevant primary text was inspected in its introduction, Theorem 1.3, Remark 1.5 and two-interval proof, and the broad classical survey's Fourier stability discussion was compared.

Self-review: passed. Independent audit: not yet performed.
