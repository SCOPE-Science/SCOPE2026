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

Run `python check_weighted_lse.py` with standard Python 3. The program constructs log-sum-exp by shifted exponentials, computes its exact analytic Jacobian in floating arithmetic, evaluates step-column operator norms, checks random real finite-pair inequalities, checks concentrated near-extremal profiles and finite equality pairs. Its output was:

```
FINITE_JACOBIAN_AND_TWO_INPUT_CHECKS_PASS 9800
SHARPNESS_AND_TEMPERATURE_TESTS_PASS 48
FINITE_NONEXPANSIVE_EQUALITY_CHECKS_PASS 12
ALL_WEIGHTED_LOGSUMEXP_VARIATION_CHECKS_PASS
```

These checks are finite corroboration only. The rigorous universal bound, sharpness and nonattainment are proved algebraically in `RESULT.md`. Python floating-point tolerances are explicitly used, not presented as exact-rational certificates. The theorem does not claim any independent external audit or publication priority certification.
