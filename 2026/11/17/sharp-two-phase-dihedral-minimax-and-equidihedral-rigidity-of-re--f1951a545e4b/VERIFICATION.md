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
# Direct reproducibility checks

Run `python verify.py` using the Python standard library. The verifier computes all three types of ridge-normal pair directly from unit three-dimensional vectors for orders \(3\le n\le24\) and samples admissible positive heights. It separately checks the global minimum and the fixed-normal-asymmetry envelope over a discrete admissible grid; a passing numerical grid is **not** a continuum or uniqueness proof. The analytical proof in `RESULT.md` establishes the unrestricted claim. The run performed 172,040 passed assertions using floating-point tolerance \(10^{-12}\) for angle identities and a coarser tolerance for sampled extremum proximity. No independent audit was performed.
