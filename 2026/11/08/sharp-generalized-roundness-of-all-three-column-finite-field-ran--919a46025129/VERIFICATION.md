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
# Verification and reproduction

Run `python rank3_checker.py` using Python 3 without third-party packages. The checker constructs rank metrics and exact additive Fourier characters in F2, F3, and F4, then compares their rank-shell transforms with the explicit symbolic formulas. The binary 3-by-3 Walsh transform is exhaustive across all 512 Fourier frequencies; further exact sums check a representative of every rank for 4-by-3 matrices over F2, 3-by-3 matrices over F3, and 3-by-3 matrices over F4 as detailed in the script output. It also evaluates the exact scalar expressions and tests their strict spectral ordering and numerical threshold for fifteen parameter combinations.

Expected final line: `ALL_RANK3_FOURIER_CHECKS_PASSED`.

These finite tests check implementations and sample instances, not the all-field theorem. The universal proof is the row-space character orthogonality and sign comparison in RESULT.md. Exact arithmetic is used for finite Fourier sums; bisection is used only to approximate unique roots whose existence and uniqueness have already been proved. No independent mathematical validation has been performed.
