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

# Reproduction notes

Execute `python check.py` in a directory containing the accompanying standalone file with SymPy installed. The result of the recorded execution was:

```
VERIFY_OK symbolic_identities=14 exact_rational_cycles=50 critical_parameters=2 inverse_lift_search=255 area=0.013313899426
```

The checker reconstructs the two exact affine orbit equations for both possible integer lifts, confirms the slope-product threshold, simplifies the two critical parameters, checks the first-order tongue opening and exactly integrates the combined area. An independent integer-lift search at 255 rational parameter points corroborates the absence of omitted regular mixed cycles, and fifty rational tests use the original affine branch formulas and integer modular reductions with exact fractions. This is corroboration, not a numerical proof of an infinite statement: exhaustive classification rests on the integer-difference inequality and parameter interval proof in `RESULT.md`. The code does not test breakpoint cycles, other orbit periods, global attraction, or historical priority.
