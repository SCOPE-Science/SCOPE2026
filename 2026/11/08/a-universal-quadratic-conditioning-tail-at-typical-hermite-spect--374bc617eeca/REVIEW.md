# Scientific review: Hermite spectrogram zero conditioning

## Correctness

PASS. The real differential of a polyanalytic field at a zero has singular values \(|\partial_z f|+|\partial_{\bar z}f|\) and \(\big||\partial_z f|-|\partial_{\bar z}f|\big|\). The Hermite raising/lowering identities make these two derivative magnitudes independent scaled Rayleigh variables, independent of the field value at the base point. Marked Kac–Rice gives the necessary absolute-Jacobian size bias. The displayed ratio density is obtained by a legitimate two-dimensional change of variables, integrates to one, and yields the exact survival law, the positive sharp quadratic tail, the moment threshold and the explicit limiting law. The finite checker verifies the normalization and rational antiderivatives against direct numerical integration. The theorem does not equate a conditioned base-point derivative with a typical-zero derivative.

## Originality

PASS relative to the inspected published and indexed material. Bellourak et al. (arXiv:2610.13531v1) give local Hermite Gaussian derivatives, charged first and two-point intensities, and a winding-number detection algorithm, but not a distribution of the condition number at a typical zero. Haimi–Koliander–Romero (2022) provide the general Kac–Rice and charge framework, but their first-intensity formula does not directly state the marked ratio distribution or critical moments. Abreu–Shirai (arXiv:2605.17296v1) study correlations across orders, while Feldheim–Haimi–Koliander–Romero (2026) treat spatial count fluctuations. Targeted mathematical-index and literature queries yielded no equivalent statement. The result could be an elementary consequence of a more general marked Rice formula in older literature; this is a residual priority risk, not a claim of independent priority certification.

## Value

PASS. The new observable is the *local numerical conditioning of a typical spectrogram zero*, directly associated with differentiable zero-location and winding-number detection. Almost-sure nondegeneracy alone does not quantify how often zeros are ill-conditioned. The exact power-law tail, its sharp order-dependent coefficient, and the divergence of the second moment despite a finite first moment provide useful quantitative information, while the explicit high-order limiting distribution resolves an entire natural Hermite-order family. No finite-sample detection-performance claim is made.

## Limits

Only single-window stationary complex white noise, normalized local real-Jacobian condition numbers, and the intensity-Palm law are covered. A non-isotropic coordinate change alters condition numbers. Full publication-priority assessment and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
