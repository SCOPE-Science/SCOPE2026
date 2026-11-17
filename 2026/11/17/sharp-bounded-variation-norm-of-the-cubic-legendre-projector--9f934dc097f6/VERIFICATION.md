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

# Reproducible mathematical verification

Run `python3 check_legendre.py` using Python 3 and the standard library. No network connection, external theorem prover, precomputed data file or optional package is required.

The checker first expands normalized Legendre polynomials through degree four and compares every coefficient of the step-derivative kernel. It next verifies the eight *exact rational* Bernstein coefficients of the polynomial positivity certificate on `0 <= u <= 1/16`. Lastly it divides the remaining continuous jump-position range into 300 intervals: a universal analytic derivative estimate bridges each interval, and exact rational root brackets and primitive integrations bound the absolute quadratic integral at every center. It checks each exact inequality against `17/10`. This establishes the upper bound on the continuous family, not merely on a numerical sample.

Expected final message: `CUBIC_LEGENDRE_VARIATION_PROJECTION_ALL_CHECKS_PASS`. The maximum center-bound reported is approximately `1.683714543511447`, strictly below `17/10`. Floating-point printing of that approximation is informational only; all proof decisions use integers and rational numbers.

The mathematical derivation of the distributional BV jump decomposition and coefficient normalization is in `RESULT.md`. The sharp midpoint value is an elementary exact integral and is independently inspectable by hand. The limits of the result are stated in `RESULT.md` and `REVIEW.md`. No external independent audit has been conducted.
