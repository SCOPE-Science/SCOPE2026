# Scientific review

## Correctness — PASS
The quantifier is over **all squarefree positive integers** satisfying the *single-redundant-divisor* relation \(\sigma(n)=3n+d\) with \(0<d<n\) and \(d\mid n\). The proof independently establishes the prime-support congruence restrictions for both parities, an exact extremal product forcing at least 122 odd prime factors, a parity obstruction for even support counts, and the complete three-case nondivisibility certificate at the first even abundance-feasible support count. The attached checker verifies the necessary exact arithmetic; no finite experiment is extended to an infinite claim without the preceding reduction.

## Originality — PASS within inspected sources
Das–Saikia (2017), the primary source for near-3-perfect numbers, proves statements about specific nonsquarefree three-prime-support shapes and gives four-prime-support constructions, not these global restrictions on squarefree numbers. OEIS A289056 records those ten special cases. Related near-perfect and multi-omission work has a different defining equation. Searches for congruence/prime-support equivalents and the precise numerical bounds did not find a covering published assertion. Accessible preceding research claims were compared for implication, not only title. The absence of a database match is not a uniqueness proof: residual literature risk remains.

## Value — PASS
The motivating generalization had examples with low prime support but no inspected global obstruction for the squarefree class. The result gives a strong and qualitatively different rarity condition: at least 15 prime factors in any squarefree case and at least 122 in the odd case, with all smaller even boundary possibilities eliminated by an exact arithmetic certificate. The combined local-divisibility and extremal-abundancy mechanism applies across an unbounded integer family. These are meaningful necessary conditions for a natural divisor-sum equation, not the verification of a few isolated numbers.

## Closest literature and limits
Das and Saikia, *On Near 3-Perfect Numbers* (2017), DOI 10.18576/sjm/040101, is the primary comparison. OEIS A289056 is only a restricted table. The theorem does **not** prove existence, nonexistence, or optimality of the 15/122 thresholds, and obscure equivalent work might remain undiscovered.

Self-review: passed. Independent audit: not yet performed.
