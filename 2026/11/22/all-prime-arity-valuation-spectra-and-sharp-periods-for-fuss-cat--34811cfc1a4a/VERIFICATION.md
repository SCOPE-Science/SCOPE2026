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

# Reproducibility

Run `python verify.py` using Python 3 with standard-library modules only. Its independent exact-integer enumeration checks the Fuss–Catalan normalizations for fixed sizes 2 through 27, 40 variable arities per case, and primes 2, 3, 5, 7. Exact-rational carry matrices are compared with full valuation histograms on 352 complete prime-power periods; the period-sharpness test seeks actual unequal valuations under the unique next-shorter prime-power shift. The mean check covers 400 digit columns.

The expected final line is:

```
VERIFY_OK assertions=59040 full_period_histograms=352 primes=2,3,5,7 mean_cases=400
```

These finite computations only test specified instances. The unrestricted theorem follows from the algebraic normalization, Kummer carry-count argument, tail generating function and least-period proof in `RESULT.md`. No independent mathematical audit has been performed.
