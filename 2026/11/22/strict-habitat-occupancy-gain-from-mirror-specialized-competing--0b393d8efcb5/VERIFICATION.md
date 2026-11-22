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

## Reproduction

Run `python checker.py` with Python 3, SymPy, NumPy, and SciPy. The script uses the algebraic equilibrium identities and two distinct symbolic Jacobian blocks from the result, exact witness arithmetic, and 158 independent supercritical random parameter tests. The expected final line is:

`PASS symbolic determinant identities, Rayleigh gap, exact example; numerical admissible cases: 158`

## What is and is not verified

The determinant identities, strict Rayleigh-gap normalization, and exact witness are checked symbolically or exactly; positive viable random cases also confirm both Jacobian blocks are Hurwitz and total occupancy increases. Finite parameter tests do not certify infinitely many parameter choices: the analytic proof supplies the universal inequality. Monospecific uniqueness is an established monotone-system result as cited. Independent mathematical audit remains unperformed. The statement is limited to local attraction and makes no claim about nonsymmetric equilibrium uniqueness or stochastic outcomes.
