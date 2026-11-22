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

# Verification record

The exact mathematical argument is in `RESULT.md`. Two executable Python 3 programs using only the standard library are included: `verification/exhaustive.py` computes recursively the mex of every actual legal suffix deletion on all 32,767 nonempty binary words of length up to 14 and checks the excursion-run formula, while `verification/series.py` computes formal coefficients through length 78 and compares them with a separately implemented renewal recurrence through length 50, including normalization and the parity and extremal identities. To replay, run each program from the package root and compare stdout with `verification/checks.txt`. The recorded outputs are the actual output of successful executions. These tests cannot establish the all-length assertions by themselves; the proof supplies that extension.
