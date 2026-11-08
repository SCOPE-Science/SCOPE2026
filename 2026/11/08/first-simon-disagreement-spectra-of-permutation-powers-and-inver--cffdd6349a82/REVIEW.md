# Self-review

## Correctness — PASS

The claim concerns distinct permutations of the same \(q\)-letter alphabet, positive equal powers, and the *first* distinguishing subsequence length. Greedy embedding uses precisely one additional period at every weak descent of the letter rank. Therefore every length-at-most-\(r\) word embeds in either \(r\)-fold power, and the absent words of length \(r+1\) are exactly the descending sort of each size-\(r+1\) multiset. A multiset is absent in both powers exactly when its distinct-letter support is independent in the relative-order inversion graph; independent supports with \(j\) vertices admit \(\binom r{j-1}\) positive multiplicity assignments. The theorem, generating series, sharp bounds, equality cases, and Newton-binomial recovery all follow with the stated quantifiers and endpoint conventions. Direct enumerative checks (488 cases, 127,920 words) and independent-polynomial/rigidity checks (5,912 cases) passed. Computations are supporting finite checks, not infinite proofs.

## Originality — PASS, with residual risk

Four directly relevant full texts were consulted: *Scattered Factor Universality — The Power of the Remainder* (2021; arXiv:2104.09063), *m-Nearly k-Universal Words — Investigating Simon Congruence* (2022; arXiv:2202.07981), *\(\alpha\)-\(\beta\)-Factorization and the Binary Case of Simon's Congruence* (2023; arXiv:2306.14192), and *Absent Subsequences in Words* (2021; arXiv:2108.13968). Their universality, factorization, and absent-subsequence characterizations are general tools, not the explicit paired equal-power first-disagreement and inversion-graph transform. No inspected paper provided the two-sided witness classification, binomial independent-set formula, extremal equality characterization, or inversion-profile recovery. Related searchable research results concern insertion universality, a one-word binary distribution, and shortest absent subsequences; none covers the paired relative-order theorem. No bibliographic search proves unique priority; an equivalent unindexed specialization remains possible.

## Mathematical value — PASS

The precise invariant is motivated by the first level at which the piecewise-testable (Simon) profiles of two repeated permutation strings separate. The theorem identifies the complete finite witness language, counts it for every exponent, and turns those counts into the independent-set polynomial of a permutation inversion graph. The exact extremizers connect the smallest and largest possible disagreement to adjacent swaps and reversal, while the first coefficient recovers Kendall distance. These constitute a natural complete infinite-family structural classification, not an arbitrarily selected numerical instance or a routine fixed-parameter tabulation.

## Closest coverage and limitations

General single-word universal/absent-subsequence algorithms can compute individual examples, and standard stars-and-bars and Newton inversion supply arithmetic tools; neither alone asserts the paired inversion-support identity. The argument does not cover unequal powers, nonpermutation periods, or higher-length disagreement profiles. Independent verification and an independent priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
