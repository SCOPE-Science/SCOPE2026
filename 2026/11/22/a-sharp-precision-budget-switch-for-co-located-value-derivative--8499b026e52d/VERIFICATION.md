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

# Reproducibility and verification

Run `python check.py` from the folder containing `RESULT.md` and `requirements.txt`, after installing the three declared Python dependencies. The script reconstructs from exact symbolic expressions the covariance matrix, both normal-equation coefficient formulas, the mixed information formula, the derivative numerator, the nine transformed polynomial coefficients, the activation-site factorization, and the double-root certificate at the critical activation precision. It also checks the closed-form endpoint allocation and the stationary condition for the pure-derivative observation time.

A complete successful execution on the packaged source produced:

```
threshold 8.578152164906413 transition_site 0.725481854958253 critical_P 12.531972647421808
PASS symbolic identities, covariance integrations, and 131599 supplementary comparisons
```

It additionally checked 21 independent numerical integrations of the Brownian white-noise kernels and 131,599 supplementary conditioning competitors. These are independently assembled numerical diagnostics; their finite sampling does not certify globality. The infinite-domain conclusions are instead justified by the exact positivity, Descartes root-count and envelope-crossing arguments in `RESULT.md`.

The exact crossover \(P_*\) is defined by the unique equality of the displayed analytical information functions; reported decimals are approximations and are not formally interval-certified. The result has no independent mathematical audit or exhaustive historical-priority validation.
