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

# Verification record

The closed-form multiplier is obtained by applying Plancherel to the frequency-unbounded short-time Fourier strip. Differentiation reduces every stationary point to the equation of a single hyperbolic function. The partial-fraction expansion of the hyperbolic cotangent gives strict one-hump control. A two-case inequality controls the centered branch, and the envelope theorem proves that the outer maximum and the central maximum cross exactly once. These are analytic, infinite-parameter arguments and not deductions from numerical scans.

The standalone `checker.py` reproduces exact Taylor coefficients, verifies five distinct first-order transition roots and corresponding strict negative slopes, and checks the square-root and quartic-root asymptotic formulas in two sample parameter regimes. It requires Python 3, NumPy, SciPy and SymPy; invoke `python checker.py` after extracting the source into the same folder. Its finite checks do not certify every continuous parameter. No independent audit has been performed.
