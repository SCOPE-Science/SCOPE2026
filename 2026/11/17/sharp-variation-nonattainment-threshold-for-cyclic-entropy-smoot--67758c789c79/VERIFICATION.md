---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For n≥2, 1≤w≤n, fixed positive site weights and τ>0, the Jacobian row is a sliding-window positive distribution. Successive distribution CDF differences factor D J_z=C_z D: each C column has positive support on exactly w consecutive cyclic output edges and sum 1. Therefore global two-input cyclic variation ≤ input variation. If w<n<2w every positive and negative gradient column pair intersects and strict triangle inequality applies at every finite segment point. If n≥2w, two disjoint complete windows give finite equality. If w<n<2w, a one-site dominating input pair approaches gain 1 without attaining it. If w=n the output is constant. w=1 and n=2 covered.

## originality

PASS

The basic entropy-smoothed maximum and softmax probability gradient are due to Nesterov; path-window running maxima and minima already exhibit two-input BV nonexpansivity and may, via a Gumbel representation, explain the weak global upper bound. The precise cyclic all-positive-weight finite-pair equality iff n≥2w, strict inequality when w<n<2w despite sharp coefficient 1, and saturated limits add a structurally distinct sharp attainment classification not found in the full relevant published path proof or primary entropy-smoothing material.

## value

PASS

The exact half-cycle threshold is a complete classification of when smooth local dilation has finite equality versus pointwise strict contraction without a uniform gap. This is mathematically useful when distinguishing strict improvement from global contraction for a standard entropy-smoothed nonlinear filter, with a reusable positive-column-overlap explanation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
