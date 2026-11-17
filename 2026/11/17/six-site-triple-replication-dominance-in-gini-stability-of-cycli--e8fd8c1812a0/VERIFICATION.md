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

The included `verify.py` runs with Python 3 and the standard library only. Execute `python3 verify.py` after extracting this file beside the present Markdown.

Observed exact-rational output:

```
ALL_ORDER_CHAMBERS_EXACT_CUT_NORMS_PASSED 46232
MULTIPLICITY_CUT_GRID_PASSED 1810900
ARBITRARILY_CLOSE_SHARP_WITNESSES_PASSED 198
EXACT_ARBITRARY_TWO_INPUT_DIAGNOSTICS_PASSED 4350
ALL_CYCLIC_OPENING_GINI_CHECKS_PASSED
```

The checker evaluates actual min/max outputs, the exact Gini seminorm, cut ratios of all strictly ordered selector chambers through size eight, integer parameter bounds through dimension two hundred, and local attaining input pairs in dimensions three through two hundred. It also validates 4,350 arbitrary rational two-input inequalities. Its finite scope does not certify the universal theorem: the written proof supplies the all-dimension argument, especially the two-case multiplicity cut bound and explicit construction.

There is no independent scientific audit or third-party validation in this package.
