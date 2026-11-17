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

The exact-rational standalone verifier is `check_gini_cesaro.py` (Python 3 standard library only). Execute `python3 check_gini_cesaro.py`.

The run checks all 494 nonempty proper cuts for each small dimension \(2\le n\le8\) in aggregate, the 17 rational positive base values \(F(2k,k)\) for \(5\le k\le21\), and the three positive anchor values \(F(9,2)\), \(F(9,3)\), and \(F(9,4)\). It also independently verifies column formulas, strict first-difference identities on a bounded grid, and 6,000 signed-signal inequalities. The resulting log is:

```
ALL_SMALL_CUTS_EXHAUSTIVELY_VERIFIED 494 {2: '1/2', 3: '2/3', 4: '29/36', 5: '37/40', 6: '103/100', 7: '118/105', 8: '2369/1960'}
EXACT_DIAGONAL_HARMONIC_BASE_CASES_VERIFIED 17 minimum (5, Fraction(235, 2268))
EXACT_LOW_K_ANCHORS_AT_NINE_VERIFIED
COLUMN_MONOTONICITY_SUM_IDENTITIES_AND_DIFFERENCE_GRID_VERIFIED
INDEPENDENT_SIGNED_SIGNAL_DIAGNOSTICS_VERIFIED 6000
FIRST_SPIKE_ATTAINMENT_VERIFIED_FOR_ALL_SMALL_DIMENSIONS
ALL_FINITE_CESARO_GINI_CHECKS_PASSED
```

The all-dimension claims are proved by the cut decomposition, harmonic first-difference monotonicity, and explicit logarithmic lower bound in RESULT.md; the finite checks do not by themselves establish those claims. Independent audit has not been performed.
