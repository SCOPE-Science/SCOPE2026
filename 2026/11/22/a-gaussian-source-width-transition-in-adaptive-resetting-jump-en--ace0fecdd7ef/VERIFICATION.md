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

The companion executable `checks/verify_jump_width.py` was run with Python 3, SciPy quadrature and scalar minimization; its 47 deterministic numerical/structural checks passed. The checks cover positive-hazard boundary optimization, zero-mean balance, finite-second-moment coefficient, entropy positivity and monotonicity for representative values, and high-rate/crossover numerical comparisons. The latter use deliberately broad tolerances because logarithmic convergence is slow; no finite set of samples is represented as a proof of the asymptotic theorem.

The exact proof depends on the Gaussian Fokker–Planck identity, stationary flux factorization, Gamma-half tail with the specified prefactor, a convergent Mellin integral for subcritical exponents, a critical truncated-second-moment estimate, and uniform localization of the crossover integral. Each is stated in `RESULT.md`. The assumptions exclude bounded reset-policy implementation, multidimensional source covariance, and physical work required by an engineered reset mechanism. The standard diffusion contribution stays positive, independently of the vanishing jump-channel term. Independent audit remains unperformed.
