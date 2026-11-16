# Scientific review

## Correctness — PASS

The normalized Gaussian STFT orthogonalizes the Hermite modes on concentric masks and yields exact incomplete-gamma concentration eigenvalues. The adjacent-eigenvalue integration-by-parts identity proves unimodality across the prescribed band, and hence reduction of the least eigenvalue to the endpoint modes. Strict monotonicity of the endpoint ratio gives a unique balance; the unique peak of the upper-order integral proves that the balance is the unique global maximin configuration. Exact Stirling expansion gives the logarithmic second term and the full leading sharp stability constant. The standalone checker independently samples spectra and optimizer comparisons; its finite tests are supplementary.

## Originality — PASS (bounded assessment)

The 2018 Hermite-STFT large-sieve literature motivates the restricted-stability question. The 2019 ring paper supplies the known diagonalization and largest-eigenvalue asymptotics, not the proposed min-over-band optimization. The 2021 STFT Faber–Krahn theorem optimizes the best signal, not the worst prescribed-band signal. The 2024 generalized Daubechies treatment is spectral background. The 2025 radial Toeplitz theorem already handles the two-mode case (first two Hermite modes), which is excluded here; it optimizes the full-operator second eigenvalue rather than the finite-band least eigenvalue for at least three modes. Matching records were not located in the bounded scientific searches. Equivalent terminology and uninspected specialist references remain a priority risk.

## Value — PASS

The exact maximin annulus is a natural sensing-region design solution for guaranteed Gaussian STFT energy on a fixed finite Hermite signal class. The theorem classifies the only least-observable modes at the optimum and determines the high-bandwidth \(1/e\) location, logarithmic drift, and exponentially small sharp floor with its prefactor. The result does not assert general nonradial, arbitrary-set, or varying-area optimality.

## Verification and limits

Run `python3 check_annulus.py` from the package. The script verifies sampled gamma-integral ratios, endpoint dominance and strict off-optimality, plus numerical asymptotics; it does not certify the infinite proof. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
