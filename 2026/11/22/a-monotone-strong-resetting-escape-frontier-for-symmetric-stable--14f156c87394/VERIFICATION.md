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

The analytic chain is: short-time stable exit intensity; Laplace asymptotic; Poisson-renewal mean; known unreset first-exit mean; Gamma-function simplification; strict monotone hyperbolic position threshold; Euler-product monotonicity in the stable index; endpoint expansions.

The standalone standard-library `checker.py` was executed and produced:

```
PASS: 6359 independent finite consistency assertions
Cauchy-frontier check: 0.771177842933
Small-index frontier limit: 0.719640870293
Analytical claims require the proof; these finite checks do not establish them.
```

Its finite tests cover numerical normalization, two-sided exit intensity, ratio identity, threshold comparisons, index ordering samples and limit benchmarks. They do **not** prove the infinite-index statements; those require the argument in RESULT.md. The strong-reset mean and free exit-time mean are separately attributed to the cited literature. The finite-reset sign at equality, all-rate global benefit, noisy data, and independent expert validation are unproved.
