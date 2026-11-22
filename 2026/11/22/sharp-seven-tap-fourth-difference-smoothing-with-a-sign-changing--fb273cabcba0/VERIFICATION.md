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

# Reproduction of the exact arithmetic tests

From a directory containing `checker.py`, run `python checker.py` under Python 3.10 or later. The script uses only `fractions.Fraction` and `decimal` from the standard library; every assertion is an exact rational comparison.

The script checks a four-node interpolation identity annihilating all three variable polynomial terms; it isolates the three distinct stationary roots of a rational near-extremizer with disjoint width-\(10^{-12}\) rational intervals; it gives exact Taylor enclosures for the extrema of that polynomial; and it produces a rigorous two-sided interval for the sharp real minimax norm. Crucially, the exact lower bound holds for *all* eligible polynomials, not just the test polynomial. The proximity of the test upper bound to this lower bound and a dual-interpolation stability calculation bound the actual (analytically existing and unique) optimizer's coefficients, proving strictly positive tap weights and a strictly negative value of its Fourier symbol.

Expected printed interval for the optimal convolution-difference norm: strictly between \(0.2029850838641552356566\) and \(0.2029850838641552387172\). Numerical root estimates are not taken as an exact algebraic solution; analytic equioscillation establishes existence and uniqueness. No independent audit or higher-radius certification is claimed.
