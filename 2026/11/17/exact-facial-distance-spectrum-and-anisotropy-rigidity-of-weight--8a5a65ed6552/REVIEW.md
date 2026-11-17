# Scientific review

## Correctness — PASS

The result defines both the face-complement distance and the fixed Euclidean metric. A missing coordinate places the origin in the complement and forces all included coordinate differences to retain their signed magnitude; sharp weighted Cauchy–Schwarz gives every nonfacet distance. The complementary set of a facet is its opposite facet, where convexity gives exactly twice the facet's minimum norm. Strict optimization over included index sets and a separate facet comparison classify all global minimizers. Vertex-pair distances give the exact diameter. Eight numerical instances with 712 independently optimized pairs corroborate the formulas, but the proof (not the numerics) establishes all positive weights and all dimensions.

## Originality — PASS (provisional historical priority)

The closest directly relevant primary paper is Peña–Wirth, *Calculus of the Facial Distance* (arXiv:2608.28971), inspected in full at Definition 2.1, Section 5 and Example 6.2. Its Example 6.2 **already proves** the unweighted \(\ell_1\)-ball formula, and that case is excluded from the new contribution. Its Corollary 5.2 only bounds facial distance under arbitrary invertible maps using operator norms; its Example 7.4 concerns a nonorthogonal three-dimensional perturbation. Neither gives exact diagonal-weight all-face distances, minimizing-face classification, or strict anisotropy-rigidity identities. Exact published-finding corpus searches and mathematical-literature searches for weighted orthogonal cross-polytopes, anisotropic \(\ell_1\) balls and diagonal transforms found no equivalent published theorem; the closest published-finding corpus records concerned hypersimplex facial distances and weighted \(\ell_1\)-ball projections. A later 2026 paper on normalized facial distance by Deza et al. has a stronger global extremal statement, but that statement does not determine this within-family metric spectrum. Historical priority is not certified; an unindexed derivation under an equivalent description remains possible.

## Mathematical value — PASS

Facial distance / pyramidal width is an established quantitative condition measure for variants of the Frank–Wolfe method, and anisotropic axis scalings are natural in applications. Euclidean facial distances do not survive these affine changes of variables. Determining every face distance, the sharp bottleneck support and its exact multiplicity, and the unique aspect-ratio optimizer provides a complete, dimension-uniform metric classification rather than a recomputation of the regular case or just an operator-norm bound.

## Limits and closest literature

The result is restricted to orthogonal positive diagonal stretches in the fixed Euclidean metric. It does not handle arbitrary non-orthogonal affine cross-polytopes. Peña–Wirth (arXiv:2608.28971, especially Example 6.2 and Corollary 5.2) is the closest inspected full text. Deza et al. (arXiv:2609.32440) was inspected at the abstract but not in full; the residual search risk and absent independent validation are not disguised.

Self-review: passed. Independent audit: not yet performed.
