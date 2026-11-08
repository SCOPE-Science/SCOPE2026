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

# Verification details

The analytic proof is given in `RESULT.md`. It derives stationary moment identities directly from the generator, integrates the two-component conditional covariance evolution, and analyzes the exact Prony determinant across distinct modes, confluent modes, and a cancelled mode. The hard special case has an explicit all-rational parameter witness.

With Python 3, NumPy and SciPy available, executing `python check.py` produced the following observed output:

```text
PASS: 1409 exact/rational/numerical checks
```

The checker covers a rational parameter grid, the derivative recurrence, rate recovery, a single-exponential cancellation witness, a repeated-eigenvalue witness, and finite-generator/matrix-exponential comparisons. It evaluates the formulas numerically as well as through exact fractions. No numerical grid can replace the proof of injectivity for the full positive parameter region. There is no independent scientific audit and no empirical/noisy-observation validation.
