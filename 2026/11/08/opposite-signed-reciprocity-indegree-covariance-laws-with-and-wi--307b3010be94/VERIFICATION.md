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

# Reproducible finite checks

Run `python3 verify.py` using the Python standard library. It enumerates all independent outgoing-subset configurations at labeled orders 3–5 for each eligible small outdegree, computes the reciprocity count and full indegree histogram, and compares every exact rational covariance coefficient against the closed-form binomial second-difference formula. Expected result: 17 test configurations, 86 coefficient comparisons, all PASS.

The proof in RESULT.md handles all valid orders and outdegrees; finite enumerations do not establish generality by themselves. The fixed-outdegree limit is a coefficientwise binomial-to-Poisson argument. There is no independently performed scientific audit.
