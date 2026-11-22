# Self-review

## Correctness — PASS

The full joint Lévy measure follows by representing each reflected or ordinary signed-rate Gamma component with a Poisson density \(e^{-r}dr/r\), then applying the canonical HBB Fourier–Laplace transform and taking truncated Thorin-measure limits. The Lévy-kernel integrability bounds are uniform and summable under Thorin's logarithmic and inverse-square conditions. Inversion uses the bijection \((\lambda,r)\leftrightarrow(z,y)=(r/\lambda,r/\lambda^2)\), and the given density uses its exact Jacobian. Under absolute first-moment integrability, differentiating the joint transform yields a Stieltjes-transform identity. Injectivity of the Stieltjes transform of a signed, weighted-finite measure proves both directions of the affine conditional regression criterion. Independence and association use respectively the axes condition for infinitely divisible components and positivity of simultaneous Poisson jumps. The standalone finite diagnostic checker verifies transform, Jacobian and balanced-regression identities but does not substitute for the infinite-dimensional analytical steps. The zero-Thorin case is explicitly handled: its second coordinate is deterministic, and slopes are not unique.

## Originality — PASS (best-knowledge, not exhaustive priority certification)

The closest prior source, Kloster, *A characterization and closure property of Thorin's class*, arXiv:2611.01058v1, 2026-10-31, supplies the unique HBB coupling, single-gamma examples, the \(Y\) marginal and a mixed-cumulant formula. The present statement identifies the entire two-coordinate ray Lévy measure and its exact inverse, then classifies every integrable signed Thorin spectrum with affine conditional regression. The latter is not implied by the stated prior marginal and cumulant formulas without the new Stieltjes uniqueness argument. Barndorff-Nielsen–Maejima–Sato (2006) and Torricelli (2025) develop general multivariate Thorin Lévy representations but do not classify the specific HBB conditional regression. Weighted-gamma regression literature about independent variables and ratios is mathematically different. Targeted searches in research records and published literature found no explicitly covering result. Risk: a more general, unlocated conditional regression theorem for common-jump infinitely divisible pairs could imply this specialization.

## Mathematical value — PASS

This is a complete natural structural classification of when the latent positive component of a canonical Thorin representation gives an exactly affine prediction of its signed coordinate. The measure criterion exhibits two qualitatively distinct mechanisms: a one-sided spectrum is rigidly forced to a single rate, whereas two-sided spectra can be continuously distributed and asymmetric while retaining exact affine regression. It also gives a signed-rate spectral inverse from joint jump geometry, a Gaussian-only independence frontier, and positive-dependence results on one-sided supports. The result is not presented as a solution to general multivariate Thorin classification or all conditional-regression problems.

## Limitations and residual priority risk

The affine result assumes finite absolute expected jump sizes in both coordinates; it does not treat arbitrary infinite-mean spectra. Finite checks validate selected identities, not the full theorem; the proof covers general Borel spectra. The 2006 multivariate paper was inspected in available textual sections, not exhaustively across every appendix; a specialized unlocated regression result remains a historical-priority risk. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
