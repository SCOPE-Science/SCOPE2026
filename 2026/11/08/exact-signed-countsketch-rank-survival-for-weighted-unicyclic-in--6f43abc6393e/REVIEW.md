# Scientific assessment of the exact unicyclic CountSketch rank law

## Correctness — PASS

For each finite connected unicyclic graph, deleting one vertex column gives a rank-\(n-1\) weighted incidence matrix. Its column space is the orthogonal hyperplane to the reciprocal-weight cycle circulation. The sketch has kernel dimension \(n-u\), with \(u\) the number of occupied buckets. Consequently only collision-free hashings and hashings with a single doubleton can preserve full rank. In the latter case the one-dimensional kernel test gives the sign-averaged weights \(0\), \(1\), or \(1/2\) depending on whether two off-cycle edges, a mixed/differently weighted cycle pair, or an equally weighted cycle pair collide. Disjoint hashing event counts prove the theorem for every admissible graph and sketch size. Completing a square and taking discrete increments prove the optimizer classifications. Weyl's singular-value inequality proves the scale-perturbation conditioning limitation.

Exact-Fraction brute-force rank elimination verified all bucket/sign outcomes in 27 small scenarios, supplemented by 3,780 seeded structural checks and 94 finite discrete-optimizer comparisons. These computations are corroboration, not substitutes for the all-parameter proof. Risks include only the deliberately excluded norm-embedding and finite-precision interpretations; the claim itself is algebraic rank.

## Originality — PASS, with publication-precedence risk

Hu et al., *Sparse graph based sketching for fast numerical linear algebra* (arXiv:2102.05758, 2021), compare CountSketch with other sparse sketches and prove general norm-embedding guarantees; they do not state the exact incidence-matrix collision-pair formula in the inspected manuscript. Clarkson and Woodruff, *Low rank approximation and regression in input sparsity time* (arXiv:1207.6365, 2012), give the one-nonzero CountSketch distribution and general sparse subspace-embedding theory; the inspected sections use collision avoidance rather than a rank-surviving collision enumeration. Woodruff and Kocurek's 2024 lecture note gives a birthday-paradox obstruction for independent input rows, which is not the same as a codimension-one dependent incidence row family. Chen, Khanna and Li, *On weighted graph sparsification by linear sketching* (arXiv:2209.07729, 2022), use graph *incidence sketches* in the sense of linear measurements of edge weights at vertices, distinct from left-multiplication by CountSketch on a weighted incidence matrix. That last comparison is abstract-only and cannot rule out all related material in the full text. Zhao and collaborators (arXiv:1803.09631, 2018) discuss incidence-matrix sparse recovery with cycle-dependent conditions; the abstract describes a different recovery problem, but full-text precedence was not ruled out.

Semantic searches against public mathematical-result summaries returned topics such as graph antisymmetric-adjacency rank enumerators and collision envelopes for limited-independence hash functions, neither of which states the fully independent signed CountSketch law. Searches and the inspected text provide bounded evidence of non-coverage, not a uniqueness certificate. An equivalent formulation in matroid representation, occupancy, or signed-hashing literature remains the principal originality risk.

## Value — PASS

The theorem exactly resolves an identifiable design gap between generic sketch-embedding guarantees and how the sole cycle dependence of graph incidence data interacts with one-bucket collisions. At fixed bucket budget it identifies the best cycle size for equal weights, the different best sizes for pairwise distinct weights, and a discontinuous algebraic-rank effect that disappears as a robustness guarantee. This establishes a mathematically meaningful boundary for rank-only benchmarks and cautions against treating exact rank survival as adequate numerical stability. The numerical example distinguishes two unweighted graph topologies at identical dimensions and shows a factor-two equal-versus-distinct cycle-weight effect.

## Limitations and closest literature

The statement is not a norm-embedding probability, a floating-point rank guarantee, or a result for nonuniform/limited-independence hashes. The full texts of Chen–Khanna–Li and Zhao et al. were not inspected, and specialist matroid/graph-hashing precedence remains uncertain. The paper and code supply no independent scientific verification.

Self-review: passed. Independent audit: not yet performed.
