# Scientific review

## Correctness: PASS

The claim concerns a finite, explicitly specified 15-vertex graph and all its 3^15 labelled initial states, not a sample or an unbounded family. The Petersen-to-line-graph construction is checked for degree four by two presentations, and the exact update rule is independently encoded in two standalone programs. A functional-graph indegree decomposition and a different direct-trajectory decomposition agree on all four threshold-specific period counts, full entry-time/least-period cross tables, and every individual basin-size histogram. The reproducible `replay.py` reconstructs and replays both programs from supplied sources, checks the exact expected totals, and fails on any disagreement. A six-update extinction witness and a twelve-update periodic-entry witness prove sharpness. Code execution was successful; the algorithms and full reproducibility procedure constitute the finite proof. No conclusion for arbitrary graph sizes is made.

## Originality: PASS, with specified residual priority risks

The closest recorded results are the general Tait-edge-coloring/primitive-three correspondence and half-degree balance rigidity. They exclude only period-three recurrence at threshold two on the Petersen line graph, leaving other periods, finite extinction and its sharp cutoff unresolved. The published induced-density bound cannot be applied at threshold two since this four-regular line graph has maximum induced edge density exactly two. The threshold-one literature studies finite-graph dynamical criteria but does not provide the claimed specific complete basin and attractor census. Searches for Petersen line graph excitation, alternative names, period and threshold variants, exact tables, and stronger covering theorems did not identify an implication covering the final claim. The detailed comparison and actual repository identifiers appear in `AUDIT.json`. Unindexed tables or an uninspected section of an older full paper could still bear on priority; failed searching alone was not treated as proof.

## Value: PASS

The result measures a sharp nonlinear phase transition of a canonical 15-site 4-regular network: 220,960 coexisting oscillatory cycles at one excited contact disappear completely at the next threshold, exactly at the edge-density bound's unresolved equality case. The six-update universal extinction and detailed per-period attraction basins are natural model invariants, not an arbitrary numerical slice. Their reproducible complete finite classification provides a stringent benchmark for threshold excitation dynamics and a concrete critical-equality example. No generalized graph theorem is claimed.

## Scientific limits

All computations are exhaustive only because the graph has fifteen sites. The two replayable implementations are not external independent certification. The historical priority inquiry was bounded and may omit unindexed equivalent computations.

Self-review: passed. Independent audit: not yet performed.
