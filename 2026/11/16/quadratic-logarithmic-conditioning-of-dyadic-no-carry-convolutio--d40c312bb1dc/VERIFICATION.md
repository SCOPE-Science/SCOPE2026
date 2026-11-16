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

The standalone `check_no_carry.py` can be run as `python3 check_no_carry.py`. It compares direct sums and digit-product evaluations for every frequency through \(n=5\), checks the analytic lower bound throughout that range, and tests the upper-bound witness through \(n=10\). The final PASS marker is reported only upon successful completion.

The computations use floating-point complex arithmetic with stated tolerances; they are not a proof of nonvanishing for all lengths. The analytic argument in RESULT.md proves the infinite claims. The exact minimum at a general fixed length was not computed. Independent validation was not performed.
