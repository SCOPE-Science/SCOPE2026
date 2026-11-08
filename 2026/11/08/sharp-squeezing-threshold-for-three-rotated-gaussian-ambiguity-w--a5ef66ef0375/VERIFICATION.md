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

# Verification of the analytical calculation

The mathematical proof is in RESULT.md. The included executable `check_three_gaussians.py` uses Python, NumPy, SciPy and SymPy. Its output from an actual local replay is:

`THREE_GAUSSIAN_DISK_MINIMAX_CHECKS_PASS 99`

The checker verifies the exact second derivative of the threshold inequality, tests numerical optimization against a dense squeeze grid for eleven disk parameters, compares the closed angular margin with 4,001 angular samples at each of fifty-five parameter combinations, tests unequal allocations and checks both endpoint asymptotic regimes.

A finite angular grid cannot certify a universal minimum, and numerical agreement cannot establish global uniqueness. Those statements follow instead from the divided-difference sign and the scalar inequality in RESULT.md. The critical radius and the large-radius limit depend on unit-norm Gaussian normalization and the squared ambiguity (rather than the unsquared sum used in some STFT reconstructions). No independent mathematical audit has been performed.
