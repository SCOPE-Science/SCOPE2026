# Mathematical review

## Correctness — PASS
For each root edge, the four sign evaluations uniquely encode a constant edge sum, two shared vertex-linear coefficients, and one edge-interaction coefficient. An odd linear component forces at least six nonzero sample values, so every minimum-support word is even. If at most two edge sums are nonzero, the complementary complete graph forces all vertex potentials to vanish unless dimension four leaves a bipartite four-cycle. This yields exactly the claimed square supports and counts. The standalone integer checker independently exhausted all 12,950 erasures of cardinality at most four in the 24-cell. Its finite computation is additional evidence, not the reason the dimension-uniform theorem holds.

## Originality — PASS, provisional historical priority
A 2022 spherical-harmonic recovery paper handles random sampling rather than deterministic root-orbit erasures. The 2023 root-system design paper classifies design properties and uniqueness, not the minimum support of the low-degree evaluation code. Two closely related published mathematical records on the 24-cell's exact-degree harmonic spectrum and cuboctahedral quadratic-harmonic erasures were materially compared; the first gives whole-grid one-degree eigenvalues, the second addresses a distinct smaller root configuration. None of their inspected statements implies the exceptional all-dimensional four-erasure classification. The residual risk is an older equivalent in algebraic coding or interpolation matroids.

## Value — PASS
Even though the root systems have substantial sampling redundancy, precisely four missing observations can already destroy a  degree-at-most-two reconstruction. The complete minimum-erasure classification identifies all such configurations, and the extra twelve only in dimension four reveal a sharp graph-theoretic structural exception. This is an exact identifiability result for a natural infinite family of spherical harmonic sampling grids, relevant to robust fixed-node reconstruction, rather than an arbitrary numerical example.

## Limitations
No complete rank formula for erasures of cardinality five or greater and no sharp conditioning constant. Publication priority remains provisional. The integer computation is exhaustive only for the stated finite 24-cell range; the proof supplies the uniform dimension quantifier.

Self-review: passed. Independent audit: not yet performed.
