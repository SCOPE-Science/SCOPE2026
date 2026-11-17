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

The exact proof is contained in RESULT.md. Reproduction command: `python checker.py` with NumPy and SciPy available. The checker runs an independent, finite-dimensional linear program for each tested pair of zero coordinates and separately checks the projected Frobenius Gram entries using exact rational arithmetic. The script is not a machine proof of the all-dimensional claim.

Observed verification output:

```
TRANSPORT_RIDGE_LP_PASS pair_cases=7068 dimensions=3..5 margin_cases=54 normals=exact_projection
TRANSPORT_RIDGE_GRAM_EXACT_PASS dimensions=3..8
```

The linear programs use floating-point arithmetic and a fixed feasibility tolerance, so only the Gram test is exact arithmetic. The analytic proof covers the equality boundaries and all positive real margins. No independent expert or machine certification has been conducted.
