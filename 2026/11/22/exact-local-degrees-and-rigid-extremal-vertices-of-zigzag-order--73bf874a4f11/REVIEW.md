# Scientific assessment of the zigzag-order-polytope local-degree theorem

## Correctness — PASS
With ideal-indicator coordinates, complementing **odd** positions (not even positions) correctly identifies the zigzag order polytope with a path stable-set polytope. The connected-difference interval rule is justified from common tight facet equations. Counting flippable intervals gives the exact cluster formula. The disjoint augmented-span inequality and strict convexity prove the sharp degree bound, exclusion of multiple-cluster equality and parity-dependent equality cases. The included `CHECK.py` verifies the entire per-vertex theorem for dimensions 3 through 11, and exact rational face ranks of every vertex pair in dimensions 3 through 7. Finite checks corroborate but cannot replace proof for unbounded dimensions.

## Originality — PASS, historically provisional
Mori, arXiv:2307.08447 (first public 2023-07-17), already provides general order-polytope edge facts. Lee, arXiv:2610.07413 (first public 2026-10-05), gives the general connected-convex-subset edge partition and global zigzag edge counts. Both were compared by implication. The cluster-by-cluster local degree identity and all sharp equality cases are not reported in their inspected treatments. Published published-finding corpus records and targeted web searches for stable-set-path aliases did not locate such a formula. The general adjacency rule, global counts, and interval-length census are prior work, not assessed as new. The local formula is derived from the known edge theorem and could be an unindexed existing corollary; that is the principal residual priority risk.

## Mathematical value — PASS
Four simple vertices among exponentially many vertices coexist with a maximum of quadratic order in dimension; the exact degree at every vertex and rigid parity-sensitive extremizers describe local geometric complexity of this natural polytope family. This is a structural extremal characterization rather than an arbitrary finite instance or mere recomputation of total edges.

## Limits
Only the zigzag/path case is addressed, no full degree-distribution generating function or higher skeleton classification is asserted. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
