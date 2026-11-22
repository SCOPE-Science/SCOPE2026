# Scientific review

## Correctness
**PASS.** The normalized full-size one-node Lanczos Ritz value is the arithmetic spectral mean. The Hermite tangent is explicit. The two-eigenvalue minimal polynomial yields an *exact matrix identity* for the residual, and fixed-norm sign probes turn it into a samplewise centered error identity. A one-variable rational function gives all sharp cutoffs, equality cases and the minimal dimension. Exhaustive exact-rational sign tests corroborate both the matrix identity and variance laws. These tests do not replace the proof.

## Originality
**PASS, qualified.** The motivating source specifies the general full-size Hermite-corrected trace estimator and the ordinary Rademacher variance formula, but the examined body does not state the two-level samplewise variance identity, multiplicity-dependent amplification interval, or sharp seven-dimensional crossover. Related inverse-trace deflation, randomized Krylov-aware trace estimation, and diagonal-interpolation methods differ in the approximation whose trace is controlled. The generic control-variate concept and sign-probe variance formula are known. Exact historical priority remains uncertain outside inspected material.

## Value
**PASS.** The new source specifically motivates variance reduction from global Lanczos error correction. The theorem identifies its first finite-dimensional variance-regression boundary, exact all-probe cancellation contrast, and sharp worst amplification across a canonical spectral class. The seven-dimensional example even has a more-than-fourfold reduction in squared total Frobenius norm while Rademacher variance increases, exhibiting why off-diagonal rather than full-norm control matters. It therefore supplies a useful check on when one-node Hermite correction is beneficial, without implying an advantage in computational cost.

## Closest literature and limits
Rinelli--Simunec--Vermeiren (arXiv:2611.18864), Sections 2.6, 3.1 and 4.1, gives the exact error matrix, stochastic correction and general probe variance. Gambhir--Stathopoulos--Orginos (arXiv:1603.05988) studies variance changes from spectral deflation; Chen--Hallman (arXiv:2205.01736) uses randomized block Krylov approximation. The stated comparison is restricted to exact inverse actions, one full-size global step, two-point positive spectra and Rademacher probes. Other matrices, sampling laws, finite-precision computation, and runtime are not covered.

Self-review: passed. Independent audit: not yet performed.
