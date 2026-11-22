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

# Reproducibility and verification

The complete proof, including the exact support identity, piecewise integral calculations, and positivity of the quadratic coefficient for every positive aspect ratio, appears in RESULT.md.

To reproduce the numerical checks with Python 3 and the standard library, run:

```
python3 verify_width.py
```

The observed output on replay was:

```
ALL_CHECKS_PASSED: 203 numerical regressions
```

The checker obtains directional widths directly from extrema of the four vertex projections, independently integrates on positive and negative angular quadrants, and compares with the explicit base and kite moment expressions and the coupled two-skew expansion. It also checks sample strict local decreases. These checks use finite resolution and sample values; they do not establish the universal quantifiers, the non-smooth cubic form, or the fourth-order error bound without the analytic arguments.

The equality of both diagonal lengths and area follows immediately from the vertex coordinates. The independent mathematical audit remains unperformed.
