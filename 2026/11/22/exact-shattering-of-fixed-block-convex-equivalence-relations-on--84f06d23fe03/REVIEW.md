# Mathematical review of fixed-block convex equivalence shattering

## Correctness — PASS

The cut-site encoding is a bijection from \(b\)-block convex equivalence relations to \((b-1)\)-element cut sets. Necessity follows from three literal trace patterns: one negative query, all negatives, and all positives. The no-triple-intersection lemma follows rigorously from each interval having a private site; it justifies the replacement of bad piercing sites by private sites without losing any intended hits. The padding argument gives an exact, rather than merely upper-bounded, cut count for every requested trace. For the VC bound, the cardinality of private sites, doubly occupied all-negative cuts, and all-positive reserve sites are compared without double counting. Three-site overlapping-interval gadgets achieve all constraints for every admissible parameter pair, including the endpoints. The checker directly compares two separately implemented criteria in 397,284 finite instances, verifies 45 full VC-dimension cases, and cross-checks an additional 3,040 deterministic instances. The proof is all-parameter; finite tests alone would not establish it.

## Originality — PASS, with priority limitations

The unrestricted-cut published result [3] has the same queries but allows all block counts. Its private-site criterion alone does not imply shattering by any fixed-size cut layer: the additional piercing and outside-union constraints are genuinely necessary, and its dimension \(n-1\) differs sharply from the exact fixed-block formula. The refinement-closed family theorem [4] explicitly requires closure under arbitrary refinement, which the exact-\(b\)-block class lacks. The fixed-*size* two-block partition result [5] instead has no convexity restriction and a different query-completion geometry. The inspected arXiv literature [1–2] motivates VC studies and bounded unions of intervals but does not state the all-parameter pair-equality theorem. Relevant published results were examined by their full scientific statements, and searches included alternate interval-hitting and uniform-rank terminology. Unindexed or differently formulated historical coverage remains possible, and no independent priority verification has occurred.

## Value — PASS

The exact number of convex equivalence classes is a natural resource constraint for segmentation, ordered clustering, and fixed-complexity concept learning. The complete support test separates three independent obstacles: private witnesses for individual queries, the number of cuts needed to realize all negatives, and an equal-cardinality reserve to realize all positives. The sharp three-way VC formula is nonmonotone in the number of blocks, with a plateau followed by a collapse as nearly every site is forced to be a cut. This is a structural all-parameter statement, not a recomputation of a classical interval count, a formal corollary of unrestricted partitions, or a small finite example.

## Sources and limits

Relevant scientific sources: [1] H. Chase and J. Freitag, arXiv:1801.06566v1; [2] E. Blais et al., arXiv:2012.03923v1; [3] *Exact shattering polynomial for convex equivalence relations on a finite chain*; [4] *Refinement-closed partition concepts: exact shattering supports, online dimension, and coloring quotients*; [5] *Forest size profiles determine shattering by fixed-cardinality cuts*. Complete references and URLs appear in `RESULT.md`. Alternate-language priority risk, absence of adaptive dimensions, and finite checker coverage are disclosed in that document.

Self-review: passed. Independent audit: not yet performed.
