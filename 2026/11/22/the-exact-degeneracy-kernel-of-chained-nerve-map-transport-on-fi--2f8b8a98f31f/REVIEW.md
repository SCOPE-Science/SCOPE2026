# Review: exact degeneracy kernel for finite nerve-map transport

## Correctness

PASS. The proof identifies the cost at a nonisolated site's center and establishes a strictly positive uniform price for any off-diagonal transfer involving that site. An arbitrary finite chain must pay at least that price times the coordinate's endpoint mass discrepancy. Conversely, a zero-cost coupling exists for every change supported entirely on scale-isolated sites. Mass conservation yields the sharp one-isolated-site threshold and an explicit total-variation lower bound. The zero-ball boundary convention and all quantifiers are included in the proof. A standalone linear-program computation checked the paper's exact Appendix A example, both directions of the zero-kernel criterion, and 275 independent finite metric/radius instances. These computations are supporting evidence, not a substitute for proof.

## Originality

PASS subject to non-exhaustive priority risk. McCabe and Perea, *Wasserstein Stability of the Nerve Map*, arXiv:2611.15938v1, specifically introduce the chain pseudometric and leave suitable point-separation hypotheses as an open question. Their Proposition 3.3 establishes that a different, larger localized transport construction is a metric, not this smaller chain metric. Their Theorem 3.4 provides an upper bound, not the necessary lower bound. Jin and collaborators' kernel localization results likewise concern a different Wasserstein construction and upper stability estimates, not the sharp radius threshold or zero-kernel equivalence. The related 2018 metric-thickening work concerns a different object. Indexed and web literature searches found no broader implication covering the present statement, but an equivalent unpublished or unindexed theorem remains possible.

## Value

PASS. This is a sharp necessary-and-sufficient answer on a natural finite-data class to a concrete question posed in the 2026 nerve-map-stability paper. It characterizes *every* zero-distance pair, gives the exact radius transition (including equality), and supplies a uniform quantitative coercivity inequality. The fact is useful when deciding whether a sharp pointwise stability estimate can safely be metricized without losing information about landmark weights.

## Limitations

The assertion is for finite strict metrics and strictly positive full-support probabilities only. Chains cannot exit the positive simplex; changing this domain can change the result. Nonzero chain distances are not evaluated exactly. The result is independently unvalidated and an equivalent unpublished proof cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
