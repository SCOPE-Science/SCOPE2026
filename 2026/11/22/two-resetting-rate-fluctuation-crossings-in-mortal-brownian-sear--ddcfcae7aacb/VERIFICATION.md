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

# Reproducibility checks

The standalone `check.py` runs under Python 3 using only standard-library `decimal` and integer arithmetic. It verifies the derivative-polynomial identities by exact coefficient operations and numerically compares the conditional mean and variance with the previously published explicit formulas for a collection of regimes. With 72-digit decimal precision, it isolates the unique maximum of the crossing curve and both positive crossings at mortality \(m=1.05\). It checks the first 500 Taylor coefficients, but the proof that **all** remaining coefficients are positive is in `RESULT.md`, using an induction valid for every integer \(n\ge11\). The numerical root calculations are reproducibility diagnostics, not infinite-sign or uniqueness certificates on their own.

Run from the file directory:

```bash
python3 check.py
```

The verification is analytical and computational; an independent external audit has not been carried out. The stated mathematical limitations and the distinction between known formulas and new zero-count analysis are described in `RESULT.md` and `REVIEW.md`.
