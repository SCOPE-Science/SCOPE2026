# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** C4-free 5-chromatic unit-distance graph in R3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1674
- **Disposition:** NO_RESULT
- **Domain:** discrete geometry / Hadwiger-Nelson in R3
- **Method:** explicit coordinates plus SAT non-4-colourability and C4 check

## Problem

Does there exist a finite point set P in R^3 whose unit-distance graph G(P) (vertices P, edges {x,y} with Euclidean distance |x-y| exactly 1) contains no 4-cycle C4 as a (not necessarily induced) subgraph and satisfies chromatic number chi(G(P)) >= 5? A complete answer either gives explicit coordinates of such a P plus verifiable certificates that all claimed unit pairs have distance exactly 1, that no four distinct points of P form a C4, and that G(P) is not 4-colourable, or proves that every finite C4-free unit-distance graph in R^3 is 4-colourable.

## Attempted claim

Does there exist a finite point set P in R^3 whose unit-distance graph G(P) (vertices P, edges {x,y} with Euclidean distance |x-y| exactly 1) contains no 4-cycle C4 as a (not necessarily induced) subgraph and satisfies chromatic number chi(G(P)) >= 5? A complete answer either gives explicit coordinates of such a P plus verifiable certificates that all claimed unit pairs have distance exactly 1, that no four distinct points of P form a C4, and that G(P) is not 4-colourable, or proves that every finite C4-free unit-distance graph in R^3 is 4-colourable.

## Research outcome

No TARGET result: the naive Mycielski candidate route was exactly tested and structurally blocked (M4/M5 contain many C4s), and no verified C4-free 5-chromatic R3 embedding or 4-colourability proof was completed; honest NO_RESULT with CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No TARGET resolution was achieved: neither an explicit exactly-verified C4-free 5-chromatic unit-distance point set in R3 nor a universal 4-colourability proof was produced. The bounded computational evidence covers only the Mycielski M4/M5 abstract-candidate screen (exact pair common-neighbour counts with witnesses, dependency-free and reproducible); it does not decide the target existence question. Numeric unit-distance embedding, symmetric-orbit search, and proof routes were not completed. The environment lacked working scientific-graph libraries (networkx import broken, scipy absent), which constrained computation to pure-python exact enumeration.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No TARGET resolution was achieved: neither an explicit exactly-verified C4-free 5-chromatic unit-distance point set in R3 nor a universal 4-colourability proof was produced. The bounded computational evidence covers only the Mycielski M4/M5 abstract-candidate screen (exact pair common-neighbour counts with witnesses, dependency-free and reproducible); it does not decide the target existence question. Numeric unit-distance embedding, symmetric-orbit search, and proof routes were not completed. T…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
