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

# Verification evidence and limits

Execute `python3 verify.py` in the directory containing `RESULT.md`, `verify.py` and the other files. It uses only Python's standard library. The checker enumerates all histories for \(q=2\), \(1\le n\le11\); \(q=4\), \(1\le n\le7\); and \(q=6\), \(1\le n\le5\). It tests literal source-to-output transformations, the two canonical marker rewrites, the closed sphere-size formula, and the complete distribution-polynomial recurrence.

Recorded run: `ALL CHECKS PASSED; total sources: 35268`. The nonstandard two-marker alignment lemma and all-length run-factorization are proved in `RESULT.md`; enumerating 35,268 inputs is not an independent all-length certificate. Neither research priority nor optimal code cardinality is certified by the computation.
