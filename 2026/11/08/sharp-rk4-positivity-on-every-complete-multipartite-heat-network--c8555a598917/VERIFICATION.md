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

The theorem is proved analytically for all part sizes and all nonnegative timesteps using a complete Laplacian projector decomposition, sign-discriminant analysis and a cubic monotonicity argument. The full proof is in RESULT.md.

The included Python 3 script `verify.py` reconstructs the graph Laplacian and its RK4 polynomial independently using standard-library exact rational arithmetic; for every partition of \(N=2,\ldots,9\), at nine rational steps, it checks every matrix entry against the closed form, checks stochastic row sums and verifies the positivity criterion. It separately confirms the quadratic discriminant for integer \(2\le N<300\) and brackets the cubic cutoff rationally. Extract and run `python3 verify.py`. Its reported result was `VERIFY_OK assertions=96054 numerical_domain=partitions_of_2_to_9 exact_fractions=True`.

The finite checks cannot establish the infinite statement, infer priority, or replace the proof. Unequal graph weights, disconnected graphs, different RK schemes and individual internal stage values are outside the theorem. Independent scientific audit is not performed.
