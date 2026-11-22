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

The result is supported by an analytical reduction to unit jumps, exact integration of degree-two B-splines, and a signed-residual equality argument. The standard-library checker `check_quadratic_schoenberg.py` independently constructs clamped B-splines by the rational Cox–de Boor recurrence and integrates the degree-two step responses exactly on knot and jump intervals. Run `python3 check_quadratic_schoenberg.py`.

Observed output:

```
EXACT_RATIONAL_STEP_BOUNDS_PASS 1710
EXACT_INTERIOR_QUADRATIC_RESPONSE_PASS
EXACT_EXTREMAL_NODES_AND_AFFINE_REPRODUCTION_PASS 20
QUADRATIC_SCHOENBERG_BV_L1_CHECKS_PASS
```

The verification evaluates finitely many rational sites and twenty mesh sizes; it is not an exhaustive or infinite-dimensional certificate. The unbounded family and complete equality classification are established by the explicit polynomial identities and the variation-measure argument in `RESULT.md`. The right-continuous representative convention is essential for pointwise sampled operators. Historical-priority comparisons are self-review only; independent audit is not yet performed.
