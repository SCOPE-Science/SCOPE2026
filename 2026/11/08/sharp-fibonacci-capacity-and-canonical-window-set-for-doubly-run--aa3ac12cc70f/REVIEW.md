# Scientific review: sharp two-sided run-constrained cyclic window capacity

**Correctness — PASS.** The overlap graph's in/out imbalance gives an upper bound of \(2F_{n-3}\) omitted edges. The uniquely forced family with doubled initial and terminal symbol pairs repairs that imbalance. The remaining edges form a balanced, strongly connected graph by alternating-extension routes. The equality case identifies every omitted edge, yielding the common window set. The standalone checker reconstructs Euler cycles, edge sets and the claimed counts at orders 3–16, with additional exhaustive circular-word checks at orders 4–5. No empirical enumeration is being used as an infinite proof.

**Originality — PASS (qualified).** The 2016 rotation-closed language theorem of Sawada, Williams and Wong does not cover the non-rotation-closed optimum window set. Chee et al.'s 2024 maximum-length RLL work explicitly addresses a one-sided zero-run restriction, not the simultaneous no-\(000\)/no-\(111\) restriction and canonical optimum set here. Direct statement and implication searches found no exact matching all-length result. There remains an unindexed-publication priority risk, particularly in the literature on constrained universal cycles.

**Value — PASS.** The cyclic uniqueness-of-windows condition is the synchronization/position-identification invariant of cut-down de Bruijn sequences. Simultaneously bounding runs of both symbols breaks full-graph Eulerian balance, so this exact all-length Fibonacci optimum and its uniquely determined window spectrum resolve a motivated structural capacity problem rather than an arbitrary enumeration. At order four the optimum eight windows exceeds the six cyclically admissible four-bit words, emphasizing why using only necklaces or cyclically admissible windows misses the optimum.

**Limits.** Binary alphabet, both runs capped at two, \(n\ge4\). No count of Euler cycles, no higher-cap bounds. Historical-priority uncertainty persists; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
