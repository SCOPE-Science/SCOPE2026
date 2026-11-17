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

# Reproducible mathematical verification

Run `python3 verify_quadratic_bv.py` in a directory containing the standalone script. The script relies only on the Python standard library and uses rational arithmetic throughout.

The checks were successfully executed on the packaged script, producing the following scientific test summaries:

```
CARDINAL_SPLINE_DERIVATIVE_AND_MOMENTS_PASS 71
EXACT_STEP_FORMULAS_AND_QUADRATIC_REPRODUCTION_PASS 14/11
EXACT_MULTI_JUMP_BV_BOUND_PASS 960
TRANSLATION_INVARIANT_SHARPNESS_PASS 18
ALL_QUADRATIC_QUASI_INTERPOLANT_TESTS_PASS
```

These tests verify spline derivatives and moments at 71 rational positions, exact triangular variation at six strengths, random finite multi-jump inequalities in four regimes, and translated sharpness witnesses. The general sharp theorem does **not** follow from the finite tests; it follows from exact piecewise-linear integration and the absolutely summable-jump representation in RESULT.md. The test cases do not cover negative correction parameters, boundary-modified splines, or nonuniform samples.
