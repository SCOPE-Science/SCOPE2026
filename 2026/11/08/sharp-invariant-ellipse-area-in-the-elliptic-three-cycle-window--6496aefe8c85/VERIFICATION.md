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

Exact algebraic verification: matrix symplecticity and the positive-definite invariant form, both vertical dual norms, sharp radius and area identity are checked with SymPy in `check.py`. A numerical boundary test at five distinct interior parameters checks 10,000 perimeter points (1,000 per orbit per parameter) and verifies that every point follows the prescribed three-branch itinerary and that the third iterate equals the affine return modulo integer translations. Numeric perimeter samples are supporting evidence only; they are not used as a substitute for the Cauchy–Schwarz sharp-radius proof or for universal branch inequalities. No independent audit has been performed.
