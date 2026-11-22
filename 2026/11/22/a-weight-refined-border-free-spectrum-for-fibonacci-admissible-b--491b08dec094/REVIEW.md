# Mathematical review

## Correctness — PASS

The unbordered shortest-border decomposition is bijective and exhaustive. Length-one shortest borders `0` and `1` require separate junction constraints; longer shortest borders begin and end differently. These three groups yield the weight-refined Mahler functional equation and its all-length coefficient recurrence. The scalar Fibonacci convolution proves the limit after absolute convergence, with an explicit tail bound. The two alternative verification programs passed exhaustive prefix/suffix checks through length \(21\) and polynomial sandwich recurrence through length \(150\), respectively. Computations support the proof, but the symbolic decomposition and Binet bounds establish the infinite assertions.

## Originality — PASS, qualified

The 2004-11-11 OEIS fixed-weight table and its Harju–Nowotka reference enumerate unbordered words without forbidding adjacent ones. The Gabric–Shallit 2023 presentation gives the classical unrestricted unbordered recurrence, while Nyblom 2013 treats palindromes under run avoidance. The closest published records found address Abelian border variants or sparse-marker subsets; these do not imply the claimed combined adjacency-constrained weight spectrum. Searches included aliases, fixed-weight tables, generating functions, and Fibonacci-admissible words. The 2004 report's entire text remained unavailable, and an earlier unindexed equivalent remains a genuine priority risk; no stronger prior covering theorem was established from accessible material.

## Value — PASS

Border-free words have a specific structural role in string matching and synchronization: a word without a proper self-overlap cannot overlap a copy of itself by a nonzero shift shorter than its length. The natural finite-type source forbidding consecutive ones changes both the exact border-free enumeration and its proportion of the admissible source. The theorem gives a complete weight-refined answer plus a rigorously positive limiting prevalence; it does not claim maximum packing across multiple words.

## Scope and limitations

All results concern linear binary strings avoiding `11`, not cyclic words, Abelian borders, or cross-bifix-free sets. First public foundational date refers to the 2004 mathematical unbordered-weight enumeration, not to publication of this derived constrained identity. Priority remains qualified and independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
