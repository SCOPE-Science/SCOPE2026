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

The proof directly establishes the full complex-geometric claim. Execute `python3 verify.py` with Python 3 standard library, inside the extracted package. Expected exact output: `VERIFY_FERMAT12_OK nodes=12 quadratic_orbits=6 dual_orbit=1280`. The checker enumerates all 81 cube-root cyclotomic coordinate patterns and verifies the 12 valid solutions, their defining and gradient equations, Galois pairing, and the orbit cardinality. The nonstandard geometric steps are separately proved in RESULT.md: Hessian rank three, dual multiplicity equals total Milnor number, and automorphism-stabilizer classification. Finite checks are not substituted for infinitary arguments. The equation of the section was known (Jacobi–Madden); the historical full text was not accessible. No independent audit has been performed.
