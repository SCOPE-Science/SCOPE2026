# Review of the cycle-rose sliding-puzzle theorem

## Correctness — PASS

The component-state classification is proved by reducing hub-return blank walks to oriented petal loops and noting that these act by commuting, disjoint full-cycle token rotations. The explicit core subdivision is a graph isomorphism, including two distinct parallel core edges for every triangle petal. The spanning-tree formula follows from a direct spanning-tree subdivision bijection and the weighted matrix-tree theorem. Both spectral normalization (division by the core vertex count) and the all-triangle specialization are explicitly derived. The independent finite verifier compares the complete original swap component with the constructed core and compares two exact integer determinant computations. No finite enumeration is taken as a substitute for the unrestricted proof.

## Originality — PASS with residual historical-priority risk

Yang's recent seven-page paper (arXiv:2611.23295v1) concerns vertex-disjoint routes for **2-connected** boards; these roses are not 2-connected. Krishnan–Li (arXiv:2410.21334v3) gives component vertex connectivity, not the complete component graph or spanning-tree complexity. Defant–Kravitz (arXiv:2009.05040v2) treats one cycle and gives cut-vertex component-count lower bounds, not the multi-petal graph isomorphism or tree product. The inspected Jeong and Defant–Dong–Lee–Wei studies address girth and other cycle spaces. Exact-query searches for rose board, sliding puzzle, subdivided Cartesian cycles, spectral spanning-tree product, and equivalent configurations did not reveal coverage. Wilson's 1974 puzzle paper was not inspected in full; potential implicit coverage of the hub action is acknowledged, but no accessible evidence demonstrates the specific multi-rose graph-and-tree theorem. Historical priority is not independently certified.

## Value — PASS

This yields an explicit structural model for *every* connected component of a natural family of partially connected sliding-puzzle configuration graphs, determines all cycle ranks, and counts spanning trees exactly for an arbitrary number of petals and arbitrary cycle lengths. Spanning-tree complexity measures the count of fault-tolerant connecting backbones of the configuration space and is not determined by component connectivity alone. The uniform-triangle specialization yields an exact unbounded-parameter product.

## Limits and sources

The board must be a pure rose of simple cycles and all tokens are distinct. This work does not claim a general cactus classification. The cited primary full texts were inspected for their relevant results; the older Wilson article remains an explicitly unresolved historical comparison. The integer computations check small parameter instances only.

Self-review: passed. Independent audit: not yet performed.
