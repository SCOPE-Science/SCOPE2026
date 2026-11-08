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

# Verification notes

The exact covariance recursion is checked independently against exhaustive rational enumerations of joint root degree and total leaves for six attachment offsets through size \(11\). Each distributional probability is summed over the four possible combinatorial transitions, including the initial vertex being a leaf. Every tested state verifies that the probabilities are nonnegative and sum to one by the subsequent equalities of moments. Direct computed covariance is compared to the deterministic recurrence, while the two exact mean identities are also checked.

The same verifier iterates the analytical moment recurrences through size \(100000\) for six floating attachment offsets. The ratios approach the predicted limits with offsets near the lower boundary converging more slowly. These checks are finite; the infinite result follows from the exact analytical recurrence, gamma products, and summability argument in RESULT.md.

Reproduce with `python3 check_covariance.py`. A successful run finishes with `ALL CHECKS PASS`. No external packages or internet access are required. The verifier does not establish originality or an independent mathematical audit.
