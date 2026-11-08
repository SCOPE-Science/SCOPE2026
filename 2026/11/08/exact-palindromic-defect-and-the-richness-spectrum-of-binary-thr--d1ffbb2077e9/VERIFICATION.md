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

# Verification of the fixed-content defect formula

The theorem gives an unconditional symbolic derivation of the defect and a separate rational generating-function argument. The stand-alone program `verify.py` is an ordinary finite cross-check, not a proof of the infinitely quantified statement.

Reproduce with `python3 verify.py` from the directory containing this file. It uses the Python standard library and directly enumerates the set of distinct palindrome factors for each of 52,360 binary words with three ones at lengths 3–34. It compares the direct result with the closed-form defect, the four palindromic-factor classes, and exact defect-layer coefficients. It also checks the min/max identities for all \(18^4=104976\) gap tuples and verifies the atom, first two moments and variance by exact rational integration.

Observed output:

```
VERIFY_OK 52360 direct words; 18^4 algebra tuples; rational moments
```

**Limits of checks:** Neither the 52,360 direct words nor the gap grid constitute exhaustive verification for unbounded lengths. The all-length claim rests on the marker-class decomposition, its case split, the formal-series bijection and coefficient asymptotics given in `RESULT.md`. The finite tests can detect implementation or algebra errors only within their tested domains.
