# Mathematical review

## Correctness — PASS

Every odd closed token walk projects mod two to a nonempty odd-cardinality Eulerian base subgraph and therefore contains a base odd cycle no longer than the walk. Equality at the shortest odd length forces a unique base simple cycle with each edge traversed exactly once. Conservation forces cyclically aligned token moves; the chronological ordering of their edges is a permutation, and the occupied vertices are exactly its cyclic descent locations. Cyclic Eulerian counting and the exactly \(g\) starting points prove the formula. The independent checker corroborated 39 base graph cases and 126 token choices.

## Originality — PASS with residual historical risk

Full-text comparisons include the September 2025 generalized-token paper, the 2009 token-graph foundational paper, the 2024 token-digraph oriented-girth theorem, and the November 2026 maximum-cut paper. The last explicitly covers triangle multiplicities, which are acknowledged as previously known. Neither the oriented-girth result nor that triangle special case implies the general Eulerian multiplicity formula for every shortest odd length. Semantic record searches for girth, exclusion dynamics, cycle lifts, and Eulerian counts did not identify an equivalent unrestricted theorem. Historical priority remains provisional due to possible unindexed exclusion-process literature.

## Value — PASS

Shortest odd cycles are the smallest combinatorial obstructions to bipartiteness and underlie odd-cycle inequalities for maximum cuts. Counting them exactly for an arbitrary token graph is useful even when the base odd-cycle count is given: it reveals unexpectedly nonconstant amplification governed by Eulerian numbers. The formula generalizes the familiar triangle-parent count to every odd girth and yields a complete all-token-number distribution for each base shortest odd cycle. It is not a numeric restatement of known girth preservation.

## Limitations

Only minimum-length odd cycles are enumerated, and no maximum-cut value is asserted. Finite checks do not replace the proof; no independent audit was performed. The possible existence of older equivalent exclusion-process enumerations is an explicit priority risk.

Self-review: passed. Independent audit: not yet performed.
