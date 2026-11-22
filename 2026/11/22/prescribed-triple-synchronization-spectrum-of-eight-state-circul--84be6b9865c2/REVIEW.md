# Review: prescribed-triple synchronization on an eight-state circular family

## Correctness — PASS

The normalization is a genuine bijection between cyclic-conjugacy classes and rank-seven maps omitting output zero. The count \(7\binom82 6!=141120\) follows from the duplicated output, two preimages and six remaining assignments. Every subset transition is exact on the 255-state subset graph. Reverse multi-source BFS determines every shortest triple-merging distance; an independently enumerated forward BFS for each of 56 triples verifies the distribution, nonsynchronizing count, unique maximum and second-place cases. Both programs ran to completion and agreed on every histogram bin. The maximum distance and non-implication examples were also checked with a separate word-producing script. The result makes only a finite eight-state claim.

## Originality — PASS (qualified)

Behague–Johnson (2020; 2022 journal) motivates the worst prescribed k-set time but its inspected material does not provide the present full circular rank-seven eight-state census. The already published all-map reset-threshold classification covers the same 141120 automata but a different invariant. A published Černý-specific all-subset formula does imply the value 37 for one automaton; that singleton value is credited and not a discovery. It cannot by itself imply the unique extremality across all maps, the 23-value histogram, or the equal-reset contrast. The present original claim is the all-map prescribed-triple spectrum and its tail structure. The full supplemental technical document of a plausible 2026 triple-rendezvous work was not obtainable; it and unindexed computer tables are documented residual risks rather than excluded claims.

## Value — PASS

Worst prescribed-subset synchronization is a natural invariant in automata and control, different from the minimum time for some chosen subset. The exact sharp maximum, isolated uniqueness, and four-letter gap identify how exceptional the cyclic defect-one extremizer is. Two maps with the identical full reset threshold 28 but worst prescribed-triple times 12 and 24 show that familiar full-state reset data fail to capture the new control performance metric. The comprehensive small-state benchmark supports tests of future upper bounds and algorithmic heuristics. No paper-sized infinite theorem is asserted or required for this exact classification.

## Closest literature and limitations

- Behague and Johnson, *Synchronizing Times for k-sets in Automata*, arXiv:2008.12166 — same prescribed-set motivation, not the finite spectrum.
- *Complete reset-threshold spectrum for eight-state circular defect-one automata* — same maps, different full-state quantity; previously known counts credited.
- *An exact circular-gap formula for every Černý subset rendezvous time* — covers the unique extremizer's particular value, but not all maps' frequencies or uniqueness.
- Zhang (2026), triple-rendezvous work — different minimum-over-triples formulation; supplemental complete text inaccessible, genuine remaining risk.
- Finite exhaustive verification is not independent mathematical validation; no assertion about other automaton orders.

Self-review: passed. Independent audit: not yet performed.
