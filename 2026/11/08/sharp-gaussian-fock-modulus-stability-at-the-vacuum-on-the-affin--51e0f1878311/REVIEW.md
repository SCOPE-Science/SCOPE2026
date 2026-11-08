# Mathematical review

## Correctness — PASS
The Hilbert-space reduction uses the orthonormal basis of the normalized Gaussian Fock space and exactly handles the phase minimization and arbitrary competitor scale. The nontrivial analytic lemma is strict convexity of the constant-second-moment Rician mean; its Bessel derivatives and Riccati subsolution give a global proof, not a numerical extrapolation. The equality classification follows from strict convexity and the unique optimal scale. A standalone script independently checks normalized Gaussian quadrature, the special-function expression and representative bounds. Risk: errors in Gaussian normalization or special-function identities; both are checked algebraically in the proof and numerically with independent quadrature.

## Originality — PASS relative to inspected evidence
The closest 2026 Fock-stability theorem proves existence of an unspecified constant on an infinite-dimensional space; its conclusion is stronger in coverage but strictly weaker in numerical sharpness. The 2026 square-restricted note concerns another nonlinear mapping and cannot imply this exact first-degree constant. A Rice mean formula itself is not an extremal phase-retrieval theorem. Searches for the exact constant, Gaussian affine competitors, phase-retrieval stability and Rician convexity in the research index and public literature did not identify the same optimization. Risk: an equivalent old Gaussian Rice-mean inequality or degree-one example could be present in unindexed work; searches do not certify priority.

## Mathematical value — PASS
The sharp stability constant in the first nontrivial Hermite truncation is a natural baseline for quantitative Gabor/STFT phase retrieval, directly motivated by the recently established qualitative finite local constant on the full Fock space. It distinguishes the exact global worst case from the infinitesimal behavior and identifies every extremizer. Its exact value is not supplied by the general existence theorem or the tabulated Rice mean; the extremal optimization requires a nontrivial strict convexity argument. The result neither extends the global theorem nor asserts a general nonlinear-recovery guarantee.

Self-review: passed. Independent audit: not yet performed.
