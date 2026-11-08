# Scientific review

## Correctness

PASS. The proof defines the precise alternating order and treats primitivity, parity and all length boundaries. The original odd-border comparison gives the parity obstruction; an independent two-rotation argument shows that odd periods of at most half the word length are impossible. Explicit words achieve each permitted border length, with all possible competing rotations classified at their first mismatch. The extracted verifier exhausts binary words through length 16 and directly checks constructions through length 256. Finite verification alone does not establish the unbounded claim.

## Originality

PASS with bibliographic risk. Reutenauer's 2006 Proposition 3.1 and Dolce–Restivo–Reutenauer's 2019 Lemma 35 supply only the odd-border parity condition, which is explicitly credited. The 2024 Galois algorithm paper contains a period framework and restates the parity condition, but the inspected full HTML did not contain the exact parity-dependent attainable spectrum or complete binary witness family. Bannai et al. (2023) discuss the unresolved algorithmic difficulty of bordered Galois subsequences rather than realizing border lengths. Searches for equivalent phrases, general periodicity consequences, broader theorems and exact tables did not identify equivalent coverage; an unindexed equivalent is possible.

## Value

PASS. The border spectrum is a natural structural invariant for alternating-order Lyndon (Galois) words. It closes the gap between the necessary odd-border condition and realizability by finding an additional sharp half-length obstruction at even word lengths, and it supplies explicit witnesses for all remaining values over every non-unary alphabet. This is a complete infinite-parameter classification, not a routine fixed instance; the statement does not imply an algorithm for subsequence optimization.

Self-review: passed. Independent audit: not yet performed.
