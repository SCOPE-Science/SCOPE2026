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

The package contains `artifacts/verify.py`, a standalone standard-library executable. Replaying `python3 artifacts/verify.py` produces the following successful output from actual code:

```text
EXACT_14_SKELETON_SYMBOLIC_REDUCTION_OK skeletons=14 profiles=5
EXACT_SOURCE_LAYER_AND_FIVE_POWER_FORMULA_OK n=0..12
ALL_EDGE_ORIENTATIONS_OK n=0 edges=4 acyclic=14
ALL_EDGE_ORIENTATIONS_OK n=1 edges=8 acyclic=78
ALL_EDGE_ORIENTATIONS_OK n=2 edges=12 acyclic=426
ALL_EDGE_ORIENTATIONS_OK n=3 edges=16 acyclic=2286
ALL_EDGE_ORIENTATIONS_OK n=4 edges=20 acyclic=12090
VERIFY_OK
```

The finite 14-skeleton calculation verifies the symbolic exponential generating-function identity exactly in the polynomial ring with integer coefficients; combined with the source-layer bijection it proves the unrestricted statement. The checks over bounded graph sizes are corroboration and do not independently validate priority or provide an alternative infinite proof. No independent mathematical audit has been performed.
