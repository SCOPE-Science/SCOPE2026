# Self-review

## Correctness — PASS
For distinct shifts, intersections of observed sample-hit subsets yield different representations of the same positive difference, so they have size at most \(g\). Selecting \(r\) distinct occupied weights at least two forces total incidence at least \(r(r+3)/2\). The exact second-moment identity, pairwise-overlap upper bound and Cauchy--Schwarz give the finite inequality without any unverified infinite induction. The asymptotic inversion is elementary and uniform for fixed \(g\). The dyadic witness and its Sidon condition are directly checked. The standalone verifier independently passes 10,036 finite profiles; these tests are not substituted for the proof.

## Originality — PASS against inspected sources
The 2026 primary paper proves the forest characterization for attaining the minimum, the size-three Sidon characterization, and only a lower bound \(P(6)\ge5\) for the powers-of-two example. Its Lemma 6.5 uses Sidon differences to bound **local support density**, not the number of distinct translate-hit weights for arbitrary sampling patterns. Our theorem permits any finite positive-difference multiplicity \(g\) and gives a global square-root bound on that different invariant; forest criteria and sparse-support counts do not imply it. The 2013 primary work addresses recurrence and lower bounds, not this nonrecurrent bounded-difference upper bound. No matching theorem appeared in actual targeted literature and indexed-record searches. Risk: a general incidence-design bound may already have been applied to this particular invariant in unindexed literature; no independent priority judgment has occurred.

## Value — PASS
The 2026 paper naturally separates Sidon from the stronger forest property, leaving quantitative higher-pattern complexity of nonforest Sidon supports. This theorem shows **all** such supports still have square-root, rather than potentially linear, Abelian maximal pattern complexity; moreover the argument controls the additive-combinatorics class with bounded (not necessarily unique) differences. It also turns the paper's strict lower bound in the dyadic example into the first explicit exact size-six value. This is an all-parameter structural bound, not a routine finite check or a mere restatement of the forest result.

## Prior-art limits
Most relevant: Zeng--Xue--Zeng, *Abelian maximal pattern complexity and extremal words* (2026), Sections 5--7, especially 6.5, 6.8, 6.10. Additional: Kamae--Widmer--Zamboni (2013/2015). Indexed work concerning shifted geometric supports gives girth and minimum-complexity boundaries only. Residual risk concerns unindexed bounded-difference second-moment arguments and the nonsharp asymptotic constant.

Self-review: passed. Independent audit: not yet performed.
