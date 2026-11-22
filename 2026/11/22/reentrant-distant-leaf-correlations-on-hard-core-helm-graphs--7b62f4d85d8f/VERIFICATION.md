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

Execute `python3 verify.py` with the standard Python 3 library. The script computes the exact two-site covariance from independent rim configurations and compares it with the conditional partition formula for several even sizes and rational activities. It also checks the stated transfer ratio, unit-activity signs and limiting-sign probes. Observed result: `NEW_HELM_CHECKS_PASSED 76`. All-size statements, including the exponential-scale existence result, are proved in `RESULT.md`; finite tests are supplementary. Independent scientific audit has not been performed.
