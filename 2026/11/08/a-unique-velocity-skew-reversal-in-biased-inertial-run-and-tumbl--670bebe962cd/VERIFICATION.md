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

Run `python3 check.py` in a directory containing the extracted standalone file. The script needs only Python 3 standard library. It reconstructs stationarity equations with exact rational arithmetic and compares them to the exact cubic tensor over a finite grid; it separately evaluates causal-filter third-cumulant integrals in the underdamped regime. The observed output for the supplied file is:

```
PASS: 1096 exact-rational generator assertions and 12 independent impulse-filter quadratures
```

Finite checking does not prove the global identities, convergence of the stationary filter, or uniqueness of the sign transition; the mathematical argument for all admissible parameters is in `RESULT.md`. No independent scientific audit or external validation has been performed.
