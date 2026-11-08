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

# Reproduction

Run `python verify.py` with NumPy and SciPy installed. The script uses the fixed pseudo-random seed 314159; it compares the smaller eigenvalue of the exact two-plane compression against the rationalized error-ratio formula, tests Gaussian-coupled local multipliers against the relevant beta CDF and its first three moments, and checks the algebraic first-moment formula over multiple codimensions. Executed output: `PASS 1851 matrix/beta-moment/limit/joint checks; 5 codimensions, exact RR matrix formula`.

# Analytical checks and boundaries

The proof in `RESULT.md` derives the exact compression and its rationalized smallest-eigenvalue expression, so convergence follows from almost-sure Gaussian coupling and the independent chi-square ratio. Boundedness by one justifies moment limits. The iteration's orthogonal symmetries justify a scalar conditional kernel, and monotonicity of the squared error allows induction for any fixed finite horizon. Numerical checks are finite and do not establish the limits on their own. Floating-point conditioning at much smaller errors and global iteration counts are untested.
