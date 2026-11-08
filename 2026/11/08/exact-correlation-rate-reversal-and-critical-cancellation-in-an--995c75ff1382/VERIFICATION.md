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

# Reproducibility and scope

Run `python checker.py` using Python 3 and `mpmath`. It performs 96 direct checks of the stationary covariance against an independently integrated Gaussian expression, the correlation-rate derivative identity, the short-lag diffusion normalization, the unique tilted-mean threshold, the strict tilted-variance identity, and the critical \(e^{-2\mu t}\) correction. The observed output was:

```
PASS 96 independent quadrature, derivative, sign, root, and critical asymptotic checks
```

The analytical proof in `RESULT.md` is necessary for global uniqueness and asymptotic validity. Quadrature tolerances account for finite-precision tail integration; no finite grid is treated as an exhaustive test. The model requires \(\kappa>2D_K/\mu^2\), \(\mu,D,D_K>0\), independent Brownian noises, and a stationary OU stiffness. At the exact phase boundary, the order \(e^{-\mu t}\) coefficient vanishes and the positive order \(e^{-2\mu t}\) coefficient follows from the derivative of the tilted mean. This is a self-review only. No independent validation has been performed.
