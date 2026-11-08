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

The normalized Landau-level field, derivative covariance and marked Kac–Rice formula are specified in RESULT.md. The analytical proof derives the full condition-number distribution and its sharp tail; the embedded Python checker verifies exact rational antiderivatives and numerical integration for representative orders and thresholds.

Run `python3 CHECK.py` in the same directory as the other files, using Python 3 standard library only. Verified local output: `HERMITE_PALM_CONDITIONING_CHECKS_PASSED`.

The test covers finite parameter samples and is not a proof for all orders or all condition-number thresholds. The result is a Palm mark law, not a sample-based detection guarantee; none of these checks constitutes independent mathematical validation.
