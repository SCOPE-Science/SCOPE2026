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

The direct enumeration in `verify.py` constructs all distinct legal parent words and their distinct subsequences, rather than relying on the rational-series construction. It tests the parent-count formula for all received words with lengths \(0\) through \(8\) and all deletion counts \(0\) through \(5\), a total of 3,066 independent comparisons, as well as complete parameter-type counts and generating-series coefficients through length \(12\).

The algebraic proof uses canonical greedy embeddings; no finite check is claimed to establish the general theorem. The asymptotic expansion uses the unique positive dominant pole of the rational transfer series for fixed deletion count. These tests do not assess deletion-mask probability weights or optimal error-correcting code sizes. Independent audit has not been performed.
