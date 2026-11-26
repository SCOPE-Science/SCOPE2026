# Independent mathematical audit

## correctness

PASS

Reconstructed the unrestricted repaired proof. A maximal independent set is independent and dominating. All-positive labels rule out adjacency; across a forbidden run beginning and ending with two distinct short gaps, positives at its endpoints (a single positive if they coincide cyclically) and zeros inside force a chain of selected right neighbors, the last adjacent to the final positive. Conversely, a gap ≥4 ensures at least two steps even if both helpers move inward. Across a gap 3, the two negative labels cannot use right/left helpers together; common orientation within a block avoids this. At gap 2 a mixed label forces the negative's outward helper; because each block has at most one such gap, a single choice works per block. The witnesses never occupy negative queried vertices, are independent, and their fixed domination ensures that greedy maximal extension preserves all queried bits. The repaired text explicitly treats singleton and both arcs for k=2. With p long gaps and q short gaps, p intervals have generating function (1/(1−u)+v/(1−u)^2)^p, yielding binom(p,q)binom(k−1,k−p−q); long-gap excess contributes stars-and-bars. Count indexed sequences with a marked long gap in two ways, including periodic sequences, then label a start vertex and divide by k, yielding n/p. Without long gaps only all-three and single-two gap types are allowed, giving 3 and n respectively. These are disjoint counts with empty support handled separately. Independently enumerated all 524280 supports at n=3..18 by rotated adjacency/domination bit masks and direct distinct trace cardinalities (an adjacent support cannot realize all ones); agreed for each support and coefficient. The examples n=3,4,10 give [1,3], [1,4], and [1,10,35,40].

## originality

PASS

Reassessed narrower claim: all-degree exact support counts for arbitrary n. The known VC dimension, necessary forbidden-run condition, and mechanically implied tight top coefficient are not claimed as contributions. The genuinely surviving count requires handling arbitrary admissible supports, including those with several short gaps, and counting all of their sizes.

## value

PASS

The known VC dimension only answers whether a size is attainable. The repaired all-degree formula computes the number, hence the exact fraction of supports of each size that can realize all assignments; it requires distinguishing arbitrary cyclic configurations with several short gaps. This is a natural exact refinement, not a repeated computation of the old dimension or tight coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
