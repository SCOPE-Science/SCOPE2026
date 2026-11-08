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

# Reproduction notes

Run `python3 verify.py` in the directory containing this file and the bundled `verify.py`. The checker requires the Python standard library only. It tests five real two-eigenvalue Gaussian-sketch configurations with 40,000 draws each, checks sign equivalence and the direct scalar formulas, confirms the spectral-angle extremizer numerically against grid values, and verifies the analytic reciprocal-tail density identity for several values of \(s\) and \(\rho\). The deterministic output ends with `VERIFY_OK`.

The simulations do not prove any tail, infinite-mean, all-matrix, or asymptotic statement. Those assertions follow from the complete Gaussian regression, beta, spectral inequality, and density-at-zero arguments in `RESULT.md`. All calculations and probabilities concern exact-arithmetic random variables. The original source's condition that a sketch satisfy a suitable embedding inequality is not conditioned on here.

No independent mathematical audit or external validation has been performed.
