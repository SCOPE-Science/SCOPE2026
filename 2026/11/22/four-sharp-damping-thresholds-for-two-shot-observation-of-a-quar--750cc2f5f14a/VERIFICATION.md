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

Run `python3 verify.py` with Python 3 and its standard library; it prints `VERIFICATION_OK` and the four threshold values. The checker compares exact rational polynomial eliminations, verifies root brackets and multiple direct two-row Gramian traces and determinants, and performs 6970 finite numerical comparisons at lags through 64. These tests do not prove any quantifier over all integers or damping values; the analytic elimination and monotonicity arguments in RESULT.md provide that proof.

The source comparisons include the complete accessible arXiv/HTML materials and publicly available related results, but absence of a matching result is not proof of exhaustive historical originality. The statuses in this file do not assert an external audit.
