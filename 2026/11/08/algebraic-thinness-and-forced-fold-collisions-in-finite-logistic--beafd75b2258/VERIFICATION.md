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
The exact checker `verify.py` was run with Python 3 and SymPy. It established polynomial quotient divisibility and degree formulas for iteration orders one through three; nonzero symbolic resultants for all nine factors of the size-two elimination polynomial; exact two- and three-point invariant sets; and finite checks of the candidate-count formula for bounds one through five.

The all-size theorem is an analytic proof, not a finite computational census. Symbolic tests at bounded orders do not prove nonvanishing of every elimination resultant at arbitrary order. The proof supplies that by choosing the first parameter to be two and excluding endpoints from the resultant root set. The code also does not test historical originality or establish attraction or probability distributions.
