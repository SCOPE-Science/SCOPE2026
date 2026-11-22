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

## Reproduction

Execute `python3 verify.py coefficients.json`. The script computes exact finite-field polynomial powers and Hasse–Witt ranks from the 215 coefficient strings and independently enumerates all rational projective points over the specified ground field. It asserts all per-field counts, four exceptional entries and no rational points. A successful invocation prints `EXACT_QUARTIC_CARTIER_CENSUS_VERIFIED`. The authoritative source establishes that the 215 inputs are a complete set of isomorphism-class representatives; the certificate does not independently prove that literature theorem. The check was executed from these attached files.
