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

# Reproducibility

Run `python3 verify.py` using only the Python standard library. It checks exact rational budget, eigenvector and Rayleigh identities for 108 cases, verifies the spectral value for 120 independently generated floating-point cases, and compares 1,440 feasible asymmetric competitors. Expected output:

`VERIFY_OK exact_certificates=108 eigenvalue_instances=120 asymmetric_competitors=1440`

The mathematical proof uses a centered Rayleigh certificate, reflection-sector spectral comparison, a ground-state identity, and equality-forced edge uniqueness. The finite tests do not certify the universal quantifiers. No external independent review has been carried out.
