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
# Verification scope
Run `python3 check_ridge_angles.py` with standard Python 3. The checker independently enumerates stable sets for every cycle order from four through thirteen, forms the specified facet normals and bounds, computes every pair's tight vertex set, determines its affine dimension with exact rational elimination, and checks the predicted ridge types and exact outward-normal dot products.

Expected terminal marker: `CYCLE_STAB_RIDGE_ANGLE_PASS  n=4..13  exact_rank_and_normal_products`.

The odd orders five, seven, nine, eleven, and thirteen directly exercise the theorem. The even orders are auxiliary comparator checks only; they are not part of the claimed result. Exact finite rank computations cannot prove the asserted formulas for unbounded cycle order. The analytical proof establishes the complete facet list and the ridge classification in all specified orders. No independent audit has occurred.
