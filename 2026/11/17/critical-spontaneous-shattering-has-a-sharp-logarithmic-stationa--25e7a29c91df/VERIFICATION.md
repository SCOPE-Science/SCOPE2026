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

The accompanying `check_stationary.py` performs exact fraction arithmetic for 18 recurrence coefficients and their generating-ODE identities; a separate finite prefix of 6,000 positive coefficients provides a numerical consistency check. Command: `python3 check_stationary.py`. Expected opening line: `VERIFY_OK exact_series_coefficients=18 finite_prefix=6000`. The numerical residuals are neither bounds for all cluster sizes nor evidence of an infinite asymptotic by themselves.

The analytical proof verifies initial coefficient normalization, radius-one existence via positive-series Pringsheim theorem, boundary derivatives, transformed ODE asymptotics and the Tauberian passage from a generating function to a nonincreasing tail. Classical Laplace Karamata and monotone density theorems are invoked explicitly rather than reconstructed as external certificates.

Scientific limits: exact critical rate four; mass-one infinite stationary solution; no assertion about dynamical relaxation, noncritical parameters, or numerical solvers' global convergence. Independent scientific audit has not been performed.
