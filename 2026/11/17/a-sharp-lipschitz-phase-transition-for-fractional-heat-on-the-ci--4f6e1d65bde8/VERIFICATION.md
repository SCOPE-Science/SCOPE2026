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

# Reproducibility and limits

Run `python check.py` with the Python `mpmath` package. The checker compares the heat Fourier half-circle profile against independent periodized-Gaussian quadrature, verifies the \(\alpha=1/2\) exact Poisson arctangent profile, tests the positivity of the explicitly normalized gamma--Dirichlet-beta jump slopes, and confirms the Gaussian endpoint's sharp small-time coefficient at several strictly positive times. The checks completed with the output:

```
GAUSSIAN_PERIODIZATION_VERSUS_FOURIER_PASS
POISSON_CLOSED_FORM_VERSUS_FOURIER_PASS
FRACTIONAL_MONOTONICITY_RANGES_AND_POSITIVE_JUMP_SLOPES_PASS
POISSON_SHARP_INITIAL_SLOPE_PASS
GAUSSIAN_SUPERALGEBRAIC_BOUNDARY_PROFILE_PASS
ALL_FRACTIONAL_CIRCLE_CHECKS_PASS
```

The proof requires: the mean-zero derivative representation of periodic Lipschitz functions; the Jacobi product for strict heat-kernel radial monotonicity; positive stable subordination; the correctly normalized torus fractional-Laplacian kernel; and the small-time Lévy jump law for sets separated from the starting point. These are described and applied in `RESULT.md`. Numerical agreement is not a proof for every exponent or time. No independent review was carried out.
