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

# Verification of the cyclic three-point median Gini formula

Run `python3 check_median_gini.py` using a standard Python 3 interpreter. The program uses exact rational arithmetic and no third-party packages. It enumerates every strict input ordering and every nonempty proper binary cut for cycle sizes three through eight; it then evaluates actual input/output pairs with rational one-coordinate perturbations for sizes four through 110, and checks the universal three-copy cut bound directly for sizes five through 100.

Observed output:

```
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 3 0
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 4 4/3
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 5 3/2
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 6 9/5
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 7 2
EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED 8 15/7
EXHAUSTIVE_PERMUTATIONS_TOTAL 46230
EXPLICIT_TWO_INPUT_SHARP_WITNESSES_PASSED_4_TO_110
EXACT_CAPACITY_CUT_BOUND_PASSED_5_TO_100
ALL_MEDIAN_GINI_CHECKS_PASSED
```

The proof in `RESULT.md` establishes arbitrary dimension using selector linearization, exact coarea reduction, a uniform cut bound, and explicit attainment. These computations corroborate but cannot replace those unrestricted steps. No weighted, iterated, or nonperiodic statement is certified here.
