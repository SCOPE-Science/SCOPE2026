# Review of the two-circle positive-semidefinite fiber theorem

## Correctness
PASS. The five-point Fourier inversion proves a one-dimensional Hermitian kernel with explicitly invertible generator. The two-negative-direction argument rules out negative kernel parameter, and a positive-definite principal block plus Schur complement proves the complete positive-parameter interval, including its rank transitions. A separate scalar evaluation proves exact one-sample completion. The Gaussian-STFT reduction is an exact Gaussian-integral identity. The standalone numerical tests independently reconstruct the measurement matrix and quadrature; finite testing is corroboration rather than proof.

## Originality
PASS relative to the inspected primary literature and searched mathematical record. The original 2026 STFT two-window study treats different sampling assumptions; the 2024 two-circle analytic work already supports rank-one uniqueness. The present claim is the exact **positive-semidefinite mixed-rank fiber**, its sharp coefficient cone and endpoint ranks, together with a minimal one-sample Hermitian completion. The 2016 strictly-complete tomography work supplies the general notion, while the 2024 Gabor-semidefinite paper concerns general reconstruction and matrix-completion methods, not this two-circle three-tone classification. Search and literature comparisons did not show full implication of the new exact statement. Risk: an equivalent degree-two truncated moment or complex polynomial covariance calculation may have been published under older terminology; independent priority review has not occurred.

## Mathematical value
PASS. Distinguishing pure-signal uniqueness from positive-semidefinite lifting uniqueness is necessary for interpreting convex phase-retrieval reconstructions. The result identifies exactly which three-tone signals admit spurious higher-rank PSD reconstructions, their complete feasible segment, and the smallest additional measurement that resolves the defect. A trace-one, orthogonally supported ambiguity demonstrates a substantive obstruction rather than merely infinitesimal nonuniqueness. The result is limited to degree two, specified grids, and noiseless samples; no stability claim is made.

Self-review: passed. Independent audit: not yet performed.
