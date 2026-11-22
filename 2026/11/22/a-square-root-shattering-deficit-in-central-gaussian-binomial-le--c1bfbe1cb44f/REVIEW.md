# Self-review

## Correctness — PASS

The support test is proved for every finite poset: traces with prescribed positive and negative membership correspond to ideals between a forced minimum and a forced maximum, and every intermediate cardinality is attained by a linear extension. For square grids, every shattered antichain of size \(s\) has an incomparable-cell free region of size at least \(s\), but at most \((m-s)^2\); this implies the sharp quadratic bound. The explicit anti-diagonal support has exactly \(B=s(2m-s+1)/2\) cells in both closures, proving central attainment and the claimed band. All boundary cases, including \(m=1\), are included. The standalone checker successfully replayed 8,900 finite support–rank comparisons; no finite test is used as an infinite proof.

## Originality — PASS (with historical-priority risk)

The general finite-poset rank-slice antichain/two-closure test was previously obtained and is credited background here. It does not imply the sharp square-grid bound without the new free-cell extremal argument. A comparison by mathematical implication finds no covering statement in the inspected 2019 shatter-complex theory of intersection-closed families (arXiv:1909.02159) or the 2020 bounded-positive search problem for ideals (arXiv:2009.07348). The former does not directly apply to nontrivial rank-selected layers because they are not intersection-closed; the latter has a different concept family and target quantity. Published search summaries on unrestricted ideal-class online rank, and on maximal antichains of grid posets, do not logically imply fixed-area Ferrers-diagram VC dimension. Full text of two relevant indexed records was not available through the accessible retrieval route; unindexed equivalent results remain a genuine priority risk, not an assertion of global uniqueness.

## Value — PASS

Square-grid Ferrers diagrams form the Gaussian-binomial rank levels of a classical distributive lattice. Exactly fixing diagram area is a natural combinatorial constraint, and the resulting VC dimension can differ substantially from the width of the underlying grid. The proven exact \(\sqrt m\)-scale loss, together with an all-support feasibility test and an explicit optimal construction, determines a previously unaccounted learning-complexity effect for an infinite family. This is more than a numerical recomputation of small cases; the all-order theorem is motivated by the rank restriction.

## Closest literature and scientific limits

A previously established general fixed-rank support test is credited, not claimed new. The closest directly inspected published sources are Chen–Eur–Yang–Zhang (2019) on intersection-closed shatter complexes and Iams–Johnston–Muth (2020) on constrained adaptive ideal search. Known Gaussian-binomial enumeration and unrestricted poset width facts are not asserted new. The proof does not determine all rank-specific dimensions or face counts. Historical novelty has not been independently established.

Self-review: passed. Independent audit: not yet performed.
