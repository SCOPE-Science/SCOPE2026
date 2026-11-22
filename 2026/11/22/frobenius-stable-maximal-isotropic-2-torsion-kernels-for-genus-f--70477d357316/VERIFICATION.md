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

# Verification record

The standalone standard-library script `verify_genus4_lagrangians.py` was executed successfully. It uses independent extension and reduced-row-echelon constructions and verifies equality of the entire 2295-element sets, all 42 fixed-count pairs, and relabelled conjugates. The mathematical proof that this finite test covers all odd finite fields is included in `RESULT.md`.

Run: `python3 verify_genus4_lagrangians.py`.

Expected terminal line: `GENUS4_HYPERELLIPTIC_2295_LAGRANGIAN_42_FROBENIUS_TYPES_VERIFIED_OK`.

The program verifies finite symplectic-module calculations, not historical priority, the existence of curves with every splitting type over each field, or the geometric nature of isogenous quotients. Independent scientific assessment has not been performed.
