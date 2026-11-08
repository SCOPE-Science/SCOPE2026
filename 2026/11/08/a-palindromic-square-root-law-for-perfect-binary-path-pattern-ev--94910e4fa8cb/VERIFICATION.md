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

The included `verify.py` independently enumerates all binary diagonal strings in sizes 2 through 12 and checks invertible and palindromic counts against exact formulas. In sizes 2 through 6 it tests every permutation of all perfect structure matrices to confirm the full ordinary automorphism group. The checker requires only standard-library Python. The general theorem follows from the continuant proof and the established monomial-isomorphism theorem; exhaustive tests are finite checks, not an infinite certificate.
