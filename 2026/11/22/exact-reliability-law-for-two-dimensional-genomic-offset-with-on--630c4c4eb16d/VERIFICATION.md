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

# Verification and reproducibility

`verification/check.py` is a standalone Python 3 standard-library checker. Run it from the parent directory containing `RESULT.md` using `python verification/check.py`.

It checks the original covariance-projection expression independently of the transformed Cauchy expression, exact cases at \(\kappa=1,4\), the analytic mean against independent angular Simpson integration for six ratios, the median and CDF endpoints, and three seeded Gaussian ensembles of 60,000 architectures each. Its output should be `PASS: 6 angular integrations, exact cases and 3 seeded Gaussian samples.`

These numerical tests are finite and cannot establish probability-law identities for all admissible parameters. The rigorous proof is in `RESULT.md`: the exact Gaussian covariance reduction, Cauchy-ratio CDF inversion, angular integrals, positive derivative factorization, and asymptotic expansions are the mathematical certificate. The title and claim concern predictive correlation of the *conditional mean negative log-relative fitness*, not the residual fitness outcomes. No external or independent validation has occurred.
