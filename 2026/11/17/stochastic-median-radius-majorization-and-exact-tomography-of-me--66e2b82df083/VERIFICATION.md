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

The embedded `verify.py` was executed under Python 3 with only standard-library dependencies and returned `STAR_MEDIAN_CHECKS_OK` followed by observed/predicted numerical survival proportions. It checks rational stochastic inequalities across all elementary unequal-length transfers for odd sample sizes \(3,5,7,9\), exact algebraic breakpoint reconstruction including multiplicities, and a seeded Monte Carlo test with \(60{,}000\) five-point stars. The mathematical proof is in RESULT.md; finite tests do not certify universal claims. No independent audit has been performed.
