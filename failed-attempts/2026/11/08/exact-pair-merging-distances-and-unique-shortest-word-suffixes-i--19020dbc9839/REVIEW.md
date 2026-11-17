# Independent mathematical audit

## correctness

PASS

For the standard Cerny n-state cyclic letter a and single-merging b, the submitted piecewise integer rank D(i,j) partitions all unordered pairs into the complete interval 1..binom(n,2). Each pair has exactly one letter reducing D by one and no letter reducing it more than one, so it equals the minimum merge length and fixes the unique shortest word. The rank-N descent gives explicit W_n whose suffixes are the unique shortest words. Independent reverse pair-BFS and rank-transition checks for n=2..26 corroborated both parity cases; all-n justification is the piecewise case proof.

## originality

FAIL

FAIL: A November 2, 2026 published stronger theorem Coordinatewise-optimal pair synchronization in the Černý automata gives the exact unique minimizing word for every pair simultaneously for ALL strictly positive letter costs, its explicit a/b Parikh vector, and the all-distinct pair-length spectrum 1..binom(n,2). For costs c_a=c_b=1 it directly implies every submitted distance and word. The earlier words form suffixes of its longest word by its explicit formulas. Its entire theorem and proof were read; no independent original remainder is present.

## value

PASS

A full shortest-pair distance spectrum and synchronized unique suffix-chain are natural precise state-merging invariants with genuine algorithmic meaning. The conclusion is valuable but already mathematically established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
