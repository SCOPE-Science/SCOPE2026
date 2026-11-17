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

# Direct verification and proof limits

The attached `check_fiber_law.py` recomputes the image of each full third-coordinate interval under all \(3^n\) ternary branch sequences for \(0\le n\le9\), using exact rational arithmetic. For every sequence it compares the resulting interval length with the reflected-walk formula \(2^{S_n-M_n}\). It independently counts saturation events and verifies the exact weighted-ballot sum at every tested length. It also counts the nonpositive balanced ternary blocks for \(1\le m\le6\), checking the weighted Catalan factors and the stated dimension constant.

The checker outputs `HETEROCHAOS_SATURATION_BALLOT_DIMENSION_CHECK_OK` on success. Its numerical dimension and asymptotic-constant output is descriptive; the analytical proofs in `RESULT.md` establish the all-time and infinite-set results. Finite enumeration neither proves all lengths nor a Hausdorff-dimension identity.

Scientific uncertainties: previously published exact formulas for this specialized full-leaf observable may exist outside the inspected literature; no independent mathematical audit has been performed. The conclusions depend on the precise affine branch convention away from boundary fibers. No third-party full article is reproduced here.
