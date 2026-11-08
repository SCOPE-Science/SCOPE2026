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

# Reproducibility

Run `python verify.py` with Python 3, SymPy and NumPy. The script symbolically verifies three gap identities, the force derivative, and two exact trigonometric relations; it checks the strict logarithm inequality on four rational samples and exact Jacobian eigenvalue formulas at six parameter values. This is finite corroboration only, not an independent certificate or proof of the all-parameter result. Refer to `RESULT.md` for analytic proof and citations.
