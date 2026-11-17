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

# Reproducible checks and their limits

Execute `python VERIFY.py` in a directory containing `VERIFY.py`. Only the Python standard library is required; the program uses reproducible pseudorandom inputs and checks independently of the prose proof.

The executed package tests every edge-sign configuration in dimensions \(2\) through \(10\), including the integer identity for the norm of the signed incidence transpose, the inner-product identity at each cut and the resulting sharp formula. It also checks explicit norming vectors for dimensions \(2\) through \(100\), tests \(7{,}540\) ordinary two-input inequalities, and numerically approaches the boundary derivative at three positive thresholds through dimension \(100\).

The recorded pass lines were:

```
EXACT_SIGN_CHAMBER_FORMULA_DEPTHS_2_TO_10_PASS 8194
EXPLICIT_BOUNDARY_WITNESSES_DEPTHS_2_TO_100_PASS
RANDOM_TWO_INPUT_BV_BOUND_CHECKS_PASS 7540
BOUNDARY_APPROACH_ALL_DIMENSIONS_2_TO_100_PASS
ALL_CENTERED_GROUP_SHRINK_CHECKS_PASS
```

These checks establish finite arithmetic facts and test floating-point behavior only. The unlimited-dimension inequality, strict nonattainment assertion and parameter discontinuity are proved symbolically in `RESULT.md`; they are not inferred from samples or a finite search. Independently validated results have not been claimed.
