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

The standalone `verify_equilibria.py` requires Python 3 and the standard library. Execute `python3 verify_equilibria.py` to check the polynomial identity, rational coefficients, four sign-changing brackets and positivity of both prey and predator densities.

The finite exact arithmetic verifies the supplied witness. The at-most-four theorem and persistence under perturbations are justified by the general polynomial identity, the intermediate value theorem and strict inequalities in `RESULT.md`; finite enumeration is not an infinite proof. The zero-polynomial degeneracy is excluded from the theorem. No independent mathematical audit has been performed.
