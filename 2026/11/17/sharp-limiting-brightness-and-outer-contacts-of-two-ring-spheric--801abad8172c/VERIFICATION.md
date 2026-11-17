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

The analytic proof checks cubic moment equalities using the regular-grid Fourier sum, constructs the equal-area Minkowski polytope by the standard existence theorem, derives brightness from Cauchy's area projection formula, and proves the sharp outer radius using the second-moment Cauchy--Schwarz equality condition. The limiting inner radius follows from an explicit uniform circle quadrature error, a one-variable integral, and a strictly concave root equation.

The companion script `check_projection_design.py` was executed successfully with Python, NumPy, and SciPy. It passed 1,948 finite numerical assertions for \(4\le n\le30\); the finite tests are not a proof of the universal or asymptotic claims. The minimizer convergence follows from uniform support convergence and uniqueness of the limiting polar-height minimizer. The listed radius decimals are approximations; the implicit root equation and radicals define the exact quantities. No external mathematical audit has been performed.
