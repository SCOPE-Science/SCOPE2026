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

# Reproduction and limits

Run `python verify.py` in a Python environment containing NumPy, SciPy and SymPy (`requirements.txt`). The verifier checks the exact covariance-square integration, its derivative and the exact quadratic-energy variance, including the continuous Brownian limit. It independently integrates the covariance-square kernel at 25 settings, and checks 19,932 additional competing design values for a parameter grid. It also checks strict monotonicity along the tested noise grid and convergence toward the unique high-noise root.

The proof in `RESULT.md` provides the required global statement over continuously varying damping and noise values. Finite numerical sampling is only supplementary and cannot prove uniqueness for untested parameters. No independent audit was performed.
