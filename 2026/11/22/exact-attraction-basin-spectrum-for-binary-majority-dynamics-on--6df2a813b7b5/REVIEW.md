# Mathematical review: Desargues majority basin census

## Correctness — PASS

All 1,048,576 labelled input states are classified by a direct exhaustive 20-vertex majority-map computation, independently reproduced by an exact base-graph phase convolution with a checked graph-isomorphism witness. The base map on 1,024 Petersen colourings has 124 recurrent phases with phase-preimage multiplicities 72 occurrences of 1, 50 of 10 and two of 226. The identity \(T(x,y)=(f(y),f(x))\) converts the phase multiplicities into every fixed-point and two-cycle basin size. The two weighted basin totals, 107,224 and 941,352, account for the full state space. The separate first-entry-time count gives a sharp four-update cutoff. The finite nature of the problem makes the complete enumerations exhaustive, unlike sampled experiments.

## Originality — PASS, qualified

Adam, Dahleh and Ozdaglar (arXiv:1211.0654, Definition 4.14 and Lemma 6.10) already supply the bipartite expansion construction and an exact general cycle-count identity; those are expressly excluded from the novel contribution. Benjamini et al. (arXiv:1405.2486) give the general period-two property, and Kaaser et al. (arXiv:1508.03519) give general voting-time results. The checked results do not furnish the Desargues graph's nine-class **individual attraction-basin spectrum**, the base phase-preimage multiplicities (1, 10, 226), or its exact entry-time population. Closest published research records concern other graph families, including the dodecahedron and Heawood graph. Search non-detection is not proof of global novelty: an equivalent unindexed census or an undiscovered exhaustive table remains a residual historical-priority risk.

## Value — PASS

The Desargues graph is a natural, highly symmetric 20-vertex cubic graph and the bipartite cover of the Petersen graph, not a parameter chosen to manufacture a count. Existing orbit-count results do not determine individual attractor-basin populations. The exact full basin-size spectrum reveals sharply unequal attraction (from 1 to 102,152 configurations), a large anticonsensus oscillator whose basin matches the combined unanimous basins, and a complete sharp time-to-recurrence distribution. These facts provide a reproducible benchmark for nonlinear consensus/oscillation on a standard distance-transitive graph, without claiming a graph-universal extension.

## Closest literature and limitations

The principal overlap is the 2012 bipartite-expansion and orbit-count theory (not a new claim). Other checked general theories do not assert this precise basin census. Scientific scope is a finite labelled state space, and its calculation has not been independently peer reviewed. Unindexed equivalent work cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
