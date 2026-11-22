# Scientific review

## Correctness — PASS

The quadratic Rademacher variance is derived from independent class-supported probe vectors and is used in exact rational comparisons. The seven-vertex precision matrix is invertible for every positive screening shift. `verify_symbolic.py` reproduces every rational-function gap identity; `verify_exact.py` independently reconstructs the rational inverse and all sixty-four sign assignments with a complete grouped table. The analytic screening interval follows from signed polynomial factors and positive denominators. For arbitrary finite numbers of weakly attached leaves, a positive leading \(\varepsilon^2\) singleton gap, uniform continuity across the finitely many old moves, and a persistent strict global improvement prove the extension. The perturbation result does not rely on extrapolating seven-vertex enumeration to infinite size.

## Originality — PASS, with residual risks

The first full-text baseline (Stathopoulos–Laeuchli–Orginos, arXiv:1302.4018) develops inverse-trace hierarchical distance probing. Frommer–Schimmel–Schweitzer (arXiv:2009.01589) studies decay/error bounds for probing with distance-color partitions. Frommer–Rinelli–Schweitzer (arXiv:2308.07722) supplies exact supported-Rademacher variance formulas. These do not imply strict local optimality of a proper bipartition under both vertex and edge-component moves at the same time as a strict global defeat, much less a robust arbitrary-order family. Searches of indexed research findings located complete-bipartite two-color threshold results, cycle/hypercube checkerboard optima, and path optima; their restricted graph families and global classifications do not cover the constructed weighted-tree metastability statement. Search absence does not prove priority, and possible unindexed, unpublished, or differently named equivalent examples remain risks.

## Value — PASS

A proper two-coloring is natural for bipartite trees and inexpensive to construct. The result proves that optimizing exact stochastic trace variance is a different problem from proper graph coloring: the proper coloring can be a strict local trap even under the stronger one-edge-component move neighborhood. An exact nontrivial screening interval makes the failure robust in a physical regularization parameter, and a positive-conductance infinite family shows it is not solely a tiny-graph curiosity. This gives a mathematically motivated boundary for local partition-refinement heuristics without claiming their overall practical failure rate.

## Limits

The result is existential and supplies no guarantee about typical random weights or alternative search neighborhoods; seven-vertex optimality is exhaustively verified but minimality among smaller trees is not claimed. It is unknown whether historical literature contains an equivalent result outside the inspected evidence.

Self-review: passed. Independent audit: not yet performed.
