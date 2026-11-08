# Self-review

## Correctness
**PASS.** In order of unit-interval left endpoints, nonconsecutive overlaps would create a triple intersection, so the overlap graph is a union of paths. The only possible point-order inversions are disjoint adjacent edges; every edge matching is realizable. The sharp word lemma is proved by an explicit recursive upper construction and a two-case induction on the occurrence count of the last label. Projection to each component proves an additive lower bound. The exact domain includes singleton components and coincident pair intervals. The standalone checker verifies 255 overlap masks, 1,930 composite orders and exact breadth-first minima through path size six. These finite checks support, but do not substitute for, the proof for all sizes.

## Originality
**PASS within available evidence; residual priority risk.** In *Preprocessing Uncertain Data into Supersequences for Sorting and Gaps* (arXiv:2601.19453), Lemma 13 supplies a \(4\Delta n\) upper bound for unit intervals, not the exact ply-two minimum, and its Theorem 5 additionally imposes smoothness. The related 2025 convex-hull paper arXiv:2502.03633 repeats the broader supersequence bound in Lemma 34. A classical arbitrary-permutation universal-word bound is a different, stronger target family but does not imply the sharp restricted minimum. Semantic-index checks for the exact formula, path matching permutations, aliases, and primary source returned no equivalent statement. Residual risks include implicit combinatorial folklore and unindexed earlier presentations; absence of search hits is not a uniqueness certificate.

## Mathematical value
**PASS.** Exact finite-length optimal preprocessing words are a natural unresolved invariant when the source framework gives only asymptotic/broad upper bounds. This result handles **every** unit-ply-two interval configuration, with a meaningful component-sensitive formula \(2n-c\), an optimal construction, and the precise set and number of realizable orders. It is the first nontrivial ply regime and is not a numerical slice or parameter substitution. Its minimum-length guarantee is separate from smoothness or reconstruction-time guarantees.

## Closest literature and limits
The closest full-text source is Löffler–Raichel 2026 (arXiv:2601.19453, especially Section 3, Lemma 13); the 2025 precursor (arXiv:2502.03633, Section 4.3, Lemma 34) was also inspected. The 2012 Radomirović all-permutations work was checked through bibliographic description and the cited comparison in the 2026 paper, not independently in full. The classification does not extend automatically to unequal-length intervals or larger ply. Historical priority remains conditional and independent validation is unperformed.

Self-review: passed. Independent audit: not yet performed.
