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

## Reproducible finite checks

Run `python verify.py` with NumPy and SciPy installed. The script independently constructs the generator of the resetting Brownian driver on polynomials through degree four and evaluates four ordered moments by matrix exponentiation. It separately computes telegraph moments from the two-state transition matrix and subtracts the three stationary covariance pairings. All 432 cross-parameter/time cases pass the stated formulas and sign tests; a discrete quadrature check confirms the filtered-sign prediction on one collection of four unequal positive exponential response functions.

## Analytical basis and limitations

The proof in `RESULT.md`, not the finite test grid, supports the assertions for all continuous time gaps and parameters. No independent audit or external mathematical certification has been performed. Experimental observability, arbitrary sign-changing response kernels and all other nonlinear stochastic forcing classes are outside this result.
