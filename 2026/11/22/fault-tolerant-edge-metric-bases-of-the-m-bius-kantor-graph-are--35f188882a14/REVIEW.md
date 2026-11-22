# Scientific review: fault-tolerant edge metric bases of the Möbius–Kantor graph

## Correctness — PASS

The claim uses the standard shortest-path distance from a vertex to an edge and requires two distinct witnesses for every edge pair. All 276 pair masks are calculated from the explicitly labelled 16-vertex, 24-edge graph. Independent exhaustive programs cover all 1820 four-sets and 4368 five-sets (plus the independent ordinary three-set test). They find no four-set satisfying fault tolerance and exactly 16 five-sets, equal to the 16 distinct five-element third-distance shells. Because the two-witness property is monotone in the chosen set, this proves global minimum 5. The two bipartite shores and their common-neighbour intersections prove the exact exchange structure after the finite optimizer classification. Both complete programs and their execution methods are included.

## Originality — PASS, subject to priority uncertainty

The foundational edge metric paper (Kelenc–Tratnik–Yero, arXiv:1602.00291) supplies the ordinary invariant and conventions, not the fault-tolerant Möbius–Kantor optimizer list. Filipović–Kartelj–Kratica (arXiv:1807.00580) studies ordinary edge metric dimension for generalized Petersen graph families, not one-failure robustness. Wang–Wang–Zhang (arXiv:2005.08038) supplies ordinary edge-metric results for step three and includes Möbius–Kantor as an example, but does not establish this precise two-witness classification. Liu–Ahsan–Zahid–Ren (doi:10.3934/math.2021069) defines the fault-tolerant variant and studies other named graph families. Indexed mathematical-result searches for direct aliases, exact parameters, and reduction relations did not identify a stronger prior theorem. The relevant later papers were not all available in an exhaustively audited line-by-line version, and unindexed priority cannot be excluded.

## Value — PASS

The exact optimizer count concerns a canonical small cubic symmetric incidence graph. It attains the natural general one-unit resilience lower bound, while the distance-three-shell correspondence is an intrinsic graph-geometric description, not just a solver count. It implies a sharp distinction between local and global monitor relocation: all 16 minimum robust placements split into the two bipartition classes, internally densely connected at replacement budget two but separated until the entire five-sensor placement changes. This establishes a concrete reliability-versus-mobility boundary in a natural graph, rather than an arbitrary graph slice.

## Limits

No proof of an all-generalized-Petersen classification is claimed. No independent peer or expert audit has been performed. Exact priority is subject to unindexed historical work. The ordinary four-landmark result is context, not claimed as original.

Self-review: passed. Independent audit: not yet performed.
