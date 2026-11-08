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

Run `python checker.py` with Python 3 and installed NumPy and SciPy. The checker evaluates the exact formula at deterministic and exponential clocks, verifies a two-point family approaching the sharp upper endpoint, checks Cauchy–Schwarz moment bounds for 10,000 random four-point laws, tests 120 exact reset-age cancellations at finite population sizes, and performs 8,000-draw finite-population top-gap simulations for each of the deterministic-age and exponential-age cases. It reports the empirical correlations and theoretical limiting values.

The exact theorem is proven analytically in RESULT.md using equilibrium-renewal age calculus, Gaussian extreme-spacing asymptotics with uniform-integrability control, and strict Cauchy–Schwarz with a two-point attainment construction. The finite tests do not establish any infinite-sample limit or the exhaustive range by themselves.

Scientific scope is fixed distinct right-edge ranks in the equilibrium-renewal stationary ensemble with positive finite-second-moment reset intervals. No independent audit or external certification is represented here.
