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

Exact verification uses the included standalone `verify.py` (Python 3 standard library). It exhausts every uniform recursive-tree parent sequence through nine vertices and checks leaf-event probabilities, mean total path length, every indexed conditional mean and covariance, and the total leaf-count covariance with exact rational arithmetic. The same file evaluates the analytic conditional-mean recurrence for all intermediate indices through 159 vertices.

Execution outcome: `PASS: 669769 mathematical exact assertions, 46233 enumerated trees, n<=9 exhaustive, recurrences through n=159`.

Enumeration covers only finite orders; the universal result is justified by the independent-choice conditioning and exact recurrence in `RESULT.md`. No independent audit or external certification is claimed.
