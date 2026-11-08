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

# Verification and proof boundary

The attached standalone file `verify_lyndon.py` requires Python 3 and uses only the standard library. Execute `python3 verify_lyndon.py` in the directory containing that file.

Direct execution of the script produces:

```
PASS direct brute-force Lyndon subsequences: 201 words; by number of gaps: {1: 7, 2: 28, 3: 61, 4: 64, 5: 41}
PASS direct suffix Lyndon witness and exact length: 201 cases
PASS triangular, constant and geometric leading block formula: 72 families
```

The direct oracle constructs the actual set of scattered subsequences and tests every proper suffix, independently of the threshold proof. The symbolic extension checks the explicit construction, not the combinatorial upper bound. The exact theorem for all nondecreasing positive integer gaps is supported by the fully quantified argument in RESULT.md, not by an extrapolation of finite cases. No separate independent scientific audit has been performed.
