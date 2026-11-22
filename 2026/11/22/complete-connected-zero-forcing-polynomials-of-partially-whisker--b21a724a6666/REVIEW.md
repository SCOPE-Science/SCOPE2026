# Self-review

## Correctness — PASS
For every \(n\ge3\) and every cyclic leaf subset \(A\), initial connectivity forces selected cycle vertices to be a cyclic interval, with any selected leaves supported inside it. With a proper interval containing at least two cycle vertices, the only possible advance into the complementary white segment is from its two ends; a newly reached leaf-bearing vertex blocks advance beyond itself until the opposite front reaches the boundary of the remaining gap. The two reach lengths therefore cover the gap exactly when the stated inequality holds. Once the cycle is colored all private leaves are forceable. Internal leaves and boundary activity choices then give the formula without double-counting. A separate direct subset simulator agrees for all 120 leaf-placement patterns on cycles of orders \(3\le n\le6\), plus two contrasting seven-cycle placements. The checker is supporting finite evidence, not the infinite proof.

## Originality — PASS (historical priority provisional)
The strongest structural antecedent is Brimkov (arXiv:1607.00658), which treats feasible omitted segments to compute minimum connected forcing numbers on general unicyclic graphs. A public result already enumerates all connected forcing sets of the fully whiskered cycle (published-finding corpus record a54ae5ebc761); this special case is excluded from the novelty claim. The new claim is a uniform all-weight polynomial for **every** cyclic placement of up to one pendant leaf per vertex, with exact endpoint seed weights and a gap coverage criterion. Tree-only enumeration and coronas with isolate-free attached graphs do not imply it. Searches against published-finding corpus, the accessible own claim ledgers, and the primary full texts identified no dominating all-cardinality theorem for arbitrary partial whiskering. Unindexed earlier work could alter historical priority.

## Value — PASS
Partial whiskering is a natural interpolation between a bare cycle and a full sunlet. The explicit formula classifies every connected initial forcing configuration on this whole class, not only the minimum cardinality. It records cyclic placement, a structural feature lost by order and degree sequence: on seven-cycle bases with three leaves the full coefficient distributions differ dramatically for consecutive versus separated attachment sites. The polynomial provides a reusable exact test for connected deployment counts across nonuniform cycle networks.

## Scientific limitations and closest literature
The minimum parameter on unicyclic graphs and the full-sunlet polynomial are not new, and the result is bounded to at most one private leaf per cycle vertex. Brimkov (2016), Brimkov–Davila–Schuerger (2025), Mukherjee–Ray (2026), and the published sunlet RESULT.md were examined at the stated relevant sections. Priority remains provisional and the finite computational check is not a substitute for proof.

Self-review: passed. Independent audit: not yet performed.
