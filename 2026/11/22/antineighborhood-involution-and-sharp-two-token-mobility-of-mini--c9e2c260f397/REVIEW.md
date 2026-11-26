# Independent mathematical audit

## correctness

PASS

At weight ≤5 one color covers at most ten vertices by open neighborhoods but at least eleven are blank. At weight six a class of two covers at most eight blanks: nonadjacent members have two common neighbors, while adjacent members occur in their own union of open neighborhoods. A smaller class covers at most five. Thus both classes are triples. Closed neighborhoods of distinct vertices intersect in two vertices; triple inclusion–exclusion and the two transitive triple types yield antineighborhood size three for independent and path triples and four for one-edge triples. A vertex outside N[A] must bear the other color, so the equality case forces B=F(A); the representative XOR computations and the transitivity of translations and direction permutations give F(B)=A, switching the two types. This proves feasibility and the disjoint, named-color classification. A one-copy move would keep one entire class fixed and is impossible. A fresh exhaustive audit included overlapping supports through weight six; it found 320 optima, 1,440 exact two-copy edges, degree nine, no triangles, and the common shell tuple (1,9,54,159,90,7) from all 320 starts, giving radius and diameter five. Replay: python3 /workspace/branches/9aed25f4-3652-4d2d-830b-1d9a229f6a69/clebsch_mobility_audit.py. The uploaded checkers were inspected, not executed.

## originality

PASS

Credit the same-day Clebsch power-domination record for literal coverage of the independent/path triple geometry, counts and antineighborhood involution; date does not resolve precedence. The distinct supported claim here is the optimum classification for named 2-rainbow functions and especially the simultaneous color-preserving exchange obstruction and metric. The one-support jump and slide graphs in that comparator do not establish these conclusions.

## value

PASS

The two-support equality characterization explains why every one-color copy move fails despite plentiful single-support jumps. The exact threshold of two simultaneous copies, and the connected bounded-diameter graph at that threshold, answer a natural mobility question for the canonical strongly regular graph. This value does not depend on claiming novelty for the common antineighborhood geometry or on a new general rainbow-domination method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
