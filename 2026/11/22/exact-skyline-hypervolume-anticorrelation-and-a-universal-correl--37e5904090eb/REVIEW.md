# Review of skyline–hypervolume dependence

## Correctness

**PASS.** The definition of dominated area and the exact population assumptions are explicit. Sorting first coordinates gives independent Dirichlet spacings and a uniform permutation of second-coordinate ranks. The record/running-rank kernel has zero entries at and below the diagonal and strictly negative entries above it; telescoping produces the covariance formula. The complementary uncovered area is an independent Dirichlet-weighted sum of running minima, whose elementary pairwise covariance kernel yields the stated variance. Standard harmonic estimates give the nonzero correlation limit. All boundary cases, including the absence of ties and \(n\ge2\), are accounted for. A standalone exact-arithmetic checker validates the formula independently through two kernel sums and complete enumeration of small rank permutations, without substituting this enumeration for proof.

## Originality

**PASS, with historical-priority reservations.** The inspectable 2010 primary full text on dominance records treats marginal maxima and record moments and does not establish the covariance between skyline cardinality and dominated area. The accessible 2001 planar-maxima abstracts and author-manuscript excerpts likewise focus on marginal count laws. A closely related published corner-count covariance concerns the *number* of observations exceeding a fixed threshold, not the nonlinear event that at least one exceeds it; integrating that count does not produce dominated area. The exact mixed hypervolume covariance and its \(-1/\sqrt2\) correlation limit were not found in the actual queries. Nonetheless an uninspected older specialization, particularly in record or hypervolume literature, could exist; absence from a search is not a uniqueness certificate.

## Value

**PASS.** Skyline cardinality and dominated hypervolume measure distinct aspects of a Pareto sample and are commonly used together in multiobjective data analysis. The exact negative dependence is not a monotonicity tautology: increasing a set's cardinality by adding dominated samples leaves the skyline unchanged while changing placement can improve both the number and the area. The limiting correlation quantifies the persistent tradeoff at natural fluctuation scales; marginal record-count limit laws cannot supply it. A finite-sample formula and exact variance enable immediate calibration, without requiring a proposed downstream theorem.

## Closest literature and limitations

The closest primary background is Bai–Hwang–Liang–Tsai (2001), Barbour–Xia (2001), and Hwang–Tsai (2010) for maxima and records, alongside Shukla–Doll–Schmeck (2014) for hypervolume motivation. An existing fixed-threshold skyline/corner-count covariance is a nearby but not equivalent statistic. The conclusion is limited to independent uniform coordinates in the unit square with origin-anchored hypervolume. The original planar-maxima full texts could not all be inspected page by page; they remain a material literature-priority uncertainty. No distributional joint central limit theorem or stochastic-order claim is made.

Self-review: passed. Independent audit: not yet performed.
