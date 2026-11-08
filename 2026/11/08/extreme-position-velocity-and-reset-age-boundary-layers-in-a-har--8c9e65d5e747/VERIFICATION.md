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

# Verification and limits

The analytic claim follows from a last-reset regenerative decomposition, explicit Gaussian stochastic integrals, the positional exponential-tail result in arXiv:2306.09453, a Laplace saddle for the large conditional age, a short-age density change of variables, and the stationary no-position-jump flux identity. These proof ingredients must be checked together; the numerical tests are neither exhaustive nor substitutes for the large-position limit.

Run `python check_science.py` using Python with NumPy and SciPy. The checker integrates the covariance kernels independently, evaluates saddle-density and conditional Gaussian integrals for three parameter sets, and verifies the algebraic cancellation coefficient. Rare young-reset paths are assessed analytically because direct Monte Carlo would undersample them severely. The checker does not claim an independent proof of convergence or measure completeness.

The prior paper's exponential positional tail and the limiting weak velocity law do not by themselves imply convergence of conditional velocity means. The separate rare-age analysis and exact continuity-equation argument are required. No independent scientific audit is asserted.
