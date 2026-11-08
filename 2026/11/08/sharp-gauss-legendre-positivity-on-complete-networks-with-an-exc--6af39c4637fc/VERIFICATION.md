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

Run `python3 verify.py` using Python's standard library. The script independently builds weighted Laplacians and the rational matrix map with exact fractions, compares it with the spectral projector formula, checks row sums, verifies the closed exceptional-edge numerator identity and coefficient threshold for a range of integer sizes, and exercises the two-vertex exception. A passing run prints `VERIFY_OK`. All tests use exact rational arithmetic; the unrestricted theorem rests on the projector derivation and polynomial signs in RESULT.md. Independent mathematical validation has not been performed.
