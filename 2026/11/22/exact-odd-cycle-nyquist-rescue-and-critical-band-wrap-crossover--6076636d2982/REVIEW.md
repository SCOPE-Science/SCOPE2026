# Self-review

## Correctness — PASS

The kernel is absolutely summable for each integer power at least two. Its discrete Fourier spectrum is the circular periodization of the probability density of a sum of independent uniform variables, with the normalization \(2\pi\). Positivity, circular unimodality, strict open-support counting and the B-spline simplex-edge identity rigorously give the exact rank, sharp strict invertibility thresholds, critical eigenvalue and finite-scale crossover. The separate exact-rational standalone checker verifies thousands of spectra, boundary cases and coefficients. That finite evidence supports, but does not replace, the analytic proof.

## Originality — PASS relative to inspected evidence

The closest primary paper, Pillai (arXiv:2611.08401v1), works with principal finite Toeplitz truncations and Szegő asymptotic quantiles. Its B-spline symbol identity supplies a building block, but its results do not imply exact eigenvalues of a different finite periodized matrix, the parity-dependent rank rescue or the critical finite-grid crossover without new circular-alias and grid-counting arguments. Standard circulant diagonalization and the B-spline edge are acknowledged rather than presented as new. A related cardinal B-spline collocation study concerns an operator with different matrix entries. Searches for equivalent Nyquist/parity and cyclic sinc-power finite-rank statements did not find a complete matching theorem. An older unindexed formulation could still cover some or all of the result.

## Value — PASS

Periodic approximation and cyclic signal processing use genuinely cyclic covariance matrices, not Toeplitz principal blocks. Here the exact rank and least eigenvalue determine the precise stable-versus-singular boundary for all integer powers and all cycle lengths. The odd-only window of strict positivity below the half-circle continuum threshold and the two distinct \(N^{-1}\)-bandwidth crossover laws are natural finite-grid effects, not arbitrary parameter slices. The theorem provides sharp, reusable test cases for circular spectral regularization. It does not extrapolate these conclusions to ordinary finite Toeplitz truncations.

## Residual risks and limits

Potential prior coverage by less searchable work on cyclic covariance kernels or wrapped B-splines remains; the new theorem is therefore a same-model finding, not a certified statement of historical uniqueness. The infinite argument relies on circular-unimodality preservation, justified geometrically by arc-overlap layer cake, and the strict endpoint support of the B-spline; both are explicitly stated in the proof. An independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
