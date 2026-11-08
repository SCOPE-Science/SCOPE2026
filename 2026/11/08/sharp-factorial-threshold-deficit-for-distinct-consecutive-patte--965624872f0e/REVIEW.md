# Scientific review

## Correctness
PASS. The key observation is that, at shift \(d<k\), the \(k\) aligned index pairs form a forest of paths; an alternating edge color class supplies at least \(\lfloor k/2\rfloor\) disjoint pairs. Equal full patterns force equal order types on the two disjoint matched index sets, whose relative orders are independent uniform permutations. This proves the factorial collision bound and, combined with elementary collision-count and factorial-tail inequalities, closes a two-sided asymptotic proof. The included exact checker passed 362934 assertions; it is not used to infer the infinite limit.

## Originality
PASS with historical-priority qualification. Allen et al. (arXiv:2011.12179, 2020) prove a quadratic first order and find the deterministic factorial threshold, but their expectation lower bound loses order \(n\log n\). Godbole and Swickheimer (arXiv:2310.14071, first posted 2023, Theorem 1.2 and Section 3) give a sharper yet still order-\(n\log n\) loss and ask for improvement. Neither inspected text states an expected deficit asymptotic to \(n\log n/\log\log n\) or entails its coefficient by the displayed bounds. Comparable records about ordinary substrings of independent words concern a different equivalence relation and source model. An unindexed independent derivation remains possible.

## Value
PASS. The motivating studies established near-maximal random permutation pattern diversity but left a factor of \(\log\log n\) between an unavoidable pigeonhole deficit and their expectation estimates. The theorem exactly closes that gap and gives a universal coefficient, revealing that the factorial crossover dictates the dominant expected loss.

## Limitations
Uniform one-line permutations, distinct consecutive relative-order patterns, and the expectation only. No variance, concentration or finer error term. Literature and record search do not substitute for independent priority assessment.

Self-review: passed. Independent audit: not yet performed.
