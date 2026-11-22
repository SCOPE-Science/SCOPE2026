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

Run `python3 verify.py` with Python 3.10+ (no third-party packages). The script independently enumerates each orientation of \(D_{2,b}\) for \(2\le b\le10\), checks the complete coefficient lists against the derived polynomial, verifies the total \(2^{b+3}\), checks every coefficient of the exact \(H_{11}\) polynomial identity, checks all positive Bernstein coefficients and the derivative values, and verifies the rational \(H_{13}(6/5)>0\) witness. The captured local run returned:

```
DIRECT_ORIENTATION_CENSUS_PASS b=2..10
POSITIVE_POLYNOMIAL_CERTIFICATE_PASS
ODD_THRESHOLD_RATIONAL_WITNESS_PASS
VERIFY_OK
```

These checks are finite or exact algebraic spot certificates; the proof of the unbounded statement is in RESULT.md. The sign-variation bound, monotonicity and limiting arguments are mathematical deductions in that proof, not separately externally certified.
