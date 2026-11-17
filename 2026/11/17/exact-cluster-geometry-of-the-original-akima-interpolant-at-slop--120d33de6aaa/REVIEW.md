# Scientific review: Akima interpolant cluster geometry

## Correctness — PASS

For each knot the original slope is a convex combination of its two adjacent secants. A denominator approaching a nonzero value has a unique limit; a zero denominator with equal adjacent secants also has a unique limit. Only a zero denominator separating unequal constant-slope patches permits an interval of limiting slopes. To realize every vector of slope limits, place the vanishing gap weights on a graph with edges between gap indices two apart; this graph has no cycles. Recursively prescribed positive ratios and vanishing common scales yield any collection of endpoint or interior ratios, and integrating small secant differences constructs actual data perturbations. Cubic Hermite basis functions then identify the complete box; distinct critical sites are at least two knots apart, so their open bump supports are disjoint. Exact elementary extrema give sup norm 4/27 and variation 16/27 for each unit-amplitude bump. These steps prove the formulas for every finite critical set, not merely examples. A standalone Python 3 checker independently exercises rational extremal identities and simultaneous critical-corner constructions.

## Originality — PASS, with stated limitations

The original Akima formula was published by Akima in 1970 and reconstructed in full in Evenden's 1989 report. Moler and Ionita (2019) expressly exhibit a discontinuity caused by the zero-denominator fallback; this qualitative phenomenon is **not claimed to be new**. A previously published 2026 uniform-grid Akima result proves a 2/27 single-signal monotone range defect, a different quantifier and norm. The new theorem is the complete joint cluster set for arbitrary finite configurations of degenerate knots, with simultaneous independent realizability and sharp uniform and total-variation diameters. The mathematical implications of those closest sources were compared with the full current claim. Residual risk: the 1970 original article and the 1969 predecessor report were not inspected in full, and an unindexed historical exact-cluster theorem may exist.

## Mathematical value — PASS

Stability of piecewise-cubic reconstruction under arbitrarily small data perturbations is a natural question, particularly where interpolation formulas include a zero-weight branch. The full family of possible limits, rather than a single failure example, distinguishes benign zero-weight knots from unstable corners and quantifies the cumulative variation ambiguity of multiple separated corners. The path-forest compatibility argument shows that all local defects can indeed be realized at once; this is the nontrivial global obstruction that a one-corner example does not address. The exact formulas provide natural sharp measures for judging and redesigning nonlinear slope selectors.

## Closest evidence and residual limits

- Akima, 1970, DOI: https://doi.org/10.1145/321607.321609 — original method; full publisher article not read.
- Evenden, 1989, https://pubs.usgs.gov/of/1989/0019/report.pdf — full technical exposition and code defining the original selector.
- Moler and Ionita, April 29, 2019, https://blogs.mathworks.com/cleve/2019/04/29/makima-piecewise-cubic-interpolation/ — qualitatively demonstrates the discontinuity, but not the full cluster-set identities.
- Published uniform Akima range result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-uniform-akima-interpolant-has-sharp-monotone-range-defect-2--4f68318a3dd5 — full RESULT.md inspected; different extremal statement.

Self-review: passed. Independent audit: not yet performed.
