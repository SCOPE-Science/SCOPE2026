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

The proof reduces the infinite statements to exhaustive subgroup forms, automorphism choices, and finite-generator homomorphism constraints; no infinite conclusion is inferred from finite experimentation.

Reproduce with `python checks/check_dihedral.py` and `python checks/check_generalized_dihedral.py`. The first enumerates actual subgroups and all possible generator images for 14 dihedral orders. The second uses the multiplication law of a noncyclic-kernel generalized dihedral group, enumerates subgroups and tests candidate group homomorphisms by propagation. No third-party packages or external services are required.

Expected terminal markers: `DIHEDRAL_PARTIAL_ISOMORPHISM_OK 3..16` and `GENERALIZED_DIHEDRAL_C3_SQUARED_OK 1458 730 28`. These are finite consistency checks, not independent external validation.
