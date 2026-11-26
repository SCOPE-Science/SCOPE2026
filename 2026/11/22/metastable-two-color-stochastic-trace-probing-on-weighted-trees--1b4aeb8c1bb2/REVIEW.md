# Independent mathematical audit

## correctness

PASS

The supported Rademacher quadratic form has centered terms 2G_ij ξ_iξ_j for within-class distinct unordered pairs; those terms are uncorrelated except for identical pairs. This gives the stated factor 4 and flip gap −4∑_{i in S,j outside S} b_i b_j G_ij². Independently built the inverse by eliminating the five leaf coordinates and inverting the resulting 2×2 center block, verified QG=I as a rational-function identity, and reproduced every singleton, bridge and specified competitor gap (RESULT.md lines 53–84). The leaf gaps force x>α, the competitor forces x<β, and the remaining gaps are strictly positive there by the displayed factorizations. The interval is sharp for this conjunction, not a classification of all local traps. At x=1/3 independent enumeration over 63 admissible unlabeled partitions gave variances 384984171/95452900 for the proper coloring and 377990793/95452900 for the optimum, attained exactly by the three stated colorings. All grouped entries, including the harmless inadmissible constant-sign row entry, match. Reproduce this finite certificate with python /workspace/review-4-exact.py (SymPy); the supplied scripts were only inspected. For each fixed number of new leaves, at μ=1/3 the old gaps persist by continuity as ε→0. In the new-leaf row, G_zj=εG_3j/(μ+ε) for j≠z, so the new-new cross entries are O(ε²); the leading new-leaf variance gap is 4(ε/μ)² times H_3, independently verified as 223184259/190905800>0. The leaf-component move equals its singleton up to a global sign, and the competitor remains better. This establishes the arbitrary-order result for sufficiently small positive ε at each order, without requiring a common ε or the full screening window at every order.

## originality

PASS

The exact variance functional is established background, and prior studies optimize it on other graph families. The supported distinct claim is the simultaneous strict local trap for bridge and singleton flips in a positively weighted branched tree, with a specified exact screening interval, global classification at one screening, and extension to each larger order. No inspected theorem gives that conjunction.

## value

PASS

A proper bipartition is a natural low-cost default for trace probing on a tree; strict stability under both readily interpretable neighborhoods makes it a genuine obstruction to improving that default by either move family, rather than merely a bad coloring. The rigorous window and growth construction rule out an isolated numerical tie or fixed-order anomaly. The claim is existential, not a claim about minimal witness size, typicality, or all refinement heuristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
