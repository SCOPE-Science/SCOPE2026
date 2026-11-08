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

The self-contained Python 3 program `verify_circle.py` enumerates all point supports of size one, two, and three for the field orders listed in `RESULT.md`. It builds the dual center-incidence bitsets, tests all binary traces for each support, and compares against the claimed coefficients. Its field-of-nine multiplication is explicit rather than relying on an external package. Every nonzero radius is checked for field orders 3, 5, 7 and 9, while radius one is checked for orders 11 and 13. Execute:

```
python3 verify_circle.py
```

Expected final marker: `FINITE_FIELD_UNIT_CIRCLE_SHATTER_PASS`.

The verifier does not enumerate all support sizes at large field orders. Instead, the written uniqueness-of-three-points argument proves that no four-point support is shattered; downward closure settles larger supports. The verifier checks finite examples; no probabilistic extrapolation or independent audit is claimed.
