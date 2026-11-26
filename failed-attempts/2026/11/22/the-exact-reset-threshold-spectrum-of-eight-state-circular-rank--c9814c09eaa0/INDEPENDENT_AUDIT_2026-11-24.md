# Independent mathematical audit

## correctness

PASS

Independently filtered all 8^8 maps by rank, selected the least lexicographically packed cyclic conjugate, and used reverse preimage BFS from all singletons. The full set is reached at depth k exactly when some word of length k resets; the empty preimage is a dead state. This reproduced all 31 rows in the frozen CSV and RESULT.md, 5362560 labeled maps, 670608 classes and 2304 half-turn-fixed maps. The latter have orbits of size four; other stabilizers are excluded because the rank-six image cannot be a union of orbits of size four or eight. A constant word cannot commute with the fixed-point-free half-turn. The sole length-36 representative is 01234017; direct evaluation confirms the supplied 36-letter word ends at 0. The mean is 3322203/331840 and exactly seven classes have length at least 29. Replay: /workspace/review-check-1.py and /workspace/review-check-1.log; the frozen C++ and Python checked by inspection, not executed.

## originality

FAIL

A distinct indexed exact joint census covers the same length classification: actual summation of its 648 cells by length gives every one of the 31 frozen rotation counts, and the joint source states the very same unique length-36 representative. Labeled counts are the same marginal with the elementary half-turn weighting. This is a coverage decision, not a priority finding: the joint source itself describes the length marginal and extremum as previously established and does not claim them as new. Its reference for that marginal does not identify a dated record, so neither the direction of priority nor an external predecessor is inferred just from the two dates.

## value

FAIL

The conditional census is a well-motivated benchmark, and this independent reproduction is useful corroboration. But the exact values and extremum are already represented in a stronger available census. Marginalization, elementary stabilizer weighting, and summary statistics do not create a further scientific invariant or a valuable narrowed result here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
