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

# Reproduction and limitations

The accompanying `check.py` verifies four exact symbolic relations for the bridge-knot covariance, rational derivative, transformed-degree-six objective and discriminant, and reports the unique algebraic turning point to 30 digits. Its finite diagnostic comparisons use seven noise regimes and 1,000 pseudorandom time pairs per regime with fixed seed; they cannot replace the analytic uniqueness, centering and global optimality proofs.

Requirements: `python` with the versions in `requirements.txt`; run `python check.py` from the package directory. The finding does not require datasets, external models, or hidden input files. All stated numerical digits are approximations to uniquely characterized algebraic numbers. The exact results are provided by the equations and their sign certificates. No independent scientific audit was performed.
