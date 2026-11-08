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

The included `verify.py` uses Python standard-library exact fractions to compare the reflection-principle finite-lag formula against the formal generating-function inversion at 17 consecutive lags for six rational parameter values. It independently tests the stationary dyadic conditional moment, checks published exact lag-one and lag-two identities, and verifies high-lag amplitude ratios on both sides of the spectral collision. The finite tests cannot certify the asymptotic law or the claim of originality; these depend on the analytic singularity argument and literature comparison in `RESULT.md`. No independent audit was performed.
