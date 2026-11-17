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

# Verification notes

Reproduce the mathematical calculations with `python checker.py`. The checker was run successfully from the accompanying standalone source. It verifies the exact phase-difference Jacobian, second-order expansion, constant quotient-metric norm of the quadratic term, all four roots of the blow-up equation, transverse saddle eigenvalues and three small-parameter numerical branch families.

The inradius bound is justified by the analytic radial differential inequality plus an implicit-function-theorem saddle obstruction, not by finite grids. The result is local in the coupling parameter, is stated on the phase quotient, and does not determine global basin volume or stochastic escape times. No independent mathematical audit is represented here.
