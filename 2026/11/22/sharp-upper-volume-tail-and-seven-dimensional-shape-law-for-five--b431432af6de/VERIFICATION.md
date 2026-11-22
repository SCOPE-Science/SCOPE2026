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

The volume identity is computed exactly from two pyramids sharing a triangular base. The standalone `verify.py` constructs this identity with symbolic square roots, differentiates at a triangular bipyramid, checks the whole seven-coordinate Hessian, its determinant and all eigenvalues, and checks the twenty-branch measure normalization yielding \(24/7\).

Replay command: `python verify.py` (requires SymPy). Recorded result: `ALL_CHECKS_PASSED`. This check does not constitute an independent audit or a numerical proof of the full limit; the compactness localization and total-variation passage are argued in `RESULT.md`. Historical priority has not been independently certified.
