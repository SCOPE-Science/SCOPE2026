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

# Reproducibility and limits

`check.py` runs independently from this package with Python 3, NumPy and mpmath. It tests finite Cauchy identities against independently formed Gram-matrix determinants, checks the exact critical finite-size sums, and evaluates the predicted asymptotic trends. Infinite asymptotics, trace-class membership, and bounded invertibility rely on the analytic proof in `RESULT.md`, not finite tests.

No uniform critical-window theorem is claimed; no independent mathematical verification has been performed.
