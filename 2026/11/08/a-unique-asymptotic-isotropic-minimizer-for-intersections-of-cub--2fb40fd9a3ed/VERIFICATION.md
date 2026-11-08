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

# Computational and analytic verification

Run `python3 CHECK.py` using Python 3 standard library. It checks the volume and second-coordinate moment identities by two independent exact rational integration methods across 153 positive-volume choices in dimensions 2--10. It checks 101 series derivative coefficients, including the negative tail onset, and the analytical derivative factorization at 12 high-precision parameter points. Finally it solves the defining sign equation by Decimal bisection to 65-digit precision and verifies that the minimum lies below both endpoint values.

Actual successful run marker:

`CLIPPED_CUBE_UNIQUE_MIN_CHECKS_PASSED 153 exact rational volume/moment tests; 101 derivative signs; 12 derivative factorizations`

These computations check formulas and constants. The analytic series-sign proof is required for uniqueness on the entire positive half-line; finite tests do not establish an infinite statement. The local central limit theorem supplies the remaining dimension-limit step. Independent mathematical audit has not been performed.
