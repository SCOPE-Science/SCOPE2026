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

# Reproducibility and proof boundaries

The proof appears in `RESULT.md`. Run `python check.py` using Python 3; no external dependencies are required. The executable independently evaluates symmetric finite differences of the logarithmic Laplace transform at high decimal precision, compares them with the displayed mean and variance, and checks optimizer roots, optimal-variance identity, comparison with complete resetting, and small/large threshold asymptotics. Expected output begins `PASS 549`.

The derivation of the inverse-local-time Laplace transform uses strong Markov regeneration at the reflecting boundary and the stated normalization of the reflection regulator. Global uniqueness, monotonicity, convexity, and strict variance deficit are analytic; finite numerical checks do not certify infinite parameter ranges. The previously known position-only mean and full inverse-local-time transform are cited, rather than claimed as new. External independent audit and finite-sample physical validation are not performed.
