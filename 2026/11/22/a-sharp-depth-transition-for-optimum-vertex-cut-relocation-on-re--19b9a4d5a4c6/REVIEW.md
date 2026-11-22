# Self-review

## Correctness — PASS

The proof establishes the minimum cut cardinality using three vertex-disjoint rails and an explicit upper bound. Every possible minimum cut is restricted to three distinct rails; two bypass-path constructions prove the adjacent-column inequalities and the outer-row endpoint constraints. An explicit two-colour separation proves the converse. The enumeration and token adjacency follow coordinate-by-coordinate, separately treating the short-column exception. Two standalone standard-library checkers, one testing actual graph disconnection and the other checking the coordinate model, passed 56 and 1,232 distinct parameter instances, respectively. These tests support but do not substitute for the all-parameter proof.

## Originality — PASS (qualified)

The 2023 primary paper on minimum-separator reconfiguration, arXiv:2307.07782, was materially inspected (introduction, canonical-path lemmas, both movement models, and searches for grid/Cartesian/ladder terminology). Its general polynomial-time slide framework does not state or directly imply the exact rectangular-grid cut description and sharp mobility phase classification without additional graph-specific analysis. The 2020 nonminimum vertex-separator paper, arXiv:2004.10873, was accessible only at abstract level. Related existing work on width-three grids concerns a disjoint parameter range and does not cover width at least four. Available indexed findings and primary literature searches did not reveal a covering statement. Residual risk: an unindexed or unread mathematically equivalent result remains possible.

## Value — PASS

A complete natural-parameter classification of optimal network cutset mobility is a structural reconfiguration benchmark. Holding the minimum cut capacity fixed at three, moving both terminals only one row deeper produces absolute token-slide rigidity, while at three columns the jumping model remains connected even after sliding freezes. These sharp distinctions are not detected by the minimum-cut value alone and distinguish local relocation feasibility from unrestricted replacement feasibility. The result is for the complete parameter family, not an arbitrary small graph or an incrementally improved table entry.

## Boundaries

Same-row, interior, opposite-side terminal placements only; at least four rows and three columns. Only strict minimum separators and one-token moves. The finite tests are corroboration, not an infinite proof. The 2020 abstract-level prior comparison and the potential existence of unindexed historical equivalences are the principal scientific-access risks.

Self-review: passed. Independent audit: not yet performed.
