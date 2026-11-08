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

# Reproducible mathematical checks

Run `python verify_wheel_h1.py` with Python 3 and SymPy. The code independently solves the distributional Kirchhoff equation \(-g''=\delta_x-ds/(2m)\) after inserting each test point as a vertex, taking the constant source on every edge segment into account. Exact rational integration then enforces mean zero and reads off the evaluation diagonal \(g(x)\). These values are compared to the analytically derived spoke and rim quadratics.

A successful run produces:

```
EXACT_CENTERED_KIRCHHOFF_POISSON_CHECKS_PASSED 99
EXACT_RIM_SPOKE_GAP_AND_EXTREMIZER_CHECKS_PASSED 9
ALL_METRIC_WHEEL_SOBOLEV_CHECKS_PASSED
```

The 99 exact checks cover \(m=3,\ldots,11\), both edge types, endpoints, several interior points, and each spoke stationary point. Symbolic rational identities of the finitely checked graphs are consistency checks, not a substitute for the explicit all-\(m\) resolvent and strict polynomial comparison proved in RESULT.md. The proof also covers the tetrahedral boundary \(m=3\) and the limit as \(m\to\infty\).
