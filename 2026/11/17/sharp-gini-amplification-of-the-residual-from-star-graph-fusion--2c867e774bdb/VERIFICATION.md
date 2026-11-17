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

# Reproducibility and verification

Run `python3 check_star_residual.py` from the directory containing the embedded script. Only the Python standard library is required. The package's script was executed on its actual path with the following output:

```
EXACT_ALL_BLOCK_BINARY_CUTS_AND_OPTIMAL_INTEGER_SIZES_PASSED 6477
EXACT_STRICT_COMPLEMENTARITY_SHARP_TWO_INPUT_WITNESSES_PASSED
EXACT_RANDOM_ACTUAL_NONLINEAR_TWO_INPUT_CHECKS_PASSED 1500
SHARP_FIRST_AMPLIFICATION_DIMENSION_FOUR_PASSED
ALL_STAR_FUSION_RESIDUAL_CHECKS_PASSED
```

The first test considers every binary cut count for each permissible pooled block of sizes two through the current dimension, for all dimensions from two through 18, and verifies the closed formula exactly with rational arithmetic. The second tests actual data perturbations, using a separate exact solution of the star proximal KKT equation. The third checks 1500 arbitrary exact-rational pairs with varied positive penalties; these are diagnostics and do not prove the uniform theorem. Infinite-dimensional or unrestricted finite-dimensional claims come only from the mathematical proof in `RESULT.md`. No external validation or independent certification is asserted.
