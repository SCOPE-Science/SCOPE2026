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

Run `python verify.py` in a Python 3 environment with NumPy installed. The verifier constructs the graphs from their defining vertex sets, enumerates connected initial subsets directly, simulates the color-change rule, and compares coefficients with the proved generating-polynomial formula for 32 small cases. It then numerically approximates all roots of 240 parameter polynomials and compares the number of open-right-half-plane and negative-real roots with the theorem.

Observed replay:

```
EXHAUSTIVE_BROOM_POLYNOMIALS 32
NUMERICAL_ROOT_CENSUS 240 h=1..24 r=3..12
RIGHT_HALF_PLANE_EXAMPLES [(1, 0), (2, 0), (3, 0), (4, 2), (5, 2), (6, 2), (7, 2), (8, 4), (9, 4), (10, 4), (11, 4), (12, 6)]
DOUBLE_NEGATIVE_ROOT h=2 r=4 root=-2
VERIFY_OK
```

The numerical tolerances are not a rigorous infinite or exact complex-root certificate. The independent logical proof is the no-imaginary-crossing homotopy and real-variable maximum argument in RESULT.md. The source polynomial itself is known from earlier literature, which is credited.
