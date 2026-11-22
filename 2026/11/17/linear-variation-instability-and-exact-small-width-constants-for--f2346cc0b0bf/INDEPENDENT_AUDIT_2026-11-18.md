# Independent mathematical audit

## correctness

PASS

Euclidean isotonic projection is continuous piecewise linear; every locally realizable active pattern pools connected tight blocks, and a block partition is feasible when its contracted directed quotient is acyclic, using positive relative-interior normal multipliers. This gives exact maximum over block-averaging Jacobians. The graph-variation coarea formula reduces each averaging-operator norm to binary cuts. Inspected actual verify_ladder.py and independently enumerated all feasible partitions/cuts with exact integer arithmetic: for k=2,3,4 there are respectively 10,52,272 partitions and 140,3224,69088 tests; for k=5,6 independently replayed 1424 and 7456 partitions, 1455328 and 30524864 cut tests, maxima respectively 19/10 and 9/4 with explicit equality masks. Combined constants are (1,4/3,3/2,19/10,9/4). For arbitrary k, top-row pooled local face with simultaneous binary step gives ratio 1/2+floor(k²/4)/k; order-preserving and translation-equivariant projection bounds each output edge difference by input oscillation and hence by graph variation, giving C_k≤3k−2. Therefore Θ(k), no exact k≥7 claimed.

## originality

PASS

Best-of-knowledge originality for the final precise statement, after a direct implication comparison of published SCOPE/Resultary records and primary literature; see four named checks and actual material read. Read full RESULT.md: sharp C2=1 is covered by its entire-Hasse-undirected-cycle case. Ladders with k≥3 contain multiple square cycles and do not have entire Hasse graph a cycle, so its contractivity theorem cannot imply the 4/3,3/2,19/10,9/4 or linear-width instability. The present result correctly includes but does not claim novelty for k=2.

## value

PASS

The first strict loss of graph-edge variation nonexpansivity occurs in a minimal natural family of multidimensional isotonic grids, and the first five sharp coefficients plus explicit linear growth supply exact stability data beyond Euclidean nonexpansivity. This is a motivated finite natural classification and an infinite-width structural instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
