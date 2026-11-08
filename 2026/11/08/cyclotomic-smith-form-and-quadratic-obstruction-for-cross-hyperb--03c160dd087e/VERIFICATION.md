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

# Finite checks and their limits

Run `python verification/check_hyperbola.py` from the directory containing this document; the script uses only the Python 3 standard library. Its successful output begins `CROSS_HYPERBOLA_LOCAL_SMITH_PASS`.

For each prime \(p\in\{3,5,7,11,13,17,19,23,29,31\}\), the checker evaluates both a square and a nonsquare parameter \(c\). For every multiplicative exponent \(r\), it calculates the reductions modulo \(p\) of all cyclotomic-binomial coefficients through the first predicted nonzero degree, checking the zero coefficients at smaller degrees. It verifies exact coefficient-vector cancellation in the nonsquare quadratic case using integer arithmetic. Independently, it constructs the complex cross-Fourier matrix, performs Gaussian elimination and checks the predicted rank and quadratic-character null vector. Numerical rank tests use tolerance \(10^{-7}\); exact symbolic coefficient checks and the full algebraic proof do not depend on numerical tolerances.

The proof in `RESULT.md`, not the finite enumeration, establishes the theorem for all odd primes. Neither the finite checker nor this document represents independent mathematical validation.
