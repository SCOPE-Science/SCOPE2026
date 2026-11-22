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

# Mathematical verification

Run `python checker.py` with Python 3, SymPy, NumPy, and SciPy. The script reconstructs the exact stationary moment balances, the four-dimensional forward Markov hierarchy, the opposite-time first-moment transform, and the symbolic four-pole difference with zero thermal-noise dependence. It also checks the first three time derivatives and independently compares six finite-dimensional full moment generators against a positive convolution cascade for six parameter regimes at eight lags, including coincident exponent rates and large thermal noise.

The verified run reports `PASS 100 independent symbolic/semigroup checks`. These finite tests corroborate, but cannot prove, infinite-parameter sign strictness; the algebraic resolvent identity and positivity of the convolution kernel give the analytic proof. Independent scientific audit has not been performed.
