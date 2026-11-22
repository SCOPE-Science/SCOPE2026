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

From the directory containing this file, invoke `python3 verify_rule28.py`. The checker reimplements Rule 28 from its eight-entry truth table and, for each indexed cyclic ring length 1 through 15, enumerates all no-adjacent-one inputs. It compares image membership with cyclic avoidance of `111` and `0100`, verifies injectivity and decoding for each source, verifies reconstruction for each allowed output, and checks the Lucas counts. It also exhaustively checks the relevant 5-bit local configurations. The checker prints `VERIFY_OK` on success.

These are finite tests only. For arbitrary length and on bi-infinite configurations, the asserted equivalence is established by the local proof in `RESULT.md`, and the periodic counts by an adjacency-matrix identity. External independent mathematical audit has not been performed.
