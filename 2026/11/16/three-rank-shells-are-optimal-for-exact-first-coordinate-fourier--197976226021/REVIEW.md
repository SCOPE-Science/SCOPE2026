# Mathematical review: optimal three-rank-shell Fourier sampling

## Correctness — PASS
For every prime power \(q\ge2\) and \(n\ge2\), the frequency differences among constant and one-entry additive characters have rank at most two. Left-right rank invariance reduces the Gram off-diagonals to two Fourier coefficients. Uniform-kernel counting gives their exact equivalence to \(\mathbb EZ=2-N^{-1}\) and \(\mathbb EZ^2=q+3-2(q+1)N^{-1}+qN^{-2}\), where \(Z=q^{n-\operatorname{rank}(M)}\) and \(N=q^n\). The two-point variance identity forces the second support point \(q+1-q/N\), strictly between consecutive admissible powers, proving the obstruction. Explicit positive weights on \(1,q,q^2\) satisfy the two moments. An independent exact-arithmetic checker verifies the identities and several exhaustively enumerated prime-field cases; finite tests are not used as infinite proof.

## Originality — PASS, with priority limitation
The 2020 rank-orbit Fourier work of Kawamura supplies general transform coefficients but does not present the positive rank-shell design or its sharp rank-stratum minimum. Yang and Honold (2010) study \(k\)-good distributions and minimum individual matrix support; their optimized cardinality and construction statements do not assert the minimum number of distinct rank orbits under left-right invariance. Byrne and collaborators (2023/2024) analyze weighted subspace designs within a different fixed-dimension block framework. Closest published sampling studies of uniform invertible matrices establish nontrivial Gram spectra, rather than an exactly identity Gram via a rank mixture. An older equivalent low-strength rank-metric cubature statement may exist; this risk remains, and independent priority review has not been performed.

## Mathematical value — PASS
The number of rank strata is an intrinsic, symmetry-preserving complexity measure distinct from point support size. Exact orthonormality of the full first-coordinate Fourier band is a natural target for unbiased, optimally stable linear-feature sensing. The theorem completely determines the smallest achievable rank-stratum complexity for every field order and matrix size, supplies constructive strictly positive weights, and proves uniqueness on the canonical three consecutive top-rank strata. This is a structural sharp finite-field design result, not merely a recomputation of a known matrix-rank Fourier coefficient.

## Scientific limits
The lower bound requires bi-invariance and positive weights; neither arbitrary non-invariant measures nor other three-shell choices are classified. The proof is analytical, and the exact checker samples only prime fields of small order while validating symbolic identities for all parameter values. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
