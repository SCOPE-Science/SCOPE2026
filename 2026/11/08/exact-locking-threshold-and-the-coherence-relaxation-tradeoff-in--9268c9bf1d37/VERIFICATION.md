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

The analytic proof is contained in `RESULT.md`. The executable `verify.py` requires Python 3, NumPy and SciPy and checks the exact normalization, implicit branch, symmetric eigenvalues of the full three-node Jacobian, strict monotonicity for finite sample parameters, and leading asymptotic coefficients.

The script was run locally and printed `VERIFY_OK checks=423 asymptotic_cases=15 full_jacobian_and_phase=52`. Its samples include 13 exponent values, 7 budget multipliers, monotonic sequences, and 15 large-exponent asymptotic cases. The main theorem remains an analytic theorem; finite testing is only corroboration. None of these checks proves a global basin classification or independent historical priority.
