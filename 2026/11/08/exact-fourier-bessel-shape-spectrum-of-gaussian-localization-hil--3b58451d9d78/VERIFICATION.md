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

# Verification scope

The exact analytical proof is in `RESULT.md`. Running `python checks.py` with NumPy and SciPy re-evaluates the original squared Hilbert–Schmidt Gaussian double integral by independent tensor-product Gauss–Legendre quadrature in squared-radius and angle coordinates; it does not insert the Bessel formula into the quadrature integrand. It checks three areas and angular modes 2 through 5, several area-dependent Bessel inequalities, and the predicted extreme-area coefficient laws. The numerical tests use finite angular and radial grids and therefore cannot replace the Taylor argument, the all-mode Bessel ordering proof, or a uniform-in-function statement. No independent mathematical audit has been performed.
