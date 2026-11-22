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

# Reproducible verification

Execute `python3 verify_minmod_bv.py` with Python 3. The standalone checker imports only `fractions` and `random`. It calculates the variation of each piecewise-affine reconstruction as the sum of exact within-cell absolute slopes and exact discontinuity sizes, not merely a variation proxy on sampled cell centers.

Checks previously executed and passed:

```
EXACT_ALL_DIMENSION_EXPLICIT_ATTAINING_PAIRS_PASS 145
EXACT_SECANT_STEP_COLUMN_IDENTITY_PASS 125
RANDOM_RATIONAL_ONE_INPUT_ISOMETRY_AND_TWO_INPUT_BOUND_PASS 22000
EXACT_NEGATIVE_SLOPE_SYMMETRIC_WITNESSES_PASS
ALL_MINMOD_RECONSTRUCTION_BV_CHECKS_PASS
```

The exact 22,000 seeded rational trials use dimensions two through twelve; the 145 witness tests use dimensions two through thirty and five rational slope scales. The three-way derivative selector identity and step decomposition in RESULT.md establish the bound for all dimensions and real inputs. Finite checks do not establish infinite validity by themselves, and historical originality is not independently certified.
