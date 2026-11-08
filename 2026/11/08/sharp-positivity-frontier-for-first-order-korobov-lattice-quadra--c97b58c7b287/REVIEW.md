# Scientific review: sharp positivity frontier for first-order Korobov lattice quadrature

## Correctness — PASS

The proof uses the exact Fourier normalization \(K_\gamma=1+2\pi^2\gamma B_2\) and the exact sine-periodization probability density. The variational Euler equation identifies the kernel interpolant as a periodic linear interpolant with one common bubble correction. The Fourier signs of the density and the nonnegative Fourier multipliers of the hat function prove the global least-weight location for every grid size. Evaluation of the bubble integral and a strictly positive threshold denominator yield an all-grid, necessary-and-sufficient condition. The \(N\to\infty\) statement follows from explicit Taylor expansions. `verify.py` independently tests the source kernel linear system and segmented quadrature at 44 parameter combinations. The script is supplementary; it does not certify the infinite quantifier.

## Originality — PASS (best-knowledge, with priority risk)

The principal full text arXiv:2610.01113v1, especially Sections 2.1, 3.1–3.3 and 7.2, provides the method but neither the explicit endpoint-weight frontier nor its \(N+\pi^2/3\) law. The primary full text arXiv:1812.08509v2 establishes conditions under total positivity and locally optimized designs, not this fixed nonuniform-density lattice with a possibly sign-changing kernel. arXiv:2506.07729 concerns lattice approximation rates, not these quadrature weights. Searches for periodic spline/kernel quadrature positivity, Korobov weights and the specific sine periodization, along with comparisons against accessible mathematical findings, produced no covering implication. Older spline/product-integration literature is a remaining priority risk; search failure is not a uniqueness proof.

## Value — PASS

The threshold is a natural numerical-stability boundary for a directly defined family of quadrature rules: it determines exactly when a strictly positive input can receive a negative integration coefficient at the unique endpoint, and when every coefficient is guaranteed positive. The unexpectedly simple linear sample-size scaling and the odd/even finite-grid effect give actionable parameter information; the source identifies positivity as a methodological concern but does not settle even this one-dimensional baseline. The result is a complete classification, not an arbitrary finite instance or a generic interpolation restatement.

## Scope and remaining risk

First-order Korobov smoothness, one dimension, all full cyclic grids with \(N\ge2\), one specified sine-periodization density, exact arithmetic, no weight correction. No assertion for multivariate or subsampled methods, higher kernel smoothness, or independent certification.

Self-review: passed. Independent audit: not yet performed.
