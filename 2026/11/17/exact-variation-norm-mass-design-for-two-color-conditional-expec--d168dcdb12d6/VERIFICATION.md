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

# Reproducible finite checks

Run `python check.py` using Python 3 and its standard library. The deterministic program checks, with exact rational arithmetic, the signed-prefix formula against direct single-jump responses; positivity of explicitly constructed norm-one masses; and sharp approach to the unattained weight-ratio envelope. The tested set contains every binary word with 2 through 10 vertices, modulo exchanging color names, under both uniform and seeded heterogeneous positive edge and mass profiles.

Expected final lines:

```text
EXACT_WEIGHTED_STEP_DUAL_TESTS_PASS 2026
EVERY_WORD_POSITIVE_MASS_ONE_NORM_DESIGN_PASS 2026
SHARP_WEIGHTED_SUPREMUM_APPROACH_PASS 2026
ALL_WEIGHTED_PATH_TWO_COLOR_CHECKS_PASS
```

The proof is in RESULT.md; the finite checker does not constitute an infinite or independent certificate. No independent audit has been performed.
