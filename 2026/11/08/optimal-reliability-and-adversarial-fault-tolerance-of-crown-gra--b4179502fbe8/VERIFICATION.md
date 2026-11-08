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

Run `python3 artifacts/verify.py` using the standard Python 3 library, from the directory containing these files. Expected final output begins `VERIFY_OK`.

The test checks exact Laplacian eigenvectors, eigenspace restriction rank, direct Kalman rank for small cases, rational failure probabilities, all small budget-optimal reliability probabilities, and adversarial failure tolerance. The scientific proof establishes the all-order and all-probability statements independently of finite enumeration.

No third-party mathematical audit or external certification has been performed.
