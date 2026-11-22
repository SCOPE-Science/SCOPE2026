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

The standalone `CHECKER.py` uses only Python's standard library. Running `python CHECKER.py` exhaustively checks all forward reveal permutations for six pairs: `(5,1)`, `(6,1)`, `(7,1)`, `(8,1)`, `(6,2)`, `(7,2)`. It reconstructs the forward isolation indicators independently of the reverse-rank formula, checks each maximal isolation interval and killing direction, and verifies the active-isolate expectation by exact integer cross-multiplication. Execution completed with **944805 assertions passed**. The exact checker is reproducible without data or other packages.

The infinite marked Poisson limit is established by the analytical factorial-moment, overlap-cluster, empirical-priority comparison and Poisson time-change proof in `RESULT.md`; finitely many checked instances cannot certify an infinite limit. Assumptions include fixed radius and uniform vertex order. Self-review passed on correctness, originality under inspected sources, and mathematical value. Independent assessment has not been performed.
