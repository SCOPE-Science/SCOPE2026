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

## Reproducible verification

Run `python3 verify.py` with Python 3.10 or newer and no additional dependencies. The recorded result from the included code was:

```
VERIFY_OK: 9685 exact rational and exhaustive/sampled assertions; all true
```

The checker verifies exact shifted-Laplacian inverses in hypercube dimensions one through four for three positive rational shifts; exact Fourier-level degeneracies, strict ordering, and variance identities; all colorings in dimensions at most three; deterministic samples of colorings in dimension four; a two-atom positive heat mixture; and full outcome enumeration of the three-cube estimator for parity and a nonuniform partition. All essential computations are carried out with `fractions.Fraction` and integer operations, without floating-point tolerances.

## Analytic versus computational scope

The proof in `RESULT.md`, not the finite tests, establishes the theorem for every integer dimension and every finite positive mixing measure with nonzero positive-time mass. The code does not certify claims for arbitrary dimensions or arbitrary measures by enumeration. The proof requires exactly the standard Rademacher variance identity, the coordinate-product heat kernel, Tonelli/Fubini for finite measures, Walsh orthogonality, and the strict positivity of the spectral-order integrand for positive times.

Independent validation has not been performed.
