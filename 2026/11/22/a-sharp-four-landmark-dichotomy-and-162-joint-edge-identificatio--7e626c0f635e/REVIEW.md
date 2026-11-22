# Scientific review: Petersen joint edge-identification census

## Correctness — PASS
The ten Petersen vertices and fifteen edges are explicitly fixed as the two-subset Kneser model. For every edge, exactly four root cross-pairs are at edge distance two, so a four-landmark set fails vertex–edge coverage exactly when it equals one of the fifteen distinct cross-pair sets. The exact certificate tests all \(2^{10}=1024\) vertex subsets and all fifteen signatures; all \(210\) four-sets and all \(252\) five-sets are partitioned into respectively six ground-label symmetry orbits, whose members have the same measured edge-resolving predicate. The four accepted five-set orbits have sizes \(60,60,30,12\). An independently written standard Petersen-graph/BFS implementation agrees with all three cardinality polynomials. The claim concerns only this finite graph, for which the enumeration is exhaustive.

## Originality — PASS, provisional
Ikhlaq, Hayat and Siddiqui (arXiv:2211.09327; first posted 2022-11-17) introduced the exact joint invariant but did not give a Petersen four-landmark dichotomy or a full joint census. Filipović, Kartelj and Kratica (arXiv:1807.00580) had already established the Petersen ordinary edge-metric value \(4\); this scalar is explicitly excluded from the novelty claim. Tavakoli et al. (DOI:10.5614/ejgta.2023.11.1.16) use vertex-cover domination, which differs from the distance-one vertex–edge domination employed here. The numerical answer and the root-graph orbit classification are not implied by those results. Search coverage cannot rule out an uncatalogued earlier computation; the 2023 publisher article was read in its complete publicly accessible twelve-page PDF and does not use the Petersen graph.

## Mathematical value — PASS
The two independently motivated sensor conditions give a sharp and non-obvious incompatibility at their first relevant cardinality in a canonical 3-regular graph. The exact difference between ordinary and joint minima, the 162 configurations divided into four geometric types, and the complete feasible-set polynomials are stronger than an isolated invariant evaluation. They furnish a reproducible benchmark for distance-sensitive sensor coverage versus identifiability.

## Computational verification and limits
The two standalone programs `census_symbolic.py` and `census_bfs.cpp` yield `PET_X5_SYMBOLIC_OK` and `PET_X5_BFS_OK`. The first computes the full \(S_5\)-orbit census and the second independently constructs shortest-path distances by BFS on \(GP(5,2)\). Their saved outputs are included. The classification is not extrapolated to other generalized Petersen graphs. Literature-priority coverage is provisional and no independent external mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
