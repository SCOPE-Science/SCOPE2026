# Self-review

## Correctness — PASS

The claim has a complete proof for each integer \(r\ge2\) and \(k\ge1\), over precisely the binary alphabet. Minimal absence is characterized by greedy prefix existence, terminal nonoccurrence, and all intervening deletion bridges. The possible greedy states and first-match transitions for the periodic host \((0^r1)^k\) are exhausted explicitly. Boundary-crossing terminal choices are counted exactly once. Algebraic elimination of the weighted state equations gives the claimed bivariate rational generating function, whose specialization \(t=1\) yields \(3\cdot2^{k-1}\). No infinite claim is inferred from finite enumeration. The included independent `verify.py` passed 131 parameter/spectrum comparisons, including 19 direct literal-host/brute candidate-set checks and 11,133,114 candidate words; additional symbolic manipulation confirmed the rational expression. This verifies the nonstandard local state construction and all inspected boundary cases.

## Originality — PASS, with residual bibliographic risks

The closest primary paper is Kosche, Koß, Manea and Siemer, *Absent Subsequences in Words* (arXiv:2108.13968), whose full-text Theorem 3.1 gives the general MAS bridge characterization. Their Proposition 3.8 treats repetition of a block of distinct letters, not the repeated-symbol blocks \((0^r1)^k\), and does not state the present all-length rational spectrum or its run-length invariance. Manea et al. (arXiv:2504.21471) supply general enumeration algorithms, not this exact family formula. Adamson et al. (arXiv:2407.18599) optimize the number of all absent subsequences, not distinct minimal absent words. A broader theorem would cover this claim if it provided the actual coefficient distribution; no such implication was found. Search comparisons against existing published records and the accessible prior claim ledger did not identify the same theorem; the previously recorded alternating binary and ternary-permutation instances are different host families and do not imply it. The 2023 chapter by Troníček was identified by title/abstract but not inspected in full, leaving a specific overlap risk. Unknown or unindexed equivalent results cannot be excluded by search alone.

## Mathematical value — PASS

Periodic hosts with unbalanced letter multiplicities are the first natural departure from the distinct-symbol permutation-block model for minimal absent scattered subsequences. The result determines the exact length distribution for *all* repetition counts and all zero-run lengths, not a small numerical table. Its run-length-invariant total is mathematically surprising: the entire length spectrum varies with \(r\), while the total collapses to \(3\cdot2^{k-1}\) for every \(r\ge2\). The result exposes a real boundary at the alternating period \(r=1\) and motivates more general periodic-block classifications. It is neither a substitution of previously published enumeration formulas nor a routine computational exercise.

## Limitations and residual risks

The statement concerns scattered subsequences, not contiguous factors; it excludes \(r=1\) and arbitrary nonconstant periods. The mathematical proof is self-contained but its scientific originality remains subject to external peer evaluation, especially in view of the inaccessible full 2023 Troníček chapter and possible unindexed examples. The included finite computer checks are supporting evidence, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
