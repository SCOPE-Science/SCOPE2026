# Self-review

## Correctness — PASS
All nonzero eigenvalues and their spectral projector entries were reconstructed for a star with arbitrary integer leaf count. The unique root follows from the single change of sign of the leaf-pair derivative. Eliminating the strength by the eigenvalue ratio gives a strictly concave logarithmic scalar function, an interior maximizer, and explicit strong and large-star limits. The independent matrix-exponential checker passed 280 matrix/sign comparisons plus optimizer and limiting checks. Numerical tests are corroboration only; the displayed symbolic derivation supplies the universal proof.

## Originality — PASS (bounded historical claim)
Daners–Glück–Kennedy supplies qualitative eventual positivity. Gregorio–Mugnolo contains the pure squared-graph-Laplacian case, including three-site path entries. Published pure biheat complete-multipartite results give the endpoint family, and published sharp spectral-window envelopes optimize over a **larger class of generators**, not over the fixed-star polynomial spectral coupling. In particular for at least three leaves, the star leaf-pair coefficients do not saturate those unconstrained spectral envelopes. None of the inspected results states or implies the exact unique mixed-strength optimizer or its all-star asymptotic. Literature indexing and older differently phrased exact formulae remain residual risks.

## Value — PASS
This is a natural complete classification of the finite positivity-recovery time for the smallest non-Markovian higher-order graph heat family and its full star generalization, not an isolated sampled example. The exact optimizing strength gives a quantitative design worst-case, and the large-star laws identify how the risk window and dangerous strength scale with graph size. The sharp sign change controls whether any nonnegative initial signal can turn negative, a standard semigroup stability issue.

## Limits
Only finite unweighted stars, ordinary counting-space cone order, and the mixed generator \(L+\eta L^2\) are proved. The proof does not address other graph families, and an unindexed historical equivalence has not been ruled out by an independent human bibliographic search.

Self-review: passed. Independent audit: not yet performed.
