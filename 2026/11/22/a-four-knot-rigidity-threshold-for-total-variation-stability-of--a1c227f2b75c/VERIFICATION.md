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

# Verification

The `verify_convex_bv.py` script requires only Python 3 and the standard library. The proof is analytical and finite arithmetic is supplementary. An executed replay reported:

```text
THREE_KNOT_EXACT_WEIGHTED_FORMULA_PASS 1600
FOUR_KNOT_ALL_ACTIVE_FACES_EXACT_PASS 4
FOUR_KNOT_ATTAINED_SHARP_SIX_FIFTHS_PASS
ARBITRARY_MESH_MASS_ALL_AFFINE_FACE_SHARPNESS_PASS 150
EXACT_BALANCED_JUMP_LOWER_BOUND_PASS 37
ALL_CONVEX_REGRESSION_BV_CHECKS_PASS
```

The three-site tests cover 1,600 positive rational masses/spacing combinations; the four-site test exhausts all four local active subsets rather than all possible real data, which are handled by the piecewise-linear segment proof. The irregular-grid tests generate strictly positive rational observation masses and strictly increasing rational knot sequences. The KKT witness construction explicitly ensures positive active multipliers and evaluates the projected step-response gain. The uniform-grid check confirms the exact binomial/centroid identity through 39 sites. The exact counts are not a claim of exhaustive all-parameter computational verification, nor an independent audit. The continuous all-n theorem follows from the proof in RESULT.md.
