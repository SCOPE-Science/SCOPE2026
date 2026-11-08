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

The `verify.py` script runs with Python 3 and SymPy and prints `VERIFY_OK` and `GENERAL_CUBIC_VERIFY_OK` when exact symbolic checks pass. It reconstructs the equilibrium equation, parameterization, fold, quadratic contact, center drift coefficient, Jacobian signs, and a rational two-equilibrium witness. The coefficient positivity and infinite root count follow from the documented analytical proof; finite code checks are not exhaustive certification. Independent validation has not been performed.
