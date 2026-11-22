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

Run `python checker.py` with Python, NumPy and SciPy. The checker reports 2,566 passed analytic, rate-identity and Gauss–Jacobi quadrature assertions. Its quadrature checks normalize the exact one-pair spherical inner-product density and recover the Poisson-kernel first and second moments for multiple dimensions and parameters. It also verifies the squared-distance factorization, the thresholds, the constrained-rate boundary and the strict truncated second-moment inequality in representative cases.

These finite checks do **not** certify a probability limit. The mathematical verification rests on the full proof: spherical angular large deviations, pairwise independence of distinct unordered edge inner products, finite-bin concentration bounds, a constrained variational principle, tilted-measure concentration, a truncation variance estimate and exact Poisson-semigroup convolution. The results are for the normalized off-diagonal pair average and fixed positive kernel parameter. Neither the critical probability limit at the first threshold nor a distributional limit at the second threshold has been established.
