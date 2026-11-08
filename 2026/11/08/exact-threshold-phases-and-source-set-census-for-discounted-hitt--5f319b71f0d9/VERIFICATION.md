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

Use `python3 verify.py` (standard-library only). The script independently constructs all labelled cycle source sets for orders 3 through 9, solves the original random-walk equations over exact rational numbers by Gaussian elimination, and checks the worst-vertex condition against an independently solved interval-support threshold. It compares every cardinality coefficient against the bounded cyclic-composition formula for 205 parameter cases, including equality at the tested gap transitions. The exact replay output was:

```
INDEPENDENT_EXACT_GAUSSIAN_AND_GAP_COUNTS_OK 205 parameter_cases n=3..9
EXAMPLE_n10_lambda_half_tau_third 25
VERIFY_OK
```

The universal mathematical argument is given in `RESULT.md` and does not rely on extrapolating finite checks. No external/independent audit was performed. For arbitrary real parameters, transcendental evaluations are interpreted as exact mathematical definitions, not floating-point certificates.
