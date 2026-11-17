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

# Verification performed

The exact-integer checker `check_three_tap.py`, executed with Python 3, returned:

```
ALL_CUTS_EXHAUSTIVE_EXACT_N3_TO_N16_PASSED 131036
EXACT_INTEGER_NONBINARY_INPUTS_PASSED 7650
FOUR_SITE_EXACT_GINI_SIMILARITY_PASSED
DOBRUSHIN_SEPARATION_N6_TO_N99_PASSED
ALL_THREE_TAP_GINI_CHECKS_PASSED
```

The binary checks verify the squared-level-count identity at every cut through sixteen sites, the claimed sharp coefficient and the equality geometry. The nonbinary checks are additional tests, not a substitute for the layer-cake proof in RESULT.md. The unrestricted theorem is established by the exact cut argument and does not depend on a finite-size extrapolation. There has been no independent external validation.
