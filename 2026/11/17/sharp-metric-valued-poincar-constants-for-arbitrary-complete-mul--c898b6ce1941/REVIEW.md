# Review of the multipartite metric Poincaré formula

## Correctness: PASS
Summed triangle inequalities control within-part distances by the minimum cross-part average. A layer-cake argument bounds the resulting minima by the edge-average times the largest subset ratio. For every subset an explicitly defined \(\{0,1,2\}\)-valued pseudometric yields exact equality after zero-distance quotient. An exchange-or-remove argument proves that the maximizing subset can be chosen as a prefix of parts sorted by size. Every denominator is positive because there are at least two nonempty parts. The full proof handles singleton parts, zero-distance maps and all metric targets. The standard-library checker passed 7,136 supplementary exact assertions; they are not substitutes for the proof.

## Originality: PASS (qualified)
The closest recent cotype/spectral-gap paper proves upper bounds for regular expanders in restricted Banach targets, not an exact universal metric Poincaré constant for complete multipartite graphs. The general nonlinear spectral-gap framework and previously reported exact bipartite or restricted tripartite formulas do not imply the all-multipartite classification, the explicit maximizing-prefix reduction or the examples requiring more than one selected part. Searches of published mathematical records for the exact ratio, arbitrary metric targets, subsets and prefix extremizers found no directly covering result. Only the primary source's abstract, classification and publication record were accessible; an equivalent earlier treatment of this specialized graph family cannot be completely ruled out.

## Mathematical value: PASS
Metric-target Poincaré constants quantify average-distance amplification by graph edges, an invariant central to nonlinear expansion and Banach-space embedding questions. The result supplies all part sizes without target restrictions and reduces exponentially many candidate subsets to linearly many. Exact intermediate-size optimizers demonstrate that neither a single largest part nor the entire graph always controls the sharp constant, giving a new structural phase distinction.

## Closest literature and limitations
A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1 (first public 3 November 2026); D. J. Altschuler, P. Dodos, K. Tikhomirov and K. Tyros, *A combinatorial approach to nonlinear spectral gaps*, arXiv:2410.04394. Applicability is restricted to unweighted complete multipartite graphs and first powers of distances. Full source manuscripts were not accessible, and independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
