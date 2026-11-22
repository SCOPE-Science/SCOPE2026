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

The proof establishes an exact Beta probability by an exponential-spacing integral and a conditional Gamma limit by an explicitly normalized density and conditional concentration of the Gamma denominator. It does not rely on finite simulation for the limiting theorem.

The standalone `check.py` uses only the Python standard library. The command `python check.py` checks exact rational equality for sample sizes 1 through 40, numerical quadrature, finite conditional-density positivity, asymptotic normalization, and seeded Monte Carlo agreement. The checks cannot certify all infinite cases, external novelty, or independent validation.
