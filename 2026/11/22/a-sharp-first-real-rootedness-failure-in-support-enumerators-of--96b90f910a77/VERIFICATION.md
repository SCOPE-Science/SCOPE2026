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

## Reproducible checks
Execute `python standard_example_verify.py` in the same directory as this document, using Python 3.9 or later and no third-party libraries.

The script checks Hall endpoint-pair coefficients for all orders 1–7; evaluates the original ideal-inequality lattice-point definition and the gamma expansion for orders 1–4; and performs exact rational Sturm divisions for orders 2–12. For orders 3–11, the distinct negative-root counts are 3, 4, ..., 11. For order 12, the Sturm sign variations at negative infinity and zero are 11 and 1, respectively, giving exactly ten distinct negative real roots. The last Sturm polynomial is a nonzero constant, confirming squarefreeness and the conjugate pair of nonreal roots.

Expected final output: `VERIFY_OK`. The finite Sturm checks establish the first failure through order 12. The all-order formula rests on the mathematical Hall argument, not on numerical extrapolation. No independent validation or publication-priority certification has been performed.
