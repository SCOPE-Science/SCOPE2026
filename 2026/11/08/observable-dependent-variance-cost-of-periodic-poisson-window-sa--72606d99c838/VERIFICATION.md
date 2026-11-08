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

# Verification and limits

The associated `verify.py` executes without external packages using standard Python 3 and prints `PASS final total 324 algebraic and numerical diagnostics`. It compares exact finite bivariate Poisson–Charlier moments with the claimed generating-function identity; checks finite Fourier sums for several real periodic profiles; and numerically integrates sinusoidal overlap kernels against their exact analytic values. All these checks were run directly from the submitted file, not from a previous executable.

The proof's infinite-state and asymptotic claims have separate analytic support: completeness and orthogonality of Poisson–Charlier polynomials in Poisson \(L^2\), the Poisson overlap decomposition, monotone convergence for the positive chaos covariance series, Fourier strictness for measurable bounded periodic rates, and the stationary one-dependent central limit theorem for period-block averages. No finite computation proves the CLT or historical originality. The theorem is restricted to unit-period deterministic arrival rates, unit-width observation windows, a one-dimensional Poisson count and continuous physical-time averaging.

Scientific novelty assessment is provisional; no independent audit was performed.
