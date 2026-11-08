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

The standalone `verify.py` was run directly using Python and returned:

```
DYCK_PRIMITIVE_MULTIPLIER_EXACT_OK M=2,3 tested_cases= 91
```

It exhaustively enumerates full-shift representatives for \(M=2\) up to \(n=10\) and \(M=3\) up to \(n=8\), comparing exact primitive heights with the divisor formula. The small enumeration cannot establish statements at arbitrary period or the asymptotic distribution. The manuscript supplies a mathematical argument using symbolic coding, divisor inversion, binomial tails, Stirling asymptotics and a transferred central limit theorem. No external independent verification was conducted.
