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

The analytical proof in `RESULT.md` establishes strict positive definiteness, the exact Cramer formulas, outer-weight positivity by Chebyshev covariance and a positive hyperbolic-cosine term, positivity of the collision coefficient, and every limit by Taylor expansion. Computation is not the source of any universally quantified assertion.

Run `python verify.py` with the versions compatible with `requirements.txt`. It uses `sympy` for exact identities and `mpmath` at 110-digit working precision for independently solved three-by-three systems. The completed run printed:

```
PASS: symbolic Gramian identities and Taylor coefficients
PASS: mixture covariance and Matérn 5/2 direct-solve, sign, and asymptotic comparisons
finite parameter groups: 112
Matérn example: lambda=1, d=0.1
critical noise variance = 0.000216563659988181958701881804242
noiseless central weight = -5.52826600287479720290024347609
```

The finite tests include a two-Gaussian mixture with a three-point discrete target, four Matérn inverse lengthscales, finite noise values on both sides of the sign threshold, exactly zero middle weights at the threshold, and several coalescing spacings. Discrete tests are not an exhaustive numerical certificate for arbitrary probability distributions. Computing the symbolic coefficient does not certify a literature novelty claim; the source comparisons and residual priority risks are recorded separately.
