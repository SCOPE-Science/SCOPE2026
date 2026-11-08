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

# Reproducibility

Extract `verify.py` and run `python3 verify.py` using Python 3 and the standard library only. It compares the exact binomial recurrence for Fubini numbers against Stirling-number sums for the first 30 nonzero indices; computes every adjacent gap residue modulo \(2^k\) for \(7\le k\le15\); exhaustively verifies 45 full blocks covering 5,110 residue observations; checks 6,232 exact scaled-isometry cases and 360 series comparisons; and tests selected higher-precision branch identities modulo \(2^{17}\), \(2^{19}\), and \(2^{23}\).

Successful output:

```
VERIFY_OK levels=7..15 gap_image=PASS sharp_start=PASS least_period=PASS
complete_blocks= 45 residue_cells= 5110 scaled_isometry_pairs= 6232 series_cases= 360
independent_stirling_rows=1..30 exact_integer_recurrence=0..130 extra_precision=17,19,23
```

The code performs finite consistency checks only. For every precision, the proof rests on two-adic series (1), exact interpolation error (6), unique lowest-valuation term (9), and the resulting bijections, not on computation beyond a fixed cutoff. Independent mathematical audit has not been performed.
