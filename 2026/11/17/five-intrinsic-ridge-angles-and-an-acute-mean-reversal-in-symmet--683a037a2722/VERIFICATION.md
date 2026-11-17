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

# Verification and reproducibility

Run `python3 check_symmetric_stochastic.py` with Python 3.10 or later; only the standard library is needed. The checker constructs the intrinsic tangent basis independently of the projected-normal derivation, inverts its Gram matrix using exact fractions, checks all five claimed normal-product classes, and explicitly witnesses every codimension-two coordinate intersection in dimensions 3, 4, 5, 6, and 7. It also verifies the exceptional non-ridges for dimension 3.

The observed complete facet-pair counts are: 3: nine ridges out of fifteen pairs; 4: forty-five of forty-five; 5: one hundred five of one hundred five; 6: two hundred ten of two hundred ten; 7: three hundred seventy-eight of three hundred seventy-eight. The final reproducibility marker is `SYMMETRIC_STOCHASTIC_RIDGE_EXACT_PASS`.

The general incidence, angle formulas, strict finite-dimensional mean sign, and limit laws are proved symbolically in `RESULT.md`. Finite enumeration by itself does not certify any statement beyond the tested dimensions. Independent audit was not performed.
