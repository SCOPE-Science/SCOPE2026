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

# Verification

Run `python projection_tv_checker.py` with Python 3 standard library. On the packaged source the checker reported:

```
ALL_EXACT_STEP_VARIATION_BOUNDS_PASS 8205
ALL_EXACT_PIECEWISE_CONSTANT_BV_BOUNDS_PASS 55608
GEOMETRIC_SHARPNESS 1 gain 2.248127808288 limit 2.25
GEOMETRIC_SHARPNESS 2 gain 2.622097846698 limit 2.625
GEOMETRIC_SHARPNESS 3 gain 2.808942813664 limit 2.8125
GEOMETRIC_SHARPNESS 4 gain 2.902295265351 limit 2.90625
GEOMETRIC_SHARPNESS 5 gain 2.948936501526 limit 2.953125
GEOMETRIC_SHARPNESS 6 gain 2.972239637894 limit 2.9765625
GEOMETRIC_SHARPNESS 7 gain 2.983882471771 limit 2.98828125
ALL_CONTINUOUS_LINEAR_SPLINE_BV_TESTS_PASS
```

The direct rational Gram-system solves verify integrals and finite cases. The proof's universal quantification, alternating-tail inequality and limiting sharpness follow from exact analysis; sampling cannot replace those steps. The assessment is same-model only; independent audit has not been performed.
