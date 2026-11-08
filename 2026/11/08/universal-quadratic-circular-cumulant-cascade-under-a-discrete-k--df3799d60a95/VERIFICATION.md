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

Run `python3 verify.py` (Python standard library only). The checker uses exact rational quadratic polynomials for each moment, then generates cumulants by an independent triangular recurrence, and checks direct complex nonlinear sine-kick integrals using midpoint quadrature. It checks five exact Poisson parameters and 40 direct quadrature cases. The analytic proof covers arbitrary interior complex Poisson parameter, real rotation and every **fixed** integer harmonic order; computation alone does not certify infinitely many orders.

The check does not simulate self-consistent long-time dynamics or test non-weak coupling. No independent scientific audit was performed.
