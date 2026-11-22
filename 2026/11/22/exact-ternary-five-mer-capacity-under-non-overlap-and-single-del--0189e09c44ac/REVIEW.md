# Scientific review

## Correctness — PASS

The prefix-suffix condition and deletion-confusability condition are defined for all ordered codeword pairs, including self-overlap checks. The length-five upper bound has a direct integer conflict-clique-cover certificate on the 48 normal-form words: 28 pairwise-incompatible groups, denominator 16, total group numerator 98, and coverage at least 16 for every source. The normal-form reduction applies to *every* ternary non-overlapping code because first- and last-symbol sets are disjoint. An explicit six-word code attains the upper bound. The complete 72-code census and seven-orbit decomposition are reconstructed by a second exact graph enumeration, while an independent longest-common-subsequence-based program counts 12 canonical-orientation optima. Both programs were replayed and passed. No floating-point computation is needed for correctness.

## Originality — PASS, qualified

Blackburn (2013/2015) treats non-overlapping codes without the simultaneous deletion correction, the published exact length-five ternary maximum 17 refers to the broader code family, and the published length-five substitution-detection maximum 9 uses a different weaker channel condition. The binary non-overlap deletion-correction census does not dominate a ternary result, and the coincidentally equal unconstrained ternary two-deletion maximum of six cannot upper-bound a one-deletion capacity. The Wang–Fang–Feng (2025) accessible Section 4 studies Hamming spheres and partially restricted overlaps, not the exact one-deletion descendant condition. Searches also examined aliases such as cross-bifix-free, mutually uncorrelated, self-synchronizing, and single insertion correction. No indexed equivalent exact codebook census or stronger implication was located. Full-text gaps in two closely related sources and unindexed historical calculations remain risks; the priority assessment is qualified rather than a proof of absence.

## Mathematical value — PASS

Non-overlap provides framing while deletion correction resolves an unknown lost symbol. Their joint short-block capacity is a natural coding-design parameter, not an arbitrary selection of words. The ternary five-mer is the first small instance in this census with six messages, and the sharp cost from 17 to 6 is substantial. A short exact upper certificate and the complete seven-class optimizer census make the finite result reusable as a concrete synchronization-code benchmark. No unwarranted asymptotic or streaming reliability claim is made.

Self-review: passed. Independent audit: not yet performed.
