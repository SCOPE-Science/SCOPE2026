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

# Verification of the localized two-in-three deletion sphere law

Run `python checker.py` using Python 3 with its standard library. The script independently enumerates actual deletion outputs for each word, calculates the triple-statistic formula, builds the entire finite distribution by an ordered-pair transfer recurrence, and compares exact rational moments and all extrema. It contains no external input dependencies.

Actual replay result:

```
PASS direct comparisons: 144555; exact distribution/moment/extremum profiles: 27
```

The checks cover binary lengths 3 through 12; ternary lengths 3 through 9; four-symbol lengths 3 through 8; and five-symbol lengths 3 through 6. Exhaustive enumeration is only for these finite cases. The all-length combinatorial identity is proved by the two deletion-output families in `RESULT.md`; the limiting Gaussian law uses bounded two-dependence and independent-block Lindeberg, not computational extrapolation. No independent audit is claimed.
