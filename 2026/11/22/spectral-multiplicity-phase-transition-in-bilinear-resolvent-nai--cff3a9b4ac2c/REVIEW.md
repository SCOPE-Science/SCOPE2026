# Self-review

## Correctness — PASS

The source's exact resolvent decomposition is used with its hypotheses, not inferred from numerical tests. Direct Laplace transformations give the positive scalar kernel; the block Schur complement proves that the unsmoothed matrix coefficient is coercive for interior completions and rank one at the boundary. At the boundary the two exponentially smoothed terms have disjoint wedge supports and codimension-one kernels by the spectral theorem and isolated bottom eigenvalues. Completing indicator-vector sections identifies each pointwise rank with minimal dilation multiplicity. The proof is valid for arbitrary separable Hilbert dimension. `CHECK.py` tests 588 exact rational matrix identities and 24 finite density-rank instances; neither finite test certifies the infinite theorem.

## Originality — PASS, qualified

Tian (arXiv:2611.03081v1) already proves existence, uniqueness, decomposition and the block matrices; it explicitly asks for the minimal dilation's spectral multiplicity in Section 6. The nearby 17 November 2026 publication *A sharp total-variation jump for unique bilinear-resolvent joint measures* analyzes a 2-by-2 rank-drop family and identifies a singular component and variation discontinuity, without the full minimal direct-integral multiplicity function. The assessed claim is the **entire** multiplicity classification, including both wedge fibers in arbitrary dimension. Actual subject, alias, and implication searches against published records and accessible prior claims found no match. An implicit older POVM direct-integral result remains a genuine bibliographic uncertainty; general background was not all read in full.

## Mathematical value — PASS

The theorem addresses a specifically stated open structural question, classifies the minimum multiplicity along all geometric strata, and demonstrates a discontinuous change of spectral type and dimension at the rank-drop boundary. The result is not a recapitulation of existence or a finite-dimensional table.

## Limitations and closest literature

Only Tian's cyclicity/simple-isolated-bottom class is covered, not all POVMs or all positive-completion pairs. The source is J. Tian, *Joint Moments of Bilinear Resolvents* (2026), arXiv:2611.03081v1, Section 5–6; the nearest additional result is the public 2026 study of a sharp total-variation jump in a two-dimensional family. Finite diagnostics supplement rather than replace the proof.

Self-review: passed. Independent audit: not yet performed.
