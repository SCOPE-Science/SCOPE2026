# Mathematical review

## Correctness — PASS

The invariant is defined by distances from each of the fifteen Petersen edges to nonempty blocks in a vertex partition. Both independently written exhaustive verifiers visit all \(115975\) unordered ten-element set partitions. They return no solutions with fewer than four blocks, exactly forty four-block solutions, and the same full higher-cardinality polynomial. The programs independently generate \(KG(5,2)\) and \(GP(5,2)\); a direct four-block example has fifteen pairwise distinct edge signatures. The three-block necessary-condition screen checks \(9330\) partitions, with exactly \(105\), then \(15\), candidates surviving successive crossing-edge filters, none resolving. All forty optima are in one orbit under a 120-element automorphism action. Complete checker sources and expected outputs are included.

## Originality — PASS (provisional historical priority)

Kuziak–Maritz–Vetrík–Yero (2023) introduced the invariant and established bounds, but their paper has no Petersen-specific edge-resolving partition theorem. Ali–Ahmad–Jamil (2024), Theorem 16 and Table 10, explicitly report the incompatible minimum six; the new four-block witness disproves this published scalar conclusion. A previously published result enumerating 7040 *vertex*-resolving Petersen partitions was compared using its full RESULT.md; resolving ten vertices does not imply resolving fifteen edges, and its result does not give the forty edge-resolving partitions. A further full-text comparison found a separate forty-state proper distinguishing-colouring orbit, but its block sizes are \(4,2,2,2\), unlike the present \(1,3,3,3\), and all its blocks are independent, unlike these induced-path triples. Database and literature searches did not identify a covering enumeration. Unindexed publications remain a priority risk.

## Mathematical value — PASS

The Petersen graph is a canonical symmetric graph against which the recently introduced invariant can be calibrated. Establishing its correct sharp minimum and the entire forty-minimum single-orbit family resolves a concrete published discrepancy and gives a reproducible complete benchmark. The full partition polynomial also records how resolution changes as partition granularity increases; this is not a renamed vertex-partition table.

## Sources and limitations

The defining source is the full 2023 article (DOI:10.47443/dml.2023.010). The directly competing 2024 primary paper (DOI:10.30538/psrp-odam2024.0105, published December 22) was inspected at its Petersen theorem and summary. A relevant public 7040-vertex-partition RESULT.md was read and compared by mathematical implication. The new statement is finite and specific to the Petersen graph; literature priority and mathematical correctness have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
