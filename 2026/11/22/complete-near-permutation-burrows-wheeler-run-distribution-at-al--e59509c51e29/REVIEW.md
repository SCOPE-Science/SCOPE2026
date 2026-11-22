# Scientific review

## Correctness — PASS

All near-permutation necklaces are primitive because at least one symbol occurs once. The BWT last column has exactly two equal entries; sorted-rotation first-letter blocks identify their positions. The nonadjacent source case reduces to two singleton first-letter blocks, and the adjacent-source case is resolved by the relative ordering of the two rows beginning with the duplicated symbol. Both lead to precisely the same rank-adjacency test. The uniform successor-pair bijection has exactly \((n-3)!\) necklaces per pair for every repeated symbol. Explicit multiplication and subtraction give the stated exact formulas, including the boundary case \(n=3\). Source-based exhaustive BWT calculation and independent stable-LF single-cycle enumeration agree for every \(3\le n\le9\). Finite enumeration is not presented as an all-length proof.

## Originality — PASS against inspected evidence

Relevant primary full-text sections of [1], [2], and [3] were checked for the fixed-content profile and a stronger counting result. [1] develops generalized de Bruijn structures; [2] gives existence and a lower bound for ternary families, and specifically raises characterization/counting of unclustered necklaces as a further problem. [3] gives an unrestricted fixed-Parikh necklace count (Proposition 5.5) and explicitly notes that it does not count the unclustered subclass; its principal quantitative result minimizes **source** cyclic run counts, not output run counts on near-permutation necklaces. None of these statements entails the asserted \((n-3)/(n-1)\) proportion or the successor-rank classification. Special fixed lengths may be recoverable from known tables and are not claimed as new in isolation. Remaining risk: an unpublished or unindexed equivalent all-length observation.

## Value — PASS

The first defect away from a permutation uses exactly one repeated letter. It is a canonical, composition-constrained stress test of BWT clustering: whether this single collision causes an equal-letter run after cyclic-context sorting. The theorem completely classifies this natural family by a local successor-order invariant and gives exact counts and an asymptotic law, instead of a collection of short examples. It addresses the published request for structural characterization/counting, while explicitly not solving fixed-alphabet or arbitrary-content problems.

## Scope of review

The boundary, adjacent-symbol case, uniform-pair counting, and relevant prior statements were examined. No claim of mathematical uniqueness, independent validation, or external certification is made.

Self-review: passed. Independent audit: not yet performed.
