# Scientific review of pendant-edge collapse invariance

## Correctness — PASS
The claim quantifies over all finite simple base graphs containing a degree-one vertex. The six possible neighborhood generators containing one of the three new fiber vertices are explicitly characterized. Each of three triangle pairs has a free edge unique to that generator; after their deletion every new-vertex face lies in one of three cones over old neighborhood simplices. An ordered pivot matching in each cone removes exactly \(2^{d+1}\) elementary pairs, with all competing cofaces already removed. This proves the asserted exact collapse count and terminal equality. A separate standalone checker recomputed and confirmed 22,080 individual legal free-face pairs in 320 examples; finite checks are not used as the all-graph proof.

## Originality — PASS against inspected evidence
Shukla's first-public 2018 study addresses maximum-degree-at-most-three graphs and four-regular circulants and uses ordinary graph foldings; it does not cover an arbitrary high-degree base or the claimed relative triangular-product leaf collapse. The closest published large-clique Cartesian-product theorem assumes a clique factor of size at least four, where the alleged invariance is false. The existing triangle-cycle calculation identifies the topology of a leafless cycle, not arbitrary pendant-tree modifications. Searches for pendant attachments, triangular-fiber products, core reduction, and exact elementary collapses yielded no statement dominating this leaf-pruning theorem. An unindexed equivalent or overlooked general operation theorem remains possible.

## Value — PASS
This is an all-graph structural invariance theorem for a natural graph operation on a topological graph invariant; it yields an explicit simple-homotopy equivalence and an exact number of elementary moves, not just a Betti-number calculation. It reduces all triangular-fiber neighborhood calculations to the graph's leaf-pruned core, completely determines every tree case, and shows torus topology and cup products survive arbitrarily many pendant-tree attachments to a cyclic base. The boundary is meaningful: the same leaf operation changes the homology already at clique width four.

## Limitations and closest literature
The theorem is specific to the ordinary open neighborhood complex and a triangle factor. It does not determine the types of general leafless cores and does not establish priority against inaccessible or unindexed mathematics. The nearest works are Shukla (arXiv:1802.04526), the published triangular-cycle torus calculation, and the published clique-fiber theorem for width at least four. No external independent review is claimed.

Self-review: passed. Independent audit: not yet performed.
