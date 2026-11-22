# Scientific assessment

## Correctness — PASS

The claim specifies both edge-distance separation and radius-one vertex–edge coverage. On the 14-vertex, 21-edge Fano incidence graph, exact predicates reduce the claim to a finite exhaustive domain of 6,476 subsets of cardinality at most six and, for the 1,386 qualifying minimizers, all potential one-vertex exchanges. `verify_incidence.py` and `verify_binary.py` use distinct incidence representations and independently verify 168 five-vertex edge-metric bases, none additionally vertex–edge dominating; 1,386 qualifying six-sets and their five-basis containment profile; 17,514 unrestricted replacement edges; 5,040 adjacent replacement edges; all-pairs connectivity and sharp diameters six and nine, respectively. The original-graph radius-one cover condition is proved equivalent to distance-to-edge at most one. Both programs were executed from the package, not inferred from saved logs. The 11 automorphism orbits are exhaustively certified by the first program.

## Originality — PASS (qualified)

The 2022 source arXiv:2211.09327 introduces the combined predicate and gives formulas on common graph families but not on the Heawood graph. The 2016 full primary text arXiv:1602.00291 concerns edge distinguishability without vertex–edge coverage. The full published Heawood minimum edge-metric-basis result (identifier `2026/11/8/SCOPE-edge-metric-bases-of-the-heawood-graph-and-octagonal-slide-recon--d4a919fbecfd`) proves 168 size-five bases and a disconnected 21-cycle-family slide graph under the **weaker** predicate. The current stronger predicate excludes each of those five-bases, yields a larger optimum family not obtained by merely renaming or reusing their reconfiguration graph, and has different, connected slide geometry. Targeted indexed mathematical and literature queries found no theorem covering the joint six-set census and mobility metrics. Absence from a search index is not proof of priority; unindexed alternatives remain possible.

## Value — PASS

The conjunction of edge identification and local edge coverage is a natural sensor-design constraint introduced in 2022, not an invented arbitrary optimization criterion. The Heawood graph is a canonical symmetric cubic incidence network, so the exact cost of adding coverage to edge identification has an interpretable baseline: precisely one extra sensor, yet a nontrivial change from 21 isolated 8-cycles among the weaker optima to a connected 1,386-state local mobility graph. The count of 574 optimal configurations containing no five-landmark edge-resolving subset demonstrates that this is not merely a blanket one-token augmentation of the known solutions. Eleven full-automorphism orbits make this a classification, not just a single minimum number. The claim is finite and does not imply a projective-plane all-order theorem.

## Closest literature and remaining limits

The relevant 2016, 2022 and indexed Heawood primary texts were compared at the level of predicates, underlying graph, solution family and transitions, rather than titles. General earlier edge-resolution results are not claimed as new. Unindexed prior work and alternate naming may still contain equivalent six-set calculations. Scripts are reproducible but not an independent scholarly audit.

Self-review: passed. Independent audit: not yet performed.
