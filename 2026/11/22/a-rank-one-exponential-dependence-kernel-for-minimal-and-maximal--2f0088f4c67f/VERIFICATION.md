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

# Reproducibility and limitations

`verify.py` uses only the Python 3 standard library and exact `fractions.Fraction` arithmetic. Execute `python3 verify.py` from the extracted artifact directory. It checks all ordered-graph configurations for orders 2 through 6 under two nontrivial rational edge probabilities. It reconstructs the marginal laws, the exact finite mixed covariance, and the weighted geometric sum identity. These are finite consistency checks; the bivariate asymptotic statement is established by Bernoulli interpolation and analytic localization in `RESULT.md`, not by computation. There has been no independent audit.
