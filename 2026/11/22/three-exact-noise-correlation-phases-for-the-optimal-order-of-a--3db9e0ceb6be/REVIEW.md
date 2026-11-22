# Self-review

## Correctness — PASS
The exact recursion yields a permutation-invariant deterministic bias and a three-weight quadratic covariance polynomial. Both winner-crossing identities are checked symbolically. Since all permutation variances coincide at correlation one, every pairwise normalized difference is affine in correlation; checking two endpoints per interval suffices. The standalone exact certificate verifies all 30 required interval-endpoint inequalities for the full continuum of rates through nonnegative Bernstein coefficients, plus threshold inequalities and a generic two-step order identity. Rational interior checks are sanity tests, not substitutes for the certificate. Only second-moment assumptions are used.

## Originality — PASS (subject to historical-priority uncertainty)
Compared directly against published prior research on geometric rate decay, automated rate drops, Markovian SGD, asymptotic covariance efficiency, and the closest searchable same-parameter published result for *independent* oracle noise. The latter implies descending optimality at correlation zero but does not cover correlation-dependent order reversals. The general Markovian SGD papers supply convergence or asymptotic efficiency bounds, not exact minimization over the six permutations at finite horizon three. Published-claim comparisons did not treat keyword matches as proofs of coverage. An unknown prior equivalent calculation, including older colored-noise numerical-analysis literature, remains a real risk; no independent novelty certification is claimed.

## Value — PASS
Geometric step decay is mathematically and practically motivated in stochastic optimization, and temporal oracle correlation changes effective accumulation of noise at the final iterate. The theorem supplies exact decision boundaries and shows a counterintuitive reversal of the standard descending-rate policy at both positive and negative correlation. Its three steps are not an arbitrary unmotivated slice: two steps provably cannot exhibit this phenomenon. This is a rigorous calibration benchmark, not a universal prescription for long schedules.

## Scientific limits
The rate multiset is geometric with ratio two, curvature is scalar and normalized, the largest rate does not exceed one, only terminal squared loss is optimized, and noise is stationary in covariance but not assumed Gaussian or conditionally unbiased. No claim is made for arbitrary schedules or multidimensional dynamics. The first reference was inspected at publicly accessible abstract level; relevant full texts of other sources were inspected, with details in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
