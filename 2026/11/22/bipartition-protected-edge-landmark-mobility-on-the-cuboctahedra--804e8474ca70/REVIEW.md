# Scientific review: cuboctahedral edge-landmark mobility

## Correctness — PASS

Two explicit reconstructions of the twelve-vertex cuboctahedron, one as \(L(Q_3)\) and the other from Cartesian coordinates, agree. The first checker enumerates all \(495\) four-subsets and all \(792\) five-subsets, obtaining zero and \(168\) edge-resolving sets respectively; the second checker uses an independent witness-mask characterization. Both exhaustively generate all legal one-token moves and compute all component eccentricities. The parity obstruction is proved combinatorially: a slide of cube edges sharing a corner changes only one bipartition side, while every optimum covers exactly three corners on one side and four on the other. The two independent output files agree on all reported counts and metrics. This verifies the exact finite claim, not generalizations.

## Originality — PASS, qualified

Actual published-finding corpus searches for edge-metric landmark mobility, the cuboctahedron, \(L(Q_3)\), \(168\) optima, \(84\)-component parity and aliases returned related but noncovering records, including exact edge-metric results on the Heawood and Chvátal graphs and different cuboctahedral invariants. Searches of the public web for "cuboctahedral edge metric dimension", "line graph of cube edge metric dimension" and "edge metric basis reconfiguration cuboctahedron" yielded no covering primary theorem or exact table. Examination of Yi's 2021 edge-dimension paper shows general results rather than this graph-specific optimizer classification; Avis–Hoang concerns independent sets, not the edge-resolving predicate. MathWorld identifies the base graph but supplies no optimum-set geometry. The exact statement and implication comparisons are recorded in AUDIT.json. These searches support a best-knowledge novelty assessment, not proof of priority; an unindexed or unpublished equivalent remains possible.

## Value — PASS

The finite result identifies a natural, structurally motivated disconnection invariant in the minimum edge-failure-localization sensors of a canonical polyhedral network. The sharp difference from ordinary vertex localization on the same graph—two immovable-with-respect-to-each-other edge-basis communities versus one connected metric-basis slide network—clarifies which sensor task controls mobility. The exact \(84\)-state component sizes and radius/diameter provide reproducible relocation benchmarks, not arbitrary sampled constants. The invariant supplies a conceptual explanation for disconnectedness beyond raw exhaustive counts. The claim remains valuable even though it is limited to one canonical graph.

## Closest sources and limitations

- Yi, *On the edge dimension and fractional edge dimension of graphs*, arXiv:2103.07375 (first posted 2021-03-12); general edge dimension and fractional edge dimensions, not exact cuboctahedral reconfiguration.
- Avis and Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (first posted 2022-03-31); reconfiguration graph framework for a different feasibility class.
- MathWorld, *Cuboctahedral Graph*; confirms the twelve-vertex line-graph representation, not minimum edge bases.
- Published indexed records on the Heawood and Chvátal edge-metric basis graphs; distinct base graphs and no general result implying the present enumerator.

The result is a finite theorem with reproducible exhaustive checkers, not an assertion of an infinite-dimension pattern. No external independent audit was performed; historical-priority uncertainty remains.

Self-review: passed. Independent audit: not yet performed.
