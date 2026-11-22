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

# Verification of the periodic quadratic-spline theorem

The statement is proved analytically in RESULT.md. For a reproducible exact-arithmetic check, place `check_periodic_quadratic.py` beside this file and run:

```sh
python3 check_periodic_quadratic.py
```

Observed on this package's source file:

```
EXACT_ODD_CYCLE_PAIR_TRANSPORT_AND_EXTREMIZERS_PASS 11900
EXACT_RATIONAL_RANDOM_DATA_BV_BOUND_PASS 1800
EVEN_CYCLE_COMPATIBILITY_AND_NULL_SPLINE_PASS
ALL_PERIODIC_QUADRATIC_VARIATION_CERTIFICATES_PASS
```

For odd n between three and 41 inclusive, all ordered elementary cyclic difference pairs are tested with exact rational integration of the absolute affine derivative on each cell. A further 1,800 deterministic rational-data examples test the predicted norm bound. For even n from four through 64, the compatibility obstruction, explicit nonzero zero-data spline and a compatible nonconstant datum are checked. The exact computations do not establish the universal quantifier, which instead follows from the cyclic-shift inverse, elementary two-edge bound and transport decomposition in the proof. A standalone verifier and all six descriptive files are included in the same record. No external independent audit has occurred.
