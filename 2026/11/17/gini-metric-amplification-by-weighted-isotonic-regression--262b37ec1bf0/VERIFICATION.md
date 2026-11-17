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

# Verification and reproducibility

Run `python verify_weighted_isotonic_gini.py` with Python 3.10 or later. No optional libraries or external data are required.

The executed standard-library exact-rational diagnostics printed:

```text
EXACT_ALL_PARTITIONS_AND_BINARY_CUTS_PASSED 36
EXACT_FOUR_SITE_MASS_RATIO_FORMULA_PASSED 256
EXACT_DOMINANT_MASS_SHARP_ENVELOPE_WITNESSES_PASSED 36
INDEPENDENT_EXACT_PAV_TWO_INPUT_WITNESSES_PASSED 10
ALL_WEIGHTED_ISOTONIC_GINI_DIAGNOSTICS_PASSED
```

The first check directly computes all consecutive-block branch matrices and every nontrivial binary cut for selected dimensions two through seven, comparing their rational ratios against the sharp dimension envelope. The second enumerates all 256 positive-integer quadruples drawn from a four-value grid. The third checks the explicit dominant-mass witness and its exact deficit through dimension 15. The fourth independently implements rational PAV and checks local two-input perturbations on dimensions four through eight.

These are finite computations. The unrestricted assertions about arbitrary dimension, real positive masses, all input pairs, and strict nonattainment are established by the mathematical proof in RESULT.md, not certified by experimental extrapolation. Independent mathematical audit has not been performed.
