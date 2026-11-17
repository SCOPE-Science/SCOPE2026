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

Run `python3 checker.py` using Python 3 with only the standard library. Successful output:

```
EXACT_FINITE_COEFFICIENTS_N2_TO_N16_PASS
INDEPENDENT_SUBSET_AND_CUT_ENUMERATION_N2_TO_N11_PASS
INDEPENDENT_EXACT_FINITE_INPUT_ATTAINMENT_N4_TO_N21_PASS
PROVED_LINEAR_BOUNDS_SPOT_CHECK_N2_TO_N54_PASS
ALL_OSCILLATION_BALL_CHECKS_PASS
```

The script performs exact rational comparisons and a separate direct clipping-interval minimizer for extremizing input pairs. These finite tests independently check the claimed formula and witnesses in the listed dimensions. The all-dimension proof is in RESULT.md. The project has not undergone independent audit, and the finite tests alone do not certify an infinite-dimensional assertion.
