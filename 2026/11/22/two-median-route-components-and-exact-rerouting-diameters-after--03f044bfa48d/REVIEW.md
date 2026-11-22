# Self-review

## Correctness — PASS

For every pair of positive rectangle side lengths at least two and every strict interior fault, the proof identifies a unique split into two interval-defined path classes using the visit criterion \(h_j\le i\le h_{j+1}\). It reconstructs all allowed local moves, proves coordinatewise \(\ell_1\) geodesics inside each interval, derives sharp diameters and binomial counts, and verifies finite cases with a standalone route-graph checker. No extrapolation from finite experiments is needed.

## Originality — PASS (qualified)

Asplund et al. explicitly treat the intact rectangular grid as a staircase graph. Bonsma gives a general planar reachability algorithm and topological obstructions which can imply a sector separation; Bousquet et al. give parameterized complexity results; Gajjar et al. give general graph-class results. The reviewed precise fault-separated median components, their all-pairs metric and sharp parameterized diameters are not stated in the inspected material. The known staircase representation considerably reduces the proof, and an unindexed or implicit corollary remains possible; there is no claim of absolute priority.

## Value — PASS

The object is a standard shortest-route network under one failed internal routing site. Reachability alone is insufficient: the theorem determines the sharp failure-induced split, gives exact size of both surviving route families, and supplies optimal rerouting distances, maximum relocation budgets and minimal cube coordinates for every failure location. These are structurally natural fault-tolerance invariants, not arbitrary isolated parameter cases.

## Residual limitations

Only strictly interior single-vertex failures and opposite-corner terminals are addressed. The comparison to broader planar reconfiguration literature is not an exhaustive history of all possible local-fault deductions. Independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
