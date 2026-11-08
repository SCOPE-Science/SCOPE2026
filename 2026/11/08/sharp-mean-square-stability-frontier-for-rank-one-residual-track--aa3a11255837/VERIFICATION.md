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

Run `python verify.py` with Python 3.10+ and SymPy. The verification script checks the closed-form moment matrix, the symbolic factorization of the unit-eigenvalue determinant, the simple eigenvalue derivative at zero, exact-rational conditional transitions and finite sample-word recurrence, and numerical spectral values below and above the proposed threshold. It reports 354 successful checks on the current source.

All analytic convergence statements require the proof in `RESULT.md`: covariance-map cone Perron–Frobenius, symmetry reduction, and a spanning argument for the initialized state. No finite enumeration proves infinite-time convergence, and no automated independent mathematical validation has been performed.

The source's algorithm uses independent uniform singleton samples and stores pre-update row residuals. This verifier tests precisely that convention; drawing without replacement or updating residuals from a post-step iterate would be a different method.
