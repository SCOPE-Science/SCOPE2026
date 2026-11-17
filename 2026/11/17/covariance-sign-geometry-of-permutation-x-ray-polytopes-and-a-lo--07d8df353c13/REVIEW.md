# Scientific assessment: covariance sign geometry of permutation X-rays

## Correctness

**PASS.** The covariance of permutation indicators is reconstructed from the four cases for cell coincidences and summed over anti-diagonals. On one side of the center the row intervals are nested and the off-diagonal numerator is strictly negative; across the center the overlap is the explicit positive part of \(a+b-k\), so the correlation threshold reduces exactly to \((2k-a)(2k-b)=2k^2\). Each positive cross pair is counted by a strict integer threshold, yielding the ceiling sum. Its Riemann limit proves the claimed \(1-\log2\) density. The kernel proof uses all adjacent two-row, two-column permutation swaps, and the trace follows from exact sums of anti-diagonal lengths. An independent finite enumerator passed 662674 exact checks; the infinite conclusions rest on proof, not enumeration.

## Originality

**PASS, provisionally.** The closest source [1] establishes the X-ray polytope and its affine hull and studies facets; the complete X-ray sign kernel and correlation-pair density are not among its statements. The foundational X-ray-permutation source [2] concerns enumeration, and the published diameter finding [5] concerns pairwise distances, not probability-weighted covariance of permutation images. The general permutation-indicator covariance identity is known and credited. The new classification requires identifying anti-diagonal row overlaps, their opposite-side sign boundary, and a complete counting limit, not merely relabeling a previously classified distribution. The older Hankel/Toeplitz paper [4] was not accessible in full, so exhaustive historical priority is not asserted.

## Value

**PASS.** The natural canonical distribution on the newly investigated X-ray polytope is induced by uniformly sampled Birkhoff vertices. Its coordinates are constrained by two affine conservation laws, yet their mutual dependence is not uniformly negative: a curved region of positive correlations survives between opposite tails, occupying asymptotically exactly \(1-\log2\) of all unordered coordinate pairs. This provides a complete, order-uniform dependence classification and a nontrivial quantitative limit for a natural polytope representation, beyond its facet and diameter data. The result is sensitive to the sampling convention, which is expressly stated.

## Scope and remaining risk

The proof covers all integer orders at least two and no uniform-volume interpretation. The full text of [4] and some unindexed discrete-tomography literature remain possible historical-priority risks. The closest modern paper's full accessible HTML and the older arXiv X-ray paper were inspected in their relevant sections; publication priority is therefore provisional.

Self-review: passed. Independent audit: not yet performed.
