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

# Verification and reproduction

The proof is in RESULT.md. Run `python3 checks/checker.py` using Python 3 and the standard library. The exact-rational checker tests four strictly positive polynomial weight profiles and five rational grids; it verifies zeroth and first moments, two-point covariance identities, and the exact uniform deficit/equality conditions. It reports `PASS: 1764 exact rational assertions (pair identities, moments, gap and equality).`

These are finite arithmetic checks. The universal inequality and complete uniform extremizer theorem depend on the analytic signed-measure coupling and strict equality analysis, not on sampled verification. The historical-literature comparison does not constitute independent priority verification; the independent audit status above is unperformed.
