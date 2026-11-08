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

Run `python CHECK.py` in a Python environment with NumPy and SciPy. The expected terminal line is `BALANCED_QUADRATURE_CHECKS_PASSED`. The code checks the real Hermitian measurement matrices on multiple radii and phase-offset choices, degeneracy counterexamples, the explicit null generator and the Gaussian transform identity by numerical integration. These finite tests do not establish the all-parameter assertion or publication priority; the symbolic argument in `RESULT.md` does.
