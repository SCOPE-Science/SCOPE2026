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

## Checks performed

Run `python3 CHECK.py` with Python 3's standard library. The exact-rational determinant routine checks squared intrinsic Euclidean facet measures against the barycentric-gradient formula on 900 rational weight profiles in dimensions 2--5. The program then checks 11 log-product-constrained numerical optimality systems in dimensions 2--12, their reversal symmetry, the strict endpoint inequalities for dimensions at least three, and the analytical dimension-three value. Successful execution ends with `LECTURE_HALL_FIXED_VOLUME_SURFACE_OPTIMIZER_PASS`.

## Proof versus computation

Strict convexity of the exponential Euclidean edge norm, coercivity on the zero-sum log hyperplane, the exact KKT identities and the endpoint comparison establish the theorem for every dimension and all positive weights. Finite numerical optimizers are diagnostics only. The displayed formulas and extremality statements do not rely on numerical global optimization or on floating-point uniqueness tests.

## Limits

The general sharp constant is implicitly characterized, not claimed to have a closed elementary expression. No numerical test certifies absolute historical originality. Independent mathematical verification has not been performed.
