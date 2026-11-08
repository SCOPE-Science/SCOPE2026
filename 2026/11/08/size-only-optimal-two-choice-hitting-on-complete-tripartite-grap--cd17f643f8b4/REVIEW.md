# Review of the tripartite two-choice hitting theorem

## Correctness: PASS

The theorem precisely fixes the graph, the target, the with-replacement two-offer mechanism, the objective and all parameter ranges. The stated policy induces the displayed three-state substochastic transition system. The target is reached with finite mean, so the linear system has a unique positive solution. Two exact Cramer-determinant identities establish the ordering of all three values: one difference factors with the sign of the difference between the two other part sizes, while the second difference has a strictly positive-coefficient decomposition on the full allowed integer domain. The verification script checks both polynomial identities by exact interpolation using the proved degree bound and independently solves full-vertex chains for 45 graphs. The final order satisfies Bellman optimality, including against history-dependent competitors. There is no extrapolation from experiments to an unproved infinite claim.

## Originality: PASS (with residual historical risk)

The closest primary source is Georgakopoulos, Haslegrave, Sauerwald and Sylvester, *The Power of Two Choices for Random Walks* (first public posting November 12, 2019), especially Section 7.1, Lemma 7.1 and Theorem 1.6. These prove the general lower-hitting-value preference principle and polynomial computability, but do not give an all-parameter explicit size-only ranking for a target-rooted three-part complete graph. The related 2020 conference treatment addresses generic algorithms, bounds and applications rather than the asserted classification. The general principle is used, not claimed as novel. A search for exact tripartite instances, alternative descriptions, fuller domination and tabulations found no decisively covering result. The graph family and objective also differ from finite complete-multipartite cover-walk classifications. Lack of a found statement is not proof of worldwide priority; unindexed or inaccessible literature remains a risk.

## Mathematical value: PASS

The theorem supplies an explicit state-independent decision rule valid uniformly over an infinite natural family, resolves nontrivial distance ties between two neighbor classes by their *relative sizes*, and replaces an optimization over all adaptive controls with a three-state rational calculation. Strict inequality and equal-size degeneracy are both established. This is more informative than restating generic Bellman equations or merely checking small instances, and the certificate covers all integer parameters in the stated domain. It does not address more than three parts, deadline-wise optimality or robustness.

Self-review: passed. Independent audit: not yet performed.
