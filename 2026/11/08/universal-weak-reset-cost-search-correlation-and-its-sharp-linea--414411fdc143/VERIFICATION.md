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

The standalone `check_cost.py` evaluates explicit Brownian killed-resolvent integrals, their derivatives, first-passage moment formulas and resulting Pearson coefficients for multiple power costs and costs multiplied by a nonconstant slowly varying logarithmic factor. It checks variance positivity and numerical convergence to the gamma-function profile.

Run `python check_cost.py` using Python 3 with SciPy and NumPy installed. These finite computations independently test the analytic formulas but do not prove the infinite-parameter and regularly varying statements. Those follow from the renewal identity, the resolvent split and dominated-convergence/Potter bounds described in `RESULT.md`. No independent scientific audit has been performed.
