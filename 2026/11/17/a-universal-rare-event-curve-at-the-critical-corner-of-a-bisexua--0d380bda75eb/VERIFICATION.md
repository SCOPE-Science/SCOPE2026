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

# Verification record

The proof derives the invariant directly from the two evolution equations, uses the exact scalar recurrence and the exact square-to-strip area Jacobian, and proves uniform compact-parameter convergence with an explicit cumulative-error estimate. The limiting measure assertion is vague convergence on compactly supported continuous tests, not convergence in total variation.

To numerically reproduce the sampling-window calculation, run `python check.py` in an environment with NumPy installed. The checker calculates finite-generation quadratures on parameter pairs and verifies convergence toward the displayed limiting formula. It also checks the fixed critical-fiber logarithmic correction. Floating-point quadrature and finite iterates cannot certify an infinite limit; the analytic proof supplies that certification at the stated same-model level.

No independent mathematical audit has been conducted, and publication priority against inaccessible or unindexed equivalent work is not certified.
