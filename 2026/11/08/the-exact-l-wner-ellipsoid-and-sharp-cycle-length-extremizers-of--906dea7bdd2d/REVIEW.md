# Scientific review

## Correctness — PASS

The edge roots span the zero-sum space, the weighted Laplacian is positive definite there, and the matrix-tree polynomial factors into one bridge factor and one cycle factor per cactus block. Differentiation at the displayed positive weights gives every squared Mahalanobis root norm exactly one. The weights sum to the intrinsic dimension, furnishing a global trace/determinant certificate against **arbitrarily centered** ellipsoids, with equality only at the stated center and matrix. The weighted matrix-tree normalization includes the factor \(n\) converting a cofactor into the product of the nonzero eigenvalues. For fixed \(n,c\), strict increase and strict log-concavity of \(F(k)\) give both sharp bounds and equality classifications. Exact rational finite checks passed 110 cactus cases and 1,274 edge contacts, plus 75 independent extremal profiles.

## Originality — PASS, with historical-priority risk

The closest primary work by Ohsugi and Tsuchiya (arXiv:2008.08621) studies lattice \(h^*\)-data and normalized volumes of **suspensions**, not optimal Euclidean ellipsoids of the cactus graph itself. D'Alì, Juhnke-Kubitzke, and Koch (arXiv:2307.04933, Theorem 4.6) prove graphic-matroid/unimodular equivalence: this already explains qualitative volume invariance for fixed matroid and dimension, and that subclaim is not presented as newly discovered. Their paper gives no explicit positive cycle weighting, globally unique enclosing Euclidean ellipsoid, contact certificate, numerical outer-volume formula, or fixed-\(n,c\) sharp extremizers. Chen–Davis–Korchevskaia (arXiv:2107.12315) study facets, and Todd's earlier ellipsoid notes give general design duality rather than the cactus application. Published mathematical-record comparisons include wheel and other graph-root Löwner ellipsoids, but no inspected claim covers this cactus formula. A nonindexed earlier explicit D-optimal cactus allocation is possible.

## Mathematical value — PASS

Minimum-volume enclosing ellipsoids are canonical affine-covariant approximations; their shapes provide quantitative effective-resistance/contact data and their volumes provide a metric functional of the graph-root polytope. The entire infinite cactus family is solved by two local weight rules, and the sharp extremes at prescribed \(n,c\) exhibit a nontrivial increasing, strictly log-concave dependence on cycle lengths. This is a natural complete classification, not an arbitrary finite sample or a minor numerical improvement. The cycle-attachment independence and extremal equality cases are usable directly to compare polytope families.

## Scope and limitations

Proof completeness was assessed for the stated canonical Euclidean embedding, including trees, shared cut-vertices between cycles, the minimal feasible order, and unrestricted ellipsoid centers. It does not apply to overlapping-edge cycles or weighted generator configurations. The included finite checker corroborates but does not prove all orders. The prior-literature search is not a mathematical proof of priority; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
