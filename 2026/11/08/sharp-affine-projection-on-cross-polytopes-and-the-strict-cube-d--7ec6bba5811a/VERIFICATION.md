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

# Verification and reproduction

Run `python3 check_crosspoly.py` with Python 3 standard-library arithmetic. The program independently integrates the cross-polytope beta-coordinate density as a finite rational polynomial, verifies covariance and the claimed closed form for dimensions \(1\) through \(63\), and computes exact cube norms using the Irwin--Hall cumulative distribution. It checks cross-polytope/cube equality in dimensions \(1,2\), strict cross-polytope dominance in dimensions \(3\) through \(8\), and monotonicity and positivity identities over the tested dimensions.

Observed terminal lines include:

```
CROSS_POLYTOPE_BETA_AND_MONOTONICITY_IDENTITIES_PASSED 63 DIMENSIONS
CUBE_CROSSPOLYTOPE_EXACT_LOW_DIMENSION_GAPS_PASSED
ALL_CROSSPOLY_AFFINE_CHECKS_PASSED
```

The infinite statements are proved in RESULT.md using a convexity argument, a beta integral, a strict derivative inequality, the Cauchy--Schwarz inequality for dimensions at least eight, and finite exact rational base cases. The reproducibility program provides independent finite diagnostics, not an infinite formal certificate. Independent mathematical audit has not been performed.
