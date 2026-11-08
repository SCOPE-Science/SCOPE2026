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

# Reproduction

Run `python3 verify.py` using Python 3 standard library. Verified output includes `VERIFY_OK`, `local_tests=66 local_domain_elements=377179`, and `global_moduli=300 global_residue_indices=113400`. It compares local histograms exactly, tests least periods by every proper divisor, and confirms all image-cardinality predictions. These finite tests do not prove the formulas for unrestricted moduli; the mathematical proof is in `RESULT.md`. External independent audit has not been performed.
