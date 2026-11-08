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

The exact-integer verifier `verify_relation.py` constructs both four-vertex labeled de Bruijn relations, determines all reachable Boolean-relation states (83 for Rule 172 and 34 for Rule 184), and checks each of the 117 recurrence equations needed for the Cayley–Hamilton proof. It separately records the initial values. `direct_check.py` independently enumerates each binary cyclic input and compares the full image-set cardinalities for both rules at lengths 1 through 16. Both scripts were executed successfully from the complete package. The direct checker also asserts that length-five output `11000` is present only for Rule 172. The infinite result follows from the proven finite-state representation and Cayley–Hamilton, not from extrapolation of the direct enumerations. These verifications are not an external independent audit.
