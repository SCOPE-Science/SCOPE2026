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

The independently written finite-field tests `verify_blocking_quartic_zeta.py` and `verify_independent_field.py` completed successfully. The former enumerates all 567 rational-point-exact quartic forms for one six-point blocker, tests the 222 geometrically smooth forms by complete affine chart Gröbner bases, finds the 10 stabilizer orbits, and calculates all three field extensions and Weil numerators. The latter uses different monic irreducible polynomials for fields of orders 9 and 27 and checks all ten published representatives against direct point enumerations and coefficient identities.

Expected success markers: `BLOCKING_QUARTIC_ARITHMETIC_REPLAY_PASS` and `BLOCKING_QUARTIC_INDEPENDENT_FIELD_PASS`. Both were observed in the current checks. Running the main checker requires Python 3 and SymPy; the independent field checker uses only the Python standard library. The mathematical output is an exhaustive finite-field certificate; it is not a formal proof in a proof assistant and has not received independent external validation. Previous computations and external archives are not required for the checkers.
