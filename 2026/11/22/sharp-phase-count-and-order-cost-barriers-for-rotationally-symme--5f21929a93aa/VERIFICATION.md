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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library in the same directory. The expected successful output is `VERIFY_OK 1721`. The checker independently constructs Hermite polynomials by recurrence; computes Gaussian moments by double factorials; tests the exact moment formula for many derivative orders and Taylor degrees; tests the roots-of-unity filter; compares Legendre recurrence against the finite variance identity; and checks convergence toward the stated growing-order asymptotic coefficient and base.

All tests use exact integer or rational arithmetic except complex roots-of-unity cancellation and asymptotic ratio spot checks. The proof of the all-order statements is in `RESULT.md`: these finite tests neither enumerate arbitrary admissible inputs nor prove an infinite limit on their own. The entire result is limited to the stated one-dimensional estimator and to the prescribed order of asymptotic limits. No independent mathematical audit has been performed.
