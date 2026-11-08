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

# Reproducible self-review

The file `CHECK.py` runs under Python 3 with no optional libraries. Run it next to the other files using `python CHECK.py`. Its sparse multivariate polynomial verifier uses exact rational arithmetic, establishing the identities needed for differentiation and rational factorization without floating-point assumptions. It additionally tests published example parameters, the exact local-maxima/coexistence separation, and both tricritical limiting laws numerically. These finite numerical diagnostics do not establish a universal theorem; the analytic positivity and root-count arguments are in `RESULT.md`.

The underlying stochastic diffusion formula and wall-motion idealizations are taken from Pietrangeli et al. (2024). This package verifies consequences of that formula, not the stochastic homogenization derivation. No independent scientific audit or independent validation has been performed.
