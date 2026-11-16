# Scientific review of winner-free tournament Fourier projections

## Correctness
PASS. Each excluded Condorcet-winner event fixes an edge star and is disjoint from every other such event. Character orthogonality gives the exact Fourier support, including cancellation at singleton-edge frequencies. The inverse transform gives a graph polynomial in edge count and isolated-vertex count. Translation averaging is applied to arbitrary projections, not merely convolution projections. The graph-sum expression follows exactly; the asymptotic uses a binomial CLT plus a controlled exponentially rare isolated-vertex correction. The included checker independently verifies every coefficient through six vertices and the exact binomial count through twenty.

## Originality
PASS under bounded documentary comparison. Altman–Kleinberg (2010) studies tournament winner selection and incentives, not Fourier ranges. Kolesnik–Sanchez (2020/2023) studies attainable score sequences through zonotopes and forests rather than winner-free character sums; its open full article was inspected. Zippin (2004) establishes the general averaging principle; this general method is explicitly acknowledged and is not claimed novel. Gilbert–Rzeszotnik (2010) concerns norms of the whole Fourier transform, not this particular idempotent multiplier. Relevant indexed mathematical findings concern regular-tournament first-coordinate sampling, random score-histogram covariance and other supports, not the non-winner range. Exact equivalent formulations and full-text historical coverage beyond these sources remain residual risks.

## Mathematical value
PASS. The projection constant is the exact smallest norm over all bounded linear projections, not just the norm of a convenient Fourier projection. Its all-order expression unexpectedly mixes a central-limit contribution with a rare-graph-isolation contribution of the **same linear order**. The explicit coefficient \(1+2e^{-1/4}/\sqrt\pi+\operatorname{erf}(1/2)\) and the associated sparse Fourier rank distinguish operator geometry from the classical count of tournaments admitting a winner. The result describes a natural constraint on the complete orientation cube and provides a reproducible family of sharp endpoint stability benchmarks.

## Limits
Only the complete labelled tournament family and endpoint projection norms are settled; a full intermediate-\(p\) theory is not claimed. Historical-priority verification is bounded and independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
