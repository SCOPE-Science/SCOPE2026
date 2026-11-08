# Self-review

## Correctness — PASS

The finite result is stated for exact labelled permutations with a fixed one-swap adjacency relation. The left-to-right recurrence appends each unused value and checks precisely the new differences at every gap, which proves both that no valid array is discarded and that every retained completed array is valid. Every transposition is checked against the full enumerated set, and degrees and gap counts are calculated at both endpoints. The independent right-to-left implementation computes displacement masks and checks the complete Costas property after every potential swap. Executed checker programs agree on all counts and gap histograms and reject deviations from expected values. There is no infinite-order extrapolation.

## Originality — PASS, qualified

The closest primary document is Drakakis, Healy and Rickard (2008), Section 3.2, Table 2: it already lists Hamming-distance-two pair counts 136, 88 and 120. Those totals are not claimed. Its table and discussion do not identify vertex degrees, connected components or the positional-gap histogram; aggregate pair totals cannot logically determine whether two pairs share an endpoint. The 2023 modular-index transformation is a different operation. Targeted literature and published published-finding corpus searches did not identify a dominating or equivalent complete degree/component classification. Unindexed earlier work could contain it, so priority is qualified.

## Value — PASS

A valid Costas permutation is a frequency-hopping design; pair swaps are the local operation explicitly investigated in the 2008 stochastic-search literature. The sharp degree-one property means every valid-state-only local walk at these orders is confined to at most two arrays, a structural obstruction stronger than simply having few close pairs. The order-eleven degree-two examples demonstrate the behaviour is not a tautological consequence of the Costas definition. Positional-gap data identify which geometric rearrangements can occur, giving a natural finite reconfiguration benchmark. This does not imply a general-order theorem or invalidate algorithms allowed to leave the Costas family.

## Prior literature and remaining limitations

The previously published totals and the full 2008 relevant section were inspected directly; the 2023 paper's alternative transformation was examined. The 2007 arXiv article supplies a verified prior public date and underlying definition. Exact novelty outside indexed and accessible literature cannot be guaranteed. Scientific validation is finite, with the reproducible exhaustive methods included in the package.

Self-review: passed. Independent audit: not yet performed.
