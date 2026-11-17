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

Run `python check_cusp_distance.py` with `mpmath>=1.3.0` installed. The program, read and executed from the included path, independently samples 630,000 pairs by normalized hyperbolic area and computes each shortest path from actual upper-half-plane coordinate differences and horizontal deck translates. Twelve Monte Carlo comparisons use the analytic survival integral at several non-asymptotic thresholds; nine separate deterministic quadrature comparisons test the sharp tail coefficient at large thresholds. The checks of the product-survival integration are exact algebraic identities evaluated at representative parameter values.

Observed coefficient ratios at threshold \(r=5\): \(1.00005448315\) for boundary length \(\lambda=1\) and \(1.00012714232\) for \(\lambda=3\). Successful execution ends `HYPERBOLIC_CUSP_DISTANCE_LAW_OK`.

The proof itself is analytical and covers every strictly positive real horocycle length and every nonnegative threshold. The numerical checks are neither exhaustive nor an independent audit. The error estimate is for each fixed cusp, not uniformly over changing lengths.
