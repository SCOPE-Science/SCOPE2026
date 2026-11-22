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

Execute `python3 verify_inverse_frontier.py` with Python 3. The deterministic exact-fraction test reports `VERIFY_OK 1734`: 1,729 sampled exact-rational identities/inequalities and five fixed exact sample checks. The checker's parameter and angle samples are finite and are not a proof of uniformity; the exact analytic minimization in RESULT.md is the infinite-domain proof. The inverse sensitivity refers to the Euclidean operator norm of the local tangent inverse and not an end-to-end solver guarantee.
