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

# Verification record

The mathematical proof appears in `RESULT.md`. Running `python3 check.py` from the extracted package verifies analytic gamma moments, sphere constants, exact two-/three-dimensional survival functions, and seeded Gaussian diagnostic samples, including a circulating three-dimensional model. The checker requires only Python's standard library and does not download any data.

The direct Gaussian sample simulation is deliberately finite and cannot establish an infinite tail, a divergent moment, or a sharp dimension threshold. Those statements follow analytically from Gaussian polar coordinates and dominated convergence. The universal prefactor requires strictly positive stationary and innovation covariances. The three-dimensional second-moment formula requires isotropic noise and a single skew rotation generator; it is not stated for arbitrary anisotropic diffusion.

This work has undergone self-review only. No independent audit has been performed.
