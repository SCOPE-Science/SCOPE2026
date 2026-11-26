# Scientific notes

## Correctness

A radius-one correction code is an independent set in the distance-at-most-two graph on the zigzag source. Same-orientation distance is at least three, and separated swap centers give topological-order witnesses attaining the sharp cross-orientation distance at all lengths with two orientations. The exact finite graph census accounts for the maximum code sizes and multiplicities. Eight is the first conflict-free length among lengths with two orientations; the length-one singleton is also conflict-free. The accompanying reproducibility checks supplement the general combinatorial argument and certify only the finite ranges stated in `RESULT.md`.

## Relation to prior work

Classical permutation codes use the unrestricted Kendall space. The rank-deletion channel on one zigzag orientation and the graph of legal exchanges within one fixed fence have different error or edge models. The finite census and the cross-orientation bound here concern the union of both zigzag orientations in the adjacent-position Kendall space. Historical priority against uninspected sources is not established.

## Value and scope

The threshold determines when this constrained source needs no expurgation, while the matching plateau gives exact optimum sizes and counts at the two lengths just below it. The result applies only to correction of at most one adjacent-position swap with unrestricted received permutations.
