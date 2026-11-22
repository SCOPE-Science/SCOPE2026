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

Execute `python3 verify.py` with Python 3 and its standard library. The checker independently builds the original blank-swap graph by breadth-first search, constructs the predicted component subdivision by distinct petal-loop rotations, compares every vertex and edge, and evaluates two different integer Kirchhoff cofactor counts. It checks the core conductances exactly by clearing the least common multiple of the petal lengths and uses exact-division Bareiss elimination. The sample parameter tuples are `(3,3)`, `(3,4)`, `(4,3)`, `(4,4)` and `(3,3,3)`.

Observed exact output:

```
EXACT_COMPONENT_AND_MATRIX_TREE_PASS (3, 3) components 6 vertices 20 edges 24 trees 7776
EXACT_COMPONENT_AND_MATRIX_TREE_PASS (3, 4) components 20 vertices 36 edges 42 trees 1620000
EXACT_COMPONENT_AND_MATRIX_TREE_PASS (4, 3) components 20 vertices 36 edges 42 trees 1620000
EXACT_COMPONENT_AND_MATRIX_TREE_PASS (4, 4) components 80 vertices 63 edges 72 trees 12230590464
EXACT_COMPONENT_AND_MATRIX_TREE_PASS (3, 3, 3) components 90 vertices 56 edges 72 trees 6347497291776
VERIFY_OK
```

All general statements rely on the proof in `RESULT.md`; the finite computations support reproducibility, not completeness for all parameters. No independent mathematical audit has been performed.
