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

Run `python3 check.py` using Python's standard library. The script performs an independent self-map enumeration for \(2\le n\le6\), compares exact Walsh multipliers, checks the pointwise derivative identity algebraically for \(2\le n\le25\), and tests the claimed signs for \(2\le n\le49\). These are finite consistency checks; all-order strict negativity follows from the explicit integral sign proof in RESULT.md. No independent validation has occurred.
