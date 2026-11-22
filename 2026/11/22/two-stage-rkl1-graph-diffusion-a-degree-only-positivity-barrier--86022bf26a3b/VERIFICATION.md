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

Run `python verify.py` using Python 3 standard library. Observed output from the included checker:

```
PASS 1099 labelled simple graphs with n<=5, 40565 exact checks; 100 star sizes and exact witness -1/8
```

The checker uses rational matrix powers and exact sign tests on each labeled simple graph of order at most five at twelve fixed rational steps, plus analytic star-entry formulas tested for one hundred integer sizes and a four-vertex rational witness. The finite checks do not establish the all-graph or continuum-in-step quantifiers; the fully written entrywise sign and spectral proofs in `RESULT.md` do. Modified RKL1, nonlinear evolution and floating-point error were not tested.
