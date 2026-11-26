---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

## Reproducible checks
Run `python3 verify.py` using Python 3.10 or later. The original program uses standard-library rational arithmetic and no external data or network. It includes 28 sampled noninteger Vandermonde consistency checks, alongside integer-order consistency checks at orders 1 through 6 for the comparison described in `RESULT.md`. The original package records this output:

```
PASS: m=1,...,6 exact polynomial-kernel and spectral-product identities;
PASS: 28 noninteger finite Vandermonde consistency certificates.
```

## Mathematical and scientific limits
The general claim is proved by the kernel expansion on a separated rectangle, the resulting Vandermonde independence for arbitrarily many columns, compactness, and reflection anticommutation. The numerical or exact-arithmetic checks at finitely many examples do not establish any universal rank or inertia statement. The integer formulas are supplied for comparison and credited in `RESULT.md`. Noninteger eigenvalue decay rates and the nullspace are outside the claim. Historical priority over possible broader convolution results is not asserted.
