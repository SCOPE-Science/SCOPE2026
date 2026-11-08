# Scientific review

## Correctness

**PASS.** The clique-line reduction, rook-placement saturation condition, converse maximality argument (including full-column length two), and separate \(2\)-by-\(2\) overlap are proved. The two classes and their falling-factorial counts agree with direct forbidden-induced-subgraph enumeration on fourteen rectangular boards and 1,763,152 candidate vertex subsets. The probability law follows from an exact ratio and makes no inference from finite testing alone.

## Originality

**PASS, provisionally.** Cao (arXiv:2004.09885, Theorem 1.1 and Proposition 5.6) gives a general polynomial-delay procedure for maximal induced split subgraphs; it does not provide the rook-graph cardinality distribution. Brosse et al. (arXiv:2007.01031) distinguish maximal induced split enumeration from their maximal split *edge*-subgraph procedure. The closest result is Brosse's thesis (2023, Theorem 3.13), which already gives a necessary maximal-clique-plus-maximal-independent-set representation for arbitrary graphs. That reduction is acknowledged and is **not** claimed new. Its graph-independent statement does not supply the precise two-class rook census, uniqueness boundary, or size-distribution crossover; those are separately proved. Published-record comparisons for rook, lattice, Cartesian-clique and complete-bipartite-line descriptions did not identify an earlier equivalent complete formula. The residual priority risk is an unindexed or differently phrased special-family result, and the specialized enumeration is elementary once the general representation is known.

## Mathematical value

**PASS.** Maximal split deletion is a natural enumeration problem, not an arbitrary induced-subgraph statistic. The exact classification of every maximal solution on a canonical connected vertex-transitive graph family determines all inclusion-minimal split-vertex-deletion cardinalities by complementation. The gap of \(n-m-2\) missing sizes and the probability \(m/(m+d(d+1))\) prove a quantitative square-root crossover between two structurally different deletion regimes. This is stronger than a minimum cardinality or a generic enumeration algorithm; no general-purpose graph algorithm is asserted.

## Limits and nearest literature

The 2023 general reduction and the established 1977 split-graph forbidden-subgraph criterion are prerequisites, not novelties. The verifier tests finite boards only; the proof handles every \(2\le m\le n\). Priority is not an independent certification, and no claim about higher-dimensional rook graphs is made.

Self-review: passed. Independent audit: not yet performed.
