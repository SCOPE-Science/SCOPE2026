# Scientific review

**Correctness — PASS.** The proof covers every integer \(n\ge3\). Edges of the path-token graph are classified exhaustively as increments of the larger or smaller coordinate; the indexed paths \(Q_j\) are vertex-simple and partition the path-token edges. Unique wrapping edges close them into \(n-2\) edge-disjoint \(n\)-cycles. For odd \(n\), any graph cut misses at least one edge in each cycle, and the base-parity lifted cut misses exactly that many. Even \(n\) gives a bipartition crossing every edge. An independently generated checker corroborates the n-cycle partition through \(n=150\) and exact maximum cuts by exhaustive enumeration through \(n=7\).

**Originality — PASS, with historical-priority qualification.** The eligible September 25, 2026 Rivera preprint studies vertex packing on the exact graph but not the asserted edge optimization. The November 18, 2026 *Max-Cut on Token Graphs* paper supplies a general **lower** bound using parity lifting; its other exact classes are not cycles, and it does not prove the matching upper bound. Rivera's November 17, 2026 paper classifies maximum independent sets on the same graph; earlier accessible work studies spectral radii. A full-text comparison of these sources and published mathematical records searches for maximum cuts, frustration indices, path/cycle decompositions, aliases and stronger coverage did not identify the all-order claim. Older unindexed literature remains a risk; inaccessible motivating full text is explicitly noted.

**Value — PASS.** The complete edge partition yields an exact maximum-cut answer for every two-token cycle graph and the sharp odd-cycle bipartization cost. This establishes nontrivial equality in a recent general bound and a useful structural reason for it; the claim is not a small isolated numerical computation or a parameter substitution.

**Limitations.** No weighted, higher-token or general base-graph result is claimed. Direct finite checks only corroborate the all-order proof. No independent validation has taken place.

Self-review: passed. Independent audit: not yet performed.
