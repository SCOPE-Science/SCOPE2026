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

# Verification evidence and limitations

The executable `verify.py` was run from the supplied package directory with NumPy and SciPy available. It reported:

```
JACOBIAN_FINITE_DIFFERENCES_OK
NORMALIZATION_MOMENT_HYPERBOLIC_TAIL_OK
CARTESIAN_MOBIUS_INVERSION_AND_POISSON_PHASE_OK sample_size 120000 ks_distance 0.003308 sample_mean_squared_radius 0.407965
IDEAL_HYPERBOLIC_INCENTER_CHECKS_OK
```

The Jacobian test differentiates the boundary-vertex map by independent centered finite differences, comparing the resulting numerical determinant with the claimed analytic expression. Numerical quadrature checks the incenter density normalization, its mean squared radius and the exponential radial tail. The direct sampler draws 120,000 triples of independent uniform boundary angles, then reconstructs the center as the image of zero under the unique fractional-linear map matching the ordered cubic roots of unity to the sampled triple; this numerical reconstruction does not use the proved density. The sampler checks four CDF values, an empirical Kolmogorov–Smirnov distance and a conditional angular Fourier coefficient.

The symbolic proof in `RESULT.md`, not these finite experiments, establishes the distributional statements. The experiments are only reproducibility and diagnostic checks; no external independent audit or formal certification was performed.
