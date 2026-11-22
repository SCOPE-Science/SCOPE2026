# Review of the leaf-majority involution and basin classification

## Correctness — PASS

For every finite simple core and each pendant multiplicity exceeding its core degree, the pendant blocks become unanimous after one update. On this set the update is exactly the involution \(z(a,b)\mapsto z(b,a)\) because the pendant votes strictly outweigh all other neighbours. This proves \(F^3=F\), identifies the entire recurrent set, and yields the exact orbit counts. Given an initial core word, each pendant block contributes a binomial factor to the next core word independently; their product supplies each attractor basin. The proof explicitly covers tie retention, isolated core vertices, and the small-mantle boundary. The two independently designed verification programs pass, including 1,363,612 exhaustive state cases and 37,956 independently traced states. The finite tests corroborate, not replace, the all-core proof.

## Originality — PASS with historical-priority qualification

The classical symmetric-threshold result proves eventual period at most two, not a universal one-update cutoff or individual basin weights. The 2026 finite-tree result includes a known local *passive-vertex* stability mechanism, duly credited; that tree-specific mechanism is not presented as independently novel. The indexed degree-two single-leaf corona and clique-corona results use different leaf regimes and do not imply the present arbitrary-core, degree-dominating, exact basin product. Full relevant portions of the tree work and the complete two indexed corona results were compared against the claim. Unindexed equivalent formulations in threshold automata remain possible; an inaccessible historical source would not establish uniqueness.

## Value — PASS

The classification applies to **every finite core topology**, including cyclic, complete, disconnected and irregular cores, and all sufficiently large heterogeneous pendant multiplicities. It provides a natural complete attractor and basin description, not just a generic period bound: orbit counts depend only on core order, whereas basin weights retain the precise core adjacency, and immediate recurrence occurs with exact probability \(2^{k-M}\). The double-star example visibly separates fixed and oscillatory basins; minimum-mantle complete cores give a rapidly vanishing recurrent fraction while preserving all \(2^{2k}\) recurrent phases. This exact distinction is useful in assessing how leaf reinforcement alters deterministic opinion networks.

## Closest literature and limitations

See the references in `RESULT.md` and the structured comparisons in `AUDIT.json`. The theorem does not cover insufficient mantles or nonstandard update rules; priority beyond the inspected indexed sources remains open. The theoretical proof, rather than computational sampling, supports the arbitrary-core quantifiers.

Self-review: passed. Independent audit: not yet performed.
