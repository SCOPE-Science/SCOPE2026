# Scientific assessment: exact constrained Černý reset length

## Correctness — PASS

The claim defines the exact transition table and the forbidden literal factor. Removing initial cyclic shifts, redundant repeated idempotent letters and terminal rotations normalizes a shortest constrained reset word to `b (ab|aab)*`. On the image after its initial `b`, the two blocks act as a cyclic permutation and a single rank-deficient map. The full inverse actions map cyclic intervals to cyclic intervals with three verified cases. The parity-sensitive potential \(g_w(r)\) obeys the explicit Bellman inequalities on every inverse step and gives the global lower bound; a descending-endpoint construction attains equality. Summing the growth and shift costs yields \(\lfloor(3n^2-8n+6)/2\rfloor\) for every \(n\ge3\). Two stand-alone checkers independently corroborate the lengths, inverse inequalities, and concrete words over stated finite domains.

## Originality — PASS, with residual risk

Full-text comparisons with the 2019 regular-constraint synchronization paper and the 2021 simple-idempotent automata paper concern existence and complexity rather than the exact shortest no-`aaa` length. Published results about weighted unrestricted Černý resets, mandatory scattered reset subsequences, early rank deficiencies, and individual inverse-image extension lengths were compared at the statement and proof level. None gives the exact minimum **under this regular-language constraint**. The previously established feasibility of rotation runs of length two is specifically not presented as new; this paper closes its separate sharp-length question. An equivalent statement in unindexed older literature remains possible. No exhaustive historical uniqueness is claimed.

## Value — PASS

The exact constrained optimum resolves a natural, algorithmically meaningful word-length objective left open by mere constrained existence. The result quantifies the penalty for a forbidden command run for every automaton order and exhibits a reusable interval-potential proof/certificate and constructive optimal control word, rather than a numerical or arbitrary small slice.

## Scope and verification limits

Two independent finite algorithms have been replayed: literal constrained subset BFS for orders three through fourteen, and full inverse-interval Dijkstra through thirty-five, all local Bellman inequalities through eighty, and explicit reset words through one hundred fifty. The infinite theorem relies on the symbolic inverse-interval proof rather than those finite cases. Historical equivalence cannot be excluded conclusively by finite indexing, and independent evaluation has not occurred.

Self-review: passed. Independent audit: not yet performed.
