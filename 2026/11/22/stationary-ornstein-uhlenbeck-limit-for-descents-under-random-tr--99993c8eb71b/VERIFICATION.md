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

# Verification record

Run `python3 checker.py` from the extracted package directory. The checker uses only Python's standard library, enumerates all permutations for sizes \(3\) through \(7\), and checks the pointwise cyclic eigenfunction identity, static variances, stationary lag-one covariances and mean square increments using exact rational arithmetic.

Observed output: `PASS: 5936 exact tests; all permutations n=3,...,7`.

The computation is finite; the uniform bracket concentration, martingale limit and path-space convergence are proved mathematically in RESULT.md rather than asserted from enumeration. Independent audit has not been performed.
