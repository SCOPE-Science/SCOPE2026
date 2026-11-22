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

The dependency-free Python 3 program `checker.py`, in the same directory as this document, implements an interval private-site / greedy piercing support test and a separate exhaustive enumeration of all prescribed-cardinality cut sets and realized traces. The command `python checker.py` completes with `FIXED_BLOCK_INTERVAL_SHATTERING_PASS` when all assertions hold. Its actual captured output is included as `verification_output.txt`.

The recorded completed run checked 397,284 finite support decisions (all supports for up to five sites; supports of size at most five for six sites), 45 complete dimension cases for cut-site counts up to eight, and 3,040 additional deterministically sampled support decisions for seven through ten sites. The checker separately tests the exact closed dimension formula against recursive trace-fiber splitting. It does not formally certify the all-parameter theorem, which is established by the mathematical argument in `RESULT.md`.

Every executed finite comparison passed. No independent review or external mathematical audit has taken place. Generic interval-piercing algorithms, and the code's finite coverage, do not establish novelty or exhaustive prior-art search coverage.
