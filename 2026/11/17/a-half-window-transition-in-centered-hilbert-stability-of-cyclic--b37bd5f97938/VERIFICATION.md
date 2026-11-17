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

# Computational checks and limits

The standalone `verify_hilbert.py` uses exact rational arithmetic, no external dependencies, and a fixed seed for randomized rational test inputs. Execute `python verify_hilbert.py` from a directory containing that file.

Verified diagnostic lines:

```
EXACT_CHAMBER_TWO_SITE_DIRECTION_TESTS 812314
EXACT_ARBITRARY_INPUT_PAIR_TESTS 5292
EXACT_ATTAINED_TWO_PEAK_WITNESSES 171
ALL_CYCLIC_MAX_CENTERED_HILBERT_CHECKS_PASSED
```

The chamber test enumerates all strict coordinate orders for dimensions two through seven and all window widths, checking two-site directions, not every real perturbation. The rational test samples finite input pairs for dimensions two through nineteen. The two-peak witnesses attain the asserted sharp squared constant for every nonconstant case in those dimensions. Analytic inequalities and explicit constructions in `RESULT.md` prove the unrestricted all-dimension statement. Independent mathematical audit has not been performed.
