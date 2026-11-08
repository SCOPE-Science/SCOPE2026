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

# Verification and its limits

Execute `python check.py` with Python 3.9 or later. This is a standalone script using only the standard library. From the exact package version it produced:

```
EXACT_PERMUTATION_FOURTH_MOMENT_IDENTITIES_OK 136
EXACT_BILINEAR_RECTANGLE_DOMINANCE_OK 197
EXACT_TWO_LEVEL_POWER_SUM_EXTREMA_OK 3157
EXACT_ATTAINMENT_AND_FOUR_STATE_TRANSITION_OK
ALL_PERMUTATION_RANK_ONE_MOMENT_CHECKS_OK
```

The test separately evaluates \(\sum_i a_i b_{\pi(i)}\) for each enumerated permutation, normalizes its second and fourth moments with exact rational arithmetic, and compares with the closed formula. Two-level profiles and the proposed boundary regimes receive independent exact checks. The code does not enumerate arbitrary real coefficient vectors, all dimensions, or all possible literature, and is not a certificate of the infinite-dimensional range of the theorem. Those conclusions rely on the written proof; the three-coordinate smoothing lemma and the bilinear corner comparison must be checked analytically. Independent mathematical audit has not been performed.
