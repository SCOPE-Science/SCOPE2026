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

Run `python3 verify.py` in this directory with Python 3.9 or later and no additional dependencies. The script builds the coefficients of the hook-length and core generating functions by two unrelated exact-integer algorithms, then checks equality, global gcds, first-sharp indices, and local composite obstructions. It successfully produced:

```text
VERIFY_OK parameter_cases=21 coefficients_cross_checked=1611 exact_integer=yes
SAMPLE t=4 first_sharp_index=2 difference=88 modulus=8
SAMPLE t=6 mod2_first_index=4 mod3_first_index=9 content=1
```

This finite replay checks 21 values of the integer parameter and 1,611 coefficients in aggregate. It does not establish universal congruence or originality. The unrestricted proof is the formal-series and binomial-valuation argument in `RESULT.md`; the source comparison and unresolved historical priority are in `REVIEW.md`.
