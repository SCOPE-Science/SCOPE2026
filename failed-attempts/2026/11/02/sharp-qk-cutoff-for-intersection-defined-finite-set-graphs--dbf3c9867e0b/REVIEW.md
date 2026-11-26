# Independent mathematical audit

## correctness

PASS

At move t<q, a bijection of the two used ground-set unions sends all previous sets to their counterparts. The reply consists of the mapped old points and at most k new points, which exist because at least (q−t)k are unused. This works in either direction, including repeated moves, and preserves equality and all intersection sizes. For disjointness a q-clique exists exactly when n≥qk; the q nested existential quantifiers distinguish qk−1 from qk. Keeping smaller graphs and replacing larger ones by the graph at qk gives the vertex bound. The proof establishes sharpness for representatives within this family, not among arbitrary finite graphs. RESULT.md lines 14–24 and VERIFICATION.md provide a complete analytic check; no computational premise is needed.

## originality

FAIL

The uniform stabilization is a mechanical instance of the ordinary equality EF game and quantifier-rank transfer for a quantifier-free k-coordinate interpretation. Equality modulo permutation, injectivity, and every intersection rule are quantifier-free in the coordinates, so each graph quantifier costs exactly a block of at most k ground quantifiers. Pure sets of size at least qk agree to rank qk by matching previously seen points and answering a new point with a fresh point. The only remaining sharpness claim is the standard Kneser disjoint-block clique witness, and the vertex bound is immediate from these two facts. This is an implication finding, not a claim that a source printed the full arbitrary-S result verbatim.

## value

FAIL

A uniform sharp rank cutoff is a meaningful invariant in principle. Here its numerical value is just the standard quantifier-block cost of a quantifier-free interpretation, met by counting ground elements in a clique of disjoint blocks. The representative bound is a direct restatement within the family; the result does not classify below-cutoff theories or give sharper information for an individual non-disjointness rule. It is a useful elementary example, but a routine deduction rather than a separate mathematical contribution under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
