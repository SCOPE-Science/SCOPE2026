# Independent mathematical audit

## correctness

PASS

For every n>=3, Boolean one-hot vertex-colour tests cannot pick two colours at one vertex in a VC-shattered set. A selected 3-run requires alternating prescribed colours, and a 4-run forces an impossible trace, so 4-window double counting gives VC<=floor(3n/4); triangle is handled separately. Anti-diagonal 1110 selected runs and free gaps realize every trace, yielding equality. Online, a depth n-1 complete mistake tree fixes the first vertex colour and then queries permissible alternatives on n-2 successive vertices; the last extends. Proper-colouring count 2^n+2(-1)^n and S3 symmetry force every query-positive root subtree to contain fewer than 2^(n-1) hypotheses, precluding depth n. Independently enumerated VC at n=3..7: 2,3,3,4,5 and exact online recurrence through n=6 agrees with n-1.

## originality

PASS

PASS best-of-knowledge for the combined exact claim, specifically its sharp static VC formula and unbounded gap. The same-day published cycle-packing theorem already proves Ldim=n-1 for every unicyclic graph, so that online component is prior-covered; it does not prove or imply VC=floor(3n/4). The Oct 26 path result is related but its selected-support geometry and closure differ, so the cyclic four-window obstruction and sharp cyclic construction are nontrivial. Primary graph-colouring learning literature studies recovery of a graph from samples, not this binary query concept class. Priority of the VC formula remains bounded by searched sources.

## value

PASS

A natural connected graph family has exact VC and online learning dimensions for the same vertex-colour equality hypothesis class and a linearly growing gap. The cyclic 4-window combinatorial obstruction and constructive optimal supports are independently useful, rather than a renamed standard chromatic polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
