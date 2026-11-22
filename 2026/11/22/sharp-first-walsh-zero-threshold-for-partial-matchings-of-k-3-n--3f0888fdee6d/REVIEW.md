# Scientific review of the sharp partial-matching Walsh threshold

## Correctness

**PASS.** The matching total is \(N_n=n^3+2n+1\); the number containing any fixed edge is \(Q_n=n^2-n+1\). The union estimate \(W_n(S)\ge N_n-2|S|Q_n\) proves strict positivity through degree \(r=(n+1)/2\) for odd \(n\), with equality \(2n\) on row stars. Parity proves invertibility for even \(n\). Appending one edge in a second row but a column already in the star causes exactly a signed decrement of \(2n\), yielding a zero. Uniqueness of the heavy row when \(r\ge2\) proves the stated constructed-zero count. Both independent exact-integer programs pass; finite tests are not substituted for the general argument.

## Originality

**PASS under bounded search.** Rectangular rook coefficients supply unsigned matching totals, while the matching-polytope and multivariate matching polynomial literature inspected have different statements and do not imply the all-width sharp Fourier-zero degree. Previous fixed-board complete-bipartite matching calculations do not imply this uniform threshold, and a spanning-tree Fourier result uses a different configuration family. Multiple indexed searches for Walsh matching sums, signed rook cancellations, and \(K_{3,n}\) found no logically dominating theorem. A possible unindexed signed-rook theorem remains a residual priority risk; this review does not establish absolute novelty.

## Value

**PASS.** The first Walsh zero is the exact boundary of faithful low-degree recovery under a natural matching-constrained convolution channel. The parity split between even and odd board widths, the strictly positive edge-frequency gap through the maximal recoverable degree, and a large explicit family of first lost modes determine a structural recovery threshold across an infinite family; this is not merely an unsigned rook polynomial recount.

## Limits and closest prior literature

The count of constructed zeros is a lower bound rather than a complete first-zero census. The full odd-width nullity is not determined. Relevant literature: Weisstein's rectangular rook polynomial exposition; Walter, arXiv:1607.01880; Leake–Ryder, arXiv:1610.00805. Priority outside the indexed and inspected literature remains open.

Self-review: passed. Independent audit: not yet performed.
