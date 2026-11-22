# Self-review

## Correctness — PASS

The two trial vectors have disjoint support, giving an exactly diagonal Rayleigh--Ritz core. Its positive diagonal gap is \(au+\delta(1-u)\). The Nyström operator is a sum of two orthogonal rank-one contributions, with nonzero eigenvalues \(1-\delta_c(a,u)\) and \(1-\delta\). This directly proves the if-and-only-if switch at \(\delta_c\), the eigenvector identities, the equality multiplicity, and the eigenvalue and angle comparisons. The proof handles every \(a,u\in(0,1)\) and \(\delta\in(0,1-a)\). The standalone exact-rational checker also evaluates 874 admissible parameter cases and one complete rational matrix instance. Those tests are supporting checks, not a replacement for the proof.

## Originality — PASS, with residual historical risk

Nakatsukasa--Tang, arXiv:2605.05043v1/v2, is the direct motivating source. Its leading-eigenvalue ordering theorem is consistent with the present result. It explicitly distinguishes subspace accuracy from accuracy of individually extracted eigenvectors, but does not give this method-specific exact switching curve, the orthogonal-mode branch for arbitrarily accurate trial planes, or the fourfold simultaneous eigenvalue improvement. Haas--Nakatsukasa, arXiv:2506.01207v2, concerns Ritz and singular-value error bounds; the earlier sharp Ritz-vector literature is about different extraction operators. Semantic published-result searches retrieved nearby studies of sketched Ritz eigenpairs and Nyström preconditioner conditioning, but none establishing the present four-mode classification. No search certifies unique historical priority, and an unreviewed specialized source could contain an equivalent example.

## Value — PASS

The exact threshold resolves a concrete, natural methodological boundary: ordered Nyström eigenvalue accuracy need not improve the **correspondingly ordered individual eigenvector**, even when the trial plane and the competing Ritz eigenvector are arbitrarily accurate. The complete two-leakage-mode phase diagram identifies the precise relevant top eigengap scale, \(\delta_c(a,u)\), and separates mode swapping from genuine power-refinement. This is informative for eigenpair labeling near spectral clusters and is not claimed to be a general Nyström failure theorem or a fixed-gap pathology.

## Scope and limitations

The classification is for the specified four-dimensional PSD diagonal family, two-dimensional orthonormal trial plane, and exact arithmetic. The original top eigenvalue stays simple but its gap closes as the trial angle goes to zero in the failure construction. Equal Nyström eigenvalues have nonunique leading eigenvectors. Individual eigenvector ordering is not invariant-subspace ordering. General PSD inputs and floating-point effects remain outside the claim. Independent historical-priority checking and mathematical audit are not performed.

Self-review: passed. Independent audit: not yet performed.
