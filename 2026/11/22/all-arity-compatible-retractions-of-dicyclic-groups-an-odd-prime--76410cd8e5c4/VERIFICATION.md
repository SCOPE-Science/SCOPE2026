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
Run `python3 verify.py` using Python 3 and the standard library. The script enumerates all homomorphisms of the dicyclic presentations for sixteen explicit integer parameters and checks every idempotent, image order and the two-generator composition congruence. It additionally compares selected ordered commuting-triple counts and reduced graph diameters. Successful output ends with `DICYCLIC_RETRACTION_COMPATIBILITY_VERIFIED`.

The general formulas are proven by the conjugation argument, CRT classification, and coordinatewise compatibility count in `RESULT.md`; finite enumeration is not an exhaustive infinite proof. The primary 2023 dicyclic descending-endomorphism article supplies previously known generator-image forms, but its graph has elements rather than operators as vertices. Complete historical priority and independent validation are unperformed.
