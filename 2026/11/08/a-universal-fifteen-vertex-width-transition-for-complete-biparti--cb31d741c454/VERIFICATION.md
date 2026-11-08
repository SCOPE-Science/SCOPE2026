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

# Verification of the width transition

The executable `verify.py` uses Python's arbitrary-precision integers to compare every squared cut width without floating-point rounding for all \(2\le p\le q\) and \(p+q\le127\). Its complete iteration ranges are visible in the code and it asserts equality of the entire expected minimizer set rather than checking only one proposed cut. In addition, 1,438 independently generated small-board tube/cut pairs verify the tube-count identity directly.

Observed replay:

`BICLIQUE_ASSOCIAHEDRON_WIDTH_CHECKS_PASSED finite_profiles=3906 exact_cut_profiles=5870718 exact_cross_comparisons=5866812 independent_tube_cut_tests=1438 bound_checks=3`

The proof in `RESULT.md` separately establishes the infinite range \(n\ge128\); no finite simulation is used to infer that range. The displayed tail inequalities hold strictly at the boundary and monotonically beyond it. Historical priority remains provisional, and this package has not been independently audited.
