# Independent mathematical audit

## correctness

PASS

The stated all-order run threshold is correct. Removing initial/terminal rotations and adjacent duplicate b's preserves synchronization and admissibility; on S={0,...,n−2}, ab is a cycle, so words without aa cannot reset. For m=n−1 the block aab(ab)^(m−1) sends each i<m−1 to i+1 and fixes m−1 (including m=2); repeating m−1 times after b works, has no aaa, and gives length 2n²−5n+3. An independently written exact backward search reproduced every length for 3≤n≤24 and replayed every stored word from every starting state. Each layer is a preimage of a terminal singleton under a suffix, with the suffix's leading a-run recorded. Prepending a uses inverse rotation and is forbidden at run two; prepending b forces membership of n−1 to match membership of 0 and resets the run. Empty preimages never grow, and first arrival at Q among the three run states proves the minimum. This verifies the finite formula, not an extrapolation of the frozen proof. The source's parenthetical assertion that every reachable subset is processed before Dijkstra terminates is unnecessary and not literally true: settling distances below the first singleton is sufficient.

## originality

FAIL

Distinct catalogue results demonstrably cover both main parts: the exact no-triple-rotation theorem uses the identical automaton, contiguity constraint and exact expression for every n≥3; a separate sharp two-rotation-run theorem explicitly includes impossibility at run bound one and feasibility at two for every n≥3. This is a finding of mathematical coverage in the checked corpus, not a finding of historical priority; the covering records carry a later catalogue date.

## value

FAIL

The contiguous-run constraint on a canonical worst-case automaton motivates a real exact invariant, and an independent exact-replay benchmark is useful as corroboration. But as a distinct mathematical contribution the all-order feasibility theorem is already matched and the 22 finite optima are contained in a constructive all-order formula. Neither alternative witnesses nor smaller search graphs establish a distinct valuable invariant here. Extending the frozen length claim to all orders would also be covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
