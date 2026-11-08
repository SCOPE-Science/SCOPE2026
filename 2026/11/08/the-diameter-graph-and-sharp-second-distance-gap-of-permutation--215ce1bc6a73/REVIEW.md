# Self-review

## Correctness — PASS

The statement fixes both the ambient Euclidean normalization and the distinction between the full convex X-ray image and its finite set of permutation X-rays. The proof uses Birkhoff--von Neumann reduction, sharp concentration bounds for nonnegative integer vectors of mass \(k\), exact characterization of near-full anti-diagonal occupancies, and strict convexity to classify diameter pairs in the full polytope. For the finite-image runner-up, every pair not attaining the diameter falls into one of three bounded cases; an explicit permutation realizes the sharp bound. The low-dimensional exceptions are covered. The standalone exact-integer verifier executed successfully with 694,526 assertions, including exhaustive image-pair checks for \(2\le k\le7\), but universality depends on the proof.

## Originality — PASS, provisional historical priority

The motivating full text [1] studies a facet classification of the exact anti-diagonal image, not its Euclidean diameter graph or finite-image second distance. Earlier permutation X-ray investigations [2,3] concern binary feasibility, degeneracy and enumeration. The complete accessible diameter paper [4] measures matrices in the original Birkhoff polytope under matrix norms; an anti-diagonal aggregation changes those distances and is not an isometry. Closest semantically retrieved mathematical results address partial permutohedra, unprojected matching/transportation polytopes, and other metric images, not this statement. Comparisons against additional related geometric statements showed no covering theorem. No search can establish historical uniqueness, and the full text of the closely related 2014 Hankel--Toeplitz paper was not available. Its accessible descriptions suggest a combinatorial focus, but that is not a full-text exclusion. This is the principal residual priority risk.

## Mathematical value — PASS

The source image has complicated, superpolynomially growing facet structure, yet its **complete metric diameter graph** always has at most two edges. The theorem explains that rigidity through extremal anti-diagonal occupancy and distinguishes the metric of the image from the original matrix polytope. The sharp second-distance gap grows linearly as \(2(k-3)\) for distinct projected permutation configurations; this is a quantitative separation theorem for the discrete configurations relevant to permutation tomography and joint laws with uniform marginals. The complete equality classification, explicit witnesses, and finite/continuous distinction make the result a motivated structural contribution, not merely a numerical diameter estimate.

## Scientific limitations and literature risk

The theorem concerns the standard Euclidean norm on **unnormalized** anti-diagonal sums; a different weighting could invalidate the formula. The runner-up gap is not a gap for distances between arbitrary convex combinations. The result does not claim the complete distance spectrum, facet graph, or additional norms. Historical originality is conditional on currently accessible sources; no independent mathematical audit was performed.

## References

[1] P. Chaudhary and K. Khandelwal, *Facets of the X-ray polytope of doubly stochastic matrices*, arXiv:2610.30058v1 (2026-10-21).

[2] B. Li, Y. Liu and Y. Yao, *Binary X-rays of doubly stochastic matrices*, arXiv:2608.01442 (2026).

[3] C. Bebeacua, T. Mansour, A. Postnikov and S. Severini, *On the X-rays of permutations*, arXiv:math/0506334 (2005).

[4] L. Bouthat, J. Mashreghi and F. Morneau-Guérin, *The diameter of the Birkhoff polytope*, Special Matrices 12 (2024), DOI:10.1515/spma-2023-0113.

[5] R. A. Brualdi and E. Fritscher, *Hankel and Toeplitz X-rays of permutations*, Linear Algebra and its Applications (2014), DOI:10.1016/j.laa.2014.02.037.

Self-review: passed. Independent audit: not yet performed.
