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

# Reproducible checks
Run `python3 verification/checker.py` (standard library only). On this package the program returned:

```
PASS: 32000 exact rational assertions, dimensions 1..5; infinite theorem uses analytic proof
```

The program checks exact-rational simultaneous witnesses and universal upper inequalities at specified rational test points over 500 random center pairs of dimensions 1–5, and verifies the exact excess identity and coordinate-antipode relation. It does **not** enumerate arbitrary real inputs and it is not a proof of the infinite theorem. The proof uses the circle half-turn identity, triangle inequality, and the explicit complementary-arc midpoint in every coordinate.

Limits: only intrinsic sum-metric product-circle tori, two prescribed sites, no assertion of independent audit or historical priority certification.
