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

The finite supplementary program `checks/verify_specialist_window.py` runs under Python 3 standard library only. It tests the rational coefficient construction and the exact-root location, recomputes 2,500 random multi-target convex optimizations using derivative bisection, and compares each minimizer with eleven independent grid allocations. It reported 32,550 assertions without error.

The global interval theorem is not inferred from the tests. It is proved by positivity of the second derivative of the optimal-allocation objective, the exact boundary derivative, and convexity of the transformed marginal \(H\). The two-pest sharpness uses monotonicity of a single exponential.

The numerical values of the switching budgets are approximations to the exact logarithmic expressions. The model is an idealized conditional-detection design and is not externally validated against field data. The broader historical-priority question remains provisional.
