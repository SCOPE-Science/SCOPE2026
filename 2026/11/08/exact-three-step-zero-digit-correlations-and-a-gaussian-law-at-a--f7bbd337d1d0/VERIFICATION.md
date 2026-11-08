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

# Reproducibility and verification

The supplied `check_golden_covariance.py` rebuilds the seven interval images directly from the affine branches and their exact algebraic endpoints, checks every row of the seven-state transition matrix, verifies reflection lumpability into four states, tests the invariant state law, verifies the characteristic polynomial and exact first-lag correlations, and checks the covariance recurrence at twelve more lags. It independently computes the asymptotic variance via geometric-series summation and the centered matrix resolvent.

Environment: Python 3 with SymPy. Run `python check_golden_covariance.py` from this directory. Successful execution prints `GOLDEN_ENDPOINT_MARKOV_COVARIANCE_EXACT_OK full_cells=7 lumped=4 lags=16`.

The checker uses exact algebraic arithmetic and supports the calculations; the general covariance recurrence is proved by the spectral identity, and the Gaussian law uses the standard martingale central limit theorem. The program is not an independent audit and does not test every possible initial point, parameter or infinite sequence.
