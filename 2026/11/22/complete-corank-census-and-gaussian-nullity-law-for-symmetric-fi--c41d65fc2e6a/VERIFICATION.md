---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The unchanged `check_tridiagonal.py` constructs each matrix, performs row elimination and compares its complete nullity histogram with the supporting polynomial recurrence. The recorded `check_output.txt` reports 18 field-size and dimension pairs, 9,887 matrices, and includes the nonprime field \(\mathbb F_4\). These finite checks concern the supporting recurrence, not the Gaussian limit. The proof combines the known invertible census with the unique block decomposition and then analyzes the dominant root of the marked generating function.
