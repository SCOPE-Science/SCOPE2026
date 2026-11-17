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

# Numerical and analytic verification

The accompanying `check.py` evaluates the two-dimensional integral for the rare-perimeter normalization by two Gauss–Legendre resolutions and checks the analytic gamma expression. An independent direct simulation of 8,000,000 spherical triples at three decreasing thresholds tests the square-root probability coefficient, mean first side, and normalized deficit mean and CDF. All tolerances passed.

At \(\varepsilon=0.006\), among 150,728 rare configurations, the empirical coefficient was 0.243236 (limit 0.242333), the first-side mean 2.093546 (limit \(2\pi/3=2.094395\)), the mean normalized deficit 0.334425 (limit \(1/3\)), and its CDF at one-quarter was 0.498255 (limit \(1/2\)). The checker prints `SPHERICAL_TRIANGLE_MAX_PERIMETER_MARKED_LAW_OK` on success.

The proof, not these finite checks, establishes the asymptotic probability and total-variation law. The orientation choice is almost surely defined for a random ordered pair; mass near degenerate pairs is analytically controlled. The circular Dyson integral is invoked as a classical identity. Independent audit has not been performed.
