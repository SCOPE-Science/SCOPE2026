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

# Verification
The exact proof uses the exterior powers of a finite weighted Fourier matrix and the second and fourth frequency moments. `check.py` separately constructs weighted Gram matrices at high precision, compares their smallest eigenvalue square roots with the predicted asymptotic, and checks the explicit integer-aperture moment identity. The observed result was `APODIZED_CLUSTER_CHECKS_PASS 186`. These finite checks do not constitute independent validation or prove the limit. The general assertion is conditional on normalized positive reflection-symmetric weights with positive variance of squared frequencies.
