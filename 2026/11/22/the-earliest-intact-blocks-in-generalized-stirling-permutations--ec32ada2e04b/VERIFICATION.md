---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The largest label occupies a unique run and is deletable, so all valid words have exactly one insertion history with the same probability. For marked surviving runs the r−1 forbidden gaps per run are disjoint, so the joint product follows by conditional survival. The one-label product telescopes in Gamma ratios with exponent alpha=(r−1)/r. The bounded early-window intensity follows by summation and the uniform bound p <= C(i/n)^alpha; b_n^(1+alpha)=n^alpha. For fixed joint order, comparing logs to the product of marginals on [epsilon b_n,T b_n] costs O(sum_{ell >= epsilon b_n} ell^(-2)); at every label Bernoulli's inequality dominates joint survival by that product. Thus the small-label loss is bounded by its vanishing first moment as epsilon decreases; repeated indices cost at most a constant times max p on the compact window. The factorial majorant exchanges the limit with all orders in the Laplace expansion. This proves vague Poisson convergence, including at the origin. Interval counts converge with no fixed limit atoms, which gives joint fixed-rank convergence and tightness since the cumulative intensity tends to infinity. For the scale assertion, beyond the balancing scale pairwise nonpositive covariances also give variance at most the mean, so diverging means imply diverging counts, not merely a first-moment suggestion.

## originality

PASS

The new conclusion is the rare birth-label Poisson process and its fixed-rank laws, not the finite survival product, gap representation, or plateau encodings. The strongest accessible exact identity is credited; passing from it to this scale and all local counts needs the rare-event argument.

## value

PASS

The smallest surviving label is a natural birth-order statistic. The multiplicity-dependent scale separates a new regime from the bulk, and the nonhomogeneous process captures all fixed ranks rather than just an expected count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
