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

# Verification

The complete proof is in `RESULT.md`. It establishes a strict derivative coefficient sign pattern analytically for every \(n\ge2\), applies Descartes' rule to count all critical points, derives the sharp BV operator norm from nodal-step decomposition, and proves the boundary limit using compact-uniform binomial-to-Poisson convergence of both a polynomial and its derivative.

`check_boolean.py` requires Python 3 and no third-party packages. Run `python check_boolean.py` to check exact rational coefficients and signs for degrees 2 through 16, low-degree formulas, numerical extrema through degree 10, and first-jump boundary scaling at degrees 20, 50, 100 and 200. Its successful final line is `ALL_BERNSTEIN_BOOLEAN_SUM_CHECKS_PASS`.

These computations are finite and do not certify an all-degree theorem independently. The sharp global BV asymptotic is unproved, and early original sources from 1984 and 1994 were not fully accessible for historical-priority comparison. Independent mathematical audit remains unperformed.
