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

# Reproducibility and verification

Run `python3 verify.py` with Python 3.9 or later. The script enumerates all degree-at-most-two simple graphs on two through five vertices and compares every vertex-query support with the two-edge-count structural criterion. It also independently enumerates path concepts and every queried coordinate support through length twelve, checks weighted state-polynomial counts and the sharp dimension formula, and verifies a degree-three counterexample. The transcript in `verification_output.txt` was produced from the embedded `verify.py` file.

Every invariant is proved for all stated parameters in `RESULT.md`; the computation is finite corroboration, not an all-order completeness argument. Historical priority against unindexed literature and external independent audit remain open.
