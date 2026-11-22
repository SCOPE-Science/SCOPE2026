# Self-review

**Correctness — PASS.** The covariance trace reduction is exact. An exhaustive orbit table of 27 possible row sequences gives a pointwise dual bound, with strictly positive slack for every repeated-row sequence throughout the open parameter range. Uniform time marginals yield the lower bound, and a rank-five linear system determines all equality distributions. The standalone exact symbolic verifier checks projector products and graph-example fractions. Boundaries and out-of-scope cases are stated.

**Originality — PASS (provisional historical priority).** Full-text comparisons with 2024 reshuffling convergence, 2023 sparse-constraint reshuffling and the 2024 survey, plus two highly relevant published results on planar three-row frame rates and two-row relaxed coupling, do not assert or imply the unrestricted three-round three-dimensional marginal optimal-transport certificate. General Kaczmarz reshuffling is of course established. A specialist optimal coupling characterization could remain undiscovered.

**Value — PASS.** This identifies a globally optimal schedule over all joint laws satisfying a realistic per-round fairness constraint, rather than merely comparing a few commonly used samplers. The explicit optimizer polytope and four-vertex path gossip instance with a 49/94 reduction in expected error against IID sampling provide nontrivial interpretable structure; the scope is intentionally a short-horizon benchmark.

Limits: fixed frame and horizon, covariance-isotropic initial error, no adaptive policies, no independent verification.

Self-review: passed. Independent audit: not yet performed.
