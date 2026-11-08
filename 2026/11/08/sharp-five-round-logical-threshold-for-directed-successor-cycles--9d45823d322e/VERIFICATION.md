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

The included `checker.py` uses only Python's standard library and prints `DIRECT_GAME_CHECKS_OK` and `ALL_CHECKS_OK` upon completion. It verifies every cycle length from \(1\) through \(32\) and every rank from \(1\) through \(5\), plus a separate EF minimax cross-check for length at most \(7\) and rank at most \(3\). The infinite range is handled by the cyclic-gap Duplicator strategy in `RESULT.md`, not by extrapolation from executable output.

The checker uses exact structural keys, including atomic equality/successor matrices and complete sets of recursive extension types. Its numeric intern IDs are symbols for exact keys and have no independent numerical significance. The result does not claim Lean verification, independent certification, or a higher-rank recurrence beyond the stated range.
