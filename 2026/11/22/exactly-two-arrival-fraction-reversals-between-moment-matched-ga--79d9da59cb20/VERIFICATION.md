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

# Verification

The complete proof is in `RESULT.md`. `check_gamma_ig.py` evaluates the specified normalized Gamma and inverse-Gaussian densities with SciPy and brackets all three density roots using the analytical stationary points. It then brackets the two CDF roots and verifies signs, moment matching, ordering, and small-variance behavior for selected cases.

Executed as `python check_gamma_ig.py` using Python 3, NumPy and SciPy. The checker reported **128 diagnostic assertions passed**, over 15 values of \(v\) from \(0.005\) to \(40\), including four small-variance cases. It is a numerical diagnostic only: the all-parameter count and small-variance limit are established by mathematical argument, not finite sampling. No external independent review was performed.

The output relies on idealized exact-distribution assumptions; it does not verify field-data model adequacy. The manuscript and checker need no hidden data or external file inputs.
