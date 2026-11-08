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

The supplied `verify.py` is a self-contained executable checker requiring Python 3, SymPy and NumPy. Run `python verify.py` from this directory and compare with `verification_output.txt`.

It rebuilds the two update matrices, covariance operator, determinant factorization and stationary optimization equalities symbolically, checks the exact rational fixed-step example, and compares matrix spectral radii with the analytic boundary across a finite parameter grid. It produced 812 numeric stability-grid assertions as well as exact symbolic checks, with all assertions passing.

Those finite checks do not establish the continuum claim independently. The proof relies on the analytically justified positive-cone Perron property, simple eigenvalue perturbation at zero step, large-step divergence and strict monotonicity of the boundary polynomial. Earlier publication precedence is not independently certified.
