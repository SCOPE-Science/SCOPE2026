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

The theorem is established by finite-graph coarea, the piecewise-permutation representation of sorting, and exact two-cut witness construction. It does not rely on a finite search for universal correctness.

The standalone checker `checker.py` uses Python's standard library and exact rational arithmetic. It independently compares cut-profile bounds to induced permutation operator norms, constructs explicit strict-order witness pairs, and checks exact examples. The observed output was:

```
ALL_CONNECTED_SIMPLE_GRAPHS_EXACTLY_CHECKED 43
EXACT_WEIGHTED_GRAPHS_CHECKED 24
PATH_STAR_CYCLE_FORMULAS_PASSED 11
BARBELL_EXACT_QUADRATIC_GROWTH_PASSED 5
ALL_SORTING_GRAPH_BV_TESTS_PASSED
```

The checks enumerate finite cases only; they neither certify all graphs nor settle historical publication priority. A full-text comparison with all older rearrangement literature is not claimed. External mathematical validation is not yet performed.
