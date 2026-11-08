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

# Reproducible checks and boundaries

Run `python3 verify_squares.py` using the Python standard library. The direct checker enumerates all contiguous substrings and explicitly compares equal adjacent halves; it stores complete square strings to remove duplicate occurrences. For all 31,465 words of length 3 through 30 containing three ones, its result agrees with the independent gap formula. An additional 240 deterministic long gap tuples were also checked.

The generating-function checker derives coefficients by finite sums of geometric-series coefficients and matches all formula totals for zero-count indices 0 through 50. Its initial totals are 1, 4, 17, 42, 89, 160, 270, 432, 663, 966, 1368, 1880. Actual output:

```
DIRECT_SQUARES_OK 31465
LONG_RANDOM_OK 240
GENERATING_FUNCTION_OK 0..50
INITIAL_TOTALS [1, 4, 17, 42, 89, 160, 270, 432, 663, 966, 1368, 1880]
```

This code is a finite regression test, not an exhaustive computation for all lengths. The infinite proof is the combinatorial decomposition into zero-one and two-one squares, its overlap correction, and exact free-parameter generating functions in `RESULT.md`. The leading constant follows from pole order five, and the limiting law from weak-composition convergence and homogeneous scaling. No machine proof or external certification is claimed. Independent audit has not been performed.
