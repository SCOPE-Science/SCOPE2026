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
# Verification record

The statements have an analytic proof in `RESULT.md`. Supplementary tests come from the embedded `checker.py`, runnable by `python3 checker.py` with standard Python 3 and no external packages. A fresh replay reported `PASS: 31080 finite assertions; example uniformization time=0.963457252632`. These tests include independent exhaustive contiguous-block partition evaluation through dimension seven and randomized consistency checks in dimensions up to eleven. They do not prove the assertions for arbitrarily many classes or establish historical priority.

The exact uniformly mixed threshold is defined only for nonconstant descending rank weights and strictly positive input probabilities. An independent mathematical audit has not been performed.
