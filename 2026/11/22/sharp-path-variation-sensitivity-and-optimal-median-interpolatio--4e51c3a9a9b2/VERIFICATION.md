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

# Reproducibility

Use `python3 verify_median_centered_clipping.py`; no external dependencies are required.

Actual execution:

```text
ALL_PIECEWISE_AFFINE_FACE_MASKS_PASS 23
EXACT_STRICT_MEDIAN_RANK_AND_CLIPPING_WITNESSES_PASS 72
RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_STRESS_PASS 1350
MEDIAN_ANCHORED_CLIPPING_ALL_CHECKS_PASS
```

The first check exhausts the finite generic centre-row/cut/mask possibilities for dimensions two through eight over specified interpolation parameters. The second constructs genuine rational data points inside strict median-order and clipping-active-set chambers and verifies that the ratio equals the analytic supremum for sampled dimensions through nineteen. The third compares directly evaluated operators at independent random rational pairs, rather than only inspecting Jacobian expressions. They are supporting finite checks, not a proof of all dimensions. The all-dimensional proof and the sharpness construction appear in `RESULT.md`. No independent mathematical audit has yet been performed.
