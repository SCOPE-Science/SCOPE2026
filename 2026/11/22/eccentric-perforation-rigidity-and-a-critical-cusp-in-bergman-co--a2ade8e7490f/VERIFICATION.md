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

The independent finite-matrix diagnostic script `verify.py` passed 43 assertions, testing the analytic disk-moment compression against concentric eigenvalues, the strict global two-mode Rayleigh lower bound, and numerical convergence toward the quadratic and cusp coefficients. Run `python verify.py` in an environment with NumPy installed.

The infinite-dimensional argument is not inferred from the finite matrices: the proof uses a nonnegative spectral Rayleigh equality, a finite Vandermonde inverse, exact centered annular monomial eigenvalues, and analytic perturbation of compact positive operators with an isolated simple or double spectral edge. The asymptotic coefficients follow from the first two monomial components. This is self-review, not independent validation.
