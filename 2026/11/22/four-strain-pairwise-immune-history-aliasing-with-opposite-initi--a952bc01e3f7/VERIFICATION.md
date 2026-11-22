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

# Verification record

`verify.py` is standalone and uses only Python 3 standard-library exact fractions. Run `python verify.py` from the directory containing that file. The program checks 4005 exact-rational equalities and inequalities, including the all-eight-class probability law, low-order equal marginals, all displayed rational susceptibility and derivative values, Möbius inversion through seven previous strains, and parity-trade cancellation through six.

Expected output:

```text
PASS: exact rational checks: 4005
Sharp H interval at c=1/2: 13/32 7/16
Positive-compartment initial growth rates: 1/54 -1/54
```

The infinite family and iff claim follow from the algebraic proof in `RESULT.md`; finite tests alone are not offered as proof. All sources are scientific references rather than independent validation. No independent audit has been performed.
