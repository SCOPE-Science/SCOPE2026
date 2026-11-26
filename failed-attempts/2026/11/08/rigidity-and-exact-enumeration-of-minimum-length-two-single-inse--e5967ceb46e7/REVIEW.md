# Independent mathematical audit

## correctness

PASS

Each aaa forces aa into the code; those diagonal pairs also cover all words with repeated letters. Taking the complement on off-diagonal ordered pairs converts every remaining forbidden uncovered word abc into the non-induced transitive triangle a→b, a→c, b→c, with opposite arcs allowed. In a feasible digraph, endpoints of any arc have disjoint out-neighborhoods and disjoint in-neighborhoods. Summing the degree bounds on arcs gives Σ_v d(v)^2≤2qE; Cauchy–Schwarz gives 4E²/q≤Σ_v d(v)^2. The bidirected balanced bipartite construction attains floor(q²/2) arcs. At even q, equality packs the out-neighborhoods across each arc into all q vertices, forcing the reverse arc, after which Mantel equality gives the balanced bipartition. At odd q=2m+1, an extremizer has some vertex of total degree at most 2m; removing it and applying the even bound forces degree exactly 2m and an even extremizer on the other vertices. Each of the deleted vertex's in- and out-neighborhoods must be one whole side of that K_{m,m}, as both are independent and their sizes sum to 2m. They must be the same side, since different sides yield a transitive triangle through the deleted vertex. This establishes exactly the stated codebooks including q=2 and q=3. The labeled count follows by choosing the smaller part, or halving for equal parts; all are conjugate under relabeling. Independently, `python3 /workspace/branches/independent_math_replay.py 2` used direct set-cover recursion on ordered distinct-letter words for q=2..5; it returned (size, count)=(2,1),(5,3),(8,3),(13,10) and found only the asserted partitions. This finite check is not the all-q argument.

## originality

FAIL

The finite directed Turán classification already gives the full codebook rigidity, not just the scalar bound. Lemma 4.1 of Kühn–Osthus–Townsend–Zhao applies exactly to the complement model at (k,n,a)=(2,q,2) and proves uniqueness of the bidirected balanced bipartition. The labeled count then follows by counting the placements of that unique extremizer. Their proof explicitly credits the a=2 case to Brown–Harary (1970).

## value

FAIL

Classifying arbitrary optimizers rather than just giving their cardinality is a natural question. Here, however, the claimed classification is a direct transfer of an existing exact extremal theorem; its label count and one-orbit assertion are simple consequences. The elementary proof is useful exposition but the record does not establish an additional nonmechanical scientific claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
