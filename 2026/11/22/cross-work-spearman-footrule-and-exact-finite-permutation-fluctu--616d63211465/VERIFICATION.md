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
Run `python3 verify_crosswork.py` with Python 3's standard library. It enumerates all permutations at sizes two through eight and all full transformations at sizes two through six, checking the original cross-work expression, pointwise decomposition, exact means, the permutation variance and covariance, and the full-transformation variance. Additional exact rational-matrix checks cover sizes nine, ten, twenty, fifty and one hundred. All pass with `VERIFY_OK`. The mathematical proof in RESULT.md handles all finite sizes; a finite computational sample alone is not a proof of universal claims. There is no external or independent mathematical audit.
