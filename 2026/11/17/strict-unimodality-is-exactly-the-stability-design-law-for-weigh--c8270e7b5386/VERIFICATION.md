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

The analytical proof derives the sharp coefficient, the equality constraints, the strict-unimodality criterion, and an explicit inverse construction valid at every finite path size. The exact rational standalone checker `check_projection.py` was executed with Python and produced:

```
EXACT_RATIONAL_ALL_WEIGHT_PATTERNS_PASS 1092 admissible=42 nonadmissible=1050
RANDOM_IRREGULAR_GRID_PROJECTION_AND_SHARP_STEP_PASS 3000
ALL_WEIGHTED_AFFINE_PATH_TESTS_PASS
```

The enumeration used one explicitly irregular integer grid per size from 2 to 7 and edge weights 1,2,3; the random tests used 3,000 seeded rational irregular-grid instances up to ten samples. A finite test is neither a proof of an infinite family nor an exhaustive novelty search. The positivity condition is strictly required. The full original classical regression article was not available for line-by-line priority comparison.
