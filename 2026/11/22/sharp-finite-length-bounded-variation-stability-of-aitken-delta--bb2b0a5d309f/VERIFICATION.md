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

# Reproduction and scope

Run `python verify_aitken.py` with standard Python 3. The script is a fully standalone finite checker. Its successful output was:

```
EXACT_RATIONAL_STEP_AND_BOUNDARY_IDENTITIES_PASS 624
EXACT_HETEROGENEOUS_DERIVATIVE_STEP_BOUNDS_PASS 27000
EXACT_RATIONAL_TWO_INPUT_INEQUALITIES_PASS 2700
EXACT_NEAR_SHARPNESS_PERTURBATIONS_PASS 24
ALL_SLIDING_AITKEN_VARIATION_CHECKS_PASS
```

The tests use exact `fractions.Fraction` rational arithmetic with six ratio caps and multiple finite sample sizes. The last batch checks admissibility of actual perturbed signals and checks close approach to the claimed constants. The proof in `RESULT.md` separately establishes general validity for every real ratio cap in \((0,1)\), every integer length at least three, and all admissible real input pairs. Finite tests cannot establish the universal theorem on their own.

The comparison literature concerns sequence acceleration, numerical cancellation, and noisy extrapolation. No external independent audit or formal machine certification is claimed.
