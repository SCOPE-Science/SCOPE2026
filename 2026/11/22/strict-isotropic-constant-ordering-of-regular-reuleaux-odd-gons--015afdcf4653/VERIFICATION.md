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

The self-contained file `verify.py` runs in the Python 3 standard library and verifies the exact rational algebraic certificate for strict monotonicity on the whole interval. Its checks cover the polynomial derivative identity, tangent coefficient recurrence, 43 exact rational polynomial coefficients, and the global tail and derivative bounds. It then numerically reconstructs the boundary flux integrals for eight odd orders and checks several further strict sample inequalities. Numerical checks are supplementary; the global proof uses an explicit analytic coefficient bound plus exact rational inequalities.

`python3 verify.py` was run on the included file and returned `PASS`. No external mathematical audit has been performed. The result does not claim optimization over irregular constant-width bodies or a direct all-order computational enumeration.
