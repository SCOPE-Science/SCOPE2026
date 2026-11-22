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

`verification/check.py` uses only the Python standard library and verifies 29 exact-rational assertions: exhaustive comparisons of ranking moments for the specified small graphs and independent local pair-probability identities for hypercubes through dimension nine.

Command: `python3 verification/check.py`.

These checks do not prove the unbounded moment statement. Its proof is the vertex-transitivity, separated-neighborhood and cumulant cancellation argument in `RESULT.md`. Publication-priority comparison of every possible synonym or all general dependency-graph literature is not certified. No independent audit has been performed.
