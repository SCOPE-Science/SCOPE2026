# Independent mathematical audit

## correctness

PASS

The DCT-I orthogonality identity with endpoint weights w0=wN=v0=vN=1/2 gives full (N+1) orthogonal Q. Two-row/two-last-column block partition identifies the N−3 unit singular squares of the surviving (N−1)×(N−1) matrix and the two eigenvalues of BᵀB. The deleted-row block has vectors (−1)^j√(2w_j/N)(x_j,1/√2), yielding trace 2t/N and determinant 2w_jw_l(x_j−x_l)²/N² and positive eigenvalues for distinct nodes. Lower bound μ−≥2w_jw_lΔ²/[3N(w_j+w_l)] for every pair, combined with Rayleigh upper bound μ−_{0,1}≤2δ²/(3N), and cosine-grid spacing (>2δ between interiors, >3δ non-nearest endpoints, Δ=2 between endpoints), strictly rules out every erasure except endpoint neighbors. Reflection ties two patterns. Exact formula α=(t−√(t²−δ²))/N with t=5/4+c², δ=1−c yields α~π⁴/(18N⁵), κ=1/α~18N⁵/π⁴. Independent SVD and formula agree for all erased pairs at N=4,5,8,16,32 and locate same optimizers; tests are finite corroboration, proof all N analytical.

## originality

PASS

Best-of-knowledge original scope after positive mathematical implication comparisons, not inferred from mere negative search. Neither prior formula can be substituted into present operator without changing sampling grid, weights and column dimensionality; the exact spectra and exponent are genuinely different. Generic singular-value identities and image-coding literature are relevant methodological background, not an inspected theorem dominating the sharp minimizer for this exact grid. IEEE full text still inaccessible, recorded as risk. Present global two-erasure DCT-I lower spectral bound is not a corollary of the inspected neighboring results; an inaccessible 2021 IEEE DCT source could alter priority assessment, not correctness.

## value

PASS

Sharp loss-of-two-data stability for a natural quadrature-orthogonal interpolation grid identifies the unique bad missing-node geometry and the exact polynomial blowup of energy conditioning. This complements, rather than renames, known single deletion Lebesgue growth and near-Nyquist half-shifted cosine results; researchers assessing erasure resilience could need the precise DCT-I weighted constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
