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

The formula and all-dimensional optimality follow from the written proof in `RESULT.md`, including the exact pair correlation, the explicit expectation correction, the rowwise variance computation, and the cost-matched risk differences. The Python program `verify.py` requires only Python 3 standard-library components (`fractions`, `itertools`, `math`). Execution after extraction of this exact package returned:

```
PASS 1423 exact-rational assertions; n=2..9, fixed-count sign orbits and matched query budgets
```

The finite tests enumerate every fixed-positive-count sign orbit only for dimensions 2 through 9, with a nontrivial rational test matrix and exact mean/variance calculations. They also test even/odd constant-off-diagonal examples and zero-row-sum cost-threshold witnesses. Exhaustive infinite-dimensional verification is neither claimed nor attempted. All matrix--vector arithmetic in the proof is exact; floating-point performance and practical wall time are not evaluated. Literature comparisons remain subject to the residual novelty risks described in the review.
