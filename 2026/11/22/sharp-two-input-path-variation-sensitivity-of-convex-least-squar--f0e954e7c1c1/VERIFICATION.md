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

# Reproducible verification

The standalone `verify_convex_bv.py` program uses only Python standard-library exact rational arithmetic (`fractions.Fraction`). Reproduce with `python3 verify_convex_bv.py` (Python 3.9+). It enumerates all 127 active sets for \(2\le n\le8\), directly constructs each Gram inverse and face projector, checks projector idempotence and constant preservation, calculates all sharp input-step columns and tests strict KKT primal/dual certificates at finite input distances. The following assertions completed in the present verification:

```
N 2 SHARP 1 ACTIVE - STEP 1 PASS
N 3 SHARP 1 ACTIVE - STEP 1 PASS
N 4 SHARP 6/5 ACTIVE 1,2 STEP 2 PASS
N 5 SHARP 4/3 ACTIVE 2 STEP 2 PASS
N 6 SHARP 7/5 ACTIVE 2,3 STEP 2 PASS
N 7 SHARP 28/19 ACTIVE 1,3,4 STEP 3 PASS
N 8 SHARP 11/7 ACTIVE 2,3,4,5 STEP 4 PASS
ALL_127_ACTIVE_FACES_AND_EXACT_WITNESSES_PASS
FIRST_EXPANSIVE_DIMENSION_FOUR_PASS
ABOVE_AFFINE_FACE_FACTOR_THREE_HALVES_AT_EIGHT_PASS
```

The finite computation does not prove the claim for an infinite sequence of dimensions. The all-dimensional active-face formula and monotonicity are proved analytically in `RESULT.md`. No independent external validation has been performed.
