# Review of the Möbius–Kantor cycle-trade classification

**Correctness — PASS.** The graph, every perfect matching, every allowed trade and every shortest-path distance are finitely and explicitly defined. Two distinct standalone algorithms count the same \(33\) matchings, and independently derive exactly \(96\) hexagon-only trades, \(36\) octagon-only trades and \(132\) combined trades. All exact degree and distance profiles and the subdivided-double-triangle description are asserted and checked in the programs. Completeness follows from checking all vertex-saturation branches and, independently, all \(8!\) possible bipartite bijections.

**Originality — PASS, qualified.** The earlier perfect-matching count \(33\) is explicitly credited to the 2025 matching-polynomial tabulation. Bryant and Dean's 2014 paper treats a different question on Hamilton decompositions and perfect one-factorizations. Bonamy et al. and Ito et al. formulate different unrestricted or four-cycle reconfiguration models whose theorems do not imply the sharp specific six/eight-cycle graph decomposition. The metric and structural classification was not found in inspected primary works or targeted searches. Risk: equivalent figures might be hidden in unindexed data or early resonance-graph literature.

**Value — PASS.** The problem arises canonically from local dimer moves on a small, highly symmetric, nonplanar cubic bipartite graph of girth six. The exact obstruction for hexagon moves, the simple octagon-only model, and the sharp reduction in maximum distance after adding hexagons give a substantive reachability benchmark, beyond the known isolated count of matchings. This does not entail a general family or prove mixing bounds.

Self-review: passed. Independent audit: not yet performed.
