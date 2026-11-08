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

# Reproduction and boundaries

Use Python 3.10+ with the dependencies in `requirements.txt`, then execute `python verify_cube_cone.py`. The script independently integrates the piecewise polynomial Irwin--Hall density, splitting each cell at any absolute-value sign change, and compares the result to exact closed truncated-power sums. It tests cube dimensions 2 through 10 with exact rational arithmetic; radial covariance identities are checked in dimensions 2 through 24; a further exact finite survey covers dimensions 2 through 38.

The executed checker reports:

```
INDEPENDENT_EXACT_IRWIN_HALL_INTEGRALS_OK 9
EXACT_COVARIANCE_AND_RADIAL_MOMENT_IDENTITIES_OK 23
EXACT_STRICT_COMPARISONS_AND_ASYMPTOTIC_SANITY_OK 37
ALL_CONE_CUBE_AFFINE_PROJECTION_CHECKS_OK
```

The rigorous universal convex-body inequality is proved by the radial probability disintegration, covariance-reproducing kernels, Jensen's inequality and strictness from a support functional. The exact cube kernel formula, strict vertex maximizers and asymptotic scaled gap are proved in `RESULT.md`. Finite calculations do not certify claims for all dimensions or all convex bodies. No independent external scientific audit has been performed.
