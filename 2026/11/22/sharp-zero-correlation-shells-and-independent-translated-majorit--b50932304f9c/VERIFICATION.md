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

The finite test is reproducible by executing `python verify.py` with Python 3. It checks the exact finite overlap sum, the two-step binomial difference and complementary-distance identity for all odd dimensions from 1 through 61. Independent brute-force cube enumeration checks every mask distance through dimension 13. For the four-mask designs it checks all eight patterns of all four triples for dimensions 3, 7, 11 and 15. This execution reported 2,115 passing assertions.

The derivation in RESULT.md is the proof for every odd dimension. The finite tests do not certify infinite generality or historical priority. No independent audit was performed.
