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

Reproduce the finite checks with `python3 verify.py` in the directory containing the standalone script. Exact Python fractions are used for the run/gap coefficients. The program verifies formula-vs-subset profile agreement for even sizes 4 through 14; rank spectra through size 16; low-rank and near-full-rank formulas; and actual partial-map membership by direct order-relation tests for sizes 4, 6, and 8. Its successful last line is `VERIFY_OK`.

The infinite exact formula is proved by the path-type classification and marked clockwise run/gap decomposition in RESULT.md. The logarithmic limits use a factorial sandwich and an automorphism-restriction bound. Finite enumeration does not independently prove either unrestricted statement. Independent mathematical audit has not been performed.
