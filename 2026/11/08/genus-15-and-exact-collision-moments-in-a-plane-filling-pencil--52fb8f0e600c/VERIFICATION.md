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

The two verification scripts `verify_symbolic.py` and `verify_counts.py` are standalone Python 3 programs, the first requiring SymPy. The symbolic program checks the exact polynomial identity, birational Kummer equation, coprime numerator/denominator, seven branch-order arithmetic, and the genus-15 Riemann--Hurwitz calculation. The second directly enumerates the parameter map over seventeen prime fields and three quadratic extensions and independently counts ordered distinct pairs. Congruence-class exact-moment predictions are compared in every applicable field.

These tests executed successfully on the extracted scientific files. Mathematical proof of the all-field statement is provided in `RESULT.md`: its Kummer branch analysis and bijectivity of seventh powers, not finite enumeration, establish the quantifiers. No independent audit or historical-priority validation has been performed.
