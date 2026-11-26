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

# Reproduction of the finite census

From the directory containing the supporting files, run `python3 verify_forward.py` and `python3 verify_independent.py`. They use only the Python 3 standard library. They cover all labelled ternary configurations, respectively by classifying an integer-encoded successor table and by following directly updated tuple trajectories. Compare the period-resolved output lines and individual basin sizes with the table in `RESULT.md`; the captured outputs are `forward.out` and `independent.out`. The second implementation also constructs the twelve Latin-square states and checks their equality with the nonzero recurrent configurations on the grid. The enumerations verify only the finite claims for orders five and nine. The all-order comparison is background supplied by a general theorem, not by computational extrapolation.
