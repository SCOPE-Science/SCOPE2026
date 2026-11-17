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

The claim was checked by reconstructing both comparison arguments, the high-predator Lyapunov excursion bound, the reciprocal-predator blow-up identity, and the integrable-error argument giving a strictly positive finite prey amplitude. Exact-rational checks in `checker.py` cover 90 parameter/state cases and three exponent classes; inverse-predator numerical integration illustrates the corresponding finite-time derivative behavior.

Run `python checker.py` in an environment with SciPy. The script checks exact algebraic inequalities with fractions and then evaluates finite numerical diagnostics. It does not prove infinite-domain assertions; those rely on the written mathematical argument. The current claim applies only to the undelayed positive-data ODE and has not undergone independent mathematical audit.
