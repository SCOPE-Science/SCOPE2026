# Review: Twenty-one rank-three theories of finite rectangular grid posets

## Correctness

**PASS.** The exact theorem is for nonempty rectangular grid posets in the pure single-order vocabulary. A three-move EF game on linear factors has the seven-point stabilization threshold. Playing two such games coordinatewise preserves both order and equality on the product, so all cases reduce to 28 factor pairs with side lengths at most seven. The standalone certificate exhaustively computes the exact three-round back-and-forth signatures for those cases and checks all 784 ordered pair comparisons against the stated 21 classes, including the strict distinction between \(G_{5,5}\) and \(G_{5,6}\). A logically independent direct EF search checks 55 pairs of smaller examples. The proof explicitly explains why the finite calculation suffices for arbitrary side lengths.

## Originality

**PASS within inspected evidence.** Kurilić's paper, *Model Theory of Products of Chains* (arXiv:2610.24683, 17 October 2026), concerns full model theory and factorwise complete theories, not an exact rank-three partition. Sankaran's 2016 dissertation provides general bounded-substructure results for grid posets but does not state the 21 classes. Mwesigye–Truss (DOI 10.1007/s11083-018-9458-3) addresses finite *coloured linear orders*. Targeted mathematical literature and indexed-research searches found no directly covering 21-class theorem. The factorwise seven-point reduction is standard, and is not asserted as new. The finite complete classification and its sharp terminal representative supply the additional content. An unindexed equivalent prior result remains a residual priority risk.

## Value

**PASS.** Quantifier-rank-bounded logical equivalence and optimal finite representatives are natural invariants in finite model theory. Here a complete classification for a basic structured family has exact thresholds and displays a genuine new collapse: \(G_{5,6}\), \(G_{6,6}\), and all larger grids share a rank-three theory despite the exceptional \(G_{5,5}\). The result is mathematically motivated by recent work on theories of finite products of chains and does not depend on inventing a bespoke parameter or claiming a broad unproved application.

## Limits and verification

The bound of 30 is minimal **only within rectangular products of two chains**, in the pure order vocabulary. The checker was run and independently cross-checked for small instances. No formal proof-assistant certification or independent expert audit is asserted; historical priority outside inspected literature is unresolved.

Self-review: passed. Independent audit: not yet performed.
