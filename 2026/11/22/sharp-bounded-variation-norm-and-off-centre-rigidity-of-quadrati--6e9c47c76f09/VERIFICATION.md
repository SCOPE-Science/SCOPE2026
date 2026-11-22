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

From the package directory, run `python3 verify_jacobi_bv.py` (Python standard library only). This checker reconstructs integer-shape Jacobi moments exactly using rational arithmetic, recomputes the jump-response derivative, numerically integrates its variation independently of the piecewise closed formula, compares optimizing roots over a range of Jacobi shapes, samples signed Stieltjes step combinations, and checks large- and small-shape limits.

Observed output:

```text
EXACT_JACOBI_MOMENTS_AND_STEP_DERIVATIVE_PASS
TWO_ROOT_GLOBAL_MAXIMUM_ALL_TEST_PARAMETERS_PASS
DIRECT_INDEPENDENT_VARIATION_INTEGRATION_PASS
RANDOM_SIGNED_STIELTJES_BV_CONTRACTION_PASS 7500
BETA_ENDPOINT_AND_GAUSSIAN_WEIGHT_LIMITS_PASS
ALL_QUADRATIC_JACOBI_BV_CHECKS_PASS
```

The critical infinite-parameter, all-BV and uniqueness claims are derived analytically in RESULT.md; finite sampling and numerical quadrature alone could not certify them. No independent mathematical audit was conducted. The available comparison literature does not establish exhaustive historical priority.
