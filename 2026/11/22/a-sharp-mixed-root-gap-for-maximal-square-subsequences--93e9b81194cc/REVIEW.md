# Mathematical review

## Correctness: PASS
The root-order equivalence is proven directly. No host shorter than seven can witness the mixed-root separation, and the seven-symbol equality classification is reduced to four possible three-letter longer roots, with a fully enumerated one-insertion table. Two independent exhaustive implementations agree on all eight witnesses. The infinite family is proved for every integer \(m\ge3\) by a two-marker central-gap obstruction: any mixed root has length at most two, the root `10` is maximal, and the best pure-zero root has length exactly \(m\). Bounded program checks are corroboration, not the infinite proof.

## Originality: PASS against inspected literature
The 2026 paper of Gong, Liyanage, Sopp and Zhu provides the definition, a root-order lemma, and algorithms for producing a maximal square but does not identify the exact smallest mixed-root gap, its eight equality hosts, or the unbounded mixed-root length discrepancy in its inspected full HTML text. Inoue--Inenaga--Bannai and Kosowski treat longest-square computation. Published spectra for repeated permutations enumerate roots rather than inclusion-maximal roots of general hosts; formulas for binary two-run powers optimize in a different host family; two-marker shuffle-square classifications employ a different membership predicate. Indexed similarity results and direct sources were compared by implications, not title alone. Unindexed prior examples remain a real priority risk.

## Value: PASS
The distinction between maximum and inclusion-maximal repeating patterns is algorithmically motivated by the 2026 near-linear maximal construction. The theorem establishes a sharp first mixed-letter obstruction with a complete eight-instance equality census, and a structural unbounded-gap family demonstrating why maximality itself cannot guarantee even a constant-factor approximation to maximum length. This is a worst-case property of the feasible-solution poset, not a claim about any particular algorithm's output.

## Limitations
The sharp finite enumeration concerns seven-symbol binary hosts; the larger family supplies examples rather than a universal optimal gap formula. Independent validation has not been performed; historical priority cannot be proved by searches alone.

Self-review: passed. Independent audit: not yet performed.
