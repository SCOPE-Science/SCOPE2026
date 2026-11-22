# Self-review

## Correctness — PASS

The Motzkin congruence from Deutsch–Sagan gives the exact finite digit-set identity. A digitwise argument excludes nontrivial progressions of length three in the upper ternary digits. The two-block geometry then proves exactly four cross-block triples, one cross-block quadruple and no longer crossing progressions at every level after the base. This yields the individual step frequencies, the four total counts and the global sharp length-six ceiling. The independent enumeration and recurrence verifier in `check.py` passed 189 grouped assertions over finite ranges; it is not an infinite proof.

## Originality — PASS (qualified)

Relevant primary full-text portions of Deutsch–Sagan (arXiv:math/0407326), Krattenthaler–Müller (arXiv:1308.2856) and Moy–Rolnick (arXiv:1502.06013) were inspected. The first paper establishes membership of Motzkin indices modulo three; the second studies stronger congruences; the third studies the progression-free Stanley digit set. The exact multi-length, per-difference count and length-six rigidity of the *thickened* set were not established by inspected claims or the targeted exact-formula searches. This is a best-knowledge priority conclusion, not a proof that no historical source covers it. Unindexed literature on discrete Cantor thickenings remains a risk.

## Mathematical value — PASS

A natural sparse nondivisibility set has an unexpectedly rigid bounded progression-length spectrum: length six occurs, length seven never occurs. The complete all-scale frequency of every possible difference for each length three through six is a natural exact arithmetic-combinatorial invariant. The structural cross-block lemma, rather than mere finite enumeration, explains why only a few new progressions appear at each scale.

## Limits and status

The claim is about increasing integral arithmetic progressions entirely within explicit ternary prefixes; it does not extend to other primes. The prior digit characterization is not new. The mathematical proof has been reviewed in the same assessment and checked finitely, but no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
