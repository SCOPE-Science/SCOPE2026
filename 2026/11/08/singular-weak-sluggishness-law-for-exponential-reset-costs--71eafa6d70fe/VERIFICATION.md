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

# Verification details

Run `python verify.py` using Python 3 with NumPy and SciPy. This standalone script evaluates the stationary density from the Bessel formula without using the derived critical or saddle approximations as its integrand. It checks normalizations at several reset rates and sluggishness exponents, the exactly soluble Brownian limit, subcritical convergence, critical logarithmically slow convergence, and the supercritical full-prefactor ratio. It separately evaluates the derivative, height and curvature of the saddle expression. The expected output begins `PASS: 72 deterministic normalization, asymptotic and saddle checks` and prints representative ratios.

The critical ratios at positive sluggishness are above one and approach one slowly; their finite-size deviation does not weaken or establish the analytic limiting constant. The supercritical full equivalent already gives ratios close to one at moderate positive exponents. The proof in `RESULT.md` provides the quantified all-parameter assertion. No theorem about simultaneous vanishing of the cost contrast and sluggishness is asserted. No independent audit is recorded.
