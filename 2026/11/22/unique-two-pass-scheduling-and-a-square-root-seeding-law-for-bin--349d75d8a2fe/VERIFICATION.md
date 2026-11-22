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

# Computational verification and limitations

`check.py` checks the exact finite-size path-divergence identity by direct summation over Markov strings and Bernoulli reveal masks for all lengths 2 through 6 and several parameter pairs. It checks the derivative of the explicit positive power-series expression by centered differences and confirms strictly positive curvature and an interior root at sampled parameters. It also checks approach to the square-root asymptotic at three small domain-wall probabilities.

Run `python check.py` from the extracted package directory; it requires Python 3, NumPy, and SciPy. The mathematical assertions for every correlation, infinitely long chains, and the limiting singular regime are proved in RESULT.md by exact entropy identities, positivity of power-series coefficients and uniform asymptotic expansion. Numeric tests are consistency checks and do not independently prove those infinite statements.

Independent audit: not performed. The priority comparison is limited to the identified primary papers, accessible historical claim material and targeted publication searches; a hidden implicit equivalent remains possible.
