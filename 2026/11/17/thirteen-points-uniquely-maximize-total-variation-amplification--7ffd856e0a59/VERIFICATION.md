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

Execute `python3 verify.py` in the same directory. The script depends only on Python 3's standard library and uses integer and `fractions.Fraction` arithmetic for every strict inequality. It prints:

```
LEAST_SQUARES_MOMENTS_AND_GRAM_COFACTOR_PASS 29
EXACT_ALL_WINDOWS_5_TO_3999_UNIQUE_13_POINT_MAX_PASS 1998
RATIONAL_CONTINUUM_ROOT_ENCLOSURES_AND_GAIN_BOUND_PASS 1.504163623348879
EXACT_INFINITE_TAIL_POSITIVE_GAP_PASS
EXACT_JUMP_SIGNAL_ATTAINS_EVERY_SHARP_KERNEL_GAIN_PASS
ALL_QUARTIC_SAVITZKY_GOLAY_VARIATION_CHECKS_PASS 3763/2431
```

The continuum decimal in this log is a rounded display of a fraction used solely for verification. Exact mathematical comparisons use rational arithmetic. The checker tests finite coefficient reconstruction and the finite portion of the global maximum; for arbitrarily large radii it checks the critical uniform estimates. The analytical inequalities in `RESULT.md` are essential to conclude the all-radius theorem and must not be replaced by finite enumeration.

Independent audit is not performed; there is no external certification or additional verification claim.
