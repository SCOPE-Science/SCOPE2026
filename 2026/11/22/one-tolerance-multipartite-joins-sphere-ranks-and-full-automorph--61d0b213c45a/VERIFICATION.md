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

Run `python3 CHECK.py` with Python 3 standard library. The check enumerates all automorphisms for the class-size patterns `(2,2,2)`, `(2,2,2,2)`, `(3,3,2)`, `(3,3,3)`, `(2,3,2,3)` and tests the signed simplicial-chain Lefschetz character against the independent orbit-cycle formula (2,448 checks in total). It also reduces each full simplicial boundary complex modulo 2 and modulo 3 for eight class-size patterns and verifies that the only reduced homology is in the predicted top dimension with the predicted rank.

**Proof boundary:** Exhaustive tests apply only to those finite patterns; they neither certify an infinite family nor imply integral torsion-freeness. The separate null-inclusion homotopy-pushout proof establishes the integral wedge uniformly. The character follows from an all-automorphism invariant-face enumeration, not interpolation from the finite tests. No independent external mathematical audit has been performed.
