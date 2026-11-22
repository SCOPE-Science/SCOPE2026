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

# Reproducibility and verification

Execute `python3 verify_one_column.py` with Python 3 standard library. The program constructs the one-column quandle operation and checks the homomorphism law, idempotence, and image cardinality directly for every map whose values avoid the active point, for the 13 nonidentity cycle profiles with \(2\le n\le5\). It compares these brute-force rank counts against the closed formula from the theorem.

Observed exact terminal output:

```
ONE_COLUMN_RETRACTION_EXHAUSTIVE_PASSED 13
```

The finite experiment cannot establish the formula in all dimensions. The proof uses constancy on each cycle, the fixed-image property of idempotents, explicit map constructions, and elementary symmetric reconstruction. The verifier does not check historical priority or independently certify the theorem.
