# Review of the single-mode spherical kernel construction

## Correctness: PASS

The specified real features are nonzero harmonic homogeneous polynomials of the claimed degrees. Each of four residue-labelled interval families has unbounded consecutive lengths. A finite set of projected nonzero complex nodes is separated by the Vandermonde matrix on a sufficiently long block; the real and imaginary moment systems separately force conjugate-symmetric and conjugate-antisymmetric coefficient sums to vanish. Repeating this for latitude-weighted moments, using the first two degrees at the zero projection, and resolving the at-most-two-point fibres proves the Gram form is strictly positive for every finite site set. The rank-one spectral and non-characteristic conclusions follow from spherical-harmonic orthogonality. The diagnostic script passed 1034 finite assertions; these are not infinite proof certificates.

## Originality: PASS (best-knowledge)

Jäger's 2020 non-isotropic coefficient theorem, Buhmann–Jäger's 2022 sufficient criteria, and Guella–Jäger's 2022/2023 general characterization were compared at their hypotheses and implications, not merely their titles. Their abstract strict-positivity tests do not explicitly provide the four real long-block families, and the latter sources' full-block or sparse-omission sufficient conditions do not cover a rank-one positive block in every degree. An explicit construction with two active complex modes per degree does not yield one real active mode per degree by deleting a summand. Targeted terminology and implication searches did not identify exact coverage. A prior undiscovered construction, or a simpler implicit derivation from old theory, remains a genuine priority risk.

## Value: PASS

The exact all-degree harmonic rank is the smallest possible **positive** rank at every degree, while Gram strictness still holds for arbitrarily many sites. This concretely separates finite interpolation from spectral universality and characteristicness; the two different probability densities give an explicit distributional witness. The construction is real, smooth, non-isotropic, and motivated by reducing spherical covariance spectral support, rather than arbitrary finite parameters.

## Limits and closest literature

The result is restricted to the two-sphere. It supplies neither a uniform condition-number bound nor a guarantee for truncations, and makes no claim that every degree must be active for strict positive definiteness. The closest primary sources are arXiv:2005.02798, DOI:10.1007/s00041-022-09913-x, and arXiv:2205.07396. First publication priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
