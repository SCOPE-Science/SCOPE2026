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

# Verification and limits

Run `python3 verify_derangement_covariance.py`. It directly enumerates all fixed-point-free permutations for orders 4 through 9, compares the exact joint frequencies against the closed formulas, and checks the inclusion-exclusion relations for orders 4 through 80. The checker passed 579 exact assertions. The independent enumeration exercises a separate representation from the analytic counting proof.

No finite check establishes the formulas for all orders. The general proof is the inclusion-exclusion and subfactorial argument in `RESULT.md`. The asymptotic statement uses the classical subfactorial limit. No independent external review has been performed.
