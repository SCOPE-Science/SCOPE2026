# Review of rectangular Monge incenter-cube theorem

## Correctness — PASS
The affine Frobenius facet normal lengths are \(\sqrt{1-1/(pq)}\) and \(2\), respectively, yielding the exact ball-containment LP. The explicitly proved comonotone-coupling identity has positive weights \(\min(aq,bp)-ab\) and gives the globally sharp radius bound. The coefficient sum is evaluated by elementary quantile covariance and sawtooth orthogonality. Constructed dual potentials attain every required equality. All equalities in the sharp bound are used to classify **all** centers; the \(\gcd(p,q)-1\) free common partition boundaries form an affine cube. The count of tangencies follows from exact overlap and endpoint zero patterns. The in-package exact checker covers 576 rectangular parameter pairs and 4390 cube corners, with an optional 64-case independently optimized Frobenius LP. These are finite checks, not an infinite proof.

## Originality — PASS for unequal sizes, with priority risk
The 2023 original Monge paper proves the H- and V-representations and a two-row volume formula, not inradii. The already published 2026 **square** incenter theorem has the diagonal specialization and is expressly excluded from novelty; it neither states nor implies the unequal-size arithmetic \(\gcd(p,q)^2\) radius term and \(\gcd(p,q)-1\) center-cube dimension without further argument. The new theorem adds a sharp comonotone-transport certificate valid across the full rectangle family. Searches for Monge Chebyshev centers, gcd inradii, transportation coupling and equivalent facet formulations returned no stronger covering theorem. The 2026 lattice-path Monge volume paper could only be checked by abstract, leaving explicit residual risk; novelty is best-knowledge, not a priority certificate.

## Mathematical value — PASS
An exact inradius and the complete optimal-center locus are intrinsic geometric invariants of the Monge cost-matrix section. The arithmetic phase distinction is substantial: coprime dimensions have a unique center, while any common divisor produces a positive-dimensional cube; the full tangent-facet count also changes at cube boundaries. This is a natural complete classification for all unequal rectangular sizes, not an arbitrary numerical slice or a renaming of the known square case. It explains how the combinatorial overlap geometry of two uniform partitions controls the convex body's Euclidean centers.

## Limitations
Only the sum-one nonnegative Monge section in its inherited Frobenius metric is treated; no assertion for fixed margins or arbitrary affine changes of metric. The inaccessible full text of the 2026 lattice-path volume work leaves a bounded historical-priority risk. The proof is analytical; finite checks do not constitute independent validation.

Self-review: passed. Independent audit: not yet performed.
