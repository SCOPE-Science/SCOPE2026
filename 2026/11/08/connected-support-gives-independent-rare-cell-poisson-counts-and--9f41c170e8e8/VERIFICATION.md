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

## Reproducible finite and algebraic checks

Run `python3 verify.py` using only the Python standard library. The test script enumerates nonnegative integer tables with balanced row and column margins, computes Gibbs weights with suppressed diagonal entries, verifies the exact reweighting against conditionally independent Poisson cell weights, and checks low-order moments, connected-incidence rank, the Gaussian covariance formula, and convergence towards discrete Bessel and Poisson marginal targets. The replay passes **831 checks** under the supplied finite test cases.

These checks are **not** exhaustive over all matrix sizes, weights, or fixed margins. The general theorem is proved by an exact conditional representation, Fourier lattice local limit with a uniform bound, dominated convergence, and Gaussian completion of squares; no computational execution proves the all-parameter limit. No external or independent mathematical validation was performed.
