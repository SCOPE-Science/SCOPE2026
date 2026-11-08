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

# Reproducible checks and evidentiary limits

The analytic proof consists of the Dirichlet covariance calculation, a strict vertex reduction, truncated beta integration, a conditional-Jensen comparison of normalized Beta variables, a fractional-moment boundary argument, and a beta central limit theorem with second-moment uniform integrability.

Run `python verify.py` with Python 3 using only its standard library. Expected markers:

```
EXACT_BETA_INTEGRAL_AND_STRICT_ORDER_OK 275
EXACT_DIRICHLET_AFFINE_REPRODUCTION_OK 5
UNIFORM_SIMPLEX_RECOVERY_OK 12
ALL_DIRICHLET_AFFINE_CHECKS_OK
```

The script independently evaluates the beta negative part by binomial-tail probabilities and direct rational polynomial integration, tests the parameter ordering across integer totals, checks the reproducing identity on heterogeneous Dirichlet parameter lists, and recovers the uniform-volume benchmark. This is finite exact corroboration; it is not an exhaustive check of arbitrary real parameters or the Gaussian limit. No external mathematical audit has been performed.
