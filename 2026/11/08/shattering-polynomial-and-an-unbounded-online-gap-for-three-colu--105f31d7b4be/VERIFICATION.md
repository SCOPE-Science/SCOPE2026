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

# Reproduction

Run `python3 check_grid.py` with the Python 3 standard library. The checker constructs paths as east/north step words independently of the ordered east-step-height representation. It verifies every two-query and three-query trace for heights 2 through 12, the four-family pair classification, every stated coefficient, and equality of the two concept representations through height 7. It computes exact finite Littlestone dimensions by memoized binary-tree recursion for heights 2 through 10 and compares them with the proved inequalities.

Successful execution prints `THREE_COLUMN_MONOTONE_PATH_VC_ONLINE_PASS`. These are finite consistency checks, not independent mathematical proof of the all-height theorem. Universal proofs and the list of scientific limitations appear in RESULT.md.
