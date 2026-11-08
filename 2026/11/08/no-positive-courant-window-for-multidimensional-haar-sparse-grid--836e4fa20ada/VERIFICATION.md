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

# Verification and limits

The fully stated theorem is proved analytically in RESULT.md. Running `python3 verify.py` with Python 3 and its standard library yields the final line `VERIFY_OK: independent exact rational projection and boundary certificates`.

The verifier constructs one-dimensional dyadic level projectors and combines them into the total-level tensor projector, rather than using the displayed closed form for the projected jump. It checks exact rational identities in dimensions two and three, multiple levels, and the one-level positivity boundary. Finite checks support implementation and normalization but are not substitutes for the all-level symbolic argument.

The bibliographic comparison does not constitute independent verification of priority. Independent mathematical audit: not yet performed.
