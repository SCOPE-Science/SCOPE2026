# Self-review

## Correctness

PASS. For an odd triangular graph, an optimum dominating set is necessarily a near-perfect matching of the underlying complete graph. The shortest-flip potential and constructive alternating-path/cycle correction justify the distance parameter. The labeled component count assigns \(2^{r-1}(r-1)!\) cyclic arrangements on \(r\ge2\) matching edges and \(2^rr!\) rooted-path arrangements on \(r\ge0\) matching edges. Their exponential generating function gives all distance-sphere cardinalities, and the two antipodal formulas follow from the maximal number of two-atom cycles. Exhaustive graph searches and an independent symbolic recurrence reproduce the stated specializations. This is a proof for all integer parameters, not an inference from finite tests.

## Originality

PASS for the distance-sphere enumerator and antipodal multiplicities only. Golovach et al. enumerate minimal edge dominating sets generally (arXiv:1208.5345), without shortest-path profiles. Suzuki et al. use add/delete reconfiguration under a cardinality cap (arXiv:1401.5714), which is distinct from exact-minimum exchanges. Aichholzer et al. (arXiv:2508.18457, Theorem 4.10) already provide a related alternating-cycle distance formula for a crossing-free geometric union; embedding any union of two complete-graph matchings in a suitable circular ordering shows the bare distance formula is not independently novel. Brenner et al. (arXiv:2607.04687, Theorem 3) prove Hamilton-connectedness of the same one-flip state graph but not the complete distance-sphere polynomial. Searches of published mathematical records and historical claims found no exact sphere-count coverage; unindexed prior tables or equivalent enumerators remain possible. This is a qualified self-review, not an independent priority certificate.

## Value

PASS. All-pairs distances are a canonical quantitative invariant for local reconfiguration. A single exact exponential generating function resolves the entire distance distribution on an infinite vertex-transitive graph family and yields parity-sensitive counts of farthest configurations. These counts are not contained in the prior general connectivity, diameter-order, or Hamiltonicity statements and are directly useful for studying random-pair transport or benchmarking reconfiguration sampling.

## Limits and close literature

The known distance expression is explicitly treated as prior context. The original claim adds the exact sphere enumeration; this claim is limited to complete odd graphs viewed as minimum-dominating-set reconfiguration of their line graphs. The 2012 paper is an enumeration algorithm for minimal (not specifically minimum) dominating sets; the 2025 paper is a broader flip-distance treatment; the 2026 paper is Hamiltonian rather than enumerative. No external independent validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
