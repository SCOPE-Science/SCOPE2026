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
# Verification notes

The proof uses independent panel variance, an explicitly bounded symmetric Taylor remainder, harmonic/power-sum comparisons, the strict rearrangement inequality, and a uniform \(C^2\) remainder for the smooth limit. These are analytic arguments valid for the ranges stated in RESULT.md; finite testing is not an infinite proof.

The standalone file `verify.py` was run from the same package and printed:

```
PASS: 552 exact-rational/deterministic assertions.
Exact cases: beta=0,1,2,3; finite-n formulas for beta=2,3;
large-cell power asymptotics, beta=5/4,3/2,7/4,2,3.
```

The integer-power tests use rational arithmetic for coefficients, means and variances; the large-cell constants are independently estimated by deterministic centered numerical integration. The latter verifies selected asymptotic coefficients, not all exponents or all finite-panel random draws.

No independent scientific audit, external reproducibility assessment, or publication-priority certification has been performed. The published source already demonstrates the scheme and empirical convergence trends; the new claim is restricted to analytic exact-variance classification and explicitly stated coupling conditions.
