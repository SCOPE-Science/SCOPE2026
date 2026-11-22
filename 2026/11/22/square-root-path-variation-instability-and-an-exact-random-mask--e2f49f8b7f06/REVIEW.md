# Mathematical review

## Correctness — PASS
The strict-chamber argument reduces the global two-input problem to finitely many projected step responses, giving threshold independence and attainment. The nontrivial upper bound is established by a Haar-band decomposition of Sylvester spectral indices: an individual step has one Haar coefficient per band, with squared norm at most one-quarter the block length, and variation of each band is controlled by its block amplitudes. The exact expectation is derived by character orthogonality and a binomial absolute Rademacher moment. Exhaustive masks for sizes 2, 4, 8 and randomized projection/chamber checks at sizes 16 through 128 corroborate rather than replace the proof.

## Originality — PASS, with historical-priority risk
The closest inspected Walsh spectral-shrinkage result is for Hamming-cube graph edge variation; it employs derivatives commuting with Walsh projections, unlike consecutive differences on the natural integer path. The related DCT-II result has the same square-root growth exponent but a distinct sine-transform projection formula; the Haar result has logarithmic growth. Primary full-text accounts of graph signal variation and Walsh sparse recovery do not establish the exact open-path Bernoulli-mask expectation or this Walsh-specific band upper bound. An unindexed general Walsh projection theorem could still cover part of this, so priority is not independently certified.

## Value — PASS
Classical Euclidean nonexpansivity is inadequate for variation-sensitive signal preprocessing. The proven basis-and-order-specific growth law gives a dimension-dependent stability warning, while the exact impulse mean quantifies a natural distribution of spectral active sets without optimizing over exponentially many masks. Its contrast with Haar and with Boolean-cube adjacency has interpretive and methodological value.

## Scope and limits
Only natural-order real Sylvester Walsh transforms, dyadic sample lengths, ordinary unweighted noncyclic adjacent variation, uniform fixed positive soft threshold, and independent fair masks are covered. The exact worst-case leading constant is unknown; the binomial expression is an **expectation** and a lower bound for the sharp constant, not an exact formula for it. All finite tests and any historical search are qualified by these limits.

Self-review: passed. Independent audit: not yet performed.
