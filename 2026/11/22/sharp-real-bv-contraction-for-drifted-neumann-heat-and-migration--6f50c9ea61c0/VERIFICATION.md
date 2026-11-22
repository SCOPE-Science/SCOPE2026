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

# Reproducibility and limits

Run `python3 CHECKER.py` in the same directory as this file. It uses only Python 3 standard-library mathematics. The checker independently integrates the positive Dirichlet column by Simpson quadrature, compares against the sine expansion at several positive times and signed drifts, verifies reflection, locates sampled unique peaks, recovers the driftless odd-mode sum, and tests the leading short-time and first late-time migration terms.

The actual replay yielded:

```text
POSITIVE_KERNEL_COLUMN_AND_UNIQUE_PEAK_SAMPLING_PASS
DRIFT_REFLECTION_AND_INDEPENDENT_QUADRATURE_PASS
DRIFTLESS_ODD_MODE_IDENTITY_PASS
SMALL_TIME_DRIFT_COMPENSATION_AND_DEFICIT_PASS
LONG_TIME_OPTIMIZER_FIRST_SPECTRAL_CORRECTION_PASS
ALL_DRIFTED_NEUMANN_BV_CHECKS_PASS
```

The checker tests finitely many real parameters and finite spectral truncations; it does not prove the positivity, all-drift uniqueness, or asymptotic remainders. Those follow from the gauge-transformed killed kernel, Gaussian log-concavity and one-dimensional spectral/first-passage analysis in `RESULT.md`. The analytical result has not received an independent mathematical audit.
