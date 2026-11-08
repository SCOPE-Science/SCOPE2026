# Scientific review

## Correctness — PASS

The exact comparison of two-length scattered-subsequence counts under one-symbol conjugation is proved, with the contribution of each moving symbol tracked for ordered distinct pairs. Every repeated-letter pair has a phase-independent count and every first-order count is fixed. Summation yields the cross-product identity with its factor \(m\), and vanishing of all cross-products forces proportional Parikh vectors because the period has strictly positive letter counts. The centered-prefix vectors implement this condition exactly. Bezout's identity proves the gcd divisibility condition. For three or more distinct single-run letters, any proper interval containing all letters contains a full interior run, excluding a proportional interval. These steps establish the entire infinite-domain result; the verifier independently builds full pair-count decks and checks 432,228 pair comparisons, not an infinite proof.

## Originality — PASS, qualified

Compared with Lejeune–Rigo–Rosenfeld (2020, Lemma 7), this result does not claim the general definition or basic equivalence-class coordinates, but derives an exact all-phase collision partition for every periodic period word and every whole-period repetition. Rigo–Stipulanti–Whiteland (2022, Definitions 1.2–1.3 and Sections 3, 7) study binomial complexity in general and several morphic settings, not this complete cyclic phase criterion. Poovanandran–Simpson–Teh (2021, Sections 3–5) investigate rotation-invariant **averages** and a binary weak-ratio multiplication identity (Corollary 4.13); their work identifies related algebra, but does not imply that every distinct-run period on three or more symbols has an injective phase deck of order two. Prior binary two-run results address a proper restricted subfamily. The observed absence of an explicit all-alphabet statement is not proof of priority; there remains a risk of a short unpublished or unindexed equivalent derivation.

## Value — PASS

The classification answers a natural word-inference question: exactly which starting phases of a repeated cyclic sequence can be recovered using length-at-most-two scattered subsequences? The sharp all-period criterion reduces potentially quadratic pair comparisons to an expected linear-size prefix-signature computation, gives an arithmetic obstruction to collisions, and establishes an exact alphabet-size-sensitive rigidity phenomenon: three or more pairwise distinct runs always require deck order exactly two, irrespective of run lengths and repetition count. The contrast between periods `001122` and `012012`, which have identical letter totals but different phase decks, shows why content alone cannot decide phase recoverability. Its significance is the complete structural classification and efficient phase partition, not complexity-theoretic speedups or an unproved downstream application.

## Closest literature and limitations

- Lejeune, Rigo, Rosenfeld, *On the binomial equivalence classes of finite words* (arXiv:2001.11732, 2020-01-31), Lemma 7 and Section 3: general two-binomial class coordinates and generation algorithms.
- Poovanandran, Simpson, Teh, *Counting Subwords in Circular Words and Their Parikh Matrices* (arXiv:2110.14858, 2021-10-28), Sections 3–5: circular averaging and binary weak-ratio multiplication identity, distinct from individual-phase complete decks.
- Rigo, Stipulanti, Whiteland, *Characterizations of families of morphisms and words via binomial complexities* (arXiv:2201.04603, 2022-01-12), especially Sections 1, 3 and 7: general complexities and morphic examples.

No theorem beyond whole-period lengths is asserted. Verification is finite and does not certify originality. An independently conducted literature and proof audit would be useful.

Self-review: passed. Independent audit: not yet performed.
