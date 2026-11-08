# Mathematical review

## Correctness — PASS

A fixed configuration on the simple four-regular graph \(C_n\square K_3\) is equivalent, bit by bit, to the six explicit local inequalities in RESULT.md. The 64-state directed-pair matrix is exhaustively defined by those inequalities. Cyclic trace counts are bijective for every \(n\ge3\). The exact integer characteristic polynomial and four strict Schur reductions are reconstructed by the supplied standalone checker; these yield the claimed root-power census and the asymptotic \(3^n+O(2^n)\) for all lengths, without assuming the matrix is diagonalizable. Independent direct majority simulation agrees for 2,396,672 bounded configurations. Direct simulation alone is only a finite cross-check.

## Originality — PASS, with priority qualification

The nearest historical majority enumeration (Agur, Fraenkel and Klein, 1988) concerns a single cycle's self-inclusive one-dimensional rule, rather than a three-column cross-section with four neighbors and ties. Nakar and Ron (2022) likewise address one-dimensional majority cellular automata, not the Cartesian product with triangles. Benjamini et al. (2014) cover majority periodicity and random-graph behavior, not exact fixed-point counts on this deterministic three-rail family. The known universal eventual period-two result does not imply the number initially fixed. Prior fixed/period-two censuses for two-row ladders and trees also concern different neighborhoods and do not imply this root decomposition. Indexed searches found no source matching both the object and coefficient statement. This is not proof of priority; unindexed transfer calculations or equivalent recurrences remain possible.

## Value — PASS

This is a complete exact infinite-size census for the first nontrivial triangular column coupling of cyclic majority dynamics. The 64-state transition is reduced to four explicit degree-at-most-four correction factors and a sharp universal fixed-state entropy \((\log3)/3\) per vertex, with a provably vanishing fixed-point fraction. Distinguishing the coupled three-rail four-neighbor setting from a one-dimensional cyclic rule and resolving the exact growth base is a natural recurrent-state counting question, not a mere finite numerical lookup.

## Sources and limits

Agur–Fraenkel–Klein (1988), open full PDF https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf ; Benjamini et al., arXiv:1405.2486v1 (2014), full preprint https://arxiv.org/pdf/1405.2486 ; Nakar–Ron, arXiv:2205.08972 (2022), full preprint https://arxiv.org/pdf/2205.08972 . These are not claimed to exhaust historical literature. The present proof does not classify transients or two-cycles.

Self-review: passed. Independent audit: not yet performed.
