# Independent mathematical audit

## correctness

PASS

A synchronous scan retaining both deletion flags and at most one unmatched survivor bit exactly represents existential common one-deletion outputs: before either deletion, prefixes must match; after one deletion there is one unmatched survivor on the longer track; after both deletions there is again no lag and equality is required. Previous source bits reject 11, never imposing an output constraint. Keeping a set of alignments makes acceptance count an input once, regardless of witnesses. Independently constructed the raw automaton by appending the kept bits and cancelling their common prefix; refined its 17 states to 12 counted-equivalence classes, 9 productive. Independently evaluated the raw 17-state formal resolvent by an exact determinant ratio, without the supplied quotient certificate, and verified (ordered series−vertex series+1)/2 equals the proposed all-length edge OGF. The +1 corrects for the empty word rejected by the pair reader; for n≥1 every diagonal is accepted and both edge orientations appear. Hamming edges are counted by flipping each 1 to 0 from the heavier endpoint once; the marked Fibonacci-language series (1+tz)/(1−z−tz²) yields z/(1−z−z²)^2, and subtracting gives the asserted extra term. The unique dominant pole is φ^−1 of order three, with coefficient φ³/(5√5) of (1−φz)^−3; the vertex asymptotic φ^(n+2)/√5 gives both stated constants. Replay python3 /workspace/branches/deletion_replay.py verified the exact resolvent and pole constant plus literal bit-deletion shadow counts through n=15 (including all ten reported terms). The finite list checks interpretation, not the all-length identity. Frozen artifacts were inspected, not executed.

## originality

PASS

The deletion graph framework and Hamming-edge summand are known. A prior larger Fibonacci-Hamming variant also encompasses the two-read part, with an exact edge count, but not the full target. The supported distinct contribution is the all-length count including exactly-one-output pairs outside ordinary Hamming adjacency and the resulting cubic-pole law.

## value

PASS

The count is a natural exact invariant of a deletion channel constrained by a standard forbidden factor, not an arbitrary graph slice. It quantifies the conflict contribution that the usual Hamming graph and two-read criterion miss and establishes quadratic mean degree at all-length scale. It provides a useful benchmark for constrained coding and graph calculations without purporting to solve maximum code size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
