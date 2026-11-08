# Scientific review

## Correctness (C): PASS

The exact domain is the class of labeled \(q\)-letter words in which all windows of length \(d+1\) are injective, for integers \(q>d\ge2\). The greedy arch criterion is established, then the last-\(d\)-seen invariant produces the exact repeat/new transition counts \(s-d\) and \(q-s\) and the formal-series renewal identity. The extremal count is independently proved from permutation blocks; the stochastic statement uses an explicitly identified i.i.d. sum of geometric waiting times. The finite script compares two exact coefficient methods and literal enumeration, but the all-parameter assertion rests on the proof, not these tests.

## Originality (O): PASS, qualified

Barker et al. (2020) supply the arch framework; Adamson (2023) addresses unrestricted counting; Adamson et al. (2023) cover general DFA counting without this evaluated all-radius expression. The existing radius-one enumeration covers the strictly weaker distance-one constraint and does not determine the radius-two-and-higher coefficients. Search comparisons considered alternative formulations as distance-\(d\) proper colorings, sliding-window injectivity and refractory coupon collection, and did not locate an equivalent formula or a stronger all-parameter theorem. The risk of an unindexed or differently named equivalent remains; generic regular-language counting gives algorithmic computability but not the specified closed form and renewal law.

## Value (V): PASS

This resolves a natural joint problem connecting proper colorings of powers of paths and subsequence-universality enumeration. The same exact formula works for every pair \(q>d\ge2\), not a one-step fixed-parameter increment, while the rigidity-to-Gaussian transition and exact optimal-word multiplicity identify structural consequences useful for constrained universal sequence design. No claim of a paper-sized or optimal algorithmic improvement is needed.

## Verification and limits

The standalone script passed all documented finite checks; these are not exhaustive for unbounded parameters. Primary full-text sections were inspected for stronger covering statements, and none identified. Independent review and complete bibliographic exclusion are not claimed.

Self-review: passed. Independent audit: not yet performed.
