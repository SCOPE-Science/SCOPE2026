# Self-review

## Correctness (C): PASS

The input domain consists of aligned monotone two-row \(q\)-ary columns. Each output is a pair of one-deletion subsequences, and inverse-list size counts distinct sources rather than deletion-position pairs. The proof partitions each distinct one-insertion set by its first letter, obtains the exact size \(1+n(q-1)\), and bounds three remaining pieces after a possible first-letter comparison. For the ordered-leading case it proves the exact extremal increment \(2(q-1)T+(q-1)(q-2)/2\). For the reversed-leading case the strict positive difference is established for all \(n\ge2\). The constant extreme received pair gives equality by a direct count of same-position incompatibilities. The induction also proves uniqueness. The separate enumerator verified 23 complete small-parameter instances; it does not supply the infinite proof.

## Originality (O): PASS against inspected literature and actual searches

The closest primary sources are [1] and [2] in `RESULT.md`. The 2025 full arXiv manuscript analyzes deletion of one channel, not one deletion in each channel. The 2026 full manuscript defines the general channel and constructs multiple-deletion-correcting codes, but the inspected deletion theorems concern forward sphere sizes, code-cardinality upper bounds and constructions. Neither inspected text gives the all-\(q\), all-\(n\) inverse-list maximum or unique maximizing output. published-research record searches for simultaneous ordered-composite deletion preimages and their mathematical equivalent insertion-supersequence order constraint returned different channel results, including an inverse-list theorem for zero-deletion and adjacent transposition, not this simultaneous-deletion channel. The recoverable own-ledger claims concern other channels; an ordered overlapping-read inverse-list theorem is not an implication because its observations are overlapping reads from one source word, not independent row deletions from an order-constrained source matrix.

Residual risk: an equivalent unindexed theorem in ordered supersequence pairs, monotone matrix subsequence reconstruction or older deletion-coding literature may exist. The search does not prove absolute historical novelty.

## Value (V): PASS

The worst-case number of candidate source composites for an uncoded two-strand read is a natural decoder-resource and identifiability invariant, particularly in the two-affected-row deletion regime explicitly present in recent composite-storage models. The order constraint reduces the naive Cartesian bound \((1+n(q-1))^2\) by the exact, necessary term \(nq(q-1)/2\), and the equality characterization identifies the sole worst received pattern. This exact structural statement is independent of code-family parameters and is not a standard one-row insertion-ball count.

## Scope and limits

The result does not imply an optimal code size or cover stochastic errors, unlabelled channels or more than one deletion per row. Independent historical-priority and mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
