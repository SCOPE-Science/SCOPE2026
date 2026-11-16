---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The recurrence-to-Chebyshev formulas are derived from the two-step recurrence and its two initial conditions. The finite-degree classification is proved by eigenvalue interlacing for a negative rank-one perturbation and exact edge evaluation. Positive gap-root squared values follow from the strict inequality between a hyperbolic sine ratio and the associated exponential. The critical regime is proved by monotonicity and locally uniform trigonometric/hyperbolic limits.

`CHECK.py` requires only Python 3 standard library and executes exact rational coefficient comparisons in several parameter sets and degrees. It also checks finite-degree sign transitions and critical-scaling convergence numerically. These finite checks are examples and regression tests, not a proof of arbitrary-degree or continuum assertions. All limits and endpoints are proved analytically in `RESULT.md`.

Self-review has passed. Independent audit is not performed.
