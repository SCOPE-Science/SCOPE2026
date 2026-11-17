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

The standalone `check_star_harmonic_gini.py` can be run using standard Python 3; it requires no external packages. Exact rational arithmetic tests all nontrivial binary cuts for four independent probability profiles at each leaf count from one to nine, 3600 rational nonbinary signals, all claimed sharp singleton witnesses, and the minimax and uniform-size inequalities.

Recorded successful terminal output:

```text
EXACT_ALL_BINARY_CUTS_4_PROFILES_PER_DIMENSION_PASSED m=1..9
EXACT_RATIONAL_REAL_INPUT_INEQUALITY_PASSED 3600
EXACT_HUB_HARMONIC_SHARPNESS_AND_MINIMAX_PASSED
EXACT_FIXED_SIZE_AND_GLOBAL_ENVELOPES_PASSED
ALL_WEIGHTED_STAR_HARMONIC_GINI_CHECKS_PASSED
```

The all-real, all-positive-conductance assertion is established by the analytical layer-cake/cut calculation in `RESULT.md`, not finite testing. Exact enumeration is comprehensive only for the expressly listed finite profiles. Independent audit: not performed.
